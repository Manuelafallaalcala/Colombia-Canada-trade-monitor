"""Configuracion del modelo MIC-CC.

Todo parametro de negocio vive aqui, con fuente, fecha y GRADO DE EVIDENCIA.
Ninguna cifra de negocio debe aparecer escrita dentro de una funcion de calculo.

Grados de evidencia
-------------------
A  Dato duro de fuente primaria, verificable y fechado.
B  Dato gremial o sectorial cualitativo, cuantificado por inferencia razonada.
C  Supuesto de trabajo. NO es evidencia. Requiere validacion antes de publicar
   cualquier conclusion que dependa de el.
"""
from __future__ import annotations
import pandas as pd

# ---------------------------------------------------------------------------
# Parametros generales
# ---------------------------------------------------------------------------
PARAMS: dict = {
    # --- ventana de datos y riesgo ---------------------------------------
    'fx_inicio': '2014-01-01',
    'fx_fin': None,                       # None = hasta hoy
    'ventana_base_dias': 90,
    'alinear_trm_rezago': True,           # TRM(D) refleja mercado de D-1; BoC(D) refleja D
    'dias_habiles_anio': 252,
    'nivel_confianza': 0.95,
    'ventana_var_movil': 252,
    'horizontes_cobro': (30, 60, 90),

    # --- incoterm ---------------------------------------------------------
    # tabla_B4 cotiza los 10 productos 'Kilogramo (FOB)'.
    # 1.0 = el flete internacional se traslada al comprador (FOB puro, o CFR con
    #       traslado completo dentro del precio).
    # 0.0 = el exportador lo absorbe: supuesto implicito, y nunca declarado, del
    #       modelo original.
    'pass_through_flete': 1.0,
    'pass_through_sensibilidad': (0.0, 0.5, 1.0),

    # --- perfil del exportador -------------------------------------------
    # 'productor'      : produce lo que exporta; el costo es su costo de finca/planta.
    # 'comercializador': compra a precio de mercado interno y exporta; el costo es
    #                    ese precio de compra, mucho mas alto respecto al FOB.
    # El modelo original nunca distinguio los dos casos, pese a que cambian el
    # margen por un factor cercano a 2 en productos con precio interno publicado.
    'perfil_exportador': 'productor',

    # --- costos accesorios de exportacion --------------------------------
    # % del valor FOB: flete interno a puerto, THC, agenciamiento aduanero, DEX,
    # seguro de carga, GMF 4x1000. Ausentes por completo en el modelo original.
    'costos_accesorios_pct_fob': 0.055,
    'costos_accesorios_rango': (0.030, 0.080),

    # --- logistica --------------------------------------------------------
    # Payload util por clase de densidad. Un contenedor de 20 pies tiene ~33 m3 y
    # payload maximo ~28 t: solo la carga densa se acerca a ese limite; la carga
    # ligera "cuba" antes de "pesar".
    'payload_kg': {'densa': 20000, 'media': 12000, 'ligera': 7000},
    'recargo_reefer': 0.60,
    'flete_aereo_usd_kg': 2.80,           # GRADO C: estimacion, no cotizacion
    'flete_aereo_rango': (2.00, 4.00),
    'flete_granel_usd_kg': {'CTG-Montreal': 0.015, 'CTG-Vancouver': 0.022},
    'flete_granel_rango': (0.012, 0.030), # GRADO C: derivado de TC Panamax

    # --- tasas ------------------------------------------------------------
    'base_dias_ibr': 360,                 # el IBR se cotiza nominal base 360
    'tasa_fondeo_pyme_ea': 0.1919,        # GRADO A: IBC credito ordinario, jun-2026
    'usar_ibr_como_piso': True,

    # --- cobertura cambiaria ----------------------------------------------
    'spread_ndf_pyme': 0.0075,            # GRADO C: 75 pb ida y vuelta, ticket pequeno
    'spread_ndf_rango': (0.0030, 0.0150),
    'monto_minimo_ndf_usd': 10000,        # GRADO A: Davivienda, Tarea 7

    # --- Plan Vallejo / IVA ------------------------------------------------
    'tarifa_iva': 0.19,                   # GRADO A: tarifa general, Colombia
    'dias_float_iva': 120,                # bimestre + radicacion + 50d (Art. 855 ET)
    'dias_float_rango': (50, 180),
    'exportador_con_derecho_devolucion': True,

    # --- cafe: constantes tecnicas de la FNC ------------------------------
    'kg_cps_por_carga': 125,              # carga = 125 kg cafe pergamino seco
    'factor_rendimiento': 94,             # 94 kg cps -> 70 kg excelso
    'kg_excelso_por_saco': 70,
}


