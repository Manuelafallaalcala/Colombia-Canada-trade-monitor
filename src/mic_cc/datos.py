"""Capa de datos: adquisicion y construccion de la serie COP/CAD.

Funciones puras, sin estado global y con respaldo local funcional. El cuaderno
original declaraba en su README que corria sin descargas externas mientras
llamaba a una API en vivo, y nunca leia el archivo de respaldo que si estaba en
el repositorio.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
import requests

URL_TRM = 'https://www.datos.gov.co/resource/32sa-8pi3.json'
URL_BOC = 'https://www.bankofcanada.ca/valet/observations/{serie}/json'


def descargar_trm(inicio: str, fin: str | None = None, timeout: int = 120) -> pd.DataFrame:
    """TRM oficial del Banco de la Republica via Datos Abiertos.

    `vigenciadesde` es el dia de vigencia de la tasa; la TRM se calcula con las
    operaciones del dia habil ANTERIOR. Ese rezago se corrige en
    `construir_copcad`.
    """
    url = (f'{URL_TRM}?$select=vigenciadesde,valor'
           f"&$where=vigenciadesde>'{inicio}T00:00:00'"
           '&$order=vigenciadesde&$limit=50000')
    d = pd.DataFrame(requests.get(url, timeout=timeout).json())
    d['fecha'] = pd.to_datetime(d['vigenciadesde'])
    d['TRM_COP_USD'] = d['valor'].astype(float)
    d = d[['fecha', 'TRM_COP_USD']].sort_values('fecha').reset_index(drop=True)
    return d[d['fecha'] <= pd.Timestamp(fin)] if fin else d


def descargar_usdcad(inicio: str, fin: str | None = None, timeout: int = 90) -> pd.DataFrame:
    """USD/CAD del Bank of Canada.

    FXUSDCAD existe desde 2017-01. Para el tramo anterior se usa la serie legacy
    IEXE0101 (noon rate), sin la cual los episodios de 2014-2016 no se pueden
    reexpresar en COP/CAD.
    """
    fin = fin or pd.Timestamp.today().strftime('%Y-%m-%d')
    marcos = []
    for serie in ('IEXE0101', 'FXUSDCAD'):
        url = URL_BOC.format(serie=serie) + f'?start_date={inicio}&end_date={fin}'
        obs = requests.get(url, timeout=timeout).json().get('observations', [])
        filas = [{'fecha': o['d'], 'USDCAD': float(o[serie]['v'])}
                 for o in obs if serie in o and o[serie].get('v')]
        if filas:
            marcos.append(pd.DataFrame(filas))
    if not marcos:
        raise RuntimeError('Bank of Canada no devolvio observaciones')
    d = pd.concat(marcos, ignore_index=True)
    d['fecha'] = pd.to_datetime(d['fecha'])
    return d.drop_duplicates('fecha', keep='last').sort_values('fecha').reset_index(drop=True)


def cargar_trm_local(ruta: str) -> pd.DataFrame:
    d = (pd.read_excel(ruta, sheet_name='Datos COP-USD')
           .rename(columns={'Fecha (aaaa/mm/dd)': 'fecha', 'TRM': 'TRM_COP_USD'}))
    d['fecha'] = pd.to_datetime(d['fecha'])
    return d[['fecha', 'TRM_COP_USD']].sort_values('fecha').reset_index(drop=True)


def cargar_usdcad_local(ruta: str) -> pd.DataFrame:
    """Respaldo offline: el archivo de la Tarea 2 que el modelo original nunca leia."""
    d = pd.read_excel(ruta)
    cf = next(c for c in d.columns if 'fecha' in str(c).lower() or 'date' in str(c).lower())
    cv = next(c for c in d.columns if c != cf and pd.api.types.is_numeric_dtype(d[c]))
    d = d.rename(columns={cf: 'fecha', cv: 'USDCAD'})[['fecha', 'USDCAD']]
    d['fecha'] = pd.to_datetime(d['fecha'])
    return d.sort_values('fecha').reset_index(drop=True)


def construir_copcad(trm: pd.DataFrame, usdcad: pd.DataFrame,
                     alinear_rezago: bool = True) -> pd.DataFrame:
    """COP/CAD = (COP/USD) / (CAD/USD).

    Con `alinear_rezago=True` se empareja TRM(D) con USDCAD(D-1 habil): la TRM
    vigente el dia D se calcula con el mercado del dia habil anterior, mientras
    que la cotizacion del BoC del dia D refleja el mercado del dia D. Sin ese
    ajuste la serie cruzada mezcla dos fechas de mercado distintas e infla la
    varianza de los retornos con ruido de emparejamiento (~260 pb de volatilidad
    anualizada en esta serie).
    """
    fx = usdcad.copy()
    if alinear_rezago:
        fx['fecha'] = fx['fecha'] + pd.tseries.offsets.BDay(1)
    d = trm.merge(fx, on='fecha', how='inner').sort_values('fecha').reset_index(drop=True)
    if d.empty:
        raise ValueError('El cruce TRM x USD/CAD quedo vacio: revisar rangos de fecha')
    d['COP_CAD'] = d['TRM_COP_USD'] / d['USDCAD']
    d['retorno_log'] = np.log(d['COP_CAD'] / d['COP_CAD'].shift(1))
    return d


def cargar_fx(params: dict, data_dir: str) -> tuple[pd.DataFrame, dict]:
    """Orquesta la adquisicion con respaldo local y devuelve la serie mas la
    procedencia de cada insumo, para que quede trazable en el informe."""
    origen = {}
    try:
        trm = descargar_trm(params['fx_inicio'], params['fx_fin'])
        origen['trm'] = 'Datos Abiertos (BanRep), en vivo'
    except Exception as e:                                    # pragma: no cover
        trm = cargar_trm_local(f'{data_dir}/TRM_COP_USD_2020_2024.xlsx')
        origen['trm'] = f'archivo local (respaldo: {type(e).__name__})'
    try:
        ucad = descargar_usdcad(params['fx_inicio'], params['fx_fin'])
        origen['usdcad'] = 'Bank of Canada Valet, en vivo'
    except Exception as e:                                    # pragma: no cover
        ucad = cargar_usdcad_local(f'{data_dir}/USDCAD_2020_2024.xlsx')
        origen['usdcad'] = f'archivo local (respaldo: {type(e).__name__})'
    return construir_copcad(trm, ucad, params['alinear_trm_rezago']), origen
