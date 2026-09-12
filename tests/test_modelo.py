"""Suite de pruebas del modelo MIC-CC.

Criterio de diseno: toda prueba aqui DEBE poder fallar.

El cuaderno original reportaba "el modulo paso N verificaciones" contando
identidades algebraicas que no podian fallar: que la razon costo_60d/costo_30d
diera 2.000 exacto (la formula es lineal en dias), que la correlacion diera 1.000
(el propio comentario la predecia algebraicamente antes de medirla), o que
costo_financiero/costo_total fuera constante (lo es por construccion). Ninguna
valida nada.

Las pruebas de este archivo son de cuatro tipos:
  1. Inversion   -- resolver por un camino y verificar por otro independiente.
  2. Control     -- casos con respuesta conocida de antemano.
  3. Deteccion   -- comprobar que los detectores efectivamente detectan.
  4. Regresion   -- fijar los errores concretos hallados en la auditoria, para
                    que no puedan reaparecer.
"""
from __future__ import annotations
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from mic_cc import config, modelo, riesgo   # noqa: E402

CFG = config.PARAMS
FX_BASE = 2600.0


# ===========================================================================
# 1. INVERSION
# ===========================================================================
@pytest.mark.parametrize('pass_through', [0.0, 0.5, 1.0])
@pytest.mark.parametrize('pct_importado', [0.0, 0.30, 0.65])
@pytest.mark.parametrize('accesorios', [0.0, 0.055])
def test_breakeven_produce_margen_cero(pass_through, pct_importado, accesorios):
    """El breakeven se resuelve analiticamente; el margen se evalua numericamente.
    Son dos caminos independientes, asi que la igualdad puede romperse de verdad."""
    bk = modelo.breakeven_fx(4.25, FX_BASE, 6600, pct_importado, 900,
                             accesorios, pass_through)
    m = modelo.margen(4.25, bk, FX_BASE, 6600, pct_importado, 900,
                      accesorios, pass_through)
    assert abs(m['margen_pct']) < 1e-8


def test_breakeven_sin_solucion_devuelve_infinito():
    """Si el costo importado supera el ingreso marginal, no hay equilibrio."""
    assert math.isinf(modelo.breakeven_fx(1.0, FX_BASE, 10_000_000, 1.0, 0))


def test_precio_fob_cafe_reconstruye_la_carga():
    """Reexpresar y volver a multiplicar debe devolver el precio por carga."""
    r = modelo.precio_fob_cafe_desde_fnc(2_210_000, 3219.31, CFG)
    assert r['precio_interno_cop_kg'] * r['kg_excelso_por_carga'] == pytest.approx(2_210_000)


# ===========================================================================
# 2. CONTROL
# ===========================================================================
def test_jarque_bera_rechaza_colas_pesadas():
    rng = np.random.default_rng(7)
    assert riesgo.jarque_bera(pd.Series(rng.standard_t(3, 4000)))['p_value'] < 0.05


def test_jarque_bera_no_rechaza_normal():
    rng = np.random.default_rng(7)
    assert riesgo.jarque_bera(pd.Series(rng.standard_normal(4000)))['normal']


def test_var_y_es_en_una_normal_conocida():
    """Percentil 5 de una N(0,1) ~ -1.645; el ES debe ser estrictamente peor."""
    rng = np.random.default_rng(11)
    x = pd.Series(rng.standard_normal(200_000))
    assert riesgo.var_historico(x) == pytest.approx(-1.645, abs=0.02)
    assert riesgo.expected_shortfall(x) < riesgo.var_historico(x)


def test_semaforo_en_los_tres_regimenes():
    assert modelo.clasificar_riesgo(3000, 2500, 2300) == 'Rojo'
    assert modelo.clasificar_riesgo(2400, 2500, 2300) == 'Amarillo'
    assert modelo.clasificar_riesgo(2000, 2500, 2300) == 'Verde'