# ---------------------------------------------------------------------------
# Correcciones de datos verificadas contra fuente primaria.
# NO se altera ningun archivo de dataraw/: el override se aplica en memoria.
# ---------------------------------------------------------------------------
OVERRIDES = pd.DataFrame([
    dict(codigo_hs='0901.11.90.00', campo='precio_usd',
         valor_original=3.200, valor_corregido=7.817, grado='A',
         fuente='FNC precio_cafe.pdf 2026-07-27: cierre NY 324.55 USc/lb + prima Colombia ~30 USc/lb; '
                '354.55 USc/lb x 2.20462 lb/kg',
         fecha_verificacion='2026-07-27',
         motivo='El precio original (1.45 USD/lb) contradice la fuente ICO/FNC que el propio archivo cita.'),
    dict(codigo_hs='*', campo='tipo_cambio_usd_cad',
         valor_original=1.33, valor_corregido=1.4083, grado='A',
         fuente='Bank of Canada, serie FXUSDCAD, ultimo dato disponible',
         fecha_verificacion='2026-07-27',
         motivo='El 1.33 del archivo no corresponde a ninguna fecha cercana a su fecha de consulta.'),
])


# ---------------------------------------------------------------------------
# Modo de transporte REAL por producto.
# El modelo original aplicaba flete de contenedor maritimo desde Cartagena a los
# 10 productos, incluidas las flores (92% se exportan por aire desde El Dorado)
# y el carbon (granel, no contenedor).
# ---------------------------------------------------------------------------
TRANSPORTE = pd.DataFrame([
    ('0901.11.90.00', 'maritimo', 'densa',  False),
    ('2701.12.00.00', 'granel',   'densa',  False),
    ('0804.50.00.00', 'maritimo', 'media',  True),
    ('0603.19.00.00', 'aereo',    'ligera', True),
    ('3004.32.00.00', 'maritimo', 'media',  False),
    ('6115.96.00.00', 'maritimo', 'ligera', False),
    ('7307.92.00.00', 'maritimo', 'densa',  False),
    ('0304.82.00.00', 'maritimo', 'media',  True),
    ('2008.19.00.00', 'maritimo', 'ligera', False),
    ('0603.11.00.00', 'aereo',    'ligera', True),
], columns=['codigo_hs', 'modo_transporte', 'clase_densidad', 'requiere_frio'])


