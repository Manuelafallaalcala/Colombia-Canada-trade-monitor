# Sección 5. Análisis financiero: riesgo cambiario COP/CAD y rentabilidad exportadora

**Working Paper MIC-CC — Monitor de Inteligencia Comercial Colombia–Canadá**
ODEM · Universidad EAN · Bogotá, 2026

Autora: Manuela Alcalá

---

> **Nota sobre la fecha de corte.** El modelo que sustenta esta sección descarga las series
> cambiarias en vivo desde el Banco de la República y el Bank of Canada. Las cifras que se citan
> corresponden a la ejecución del **11 de septiembre de 2026**, sobre una serie diaria de 2.336
> observaciones que cubre del 3 de enero de 2014 al 11 de septiembre de 2026. Al reejecutar el
> modelo en otra fecha, los niveles cambiarios, los escenarios y la clasificación de riesgo cambian;
> las conclusiones estructurales no.

---

## 5.1 Marco conceptual

El peso colombiano y el dólar canadiense **no se cotizan uno contra otro** en ningún mercado
líquido. Un exportador colombiano que factura en CAD no encuentra un precio COP/CAD publicado por su
banco central: encuentra dos precios contra el dólar estadounidense. El tipo de cambio relevante para
su negocio hay que construirlo como **tasa cruzada**:

$$\text{COP/CAD} = \frac{\text{COP/USD}}{\text{CAD/USD}}$$

donde el numerador es la Tasa Representativa del Mercado (TRM) que calcula y publica el Banco de la
República, y el denominador la cotización diaria del Bank of Canada.

Esta construcción tiene una consecuencia que el análisis debe tomar en serio: el COP/CAD hereda la
volatilidad de **dos** mercados, no de uno. Un movimiento del USD/CAD por razones enteramente
canadienses —el precio del crudo WTI, una decisión de tasas del Bank of Canada— altera los ingresos
en pesos de un exportador colombiano que nunca miró ese mercado.

La relevancia práctica es directa. El exportador vende en CAD y paga en COP: nómina, arriendo,
insumos nacionales, transporte interno. Entre el momento en que pacta el precio y el momento en que
cobra median típicamente entre 30 y 90 días, y en esa ventana el tipo de cambio se mueve. La pregunta
que esta sección responde para cada uno de los diez productos del Top 10 es cuánto de su margen
sobrevive a ese movimiento cuando el movimiento es adverso, y qué instrumentos tiene a mano para
protegerse antes de que ocurra.

---

## 5.2 La serie COP/CAD y su volatilidad

**[Insertar Figura 4 — `outputs/figures/figura_04_copcad_volatilidad.png`]**

La serie construida para el período 2014–2026 muestra tres fases claramente distinguibles. Una
**devaluación sostenida entre 2014 y 2016**, en la que el COP/CAD pasó de 1.740 a 2.466 (+41,7 %),
asociada al desplome del precio internacional del petróleo y su efecto sobre los ingresos de divisas
de Colombia. Un **período de alta turbulencia entre 2020 y 2022**, con el choque abrupto de la
pandemia y luego el ciclo de alzas de tasas de la Reserva Federal. Y una **apreciación prolongada del
peso desde finales de 2022**, que continúa hasta el cierre de la serie y que sitúa el COP/CAD en
2.243,52 el 11 de septiembre de 2026, un 9,6 % por debajo de su propia media móvil de 90 días
(2.481,14).

Ese último dato merece subrayarse: **el mercado ya está operando cerca del escenario que el modelo
califica de pesimista** (2.208,52). No se trata de un riesgo hipotético a futuro sino de una
condición vigente.

El panel inferior de la Figura 4 muestra la volatilidad rodante a 90 días. Los picos coinciden con
los episodios documentados en la `tabla_B6`, en particular con el choque de marzo de 2020. La
volatilidad anualizada del período completo es de **13,94 %**.

### Una corrección metodológica con efecto material

Esa cifra de 13,94 % difiere de la que arrojaba la primera versión del modelo (16,55 %), y la
diferencia no es de estimación sino de **alineación temporal de las fuentes**. La TRM vigente el día
*D* se calcula con las operaciones del día hábil *D−1*, mientras que la cotización del Bank of Canada
del día *D* refleja el mercado de *D*. Cruzarlas por fecha nominal empareja dos días de mercado
distintos e introduce en los retornos una diferencia que no corresponde a ningún movimiento cambiario
real.

