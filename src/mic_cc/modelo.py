"""Nucleo economico: margen, breakeven, logistica, tasas, cobertura y tributario.

Cada formula existe UNA sola vez. El cuaderno original tenia la ecuacion de
margen implementada tres veces de forma independiente, lo que obliga a
sincronizar tres ediciones para cualquier correccion.
"""
from __future__ import annotations
import unicodedata


# ---------------------------------------------------------------------------
# Margen y punto de equilibrio
# ---------------------------------------------------------------------------
def margen(precio_fob_cad: float, fx: float, fx_base: float,
           costo_produccion_cop: float, pct_importado: float,
           costo_logistico_cop: float, costos_accesorios_pct: float = 0.0,
           pass_through_flete: float = 1.0) -> dict:
    """Ecuacion de margen del modelo.

    COHERENCIA DE INCOTERM
    ----------------------
    Los 10 precios de `tabla_B4` estan cotizados 'Kilogramo (FOB)'. Bajo FOB el
    flete internacional lo paga el COMPRADOR; bajo CFR/CIF lo paga el exportador
    pero se lo factura dentro del precio. En los dos casos el flete NO destruye
    margen. El modelo original lo restaba de un ingreso FOB que nunca lo
    incluyo, cobrandolo dos veces: ese es el origen del -348% del carbon y del
    margen negativo de las flores, no la economia de esos productos.

        pass_through_flete = 1.0 -> traslado completo al comprador (defecto)
        pass_through_flete = 0.0 -> el exportador absorbe todo el flete
                                    (supuesto implicito del modelo original)

    COBERTURA NATURAL
    -----------------
    La porcion importada del costo escala con el tipo de cambio; la nacional y el
    flete no. Es un hedge genuino: amortigua tanto la perdida en el escenario
    adverso como la ganancia en el favorable.

    Los costos accesorios de exportacion (flete interno, THC, agenciamiento,
    seguro, GMF) se cobran sobre el valor FOB y son del exportador bajo cualquier
    incoterm.
    """
    ingreso_fob = precio_fob_cad * fx
    ingreso = ingreso_fob + pass_through_flete * costo_logistico_cop
    costo_importado = costo_produccion_cop * pct_importado * (fx / fx_base)
    costo_nacional = costo_produccion_cop * (1 - pct_importado)
    costo_accesorio = ingreso_fob * costos_accesorios_pct
    costo_total = costo_importado + costo_nacional + costo_logistico_cop + costo_accesorio
    m = ingreso - costo_total
    return {'ingreso_fob_cop': ingreso_fob, 'ingreso_cop': ingreso,
            'costo_importado_cop': costo_importado, 'costo_nacional_cop': costo_nacional,
            'costo_logistico_cop': costo_logistico_cop, 'costo_accesorio_cop': costo_accesorio,
            'costo_total_cop': costo_total, 'margen_cop': m,
            'margen_pct': m / ingreso * 100,
            'margen_pct_sobre_fob': m / ingreso_fob * 100}


def breakeven_fx(precio_fob_cad: float, fx_base: float, costo_produccion_cop: float,
                 pct_importado: float, costo_logistico_cop: float,
                 costos_accesorios_pct: float = 0.0,
                 pass_through_flete: float = 1.0) -> float:
    """Tipo de cambio al que el margen es cero, resuelto ANALITICAMENTE incluyendo
    la cobertura natural (el costo importado depende del propio FX que se despeja):

        P*X + pt*L - Ci*(X/Xb) - Cn - L - a*P*X = 0
        X * (P*(1-a) - Ci/Xb) = Cn + (1-pt)*L

    Con pt=1 el flete se cancela y el breakeven NO depende de la ruta: bajo
    traslado completo, elegir Montreal o Vancouver no altera la economia del
    exportador. Esa invariancia es un resultado del modelo, no un defecto.

    Devuelve inf cuando el ingreso marginal no alcanza a cubrir el costo
    importado: el producto no tiene equilibrio a ningun tipo de cambio.
    """
    ci = costo_produccion_cop * pct_importado
    cn = costo_produccion_cop * (1 - pct_importado)
    denom = precio_fob_cad * (1 - costos_accesorios_pct) - ci / fx_base
    if denom <= 0:
        return float('inf')
    return (cn + (1 - pass_through_flete) * costo_logistico_cop) / denom


