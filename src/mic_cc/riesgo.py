"""Riesgo cambiario: VaR historico, Expected Shortfall, backtesting y normalidad.

Sin dependencia de scipy: las CDF chi-cuadrado con 1 y 2 grados de libertad
tienen forma cerrada.
"""
from __future__ import annotations
import math
import numpy as np
import pandas as pd


def var_historico(retornos: pd.Series, nivel_confianza: float = 0.95) -> float:
    """Percentil empirico de la cola izquierda. No asume ninguna distribucion."""
    return float(np.percentile(retornos.dropna(), 100 * (1 - nivel_confianza)))


def expected_shortfall(retornos: pd.Series, nivel_confianza: float = 0.95) -> float:
    """Promedio de la cola mas alla del VaR. Medida coherente (Basilea III / FRTB)."""
    x = retornos.dropna()
    return float(x[x <= var_historico(x, nivel_confianza)].mean())


def var_multihorizonte(retornos: pd.Series, precios: pd.Series, horizontes,
                       nivel_confianza: float = 0.95) -> pd.DataFrame:
    """Cuantil EMPIRICO del retorno acumulado a T dias (metodo primario), junto al
    escalado raiz-del-tiempo (solo como referencia).

    Escalar un CUANTIL por sqrt(T) es exacto unicamente bajo retornos i.i.d. de
    distribucion estable (el caso canonico es la normal). Como Jarque-Bera
    rechaza la normalidad de esta serie, el escalado deja de estar justificado y
    se usa el cuantil empirico. Se reporta el N efectivo porque las ventanas de T
    dias se solapan y la muestra independiente real es len/T.
    """
    v1 = var_historico(retornos, nivel_confianza)
    q = 100 * (1 - nivel_confianza)
    filas = []
    for T in horizontes:
        acum = np.log(precios / precios.shift(T)).dropna()
        filas.append({'horizonte_dias': T,
                      'var_empirico': float(np.percentile(acum, q)),
                      'var_sqrt_t': v1 * np.sqrt(T),
                      'peor_observado': float(acum.min()),
                      'n_ventanas_solapadas': len(acum),
                      'n_efectivo_independiente': round(len(acum) / T, 1)})
    d = pd.DataFrame(filas)
    d['sesgo_sqrt_t_pct'] = (d['var_sqrt_t'] / d['var_empirico'] - 1) * 100
    return d


def kupiec_pof(violaciones: int, n_obs: int, tasa_esperada: float) -> tuple[float, float]:
    """Test de proporcion de fallos de Kupiec (1995).

    LR ~ chi2(1) bajo H0 de buena calibracion. CDF chi2(1) = erf(sqrt(x/2)).
    """
    if not 0 < violaciones < n_obs:
        return float('nan'), float('nan')
    pe, ph = tasa_esperada, violaciones / n_obs
    lr = -2 * ((n_obs - violaciones) * math.log(1 - pe) + violaciones * math.log(pe)
               - (n_obs - violaciones) * math.log(1 - ph) - violaciones * math.log(ph))
    return lr, 1 - math.erf(math.sqrt(max(lr, 0) / 2))


def backtest_var_oos(retornos: pd.Series, ventana: int,
                     nivel_confianza: float = 0.95) -> dict:
    """Backtest sin look-ahead: el VaR pronosticado para t usa unicamente los
    retornos de t-ventana a t-1. El `shift(1)` antes del `rolling` es lo que
    excluye el propio dia t.

    Un backtest in-sample (comparar la muestra contra su propio percentil) no
    prueba nada: por construccion arroja ~5% de violaciones sin importar la
    calidad predictiva del modelo.
    """
    q = 100 * (1 - nivel_confianza)
    pron = retornos.shift(1).rolling(ventana).apply(lambda x: np.percentile(x, q), raw=True)
    cmp_ = pd.DataFrame({'real': retornos, 'pron': pron}).dropna()
    viol = int((cmp_['real'] < cmp_['pron']).sum())
    lr, pv = kupiec_pof(viol, len(cmp_), 1 - nivel_confianza)
    return {'violaciones': viol, 'n_obs': len(cmp_),
            'tasa_observada': viol / len(cmp_), 'lr': lr, 'p_value': pv,
            'bien_calibrado': bool(pv >= 0.05)}


def jarque_bera(retornos: pd.Series) -> dict:
    """JB con los momentos POBLACIONALES (g1, g2), que es como esta definido el
    estadistico. `pandas.skew()` y `pandas.kurt()` devuelven los estimadores
    corregidos por sesgo (G1, G2), que no son los que corresponden aqui.

    Bajo H0, JB ~ chi2(2), cuya cola derecha es exp(-x/2).
    """
    x = retornos.dropna().to_numpy()
    n = len(x)
    d = x - x.mean()
    m2, m3, m4 = (d ** 2).mean(), (d ** 3).mean(), (d ** 4).mean()
    g1, g2 = m3 / m2 ** 1.5, m4 / m2 ** 2 - 3
    jb = n / 6 * (g1 ** 2 + g2 ** 2 / 4)
    return {'n': n, 'asimetria': g1, 'curtosis_exceso': g2, 'jb': jb,
            'p_value': math.exp(-jb / 2), 'normal': bool(math.exp(-jb / 2) >= 0.05)}


def nivel_desde_retorno_log(nivel_base: float, retorno_log: float) -> float:
    """Un retorno logaritmico se compone con exp(), no con (1+r).

    El modelo original usaba nivel*(1+r) sobre retornos log, lo que desplazaba el
    umbral del semaforo de riesgo en ~1% del nivel.
    """
    return nivel_base * math.exp(retorno_log)


def volatilidad_anualizada(retornos: pd.Series, dias_habiles: int = 252) -> float:
    return float(retornos.dropna().std() * np.sqrt(dias_habiles))