Corregir el rezago reduce la volatilidad medida en **262 puntos básicos**. Es decir: cerca de una
sexta parte de la volatilidad que el modelo original atribuía al riesgo cambiario del par era **ruido
de emparejamiento de fechas**. Toda medida de riesgo derivada de esa serie —VaR, Expected Shortfall,
escenarios— estaba inflada en la misma proporción.

---

## 5.3 Valor en Riesgo y calibración del modelo

La Tabla 04 resume los indicadores de riesgo:

| Indicador | Valor |
|---|---|
| Volatilidad anualizada | 13,94 % |
| VaR 1 día, 95 % | −1,30 % |
| VaR 1 día, 99 % | −2,32 % |
| Expected Shortfall 95 % | −1,93 % |
| VaR 30 días, 95 % (empírico) | −6,65 % |
| VaR 60 días, 95 % (empírico) | −9,50 % |
| VaR 90 días, 95 % (empírico) | −11,64 % |

**Lectura práctica.** Un exportador que despacha hoy y cobra en 90 días enfrenta, con 95 % de
confianza, una pérdida cambiaria máxima de **11,64 %** del valor de su factura. Sobre una exportación
de 50.000 CAD, son unos 14,5 millones de pesos que pueden evaporarse sin que el exportador haya hecho
nada mal: solo por esperar el pago.

### Por qué el VaR multihorizonte es empírico y no escalado

La práctica habitual escala el VaR de un día por la raíz del horizonte. Ese escalado es exacto
únicamente bajo retornos independientes e idénticamente distribuidos de distribución estable, cuyo
caso canónico es la normal. **El propio modelo rechaza esa premisa**: el estadístico de Jarque-Bera
es de 996,6 con *p* < 10⁻²¹⁶, con asimetría de +0,342 y curtosis en exceso de +3,126. La distribución
de los retornos del COP/CAD tiene colas considerablemente más pesadas que una normal.

Usar √T sobre una serie que rechaza la normalidad no es una aproximación conservadora: en esta serie
**sobreestima el cuantil entre 6,3 % y 7,4 %** según el horizonte. Por eso el modelo reporta el
cuantil empírico del retorno acumulado a *T* días como método primario, y conserva el escalado √T
solo como referencia, con su sesgo medido.

Un matiz que suele omitirse y que aquí se reporta: las ventanas de *T* días **se solapan**, de modo
que las 2.246 observaciones disponibles a 90 días equivalen a apenas **25 ventanas independientes**.
El VaR a 90 días es una estimación con mucha menos información detrás de la que sugiere el tamaño
nominal de la muestra, y debe interpretarse con la incertidumbre correspondiente.

### Validación fuera de muestra

El backtest de Kupiec se ejecuta **sin look-ahead**: el VaR pronosticado para el día *t* usa
únicamente los retornos anteriores a *t*. Sobre 2.083 observaciones se registran **124 violaciones
(5,95 %)** frente al 5,00 % esperado, con un valor *p* de **0,0524**.

La calibración se acepta al 5 %, pero **por un margen estrecho**. Honestamente leído, el modelo
subestima ligeramente la frecuencia de eventos de cola, lo que es consistente con el rechazo de
normalidad ya documentado. Es un argumento adicional para tratar el VaR como una cota razonable y no
como una garantía.

Conviene señalar el contraste con la primera versión del modelo, que reportaba un backtest
*in-sample*: comparar una muestra contra su propio percentil arroja aproximadamente la tasa nominal
de violaciones por construcción, sin importar la calidad predictiva del modelo. Ese resultado no
validaba nada.

---

## 5.4 Escenarios cambiarios y márgenes por producto

**[Insertar Figura 5 — `outputs/figures/figura_05_margenes_escenarios.png`]**

Los escenarios no son porcentajes escogidos por conveniencia sino **cuantiles empíricos del retorno
acumulado a 90 días** de la propia serie: el pesimista es el percentil 5 y el optimista el percentil
95. Sobre una base de 2.481,14 (media móvil de 90 días), esto da un escenario pesimista de 2.208,52
(−10,99 %) y uno optimista de 2.819,30 (+13,63 %).