def clasificar_riesgo(breakeven: float, fx_adverso: float, fx_muy_adverso: float) -> str:
    """Semaforo de riesgo cambiario. Los umbrales se pasan EXPLICITAMENTE.

    El modelo original los ligaba como argumentos por defecto en tiempo de
    definicion, lo que congelaba el tipo de cambio de clasificacion en silencio
    ante cualquier recalibracion posterior.
    """
    if fx_adverso < breakeven:
        return 'Rojo'
    if fx_muy_adverso < breakeven:
        return 'Amarillo'
    return 'Verde'


def semaforo_robusto(breakevens: list[float], fx_adverso: float,
                     fx_muy_adverso: float) -> str:
    """Semaforo evaluado sobre TODA la banda de costos del producto.

    Solo asigna Verde si el producto resiste en el extremo mas desfavorable de su
    propia banda de incertidumbre. Reportar un color a partir de un unico punto
    central, cuando el parametro que lo gobierna es un supuesto, es falsa
    precision.
    """
    colores = {clasificar_riesgo(b, fx_adverso, fx_muy_adverso) for b in breakevens}
    for peor in ('Rojo', 'Amarillo', 'Verde'):
        if peor in colores:
            return peor
    return 'Verde'


# ---------------------------------------------------------------------------
# Logistica
# ---------------------------------------------------------------------------
def costo_logistico_cop_kg(modo: str, clase_densidad: str, requiere_frio: bool,
                           ruta: str, tarifa_contenedor_usd: float,
                           trm: float, cfg: dict) -> tuple[float, str]:
    """COP por kilogramo segun el modo de transporte REAL del producto.

    El modelo original aplicaba tarifa de contenedor maritimo a los 10 productos,
    incluidas las flores (92% se exportan por aire) y el carbon (granel).
    """
    if modo == 'aereo':
        usd_kg = cfg['flete_aereo_usd_kg']
        detalle = f'aereo BOG-Canada {usd_kg:.2f} USD/kg'
    elif modo == 'granel':
        usd_kg = cfg['flete_granel_usd_kg'][ruta]
        detalle = f'granel {usd_kg:.3f} USD/kg'
    elif modo == 'maritimo':
        payload = cfg['payload_kg'][clase_densidad]
        tarifa = tarifa_contenedor_usd * (1 + cfg['recargo_reefer'] if requiere_frio else 1)
        usd_kg = tarifa / payload
        detalle = (f'contenedor {tarifa:,.0f} USD / {payload:,} kg '
                   f'({clase_densidad}{", reefer" if requiere_frio else ""})')
    else:
        raise ValueError(f'modo de transporte desconocido: {modo!r}')
    return usd_kg * trm, detalle


# ---------------------------------------------------------------------------
# Tasas de interes
# ---------------------------------------------------------------------------
def tasa_diaria_desde_ea(tasa_ea: float, dias: int) -> float:
    """Factor compuesto correcto para una tasa efectiva anual."""
    return (1 + tasa_ea) ** (dias / 365) - 1


def nominal_a_ea(tasa_nominal: float, base_dias: int = 360) -> float:
    """El IBR se cotiza nominal base 360 (Manual de uso del IBR, BanRep).

    El modelo original lo dividia entre 365 tratandolo como si ya fuera efectivo.
    """
    return (1 + tasa_nominal / base_dias) ** 365 - 1


def costo_capital_trabajo(costo_total_cop: float, tasa_ea: float, dias: int) -> float:
    """Costo de financiar el capital inmovilizado mientras se espera el cobro.

    Se aplica sobre el COSTO (lo ya desembolsado), no sobre la utilidad esperada,
    que todavia no existe.
    """
    return costo_total_cop * tasa_diaria_desde_ea(tasa_ea, dias)


# ---------------------------------------------------------------------------
# Cobertura cambiaria
# ---------------------------------------------------------------------------
def puntos_forward_cip(i_local_ea: float, i_extranjera_ea: float, dias: int) -> float:
    """Paridad cubierta EXACTA y CON SIGNO:

        F/S - 1 = (1+i_local)^t / (1+i_extranjera)^t - 1

    Positivo => el forward COP/CAD cotiza SOBRE el spot. Un exportador que vende
    CAD a plazo recibe ese diferencial como PRIMA, no lo paga como costo. El
    modelo original tomaba abs() de este numero y lo llamaba 'costo de
    cobertura', invirtiendo el signo del resultado economico.
    """
    t = dias / 365
    return (1 + i_local_ea) ** t / (1 + i_extranjera_ea) ** t - 1


