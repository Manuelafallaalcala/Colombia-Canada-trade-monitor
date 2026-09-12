"""MIC-CC — Monitor de Inteligencia Comercial Colombia-Canada.

Modelo financiero de riesgo cambiario para el Top 10 de exportaciones
colombianas hacia Canada bajo el TLCC. Fase 4 del proyecto, ODEM — Universidad
EAN.

Esta es la version consolidada: unifica el modelo original de la Fase 4, las
correcciones de la auditoria cuantitativa de julio de 2026 y la refactorizacion
a paquete, en un solo cuerpo de codigo. Las tres versiones previas del cuaderno
quedan en el historial de git; el arbol de trabajo tiene una sola.

Separacion de intereses
-----------------------
    config   parametros, overrides de datos y estructura de costos por producto
    datos    adquisicion de series FX y construccion de la tasa cruzada COP/CAD
    riesgo   VaR historico, Expected Shortfall, backtesting y normalidad
    modelo   margen, breakeven, logistica, tasas, cobertura y tributario

El cuaderno `notebooks/mic_cc_modelo_financiero.ipynb` ORQUESTA: no contiene
ninguna formula. Cada ecuacion existe una sola vez, aqui, y esta cubierta por
`tests/test_modelo.py`.

Uso
---
    from mic_cc import config, datos, riesgo, modelo

    fx, origen = datos.cargar_fx(config.PARAMS, 'data/raw')
    v95 = riesgo.var_historico(fx['retorno_log'].dropna())
"""
from . import config, datos, modelo, riesgo

__all__ = ['config', 'datos', 'modelo', 'riesgo']
__version__ = '3.0.0'