La asimetría de esos dos números —11 puntos abajo, 13,6 arriba— no es un error: refleja la asimetría
positiva de la distribución de retornos ya documentada en la sección anterior.

### Resultados

En el escenario base, **los diez productos tienen margen positivo**. En el escenario pesimista,
**ocho de los diez lo conservan**; rosas y pompones caen exactamente al punto de equilibrio (−0,01 %).

El rango entre productos es amplio: desde **39,4 %** en medicamentos corticosteroides hasta **3,8 %**
en flores frescas. Pero ese ordenamiento debe leerse con la advertencia que se desarrolla en la
sección 5.9: **siete de los diez ratios de costo son supuestos de trabajo, no datos verificados**, y
por eso la Figura 5 dibuja cada producto como una banda y no como un punto. Para medicamentos, por
ejemplo, la banda va de 24,4 % a 54,4 %.

### Diferencias entre rutas

**No hay diferencias relevantes entre Montreal y Vancouver**, y la razón es estructural más que
empírica. Los precios están cotizados FOB, de modo que bajo traslado completo del flete al comprador
el término logístico se cancela en la ecuación de equilibrio. La elección de puerto de destino
**no altera la economía del exportador** bajo este incoterm. La ruta sí afecta el margen porcentual,
porque el flete entra en el denominador del ingreso, pero el efecto es de segundo orden.

### La corrección de incoterm

**[Ver Figura 9 — `outputs/figures/figura_09_efecto_correcciones.png`]**

La primera versión del modelo restaba el flete internacional de un ingreso cotizado FOB. Bajo FOB el
flete lo paga el comprador; bajo CFR o CIF lo paga el exportador pero se lo factura dentro del
precio. En ninguno de los dos casos destruye margen — se estaba cobrando dos veces. Ese error
explicaba por sí solo el margen de −348 % que el modelo asignaba al carbón bituminoso y los márgenes
negativos de las flores.

El barrido de sensibilidad de la Tabla 12 mide la magnitud del supuesto: para las rosas, el margen al
tipo de cambio vigente pasa de **+0,5 % con traslado completo a −97,1 % si el exportador absorbe todo
el flete**. Ningún otro parámetro del modelo tiene esa palanca, y por eso el incoterm efectivo
encabeza la lista de datos pendientes.

---

## 5.5 Tipo de cambio de equilibrio y mapa de riesgo

**[Insertar Figura 6 — `outputs/figures/figura_06_mapa_riesgo_breakeven.png`]**

El tipo de cambio de equilibrio, o *breakeven*, es el nivel del COP/CAD al cual el margen de un
producto es exactamente cero. Por encima de él el exportador gana; por debajo, pierde. Se resuelve
analíticamente, incluyendo la cobertura natural, porque el costo importado depende del mismo tipo de
cambio que se está despejando.

| Producto | Breakeven | Colchón vs. spot | Semáforo robusto |
|---|---:|---:|:---:|
| Medicamentos corticosteroides | 813,0 | 63,8 % | Verde |
| Café sin tostar | 1.460,4 | 34,9 % | Verde |
| Medias/calcetines fibra sintética | 1.535,7 | 31,5 % | Verde |
| Filetes de trucha congelados | 1.727,8 | 23,0 % | Verde |
| Frutas tropicales (guayaba/mango) | 1.809,2 | 19,4 % | Verde |
| Accesorios tubería hierro/acero | 1.869,7 | 16,7 % | **Rojo** |
| Nueces y semillas preparadas | 1.897,0 | 15,4 % | **Rojo** |
| Carbón bituminoso | 2.192,8 | 2,3 % | **Rojo** |
| Flores frescas otras | 2.209,1 | 1,5 % | **Rojo** |
| Rosas frescas cortadas | 2.209,1 | 1,5 % | **Rojo** |

### Cómo debe leerse este semáforo, y cómo no

Tres advertencias son necesarias antes de que el lector extraiga conclusiones.

**Primera: el semáforo es robusto, no puntual.** Solo asigna Verde si el producto resiste en el
extremo desfavorable de su propia banda de incertidumbre de costos. Exigirlo cambia el color en **6
de 20 combinaciones producto-ruta**. Accesorios de tubería y nueces, por ejemplo, serían Verde
evaluados en su ratio central y son Rojo evaluados sobre toda su banda. Reportar el color puntual
cuando el parámetro que lo gobierna es un supuesto sería falsa precisión.