def evaluar_cobertura(ingreso_cop: float, prima_forward_pct: float,
                      spread_ndf: float, var_pct: float, es_pct: float) -> dict:
    """Decision de cobertura planteada correctamente.

    El modelo original comparaba un costo cierto contra un cuantil de cola al 5%
    -magnitudes no comparables-, y con |puntos_forward| proporcional a T frente a
    |VaR| proporcional a sqrt(T) la desigualdad no podia invertirse a ningun
    horizonte: la conclusion 'Cubrirse' estaba forzada por construccion, no
    obtenida de los datos.

    Aqui se separan las dos preguntas que el exportador realmente enfrenta:

      1. Valor esperado. Bajo camino aleatorio E[S_T] = S, de modo que cubrirse
         aporta la prima del forward menos el costo de transaccion (spread NDF).
      2. Valor de reduccion de riesgo. El forward elimina la cola completa, en
         ambas direcciones. Se reporta aparte y NO se suma al valor esperado.
    """
    prima_neta = prima_forward_pct - spread_ndf
    return {'prima_forward_pct': prima_forward_pct, 'spread_ndf_pct': spread_ndf,
            'valor_esperado_neto_pct': prima_neta,
            'valor_esperado_neto_cop': prima_neta * ingreso_cop,
            'cola_var_evitada_pct': abs(var_pct), 'cola_es_evitada_pct': abs(es_pct),
            'cola_var_evitada_cop': abs(var_pct) * ingreso_cop,
            'recomendacion': ('Cubrirse (valor esperado positivo + elimina cola)'
                              if prima_neta > 0 else
                              'Cubrirse solo por reduccion de riesgo (valor esperado negativo)')}


# ---------------------------------------------------------------------------
# Tributario
# ---------------------------------------------------------------------------
def beneficio_plan_vallejo(costo_importado_cop: float, aplica: bool, cfg: dict) -> dict:
    """Valor financiero REAL del Plan Vallejo para un exportador.

    El IVA sobre insumos importados no es un costo hundido para un exportador:
    las exportaciones son exentas con derecho a devolucion (Arts. 481, 485, 489 y
    850 del Estatuto Tributario), asi que ese IVA se recupera de todos modos. Lo
    que el Plan Vallejo evita es FINANCIAR ese IVA mientras se tramita la
    devolucion.

        beneficio = IVA x costo_importado x [(1+i)^(dias_float/365) - 1]

    Se conserva aparte el 19% bruto como COTA SUPERIOR: solo seria el beneficio
    real si la empresa no tuviera derecho, o acceso efectivo, a la devolucion.

    El modelo original sumaba ese 19% completo al margen, acreditando un ahorro
    sobre un costo que su propia base de costos nunca cargo.
    """
    if not aplica or costo_importado_cop <= 0:
        return {'beneficio_financiero_cop': 0.0, 'cota_superior_19pct_cop': 0.0}
    iva = cfg['tarifa_iva'] * costo_importado_cop
    carry = tasa_diaria_desde_ea(cfg['tasa_fondeo_pyme_ea'], cfg['dias_float_iva'])
    financiero = iva * carry if cfg['exportador_con_derecho_devolucion'] else iva
    return {'beneficio_financiero_cop': financiero, 'cota_superior_19pct_cop': iva}


# ---------------------------------------------------------------------------
# Utilidades
# ---------------------------------------------------------------------------
def normalizar(valor) -> str:
    """Minusculas sin tildes, para comparar texto de archivos de origen distinto."""
    t = str(valor).strip().lower()
    return ''.join(c for c in unicodedata.normalize('NFKD', t) if not unicodedata.combining(c))