def test_semaforo_robusto_toma_el_peor_de_la_banda():
    """Verde solo si el producto resiste en TODO el intervalo de costos."""
    assert modelo.semaforo_robusto([2000, 2400, 3000], 2500, 2300) == 'Rojo'
    assert modelo.semaforo_robusto([2000, 2100, 2400], 2500, 2300) == 'Amarillo'
    assert modelo.semaforo_robusto([2000, 2100, 2200], 2500, 2300) == 'Verde'


# ===========================================================================
# 3. DETECCION
# ===========================================================================
def test_kupiec_rechaza_modelo_mal_calibrado():
    """Un VaR al 95% que falla el 10% de los dias debe ser rechazado."""
    assert riesgo.kupiec_pof(100, 1000, 0.05)[1] < 0.05


def test_kupiec_acepta_modelo_bien_calibrado():
    assert riesgo.kupiec_pof(50, 1000, 0.05)[1] > 0.05


def test_backtest_oos_no_mira_el_futuro():
    """Con un salto en la ultima observacion, el VaR pronosticado para ese dia no
    puede haberlo incorporado: debe contarse como violacion."""
    rng = np.random.default_rng(3)
    x = pd.Series(np.r_[rng.standard_normal(400) * 0.01, -0.25])
    out = riesgo.backtest_var_oos(x, 252, 0.95)
    assert out['violaciones'] >= 1 and out['n_obs'] < len(x)


def test_hedge_natural_reduce_sensibilidad_al_fx():
    """Un hedge debe amortiguar en AMBAS direcciones. Si solo mejorase el
    escenario adverso seria una mejora inventada, no una cobertura."""
    def amplitud(pct_imp):
        a = modelo.margen(4.25, FX_BASE * 0.9, FX_BASE, 6600, pct_imp, 900, 0.055)['margen_pct']
        b = modelo.margen(4.25, FX_BASE * 1.1, FX_BASE, 6600, pct_imp, 900, 0.055)['margen_pct']
        return b - a
    assert amplitud(0.65) < amplitud(0.30) < amplitud(0.0)


def test_margen_crece_con_el_tipo_de_cambio():
    """Propiedad economica: el exportador cobra en CAD y gasta en COP."""
    ms = [modelo.margen(4.0, f, FX_BASE, 6600, 0.3, 900, 0.055)['margen_pct']
          for f in (2000, 2400, 2800, 3200)]
    assert all(np.diff(ms) > 0)


# ===========================================================================
# 4. REGRESION SOBRE LOS ERRORES DE LA AUDITORIA
# ===========================================================================
def test_incoterm_flete_no_destruye_margen_con_traslado_completo():
    """REGRESION. El modelo original restaba el flete internacional de un ingreso
    FOB que nunca lo incluia. Con traslado completo el margen en COP no puede
    depender del flete."""
    bajo = modelo.margen(4.0, 2300, FX_BASE, 6000, 0.3, 200, 0.055, 1.0)['margen_cop']
    alto = modelo.margen(4.0, 2300, FX_BASE, 6000, 0.3, 9000, 0.055, 1.0)['margen_cop']
    assert bajo == pytest.approx(alto)


def test_incoterm_flete_si_pesa_cuando_el_exportador_lo_absorbe():
    """La contraparte de la prueba anterior: con pass-through 0 el flete si debe
    reducir el margen. Sin esto, la primera prueba pasaria por una funcion rota
    que ignorase el flete siempre."""
    alto = modelo.margen(4.0, 2300, FX_BASE, 6000, 0.3, 9000, 0.055, 1.0)['margen_cop']
    absorbido = modelo.margen(4.0, 2300, FX_BASE, 6000, 0.3, 9000, 0.055, 0.0)['margen_cop']
    assert absorbido < alto - 1000


def test_forward_cotiza_sobre_el_spot_si_la_tasa_local_es_mayor():
    """REGRESION. El modelo original tomaba abs() de los puntos forward y los
    llamaba costo. Con i_COP > i_CAD el exportador que vende CAD a plazo cobra
    prima."""
    assert modelo.puntos_forward_cip(0.12, 0.0225, 90) > 0


def test_forward_cotiza_bajo_el_spot_si_la_tasa_local_es_menor():
    assert modelo.puntos_forward_cip(0.01, 0.0225, 90) < 0