**Segunda: esta clasificación se calcula antes de la cobertura natural y del Drawback**, que solo
mejoran el margen. La cifra más completa del modelo es el margen final ajustado de la Tabla 11, no el
breakeven crudo de esta subsección.

**Tercera, y la más importante: el Rojo de rosas, pompones y carbón no significa lo mismo que un
resultado de negocio.** Estos tres productos combinan un ratio de costo alto —0,87 para las flores,
0,85 para el carbón— con un tipo de cambio actual excepcionalmente bajo en términos históricos. Su
colchón de 1,5 % a 2,3 % contra el spot dice que, **a los niveles cambiarios vigentes en septiembre
de 2026 y bajo los supuestos de costo declarados, estos productos operan al borde del punto de
equilibrio**. Es una afirmación condicionada, no un veredicto sobre la viabilidad estructural de
exportar flores o carbón a Canadá.

Vale la pena registrar que en la versión anterior del modelo el carbón bituminoso aparecía con un
breakeven que superaba el máximo histórico de la serie completa, un resultado que se leyó entonces
como un problema estructural de costos. Corregidos el incoterm y el modo de transporte —el carbón es
granel, no contenedor—, **su breakeven cae a 2.192,8 y su margen base es positivo (8,3 %)**. Aquel
diagnóstico era un artefacto del modelo, no una característica del producto.

---

## 5.6 Stress testing histórico

**[Insertar Figura 7 — `outputs/figures/figura_07_stress_testing.png`]**

La `tabla_B6` documenta cuatro episodios cambiarios reales. El modelo los aplica a los márgenes de
los diez productos, pero antes debe corregir un problema de fondo: **la tabla mide los episodios en
TRM (COP/USD) y el modelo original aplicaba esos porcentajes al COP/CAD**, que es una divisa distinta.

| Episodio | Tipo | Δ TRM | Δ COP/CAD real | Error |
|---|---|---:|---:|---:|
| Crisis petrolera 2014-2016 | Devaluación | +80,8 % | **+41,7 %** | 39,1 pp |
| Choque pandemia COVID-19 | Devaluación | +27,7 % | **+15,2 %** | 12,5 pp |
| Alza de tasas Fed 2022 | Devaluación | +36,5 % | **+24,0 %** | 12,6 pp |
| Apreciación del peso 2022-2024 | Apreciación | −25,6 % | **−24,7 %** | 1,0 pp |

El error de la sustitución llega a **39,1 puntos porcentuales** en el episodio de 2014-2016. La razón
es que en ese período el dólar canadiense también se debilitó frente al estadounidense, de modo que
la devaluación del peso *contra el CAD* fue apenas la mitad de la devaluación *contra el USD*. Un
stress test construido sobre la divisa equivocada mide un choque que el exportador nunca enfrentó.

### El hallazgo central de esta subsección

**El episodio más adverso para estos exportadores no es ninguna de las tres devaluaciones: es la
apreciación del peso de 2022-2024 (−24,7 %).**

Este resultado invierte la narrativa habitual sobre riesgo cambiario en Colombia, que asocia
devaluación con crisis. La inversión se explica por lo que son estos agentes: **generadores de
divisas**. Facturan en CAD y pagan sus costos en COP. Una devaluación del peso les *mejora* el
margen, porque cada dólar canadiense que cobran se convierte en más pesos. Es la apreciación la que
los comprime, y por eso el episodio 2022-2024 —que la prensa económica cubrió como una buena
noticia— es el escenario de estrés relevante para el Top 10 exportador.

### Implicación de política

Que el riesgo relevante para el sector exportador vaya en dirección contraria a la percepción pública
tiene una consecuencia concreta: los instrumentos de apoyo y las comunicaciones de política que se
activan ante episodios de devaluación **no llegan cuando este sector los necesita**. Una PYME
exportadora de flores tuvo su peor momento de margen en 2024, en pleno período de fortaleza del peso,
cuando el discurso público sobre riesgo cambiario estaba en su punto más bajo. El diseño de
mecanismos de cobertura accesibles debería atender esa asimetría.