# ---------------------------------------------------------------------------
# Estructura de costos por producto.
#
# Reemplaza el factor unico de 0.60 que el modelo original aplicaba a los 10
# productos. Ese factor no solo carecia de fuente: al ser uniforme volvia el
# margen identico para todos (margen% = 1 - factor - accesorios), de modo que
# cualquier ranking de rentabilidad por producto era un artefacto del precio por
# kilogramo, no evidencia.
#
# Aqui cada producto tiene una BANDA con grado de evidencia. El modelo evalua la
# banda completa y el semaforo solo asigna Verde si el producto resiste en TODO
# el intervalo. Un punto sin intervalo, en este proyecto, seria falsa precision.
#
# ratio = costo de produccion (o de compra, si es comercializador) / precio FOB
# ---------------------------------------------------------------------------
COSTOS_SECTOR = pd.DataFrame([
    dict(codigo_hs='0901.11.90.00', producto='Cafe sin tostar',
         ratio_min=0.50, ratio_base=0.62, ratio_max=0.72, grado='B',
         fuente='FNC: precio interno de compra 2.210.000 COP/carga (2026-07-27) equivale a '
                '~94% del FOB para un COMERCIALIZADOR (grado A, ver ratio_comercializador). '
                'Para un PRODUCTOR el costo de finca es sustancialmente menor en un ano de '
                'precio alto como 2026.',
         ratio_comercializador=0.943, grado_comercializador='A'),
    dict(codigo_hs='2701.12.00.00', producto='Carbon bituminoso',
         ratio_min=0.70, ratio_base=0.85, ratio_max=0.95, grado='C',
         fuente='Sector en crisis de margenes a precios corrientes (Fenalcarbon, Portafolio). '
                'Sin desglose publico de cash cost por tonelada.',
         ratio_comercializador=0.95, grado_comercializador='C'),
    dict(codigo_hs='0804.50.00.00', producto='Frutas tropicales (guayaba/mango)',
         ratio_min=0.65, ratio_base=0.75, ratio_max=0.85, grado='C',
         fuente='Sin desglose de Asohofrucol para mango/guayaba en Colombia.',
         ratio_comercializador=0.88, grado_comercializador='C'),
    dict(codigo_hs='0603.19.00.00', producto='Flores frescas otras (pompones/hortensias)',
         ratio_min=0.80, ratio_base=0.87, ratio_max=0.93, grado='B',
         fuente='Asocolflores: mano de obra >50% del costo total y transporte especializado + '
                'frio ~25%; el gremio reporta margenes estrechos y presion por revaluacion.',
         ratio_comercializador=0.93, grado_comercializador='C'),
    dict(codigo_hs='3004.32.00.00', producto='Medicamentos corticosteroides',
         ratio_min=0.40, ratio_base=0.55, ratio_max=0.70, grado='C',
         fuente='ANDI confirma dependencia de principios activos importados, sin estructura de '
                'costos de fabricacion local publicada.',
         ratio_comercializador=0.80, grado_comercializador='C'),
    dict(codigo_hs='6115.96.00.00', producto='Medias/calcetines fibra sintetica',
         ratio_min=0.65, ratio_base=0.74, ratio_max=0.82, grado='C',
         fuente='Sin dato de Inexmoda/ACOLTEX para la partida. Rango tipico de confeccion.',
         ratio_comercializador=0.85, grado_comercializador='C'),
    dict(codigo_hs='7307.92.00.00', producto='Accesorios tuberia hierro/acero',
         ratio_min=0.70, ratio_base=0.79, ratio_max=0.88, grado='C',
         fuente='ANDI siderurgia: 22% del consumo aparente es importado; precios de chatarra y '
                'mineral con alzas de 92-108% en 12 meses. Sin margen publicado para HS 7307.',
         ratio_comercializador=0.90, grado_comercializador='C'),
    dict(codigo_hs='0304.82.00.00', producto='Filetes de trucha congelados',
         ratio_min=0.70, ratio_base=0.79, ratio_max=0.87, grado='B',
         fuente='Fedeacua/acuicola.co: el alimento balanceado es 60-70% del costo de produccion '
                'en piscicultura y depende casi por completo de materia prima importada.',
         ratio_comercializador=0.88, grado_comercializador='C'),
    dict(codigo_hs='2008.19.00.00', producto='Nueces y semillas preparadas',
         ratio_min=0.75, ratio_base=0.83, ratio_max=0.90, grado='C',
         fuente='Segmento mayormente importador-procesador: la materia prima no se cultiva '
                'comercialmente en Colombia, lo que comprime el margen de transformacion.',
         ratio_comercializador=0.90, grado_comercializador='C'),
    dict(codigo_hs='0603.11.00.00', producto='Rosas frescas cortadas',
         ratio_min=0.80, ratio_base=0.87, ratio_max=0.93, grado='B',
         fuente='Mismo gremio y estructura que pompones/hortensias (Asocolflores). La rosicultura '
                'es reconocida como particularmente intensiva en mano de obra.',
         ratio_comercializador=0.93, grado_comercializador='C'),
])


def resumen_evidencia() -> pd.DataFrame:
    """Conteo de parametros por grado de evidencia. Sirve para que ningun informe
    presente como hallazgo algo que descansa sobre supuestos de grado C."""
    filas = []
    for _, x in COSTOS_SECTOR.iterrows():
        filas.append({'parametro': f'ratio_costo · {x.producto}', 'grado': x.grado})
    for _, o in OVERRIDES.iterrows():
        filas.append({'parametro': f'override · {o.campo}', 'grado': o.grado})
    filas += [
        {'parametro': 'tasa_fondeo_pyme_ea', 'grado': 'A'},
        {'parametro': 'tarifa_iva', 'grado': 'A'},
        {'parametro': 'monto_minimo_ndf_usd', 'grado': 'A'},
        {'parametro': 'flete_aereo_usd_kg', 'grado': 'C'},
        {'parametro': 'flete_granel_usd_kg', 'grado': 'C'},
        {'parametro': 'spread_ndf_pyme', 'grado': 'C'},
        {'parametro': 'costos_accesorios_pct_fob', 'grado': 'C'},
        {'parametro': 'dias_float_iva', 'grado': 'B'},
    ]
    return pd.DataFrame(filas)