def test_retorno_log_se_compone_con_exponencial():
    """REGRESION. nivel*(1+r) sobre un retorno logaritmico subestima el nivel."""
    correcto = riesgo.nivel_desde_retorno_log(3000, -0.1381)
    incorrecto = 3000 * (1 - 0.1381)
    assert correcto > incorrecto
    assert correcto - incorrecto == pytest.approx(27.3, abs=1.0)


def test_plan_vallejo_vale_el_float_no_el_iva_completo():
    """REGRESION. El IVA de insumos es recuperable por el exportador; el beneficio
    es financiar el float, no el 19%."""
    b = modelo.beneficio_plan_vallejo(100_000, True, CFG)
    assert b['cota_superior_19pct_cop'] == pytest.approx(19_000)
    assert b['beneficio_financiero_cop'] < 0.15 * b['cota_superior_19pct_cop']


def test_plan_vallejo_sin_elegibilidad_o_sin_insumo_importado():
    assert modelo.beneficio_plan_vallejo(100_000, False, CFG)['beneficio_financiero_cop'] == 0
    assert modelo.beneficio_plan_vallejo(0.0, True, CFG)['beneficio_financiero_cop'] == 0


def test_ibr_nominal_base_360_se_convierte_a_efectiva_anual():
    """REGRESION. El modelo original dividia el IBR entre 365 tratandolo como
    efectivo. Un nominal de 11.186% base 360 equivale a ~12.01% E.A."""
    assert modelo.nominal_a_ea(0.11186, 360) == pytest.approx(0.1201, abs=0.0005)


def test_tasa_compuesta_es_menor_que_la_simple_bajo_un_anio():
    assert modelo.tasa_diaria_desde_ea(0.19, 90) < 0.19 * 90 / 365


def test_sqrt_t_sobreestima_el_cuantil_en_serie_con_reversion():
    """REGRESION. Escalar un cuantil por sqrt(T) exige normalidad, que la serie
    rechaza. En un proceso con reversion a la media el escalado sobreestima."""
    rng = np.random.default_rng(5)
    n, x, s = 3000, 0.0, [0.0]
    for _ in range(n):
        x = 0.85 * x + rng.standard_normal() * 0.01      # AR(1) con reversion
        s.append(x)
    precios = pd.Series(np.exp(np.array(s)) * 2600)
    ret = np.log(precios / precios.shift(1)).dropna()
    d = riesgo.var_multihorizonte(ret, precios, [30], 0.95)
    assert d.loc[0, 'sesgo_sqrt_t_pct'] > 0


def test_modo_de_transporte_desconocido_falla_ruidosamente():
    """Un modo no previsto debe romper, no caer en silencio al caso maritimo."""
    with pytest.raises(ValueError):
        modelo.costo_logistico_cop_kg('teletransporte', 'densa', False,
                                      'CTG-Montreal', 1000, 3200, CFG)


# ===========================================================================
# 5. INTEGRIDAD DE LA CONFIGURACION
# ===========================================================================
def test_todos_los_productos_tienen_transporte_y_banda_de_costos():
    hs_t = set(config.TRANSPORTE.codigo_hs)
    hs_c = set(config.COSTOS_SECTOR.codigo_hs)
    assert len(hs_t) == len(hs_c) == 10 and hs_t == hs_c


def test_las_bandas_de_costo_estan_ordenadas_y_son_ratios_validos():
    c = config.COSTOS_SECTOR
    assert (c.ratio_min < c.ratio_base).all() and (c.ratio_base < c.ratio_max).all()
    assert (c.ratio_min > 0).all() and (c.ratio_max < 1).all()


def test_los_grados_de_evidencia_son_validos_y_estan_declarados():
    assert set(config.COSTOS_SECTOR.grado) <= {'A', 'B', 'C'}
    assert config.COSTOS_SECTOR.fuente.str.len().min() > 30


def test_ningun_producto_depende_de_un_ratio_uniforme():
    """REGRESION. El factor unico de 0.60 volvia el margen identico para los 10
    productos y convertia cualquier ranking en un artefacto del precio por kilo."""
    assert config.COSTOS_SECTOR.ratio_base.nunique() > 5