---

## 5.7 Cobertura natural y costo de capital de trabajo

### Cobertura natural

Parte del costo de producción de estos exportadores está denominada en insumos importados, cuyo
precio en pesos escala con el mismo tipo de cambio que su ingreso. Cuando el peso se aprecia y el
ingreso en pesos cae, ese componente del costo cae también: es un **hedge genuino, incorporado en la
estructura de costos**, que no requiere contratar ningún instrumento financiero.

El modelo lo mide contra el contrafactual correcto —la misma empresa, con el mismo costo total, pero
enteramente nacional— porque compararlo contra otro producto mezclaría el efecto de la cobertura con
el de su estructura de costos. En el escenario pesimista, ruta Montreal:

| Producto | % importado | Margen sin hedge | Margen con hedge | Amortiguación |
|---|---:|---:|---:|---:|
| Nueces y semillas preparadas | 55 % | 1,21 % | 6,66 % | **+5,45 pp** |
| Filetes de trucha congelados | 55 % | 5,61 % | 10,84 % | +5,23 pp |
| Medias/calcetines fibra sintética | 55 % | 11,12 % | 16,04 % | +4,92 pp |
| Medicamentos corticosteroides | 65 % | 32,61 % | 37,01 % | +4,40 pp |
| Accesorios tubería hierro/acero | 40 % | 5,61 % | 9,42 % | +3,81 pp |
| Frutas tropicales | 30 % | 9,18 % | 11,67 % | +2,49 pp |
| Café sin tostar | 25 % | 24,68 % | 26,58 % | +1,90 pp |
| Rosas frescas cortadas | 30 % | −1,62 % | −0,01 % | +1,61 pp |
| Flores frescas otras | 30 % | −1,53 % | −0,01 % | +1,52 pp |
| Carbón bituminoso | 15 % | −0,85 % | 0,50 % | +1,35 pp |

Dos observaciones importan. La primera: **la cobertura natural es lo que mantiene a rosas, pompones
y carbón en el punto de equilibrio en vez de en pérdida** en el escenario pesimista. La segunda, que
suele omitirse: **el hedge es simétrico**. En el escenario optimista, esa misma cobertura *recorta* el
margen en 3,23 pp en promedio. No es un beneficio gratuito sino una reducción de varianza en ambas
direcciones, y presentarlo como lo primero confunde estabilidad con rentabilidad.

Este es también el indicador que mejor discrimina entre productos con la evidencia disponible, porque
depende de `pct_importado`, que es un dato por producto documentado en la `tabla_B9`, y no del ratio
de costo, que para siete de los diez es un supuesto.

### Costo de capital de trabajo

Entre el despacho y el cobro, el exportador tiene capital inmovilizado que debe financiar. El modelo
aplica ese costo sobre el **costo total ya desembolsado** —no sobre la utilidad esperada, que todavía
no existe— a la tasa de fondeo de una PYME.

Aquí fue necesaria una corrección de dos partes. La primera versión usaba el IBR, que es una tasa
**interbancaria** y no lo que paga una PYME, y además lo dividía entre 365 tratándolo como efectivo
cuando se cotiza **nominal base 360**. Convertido correctamente, el IBR de 11,19 % nominal equivale a
**12,01 % efectivo anual**; la tasa de fondeo PYME aplicada es de **19,19 % E.A.** (IBC crédito
ordinario), con el IBR como piso.

El efecto sobre el margen a 90 días, en el escenario base y ruta Montreal, va de **2,7 puntos
porcentuales** en medicamentos a magnitudes que **vuelven negativo el margen** de rosas (−0,27 %) y
pompones (−0,50 %). Para los productos de margen estrecho, el costo de esperar el pago no es un
detalle contable: es la diferencia entre ganar y perder.

---

## 5.8 Recomendaciones de cobertura cambiaria y Plan Vallejo

**[Insertar Figura 8 — `outputs/figures/figura_08_margen_bruto_vs_ajustado.png`]**

### La decisión de cobertura, planteada correctamente

La primera versión del modelo comparaba un costo cierto de cobertura contra un cuantil de cola al
5 % —magnitudes que no son comparables— y tomaba el valor absoluto de los puntos forward,
invirtiendo el signo del resultado económico. Con la magnitud del costo proporcional a *T* y la del
VaR proporcional a √T, la desigualdad **no podía invertirse a ningún horizonte**: la recomendación de
cubrirse estaba forzada por construcción, no obtenida de los datos.

