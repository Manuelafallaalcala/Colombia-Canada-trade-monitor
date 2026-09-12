"""MIC-CC — Monitor de Inteligencia Comercial Colombia-Canada.

Modelo financiero de riesgo cambiario para el Top 10 de exportaciones
colombianas hacia Canada bajo el TLCC.

Version auditada: reconstruccion del modelo de la Fase 4 tras la auditoria
cuantitativa del 26-27 de julio de 2026. Conserva intactos el cuaderno original
`04_financial_model.ipynb` y sus salidas en `outputs/`.

Separacion de intereses
-----------------------
    config   parametros, overrides de datos y estructura de costos por producto
    datos    adquisicion de series FX y construccion de la tasa cruzada COP/CAD
    riesgo   VaR historico, Expected Shortfall, backtesting y normalidad
    modelo   margen, breakeven, logistica, tasas, cobertura y tributario

Uso
---
    from mic_cc import config, datos, riesgo, modelo

    fx, origen = datos.cargar_fx(config.PARAMS, '../dataraw')
    v95 = riesgo.var_historico(fx['retorno_log'].dropna())
"""
from . import config, datos, modelo, riesgo

__all__ = ['config', 'datos', 'modelo', 'riesgo']
__version__ = '2.0.0'