def precio_fob_cafe_desde_fnc(precio_interno_carga_cop: float, trm: float,
                              cfg: dict) -> dict:
    """Reexpresa el precio interno de compra de la FNC (COP por carga de 125 kg de
    cafe pergamino seco) en COP y USD por kilogramo de cafe EXCELSO exportable.

    Sirve para dos cosas: anclar el precio FOB con fuente primaria, y medir el
    ratio costo/precio de un exportador COMERCIALIZADOR, que compra a ese precio
    interno. Ese ratio (~0.94) es radicalmente distinto del 0.60 uniforme que
    asumia el modelo original.
    """
    kg_excelso = (cfg['kg_cps_por_carga'] / cfg['factor_rendimiento']
                  * cfg['kg_excelso_por_saco'])
    cop_kg = precio_interno_carga_cop / kg_excelso
    return {'kg_excelso_por_carga': kg_excelso, 'precio_interno_cop_kg': cop_kg,
            'precio_interno_usd_kg': cop_kg / trm}


# ---------------------------------------------------------------------------
# Cobertura natural y exposicion cambiaria
# ---------------------------------------------------------------------------
def efecto_cobertura_natural(precio_fob_cad: float, fx: float, fx_base: float,
                             costo_produccion_cop: float, pct_importado: float,
                             costo_logistico_cop: float,
                             costos_accesorios_pct: float = 0.0,
                             pass_through_flete: float = 1.0) -> dict:
    """Cuanto amortigua el margen la porcion importada del costo.

    Se mide como diferencia contra el CONTRAFACTUAL de la misma empresa con el
    mismo costo total pero 100% nacional (pct_importado = 0). Ese es el unico
    contraste que aisla la cobertura: comparar contra otro producto mezcla el
    efecto del hedge con el de su estructura de costos.

    El hedge es simetrico. Amortigua la perdida cuando el CAD se debilita y
    recorta la ganancia cuando se fortalece; `amortiguacion_pp` es positiva solo
    en el lado adverso. Presentarlo como un beneficio incondicional -como hacia
    el modelo original- confunde reduccion de varianza con aumento de valor.
    """
    comun = (costo_logistico_cop, costos_accesorios_pct, pass_through_flete)
    con = margen(precio_fob_cad, fx, fx_base, costo_produccion_cop, pct_importado, *comun)
    sin = margen(precio_fob_cad, fx, fx_base, costo_produccion_cop, 0.0, *comun)
    return {'margen_pct_con_hedge': con['margen_pct'],
            'margen_pct_sin_hedge': sin['margen_pct'],
            'amortiguacion_pp': con['margen_pct'] - sin['margen_pct'],
            'pct_importado': pct_importado,
            'fx_relativo': fx / fx_base}


def exposicion_cambiaria(precio_fob_cad: float, fx: float, fx_base: float,
                         costo_produccion_cop: float, pct_importado: float,
                         costo_logistico_cop: float,
                         costos_accesorios_pct: float = 0.0,
                         pass_through_flete: float = 1.0,
                         choque: float = 0.01) -> float:
    """Puntos de margen que gana o pierde el producto por cada 1% de movimiento
    del COP/CAD, por diferencia centrada alrededor de `fx`.

    Es el unico indicador del modelo que discrimina de verdad entre los diez
    productos con los datos disponibles, porque depende de `pct_importado`
    (tabla_B9, dato por producto) y no del ratio de costo, que para siete de los
    diez es un supuesto de grado C. Menor valor = mejor cobertura natural.
    """
    comun = (fx_base, costo_produccion_cop, pct_importado, costo_logistico_cop,
             costos_accesorios_pct, pass_through_flete)
    lo = margen(precio_fob_cad, fx * (1 - choque), *comun)['margen_pct']
    hi = margen(precio_fob_cad, fx * (1 + choque), *comun)['margen_pct']
    return (hi - lo) / 2


def vulnerabilidad_relativa(margen_cop: float, ingreso_cop: float,
                            var_horizonte: float) -> float:
    """Perdida de cola del horizonte de cobro como % del margen propio del producto.

    Responde la pregunta de presupuesto que el VaR en % de ingreso no responde:
    con dinero para cubrir solo unos pocos productos, cuales primero. Dos
    productos con identico VaR sobre ingreso son muy distintos si uno gana 30% de
    margen y el otro 4%.

    Devuelve NaN si el margen no es positivo: sin margen que proteger, la razon
    no tiene lectura economica.
    """
    if margen_cop <= 0:
        return float('nan')
    return abs(var_horizonte) * ingreso_cop / margen_cop * 100