El planteamiento correcto parte de la paridad cubierta de tasas de interés, con signo:

$$\frac{F}{S} - 1 = \frac{(1+i_{COP})^{t}}{(1+i_{CAD})^{t}} - 1$$

Con `i_COP` (12,01 % E.A.) muy por encima de `i_CAD` (2,25 %), el resultado es positivo: el forward
COP/CAD cotiza **sobre** el spot. **Un exportador que vende CAD a plazo cobra esa prima; no la
paga.** Lo que sí cuesta es el spread bid-ask del NDF, que el modelo original no incluía.

| Horizonte | Prima forward | Spread NDF | Valor esperado neto | Cola VaR eliminada |
|---|---:|---:|---:|---:|
| 30 días | +0,752 % | 0,750 % | **+0,002 %** | 6,65 % |
| 60 días | +1,510 % | 0,750 % | **+0,760 %** | 9,50 % |
| 90 días | +2,273 % | 0,750 % | **+1,523 %** | 11,64 % |

**Recomendación.** A 60 y 90 días, cubrirse tiene **valor esperado positivo y además elimina la
cola**: es una decisión favorable por partida doble, y el argumento es más fuerte cuanto mayor el
horizonte de cobro. A 30 días el valor esperado neto es de apenas 0,002 % — es decir,
**indistinguible de cero**, y enteramente dependiente de un spread NDF que es un supuesto de grado C.
A ese horizonte la recomendación debe formularse solo en términos de reducción de riesgo, no de valor
esperado.

Dos restricciones prácticas acompañan esta recomendación. El **monto mínimo de operación** es de
~USD 10.000 (Davivienda); el modelo trabaja por kilogramo y no puede determinar si un exportador
concreto lo alcanza, porque eso depende del volumen del embarque. Y la **prima del forward no es
dinero gratis**: refleja el diferencial de tasas, es decir, la compensación por mantener una posición
en la moneda de tasa alta. Cubrirse convierte una exposición cambiaria en una posición de tasa.

### Prioridad bajo presupuesto limitado

Tanto la cobertura natural como el costo-beneficio del forward son casi invariantes al producto por
construcción, porque ambos escalan con el ingreso. Para una PYME que solo puede cubrir parte de su
portafolio, el criterio útil es la **vulnerabilidad relativa**: la pérdida de cola a 90 días medida
como porcentaje del margen propio de cada producto.

Los tres primeros del ranking son **flores frescas (309 %), rosas (293 %) y carbón bituminoso
(141 %)**: en los tres, la pérdida de cola supera el margen completo. En el otro extremo,
medicamentos corticosteroides (30 %) y café (36 %) tienen margen suficiente para absorber el choque.
El criterio ordena de forma distinta al VaR sobre ingreso, que es idéntico para todos, y es el que
debería guiar la asignación de un presupuesto de cobertura acotado.

### Plan Vallejo / Drawback de IVA

El beneficio del Plan Vallejo requirió la corrección de mayor magnitud relativa de toda la auditoría.
La primera versión sumaba el **19 % completo** del costo importado al margen. Eso acredita un ahorro
sobre un costo que la propia base de costos del modelo nunca cargó, y desconoce que **las
exportaciones son exentas con derecho a devolución** (Arts. 481, 485, 489 y 850 del Estatuto
Tributario): ese IVA se recupera de todos modos.

Lo que el Plan Vallejo evita, en rigor, es **financiar** el IVA mientras se tramita la devolución. Su
valor es el del *float*:

$$\text{beneficio} = \text{IVA} \times C_i \times \left[(1+i)^{d/365} - 1\right]$$

Con 120 días de float al 19,19 % E.A., el beneficio real es **5,94 % del IVA, no el 100 %**: la
sobreestimación era de aproximadamente **17 veces**.

Corregido, el Drawback mejora el margen final **entre 0,00 y 0,50 puntos porcentuales** según el
producto. El máximo corresponde a nueces y semillas preparadas (+0,50 pp), trucha (+0,48 pp) y medias
de fibra sintética (+0,45 pp), los tres con 55 % de insumos importados y elegibilidad confirmada; el
mínimo, a carbón y accesorios de tubería, donde la elegibilidad figura como *no está claro* en la
`tabla_B3` y el modelo, por prudencia, no acredita beneficio alguno. Es un beneficio real y vale la
pena tramitarlo, pero **no cambia la viabilidad de ninguna operación**: para comparar, el costo de
capital de trabajo a 90 días erosiona entre 2,7 y 4,3 puntos porcentuales, casi un orden de magnitud
más. Presentar el Drawback como factor decisivo, que es lo que hacía la versión anterior,
distorsionaba la evaluación.

Aun así, el Drawback tiene una propiedad valiosa: **es el único ajuste del modelo que diferencia
productos por sí mismo**, porque depende de la participación de insumos importados de cada uno, que
es un dato documentado y no un supuesto.

### Recomendaciones de política para PYMEs exportadoras

**Primera.** El riesgo cambiario relevante para el sector exportador colombiano hacia Canadá es la
**apreciación del peso**, no la devaluación. Los mecanismos de apoyo y las comunicaciones de política
que se activan ante episodios de devaluación no atienden a este sector; el diseño institucional
debería reconocer esa asimetría.

**Segunda.** Para horizontes de cobro de 60 y 90 días, la cobertura con forward o NDF tiene valor
esperado positivo además de eliminar la cola. La barrera no es el precio del instrumento sino el
**acceso**: el monto mínimo de operación deja fuera a los exportadores más pequeños. Un mecanismo de
agregación de tickets —a través de gremios o de una entidad de segundo piso— convertiría un
instrumento hoy inaccesible en uno viable para el segmento que más lo necesita.

**Tercera.** Los productos de margen estrecho —flores, rosas, carbón— son simultáneamente los más
vulnerables y los que menos capacidad tienen de absorber el costo de cubrirse. Cualquier programa de
apoyo con presupuesto limitado debería priorizarlos usando el criterio de vulnerabilidad relativa, no
el VaR sobre ingreso, que no los distingue de los demás.

---

## 5.9 Limitaciones del análisis

Esta subsección no es un formalismo. Condiciona la lectura de todo lo anterior.

Cada parámetro del modelo lleva un **grado de evidencia**: **A** dato duro de fuente primaria
verificable y fechada, **B** dato gremial cuantificado por inferencia razonada, **C** supuesto de
trabajo. **Catorce de los veinticuatro parámetros inventariados son grado C**, y el inventario
incluye deliberadamente los supuestos de modelado —traslado del flete, perfil del exportador, payload
por clase de densidad— que mueven el resultado tanto como cualquier dato.

De ahí se derivan tres restricciones explícitas sobre lo que este trabajo puede afirmar:

1. **No se publica ningún ranking de rentabilidad entre productos.** Siete de los diez ratios de
   costo son grado C. Un ranking construido sobre ellos sería un artefacto del precio por kilogramo,
   no un hallazgo. El ordenamiento de la sección 5.4 se presenta como banda y con su grado de
   evidencia visible precisamente para impedir esa lectura.

2. **Nueve de los diez precios son valores unitarios de Trade Map 2024**, no precios de mercado de
   2026. Solo el café tiene precio con fuente primaria fechada. La incoherencia temporal que la
   auditoría corrigió en el tipo de cambio persiste en los precios.

3. **El supuesto de mayor palanca del modelo, el traslado del flete, no está verificado contra
   contratos reales.** Su barrido mueve el margen de las rosas entre +0,5 % y −97,1 %.

Cerrar estos vacíos es **recolección de datos, no modelación**. El inventario completo —qué falta,
qué institución lo tiene, qué desbloquea cada dato y en qué orden conviene pedirlos— está en
`docs/04_datos_pendientes.md`. Tres de los siete vacíos se cierran con sendas llamadas telefónicas y
cambian el modelo más que cualquier trabajo adicional sobre el código.

---

## Referencias

Asocolflores. (2026). *Estructura de costos de la floricultura colombiana* [Información gremial
citada en prensa sectorial]. Contexto Ganadero.
https://www.contextoganadero.com/gremialidad/pese-a-aumento-de-la-demanda-los-costos-de-la-floricultura-van-al-alza-asocolflores

Asociación Nacional de Empresarios de Colombia. (2024). *Observatorio farmacéutico*. ANDI.
https://www.andi.com.co

Banco de la República. (2026). *Indicador Bancario de Referencia (IBR) — serie histórica diaria*
[Servicio SDMX]. https://totoro.banrep.gov.co/nsi-jax-ws/rest/data/ESTAT,DF_IBR_DAILY_HIST,1.0/all/ALL

Banco de la República. (2026). *Tasa Representativa del Mercado (TRM) — serie histórica*
[Estadísticas económicas]. https://suameca.banrep.gov.co/estadisticas-economicas-back/reporte-dv.html?path=tasa_representativa_del_mercado_trm

Banco de la República. (2026). *Forward, cobertura cambiaria y non-delivery forwards (NDF)*
[Glosario]. https://www.banrep.gov.co/es/glosario/forward-cobertura-cambiaria-non-delivery-forwards-ndf

Bancolombia. (2026). *Forward de divisas*.
https://www.bancolombia.com/negocios/productos/derivados/forward-divisas

Bank of Canada. (2026). *Daily exchange rates* [Valet API, series FXUSDCAD e IEXE0101].
https://www.bankofcanada.ca/rates/exchange/daily-exchange-rates/

Bank of Canada. (2026). *Target for the overnight rate* [Valet API, serie V39079].
https://www.bankofcanada.ca/valet/observations/V39079/json

BBVA Colombia. (2026). *Coberturas y derivados*.
https://www.bbva.com.co/empresas/productos/coberturas-y-derivados.html

Congreso de la República de Colombia. (2026). *Estatuto Tributario, Arts. 428, 481, 485, 489, 850 y
855*. Secretaría del Senado.
http://www.secretariasenado.gov.co/senado/basedoc/estatuto_tributario_pr017.html

Davivienda. (2026). *Coberturas cambiarias para empresas*. https://www.davivienda.com

Dirección de Impuestos y Aduanas Nacionales. (2020). *Resolución 1055 de 2020, Ministerio de
Comercio, Industria y Turismo* [Reglamentación del régimen Plan Vallejo].
https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_mincomercioit_1055_2020.htm

Fedeacua. (2026). *Estructura de costos en piscicultura: participación del alimento balanceado*.
https://acuicola.co

Federación Nacional de Cafeteros de Colombia. (2026). *Precio interno de compra del café pergamino
seco* [Boletín diario, 27 de julio de 2026]. https://www.federaciondecafeteros.org

Fenalcarbón. (2026). *Situación del sector carbonífero colombiano*. https://fenalcarbon.org.co

International Coffee Organization. (2026). *Coffee prices*. https://www.ico.org/prices/po

International Trade Centre. (2025). *Trade Map: trade statistics for international business
development* [Colombia como exportador, Canadá como importador, 2024]. https://www.trademap.org

Jarque, C. M., & Bera, A. K. (1980). Efficient tests for normality, homoscedasticity and serial
independence of regression residuals. *Economics Letters, 6*(3), 255–259.
https://doi.org/10.1016/0165-1765(80)90024-5

Kupiec, P. H. (1995). Techniques for verifying the accuracy of risk measurement models. *The Journal
of Derivatives, 3*(2), 73–84. https://doi.org/10.3905/jod.1995.407942

Ministerio de Agricultura y Desarrollo Rural. (2025). *Lineamientos Asohofrucol* [Sistema de
Información de Gestión y Desempeño de Organizaciones de Cadenas].
https://sioc.minagricultura.gov.co

Portafolio. (2024). *Peso colombiano se revalorizó frente al dólar más de 21 % entre enero de 2023 y
enero de 2024*. https://www.portafolio.co/economia/finanzas/peso-colombiano-se-revalorizo-frente-al-dolar-mas-de-21-entre-enero-de-2023-y-enero-de-2024-595566

Portafolio. (2021). *Una década de crisis petrolera y devaluación*.
https://www.portafolio.co/economia/una-decada-de-crisis-petrolera-y-devaluacion-536771

SeaRates. (2026). *Logistics Explorer: tarifas de flete marítimo Cartagena–Montreal y
Cartagena–Vancouver*. https://www.searates.com

---

*ODEM · Universidad EAN · Bogotá, 2026*
