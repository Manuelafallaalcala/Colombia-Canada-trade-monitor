

**MONITOR DE INTELIGENCIA COMERCIAL**

**COLOMBIA \- CANADA**

Guia Exhaustiva Paso a Paso de la Fase 4 Financiera

Edicion extendida: cada tarea desglosada en sub-pasos, verificaciones y resolucion de problemas

Responsable unica: Manuela

ODEM \- Observatorio de Economia y Mercados  |  Universidad EAN  |  Bogota, junio 2026

> ## Nota de vigencia — septiembre de 2026
>
> Esta guía es el **documento metodológico y de aprendizaje** de la Fase 4: explica los conceptos
> financieros desde cero, justifica cada decisión de método y sirve de referencia para entender por
> qué el modelo hace lo que hace. En ese papel sigue plenamente vigente, y su glosario final es el
> glosario del proyecto.
>
> Lo que ya **no** describe con exactitud es la mecánica operativa, porque el proyecto se ejecutó y
> luego se consolidó. Al leerla conviene tener presentes estas equivalencias:
>
> | La guía dice | En el repositorio es |
> |---|---|
> | `MIC-CC/dataraw/` o `data/raw/` | `data/raw/` |
> | `notebooks/04_financial_model.ipynb` (y sus versiones 05 y 06) | `notebooks/mic_cc_modelo_financiero.ipynb`, uno solo |
> | `MIC-CC/outputs/tables/`, 8 tablas del Bloque B | `outputs/tables/`, 21 tablas |
> | 5 figuras | 6 figuras en `outputs/figures/` |
> | Google Colab y Google Drive | Entorno local con `.venv`, y git como control de versiones |
> | Cronograma de 24 días en tres bloques | Ejecutado; el cronograma queda como registro de método |
>
> **Dónde está cada cosa ahora:**
>
> - **Qué hace el proyecto y cómo reproducirlo** → [`../README.md`](../README.md)
> - **Qué se corrigió respecto de la primera versión, y por qué** →
>   [`02_auditoria_y_correcciones.md`](02_auditoria_y_correcciones.md)
> - **Los resultados redactados en prosa académica, con referencias APA** →
>   [`03_working_paper_seccion5.md`](03_working_paper_seccion5.md)
> - **Qué datos siguen faltando y a quién pedírselos** →
>   [`04_datos_pendientes.md`](04_datos_pendientes.md)
> - **Qué hacer con los resultados, producto por producto, y qué hallazgos ya se pueden usar** →
>   [`05_conclusiones_y_recomendaciones.md`](05_conclusiones_y_recomendaciones.md)
>
> **Dos advertencias sobre el contenido de esta guía.** La primera: el **factor de costo único de
> 0,60** que aparece en la Tarea 5 y en la Etapa 6 fue reemplazado por una banda de costos con grado
> de evidencia por producto; la propia guía lo declaraba como limitación no resuelta y ya lo está,
> parcialmente. La segunda: la guía instruye restar el flete internacional del ingreso, y eso es
> incorrecto sobre precios cotizados FOB — la corrección y su efecto están documentados como error
> nº 1 de la auditoría.
>
> La `tabla_B5` de la Tarea 5, que la guía describe como una verificación manual en Excel, se
> reproduce ahora de forma programática en el cuaderno (sección 4) para que sea auditable, con sus
> cuatro verificaciones de calidad convertidas en aserciones. Reproduce exactamente el ejemplo
> numérico de la sección 6.5.4: 40,0 % / 45,5 % / 29,4 %.

---

# **1\. Proposito y forma de uso de esta guia**

Esta es la version extendida y exhaustiva del plan individual de la Fase 4 del Monitor de Inteligencia Comercial Colombia-Canada (MIC-CC). Asume que Manuela ejecuta toda la fase sola, sin asistentes, y desglosa cada tarea no solo en pasos, sino en sub-pasos, con el detalle de que hacer en cada clic, que esperar ver en la pantalla en cada momento, como verificar que el resultado de cada accion es correcto antes de continuar, y que hacer especificamente si algo no funciona como se describe.

La diferencia respecto a una guia resumida es la siguiente: una guia resumida dice 'descargar la TRM del Banco de la Republica'. Esta guia dice que pagina abrir, que escribir en cada campo, que boton presionar, que formato de archivo seleccionar, como se ve un archivo correcto, como se ve un archivo con errores, y que hacer en cada uno de los escenarios donde algo no sale como se espera. La logica detras de este nivel de detalle es simple: cuando un paso no esta completamente especificado, la persona que lo ejecuta tiene que decidir por su cuenta que hacer, y esas pequenas decisiones acumuladas son las que generan inconsistencias entre una tarea y otra, o entre un dia de trabajo y el siguiente.

Esta guia no asume ningun conocimiento previo de finanzas internacionales, programacion, ni de las paginas web que se van a usar. Cada termino tecnico se explica la primera vez que aparece, y los terminos que se repiten estan recogidos en el glosario final.

Como usar esta guia en la practica: imprimir o tener abierta la seccion correspondiente a la tarea del dia, seguir los sub-pasos en el orden exacto en que aparecen, y solo marcar una tarea como completa despues de pasar por la verificacion de calidad que cierra cada seccion. No se recomienda saltar sub-pasos aunque parezcan obvios, porque la mayoria de los errores en este tipo de trabajo ocurren precisamente en los pasos que parecen mas simples y por eso se hacen con menos atencion.

# **2\. Contexto completo del proyecto MIC-CC y la Fase 4**

## **2.1 Que es el MIC-CC**

El Monitor de Inteligencia Comercial Colombia-Canada (MIC-CC) es una herramienta analitica de acceso abierto, construida bajo el sello del ODEM (Observatorio de Economia y Mercados) de la Universidad EAN. Su proposito es ayudar a exportadores colombianos, en particular a pequenas y medianas empresas (PYMEs), a tomar decisiones informadas sobre si exportar, que exportar, y como gestionar los riesgos de exportar hacia Canada.

La razon de ser de este tipo de herramienta es que las grandes empresas exportadoras suelen tener departamentos de tesoreria, analistas de riesgo cambiario, y acceso a bancos de inversion que les dan este tipo de analisis de forma personalizada. Una PYME exportadora normalmente no tiene acceso a ese tipo de analisis, ni el presupuesto para contratarlo. El MIC-CC busca cerrar esa brecha, ofreciendo de forma gratuita y publica un nivel de analisis que normalmente solo esta disponible para empresas grandes.

El marco legal de referencia es el Tratado de Libre Comercio Colombia-Canada (TLCC), vigente desde el 15 de agosto de 2011\. Este tratado elimino o redujo de forma progresiva los aranceles entre los dos paises para la gran mayoria de productos. A la fecha de este documento (2026), el tratado ya completo todos sus periodos de desgravacion para los productos del Top 10 que se analizan en este monitor.

## **2.2 Las tres dimensiones del proyecto**

**Dimension comercial (completada en fases anteriores)**

Identifico, usando datos de comercio exterior, los productos colombianos que tienen mayor Ventaja Comparativa Revelada (VCR) hacia Canada. La VCR es un indicador que compara la participacion de un producto en las exportaciones totales de Colombia hacia Canada, contra la participacion de ese mismo producto en las exportaciones mundiales totales hacia Canada. Un valor de VCR mayor a 1 indica que Colombia exporta ese producto a Canada en una proporcion mayor a la que le correspondria si exportara en la misma proporcion que el resto del mundo, lo cual sugiere una ventaja competitiva real. Con este indicador se identificaron los 10 productos del Top 10 que se trabajan en toda la Fase 4\.

**Dimension logistica (completada en fases anteriores)**

Calculo los costos y tiempos de transporte para exportar desde el puerto de Cartagena hacia los dos puertos canadienses mas relevantes para el comercio bilateral: Montreal (en la costa este de Canada, conectado a Cartagena por rutas directas o con escala) y Vancouver (en la costa oeste, normalmente con mas escalas o rutas mas largas desde Cartagena). Estos costos logisticos (flete maritimo, seguros, manejo portuario, transporte terrestre interno) son uno de los insumos que se usan en el calculo de margenes de la Fase 4\.

**Dimension financiera (Fase 4, objeto de esta guia)**

Mide como el riesgo cambiario entre el peso colombiano (COP) y el dolar canadiense (CAD) afecta la rentabilidad real de exportar cada uno de los 10 productos del Top 10\. No se limita a calcular un numero de riesgo: construye un sistema completo que responde preguntas practicas para un exportador, como hasta donde puede caer el tipo de cambio antes de perder dinero, que pasaria si se repite una crisis cambiaria como las que Colombia ya vivio, si conviene cubrirse con un instrumento financiero, y cuanto cuesta financiar la espera del pago de una exportacion.

## **2.3 Por que los aranceles ya no son relevante para este analisis**

Antes de iniciar esta fase, la fase comercial confirmo que los 10 productos del Top 10 ya estan completamente desgravados bajo el TLCC. Esto significa que el arancel que paga Canada al importar estos productos colombianos es 0%, tanto bajo el regimen general (Nacion Mas Favorecida, NMF) como bajo el TLCC especificamente. Por esa razon, esta guia no incluye ninguna tarea de investigacion de tablas arancelarias, lo cual hubiera sido necesario en una fase anterior del proyecto o si los productos no estuvieran desgravados.

Sin embargo, que el arancel de exportacion sea 0% no significa que no haya ningun costo de tipo fiscal o aduanero relevante. Existe un beneficio distinto, llamado regimen de Plan Vallejo de importacion (tambien conocido como Drawback de IVA), que permite a un exportador recuperar el IVA (Impuesto al Valor Agregado, actualmente 19% en Colombia) que pago al importar insumos que luego incorpora en un producto que exporta. Este beneficio si se investiga en esta guia, en la Tarea 3 del Bloque A, porque mejora el margen real del exportador aunque no aparezca en ninguna tabla de aranceles.

## **2.4 Los 10 productos del Top 10**

Estos son los 10 productos que efectivamente se investigaron en el Bloque A y se calcularon en el Bloque B de esta fase, con su codigo del Sistema Armonizado (HS, por sus siglas en ingles) a 6 digitos, tal como aparecen en `tabla_B3_drawback_iva.xlsx`, `tabla_B4_precios_referencia.xlsx` y `tabla_B9_estructura_costos.xlsx`:

1\. Cafe sin tostar, sin descafeinar (HS 090111\)

2\. Carbon bituminoso, pulverizado o no, sin aglomerar (HS 270112\)

3\. Frutas comestibles: guayabas, mangos y mangostanes, frescos o secos (HS 080450\)

4\. Flores frescas cortadas, distintas de rosas, claveles, orquideas, crisantemos o lirios (HS 060319\)

5\. Medicamentos que contienen hormonas corticosteroides, sus derivados o analogos estructurales, acondicionados para la venta al por menor (HS 300432\)

6\. Calceteria sin suela aplicada, de fibras sinteticas, de punto (HS 611596\)

7\. Accesorios de tuberia de fundicion, hierro o acero \-codos, curvas, manguitos roscados\-, distintos de acero inoxidable (HS 730792\)

8\. Filetes de trucha congelados (HS 030482\)

9\. Frutos de cascara y otras semillas preparados, incluso con adicion de azucar u otro edulcorante (HS 200819\)

10\. Rosas frescas cortadas (HS 060311\)

**Nota de trazabilidad (correccion de julio de 2026):** esta seccion documentaba antes una lista distinta, que incluia Carbon de coque (HS 270400\) en vez de Carbon bituminoso, Crisantemos frescos cortados (HS 060312\) y Pantalones de algodon (HS 620462\) y Aceite de palma en bruto (HS 151110\) en lugar de tres de los productos de arriba, y no mencionaba Accesorios de tuberia de hierro/acero, Filetes de trucha congelados ni Frutos de cascara y semillas preparados. Una auditoria del proyecto encontro que los tres archivos de origen del Bloque A y la propia Etapa 6 del notebook de Python (que ya documentaba esta discrepancia en su celda de apertura) coinciden en que la lista de 10 productos de arriba es la que realmente proviene de la fase comercial (identificacion por Ventaja Comparativa Revelada) y sobre la que se construyo todo el Bloque B. Se corrige esta seccion para que el documento coincida con los datos reales del proyecto. Cualquier mencion a "Carbon de coque", "Crisantemos", "Pantalones de algodon" o "Aceite de palma en bruto" en versiones previas de este documento, del Working Paper o de comunicaciones del proyecto debe entenderse como reemplazada por la lista de arriba; si en algun momento se investigaron datos reales para esos cuatro productos originales, esos archivos deben tratarse como material de una fase descartada, no como insumo valido de la Fase 4\.

Estos 10 productos son el hilo conductor de toda esta guia: cada tarea de recoleccion de datos, y cada etapa del modelo de Python, trabaja sobre estos mismos 10 productos.

## **2.5 Que produce esta fase al final**

Al cerrar la Fase 4, deben existir cuatro tipos de productos finales, todos descritos con detalle en sus secciones correspondientes de esta guia:

Un notebook de Python (04\_financial\_model.ipynb) que corre de principio a fin sin errores, alojado en Google Colab y respaldado en Google Drive.

Quince tablas de resultados en formato Excel (siete del Bloque A: tabla\_B3 a tabla\_B9, y ocho del Bloque B: tabla\_04 a tabla\_11), que documentan cada paso del analisis, desde los datos crudos hasta los resultados finales ajustados.

Cinco figuras en formato PNG, que visualizan los resultados mas importantes del modelo.

Un repositorio publico en GitHub que aloja el codigo, las tablas y las figuras, junto con documentacion en ingles que permite a cualquier persona entender y reproducir el analisis.

Una seccion completa del Working Paper academico del proyecto, con ocho subsecciones que explican en prosa, con referencias academicas, todo lo que el modelo encontro.

# **3\. Conceptos clave explicados en profundidad**

Esta seccion explica cada concepto con mayor profundidad que en la version resumida del plan. Para cada concepto se incluye: la definicion, por que importa para un exportador real, como se calcula (si aplica), y un ejemplo numerico completo. Leer toda esta seccion antes de iniciar cualquier tarea del Bloque A es la base para que el resto de la guia tenga sentido.

## **3.1 Tasa Representativa del Mercado (TRM)**

La TRM es el precio oficial del dolar de los Estados Unidos (USD) expresado en pesos colombianos (COP). La calcula y publica el Banco de la Republica de Colombia todos los dias habiles, tomando como base el promedio ponderado de las operaciones de compra y venta de dolares que se hicieron el dia anterior entre entidades financieras autorizadas en Colombia.

***Por que importa la TRM para este proyecto***

La TRM es la primera pieza del calculo del tipo de cambio COP/CAD, que es el verdadero protagonista de todo el modelo financiero. Sin la TRM, no se puede construir esa serie.

***Ejemplo numerico***

Si la TRM publicada para un dia especifico es 4.150,32, significa que ese dia, un dolar americano se cambiaba, en promedio, por 4.150,32 pesos colombianos. Si una empresa colombiana necesita comprar 10.000 dolares americanos ese dia para pagar una importacion, necesitaria aproximadamente 41.503.200 pesos colombianos (10.000 x 4.150,32).

## **3.2 Tipo de cambio COP/CAD (tasa cruzada)**

El COP/CAD es el precio de un dolar canadiense (CAD) expresado en pesos colombianos (COP). A diferencia de la TRM, este tipo de cambio no se publica directamente en ningun mercado financiero colombiano ni canadiense, porque el volumen de operaciones directas entre peso colombiano y dolar canadiense es muy bajo comparado con las operaciones de cada moneda contra el dolar americano. Por eso, el COP/CAD se calcula de forma indirecta, como lo que en finanzas se llama una tasa cruzada (cross rate).

***Como se calcula (version corregida, julio de 2026 — ver nota de correccion al final de esta seccion)***

Se toman dos tipos de cambio que si se publican de forma directa: la TRM (COP/USD), y el dato que publica la API del Bank of Canada bajo el nombre de serie FXUSDCAD. Es fundamental entender que ese dato de Bank of Canada, pese a llamarse "USD/CAD", esta expresado como cuantos DOLARES CANADIENSES cuesta UN dolar americano (tipicamente entre 1,25 y 1,45): es una cifra CAD-por-USD, no USD-por-CAD. Para construir la tasa cruzada hay que invertir ese dato primero, y multiplicar despues:

USD\_por\_CAD \= 1 / FXUSDCAD (el numero que publica el Bank of Canada)

COP/CAD \= TRM (COP/USD) x USD\_por\_CAD

***Por que hay que invertir el dato del Bank of Canada antes de multiplicar***

Esto suele confundir a quien no esta familiarizado con tipos de cambio cruzados, y de hecho una version anterior de esta misma guia lo explicaba al reves — ver la nota de correccion al final de esta seccion. La logica correcta es la siguiente: la TRM dice cuantos pesos colombianos cuesta UN dolar americano. Lo que se necesita para la tasa cruzada es cuantos DOLARES AMERICANOS cuesta UN dolar canadiense (no cuantos dolares canadienses cuesta un dolar americano, que es lo que el Bank of Canada publica directamente). Como el dolar canadiense vale MENOS que el dolar americano, cuesta MENOS de 1 dolar americano comprar 1 dolar canadiense — por eso hay que invertir (1 dividido entre el dato del Bank of Canada) antes de multiplicar. Una vez invertido, el principio para convertir unidades es el mismo que en cualquier otro contexto: si 1 kilo cuesta 2 dolares, y 1 dolar cuesta 4.000 pesos, entonces 1 kilo cuesta 2 x 4.000 \= 8.000 pesos.

***Ejemplo numerico completo***

TRM (COP/USD) \= 4.000. Dato publicado por el Bank of Canada (FXUSDCAD) \= 1,35 (cuesta 1,35 dolares canadienses comprar 1 dolar americano). Se invierte primero: USD\_por\_CAD \= 1 / 1,35 \= 0,7407 (1 dolar canadiense cuesta 0,7407 dolares americanos). Entonces: COP/CAD \= 4.000 x 0,7407 \= 2.963. Esto significa que un dolar canadiense vale aproximadamente 2.963 pesos colombianos ese dia.

Verificacion logica del resultado: el dolar canadiense, historicamente, vale menos que el dolar americano (1 CAD \= aproximadamente 0,70 a 0,75 USD). Por lo tanto, el COP/CAD siempre debe ser un poco menor que la TRM (COP/USD), porque el dolar canadiense vale algo menos que el dolar americano. En el ejemplo, 2.963 es efectivamente menor que la TRM de 4.000, como debe ser. Si en algun calculo el COP/CAD sale mayor que la TRM, hay un error en la formula o en los datos de entrada (el error mas comun es multiplicar directamente por el dato del Bank of Canada sin invertirlo primero), y hay que revisar antes de continuar.

**Nota de correccion (julio de 2026):** una version anterior de esta seccion instruia a multiplicar la TRM directamente por el dato del Bank of Canada sin invertirlo, y su propio ejemplo numerico (TRM 4.000 x 1,35 \= 5.400) violaba la regla de verificacion enunciada dos parrafos mas abajo en esa misma version (que el COP/CAD debe ser menor que la TRM): 5.400 es mayor que 4.000, no menor. El codigo del notebook (Etapa 3, celda de construccion de la serie COP/CAD) nunca tuvo este error — invierte correctamente el dato del Bank of Canada antes de multiplicar, y por eso los resultados del modelo (por ejemplo, COP/CAD base de 3.095,59 al cierre de 2024, frente a una TRM de 4.409,15 ese mismo dia) son correctos. El error estaba unicamente en esta explicacion conceptual y en el Sub-paso 1 de la Tarea 5 (Seccion 6.5.3), que tambien se corrige mas abajo. Si se construyo alguna tabla manual (`tabla_B4_precios_referencia.xlsx`, `tabla_B5_sensibilidad_margenes.xlsx`) usando la formula sin invertir, esos valores de COP/CAD estarian inflados en aproximadamente un 35-45% y deben revisarse.

## **3.3 Volatilidad cambiaria**

La volatilidad es una medida estadistica de cuanto varia un precio (en este caso, el tipo de cambio COP/CAD) a lo largo del tiempo. Una volatilidad alta significa que el tipo de cambio sube y baja con fuerza de un dia para otro; una volatilidad baja significa que el tipo de cambio se mantiene relativamente estable.

***Como se calcula, paso a paso conceptual***

Sub-paso 1: se calculan los retornos diarios, es decir, el cambio porcentual del tipo de cambio de un dia para el siguiente.

Sub-paso 2: se calcula la desviacion estandar de esos retornos diarios. La desviacion estandar es una medida estadistica que indica, en promedio, cuanto se aleja cada dato de su propio promedio.

Sub-paso 3: como la desviacion estandar calculada en el sub-paso 2 esta en terminos diarios, se anualiza multiplicandola por la raiz cuadrada de 252 (el numero aproximado de dias habiles bursatiles en un ano). Esto convierte la medida diaria en una medida anual, que es la forma estandar en que se reporta la volatilidad en finanzas.

***Ejemplo numerico***

Si la desviacion estandar de los retornos diarios es 0,009 (es decir, 0,9%), la volatilidad anualizada es: 0,009 x raiz cuadrada de 252 \= 0,009 x 15,87 \= 0,143, es decir, 14,3% anual. Esto se interpreta asi: en un ano tipico, el tipo de cambio COP/CAD puede fluctuar, en terminos estadisticos, alrededor de un 14,3% por encima o por debajo de su nivel promedio.

## **3.4 Value at Risk (VaR historico al 95%)**

El VaR (Valor en Riesgo) es una medida de riesgo financiero ampliamente usada en bancos, fondos de inversion y tesorerias corporativas. Responde una pregunta muy concreta: en un horizonte de tiempo determinado, cual es la perdida maxima que se puede esperar, con un nivel de confianza dado (en este modelo, 95%).

***Que significa el 95% de confianza***

Significa que, segun el comportamiento historico del tipo de cambio, en el 95% de los casos la perdida real no sera peor que el numero que arroja el VaR. El 5% restante son los escenarios extremos, los llamados 'tail risk' o riesgo de cola, que el VaR no cubre. Por eso el VaR no es una garantia absoluta, sino una medida probabilistica.

***Metodo historico, paso a paso conceptual***

Sub-paso 1: se toman todos los retornos diarios historicos del COP/CAD del periodo bajo analisis (2020-2024 en este modelo).

Sub-paso 2: se ordenan esos retornos de menor a mayor (del peor dia al mejor dia).

Sub-paso 3: se identifica el valor que deja exactamente el 5% de los peores retornos por debajo de el. Ese valor es el percentil 5, y corresponde al VaR diario al 95% de confianza.

Sub-paso 4: para obtener el VaR a un horizonte mayor a un dia (por ejemplo, 30, 60 o 90 dias, que son los plazos tipicos de cobro de una exportacion), se aplica la regla de la raiz del tiempo: VaR a N dias \= VaR diario x raiz cuadrada de N.

***Ejemplo numerico completo***

Supongamos que el VaR diario al 95% es \-0,9% (es decir, en el 95% de los dias historicos, la perdida no fue peor que un 0,9% de caida del tipo de cambio). El VaR a 30 dias seria: \-0,9% x raiz cuadrada de 30 \= \-0,9% x 5,48 \= \-4,93%, aproximadamente \-5%.

Aplicacion practica: si un exportador tiene una venta de 100.000 CAD a cobrar en 30 dias, y el COP/CAD actual es 3.200, el valor en pesos de esa venta hoy seria 320.000.000 COP (100.000 x 3.200). Si se aplica el VaR a 30 dias de \-5%, la perdida maxima esperada, con 95% de confianza, seria: 320.000.000 x 0,05 \= 16.000.000 COP. Esto significa que, en el peor 5% de los escenarios historicos, el exportador podria recibir hasta 16 millones de pesos menos de lo esperado, solo por el movimiento del tipo de cambio durante esos 30 dias.

## **3.5 Escenarios cambiarios y margen neto**

Un escenario, en el contexto de este modelo, es una simulacion de un nivel especifico del tipo de cambio COP/CAD, usado para calcular como cambiaria la rentabilidad de un exportador bajo esa condicion. No es una prediccion de lo que va a pasar, es una herramienta de analisis de sensibilidad.

***Los tres escenarios del modelo***

Escenario base: se calcula como el promedio movil de los ultimos 90 dias del COP/CAD historico. Representa una condicion de mercado relativamente normal, sin asumir ni una crisis ni una bonanza.

Escenario optimista: el COP/CAD base multiplicado por 1,10 (un 10% mas alto). En este escenario, el dolar canadiense vale mas pesos colombianos, lo cual significa que el exportador recibe mas pesos por la misma cantidad de CAD facturados, mejorando su margen.

Escenario pesimista: el COP/CAD base multiplicado por 0,85 (un 15% mas bajo). En este escenario, el dolar canadiense vale menos pesos colombianos, el exportador recibe menos pesos por la misma factura en CAD, y su margen se reduce, pudiendo volverse negativo.

***Margen neto: definicion y formula***

El margen neto es el porcentaje de ganancia real que le queda al exportador despues de descontar todos los costos asociados a la operacion: produccion, logistica, y en la version mas completa del modelo, tambien el costo financiero de esperar el pago.

Margen neto (%) \= (Ingreso en COP \- Costo total en COP) / Ingreso en COP x 100

## **3.6 Tipo de cambio de equilibrio (breakeven)**

El tipo de cambio de equilibrio, tambien llamado breakeven FX rate, es el valor exacto del COP/CAD en el cual el margen neto de un producto especifico se vuelve igual a cero. Es, en terminos practicos, el numero mas directamente accionable de todo el modelo, porque le dice al exportador, sin necesidad de entender estadistica, hasta donde puede caer el valor del dolar canadiense antes de que esa operacion especifica deje de ser rentable.

***Por que es mas util que el VaR para una decision rapida***

El VaR da una probabilidad de perdida, lo cual requiere cierta familiaridad con conceptos estadisticos para interpretarse correctamente. El tipo de cambio de equilibrio, en cambio, es un numero directo: si el COP/CAD esta hoy en 3.500 y el equilibrio de un producto es 3.000, el exportador sabe de inmediato que tiene un margen de maniobra de 500 pesos antes de empezar a perder dinero en esa operacion.

***Como se calcula***

Partiendo de que el margen neto es cero cuando el ingreso es igual al costo total, y que el ingreso es precio\_CAD multiplicado por el tipo de cambio, se despeja el tipo de cambio:

COPCAD\_equilibrio \= Costo\_total\_COP / Precio\_CAD

***Ejemplo numerico***

Si el costo total de producir y exportar un kilo de un producto es 4.500 COP, y el precio de venta es 2,00 CAD por kilo, entonces: COPCAD\_equilibrio \= 4.500 / 2,00 \= 2.250. Esto significa que mientras el COP/CAD se mantenga por encima de 2.250, ese producto sigue siendo rentable. Si el COP/CAD cae por debajo de 2.250, el exportador empieza a perder dinero en esa operacion especifica.

## **3.7 Stress testing historico**

El stress testing (prueba de estres) es una tecnica de gestion de riesgo que consiste en someter un modelo financiero a condiciones extremas, basadas en eventos que ya ocurrieron en la realidad, en lugar de usar supuestos arbitrarios o inventados.

***Por que es mejor que usar porcentajes arbitrarios como \+10% o \-15%***

Un porcentaje arbitrario, por mas razonable que parezca, no tiene respaldo en la evidencia. El peso colombiano ha tenido movimientos historicos mucho mas severos que \-15% en periodos relativamente cortos. Aplicar al modelo los porcentajes de cambio reales de esos episodios historicos, en lugar de solo el escenario pesimista arbitrario, le da al analisis un respaldo empirico mucho mas solido y permite responder la pregunta: que pasaria si se repitiera una crisis como la que ya vivimos.

***Episodios historicos relevantes para Colombia (orientacion general; valores exactos verificados en tabla\_B6\_episodios\_historicos.xlsx — actualizados julio 2026)***

2014-2016 (Crisis petrolera): la caida del precio internacional del petroleo genero una devaluacion fuerte del peso colombiano. TRM del 04/06/2014 \= 1.899,74; TRM del 12/02/2016 \= 3.434,89; variacion \= \+80,81%.

2020 (Choque pandemia COVID-19): el inicio de la pandemia genero un salto rapido de la TRM. TRM del 10/01/2020 \= 3.253,89; TRM del 20/03/2020 \= 4.153,91; variacion \= \+27,66%.

2022 (Alza de tasas Fed e incertidumbre politica): una combinacion de subidas de tasas de interes en Estados Unidos e incertidumbre politica local (eleccion presidencial de junio de 2022) llevo a la TRM a superar los 5.000 pesos. TRM del 05/04/2022 \= 3.706,95; TRM del 05/11/2022 \= 5.061,21; variacion \= \+36,53%.

2022-2024 (Apreciacion del peso): moderacion del ciclo de alzas de tasas de la Reserva Federal, mayor apetito por activos de mercados emergentes, y precios del petroleo relativamente altos. TRM del 05/11/2022 \= 5.061,21; TRM del 10/04/2024 \= 3.763,43; variacion \= \-25,64%. Este es el UNICO de los cuatro episodios en el que el peso se aprecia en vez de devaluarse, y por eso es el mas importante de los cuatro para este modelo: un exportador que cobra en dolares canadienses y tiene sus costos en pesos colombianos pierde margen cuando el peso se APRECIA (el CAD vale menos pesos), no cuando se devalua. Los otros tres episodios, pese a ser las crisis cambiarias mas conocidas del periodo, en realidad MEJORAN el margen de este tipo de exportador.

Estos cuatro episodios son el punto de partida de la investigacion de la Tarea 6 del Bloque A, donde se documentan con fechas y valores exactos verificados contra la fuente oficial. La Tarea 6 exige entre 4 y 6 episodios (Seccion 6.6.5); estos cuatro son el minimo exigido y ya cubren tanto devaluaciones fuertes como el escenario de apreciacion, que es el que realmente importa para la conclusion del modelo.

## **3.8 Cobertura natural (natural hedge)**

La cobertura natural es un concepto de finanzas corporativas internacionales que describe una situacion en la cual una empresa, sin usar ningun instrumento financiero derivado, reduce su exposicion al riesgo cambiario de forma estructural, simplemente por la composicion de sus ingresos y costos en distintas monedas.

***Como funciona en el caso de un exportador colombiano***

Si un exportador colombiano vende su producto en dolares canadienses (su ingreso esta en CAD) pero todos sus costos de produccion estan en pesos colombianos, esta completamente expuesto al riesgo cambiario: cuando el peso se devalua, su ingreso en pesos sube, pero sus costos no cambian, asi que en teoria deberia ganar mas. El problema real ocurre en el escenario contrario, cuando el peso se aprecia (el CAD vale menos pesos), porque ahi el ingreso en pesos baja pero los costos siguen igual.

Ahora bien, si ese mismo exportador usa insumos importados (por ejemplo, fertilizantes o agroquimicos cotizados en dolares) para producir su mercancia, una parte de sus costos tambien esta vinculada al tipo de cambio. Cuando el peso se devalua, esos costos importados tambien suben en pesos, al mismo tiempo que sube el ingreso. Esto genera una compensacion parcial: la empresa no esta 100% expuesta al movimiento del tipo de cambio, porque una parte de sus costos se mueve en la misma direccion que sus ingresos.

***Ejemplo numerico simplificado***

Producto A: 100% de los costos en pesos colombianos. Si el peso se devalua 20%, el ingreso en pesos sube 20% (porque el CAD vale mas pesos) y los costos no cambian, asi que el margen mejora de forma completa por el efecto cambiario.

Producto B: 40% de los costos en insumos importados (dolar-vinculados) y 60% en pesos. Si el peso se devalua 20%, el ingreso en pesos sube 20%, pero el 40% de los costos tambien sube aproximadamente 20% en pesos, asi que la mejora neta del margen es menor que en el Producto A. Esto en la practica significa que el Producto B tiene menos volatilidad de margen ante movimientos del tipo de cambio, es decir, menos riesgo cambiario neto, gracias a su cobertura natural.

## **3.9 Costo de capital de trabajo (cost of carry)**

Cuando una empresa exporta y vende a credito, es decir, entrega la mercancia y recibe el pago 30, 60 o 90 dias despues, tiene que seguir operando durante ese periodo: pagar nomina, comprar insumos, cubrir transporte, sin haber recibido todavia el dinero de esa venta. Para cubrir esos gastos mientras espera el pago, la empresa necesita financiamiento, ya sea con recursos propios (que tienen un costo de oportunidad) o con credito bancario (que tiene un costo financiero explicito, una tasa de interes).

***Por que este costo es relevante en un analisis de exportacion***

Las tasas de interes en Colombia son, de forma estructural, mas altas que las tasas de interes en Canada. Esto significa que financiar una operacion de exportacion en pesos colombianos durante 30, 60 o 90 dias tiene un costo proporcionalmente mayor que si la misma operacion se financiara en dolares canadienses. Ese costo reduce el margen neto real del exportador, y la mayoria de los analisis simplificados de margenes de exportacion lo ignoran por completo.

***Como se calcula***

Costo financiero \= Costo\_total\_COP x (Tasa\_interes\_anual / 365\) x Numero\_de\_dias

Ejemplo: si el costo total de una operacion es 6.000.000 COP, la tasa de interes anual de referencia en Colombia (IBR) es 9,5%, y el plazo de cobro es 60 dias, el costo financiero seria: 6.000.000 x (0,095/365) x 60 \= 6.000.000 x 0,000260 x 60 \= 93.700 COP aproximadamente. Este monto se resta del margen bruto para obtener un margen neto mas realista.

## **3.10 Instrumentos de cobertura cambiaria: forward y NDF**

Un forward cambiario es un contrato financiero mediante el cual dos partes acuerdan, en el dia de hoy, el tipo de cambio al que se va a comprar o vender una cantidad determinada de una moneda en una fecha futura especifica. La ventaja para un exportador es que elimina la incertidumbre: sin importar como se mueva el tipo de cambio entre hoy y la fecha futura, la empresa ya sabe exactamente cuantos pesos va a recibir por su venta en dolares canadienses.

***Por que en Colombia se usa mas el NDF que el forward tradicional***

Un NDF (Non-Deliverable Forward, o forward no entregable) es una variante del forward tradicional en la cual, al vencimiento del contrato, no hay entrega fisica de la moneda extranjera: simplemente se liquida en pesos colombianos la diferencia entre el tipo de cambio pactado y el tipo de cambio real del mercado en esa fecha. En Colombia, el NDF es el instrumento mas comun para cubrir riesgo cambiario, y casi siempre se estructura a traves del dolar americano (USD), porque no existe un mercado liquido de forwards COP/CAD directos: una empresa colombiana que quiere cubrirse del riesgo COP/CAD normalmente combina un NDF de USD/COP con la posicion en CAD/USD de su contraparte canadiense, o simplemente usa el dolar americano como moneda intermedia en toda la operacion comercial.

***Como se estima el costo de un forward o NDF***

El costo de un forward esta determinado principalmente por el diferencial de tasas de interes entre los dos paises involucrados, mediante un principio financiero llamado paridad de tasas de interes. En terminos simples: si las tasas de interes en Colombia son mas altas que en Canada, el forward va a incorporar ese diferencial como un costo (los llamados puntos forward), porque el banco que ofrece el contrato tiene que compensar la diferencia de rendimiento entre invertir en pesos colombianos o en dolares canadienses durante el plazo del contrato.

## **3.11 Plan Vallejo / Drawback de IVA**

El regimen de Plan Vallejo de importacion es un mecanismo aduanero colombiano que permite a una empresa importar insumos, materias primas, o bienes de capital con beneficios tributarios (que pueden incluir exoneracion o devolucion de aranceles e impuestos), siempre que esos insumos se utilicen para producir bienes que luego se exportan.

***Por que es relevante aunque el arancel de exportacion sea 0%***

El arancel de exportacion (lo que Canada cobra por recibir el producto colombiano) y el IVA de importacion (lo que Colombia cobra por dejar entrar un insumo extranjero) son dos cosas completamente distintas. Que el primero sea 0% no tiene ninguna relacion con el segundo. Un exportador colombiano de flores, por ejemplo, puede estar pagando IVA del 19% al importar fertilizantes o agroquimicos especializados, y ese IVA es un costo real que reduce su margen, sin importar que el arancel de sus rosas hacia Canada sea cero. Si ese exportador tiene acceso al regimen de Plan Vallejo, puede recuperar ese IVA, lo cual mejora su margen real.

# **4\. Estructura de carpetas, explicada con detalle**

Toda la informacion del proyecto se organiza en Google Drive, dentro de una carpeta principal llamada MIC-CC. Esta seccion explica no solo cuales son las subcarpetas, sino por que cada una existe y que pasa si un archivo se guarda en el lugar equivocado.

**4.1 Por que la estructura de carpetas importa tanto**

El notebook de Python que se construye en el Bloque B de esta guia hace referencia a las rutas de los archivos de forma exacta, por ejemplo: /content/drive/MyDrive/MIC-CC/data/raw/TRM\_COP\_USD\_2020\_2024.xlsx. Si el archivo TRM\_COP\_USD\_2020\_2024.xlsx esta guardado en una carpeta distinta, o tiene un nombre ligeramente distinto (con mayusculas diferentes, con espacios donde el codigo espera guiones bajos, o con una fecha distinta en el nombre), el codigo de Python no va a poder encontrarlo, y va a mostrar un error del tipo FileNotFoundError. Por eso, antes de empezar cualquier tarea de recoleccion de datos, conviene crear toda la estructura de carpetas completa, una sola vez, y respetarla durante toda la fase.

**4.2 Como crear la estructura de carpetas en Google Drive, paso a paso**

Sub-paso 1: abrir drive.google.com en el navegador, con la cuenta de Google que se va a usar para todo el proyecto.

Sub-paso 2: hacer clic en el boton 'Nuevo' (generalmente en la esquina superior izquierda, con un signo mas).

Sub-paso 3: seleccionar 'Carpeta nueva'.

Sub-paso 4: escribir exactamente: MIC-CC (con guion medio, sin espacios, en mayusculas tal como esta escrito aqui).

Sub-paso 5: hacer doble clic en la carpeta MIC-CC recien creada para entrar en ella.

Sub-paso 6: dentro de MIC-CC, repetir el proceso de crear carpeta nueva para cada una de las siguientes, una por una: data, notebooks, outputs, docs, references.

Sub-paso 7: entrar en la carpeta data (doble clic) y dentro de ella crear dos carpetas nuevas: raw y processed.

Sub-paso 8: volver a la carpeta MIC-CC (usando la flecha de regreso o la ruta de navegacion en la parte superior), entrar en la carpeta outputs, y dentro de ella crear dos carpetas nuevas: tables y figures.

Sub-paso 9: verificar la estructura completa navegando por cada carpeta. Al final, la estructura debe verse exactamente asi: MIC-CC, y dentro de ella data (con raw y processed dentro), notebooks, outputs (con tables y figures dentro), docs, references.

**4.3 Tabla de referencia de carpetas y su contenido**

| Carpeta (ruta completa) | Que va aqui y por que |
| ----- | ----- |
| MIC-CC/data/raw/ | Los nueve archivos de datos originales del Bloque A (TRM, USD/CAD, Drawback, precios, episodios historicos, instrumentos de cobertura, tasas de interes, estructura de costos), sin ninguna modificacion respecto a como se obtuvieron de la fuente original. Se guardan sin modificar para que cualquier persona pueda verificar el dato contra la fuente. |
| MIC-CC/data/processed/ | Datos que ya pasaron por algun procesamiento en Python, como la serie COP/CAD combinada (que se construye uniendo la TRM y el USD/CAD). Se guardan separados de los datos crudos para distinguir claramente entre el dato original y el dato ya transformado. |
| MIC-CC/notebooks/ | El archivo del notebook de Python, 04\_financial\_model.ipynb. Este es el unico archivo de codigo de toda la fase. |
| MIC-CC/outputs/tables/ | Las tablas de resultados generadas por el modelo (las identificadas con numero, como tabla\_04, tabla\_05, etc.), ademas de la tabla\_B5 que se construye de forma preliminar en el Bloque A. |
| MIC-CC/outputs/figures/ | Las cinco figuras en formato PNG generadas por el modelo en el Bloque C. |
| MIC-CC/docs/ | Los borradores de la seccion del Working Paper, normalmente como un documento de Google Docs vinculado a esta carpeta. |
| MIC-CC/references/ | PDFs o capturas de pantalla de las fuentes consultadas durante el Bloque A, en caso de que se quieran guardar copias de respaldo ademas de la URL documentada en cada tabla. |

**4.4 Verificacion final de la estructura antes de empezar**

Antes de iniciar la Tarea 1 del Bloque A, hacer este chequeo: abrir la carpeta MIC-CC en Drive, y confirmar visualmente que existen exactamente las siguientes seis carpetas de primer nivel: data, notebooks, outputs, docs, references. Dentro de data deben existir exactamente dos carpetas: raw y processed. Dentro de outputs deben existir exactamente dos carpetas: tables y figures. Si falta alguna, crearla antes de continuar.

# **5\. Cronograma detallado de 24 dias**

Este cronograma divide el trabajo en tres bloques secuenciales. La diferencia respecto a un cronograma resumido es que aqui cada dia tambien indica cuantos sub-pasos aproximados tiene la tarea de ese dia, para que sea mas facil estimar cuanto tiempo real va a tomar.

## **Bloque A: recoleccion de datos e investigacion (dias 1 a 10\)**

| Dia | Tarea | Duracion | Entregable exacto |
| ----- | ----- | ----- | ----- |
| 1 | Preparacion: carpetas en Drive, lectura de conceptos, configuracion inicial | 3-4 horas | Estructura de carpetas creada y verificada; respuestas escritas a las preguntas conceptuales de la Seccion 7.0 |
| 2 | Tarea 1: TRM del Banco de la Republica | 1,5-2,5 horas | TRM\_COP\_USD\_2020\_2024.xlsx verificado |
| 3 | Tarea 2: USD/CAD del Bank of Canada | 2-3 horas | USDCAD\_2020\_2024.xlsx verificado |
| 4 | Tarea 3: Verificacion Drawback / Plan Vallejo | 4-5 horas | tabla\_B3\_drawback\_iva.xlsx (10 filas) |
| 5-6 | Tarea 4: Precios de referencia en CAD | 6-8 horas | tabla\_B4\_precios\_referencia.xlsx (10 filas) |
| 7 | Tarea 5: Tabla de sensibilidad de margenes brutos | 4-5 horas | tabla\_B5\_sensibilidad\_margenes.xlsx (30 filas) |
| 8 | Tarea 6: Episodios historicos de devaluacion | 5-6 horas | tabla\_B6\_episodios\_historicos.xlsx (4-6 filas) |
| 9 | Tarea 7: Instrumentos de cobertura cambiaria | 4-5 horas | tabla\_B7\_instrumentos\_cobertura.xlsx |
| 9 | Tarea 8: Tasas de interes Colombia vs Canada | 3-4 horas | tabla\_B8\_tasas\_interes.xlsx |
| 10 | Tarea 9: Estructura de costos (cobertura natural) | 6-7 horas | tabla\_B9\_estructura\_costos.xlsx (10 filas) |

## **Bloque B: construccion del modelo en Python (dias 11 a 19\)**

| Dia | Etapa | Duracion | Entregable exacto |
| ----- | ----- | ----- | ----- |
| 11 | Etapa 1-2: entorno y descarga USD/CAD via API | 2-3 horas | Notebook corriendo; DataFrame boc\_df verificado |
| 12 | Etapa 3: construir la serie COP/CAD | 3-5 horas | fx\_COPCAD\_2020\_2024.xlsx (\~1.240 filas) |
| 13 | Etapa 4-5: volatilidad y VaR | 3-4 horas | tabla\_04\_indicadores\_riesgo.xlsx |
| 14 | Etapa 6: escenarios y 60 margenes | 4-6 horas | tabla\_05\_margenes\_escenarios.xlsx (60 filas) |
| 15 | Etapa 7: modulo de breakeven | 3-4 horas | tabla\_06\_breakeven.xlsx |
| 16 | Etapa 8: modulo de cobertura natural | 3-4 horas | tabla\_07\_cobertura\_natural.xlsx |
| 17 | Etapa 9: modulo de stress testing historico | 3-4 horas | tabla\_08\_stress\_testing.xlsx |
| 18 | Etapa 10: modulo de costo de capital de trabajo | 2-3 horas | tabla\_09\_costo\_capital.xlsx |
| 19 | Etapa 11-12: costo-beneficio de cobertura y Drawback | 4-6 horas | tabla\_10 y tabla\_11\_margen\_final\_ajustado.xlsx |

## **Bloque C: figuras, publicacion y documentacion (dias 20 a 24\)**

| Dia | Tarea | Duracion | Entregable exacto |
| ----- | ----- | ----- | ----- |
| 20-21 | Construir las 5 figuras | 6-8 horas | figuras 04 a 08 en PNG, 150 dpi |
| 22 | Crear y poblar el repositorio en GitHub | 3-5 horas | Repositorio publico MIC-CC-ODEM-EAN con README en ingles |
| 23-24 | Redactar las 8 subsecciones del Working Paper | 8-12 horas | Seccion 5 completa, en Google Docs, con referencias APA 7 |

Si el tiempo disponible por dia es menor al estimado, el cronograma se extiende de forma proporcional, pero el orden de los bloques y de las tareas dentro de cada bloque no debe alterarse, porque cada paso depende de que el anterior este terminado.

# **6\. Bloque A: recoleccion de datos e investigacion, sub-paso por sub-paso**

Esta seccion contiene las nueve tareas del Bloque A, cada una desglosada en sub-pasos detallados. La explicacion de cada tarea sigue siempre la misma estructura: que es y por que se necesita, donde buscar exactamente, los sub-pasos de ejecucion uno por uno, como verificar que el resultado es correcto, y que hacer si algo no funciona como se espera.

## **Tarea 1: TRM historica del Banco de la Republica**

**6.1.1 Que es esta tarea y por que se necesita**

Descargar la serie diaria de la Tasa Representativa del Mercado (TRM) para el periodo completo del 1 de enero de 2020 al 31 de diciembre de 2024, publicada por el Banco de la Republica de Colombia, y dejarla guardada como un archivo Excel limpio en la carpeta correcta de Drive.

Esta es la primera de las dos series de tipo de cambio necesarias para construir el COP/CAD (la tasa cruzada explicada en la Seccion 3.2). Sin esta serie, ninguna otra parte del modelo se puede construir, asi que conviene completarla al principio del Bloque A.

**6.1.2 Donde se va a buscar**

La fuente oficial y unica que se debe usar es el sitio web del Banco de la Republica de Colombia, en la direccion www.banrep.gov.co. No usar paginas de terceros, blogs financieros, ni convertidores de moneda genericos, porque la serie historica completa y verificable solo la garantiza la fuente oficial.

**6.1.3 Sub-pasos de ejecucion**

Sub-paso 1: abrir el navegador de internet (Google Chrome, Firefox, o el navegador que se tenga disponible).

Sub-paso 2: escribir en la barra de direcciones, no en un buscador: www.banrep.gov.co, y presionar Enter.

Sub-paso 3: esperar a que la pagina principal del Banco de la Republica cargue por completo. Esta pagina normalmente muestra noticias, indicadores economicos destacados, y un menu de navegacion en la parte superior.

Sub-paso 4: en el menu superior, ubicar y hacer clic en la opcion 'Estadisticas'. Si el menu superior no es visible de inmediato, puede estar bajo un icono de tres lineas horizontales (menu hamburguesa) en la esquina superior, especialmente si se esta usando un celular o una pantalla pequena; en ese caso, hacer clic en ese icono primero.

Sub-paso 5: dentro del menu de Estadisticas, buscar una sub-categoria llamada 'Tasas de cambio' o 'Tipo de cambio'. Hacer clic ahi.

Sub-paso 6: dentro de esa sub-categoria, buscar especificamente la opcion 'TRM \- Tasa Representativa del Mercado'. El nombre puede aparecer tambien como 'Tasa de cambio del peso colombiano (TRM)'. Hacer clic.

Sub-paso 7: la pagina debe mostrar una herramienta de consulta con, al menos, dos campos de fecha (fecha inicial y fecha final) y un boton de consulta o busqueda.

Sub-paso 8: hacer clic en el campo de 'Fecha inicial' y escribir o seleccionar en el calendario: 01/01/2020 (dia 1, mes 1, ano 2020).

Sub-paso 9: hacer clic en el campo de 'Fecha final' y escribir o seleccionar en el calendario: 31/12/2024 (dia 31, mes 12, ano 2024).

Sub-paso 10: revisar visualmente que ambos campos de fecha quedaron escritos correctamente antes de continuar, porque un error de digitacion en la fecha (por ejemplo escribir 2020 en el campo de fecha final) generaria una descarga vacia o incorrecta.

Sub-paso 11: hacer clic en el boton 'Consultar', 'Buscar', o el equivalente que aparezca en esa version de la pagina.

Sub-paso 12: esperar a que la pagina cargue los resultados. Dependiendo del volumen de datos (mas de 1.200 filas), puede tardar algunos segundos.

Sub-paso 13: una vez cargados los resultados, buscar un boton o enlace de 'Descargar', 'Exportar', o un icono de descarga (normalmente una flecha apuntando hacia abajo sobre una linea horizontal).

Sub-paso 14: al hacer clic en descargar, normalmente aparece un menu para elegir el formato. Seleccionar el formato Excel, identificado como .xlsx o simplemente como 'Excel'. Si solo se ofrece CSV, esa opcion tambien sirve, porque se puede abrir y guardar como Excel despues (ver el Sub-paso 18).

Sub-paso 15: el archivo se descarga automaticamente a la carpeta de descargas predeterminada del computador (normalmente una carpeta llamada 'Descargas' o 'Downloads').

Sub-paso 16: abrir esa carpeta de descargas y localizar el archivo recien descargado. Normalmente tiene un nombre generado automaticamente por la pagina del BanRep, distinto al nombre final que se necesita.

Sub-paso 17: hacer clic derecho sobre el archivo y seleccionar 'Cambiar nombre' o 'Renombrar'.

Sub-paso 18: escribir exactamente: TRM\_COP\_USD\_2020\_2024.xlsx (respetando mayusculas, guiones bajos, y la extension .xlsx). Si el archivo descargado es un CSV en lugar de Excel, abrirlo con Excel o Google Sheets, y usar la opcion 'Guardar como' o 'Descargar como' para guardarlo en formato .xlsx con ese mismo nombre.

Sub-paso 19: abrir el archivo renombrado con Excel o Google Sheets para revisarlo antes de subirlo a Drive (ver la verificacion de calidad en la Seccion 6.1.4).

Sub-paso 20: una vez verificado, ir a Google Drive, navegar hasta la carpeta MIC-CC/data/raw/, y subir el archivo arrastrandolo directamente a esa carpeta desde el explorador de archivos del computador, o usando el boton 'Nuevo' \> 'Subir archivo' dentro de Drive.

Sub-paso 21: confirmar que el archivo aparece dentro de la carpeta correcta navegando visualmente hasta MIC-CC/data/raw/ en Drive y verificando que TRM\_COP\_USD\_2020\_2024.xlsx esta ahi.

**6.1.4 Verificacion de calidad del archivo**

Antes de dar por terminada esta tarea, revisar los siguientes cinco puntos, en el orden indicado:

Verificacion 1, nombre del archivo: debe ser exactamente TRM\_COP\_USD\_2020\_2024.xlsx, sin espacios, sin numeros adicionales, sin la palabra 'final' o 'copia' agregada.

Verificacion 2, numero de filas: contar (o usar la funcion CONTAR de Excel) cuantas filas de datos tiene el archivo, sin contar el encabezado. Debe haber al menos 1.200 filas, porque entre el 1 de enero de 2020 y el 31 de diciembre de 2024 hay aproximadamente 1.260 dias habiles bursatiles.

Verificacion 3, rango de valores: revisar la columna de valores de la TRM. Todos los valores deben estar entre 3.000 y 5.500 (este es el rango aproximado en el que se movio la TRM durante el periodo 2020-2024). Si aparece algun valor muy por fuera de ese rango (por ejemplo 41,50 o 410.000), es muy probable que haya un error de formato en la descarga, como una coma decimal mal interpretada como separador de miles.

Verificacion 4, celdas vacias: revisar visualmente, o usando un filtro en Excel, que no haya celdas vacias en la columna de fechas ni en la columna de valores.

Verificacion 5, rango de fechas: confirmar que la primera fecha de la tabla es cercana al 1 de enero de 2020 y la ultima fecha es cercana al 31 de diciembre de 2024\. Pequenas diferencias de uno o dos dias son normales por festivos, pero diferencias de semanas o meses indican un error en el rango de consulta.

**6.1.5 Que hacer si algo no funciona**

Si la pagina del Banco de la Republica tiene un diseno distinto al descrito (las paginas gubernamentales cambian su interfaz con cierta frecuencia): buscar en Google, no en la pagina del BanRep, los terminos 'Banco de la Republica Colombia TRM descarga historica 2024'. Los primeros resultados normalmente llevan directamente a la herramienta de consulta actualizada.

Si la descarga no incluye un campo de fechas y en cambio muestra solo el valor del dia actual: se esta en la pagina de consulta del valor diario, no en la de la serie historica. Buscar especificamente un enlace o pestana que diga 'Serie historica' o 'Historico'.

Si despues de 30 a 40 minutos de busqueda no se logra acceder a la serie historica completa: documentar exactamente que se intento (las URLs visitadas, los terminos de busqueda usados), marcar la tarea como pendiente, y continuar con la Tarea 2\. Volver a intentarlo mas tarde el mismo dia o al dia siguiente, con terminos de busqueda distintos.

## **Tarea 2: USD/CAD del Bank of Canada**

**6.2.1 Que es esta tarea y por que se necesita**

Obtener la serie diaria del tipo de cambio USD/CAD (cuantos dolares americanos cuesta un dolar canadiense) para el periodo del 1 de enero de 2020 al 31 de diciembre de 2024, publicada por el Bank of Canada, y dejarla como un archivo Excel limpio en Drive. Es la segunda de las dos series necesarias para construir el COP/CAD.

**6.2.2 Que es una API y por que se va a usar aqui**

Una API (Interfaz de Programacion de Aplicaciones, por sus siglas en ingles) es una forma en la que un sitio web permite que un programa, o incluso un navegador comun, le pida datos de forma directa y estructurada, sin tener que navegar manualmente por menus y botones. El Bank of Canada tiene una API publica y completamente gratuita, llamada Valet API, que no requiere registro, contrasena, ni clave de acceso. Se accede simplemente escribiendo una direccion web (URL) especifica, y los datos aparecen directamente en la pantalla en un formato de texto estructurado llamado JSON.

JSON (JavaScript Object Notation) es un formato de datos muy comun en internet. Para quien no esta familiarizado con el, se ve como una serie de llaves, corchetes, y pares de nombre-valor, similar a un diccionario. No es necesario entenderlo en profundidad para esta tarea: solo se necesita poder identificar la fecha y el valor del tipo de cambio dentro del texto, y convertirlos a una tabla de Excel.

**6.2.3 Sub-pasos de ejecucion, metodo principal (via API)**

Sub-paso 1: abrir un navegador de internet, preferiblemente Google Chrome, porque tiende a mostrar el JSON de forma mas legible que otros navegadores.

Sub-paso 2: copiar exactamente la siguiente direccion (URL), sin agregar ni quitar ningun caracter:

https://www.bankofcanada.ca/valet/observations/FXUSDCAD/json?start\_date=2020-01-01\&end\_date=2024-12-31

Sub-paso 3: pegar esa URL en la barra de direcciones del navegador (no en un buscador) y presionar Enter.

Sub-paso 4: esperar a que la pagina cargue. Debe aparecer un bloque largo de texto que comienza, aproximadamente, asi: {"terms":{...},"seriesDetail":{...},"observations":\[{"d":"2020-01-02","FXUSDCAD":{"v":"1.2988"}}, ...\]}

Sub-paso 5: identificar dentro de ese texto la palabra 'observations'. A partir de ahi comienza la lista de datos reales: cada bloque entre llaves contiene una fecha (etiquetada como 'd') y un valor del tipo de cambio (etiquetado como 'v', dentro de 'FXUSDCAD').

Sub-paso 6: si el navegador muestra un mensaje de error en lugar del texto JSON (por ejemplo, una pagina en blanco o un mensaje de 'no se puede acceder a este sitio'), verificar que la URL se copio exactamente, sin espacios adicionales al principio o al final, y volver a intentar. Si el error persiste, intentar con un navegador distinto.

**6.2.4 Como convertir el JSON a una tabla de Excel**

Hay tres formas de hacer esta conversion, ordenadas de la mas sencilla a la mas tecnica. Usar la primera que funcione.

**Opcion A (recomendada): usar una herramienta en linea de conversion JSON a Excel**

Sub-paso 1: en el navegador, abrir una nueva pestana y buscar en Google: 'convertidor JSON a Excel en linea' o 'JSON to Excel converter online'.

Sub-paso 2: seleccionar una de las herramientas gratuitas que aparecen en los primeros resultados (existen varias opciones confiables y gratuitas para este tipo de conversion simple).

Sub-paso 3: volver a la pestana donde se cargo el JSON del Bank of Canada (Sub-paso 4 de la seccion anterior), seleccionar todo el texto (Ctrl+A en Windows o Cmd+A en Mac) y copiarlo (Ctrl+C o Cmd+C).

Sub-paso 4: pegar ese texto JSON en el campo de entrada de la herramienta de conversion.

Sub-paso 5: la herramienta normalmente muestra varias 'rutas' o 'arrays' detectados dentro del JSON; seleccionar especificamente el que corresponde a 'observations', que es donde estan los datos diarios.

Sub-paso 6: descargar el resultado en formato Excel o CSV.

Sub-paso 7: si el resultado tiene columnas anidadas o con nombres como 'FXUSDCAD.v', renombrar esa columna simplemente como USDCAD, y la columna de fecha (que puede llamarse 'd') renombrarla como fecha.

**Opcion B: pagina alternativa del Bank of Canada con descarga directa**

Sub-paso 1: ir a www.bankofcanada.ca.

Sub-paso 2: buscar en el menu, o en el buscador interno de la pagina, la seccion 'Exchange Rates' (Tipos de cambio).

Sub-paso 3: dentro de esa seccion, buscar la opcion de tipos de cambio diarios historicos ('Daily exchange rates' o 'Historical exchange rates').

Sub-paso 4: seleccionar el par USD/CAD y el rango de fechas 01/01/2020 a 31/12/2024.

Sub-paso 5: buscar un boton de descarga en formato CSV, que es el formato que esta pagina suele ofrecer directamente, sin pasar por el JSON de la API.

Sub-paso 6: abrir el CSV descargado con Excel y guardarlo en formato .xlsx.

**Opcion C (alternativa manual, solo si las anteriores no funcionan): copiar y pegar en bloques**

Sub-paso 1: en la pestana del JSON, usar la funcion de busqueda del navegador (Ctrl+F o Cmd+F) para localizar visualmente los pares de fecha y valor.

Sub-paso 2: copiar manualmente, en bloques de varios meses a la vez, las fechas y valores hacia una hoja de Excel en blanco, en dos columnas (fecha y USDCAD).

Sub-paso 3: esta opcion es mas lenta, asi que solo se recomienda como ultimo recurso, y conviene dividir el trabajo en varias sesiones cortas para evitar errores de transcripcion.

**6.2.5 Finalizar el archivo**

Sub-paso 1: una vez que el archivo Excel tiene dos columnas claras (fecha y USDCAD) con los datos completos, revisar que no haya columnas adicionales con texto irrelevante del JSON original (como 'terms' o 'seriesDetail'); si las hay, borrarlas.

Sub-paso 2: ordenar los datos de la fecha mas antigua a la mas reciente (seleccionar toda la tabla, usar la funcion 'Ordenar' de Excel sobre la columna de fecha, de menor a mayor).

Sub-paso 3: renombrar el archivo exactamente como: USDCAD\_2020\_2024.xlsx

Sub-paso 4: subir el archivo a la carpeta MIC-CC/data/raw/ en Drive.

**6.2.6 Verificacion de calidad del archivo**

Verificacion 1, nombre exacto: USDCAD\_2020\_2024.xlsx

Verificacion 2, numero de filas: al menos 1.200 filas de datos (sin contar el encabezado).

Verificacion 3, rango de valores: todos los valores de USDCAD deben estar entre 1,25 y 1,45 (rango unificado con la Seccion 3.2 y la Etapa 2 del Bloque B). Este es el rango aproximado en el que se movio el USD/CAD durante 2020-2024, con un promedio cercano a 1,32. Si aparecen valores como 0,75 o 1,75 fuera de ese rango de forma sistematica, es posible que la serie descargada sea CAD/USD (la inversa) en lugar de USD/CAD; en ese caso, revisar el codigo de serie usado en la consulta.

Verificacion 4, celdas vacias: ninguna celda vacia en las dos columnas.

Verificacion 5, rango de fechas: la primera fecha cercana al 2 de enero de 2020 (el Bank of Canada no publica datos el 1 de enero por ser feriado) y la ultima cercana al 31 de diciembre de 2024\.

**6.2.7 Que hacer si algo no funciona**

Si la URL de la API no responde o da un error de tipo 'Not Found': verificar que el codigo de la serie sigue siendo FXUSDCAD. Los codigos de serie de la Valet API pueden cambiar con actualizaciones de la pagina; buscar en Google 'Bank of Canada Valet API FXUSDCAD documentation' para confirmar el codigo vigente.

Si los valores obtenidos no coinciden con el rango esperado (1,20 a 1,45): revisar si la serie devuelta es semanal o mensual en lugar de diaria, lo cual generaria muchas menos filas de las esperadas; en ese caso, agregar a la URL el parametro adicional que especifica frecuencia diaria, o consultar la documentacion de la Valet API en bankofcanada.ca buscando 'Valet API documentation series'.

Si ninguna de las tres opciones de conversion funciona despues de 40 minutos: documentar el intento, marcar la tarea como pendiente, continuar con la Tarea 3, y volver a intentarlo mas tarde con una busqueda mas especifica en Google del tipo 'Bank of Canada USD CAD historical data download excel'.

## **Tarea 3: Verificacion de Drawback / Plan Vallejo**

**6.3.1 Que es esta tarea y por que se necesita**

Los 10 productos del Top 10 ya estan completamente desgravados bajo el TLCC (arancel de exportacion 0%), asi que esta tarea no investiga aranceles. En cambio, verifica si cada producto puede acceder al regimen de Plan Vallejo de importacion para recuperar el IVA pagado en insumos importados. Este beneficio mejora el margen real del exportador y alimenta el Modulo 12 del modelo (ajuste por Drawback/IVA, Seccion 7.12 de esta guia).

**6.3.2 Sub-pasos de ejecucion, producto por producto**

Esta tarea se repite, en esencia, para cada uno de los 10 productos del Top 10 (la lista completa esta en la Seccion 2.4). El procedimiento es el mismo para cada uno; a continuacion se describe una sola vez, y se aplica diez veces.

Sub-paso 1: identificar el sector productivo del producto (por ejemplo, el cafe pertenece al sector cafetero, las rosas y crisantemos al sector floricultor, los pantalones de algodon y las medias al sector textil/confecciones, los medicamentos al sector farmaceutico, el aceite de palma al sector de oleaginosas, y el carbon de coque al sector minero).

Sub-paso 2: abrir una pestana nueva del navegador y buscar en Google exactamente: 'DIAN Plan Vallejo importacion sectores beneficiarios 2024'.

Sub-paso 3: revisar los primeros resultados, dando prioridad a paginas oficiales con dominio .gov.co. Buscar especificamente si el sector del producto que se esta investigando aparece mencionado como beneficiario activo del Plan Vallejo de importacion.

Sub-paso 4: en una segunda busqueda, escribir en Google: 'DIAN devolucion IVA insumos importados exportadores'. Revisar si esta busqueda aporta informacion adicional o mas reciente sobre el mecanismo de devolucion de IVA, que es distinto del Plan Vallejo tradicional pero cumple una funcion similar.

Sub-paso 5: para sectores con gremio fuerte, hacer una tercera busqueda dirigida al gremio especifico. Para floricultura: 'Asocolflores Plan Vallejo' o 'Asocolflores devolucion IVA insumos'. Para confecciones: 'ANDI Inexmoda Plan Vallejo confecciones'. Para cafe: 'Federacion Nacional de Cafeteros Plan Vallejo'.

Sub-paso 6: leer el contenido de las paginas encontradas (no solo el titulo en los resultados de busqueda) para confirmar si efectivamente describen el regimen de Plan Vallejo o devolucion de IVA aplicado a ese sector especifico, y no otro beneficio distinto.

Sub-paso 7: anotar en una tabla de Excel (que se construye en paralelo mientras se investiga cada producto) los siguientes datos para el producto: si aplica el regimen (responder unicamente 'si', 'no', o 'no esta claro'), una descripcion breve del tipo de beneficio especifico encontrado, la URL exacta de la pagina donde se encontro la informacion, y la fecha en que se hizo la consulta.

Sub-paso 8: si despues de las tres busquedas (Sub-pasos 2, 4 y 5\) no se encuentra informacion clara, no dejar la celda vacia. Escribir 'no esta claro' en la columna de aplica, y en la columna de fuente anotar cual de las busquedas se realizo, para que quede registro del intento.

Sub-paso 9: repetir los Sub-pasos 1 a 8 para cada uno de los 10 productos.

**6.3.3 Formato final del archivo**

Una hoja de Excel con 10 filas (una por producto) y las siguientes columnas: numero (1 a 10), nombre del producto, codigo HS, aplica Plan Vallejo / Drawback de IVA (si / no / no esta claro), tipo de beneficio, fuente (URL), fecha de consulta. Guardar como tabla\_B3\_drawback\_iva.xlsx y subir a MIC-CC/data/raw/.

**6.3.4 Verificacion de calidad**

Verificacion 1: exactamente 10 filas, una por producto, en el mismo orden de la lista de la Seccion 2.4.

Verificacion 2: ninguna fila tiene la columna 'aplica' vacia; cada una dice 'si', 'no', o 'no esta claro'.

Verificacion 3: cada fila tiene al menos una fuente anotada, incluso si la respuesta es 'no esta claro'.

Verificacion 4: las fuentes son paginas reales y verificables (se puede abrir la URL y encontrar contenido relacionado), no enlaces genericos a la pagina principal de un sitio sin especificar la seccion consultada.

## **Tarea 4: Precios de referencia en CAD para los 10 productos**

**6.4.1 Que es esta tarea y por que se necesita**

Encontrar un precio de venta de referencia, expresado en dolares canadienses (CAD), para cada uno de los 10 productos. Sin este dato no se puede calcular ningun margen en todo el modelo: es el insumo de entrada mas critico de toda la Fase 4\.

**6.4.2 Que tipo de precio se busca exactamente**

Se busca el precio FOB (Free On Board) de exportacion, que es el precio del producto puesto en el puerto de salida de Colombia, sin incluir el costo del flete internacional ni el seguro de transporte (esos costos se agregan por separado en otra parte del modelo, usando los datos de la dimension logistica del proyecto). Si no se encuentra un precio FOB especifico para un producto, la alternativa es usar el precio CIF (Cost, Insurance and Freight) de importacion reportado por Canada, y dividirlo entre 1,10 para aproximar el descuento del flete y el seguro y llegar a un estimado de precio FOB.

**6.4.3 Sub-pasos de ejecucion usando TradeMap (fuente principal)**

Sub-paso 1: ir a www.trademap.org en el navegador.

Sub-paso 2: si es la primera vez que se usa el sitio, sera necesario crear una cuenta gratuita: buscar el boton de 'Register' o 'Sign up', y completar el formulario con un correo electronico valido.

Sub-paso 3: una vez dentro, con la cuenta iniciada, buscar la herramienta de consulta de comercio bilateral, normalmente bajo un menu llamado 'Trade statistics' o un buscador central en la pagina de inicio.

Sub-paso 4: en el campo de pais exportador (o 'Country/Region exporting'), seleccionar Colombia.

Sub-paso 5: en el campo de producto, escribir o seleccionar el codigo HS del producto que se esta investigando (por ejemplo, 090111 para cafe sin tostar).

Sub-paso 6: en el campo de pais importador (o 'Country/Region importing'), seleccionar Canada.

Sub-paso 7: ejecutar la consulta (boton de buscar o 'Apply').

Sub-paso 8: en los resultados, buscar la columna de 'Unit value' o 'Valor unitario', que normalmente se expresa en dolares americanos (USD) por tonelada o por la unidad relevante para ese producto.

Sub-paso 9: anotar ese valor unitario en USD, y la unidad de medida exacta (por tonelada, por kilo, por docena, segun corresponda al producto).

Sub-paso 10: convertir el precio de USD a CAD dividiendo entre 1,33 (el USD/CAD promedio aproximado del periodo de analisis; si se quiere mayor precision, se puede usar el promedio real calculado a partir del archivo USDCAD\_2020\_2024.xlsx de la Tarea 2, una vez que este disponible).

Sub-paso 11: repetir los Sub-pasos 4 a 10 para cada uno de los 10 productos, cambiando el codigo HS en cada consulta.

**6.4.4 Fuentes alternativas por tipo de producto**

Para algunos productos, TradeMap puede no tener un valor unitario suficientemente especifico o actualizado. En esos casos, usar las siguientes fuentes complementarias, siguiendo la misma logica de los Sub-pasos anteriores (buscar el dato, anotar la fuente y la fecha, convertir a CAD si es necesario):

Para rosas y otras flores frescas cortadas: buscar en Google 'ASOCOLFLORES precio exportacion flores Canada 2024', y revisar si el gremio publica reportes de precios de referencia por tipo de flor.

Para cafe: buscar 'FNC precio referencia exportacion cafe 2024'. La Federacion Nacional de Cafeteros publica periodicamente el precio interno de referencia, que sirve como base, ajustandolo si es necesario por el diferencial de calidad para exportacion.

Para medicamentos corticosteroides: buscar 'Colombia medicamentos exportacion Canada precio unitario', y revisar si bases de datos de comercio exterior especializadas en el sector farmaceutico (como IQVIA, si hay acceso, o reportes sectoriales de ANDI) tienen el dato.

Para frutas tropicales (guayaba/mango), carbon bituminoso, medias/calcetines de fibra sintetica, accesorios de tuberia de hierro/acero, filetes de trucha congelados, y nueces y semillas preparadas: si TradeMap no da un valor unitario claro, intentar con la base de datos de Comtrade de Naciones Unidas (comtrade.un.org), que tiene una cobertura similar a TradeMap y puede servir como verificacion cruzada. Para el carbon bituminoso en particular, tener en cuenta que es un commodity a granel cotizado normalmente por tonelada en mercados especializados (ej. indices de precio de carbon termico/coquizable), lo cual puede dar una referencia mas precisa que el valor unitario generico de TradeMap.

**6.4.5 Formato final del archivo**

Excel con 10 filas y las columnas: numero, producto, codigo HS, precio de referencia en USD (con su unidad de medida), tipo de cambio USD/CAD usado para la conversion, precio de referencia en CAD (con la misma unidad de medida), fuente (URL), fecha de consulta. Guardar como tabla\_B4\_precios\_referencia.xlsx en MIC-CC/data/raw/.

**6.4.6 Verificacion de calidad**

Verificacion 1: 10 filas, cada una con un precio positivo (mayor a cero).

Verificacion 2: los precios son razonables para el tipo de producto. Por ejemplo, un kilo de rosas frescas no deberia costar 0,001 CAD (demasiado bajo) ni 1.000 CAD (demasiado alto); comparar mentalmente el orden de magnitud del resultado contra lo que parece razonable para ese tipo de bien.

Verificacion 3: cada fila tiene la fuente y la fecha de consulta documentadas.

Verificacion 4: si se uso la conversion de USD a CAD, el tipo de cambio usado esta anotado explicitamente en la fila correspondiente.

## **Tarea 5: Tabla de sensibilidad de margenes brutos (3 escenarios)**

**6.5.1 Que es esta tarea**

Construir una tabla preliminar en Excel, fuera de Python, que muestre el margen bruto de cada uno de los 10 productos bajo los tres escenarios de tipo de cambio (base, optimista, pesimista). En total son 30 filas: 10 productos por 3 escenarios. Esta tabla sirve como verificacion manual antes de construir la version definitiva en Python, en la Etapa 6 del Bloque B.

**6.5.2 La logica que hace que esta tabla muestre sensibilidad real**

Este es el punto mas importante y mas facil de hacer mal en toda la Tarea 5, asi que se explica con especial cuidado. Los costos de produccion de un exportador colombiano (mano de obra, tierra, insumos nacionales, transporte interno hasta el puerto) estan denominados en pesos colombianos, y NO cambian cuando se mueve el tipo de cambio COP/CAD. En cambio, el ingreso del exportador esta denominado en CAD, y al convertirse a pesos colombianos para comparar con los costos, SI cambia segun el tipo de cambio vigente.

Por esa razon, el costo de produccion debe calcularse UNA SOLA VEZ, usando el tipo de cambio del escenario base, y ese mismo valor en pesos debe usarse, sin recalcularlo, en los tres escenarios. Si por error se recalcula el costo de produccion en cada escenario usando el tipo de cambio de ese escenario, el resultado final mostraria un margen identico (40% en los tres casos, por ejemplo) en lugar de mostrar la sensibilidad real que se busca.

**6.5.3 Sub-pasos del calculo, producto por producto**

Sub-paso 1: calcular el tipo de cambio COP/CAD base. Formula (corregida, ver nota de correccion de la Seccion 3.2): TRM mas reciente disponible en el archivo de la Tarea 1, multiplicada por 1 dividido entre el USD/CAD mas reciente disponible en el archivo de la Tarea 2 (es decir, hay que INVERTIR el dato del Bank of Canada antes de multiplicar, porque ese dato viene expresado en CAD por 1 USD, no en USD por 1 CAD). Este calculo se hace una sola vez para todo el conjunto de productos, no producto por producto.

**Nota importante sobre esta version simplificada del COP/CAD base:** por simplicidad, esta Tarea 5 manual usa el valor mas reciente de un solo dia (spot) como COP/CAD base. La version definitiva en Python (Etapa 6 del Bloque B, Seccion 7.6.3) usa en cambio el promedio movil de los ultimos 90 dias, tal como se explica en la Seccion 3.5, porque es una base menos sensible a que el ultimo dia disponible haya sido, por casualidad, un dia atipico. Esta diferencia es intencional: la tabla\_B5 de esta tarea es una verificacion manual rapida y aproximada, no tiene que coincidir exactamente en cifras con la tabla\_05 que se construye despues en Python. Lo que si debe coincidir entre ambas es la LOGICA (el costo fijo, el orden optimista \> base \> pesimista), no los numeros exactos.

Sub-paso 2: a partir del COP/CAD base del Sub-paso 1, calcular el COP/CAD optimista: COP/CAD base multiplicado por 1,10.

Sub-paso 3: calcular el COP/CAD pesimista: COP/CAD base multiplicado por 0,85.

Sub-paso 4: para el primer producto de la lista, tomar el precio en CAD de la tabla\_B4\_precios\_referencia.xlsx (Tarea 4).

Sub-paso 5: calcular el costo de produccion en pesos para ese producto, usando exclusivamente el COP/CAD base: costo\_COP \= precio\_CAD x COP/CAD\_base x 0,60. El factor 0,60 (60%) es un supuesto preliminar de que los costos de produccion representan, en promedio, un 60% del valor de venta.

**Limitacion metodologica del factor 0,60 (documentada, no resuelta — julio 2026):** este 0,60 se aplica identico a los 10 productos del Top 10, pese a que son sectores con estructuras de costo muy distintas (un commodity a granel como el carbon bituminoso, farmaceuticos, flores perecederas, textiles). A diferencia de las tasas de interes, los episodios historicos o el porcentaje de Drawback (todos con fuente y fecha de consulta documentadas en sus respectivas tareas), este 0,60 no tiene una fuente citada ni un origen sectorial diferenciado: es un supuesto de conveniencia, no un dato investigado. La tabla\_B9\_estructura\_costos.xlsx de la Tarea 9 SI diferencia cada producto, pero unicamente en la proporcion de ese costo que es importada versus nacional (usado en la Etapa 8, cobertura natural); no aporta un ratio de costo total sobre precio distinto por producto, asi que no resuelve esta limitacion. Si en el futuro se consigue informacion sectorial real de margenes o estructura de costos por producto (por ejemplo, de gremios como la Federacion Nacional de Cafeteros, ASOCOLFLORES, o reportes de la industria minera para el carbon), este factor deberia diferenciarse por producto en vez de usar un unico valor fijo. Mientras eso no exista, cualquier lectura de margen o breakeven de este modelo debe tratarse como una aproximacion de primer orden, sensible a este supuesto, y no como una cifra de costo real verificada producto por producto.

Sub-paso 6: anotar ese costo\_COP calculado en el Sub-paso 5\. Este mismo numero se va a usar, sin cambios, en las tres filas correspondientes a este producto (escenario base, optimista, pesimista).

Sub-paso 7: para el escenario base, calcular el ingreso: ingreso\_COP \= precio\_CAD x COP/CAD\_base.

Sub-paso 8: calcular el margen en pesos para el escenario base: margen\_COP \= ingreso\_COP \- costo\_COP (usando el costo\_COP fijo del Sub-paso 5).

Sub-paso 9: calcular el margen en porcentaje: margen\_% \= (margen\_COP / ingreso\_COP) x 100\.

Sub-paso 10: repetir los Sub-pasos 7, 8 y 9 para el escenario optimista, usando el COP/CAD optimista del Sub-paso 2 en lugar del base, pero usando el mismo costo\_COP fijo del Sub-paso 5\.

Sub-paso 11: repetir los Sub-pasos 7, 8 y 9 para el escenario pesimista, usando el COP/CAD pesimista del Sub-paso 3, y de nuevo el mismo costo\_COP fijo.

Sub-paso 12: repetir los Sub-pasos 4 a 11 completos para cada uno de los 9 productos restantes.

**6.5.4 Ejemplo numerico completo, paso a paso (producto: rosas)**

Supongamos los siguientes datos de entrada: precio\_CAD \= 2,00 CAD por kilo (de la Tarea 4). COP/CAD base \= 3.200 (resultado del Sub-paso 1, valor de ejemplo).

Aplicando el Sub-paso 2: COP/CAD optimista \= 3.200 x 1,10 \= 3.520.

Aplicando el Sub-paso 3: COP/CAD pesimista \= 3.200 x 0,85 \= 2.720.

Aplicando el Sub-paso 5 (costo de produccion, calculado una sola vez):

costo\_COP \= 2,00 x 3.200 x 0,60 \= 3.840 COP por kilo

Fila 1, escenario base (Sub-pasos 7 a 9):

ingreso\_COP \= 2,00 x 3.200 \= 6.400

margen\_COP \= 6.400 \- 3.840 \= 2.560

margen\_% \= 2.560 / 6.400 x 100 \= 40,0%

Fila 2, escenario optimista (Sub-paso 10, usando COP/CAD \= 3.520 y el costo\_COP fijo de 3.840):

ingreso\_COP \= 2,00 x 3.520 \= 7.040

margen\_COP \= 7.040 \- 3.840 \= 3.200

margen\_% \= 3.200 / 7.040 x 100 \= 45,5%

Fila 3, escenario pesimista (Sub-paso 11, usando COP/CAD \= 2.720 y el costo\_COP fijo de 3.840):

ingreso\_COP \= 2,00 x 2.720 \= 5.440

margen\_COP \= 5.440 \- 3.840 \= 1.600

margen\_% \= 1.600 / 5.440 x 100 \= 29,4%

Verificacion logica de este resultado: el margen sube cuando el CAD se aprecia (escenario optimista, 45,5%) y baja cuando el CAD se deprecia (escenario pesimista, 29,4%), porque el costo en pesos se mantuvo fijo en 3.840 en las tres filas, pero el ingreso si vario. Esa es exactamente la sensibilidad cambiaria que esta tabla debe mostrar. Si en algun producto el margen sale identico en los tres escenarios, hay un error: probablemente el costo de produccion se recalculo con el tipo de cambio de cada escenario, en lugar de mantenerse fijo.

**6.5.5 Formato final del archivo**

Excel de 30 filas con columnas: numero, producto, codigo HS, escenario (base/optimista/pesimista), COP/CAD usado en ese escenario, precio\_CAD, costo de produccion en COP (debe repetirse identico en las tres filas del mismo producto), ingreso en COP, margen bruto en COP, margen bruto en %. Guardar como tabla\_B5\_sensibilidad\_margenes.xlsx en MIC-CC/outputs/tables/.

**6.5.6 Verificacion de calidad**

Verificacion 1: exactamente 30 filas (10 productos x 3 escenarios).

Verificacion 2: el costo de produccion en COP es identico en las tres filas correspondientes a cada producto. Revisar esto producto por producto antes de dar la tarea por terminada.

Verificacion 3: para cada producto, el margen en porcentaje del escenario optimista es mayor que el del escenario base, y el del escenario base es mayor que el del escenario pesimista. Si esto no se cumple en algun producto, hay un error en la formula de ese producto especifico y debe corregirse antes de continuar.

Verificacion 4: ningun ingreso en COP es igual a cero (lo cual generaria un error de division por cero al calcular el margen en porcentaje).

## **Tarea 6: Episodios historicos de devaluacion del peso colombiano (stress testing)**

**6.6.1 Que es esta tarea y para que sirve**

Documentar entre 4 y 6 episodios historicos (entre 2008 y 2025\) en los que la TRM (COP/USD) tuvo un movimiento grande y sostenido, sea de devaluacion o de apreciacion del peso colombiano. Esta informacion alimenta el Modulo de Stress Testing Historico (Etapa 9 del Bloque B), que aplica estos porcentajes de cambio reales a los margenes del modelo, en lugar de depender solo de los escenarios arbitrarios \+10%/-15% de la Tarea 5\.

**6.6.2 Episodios de referencia, como punto de partida**

Esta tarea no empieza de cero: hay tres episodios ampliamente documentados en la historia economica reciente de Colombia que sirven como punto de partida obligatorio, y que se deben verificar con fuentes oficiales antes de buscar episodios adicionales.

| Periodo aproximado | Movimiento aproximado | Causa principal a verificar |
| ----- | ----- | ----- |
| 2014-2016 | TRM de \~1.900 a \~3.400 (cerca de 80%) | Caida del precio internacional del petroleo, que afecta los ingresos de divisas de Colombia por ser un pais exportador relevante de crudo. |
| 2020 | TRM de \~3.300 a \~4.150 (cerca de 25%) | Inicio de la pandemia de COVID-19, con salida masiva de capitales de mercados emergentes y caida adicional del precio del petroleo. |
| 2022 | TRM superando los 5.000 en momentos puntuales | Subidas agresivas de tasas de interes en Estados Unidos, que fortalecen el dolar globalmente, combinadas con incertidumbre politica local en Colombia. |

**6.6.3 Sub-pasos de ejecucion**

Sub-paso 1: ir a la herramienta de consulta historica de la TRM en el Banco de la Republica (la misma usada en la Tarea 1, www.banrep.gov.co, seccion Estadisticas \> Tasas de cambio \> TRM).

Sub-paso 2: para el primer episodio de referencia (2014-2016), ajustar el rango de fechas a 01/06/2014 hasta 31/12/2016, y consultar.

Sub-paso 3: identificar dentro de los resultados el valor de la TRM mas cercano al inicio del periodo de devaluacion (alrededor de mediados de 2014\) y el valor mas cercano al pico mas alto alcanzado (normalmente a comienzos de 2016).

Sub-paso 4: anotar esas dos fechas exactas y sus valores de TRM correspondientes.

Sub-paso 5: calcular el porcentaje de cambio: ((TRM\_final \- TRM\_inicial) / TRM\_inicial) x 100\.

Sub-paso 6: abrir una pestana nueva y buscar en Google 'TRM historica devaluacion peso colombiano 2014 2016 causas' para encontrar una fuente periodistica o academica que explique la causa del movimiento (prensa economica como Portafolio, La Republica, Dinero, o informes de politica monetaria del Banco de la Republica).

Sub-paso 7: redactar una descripcion breve (1 a 2 lineas) de la causa principal, basada en lo encontrado en el Sub-paso 6, y anotar la fuente con su URL.

Sub-paso 8: repetir los Sub-pasos 2 a 7 para el episodio de 2020, ajustando el rango de fechas a aproximadamente febrero a abril de 2020 (el periodo mas agudo del salto cambiario por la pandemia), y para el episodio de 2022, ajustando el rango de fechas a lo largo de todo ese ano.

Sub-paso 9: una vez verificados los tres episodios de referencia, buscar entre 2 y 3 episodios adicionales. Para esto, consultar la serie completa de la TRM desde 2008 (ajustando el rango de fechas de la herramienta del BanRep a 01/01/2008 hasta la fecha mas reciente disponible), y revisar visualmente, mirando el grafico o la tabla de valores, en que periodos se observan subidas o bajadas sostenidas y pronunciadas, distintas a las tres ya identificadas.

Sub-paso 10: para cada episodio adicional encontrado en el Sub-paso 9, repetir el proceso completo de los Sub-pasos 3 a 7: identificar fechas exactas, calcular porcentaje de cambio, y documentar la causa con una fuente periodistica o academica.

Sub-paso 11: si es posible, incluir al menos un episodio de apreciacion fuerte del peso (es decir, un periodo en el que el dolar bajo frente al peso de forma sostenida), para que el conjunto de episodios no este sesgado unicamente hacia devaluaciones.

**6.6.4 Formato final del archivo**

Excel con entre 4 y 6 filas (una por episodio) y las columnas: nombre del episodio, fecha de inicio, fecha de fin, TRM al inicio, TRM al final, porcentaje de cambio, tipo de movimiento (devaluacion o apreciacion), causa principal (1-2 lineas), fuente (URL), fecha de consulta. Guardar como tabla\_B6\_episodios\_historicos.xlsx en MIC-CC/data/raw/.

**6.6.5 Verificacion de calidad**

Verificacion 1: entre 4 y 6 episodios documentados, ni menos ni mas.

Verificacion 2: los tres episodios de referencia (2014-2016, 2020, 2022\) estan incluidos y sus valores de TRM coinciden, dentro de un margen razonable, con los valores aproximados de la tabla de la Seccion 6.6.2.

Verificacion 3: el porcentaje de cambio de cada episodio esta calculado correctamente con la formula del Sub-paso 5\.

Verificacion 4: cada episodio tiene una causa explicada en lenguaje sencillo, con al menos una fuente periodistica o academica documentada.

## **Tarea 7: Instrumentos de cobertura cambiaria disponibles para PYMEs**

**6.7.1 Que es esta tarea y para que sirve**

Investigar que instrumentos financieros de cobertura cambiaria (forwards, NDF, opciones) ofrecen los bancos colombianos a empresas exportadoras, especialmente a PYMEs, y bajo que condiciones. Esta informacion, junto con la de la Tarea 8, alimenta el Modulo de Costo-Beneficio de Cobertura (Etapa 11 del Bloque B), que recomienda si conviene o no cubrirse del riesgo cambiario.

**6.7.2 Sub-pasos de ejecucion, banco por banco**

Este procedimiento se repite para al menos 3 bancos colombianos. A continuacion se describe una sola vez y se aplica a cada banco.

Sub-paso 1: en el navegador, buscar en Google el nombre del banco junto con 'cobertura cambiaria empresas' o 'tesoreria forward NDF'. Por ejemplo: 'Bancolombia cobertura cambiaria empresas forward'.

Sub-paso 2: entrar a la pagina oficial del banco (verificar que la URL corresponde al dominio oficial del banco, no a un sitio de terceros) y buscar la seccion de banca empresarial, banca corporativa, o tesoreria.

Sub-paso 3: dentro de esa seccion, buscar productos relacionados con 'derivados', 'cobertura de riesgo cambiario', 'forward', o 'NDF'.

Sub-paso 4: leer la descripcion del producto ofrecido y anotar: el nombre exacto del instrumento (forward, NDF, opcion, u otro), una descripcion breve de como funciona segun lo que explica el banco, si se menciona un monto minimo de operacion, que plazos se ofrecen (30, 60, 90 dias, u otros), y si hay algun requisito o segmento especifico para PYMEs (algunos bancos solo ofrecen estos productos a partir de cierto tamano de empresa o cierto volumen de operaciones).

Sub-paso 5: si la pagina del banco incluye algun costo indicativo, una calculadora de puntos forward, o un rango de tarifas, anotarlo. Si no se encuentra ningun costo explicito (lo cual es comun, porque los bancos normalmente cotizan el costo de forma personalizada al cliente), no es un problema: marcar como 'no publicado' y continuar, porque ese costo se puede estimar despues con los datos de la Tarea 8\.

Sub-paso 6: anotar la URL exacta de la pagina consultada y la fecha de consulta.

Sub-paso 7: repetir los Sub-pasos 1 a 6 para al menos dos bancos adicionales, recomendando usar al menos tres entre los siguientes: Bancolombia, Davivienda, BBVA Colombia, Banco de Bogota.

**6.7.3 Fuentes institucionales adicionales**

Sub-paso 8: buscar en Google 'Banco de la Republica guia cobertura cambiaria exportadores'. El Banco de la Republica, como autoridad monetaria, a veces publica material educativo sobre gestion de riesgo cambiario dirigido a empresas.

Sub-paso 9: buscar tambien 'BVC derivados cambiarios PYME'. La Bolsa de Valores de Colombia (BVC) puede tener informacion sobre el mercado de derivados cambiarios y su acceso para empresas de menor tamano.

Sub-paso 10: si alguna de estas dos busquedas (Sub-pasos 8 y 9\) aporta informacion relevante adicional, agregarla como una fila mas en la tabla, siguiendo el mismo formato que las filas de los bancos.

**6.7.4 Formato final del archivo**

Excel con al menos 3 filas (una por entidad o fuente investigada) y las columnas: entidad o fuente, instrumento (forward/NDF/opcion/otro), descripcion breve de como funciona, monto minimo si se menciona, plazos disponibles si se mencionan, requisitos para PYMEs si se mencionan, costo indicativo si se menciona, fuente (URL), fecha de consulta. Guardar como tabla\_B7\_instrumentos\_cobertura.xlsx en MIC-CC/data/raw/.

**6.7.5 Verificacion de calidad**

Verificacion 1: al menos 3 entidades o fuentes distintas investigadas.

Verificacion 2: cada fila tiene una descripcion entendible de como funciona el instrumento, redactada con palabras propias, no copiada literalmente de la pagina del banco.

Verificacion 3: los campos que no se encontraron estan marcados explicitamente como 'no publicado', no dejados en blanco.

## **Tarea 8: Tasas de interes Colombia vs Canada**

**6.8.1 Que es esta tarea y para que sirve**

Recopilar la serie historica del IBR (Indicador Bancario de Referencia) de Colombia y de la tasa de politica monetaria del Bank of Canada, de forma mensual, desde enero de 2020 hasta el mes mas reciente disponible. Esta informacion alimenta dos modulos del Bloque B: el Costo de Capital de Trabajo (Etapa 10\) y el Costo-Beneficio de Cobertura (Etapa 11).

**6.8.2 Sub-pasos de ejecucion para el IBR de Colombia**

Sub-paso 1: ir a www.banrep.gov.co.

Sub-paso 2: en el menu de Estadisticas, buscar la seccion de tasas de interes, y dentro de ella, buscar especificamente 'IBR' (puede aparecer como 'Indicador Bancario de Referencia').

Sub-paso 3: si la herramienta de consulta del IBR permite elegir un rango de fechas, configurar desde 01/01/2020 hasta la fecha mas reciente disponible en 2026\.

Sub-paso 4: si los datos se muestran de forma diaria, no es necesario copiar cada dia: basta con tomar el valor correspondiente al primer dia habil de cada mes, o el promedio mensual si la herramienta lo ofrece directamente, para construir una serie mensual.

Sub-paso 5: descargar o copiar los valores mensuales a una hoja de Excel, en dos columnas: fecha (mes y ano) e IBR Colombia en porcentaje.

Sub-paso 6: si la herramienta del BanRep no es clara, buscar en Google 'Banco de la Republica IBR historico' como alternativa de busqueda.

**6.8.3 Sub-pasos de ejecucion para la tasa del Bank of Canada**

Sub-paso 7: ir a www.bankofcanada.ca.

Sub-paso 8: buscar en el menu o en el buscador interno 'Interest rates' o 'Policy interest rate'.

Sub-paso 9: localizar la tabla o el grafico historico de la tasa de politica monetaria (tambien llamada 'overnight rate' o 'bank rate').

Sub-paso 10: anotar el valor vigente al inicio de cada mes, desde enero de 2020 hasta el mes mas reciente disponible. Como esta tasa cambia con menor frecuencia que el IBR (el Bank of Canada solo la modifica en sus reuniones de politica monetaria, que ocurren varias veces al ano, no todos los meses), es normal que el mismo valor se repita durante varios meses seguidos hasta la siguiente decision de politica.

Sub-paso 11: si no se encuentra una tabla historica completa de forma directa, otra opcion es usar la Valet API del Bank of Canada, la misma herramienta usada en la Tarea 2, pero con un codigo de serie distinto para la tasa de politica monetaria; buscar en Google 'Bank of Canada Valet API policy interest rate series code' para identificar el codigo vigente.

**6.8.4 Construir la tabla final combinada**

Sub-paso 12: combinar las dos series (IBR Colombia y tasa Bank of Canada) en una sola tabla de Excel, alineadas por fecha (mes y ano).

Sub-paso 13: agregar una columna de diferencial, calculada como: IBR Colombia menos tasa Bank of Canada, en puntos porcentuales, para cada mes.

Sub-paso 14: agregar dos columnas de fuente (una para el IBR y otra para la tasa de Canada), con sus respectivas URLs, y una columna de fecha de consulta.

**6.8.5 Formato final del archivo**

Excel con columnas: fecha (mes y ano), IBR Colombia (%), tasa Bank of Canada (%), diferencial (IBR menos tasa de Canada, en puntos porcentuales), fuente IBR (URL), fuente Canada (URL), fecha de consulta. Guardar como tabla\_B8\_tasas\_interes.xlsx en MIC-CC/data/raw/.

**6.8.6 Verificacion de calidad**

Verificacion 1: cobertura mensual (o trimestral si los datos mensuales no estan disponibles) desde enero de 2020 hasta el dato mas reciente, sin huecos mayores a un mes consecutivo.

Verificacion 2: el diferencial esta calculado correctamente como IBR menos tasa de Canada en cada fila.

Verificacion 3: ambas fuentes (IBR y tasa de Canada) estan documentadas con URL.

Verificacion 4: los valores del IBR son consistentemente mayores a los de la tasa de Canada durante la mayor parte del periodo (esto es lo que se observa historicamente entre Colombia y Canada, dado el diferencial estructural de tasas entre ambas economias; si se observa lo contrario de forma sistematica, revisar si las series se cargaron correctamente o si hay una confusion entre las dos columnas).

## **Tarea 9: Estructura de costos por producto (cobertura natural)**

**6.9.1 Que es esta tarea y para que sirve**

Estimar, para cada uno de los 10 productos, que porcentaje de los costos de produccion corresponde a insumos importados (vinculados al dolar) y que porcentaje corresponde a insumos nacionales (en pesos). Esta informacion alimenta el Modulo de Cobertura Natural (Etapa 8 del Bloque B), que reconoce que los productos con mas insumos importados sufren menos el impacto de una devaluacion, porque sus costos tambien suben en pesos al mismo tiempo que su ingreso.

**6.9.2 Sub-pasos de ejecucion, producto por producto**

Este procedimiento se repite para cada uno de los 10 productos. A continuacion se describe una sola vez.

Sub-paso 1: para el producto que se esta analizando, hacer una lista mental o escrita de los principales insumos fisicos que se usan para producirlo. Por ejemplo, para flores: fertilizantes, agroquimicos (fungicidas, insecticidas), sustratos, materiales de empaque, mano de obra, tierra, energia, agua. Para cafe: fertilizantes, mano de obra de recoleccion, transporte interno, procesamiento (trilla). Para confecciones: telas, hilos, botones y accesorios, maquinaria, mano de obra. Para farmaceuticos: principios activos, excipientes, material de empaque, mano de obra especializada.

Sub-paso 2: para cada insumo de la lista del Sub-paso 1, determinar si normalmente se produce dentro de Colombia (lo cual implica que su costo esta en pesos colombianos) o si normalmente se importa (lo cual implica que su costo esta en dolares o vinculado al dolar, incluso si la factura final se paga en pesos, porque el precio de importacion sigue el tipo de cambio).

Sub-paso 3: buscar en Google un termino especifico para el sector del producto, combinando el nombre del gremio relevante con 'estructura de costos' o 'costos de produccion insumos importados'. Por ejemplo, para flores: 'Asocolflores estructura de costos cultivo flores'. Para cafe: 'FNC costos de produccion cafe Colombia insumos importados'. Para confecciones: 'Inexmoda estructura de costos confeccion Colombia materias primas importadas'. Para aceite de palma: 'Fedepalma costos de produccion insumos importados'. Para farmaceuticos: 'ANDI farmaceutica Colombia principios activos importados porcentaje costos'.

Sub-paso 4: revisar los resultados de esa busqueda y, si se encuentra un estudio, reporte sectorial, o presentacion que desglose la estructura de costos con un porcentaje especifico de insumos importados, anotar ese porcentaje y la fuente.

Sub-paso 5: si no se encuentra un porcentaje exacto para el producto especifico que se esta investigando, pero si se encuentra para un producto similar del mismo sector (por ejemplo, no hay un dato especifico de crisantemos pero si de rosas, ambos productos de floricultura con estructuras de costos similares), usar ese porcentaje como estimacion, y anotarlo explicitamente en la columna de notas, indicando de que producto se tomo la referencia.

Sub-paso 6: calcular el porcentaje de insumos nacionales como el complemento: 100% menos el porcentaje de insumos importados encontrado en el Sub-paso 4 o 5\.

Sub-paso 7: en la tabla de Excel, anotar para este producto: los principales insumos importados identificados (lista breve), los principales insumos nacionales identificados (lista breve), el porcentaje de costos en insumos importados, el porcentaje de costos en insumos nacionales, la fuente con URL, la fecha de consulta, y si aplica, la nota de que el dato es una estimacion basada en un producto similar.

Sub-paso 8: repetir los Sub-pasos 1 a 7 para cada uno de los 10 productos.

**6.9.3 Nota especifica sobre el sector minero (carbon de coque)**

Para el carbon de coque, la mineria utiliza principalmente maquinaria importada como activo fijo de largo plazo (excavadoras, equipos de perforacion), no como un insumo recurrente que se compra en cada ciclo de produccion como ocurre con los fertilizantes en la agricultura. Por esa razon, este producto puede requerir un tratamiento distinto: documentar esta particularidad como una nota en la fila correspondiente, en lugar de forzar un porcentaje de insumos importados recurrentes que no refleja bien la realidad de este sector.

**6.9.4 Formato final del archivo**

Excel con 10 filas y las columnas: numero (1-10), producto, codigo HS, principales insumos importados (lista breve), principales insumos nacionales (lista breve), porcentaje de costos en insumos importados, porcentaje de costos en insumos nacionales (los dos porcentajes deben sumar 100%), fuente (URL), fecha de consulta, notas. Guardar como tabla\_B9\_estructura\_costos.xlsx en MIC-CC/data/raw/.

**6.9.5 Verificacion de calidad**

Verificacion 1: 10 filas, una por producto.

Verificacion 2: en cada fila, el porcentaje de insumos importados mas el porcentaje de insumos nacionales suma exactamente 100%.

Verificacion 3: cada fila tiene al menos una fuente, incluso si esa fuente corresponde a un producto similar usado como referencia (en ese caso, debe estar claramente explicado en la columna de notas).

Verificacion 4: los insumos importados y nacionales estan listados de forma especifica (por ejemplo 'fertilizantes, agroquimicos'), no de forma generica como simplemente 'insumos importados' sin mayor detalle.

# **7\. Bloque B: construccion del modelo en Python, sub-paso por sub-paso**

Esta seccion contiene las 12 etapas de construccion del modelo financiero en Google Colab. Cada etapa se desglosa en sub-pasos que incluyen: que hace cada celda de codigo, por que se escribe asi, que se espera ver como resultado al ejecutarla, y como verificar que el resultado es correcto antes de pasar a la siguiente celda. Esta seccion asume que las nueve tablas del Bloque A ya estan completas y guardadas en MIC-CC/data/raw/.

## **7.0 Antes de empezar: revision conceptual obligatoria**

Antes de escribir la primera linea de codigo, responder por escrito, en no mas de tres oraciones cada una, las siguientes preguntas, usando como referencia la Seccion 3 de esta guia: que es la TRM y de donde se obtiene; como se calcula el COP/CAD a partir de la TRM y el USD/CAD; que mide la volatilidad cambiaria; que significa el VaR al 95% a 30 dias; que es el tipo de cambio de equilibrio; que es la cobertura natural; que es el costo de capital de trabajo.

Si alguna de estas preguntas no se puede responder con claridad y en lenguaje propio (no copiando la definicion textual), volver a leer la Seccion 3 correspondiente antes de continuar. El motivo de este paso es que el codigo de Python que sigue no tiene sentido si no se entiende que es lo que cada celda esta calculando.

## **7.1 Etapa 1: Configurar el entorno de trabajo (Dia 11\)**

**7.1.1 Que es Google Colab**

Google Colab (Colaboratory) es un servicio gratuito de Google que permite escribir y ejecutar codigo en lenguaje Python directamente desde el navegador, sin necesidad de instalar Python ni ningun programa adicional en el computador. El codigo se organiza en 'celdas', que se ejecutan una por una, y los resultados (numeros, tablas, graficas) aparecen justo debajo de cada celda despues de ejecutarla. El archivo donde se guarda todo este trabajo se llama 'notebook', y tiene la extension .ipynb.

**7.1.2 Sub-pasos para crear el notebook**

Sub-paso 1: abrir el navegador y escribir en la barra de direcciones: colab.research.google.com

Sub-paso 2: iniciar sesion con la cuenta de Google que se va a usar para todo el proyecto (la misma cuenta que tiene acceso a la carpeta MIC-CC en Drive).

Sub-paso 3: en la pantalla de inicio de Colab, buscar la opcion 'Nuevo notebook' o 'New notebook', normalmente en una ventana emergente o en el menu 'Archivo' \> 'Nuevo notebook'.

Sub-paso 4: una vez creado el notebook en blanco, hacer clic en el nombre del archivo (normalmente algo como 'Untitled0.ipynb') en la parte superior izquierda, y cambiarlo a: 04\_financial\_model.ipynb

Sub-paso 5: ir al menu 'Archivo' (File) y seleccionar 'Guardar una copia en Drive' o 'Save a copy in Drive', para asegurarse de que el notebook queda vinculado a Google Drive y no solo en un estado temporal.

Sub-paso 6: una vez guardado en Drive, normalmente queda en una carpeta llamada 'Colab Notebooks' dentro de Drive. Es necesario moverlo a la carpeta correcta del proyecto: ir a Drive, localizar el archivo 04\_financial\_model.ipynb dentro de Colab Notebooks, y arrastrarlo (o usar la opcion 'Mover a' / 'Move to') hasta la carpeta MIC-CC/notebooks/.

Sub-paso 7: confirmar que el archivo aparece correctamente dentro de MIC-CC/notebooks/ navegando hasta esa carpeta en Drive.

**7.1.3 Sub-pasos para verificar las librerias necesarias**

Las librerias son colecciones de codigo ya escrito que se usan dentro de Python para tareas especificas (calculos numericos, manejo de tablas, graficas, descargas de internet). Google Colab ya trae preinstaladas la mayoria de las librerias necesarias para este proyecto, pero conviene verificarlo antes de avanzar.

Sub-paso 1: hacer clic en la primera celda del notebook (la celda vacia que aparece por defecto).

Sub-paso 2: escribir exactamente el siguiente codigo dentro de esa celda:

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import requests

print('Librerias cargadas correctamente')

Sub-paso 3: ejecutar la celda. Esto se hace presionando las teclas Shift \+ Enter al mismo tiempo, o haciendo clic en el boton de 'Play' (un triangulo) que aparece a la izquierda de la celda.

Sub-paso 4: observar el resultado que aparece debajo de la celda. Si todo esta correcto, debe aparecer el texto: Librerias cargadas correctamente

Sub-paso 5: si en cambio aparece un mensaje de error en texto rojo que empieza con 'ModuleNotFoundError', significa que alguna de las librerias no esta instalada en ese entorno de Colab. Identificar el nombre de la libreria mencionada en el mensaje de error.

Sub-paso 6: en una celda nueva (hacer clic en el boton '+ Codigo' que aparece al pasar el mouse por debajo de la celda actual), escribir: \!pip install nombre\_de\_la\_libreria (reemplazando 'nombre\_de\_la\_libreria' por el nombre exacto que aparecio en el error).

Sub-paso 7: ejecutar esa celda de instalacion con Shift \+ Enter, y esperar a que termine (puede tardar entre 10 segundos y 2 minutos dependiendo de la libreria).

Sub-paso 8: una vez instalada, ir al menu 'Entorno de ejecucion' (Runtime) y seleccionar 'Reiniciar entorno de ejecucion' (Restart runtime).

Sub-paso 9: despues de reiniciar, volver a ejecutar la celda original de importacion de librerias (Sub-paso 2\) para confirmar que ahora si funciona sin errores.

## **7.2 Etapa 2: Descargar el USD/CAD del Bank of Canada via API (Dia 11\)**

**7.2.1 Por que el notebook descarga este dato de nuevo si ya se obtuvo en la Tarea 2**

En la Tarea 2 del Bloque A, el archivo USDCAD\_2020\_2024.xlsx se obtuvo de forma manual, copiando o convirtiendo datos desde el navegador. Aqui, dentro del notebook, se vuelve a obtener el mismo dato, pero de forma automatica, usando codigo que llama directamente a la API del Bank of Canada. La razon de hacerlo dos veces es la reproducibilidad: cualquier persona que descargue este notebook desde GitHub y lo ejecute, sin haber hecho la Tarea 2 manualmente, va a poder obtener el mismo dato automaticamente, sin depender de un archivo Excel que solo existe en el Drive de Manuela. Esto es una buena practica fundamental en ciencia de datos abierta y reproducible.

**7.2.2 Sub-pasos de la celda de codigo**

Sub-paso 1: en una celda nueva del notebook, escribir el siguiente codigo, que define una funcion (un bloque de codigo reutilizable) llamada descargar\_usdcad:

def descargar\_usdcad(start='2020-01-01', end='2024-12-31'):

    url \= ('https://www.bankofcanada.ca/valet/observations'

           f'/FXUSDCAD/json?start\_date={start}\&end\_date={end}')

    respuesta \= requests.get(url, timeout=30)

    datos \= respuesta.json()\['observations'\]

    filas \= \[{'fecha': o\['d'\], 'USDCAD': float(o\['FXUSDCAD'\]\['v'\])} for o in datos\]

    df \= pd.DataFrame(filas)

    df\['fecha'\] \= pd.to\_datetime(df\['fecha'\])

    return df.sort\_values('fecha').reset\_index(drop=True)

Sub-paso 2: ejecutar esa celda con Shift \+ Enter. No debe aparecer ningun resultado visible todavia, porque solo se esta definiendo la funcion, no llamandola.

Sub-paso 3: en una celda nueva, escribir el codigo que llama a la funcion y muestra un resumen del resultado:

boc\_df \= descargar\_usdcad()

print(f'Registros: {len(boc\_df)}, promedio USD/CAD: {boc\_df\["USDCAD"\].mean():.4f}')

Sub-paso 4: ejecutar esa celda. Debe tardar pocos segundos (es una sola solicitud a internet).

Sub-paso 5: observar el resultado impreso. Debe verse algo similar a: Registros: 1254, promedio USD/CAD: 1.3204

**7.2.3 Verificacion de calidad del resultado**

Verificacion 1: el numero de registros debe ser cercano a 1.254 (el numero aproximado de dias habiles bursatiles entre el 1 de enero de 2020 y el 31 de diciembre de 2024). Un numero muy distinto, como 50 o 5.000, indica un problema con el rango de fechas o con la frecuencia de los datos devueltos.

Verificacion 2: el promedio de USD/CAD debe estar entre 1,25 y 1,45, consistente con el rango esperado explicado en la Seccion 3.2 y verificado en la Tarea 2 del Bloque A.

**7.2.4 Que hacer si aparece un error**

Si aparece KeyError: 'FXUSDCAD': significa que el codigo de la serie cambio en la API del Bank of Canada. Buscar en Google 'Bank of Canada Valet API FXUSDCAD 2024' o revisar la documentacion oficial en bankofcanada.ca/valet/docs para encontrar el codigo de serie vigente, y reemplazarlo en la URL de la funcion del Sub-paso 1\.

Si aparece un error de tipo ConnectionError o Timeout: puede ser un problema temporal de conexion a internet desde el entorno de Colab. Volver a ejecutar la misma celda (Sub-paso 4); si el error persiste despues de tres intentos, esperar unos minutos y volver a intentar, porque puede ser un problema temporal del servidor del Bank of Canada.

Si el numero de registros es muy distinto al esperado pero no hay ningun error visible: revisar que las fechas 'start' y 'end' dentro de la funcion (Sub-paso 1\) esten escritas correctamente, en el formato AAAA-MM-DD.

## **7.3 Etapa 3: Cargar la TRM y construir la serie COP/CAD (Dia 12\)**

**7.3.1 Que hace esta etapa**

Esta es la etapa que construye el dato central de todo el modelo: la serie diaria del tipo de cambio COP/CAD, explicada conceptualmente en la Seccion 3.2. Combina el archivo TRM\_COP\_USD\_2020\_2024.xlsx (Tarea 1 del Bloque A) con la serie boc\_df descargada en la Etapa 2, multiplicando ambas series segun la formula de tasa cruzada.

**7.3.2 Sub-pasos para conectar Google Drive con el notebook**

Sub-paso 1: en una celda nueva, escribir:

from google.colab import drive

drive.mount('/content/drive')

Sub-paso 2: ejecutar la celda con Shift \+ Enter.

Sub-paso 3: va a aparecer una ventana emergente pidiendo autorizacion para que Colab acceda a la cuenta de Google Drive. Hacer clic en 'Conectar con Google Drive' o 'Connect to Google Drive'.

Sub-paso 4: seleccionar la cuenta de Google correcta (la misma que tiene la carpeta MIC-CC) y otorgar los permisos solicitados.

Sub-paso 5: una vez completada la autorizacion, debe aparecer en el notebook el mensaje: Mounted at /content/drive

**7.3.3 Sub-pasos para cargar el archivo de la TRM**

Sub-paso 6: en una celda nueva, escribir el siguiente codigo para cargar el archivo Excel de la TRM:

ruta \= '/content/drive/MyDrive/MIC-CC/data/raw/TRM\_COP\_USD\_2020\_2024.xlsx'

trm\_raw \= pd.read\_excel(ruta)

trm\_raw.head(10)

Sub-paso 7: ejecutar la celda. Debe aparecer una tabla con las primeras 10 filas del archivo de la TRM.

Sub-paso 8: observar los nombres de las columnas que aparecen en esa tabla. Dependiendo de como el Banco de la Republica estructuro el archivo descargado en la Tarea 1, es posible que las primeras filas no sean datos sino texto descriptivo (titulos, notas), en cuyo caso la tabla se va a ver desordenada o con columnas sin nombre claro (Unnamed: 0, Unnamed: 1, etc).

Sub-paso 9: si la tabla se ve desordenada, es necesario indicarle a Python que omita las primeras filas que no son datos. Modificar la celda del Sub-paso 6 agregando el parametro skiprows, probando con distintos valores hasta que la tabla se vea correcta. Por ejemplo:

trm\_raw \= pd.read\_excel(ruta, skiprows=8)

Sub-paso 10: volver a ejecutar la celda con distintos valores de skiprows (probar con 0, despues 6, despues 8, despues 10\) hasta que trm\_raw.head(10) muestre claramente dos columnas: una de fechas y una de valores numericos de la TRM, sin texto descriptivo mezclado.

Sub-paso 11: una vez que la tabla se ve correcta, identificar los nombres exactos de las dos columnas (pueden llamarse 'Fecha (dd/mm/aaaa)' y 'Valor', o nombres similares dependiendo del formato exacto del archivo del BanRep).

Sub-paso 12: renombrar esas columnas a nombres simples y estandar para el resto del codigo, escribiendo una celda como la siguiente (ajustando los nombres originales entre comillas segun lo observado en el Sub-paso 11):

trm\_raw \= trm\_raw.rename(columns={'Fecha (dd/mm/aaaa)': 'fecha', 'Valor': 'TRM'})

trm\_raw \= trm\_raw\[\['fecha', 'TRM'\]\].dropna()

trm\_raw\['fecha'\] \= pd.to\_datetime(trm\_raw\['fecha'\], dayfirst=True)

Sub-paso 13: ejecutar esa celda y verificar con trm\_raw.head() y trm\_raw.tail() que las fechas y los valores se ven correctos al inicio y al final de la tabla.

**7.3.4 Sub-pasos para combinar las dos series y calcular el COP/CAD**

Sub-paso 14: en una celda nueva, escribir el codigo que une (merge) las dos tablas por la columna de fecha, y calcula el COP/CAD. Recordar que el dato 'USDCAD' que llega de la API del Bank of Canada esta en CAD por 1 USD, asi que hay que invertirlo antes de multiplicar (ver la nota de correccion de la Seccion 3.2):

fx \= pd.merge(trm\_raw, boc\_df, on='fecha', how='inner')

fx\['USD\_CAD'\] \= 1 / fx\['USDCAD'\]

fx\['COPCAD'\] \= fx\['TRM'\] \* fx\['USD\_CAD'\]

fx \= fx.sort\_values('fecha').reset\_index(drop=True)

print(fx\[\['fecha','TRM','USDCAD','USD\_CAD','COPCAD'\]\].describe())

Sub-paso 15: ejecutar la celda. El resultado de describe() muestra estadisticas resumen (conteo, promedio, minimo, maximo, etc.) de las columnas numericas.

Sub-paso 16: revisar el conteo (count) que aparece para la columna COPCAD: debe ser cercano a 1.240 filas (el numero de fechas que coinciden exactamente entre la TRM y el USD/CAD, considerando que ambos paises tienen festivos distintos, asi que el numero final de filas combinadas es ligeramente menor a las 1.254 filas individuales de cada serie).

Sub-paso 17: revisar el valor minimo y maximo de COPCAD en el resultado de describe(): deben estar dentro del rango aproximado de 2.300 a 3.800 (rango historico real 2020-2024, unificado con la Etapa 6 y la Etapa 7 de esta guia). Si el valor sale muy por encima de ese rango (por ejemplo, cercano a la TRM misma o mayor), es casi seguro que el dato de USDCAD no se invirtio antes de multiplicar.

**7.3.5 Guardar el resultado**

Sub-paso 18: en una celda nueva, guardar la tabla fx como un archivo Excel en la carpeta de datos procesados:

fx.to\_excel('/content/drive/MyDrive/MIC-CC/data/processed/fx\_COPCAD\_2020\_2024.xlsx', index=False)

print('Archivo guardado correctamente')

Sub-paso 19: ejecutar la celda y confirmar el mensaje de exito.

Sub-paso 20: ir a Drive y verificar visualmente que el archivo fx\_COPCAD\_2020\_2024.xlsx aparece dentro de MIC-CC/data/processed/.

**7.3.6 Que hacer si algo no funciona**

Si el merge (Sub-paso 14\) resulta en una tabla con muy pocas filas (por ejemplo, menos de 100): es muy probable que las fechas de las dos tablas no esten en el mismo formato (una como texto y otra como fecha real), o que tengan una diferencia de horas/zona horaria. Revisar que ambas columnas de fecha sean del tipo datetime de pandas (se puede verificar con trm\_raw.dtypes y boc\_df.dtypes), y que no haya espacios en blanco adicionales en los datos de fecha.

Si aparecen muchas filas con valores NaN (vacios) en COPCAD despues del merge: esto puede ser normal hasta cierto punto, porque los festivos de Colombia y Canada no coinciden exactamente. Calcular que porcentaje de filas tiene NaN; si es menor al 2% del total, se puede continuar sin problema. Si es mayor, revisar el formato de fechas de ambas series con mas cuidado.

## **7.4 Etapa 4: Calcular la volatilidad cambiaria (Dia 13\)**

**7.4.1 Sub-pasos del calculo**

Sub-paso 1: en una celda nueva, calcular los retornos diarios (el cambio porcentual del COP/CAD de un dia para el siguiente, usando el logaritmo natural, que es la convencion estandar en finanzas para este tipo de calculo):

fx\_retornos \= fx.copy()

fx\_retornos\['retorno'\] \= np.log(fx\_retornos\['COPCAD'\] / fx\_retornos\['COPCAD'\].shift(1))

fx\_retornos \= fx\_retornos.dropna(subset=\['retorno'\])

Sub-paso 2: ejecutar la celda. No debe aparecer ningun error; esta celda no imprime nada por si misma.

Sub-paso 3: en una celda nueva, calcular la volatilidad diaria y anualizada:

vol\_diaria \= fx\_retornos\['retorno'\].std()

vol\_anual \= vol\_diaria \* np.sqrt(252)

print(f'Volatilidad diaria: {vol\_diaria\*100:.3f}%')

print(f'Volatilidad anualizada: {vol\_anual\*100:.2f}%')

Sub-paso 4: ejecutar la celda y leer los dos numeros impresos.

**7.4.2 Verificacion de calidad del resultado**

Verificacion 1: la volatilidad anualizada debe estar entre 8% y 18%, consistente con lo explicado en la Seccion 3.3.

Verificacion 2: si el numero sale por debajo de 5%, es probable que haya un error en el calculo de los retornos (por ejemplo, calcular una diferencia simple en lugar de un cambio porcentual logaritmico).

Verificacion 3: si el numero sale por encima de 25%, revisar si hay valores atipicos extremos en la serie de COPCAD (por ejemplo, un valor erroneo de TRM o de USD/CAD que haya quedado sin corregir desde el Bloque A) que esten distorsionando el calculo de la desviacion estandar.

**7.4.3 Calcular la volatilidad por ano, para mayor detalle**

Sub-paso 5: en una celda nueva, agregar una columna de ano y calcular la volatilidad separada para cada ano del periodo:

fx\_retornos\['ano'\] \= fx\_retornos\['fecha'\].dt.year

vol\_por\_ano \= fx\_retornos.groupby('ano')\['retorno'\].std() \* np.sqrt(252) \* 100

print(vol\_por\_ano.round(2))

Sub-paso 6: ejecutar la celda y observar el resultado, que debe mostrar un valor de volatilidad para cada ano de 2020 a 2024\. Es de esperar que 2020 muestre una volatilidad mas alta que el resto, por la pandemia, lo cual sirve como una verificacion adicional de que el calculo tiene sentido.

## **7.5 Etapa 5: Calcular el VaR historico al 95% (Dia 13\)**

**7.5.1 Sub-pasos del calculo**

Sub-paso 1: en una celda nueva, calcular el VaR diario usando el percentil 5 de los retornos:

var\_diario \= np.percentile(fx\_retornos\['retorno'\], 5\)

print(f'VaR diario: {var\_diario\*100:.3f}%')

Sub-paso 2: ejecutar la celda y observar el resultado. Debe ser un numero negativo (porque representa una perdida), tipicamente entre \-0,8% y \-1,5%.

Sub-paso 3: en una celda nueva, escalar el VaR diario a los horizontes de 30, 60 y 90 dias usando la regla de la raiz del tiempo, explicada en la Seccion 3.4:

var\_30d \= var\_diario \* np.sqrt(30)

var\_60d \= var\_diario \* np.sqrt(60)

var\_90d \= var\_diario \* np.sqrt(90)

print(f'VaR 30d: {var\_30d\*100:.2f}%')

print(f'VaR 60d: {var\_60d\*100:.2f}%')

print(f'VaR 90d: {var\_90d\*100:.2f}%')

Sub-paso 4: ejecutar la celda y observar los tres resultados, que deben ser numeros progresivamente mas negativos (mayor perdida potencial) a medida que aumenta el horizonte de tiempo, lo cual tiene sentido logico: a mas tiempo de exposicion, mayor el riesgo acumulado.

**7.5.2 Guardar la tabla de indicadores de riesgo**

Sub-paso 5: en una celda nueva, construir y guardar una tabla con los cinco indicadores calculados hasta ahora (volatilidad anual y los cuatro valores de VaR):

indicadores \= pd.DataFrame({

    'indicador': \['Volatilidad anualizada', 'VaR diario (95%)', 'VaR 30 dias (95%)',

                   'VaR 60 dias (95%)', 'VaR 90 dias (95%)'\],

    'valor\_%': \[vol\_anual\*100, var\_diario\*100, var\_30d\*100, var\_60d\*100, var\_90d\*100\],

    'interpretacion': \[

        'Variabilidad esperada del COP/CAD en un ano tipico',

        'Perdida maxima esperada en 1 dia, con 95% de confianza',

        'Perdida maxima esperada en 30 dias, con 95% de confianza',

        'Perdida maxima esperada en 60 dias, con 95% de confianza',

        'Perdida maxima esperada en 90 dias, con 95% de confianza'\]

})

indicadores.to\_excel('/content/drive/MyDrive/MIC-CC/outputs/tables/tabla\_04\_indicadores\_riesgo.xlsx', index=False)

indicadores

Sub-paso 6: ejecutar la celda. Debe mostrarse la tabla completa con los cinco indicadores, y el archivo debe quedar guardado en Drive.

Sub-paso 7: ir a Drive y confirmar visualmente que tabla\_04\_indicadores\_riesgo.xlsx aparece en MIC-CC/outputs/tables/.

## **7.6 Etapa 6: Escenarios y 60 margenes (Dia 14\)**

**7.6.1 Que hace esta etapa y por que es la mas extensa del modelo**

Esta etapa replica en Python, mejorada y a mayor escala, el calculo que ya se hizo manualmente en la Tarea 5 del Bloque A (tabla\_B5\_sensibilidad\_margenes.xlsx). La diferencia es que en Python el calculo se hace de forma sistematica para los 10 productos y para las DOS rutas logisticas (Cartagena-Montreal y Cartagena-Vancouver), lo cual produce 10 productos x 2 rutas x 3 escenarios \= 60 combinaciones, en lugar de las 30 de la tabla preliminar del Bloque A (que solo consideraba un escenario de costos sin diferenciar por ruta).

**7.6.2 Preparar la tabla de productos con sus datos de entrada**

Antes de calcular los escenarios, es necesario tener, dentro de Python, una tabla (DataFrame) que reuna, para cada uno de los 10 productos: el precio de venta en CAD (de la Tarea 4 del Bloque A) y los costos logisticos para cada una de las dos rutas (de la dimension logistica del proyecto, completada en una fase anterior).

Sub-paso 1: cargar el archivo de precios de referencia (Tarea 4\) en una celda nueva:

ruta\_precios \= '/content/drive/MyDrive/MIC-CC/data/raw/tabla\_B4\_precios\_referencia.xlsx'

precios \= pd.read\_excel(ruta\_precios)

precios.head(10)

Sub-paso 2: ejecutar la celda y revisar que la tabla se ve correctamente, con las columnas esperadas (numero, producto, codigo HS, precio en USD, tipo de cambio usado, precio en CAD, fuente, fecha de consulta).

Sub-paso 3: si los nombres de las columnas en el archivo no coinciden exactamente con los que el codigo va a usar mas adelante (producto, precio\_cad), renombrarlas:

precios \= precios.rename(columns={'Producto': 'producto', 'Precio CAD': 'precio\_cad'})

Sub-paso 4: cargar tambien los costos logisticos por ruta, en el archivo MIC-CC/data/raw/costos\_logisticos\_rutas.xlsx (heredado de la fase logistica del proyecto). **Aviso importante:** este archivo NO trae, como podria asumirse, un costo en pesos ya calculado por producto y ruta. Es una tabla de cotizaciones de flete maritimo por CONTENEDOR completo (20 o 40 pies, por naviera, con las 4 combinaciones de ruta y sentido posibles), sin ninguna asociacion a un producto especifico. Convertir esto a un costo por kilogramo (la misma unidad en la que estan cotizados los 10 productos en tabla\_B4) requiere varias decisiones explicitas:

\- Usar solo las cotizaciones en sentido de EXPORTACION (Cartagena hacia el destino); descartar las de sentido contrario (importacion hacia Colombia).

\- Usar el contenedor de 20 pies, no el de 40, por ser el supuesto mas realista para el perfil de PYME exportadora que atiende este proyecto (Seccion 2.1).

\- Si hay varias cotizaciones para la misma ruta (distintas navieras), promediarlas.

\- Asumir una capacidad de carga util de 20.000 kg por contenedor de 20 pies (aproximacion estandar de la industria para carga general; el archivo no reporta peso de carga, solo tarifa por contenedor).

\- Convertir la tarifa (en USD) a COP usando la TRM mas reciente disponible en la propia serie del modelo, para no introducir una fuente de tipo de cambio adicional.

**Limitacion metodologica importante (documentada, no resuelta — julio 2026):** este modelo de costo por kilogramo, calculado a partir de tarifas de contenedor para carga general, no es apropiado para un commodity que en la realidad se transporta a granel (bulk carrier), como el Carbon bituminoso. Aplicarle esta tarifa produce un costo logistico por kilogramo muy por encima de lo que ese producto realmente vale, y genera margenes negativos extremos (hasta \-348% en la ruta a Vancouver) que no reflejan una conclusion de negocio real, sino un limite de la metodologia de calculo de flete. Estos resultados deben presentarse siempre acompanados de esta advertencia, y no deben usarse para afirmar que el carbon bituminoso "no es viable" como producto de exportacion sin antes conseguir una tarifa de flete a granel real. Los otros 9 productos de este Top 10 si se transportan razonablemente en contenedor, asi que la metodologia es apropiada para ellos.

Sub-paso 5: combinar la tabla de precios con la tabla de costos logisticos, uniendolas por el nombre del producto (o por el codigo HS, que es mas confiable porque no depende de que el nombre este escrito exactamente igual en ambos archivos):

productos \= pd.merge(precios, costos\_logisticos, on='codigo\_hs', how='inner')

productos.head(10)

Sub-paso 6: ejecutar la celda y verificar que la tabla resultante productos tiene exactamente 10 filas (una por producto) y contiene, como minimo, las columnas: producto, codigo\_hs, precio\_cad, costo\_logistico\_mtl, costo\_logistico\_yvr.

**7.6.3 Calcular los tres tipos de cambio de escenario**

Sub-paso 7: en una celda nueva, calcular el COP/CAD base como el promedio movil de 90 dias, tomando el ultimo valor disponible de esa serie:

fx\['COPCAD\_base\_roll'\] \= fx\['COPCAD'\].rolling(window=90).mean()

copcad\_base \= fx\['COPCAD\_base\_roll'\].dropna().iloc\[-1\]

print(f'COP/CAD base (promedio movil 90 dias): {copcad\_base:.2f}')

Sub-paso 8: ejecutar la celda y observar el valor impreso. Debe estar dentro del rango esperado de 2.300 a 3.800 (rango unificado con la Etapa 3 y la Etapa 7 de esta guia).

Sub-paso 9: en una celda nueva, calcular los escenarios optimista y pesimista a partir del base:

copcad\_optimista \= copcad\_base \* 1.10

copcad\_pesimista \= copcad\_base \* 0.85

print(f'Optimista: {copcad\_optimista:.2f}  |  Base: {copcad\_base:.2f}  |  Pesimista: {copcad\_pesimista:.2f}')

Sub-paso 10: ejecutar la celda y verificar que el valor optimista es mayor que el base, y el base es mayor que el pesimista.

**7.6.4 Calcular el costo de produccion fijo por producto**

Igual que en la Tarea 5 del Bloque A, el costo de produccion debe calcularse una sola vez, con el escenario base, y mantenerse fijo en los tres escenarios.

Sub-paso 11: en una celda nueva, agregar la columna de costo de produccion a la tabla productos:

productos\['costo\_produccion\_cop'\] \= productos\['precio\_cad'\] \* copcad\_base \* 0.60

productos\[\['producto','precio\_cad','costo\_produccion\_cop'\]\]

Sub-paso 12: ejecutar la celda y revisar los valores de costo\_produccion\_cop para los 10 productos: todos deben ser numeros positivos, y proporcionales al precio\_cad de cada producto (productos con precio mas alto deben tener tambien costo de produccion mas alto).

**7.6.5 Construir el bucle que genera las 60 combinaciones**

Esta es la parte central de la etapa: un bucle (loop) en Python que recorre cada producto, cada ruta, y cada escenario, calculando el margen en cada combinacion.

Sub-paso 13: en una celda nueva, escribir el codigo completo del bucle:

filas \= \[\]

escenarios \= {'Base': copcad\_base, 'Optimista': copcad\_optimista, 'Pesimista': copcad\_pesimista}

rutas \= {'CTG-Montreal': 'costo\_logistico\_mtl', 'CTG-Vancouver': 'costo\_logistico\_yvr'}

for \_, p in productos.iterrows():

    for ruta, col\_costo in rutas.items():

        for esc, tc in escenarios.items():

            ingreso \= p\['precio\_cad'\] \* tc

            costo\_total \= p\['costo\_produccion\_cop'\] \+ p\[col\_costo\]

            margen\_cop \= ingreso \- costo\_total

            margen\_pct \= margen\_cop / ingreso \* 100

            filas.append({'producto': p\['producto'\], 'ruta': ruta, 'escenario': esc,

                           'COPCAD': tc, 'ingreso\_cop': ingreso,

                           'costo\_total\_cop': costo\_total,

                           'margen\_cop': margen\_cop, 'margen\_pct': margen\_pct})

tabla\_margenes \= pd.DataFrame(filas)

print(f'Numero de filas generadas: {len(tabla\_margenes)}')

Sub-paso 14: antes de ejecutar, leer el codigo con calma para entender la logica: el bucle externo recorre cada uno de los 10 productos (for \_, p in productos.iterrows()); dentro de cada producto, recorre las dos rutas (for ruta, col\_costo in rutas.items()); y dentro de cada ruta, recorre los tres escenarios (for esc, tc in escenarios.items()). Esto produce 10 x 2 x 3 \= 60 iteraciones totales, cada una generando una fila de resultado.

Sub-paso 15: ejecutar la celda. El resultado impreso debe decir: Numero de filas generadas: 60

Sub-paso 16: si el numero impreso no es 60, revisar primero cuantas filas tiene la tabla productos (debe ser 10\) ejecutando len(productos) en una celda nueva; si no es 10, el problema viene de la Etapa 7.6.2 (la combinacion de precios y costos logisticos), no de esta etapa.

**7.6.6 Verificar los resultados antes de guardar**

Sub-paso 17: en una celda nueva, revisar visualmente una muestra de la tabla resultante:

tabla\_margenes.head(15)

Sub-paso 18: ejecutar y revisar que cada producto aparece con sus dos rutas y sus tres escenarios, con valores de margen\_pct que tienen sentido (numeros entre \-50% y 70% aproximadamente serian razonables para este tipo de analisis; valores extremos como 5.000% o \-10.000% indicarian un error).

Sub-paso 19: en una celda nueva, verificar de forma sistematica que, para cada producto y cada ruta, el margen del escenario optimista es mayor que el del base, y el del base es mayor que el del pesimista (la misma logica de verificacion que se aplico manualmente en la Tarea 5):

verificacion \= tabla\_margenes.pivot\_table(index=\['producto','ruta'\], columns='escenario', values='margen\_pct')

verificacion\['orden\_correcto'\] \= (verificacion\['Optimista'\] \> verificacion\['Base'\]) & (verificacion\['Base'\] \> verificacion\['Pesimista'\])

print(verificacion\['orden\_correcto'\].value\_counts())

Sub-paso 20: ejecutar la celda. El resultado debe mostrar que todas las 20 combinaciones de producto-ruta (10 productos x 2 rutas) tienen orden\_correcto \= True. Si alguna sale False, revisar ese producto y ruta especificos en la tabla completa para identificar el error.

**7.6.7 Guardar el resultado final de esta etapa**

Sub-paso 21: en una celda nueva, guardar la tabla completa:

tabla\_margenes.to\_excel('/content/drive/MyDrive/MIC-CC/outputs/tables/tabla\_05\_margenes\_escenarios.xlsx', index=False)

print('Archivo guardado correctamente')

Sub-paso 22: ejecutar la celda y confirmar el mensaje de exito. Ir a Drive y verificar que tabla\_05\_margenes\_escenarios.xlsx aparece en MIC-CC/outputs/tables/.

**7.6.8 Una nota sobre los margenes negativos**

Es enteramente normal, y de hecho es uno de los resultados mas importantes que el modelo busca mostrar, que algunos productos tengan margen negativo en el escenario pesimista, especialmente en la ruta mas costosa (normalmente Vancouver, por ser una ruta logisticamente mas larga o con mas escalas desde Cartagena). Un margen negativo en pesimista no es un error del calculo: es informacion valiosa, porque le dice al exportador que ese producto especifico, bajo esa ruta especifica, es vulnerable a una depreciacion del CAD del orden de 15%. Antes de asumir que un margen negativo es un error, revisar primero si tiene sentido dado el producto y la ruta.

## **7.7 Etapa 7: Modulo de Tipo de Cambio de Equilibrio \- breakeven (Dia 15\)**

**7.7.1 Que calcula esta etapa**

Para cada producto y cada ruta, el valor exacto del COP/CAD en el cual el margen neto se vuelve cero (concepto explicado en la Seccion 3.6), y una clasificacion de riesgo en formato semaforo (Verde, Amarillo, Rojo) segun que tan cerca esta ese punto de equilibrio del tipo de cambio actual y del peor escenario considerado por el VaR.

**7.7.2 Sub-pasos del calculo**

Sub-paso 1: en una celda nueva, calcular el breakeven para cada producto y cada ruta, usando la formula de la Seccion 3.6 (costo total dividido entre precio en CAD):

productos\['breakeven\_mtl'\] \= (productos\['costo\_produccion\_cop'\] \+ productos\['costo\_logistico\_mtl'\]) / productos\['precio\_cad'\]

productos\['breakeven\_yvr'\] \= (productos\['costo\_produccion\_cop'\] \+ productos\['costo\_logistico\_yvr'\]) / productos\['precio\_cad'\]

productos\[\['producto','breakeven\_mtl','breakeven\_yvr'\]\]

Sub-paso 2: ejecutar la celda y revisar los valores. La mayoria deben ser numeros dentro de un rango similar al rango del COP/CAD historico real (aproximadamente 2.300 a 3.800, mismo rango de la Etapa 3 y la Etapa 6); si algun valor sale negativo, revisar los datos de costo y precio de ese producto especifico. Un breakeven por ENCIMA de ese rango historico (incluso muy por encima) no es necesariamente un error: significa que, con los costos actuales, ese producto no seria rentable ni siquiera al COP/CAD mas alto observado en 2020-2024 — es una senal real de vulnerabilidad estructural (por ejemplo, un costo logistico calculado con un supuesto que no encaja con ese producto especifico), no un fallo de calculo. Antes de asumir que es un error, revisar si el costo de produccion o logistico de ese producto tiene sentido dado el tipo de bien.

Sub-paso 3: en una celda nueva, calcular el tipo de cambio correspondiente al peor escenario segun el VaR a 90 dias (calculado en la Etapa 5):

copcad\_var90 \= copcad\_base \* (1 \+ var\_90d)

print(f'COP/CAD en el peor escenario VaR 90d: {copcad\_var90:.2f}')

Sub-paso 4: ejecutar la celda. Como var\_90d es un numero negativo, este calculo da como resultado un COP/CAD menor que el base, representando una depreciacion del CAD.

Sub-paso 5: en una celda nueva, definir la funcion que clasifica el riesgo de cada producto comparando su breakeven contra los tres niveles de referencia (VaR 90 dias, escenario pesimista, y el propio breakeven):

def clasificar\_riesgo(breakeven):

    if copcad\_var90 \< breakeven:

        return 'Rojo'

    elif copcad\_pesimista \< breakeven:

        return 'Amarillo'

    else:

        return 'Verde'

productos\['riesgo\_mtl'\] \= productos\['breakeven\_mtl'\].apply(clasificar\_riesgo)

productos\['riesgo\_yvr'\] \= productos\['breakeven\_yvr'\].apply(clasificar\_riesgo)

productos\[\['producto','riesgo\_mtl','riesgo\_yvr'\]\]

Sub-paso 6: ejecutar la celda y leer el resultado. Entender la logica de la funcion: si el COP/CAD en el peor escenario del VaR (copcad\_var90) ya esta por debajo del breakeven de un producto, ese producto se clasifica en Rojo, porque incluso en el 95% de los casos historicos cubiertos por el VaR, ese producto ya perderia dinero en el peor 5% de escenarios. Si el escenario pesimista (-15%) esta por debajo del breakeven, pero el VaR no llega tan lejos, se clasifica en Amarillo. Si ni siquiera el escenario pesimista llega al breakeven, se clasifica en Verde, el producto mas resiliente.

**Limitacion importante de este semaforo (documentada, no resuelta):** el breakeven y la clasificacion Verde/Amarillo/Rojo de esta etapa se calculan sobre el costo de produccion y logistico "crudo" de la Etapa 6, ANTES de aplicar el efecto amortiguador de la cobertura natural (Etapa 8) o el beneficio del Drawback de IVA (Etapa 12). Un producto puede aparecer en una categoria mas riesgosa aqui de la que realmente tiene una vez se incorporan esos dos ajustes, que solo mejoran el margen, nunca lo empeoran. Al redactar el Working Paper o comunicar estos resultados, se debe aclarar explicitamente que este semaforo es una fotografia previa a la cobertura natural y al Drawback, no la conclusion final del modelo — la tabla\_11\_margen\_final\_ajustado.xlsx (Etapa 12) es la que refleja el margen mas completo y realista.

**7.7.3 Guardar el resultado**

Sub-paso 7: en una celda nueva, guardar la tabla con las columnas relevantes de esta etapa:

tabla\_breakeven \= productos\[\['producto','codigo\_hs','breakeven\_mtl','riesgo\_mtl','breakeven\_yvr','riesgo\_yvr'\]\]

tabla\_breakeven.to\_excel('/content/drive/MyDrive/MIC-CC/outputs/tables/tabla\_06\_breakeven.xlsx', index=False)

print('Archivo guardado correctamente')

Sub-paso 8: ejecutar y confirmar que el archivo aparece en Drive, en MIC-CC/outputs/tables/.

## **7.8 Etapa 8: Modulo de Cobertura Natural (Dia 16\)**

**7.8.1 Que calcula esta etapa**

Ajusta el calculo de margenes reconociendo que, segun la tabla\_B9\_estructura\_costos.xlsx de la Tarea 9, una parte de los costos de produccion de cada producto esta en insumos importados (dolar-vinculados), y por lo tanto esa parte tambien varia con el tipo de cambio, en lugar de mantenerse fija como se asumio en la Etapa 6 (concepto explicado en la Seccion 3.8).

**7.8.2 Sub-pasos de carga de la tabla de costos**

Sub-paso 1: cargar el archivo de la Tarea 9 en una celda nueva:

ruta\_costos \= '/content/drive/MyDrive/MIC-CC/data/raw/tabla\_B9\_estructura\_costos.xlsx'

costos \= pd.read\_excel(ruta\_costos)

costos.head(10)

Sub-paso 2: ejecutar la celda y verificar que las columnas relevantes existen: producto (o codigo\_hs), porcentaje de costos en insumos importados, porcentaje en insumos nacionales. Renombrar si es necesario, siguiendo el mismo procedimiento que en etapas anteriores.

costos \= costos.rename(columns={'% de costos en insumos importados': 'pct\_importado',

                                 '% de costos en insumos nacionales': 'pct\_nacional'})

Sub-paso 3: si los porcentajes en el archivo original estan expresados como numeros enteros (por ejemplo 40 en lugar de 0,40), convertirlos a decimales para que las formulas funcionen correctamente:

costos\['pct\_importado'\] \= costos\['pct\_importado'\] / 100

costos\['pct\_nacional'\] \= costos\['pct\_nacional'\] / 100

Sub-paso 4: verificar que para cada fila, pct\_importado mas pct\_nacional suma 1,0 (equivalente al 100% verificado manualmente en la Tarea 9):

costos\['suma\_check'\] \= costos\['pct\_importado'\] \+ costos\['pct\_nacional'\]

print(costos\['suma\_check'\].between(0.99, 1.01).all())

Sub-paso 5: ejecutar la celda. El resultado debe ser True. Si es False, revisar fila por fila cual producto no suma correctamente y corregir el archivo de la Tarea 9\.

**7.8.3 Aplicar el ajuste a la tabla de margenes**

Sub-paso 6: combinar la tabla de margenes (de la Etapa 6\) con la tabla de costos recien cargada, y con los datos de costo de produccion de la tabla productos:

tabla\_margenes \= tabla\_margenes.merge(costos\[\['producto','pct\_importado','pct\_nacional'\]\], on='producto')

tabla\_margenes \= tabla\_margenes.merge(productos\[\['producto','costo\_produccion\_cop'\]\], on='producto')

Sub-paso 7: ejecutar la celda. No debe arrojar error; si arroja un error de tipo 'merge keys', revisar que la columna 'producto' tenga exactamente el mismo texto (mismas mayusculas, mismos espacios) en ambas tablas que se estan combinando.

Sub-paso 8: en una celda nueva, calcular la parte de los costos que es importada y la parte que es nacional, en pesos, usando el costo de produccion base:

tabla\_margenes\['costo\_importado\_base'\] \= tabla\_margenes\['costo\_produccion\_cop'\] \* tabla\_margenes\['pct\_importado'\]

tabla\_margenes\['costo\_nacional'\] \= tabla\_margenes\['costo\_produccion\_cop'\] \* tabla\_margenes\['pct\_nacional'\]

Sub-paso 9: en una celda nueva, calcular como varia la parte importada del costo segun el escenario (porque esa parte si cambia con el tipo de cambio), mientras la parte nacional se mantiene fija:

tabla\_margenes\['costo\_importado\_esc'\] \= tabla\_margenes\['costo\_importado\_base'\] \* (tabla\_margenes\['COPCAD'\] / copcad\_base)

tabla\_margenes\['costo\_logistico'\] \= tabla\_margenes\['costo\_total\_cop'\] \- tabla\_margenes\['costo\_produccion\_cop'\]

tabla\_margenes\['costo\_total\_ajustado'\] \= (tabla\_margenes\['costo\_importado\_esc'\] \+ tabla\_margenes\['costo\_nacional'\] \+ tabla\_margenes\['costo\_logistico'\])

Sub-paso 10: en una celda nueva, recalcular el margen con este costo ajustado:

tabla\_margenes\['margen\_cop\_ajustado'\] \= tabla\_margenes\['ingreso\_cop'\] \- tabla\_margenes\['costo\_total\_ajustado'\]

tabla\_margenes\['margen\_pct\_ajustado'\] \= tabla\_margenes\['margen\_cop\_ajustado'\] / tabla\_margenes\['ingreso\_cop'\] \* 100

**7.8.4 Verificar el efecto de la cobertura natural**

Sub-paso 11: en una celda nueva, comparar el margen original (sin ajustar) contra el margen ajustado, para los productos con mayor porcentaje de insumos importados, en el escenario pesimista:

comparacion \= tabla\_margenes\[tabla\_margenes\['escenario'\]=='Pesimista'\]\[\['producto','pct\_importado','margen\_pct','margen\_pct\_ajustado'\]\]

comparacion \= comparacion.drop\_duplicates('producto').sort\_values('pct\_importado', ascending=False)

comparacion

Sub-paso 12: ejecutar la celda y revisar: para los productos con mayor pct\_importado, el margen\_pct\_ajustado debe ser mayor (es decir, menos negativo o menos reducido) que el margen\_pct sin ajustar, en el escenario pesimista. Esto confirma que la cobertura natural esta amortiguando el efecto cambiario tal como se explico conceptualmente en la Seccion 3.8. Si para los productos con mayor pct\_importado no se observa esta mejora, revisar la formula del Sub-paso 9\.

**7.8.5 Guardar el resultado**

Sub-paso 13: en una celda nueva, guardar la tabla con ambas versiones del margen para poder compararlas:

tabla\_margenes.to\_excel('/content/drive/MyDrive/MIC-CC/outputs/tables/tabla\_07\_cobertura\_natural.xlsx', index=False)

print('Archivo guardado correctamente')

Sub-paso 14: ejecutar y verificar en Drive.

## **7.9 Etapa 9: Modulo de Stress Testing Historico (Dia 17\)**

**7.9.1 Que calcula esta etapa**

Aplica a los margenes los porcentajes de cambio reales de los episodios historicos documentados en la Tarea 6 del Bloque A, en lugar de depender solo de los escenarios arbitrarios de la Etapa 6 (concepto explicado en la Seccion 3.7).

**7.9.2 Sub-pasos de carga y calculo**

Sub-paso 1: cargar el archivo de episodios historicos:

ruta\_episodios \= '/content/drive/MyDrive/MIC-CC/data/raw/tabla\_B6\_episodios\_historicos.xlsx'

episodios \= pd.read\_excel(ruta\_episodios)

episodios\[\['nombre del episodio','porcentaje de cambio'\]\]

Sub-paso 2: ejecutar y verificar que la columna de porcentaje de cambio existe y tiene valores numericos (renombrar a pct\_cambio si es necesario, igual que en etapas anteriores).

Sub-paso 3: en una celda nueva, escribir el bucle que aplica cada episodio a cada producto y cada ruta:

filas\_stress \= \[\]

for \_, ep in episodios.iterrows():

    copcad\_stress \= copcad\_base \* (1 \+ ep\['pct\_cambio'\] / 100\)

    for \_, p in productos.iterrows():

        for ruta, col\_costo in rutas.items():

            ingreso \= p\['precio\_cad'\] \* copcad\_stress

            costo\_total \= p\['costo\_produccion\_cop'\] \+ p\[col\_costo\]

            margen\_pct \= (ingreso \- costo\_total) / ingreso \* 100

            filas\_stress.append({'episodio': ep\['nombre del episodio'\], 'producto': p\['producto'\],

                                  'ruta': ruta, 'COPCAD\_stress': copcad\_stress, 'margen\_pct': margen\_pct})

tabla\_stress \= pd.DataFrame(filas\_stress)

print(f'Filas generadas: {len(tabla\_stress)}')

Sub-paso 4: ejecutar la celda. El numero de filas debe ser igual a (numero de episodios) x 10 productos x 2 rutas. Por ejemplo, con 5 episodios documentados, el resultado esperado es 5 x 10 x 2 \= 100 filas.

**7.9.3 Revisar los resultados mas extremos**

Sub-paso 5: en una celda nueva, identificar las combinaciones con el margen mas negativo, para confirmar que el modulo esta funcionando como se espera (debe mostrar resultados mas severos que el escenario pesimista de la Etapa 6, especialmente para el episodio de mayor devaluacion, como el de 2014-2016):

tabla\_stress.sort\_values('margen\_pct').head(10)

Sub-paso 6: ejecutar y revisar que los margenes mas negativos correspondan, logicamente, al episodio historico con mayor porcentaje de devaluacion documentado en la Tarea 6\.

**7.9.4 Guardar el resultado**

Sub-paso 7: en una celda nueva, guardar la tabla:

tabla\_stress.to\_excel('/content/drive/MyDrive/MIC-CC/outputs/tables/tabla\_08\_stress\_testing.xlsx', index=False)

print('Archivo guardado correctamente')

Sub-paso 8: ejecutar y verificar en Drive.

## **7.10 Etapa 10: Modulo de Costo de Capital de Trabajo (Dia 18\)**

**7.10.1 Que calcula esta etapa**

Cuantifica el costo financiero de mantener capital de trabajo en pesos colombianos mientras se espera el pago de la exportacion (30, 60 o 90 dias), usando el IBR colombiano de la Tarea 8, y lo descuenta del margen neto (concepto explicado en la Seccion 3.9).

**7.10.2 Sub-pasos de carga y calculo**

Sub-paso 1: cargar el archivo de tasas de interes:

ruta\_tasas \= '/content/drive/MyDrive/MIC-CC/data/raw/tabla\_B8\_tasas\_interes.xlsx'

tasas \= pd.read\_excel(ruta\_tasas)

tasas.tail(5)

Sub-paso 2: ejecutar y revisar las ultimas filas (el dato mas reciente) de la tabla de tasas.

Sub-paso 3: en una celda nueva, tomar el IBR mas reciente disponible y convertirlo a formato decimal:

ibr\_anual \= tasas\['IBR Colombia (%)'\].dropna().iloc\[-1\] / 100

ibr\_diaria \= ibr\_anual / 365  \# convencion Actual/365, estandar del mercado monetario local colombiano (IBR)

print(f'IBR anual usado: {ibr\_anual\*100:.2f}%')

**Nota sobre la convencion de dias usada (365 aqui, 360 en la Etapa 11):** el IBR colombiano se cotiza y se usa en el mercado local bajo la convencion Actual/365, por eso esta etapa divide entre 365. La Etapa 11 (puntos forward) en cambio usa la convencion Actual/360, porque ahi se esta calculando un diferencial de tasas para un instrumento de mercado FX internacional (forward/NDF), donde la convencion de mercado habitual para el dolar y otras monedas duras es Actual/360. No es un error ni una inconsistencia: son dos mercados distintos con convenciones distintas, pero conviene tenerlo presente porque es facil asumir por error que la misma tasa IBR deberia dividirse siempre entre el mismo numero.

Sub-paso 4: ejecutar y verificar que el numero impreso coincide con el ultimo valor visible en la tabla del Sub-paso 1\.

Sub-paso 5: en una celda nueva, calcular el costo financiero y el margen neto financiero para los tres horizontes de cobro, usando la formula de la Seccion 3.9:

for dias in \[30, 60, 90\]:

    col\_costo\_fin \= f'costo\_financiero\_{dias}d'

    col\_margen\_fin \= f'margen\_neto\_{dias}d'

    tabla\_margenes\[col\_costo\_fin\] \= tabla\_margenes\['costo\_total\_cop'\] \* ibr\_diaria \* dias

    tabla\_margenes\[col\_margen\_fin\] \= tabla\_margenes\['margen\_cop'\] \- tabla\_margenes\[col\_costo\_fin\]

tabla\_margenes\[\['producto','escenario','margen\_cop','margen\_neto\_30d','margen\_neto\_60d','margen\_neto\_90d'\]\].head(10)

Sub-paso 6: ejecutar la celda y revisar que, para cada fila, margen\_neto\_30d es mayor que margen\_neto\_60d, y este a su vez mayor que margen\_neto\_90d, porque a mas dias de espera, mayor el costo financiero acumulado, y por lo tanto menor el margen neto resultante.

**7.10.3 Guardar el resultado**

Sub-paso 7: en una celda nueva, guardar la tabla con las nuevas columnas:

tabla\_margenes.to\_excel('/content/drive/MyDrive/MIC-CC/outputs/tables/tabla\_09\_costo\_capital.xlsx', index=False)

print('Archivo guardado correctamente')

Sub-paso 8: ejecutar y verificar en Drive.

## **7.11 Etapa 11: Modulo de Costo-Beneficio de Cobertura Cambiaria (Dia 19\)**

**7.11.1 Que calcula esta etapa**

Compara, para cada producto y cada horizonte de tiempo, el costo estimado de cubrirse con un forward o NDF contra la perdida potencial que el VaR dice que se evitaria, y produce una recomendacion de cubrirse o no cubrirse (concepto explicado en la Seccion 3.10).

**7.11.2 Sub-pasos del calculo**

Sub-paso 1: en una celda nueva, obtener la tasa de interes de Canada del archivo de la Tarea 8 (de la misma forma que se obtuvo el IBR en la Etapa 10):

tasa\_canada\_anual \= tasas\['Tasa Bank of Canada (%)'\].dropna().iloc\[-1\] / 100

print(f'Tasa Canada usada: {tasa\_canada\_anual\*100:.2f}%')

Sub-paso 2: ejecutar y verificar el numero impreso contra la tabla original.

Sub-paso 3: en una celda nueva, calcular, para cada horizonte de tiempo, los puntos forward (el diferencial de tasas ajustado por el plazo), el costo de cobertura, la perdida potencial segun el VaR de ese horizonte, y la recomendacion final:

var\_dict \= {30: var\_30d, 60: var\_60d, 90: var\_90d}

for dias in \[30, 60, 90\]:

    puntos\_forward\_pct \= (ibr\_anual \- tasa\_canada\_anual) \* (dias / 360\)

    col\_costo\_cob \= f'costo\_cobertura\_{dias}d'

    col\_perdida\_var \= f'perdida\_var\_{dias}d'

    col\_recom \= f'recomendacion\_{dias}d'

    tabla\_margenes\[col\_costo\_cob\] \= abs(puntos\_forward\_pct) \* tabla\_margenes\['ingreso\_cop'\]

    tabla\_margenes\[col\_perdida\_var\] \= abs(var\_dict\[dias\]) \* tabla\_margenes\['ingreso\_cop'\]

    tabla\_margenes\[col\_recom\] \= np.where(

        tabla\_margenes\[col\_costo\_cob\] \< tabla\_margenes\[col\_perdida\_var\],

        'Cubrirse', 'No cubrirse')

Sub-paso 4: ejecutar la celda. No debe aparecer ningun error.

Sub-paso 5: en una celda nueva, revisar cuantas combinaciones recomiendan cubrirse versus no cubrirse, para cada horizonte:

for dias in \[30, 60, 90\]:

    col\_recom \= f'recomendacion\_{dias}d'

    print(f'--- Horizonte {dias} dias \---')

    print(tabla\_margenes\[col\_recom\].value\_counts())

Sub-paso 6: ejecutar y observar el patron. Es de esperar que, a mayor horizonte (90 dias frente a 30 dias), aumente la proporcion de combinaciones que recomiendan 'Cubrirse', porque la perdida potencial segun el VaR crece de forma mas que proporcional con el tiempo (por la regla de la raiz del tiempo), mientras que el costo del forward crece de forma lineal con el plazo. Si se observa el patron contrario (menos cobertura recomendada a mayor plazo), revisar las formulas de los Sub-pasos 1 y 3\.

**7.11.3 Guardar el resultado**

Sub-paso 7: en una celda nueva, guardar la tabla:

tabla\_margenes.to\_excel('/content/drive/MyDrive/MIC-CC/outputs/tables/tabla\_10\_cobertura\_costo\_beneficio.xlsx', index=False)

print('Archivo guardado correctamente')

Sub-paso 8: ejecutar y verificar en Drive.

## **7.12 Etapa 12: Ajuste por Drawback / IVA (Dia 19\)**

**7.12.1 Que calcula esta etapa, y por que es la ultima del modelo**

Para los productos donde la Tarea 3 del Bloque A confirmo que aplica el regimen de Plan Vallejo / Drawback de IVA, esta etapa calcula el beneficio de recuperacion de IVA sobre la porcion de costos correspondiente a insumos importados, y lo suma al margen neto ajustado calculado en la Etapa 8\. El resultado de esta etapa, margen\_final\_pct, es el numero mas completo y realista que produce todo el modelo, y es el que se usa como referencia principal en el Working Paper y en la ultima figura del proyecto.

**7.12.2 Sub-pasos de carga y calculo**

Sub-paso 1: cargar el archivo de la Tarea 3:

ruta\_drawback \= '/content/drive/MyDrive/MIC-CC/data/raw/tabla\_B3\_drawback\_iva.xlsx'

drawback \= pd.read\_excel(ruta\_drawback)

drawback\[\['producto','aplica Plan Vallejo / Drawback de IVA'\]\]

Sub-paso 2: ejecutar y verificar las columnas (renombrar la columna de aplicacion a drawback\_aplica si es necesario, para simplificar el codigo siguiente):

drawback \= drawback.rename(columns={'aplica Plan Vallejo / Drawback de IVA': 'drawback\_aplica'})

Sub-paso 3: en una celda nueva, combinar esta tabla con la tabla de margenes:

tabla\_margenes \= tabla\_margenes.merge(drawback\[\['producto','drawback\_aplica'\]\], on='producto')

Sub-paso 4: en una celda nueva, calcular el beneficio de Drawback (19% del costo importado en ese escenario) solo para los productos donde drawback\_aplica es 'si', y cero para el resto:

tabla\_margenes\['beneficio\_drawback\_cop'\] \= np.where(

    tabla\_margenes\['drawback\_aplica'\].str.lower() \== 'si',

    tabla\_margenes\['costo\_importado\_esc'\] \* 0.19, 0\)

Sub-paso 5: ejecutar y verificar, con una celda de revision, que las filas correspondientes a productos con drawback\_aplica distinto de 'si' tienen beneficio\_drawback\_cop igual a cero:

tabla\_margenes\[tabla\_margenes\['drawback\_aplica'\].str.lower() \!= 'si'\]\['beneficio\_drawback\_cop'\].unique()

Sub-paso 6: ejecutar la celda. El resultado debe mostrar unicamente el valor 0 (un arreglo con solo ese numero), confirmando que el beneficio solo se aplica donde corresponde.

Sub-paso 7: en una celda nueva, calcular el margen final, sumando el beneficio de Drawback al margen ya ajustado por cobertura natural (de la Etapa 8):

tabla\_margenes\['margen\_final\_cop'\] \= tabla\_margenes\['margen\_cop\_ajustado'\] \+ tabla\_margenes\['beneficio\_drawback\_cop'\]

tabla\_margenes\['margen\_final\_pct'\] \= tabla\_margenes\['margen\_final\_cop'\] / tabla\_margenes\['ingreso\_cop'\] \* 100

**7.12.3 Verificar el efecto del Drawback**

Sub-paso 8: en una celda nueva, comparar margen\_pct\_ajustado contra margen\_final\_pct para los productos donde drawback\_aplica es 'si', en el escenario pesimista:

efecto\_drawback \= tabla\_margenes\[(tabla\_margenes\['escenario'\]=='Pesimista') & (tabla\_margenes\['drawback\_aplica'\].str.lower()=='si')\]

efecto\_drawback\[\['producto','margen\_pct\_ajustado','margen\_final\_pct'\]\].drop\_duplicates('producto')

Sub-paso 9: ejecutar y verificar que, para estos productos, margen\_final\_pct es mayor que margen\_pct\_ajustado, confirmando que el beneficio de Drawback efectivamente mejora el margen donde aplica.

**7.12.4 Guardar el resultado final del modelo completo**

Sub-paso 10: en una celda nueva, guardar la tabla completa con todas las columnas acumuladas a lo largo de las 12 etapas, que constituye el resultado principal de todo el Bloque B:

tabla\_margenes.to\_excel('/content/drive/MyDrive/MIC-CC/outputs/tables/tabla\_11\_margen\_final\_ajustado.xlsx', index=False)

print('Modelo financiero completo. Archivo final guardado correctamente.')

Sub-paso 11: ejecutar la celda. Este es el cierre formal del Bloque B.

Sub-paso 12: ir a Drive y verificar que las quince tablas completas (tabla\_04 a tabla\_11, ocho tablas del Bloque B, mas las siete tablas del Bloque A que no se regeneran en Python: tabla\_B3, tabla\_B4, tabla\_B5, tabla\_B6, tabla\_B7, tabla\_B8, tabla\_B9) estan presentes en sus carpetas correspondientes antes de pasar al Bloque C.

# **8\. Bloque C: figuras del proyecto, sub-paso por sub-paso (Dias 20-21)**

Esta seccion construye las cinco figuras finales del modelo, cada una en una celda separada del mismo notebook 04\_financial\_model.ipynb, despues de la ultima celda de la Etapa 12\. Todas se guardan en formato PNG con resolucion 150 dpi (puntos por pulgada, una resolucion adecuada para verse nitidas tanto en pantalla como impresas).

## **8.1 Figura 4: Serie COP/CAD y volatilidad rodante**

**8.1.1 Que muestra esta figura**

Dos paneles apilados verticalmente. El panel superior muestra la evolucion completa del tipo de cambio COP/CAD entre 2020 y 2024\. El panel inferior muestra como cambio la volatilidad a lo largo del mismo periodo, usando una ventana movil de 90 dias, lo cual permite visualizar en que momentos especificos el mercado estuvo mas turbulento.

**8.1.2 Sub-pasos de construccion**

Sub-paso 1: en una celda nueva, calcular la serie de volatilidad rodante que se va a graficar en el panel inferior (si no se calculo ya en la Etapa 4):

vol\_rodante \= fx\_retornos\['retorno'\].rolling(90).std() \* np.sqrt(252) \* 100

Sub-paso 2: en una celda nueva, escribir el codigo completo de la figura:

fig, (ax1, ax2) \= plt.subplots(2, 1, figsize=(13, 8), sharex=True)

ax1.plot(fx\['fecha'\], fx\['COPCAD'\], color='\#2E75B6', linewidth=1.2, label='COP/CAD')

ax1.fill\_between(fx\['fecha'\], fx\['COPCAD'\], fx\['COPCAD'\].min(), alpha=0.15, color='\#2E75B6')

ax1.set\_title('Tipo de cambio COP/CAD, 2020-2024', fontweight='bold')

ax1.set\_ylabel('COP por CAD')

ax1.legend()

ax2.plot(fx\_retornos\['fecha'\], vol\_rodante, color='\#C55A11', label='Volatilidad rodante 90d (%)')

ax2.axhline(y=vol\_anual\*100, color='red', linestyle='--', label=f'Promedio: {vol\_anual\*100:.1f}%')

ax2.set\_ylabel('Volatilidad anualizada (%)')

ax2.set\_xlabel('Fecha')

ax2.legend()

plt.tight\_layout()

plt.savefig('/content/drive/MyDrive/MIC-CC/outputs/figures/figura\_04\_copcad\_volatilidad.png', dpi=150, bbox\_inches='tight')

plt.show()

Sub-paso 3: ejecutar la celda. Debe aparecer la figura completa dentro del notebook, debajo de la celda, mostrando los dos paneles.

Sub-paso 4: revisar visualmente: en el panel superior, la linea azul debe mostrar la tendencia general del COP/CAD durante el periodo, con sus subidas y bajadas. En el panel inferior, la linea naranja de volatilidad rodante debe mostrar picos visibles, idealmente coincidiendo con los periodos de mayor turbulencia historica identificados en la Tarea 6 (por ejemplo, deberia notarse un pico hacia comienzos de 2020).

Sub-paso 5: ir a Drive y confirmar que el archivo figura\_04\_copcad\_volatilidad.png aparece en MIC-CC/outputs/figures/, y que al abrirlo se ve correctamente.

## **8.2 Figura 5: Margenes por escenario y ruta**

**8.2.1 Que muestra esta figura**

Dos paneles uno al lado del otro, uno para cada ruta logistica (Montreal y Vancouver). Cada panel muestra, para los 10 productos, tres barras agrupadas (optimista, base, pesimista), permitiendo comparar visualmente que tan sensible es el margen de cada producto al tipo de cambio, y como cambia esa sensibilidad segun la ruta.

**8.2.2 Sub-pasos de construccion**

Sub-paso 1: en una celda nueva, escribir el codigo:

COLORES \= {'Optimista': '\#375623', 'Base': '\#2E75B6', 'Pesimista': '\#C00000'}

fig, ejes \= plt.subplots(1, 2, figsize=(16, 7))

for ax, ruta in zip(ejes, \['CTG-Montreal', 'CTG-Vancouver'\]):

    datos\_ruta \= tabla\_margenes\[tabla\_margenes\['ruta'\] \== ruta\]

    pivote \= datos\_ruta.pivot\_table(index='producto', columns='escenario', values='margen\_pct')

    pivote\[\['Optimista','Base','Pesimista'\]\].plot(

        kind='bar', ax=ax, color=\[COLORES\[c\] for c in \['Optimista','Base','Pesimista'\]\])

    ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

    ax.set\_title(ruta)

    ax.set\_ylabel('Margen (%)')

    ax.tick\_params(axis='x', rotation=75)

plt.tight\_layout()

plt.savefig('/content/drive/MyDrive/MIC-CC/outputs/figures/figura\_05\_margenes\_escenarios.png', dpi=150, bbox\_inches='tight')

plt.show()

Sub-paso 2: ejecutar y revisar que ambos paneles muestran las barras de los 10 productos con sus tres colores, y que la linea horizontal negra en cero ayuda a identificar de un vistazo que productos caen en margen negativo en cada escenario.

Sub-paso 3: verificar el archivo en Drive.

## **8.3 Figura 6: Mapa de riesgo por tipo de cambio de equilibrio**

**8.3.1 Que muestra esta figura**

Un grafico de barras horizontales, una por producto, mostrando el COP/CAD de equilibrio de cada uno (para la ruta Montreal, como referencia), coloreado segun la clasificacion de riesgo Verde, Amarillo o Rojo calculada en la Etapa 7\. Tres lineas verticales marcan el COP/CAD base, el pesimista, y el correspondiente al peor escenario del VaR a 90 dias, dando contexto visual inmediato de donde esta cada producto respecto a esos tres niveles de referencia.

**8.3.2 Sub-pasos de construccion**

Sub-paso 1: en una celda nueva, escribir el codigo:

colores\_riesgo \= {'Verde': '\#375623', 'Amarillo': '\#BF8F00', 'Rojo': '\#C00000'}

fig, ax \= plt.subplots(figsize=(11, 7))

breakevens \= productos\[\['producto','breakeven\_mtl','riesgo\_mtl'\]\].sort\_values('breakeven\_mtl')

ax.barh(breakevens\['producto'\], breakevens\['breakeven\_mtl'\],

        color=\[colores\_riesgo\[r\] for r in breakevens\['riesgo\_mtl'\]\])

ax.axvline(x=copcad\_base, color='blue', linestyle='--', label='COP/CAD base')

ax.axvline(x=copcad\_pesimista, color='orange', linestyle='--', label='COP/CAD pesimista')

ax.axvline(x=copcad\_var90, color='red', linestyle='--', label='COP/CAD en VaR 90d')

ax.set\_xlabel('Tipo de cambio COP/CAD de equilibrio')

ax.set\_title('Mapa de riesgo cambiario por producto (ruta Montreal)')

ax.legend()

plt.tight\_layout()

plt.savefig('/content/drive/MyDrive/MIC-CC/outputs/figures/figura\_06\_mapa\_riesgo\_breakeven.png', dpi=150, bbox\_inches='tight')

plt.show()

Sub-paso 2: ejecutar y revisar que las barras estan coloreadas de forma diferenciada (verde, amarillo, rojo) segun corresponda, y que las tres lineas verticales son claramente visibles cruzando las barras.

Sub-paso 3: verificar el archivo en Drive.

## **8.4 Figura 7: Margenes bajo episodios historicos de estres**

**8.4.1 Que muestra esta figura**

Barras agrupadas con los 10 productos en el eje horizontal, y una barra por cada episodio historico documentado en la Tarea 6, mostrando el margen porcentual promedio (entre las dos rutas) bajo ese episodio especifico.

**8.4.2 Sub-pasos de construccion**

Sub-paso 1: en una celda nueva, escribir el codigo:

fig, ax \= plt.subplots(figsize=(14, 7))

pivote\_stress \= tabla\_stress.pivot\_table(index='producto', columns='episodio', values='margen\_pct', aggfunc='mean')

pivote\_stress.plot(kind='bar', ax=ax)

ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

ax.set\_ylabel('Margen (%)')

ax.set\_title('Margenes bajo episodios historicos de estres cambiario')

ax.tick\_params(axis='x', rotation=75)

ax.legend(title='Episodio', bbox\_to\_anchor=(1.02, 1), loc='upper left')

plt.tight\_layout()

plt.savefig('/content/drive/MyDrive/MIC-CC/outputs/figures/figura\_07\_stress\_testing.png', dpi=150, bbox\_inches='tight')

plt.show()

Sub-paso 2: ejecutar y revisar que cada producto tiene una barra por cada episodio, con colores distintos por episodio, y que la leyenda a la derecha del grafico identifica claramente cada episodio por su nombre.

Sub-paso 3: verificar el archivo en Drive.

## **8.5 Figura 8: Margen bruto vs margen ajustado por cobertura natural y Drawback**

**8.5.1 Que muestra esta figura**

Para cada producto, en el escenario pesimista, tres barras agrupadas que muestran la evolucion del margen a traves de los ajustes sucesivos del modelo: el margen original sin ajustar (de la Etapa 6), el margen ajustado por cobertura natural (de la Etapa 8), y el margen final ajustado tambien por el beneficio de Drawback (de la Etapa 12). Esta figura es la sintesis visual de todo el valor agregado que aportan los modulos avanzados del modelo respecto a un calculo simplificado.

**8.5.2 Sub-pasos de construccion**

Sub-paso 1: en una celda nueva, escribir el codigo:

fig, ax \= plt.subplots(figsize=(13, 7))

datos\_pes \= tabla\_margenes\[tabla\_margenes\['escenario'\] \== 'Pesimista'\].groupby('producto')\[\[

    'margen\_pct', 'margen\_pct\_ajustado', 'margen\_final\_pct'\]\].mean()

datos\_pes.plot(kind='bar', ax=ax, color=\['\#C00000', '\#BF8F00', '\#375623'\])

ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

ax.set\_ylabel('Margen (%)')

ax.set\_title('Margen pesimista: bruto vs ajustado por cobertura natural y Drawback')

ax.tick\_params(axis='x', rotation=75)

ax.legend(\['Margen bruto (sin ajustar)', 'Margen ajustado (cobertura natural)', 'Margen final (con Drawback)'\])

plt.tight\_layout()

plt.savefig('/content/drive/MyDrive/MIC-CC/outputs/figures/figura\_08\_margen\_bruto\_vs\_ajustado.png', dpi=150, bbox\_inches='tight')

plt.show()

Sub-paso 2: ejecutar y revisar que, para la mayoria de los productos, las barras muestran una progresion logica: el margen ajustado (segunda barra) deberia ser igual o mejor que el bruto (primera barra) para productos con insumos importados, y el margen final (tercera barra) deberia ser igual o mejor que el ajustado para los productos donde aplica el Drawback.

Sub-paso 3: verificar el archivo en Drive, y confirmar que las cinco figuras (04 a 08\) estan completas en MIC-CC/outputs/figures/ antes de continuar al siguiente bloque.

# **9\. Bloque C: repositorio en GitHub, sub-paso por sub-paso (Dia 22\)**

## **9.1 Por que se usa GitHub y no solo Google Drive**

Google Drive es donde se trabaja durante todo el desarrollo del proyecto, pero no es la plataforma adecuada para publicar el resultado final de forma profesional y citable. GitHub es la plataforma estandar en el mundo de la ciencia de datos, la programacion y la investigacion reproducible para publicar codigo de forma publica, versionada (lo que significa que se guarda un historial de cada cambio realizado) y accesible para cualquier persona, sin necesidad de tener una cuenta de Google ni permisos especiales.

## **9.2 Crear la cuenta de GitHub, si no se tiene**

Sub-paso 1: abrir el navegador y escribir github.com en la barra de direcciones.

Sub-paso 2: hacer clic en el boton 'Sign up' (Registrarse), normalmente en la esquina superior derecha.

Sub-paso 3: ingresar un correo electronico valido (puede ser el mismo correo de Google usado para el proyecto, o uno distinto).

Sub-paso 4: crear una contrasena siguiendo los requisitos de seguridad que pida la pagina (normalmente una combinacion de mayusculas, minusculas, numeros y un minimo de caracteres).

Sub-paso 5: elegir un nombre de usuario. Este nombre va a aparecer en la direccion web (URL) del perfil y de los repositorios, asi que conviene elegir algo profesional y facil de recordar, relacionado con el nombre propio o con el proyecto, evitando apodos informales.

Sub-paso 6: completar cualquier verificacion adicional que la pagina solicite (por ejemplo, un captcha o una verificacion de que no se es un robot).

Sub-paso 7: revisar la bandeja de entrada del correo electronico usado en el registro, y hacer clic en el enlace de verificacion que GitHub envia automaticamente.

## **9.3 Crear el repositorio del proyecto**

Sub-paso 1: una vez iniciada la sesion en GitHub, buscar el boton verde 'New' (Nuevo), normalmente visible en la pagina principal del perfil o en la esquina superior izquierda con un signo mas.

Sub-paso 2: en el campo 'Repository name' (Nombre del repositorio), escribir exactamente: MIC-CC-ODEM-EAN

Sub-paso 3: en el campo de descripcion (Description), escribir exactamente: Commercial Intelligence Monitor Colombia-Canada | Financial Risk Analysis | ODEM-Universidad EAN 2026

Sub-paso 4: en las opciones de visibilidad, seleccionar 'Public' (Publico), no 'Private', porque el proyecto debe ser accesible para cualquier persona sin necesidad de invitacion.

Sub-paso 5: marcar la casilla 'Add a README file' (Agregar un archivo README), que crea automaticamente un archivo basico de documentacion.

Sub-paso 6: dejar las demas opciones (licencia, .gitignore) en su valor por defecto, a menos que se tenga una preferencia especifica sobre el tipo de licencia de uso del codigo.

Sub-paso 7: hacer clic en el boton verde 'Create repository' (Crear repositorio).

Sub-paso 8: confirmar que la pagina redirige a la vista principal del nuevo repositorio, mostrando su nombre y el archivo README.md vacio o con texto basico.

## **9.4 Subir los archivos del proyecto al repositorio**

Sub-paso 1: dentro de la vista del repositorio en GitHub, buscar el boton 'Add file' (Agregar archivo) y seleccionar 'Upload files' (Subir archivos).

Sub-paso 2: en el computador, descargar primero (si aun no se ha hecho) todos los archivos finales desde Google Drive: el notebook 04\_financial\_model.ipynb (desde MIC-CC/notebooks/), las cinco figuras PNG (desde MIC-CC/outputs/figures/), y las tablas de resultados relevantes (desde MIC-CC/outputs/tables/ y MIC-CC/data/raw/, segun se considere pertinente).

Sub-paso 3: para descargar un archivo individual desde Drive, hacer clic derecho sobre el y seleccionar 'Descargar'.

Sub-paso 4: una vez que todos los archivos relevantes estan descargados en el computador (idealmente organizados en una carpeta temporal), volver a la pagina de GitHub donde se abrio 'Upload files'.

Sub-paso 5: arrastrar todos los archivos descargados directamente sobre el area indicada en la pagina de GitHub ('Drag files here to add them to your repository'), o hacer clic en 'choose your files' para seleccionarlos manualmente desde el explorador de archivos del computador.

Sub-paso 6: esperar a que la barra de progreso de cada archivo llegue al 100%.

Sub-paso 7: en la parte inferior de la pagina, escribir un mensaje breve describiendo la subida, por ejemplo: 'Carga inicial del modelo financiero, tablas y figuras'.

Sub-paso 8: hacer clic en 'Commit changes' (Confirmar cambios).

Sub-paso 9: confirmar visualmente que todos los archivos aparecen ahora en la vista principal del repositorio.

## **9.5 Escribir el archivo README.md**

**9.5.1 Por que el README es tan importante**

El README.md es el primer archivo que ve cualquier persona que entra al repositorio, porque GitHub lo muestra automaticamente debajo de la lista de archivos. Es, en la practica, la carta de presentacion del proyecto. Debe estar escrito en ingles, porque es el idioma estandar de la comunidad tecnica internacional y de la mayoria de los repositorios publicos de codigo, y porque facilita que el proyecto sea entendible para evaluadores o colaboradores internacionales.

**9.5.2 Sub-pasos para editar el README**

Sub-paso 1: en la vista principal del repositorio, hacer clic sobre el archivo README.md.

Sub-paso 2: hacer clic en el icono de lapiz (editar) que aparece en la esquina superior derecha de la vista del archivo.

Sub-paso 3: borrar el contenido generico que GitHub haya generado automaticamente.

Sub-paso 4: escribir el contenido del README siguiendo esta estructura minima: un titulo (el nombre del proyecto), un parrafo de descripcion de 2 a 3 oraciones explicando el proposito del MIC-CC y de la dimension financiera, una seccion que liste los modulos del modelo financiero (VaR, escenarios, breakeven, stress testing historico, cobertura natural, costo de capital, costo-beneficio de cobertura, ajuste por Drawback), una seccion de instrucciones para reproducir el analisis (que librerias de Python instalar, que datos descargar y de donde, como ejecutar el notebook), una seccion de resultados principales (un resumen de 3 a 5 oraciones de los hallazgos mas relevantes del modelo), y una seccion final con la cita sugerida del proyecto (nombre del autor, institucion, ano).

Sub-paso 5: usar formato Markdown para dar estructura al texto: los simbolos \# al inicio de una linea crean titulos (un solo \# para titulo principal, \#\# para subtitulos), y el simbolo \- al inicio de una linea crea una lista con vinetas.

Sub-paso 6: una vez escrito el contenido completo, hacer clic en el boton 'Preview' (Vista previa) para revisar como se va a ver el README una vez publicado, con el formato ya aplicado.

Sub-paso 7: si el formato se ve correcto, desplazarse hasta la parte inferior de la pagina, escribir un mensaje breve como 'Documentacion completa del README', y hacer clic en 'Commit changes'.

## **9.6 Verificacion final del repositorio**

Verificacion 1: el repositorio es accesible desde un navegador en modo incognito o sin sesion iniciada (para confirmar que efectivamente es publico).

Verificacion 2: el README se muestra correctamente formateado, sin simbolos de Markdown sin procesar visibles como texto (por ejemplo, si aparecen simbolos \# sueltos en el texto en lugar de titulos formateados, revisar la sintaxis usada).

Verificacion 3: el notebook 04\_financial\_model.ipynb, las cinco figuras, y las tablas de resultados estan todas presentes en la lista de archivos del repositorio.

# **10\. Bloque C: seccion del Working Paper, sub-paso por sub-paso (Dias 23-24)**

## **10.1 Preparacion antes de escribir**

Sub-paso 1: crear un documento nuevo en Google Docs, dentro de la carpeta MIC-CC/docs/ de Drive (se puede crear directamente desde Drive con el boton 'Nuevo' \> 'Google Docs').

Sub-paso 2: nombrar el documento de forma clara, por ejemplo: 'MIC-CC Working Paper \- Seccion 5 Analisis Financiero'.

Sub-paso 3: tener a mano, en pestanas separadas del navegador o impresas, las quince tablas de resultados y las cinco figuras generadas en los Bloques A, B y C, porque la redaccion de cada subseccion requiere consultar resultados numericos especificos.

## **10.2 Redactar cada una de las ocho subsecciones**

Cada subseccion sigue una logica similar: presentar el resultado numerico relevante, interpretarlo en lenguaje claro, y conectar con la figura o tabla correspondiente. A continuacion se desglosa el contenido esperado de cada una.

**10.2.1 Subseccion 5.1, Marco conceptual (aproximadamente 150 palabras)**

Sub-paso 1: explicar que es el COP/CAD y por que no se cotiza de forma directa.

Sub-paso 2: explicar la formula de tasa cruzada usada para construirlo.

Sub-paso 3: explicar, en una o dos oraciones, por que este tipo de cambio es relevante especificamente para los exportadores colombianos que venden a Canada.

**10.2.2 Subseccion 5.2, Serie COP/CAD 2020-2024**

Sub-paso 1: describir la tendencia general observada en la Figura 4 (subidas, bajadas, periodos de mayor estabilidad).

Sub-paso 2: mencionar los eventos que coinciden con los picos de volatilidad visibles en el panel inferior de la Figura 4, conectandolos si es posible con los episodios documentados en la tabla\_B6.

Sub-paso 3: insertar la Figura 4 en el documento de Google Docs (Insertar \> Imagen \> Subir desde computador, usando el archivo PNG descargado de Drive).

**10.2.3 Subseccion 5.3, VaR y volatilidad**

Sub-paso 1: presentar los cinco valores de la tabla\_04\_indicadores\_riesgo.xlsx (volatilidad anual y los cuatro VaR).

Sub-paso 2: interpretar el VaR a 30, 60 y 90 dias en terminos practicos para un exportador, similar al ejemplo numerico de la Seccion 3.4 de esta guia.

**10.2.4 Subseccion 5.4, Escenarios y margenes**

Sub-paso 1: resumir los resultados principales de la tabla\_05\_margenes\_escenarios.xlsx: cuales productos mantienen margen positivo en los tres escenarios, y cuales caen en margen negativo en el escenario pesimista.

Sub-paso 2: senalar si hay diferencias relevantes entre las dos rutas (Montreal vs Vancouver).

Sub-paso 3: insertar la Figura 5\.

**10.2.5 Subseccion 5.5, Tipo de cambio de equilibrio y mapa de riesgo**

Sub-paso 1: explicar el concepto de breakeven en una oracion, similar a la Seccion 3.6 de esta guia.

Sub-paso 2: presentar cuales productos quedaron clasificados en Rojo, Amarillo y Verde segun la tabla\_06\_breakeven.xlsx, y explicar brevemente por que.

Sub-paso 3: aclarar explicitamente, en el texto de esta subseccion (no solo como nota al pie), dos limitaciones del semaforo antes de que el lector saque conclusiones de el: (a) esta clasificacion se calcula ANTES de aplicar la cobertura natural (Etapa 8) y el beneficio de Drawback (Etapa 12), que solo mejoran el margen — el numero mas completo del modelo es margen\_final\_pct de la tabla\_11, no el breakeven crudo de esta subseccion; y (b) si el Carbon bituminoso aparece en Rojo, aclarar que su breakeven esta inflado por una limitacion metodologica conocida (tarifa de flete de contenedor aplicada a un commodity que se transporta a granel — ver Seccion 7.6.2 de esta guia), y que ese resultado no debe presentarse como una conclusion de negocio sobre la viabilidad real de exportar carbon sin esa advertencia.

Sub-paso 4: insertar la Figura 6\.

**10.2.6 Subseccion 5.6, Stress testing historico**

Sub-paso 1: listar brevemente los episodios historicos documentados (de la tabla\_B6), con sus porcentajes de cambio.

Sub-paso 2: presentar los resultados mas relevantes de la tabla\_08\_stress\_testing.xlsx, destacando que productos resultan mas afectados bajo el episodio mas severo.

Sub-paso 3: insertar la Figura 7\.

Sub-paso 4: agregar una o dos oraciones de implicacion de politica: por ejemplo, si varios productos quedarian con margen muy negativo bajo un episodio del tamano de 2014-2016, esto sugiere la importancia de contar con mecanismos de cobertura cambiaria disponibles para esos sectores.

**10.2.7 Subseccion 5.7, Cobertura natural y costo de capital de trabajo**

Sub-paso 1: explicar como la estructura de costos de cada producto (insumos importados vs nacionales, de la tabla\_B9) modera su exposicion al riesgo cambiario, citando el resultado de la comparacion hecha en la Etapa 8 del Bloque B.

Sub-paso 2: presentar el efecto del costo de financiamiento sobre el margen neto a 30, 60 y 90 dias, usando los resultados de la tabla\_09\_costo\_capital.xlsx.

**10.2.8 Subseccion 5.8, Recomendaciones de cobertura cambiaria y Drawback**

Sub-paso 1: resumir los resultados del modulo de costo-beneficio de cobertura (tabla\_10), indicando para que productos y horizontes se recomienda cubrirse.

Sub-paso 2: presentar el efecto del beneficio de Drawback sobre el margen final (tabla\_11), para los productos donde aplica.

Sub-paso 3: insertar la Figura 8\.

Sub-paso 4: cerrar con dos o tres oraciones de recomendaciones de politica para PYMEs exportadoras, basadas en el conjunto completo de hallazgos del modelo.

## **10.3 Referencias en formato APA 7**

Sub-paso 1: al final del documento, crear una seccion titulada 'Referencias'.

Sub-paso 2: para cada fuente documentada a lo largo del Bloque A (las URLs anotadas en cada una de las nueve tablas), construir una referencia en formato APA 7, que generalmente sigue la estructura: Autor o institucion. (Ano). Titulo de la pagina o documento. Nombre del sitio. URL.

Sub-paso 3: ordenar las referencias alfabeticamente por el nombre de la institucion o autor.

Sub-paso 4: revisar que cada fuente citada en el cuerpo del texto (por ejemplo, al mencionar un dato del Banco de la Republica o del Bank of Canada) tiene su referencia correspondiente en esta lista final.

## **10.4 Revision final del documento**

Verificacion 1: las ocho subsecciones estan completas, en el orden 5.1 a 5.8.

Verificacion 2: las cinco figuras estan insertadas en las subsecciones correspondientes, con buena resolucion (no pixeladas).

Verificacion 3: todos los numeros citados en el texto (volatilidad, VaR, margenes, etc.) coinciden exactamente con los valores de las tablas de resultados; no se citan numeros de memoria ni aproximados.

Verificacion 4: la lista de referencias esta completa y en formato APA 7 consistente.

# **11\. Como organizar el trabajo individual de 24 dias**

Trabajar sola durante 24 dias en una fase con este nivel de detalle requiere una disciplina especifica. Esta seccion describe practicas concretas, no generalidades, para sostener la calidad del trabajo de principio a fin.

## **11.1 Documentar fuentes en el momento exacto en que se encuentran**

Cuando se trabaja en equipo, otra persona revisa el trabajo de quien investigo una fuente. Trabajando sola, ese control cruzado no existe. La practica concreta es: cada vez que se encuentra un dato relevante durante cualquiera de las nueve tareas del Bloque A, anotar de inmediato, en la misma celda de Excel donde va el dato, tres cosas: el valor encontrado, la URL exacta (copiada directamente de la barra de direcciones del navegador, no escrita de memoria), y la fecha del dia en curso. Hacerlo de inmediato, no al final de la sesion de trabajo, porque la experiencia muestra que despues de visitar varias paginas en una busqueda, es facil confundir de cual pagina especifica salio cada dato.

## **11.2 Separar la construccion de una tabla de su revision**

Una tabla recien terminada es dificil de revisar con ojo critico, porque la mente tiende a confirmar lo que se acaba de escribir en lugar de cuestionarlo. La practica recomendada es: terminar de construir una tabla, cerrar el archivo, y dejar pasar al menos un par de horas, o idealmente hasta el dia siguiente, antes de volver a abrirla exclusivamente para revisarla con la lista de verificacion de calidad de esa tarea especifica. Esta pausa entre construccion y revision es la que en la version de equipo cumplia Manuela al revisar el trabajo de Karen y David; trabajando sola, hay que generar esa misma distancia con el tiempo en lugar de con otra persona.

## **11.3 Verificar cada celda de codigo antes de escribir la siguiente**

Dentro del Bloque B, la tentacion es escribir varias celdas de codigo seguidas y ejecutarlas todas juntas al final. Esto es un error practico: si hay un fallo en una celda intermedia, se vuelve mas dificil identificar en cual celda especifica ocurrio el problema, porque el error se mezcla con el resultado de las celdas siguientes. La practica recomendada, que esta guia sigue de forma consistente en toda la Seccion 7, es: escribir una celda, ejecutarla con Shift \+ Enter, leer el resultado o el error que aparece, y solo entonces escribir la siguiente celda.

## **11.4 No saltarse el orden de los tres bloques**

Es tentador empezar a escribir codigo de Python (Bloque B) antes de tener completas las nueve tareas del Bloque A, especialmente si alguna tarea de investigacion se complica y se quiere avanzar en otra cosa mientras tanto. Resistir esa tentacion: el codigo del Bloque B carga, en distintas etapas, los nueve archivos del Bloque A. Empezar a programar con datos incompletos genera retrabajo, porque hay que volver a ejecutar celdas ya escritas cuando llega el dato que faltaba, y aumenta el riesgo de terminar usando, sin darse cuenta, una version vieja de algun archivo.

## **11.5 Llevar un registro de avance dia por dia**

Crear, desde el primer dia, un archivo simple de texto (puede ser un documento de Google Docs en la carpeta MIC-CC/docs/, o incluso una nota en cualquier aplicacion sencilla) con una lista de las 24 dias del cronograma de la Seccion 5, y marcar al final de cada jornada de trabajo si la tarea de ese dia quedo completa, parcial, o pendiente. Esto cumple la misma funcion que las reuniones semanales de seguimiento en un equipo: una pausa regular y honesta para verificar que el avance real coincide con el plan, y para detectar a tiempo si algun bloque esta tomando mas tiempo del previsto.

## **11.6 Que hacer cuando una fuente no aparece despues de buscar**

Establecer un limite de tiempo razonable, de 30 a 40 minutos, para cada intento de busqueda de una fuente especifica dentro del Bloque A. Si pasado ese tiempo no se encuentra la informacion, no seguir insistiendo de forma continua: documentar exactamente que se busco (los terminos exactos usados en Google, las paginas visitadas), marcar el dato como pendiente en la tabla correspondiente, y continuar con la siguiente tarea del cronograma. Volver a intentar esa busqueda especifica en otro momento del dia, o al dia siguiente, casi siempre da mejores resultados que insistir de forma ininterrumpida, porque permite pensar en terminos de busqueda alternativos con la mente mas despejada.

## **11.7 Que hacer cuando una celda de Python da un error que no se entiende**

Esta guia incluye, para cada etapa del Bloque B, una sub-seccion especifica de 'que hacer si algo no funciona', con los errores mas probables anticipados. El primer paso ante cualquier error es leer el mensaje de error completo (no solo la primera linea), porque Python casi siempre indica en que linea exacta de codigo ocurrio el problema. El segundo paso es revisar la sub-seccion de errores de esa etapa especifica en esta guia. El tercer paso, si el error no esta cubierto en la guia, es copiar el texto exacto del mensaje de error (sin parafrasear) y buscarlo en Google junto con la palabra 'pandas' o 'python', porque la gran mayoria de los errores de este tipo ya fueron resueltos por otras personas en foros publicos.

# **12\. Checklist final completo de los 24 dias**

Revisar cada uno de estos puntos antes de considerar cerrada la Fase 4\.

## **12.1 Archivos de datos de entrada (Bloque A, dias 1-10)**

| Tarea | Archivo | Carpeta |
| ----- | ----- | ----- |
| 1 | TRM\_COP\_USD\_2020\_2024.xlsx | data/raw/ |
| 2 | USDCAD\_2020\_2024.xlsx | data/raw/ |
| 3 | tabla\_B3\_drawback\_iva.xlsx | data/raw/ |
| 4 | tabla\_B4\_precios\_referencia.xlsx | data/raw/ |
| 5 | tabla\_B5\_sensibilidad\_margenes.xlsx (30 filas) | outputs/tables/ |
| 6 | tabla\_B6\_episodios\_historicos.xlsx (4-6 filas) | data/raw/ |
| 7 | tabla\_B7\_instrumentos\_cobertura.xlsx | data/raw/ |
| 8 | tabla\_B8\_tasas\_interes.xlsx | data/raw/ |
| 9 | tabla\_B9\_estructura\_costos.xlsx (10 filas) | data/raw/ |

## **12.2 Archivos generados por el modelo (Bloque B, dias 11-19)**

| Etapa | Archivo | Carpeta |
| ----- | ----- | ----- |
| 3 | fx\_COPCAD\_2020\_2024.xlsx (\~1.240 filas) | data/processed/ |
| 5 | tabla\_04\_indicadores\_riesgo.xlsx | outputs/tables/ |
| 6 | tabla\_05\_margenes\_escenarios.xlsx (60 filas) | outputs/tables/ |
| 7 | tabla\_06\_breakeven.xlsx | outputs/tables/ |
| 8 | tabla\_07\_cobertura\_natural.xlsx | outputs/tables/ |
| 9 | tabla\_08\_stress\_testing.xlsx | outputs/tables/ |
| 10 | tabla\_09\_costo\_capital.xlsx | outputs/tables/ |
| 11 | tabla\_10\_cobertura\_costo\_beneficio.xlsx | outputs/tables/ |
| 12 | tabla\_11\_margen\_final\_ajustado.xlsx | outputs/tables/ |
| 1 | 04\_financial\_model.ipynb (corre sin errores de inicio a fin) | notebooks/ |

## **12.3 Figuras (Bloque C, dias 20-21)**

\[ \] figura\_04\_copcad\_volatilidad.png

\[ \] figura\_05\_margenes\_escenarios.png

\[ \] figura\_06\_mapa\_riesgo\_breakeven.png

\[ \] figura\_07\_stress\_testing.png

\[ \] figura\_08\_margen\_bruto\_vs\_ajustado.png

Todas guardadas en MIC-CC/outputs/figures/, en resolucion 150 dpi, abiertas y revisadas visualmente al menos una vez cada una.

## **12.4 GitHub (dia 22\)**

\[ \] Repositorio MIC-CC-ODEM-EAN creado, publico, y verificado en modo incognito.

\[ \] README.md completo en ingles, con las seis secciones descritas en la Seccion 9.5.2 de esta guia.

\[ \] Notebook, las cinco figuras, y las tablas de resultados subidas correctamente.

## **12.5 Working Paper (dias 23-24)**

\[ \] Subseccion 5.1 Marco conceptual.

\[ \] Subseccion 5.2 Serie COP/CAD con Figura 4 insertada.

\[ \] Subseccion 5.3 VaR y volatilidad.

\[ \] Subseccion 5.4 Escenarios y margenes con Figura 5 insertada.

\[ \] Subseccion 5.5 Tipo de cambio de equilibrio con Figura 6 insertada.

\[ \] Subseccion 5.6 Stress testing historico con Figura 7 insertada.

\[ \] Subseccion 5.7 Cobertura natural y costo de capital.

\[ \] Subseccion 5.8 Recomendaciones de cobertura y Drawback con Figura 8 insertada.

\[ \] Referencias completas en formato APA 7\.

## **12.6 Prueba final de calidad**

Pedirle a una persona ajena al proyecto, que no haya participado en ninguna parte de su construccion, que abra el repositorio de GitHub. Sin darle ninguna explicacion previa, esa persona debe poder entender, leyendo unicamente el README y revisando el notebook: que hace el proyecto, como se reproduce el analisis, y cuales son los resultados principales. Si esa persona logra entenderlo sin ayuda adicional, la Fase 4 esta terminada de forma satisfactoria.

# **13\. Glosario completo**

| Termino | Definicion breve |
| ----- | ----- |
| TRM | Tasa Representativa del Mercado. Precio oficial del USD en COP publicado por el Banco de la Republica. |
| COP/CAD | Tipo de cambio entre el peso colombiano y el dolar canadiense, construido como tasa cruzada. |
| USD/CAD | Cuantos dolares americanos vale un dolar canadiense, publicado por el Bank of Canada. |
| Tasa cruzada (cross rate) | Tipo de cambio entre dos monedas que se calcula combinando los tipos de cambio de cada una contra una tercera moneda comun. |
| Volatilidad | Medida estadistica de cuanto fluctua un precio o tipo de cambio. Se expresa como porcentaje anualizado. |
| VaR (Value at Risk) | Perdida maxima esperada con un nivel de confianza dado (95% en este modelo), en un horizonte de tiempo determinado. |
| Percentil | Valor que deja un porcentaje determinado de los datos por debajo de el, una vez ordenados de menor a mayor. |
| Escenario base / optimista / pesimista | Tres niveles del COP/CAD usados para simular margenes de exportacion. |
| Margen bruto / neto | Ganancia del exportador en porcentaje del ingreso, antes (bruto) o despues (neto) de ajustes adicionales como el costo financiero. |
| Tipo de cambio de equilibrio (breakeven) | Valor del COP/CAD en el cual el margen neto de un producto es exactamente cero. |
| Stress testing historico | Aplicar a los margenes los porcentajes de cambio reales de episodios pasados del tipo de cambio. |
| Cobertura natural (natural hedge) | Reduccion del riesgo cambiario cuando parte de los costos de produccion esta en la misma moneda que varia con el tipo de cambio. |
| Costo de capital de trabajo (cost of carry) | Costo financiero de mantener capital de trabajo en pesos mientras se espera el pago de una exportacion. |
| IBR | Indicador Bancario de Referencia, tasa de interes de referencia del mercado interbancario colombiano. |
| Forward | Contrato que fija hoy el tipo de cambio de una operacion futura. |
| NDF (Non-Deliverable Forward) | Variante de forward que se liquida en pesos sin entregar la divisa extranjera; el instrumento mas usado en Colombia. |
| Puntos forward | Diferencial de tasas de interes entre dos paises, usado para estimar el costo de un forward o NDF. |
| Paridad de tasas de interes | Principio financiero que relaciona el diferencial de tasas de interes entre dos paises con el costo de un forward cambiario. |
| Plan Vallejo de importacion | Regimen aduanero colombiano que permite importar insumos con beneficios tributarios, si se usan para producir bienes exportados. |
| Drawback de IVA | Mecanismo que permite recuperar el IVA pagado en insumos importados que se incorporan a un producto exportado. |
| FOB (Free On Board) | Precio del producto puesto en el puerto de origen, sin incluir flete internacional ni seguro de transporte. |
| CIF (Cost, Insurance and Freight) | Precio que incluye el costo del producto, el seguro y el flete hasta el puerto de destino. |
| API | Interfaz de Programacion de Aplicaciones. Forma en que un sitio web entrega datos de manera estructurada y automatica. |
| JSON | Formato de datos estructurado, comun en respuestas de APIs, similar a un diccionario con pares de nombre y valor. |
| Google Colab | Herramienta gratuita de Google para ejecutar codigo Python desde el navegador, sin instalacion local. |
| Notebook | Archivo de codigo organizado en celdas ejecutables, con extension .ipynb. |
| DataFrame | Tabla de datos en Python, creada y manipulada con la libreria pandas. |
| Merge (union de tablas) | Operacion que combina dos tablas de datos usando una columna en comun, como la fecha o el nombre del producto. |
| GitHub | Plataforma de publicacion y control de versiones de codigo, usada para compartir el proyecto de forma publica. |
| README | Archivo de documentacion principal de un repositorio, que explica de que trata el proyecto. |
| HS (Sistema Armonizado) | Codigo numerico internacional que identifica un producto especifico para fines aduaneros. |
| VCR (Ventaja Comparativa Revelada) | Indicador que mide si un pais exporta un producto en mayor proporcion de lo esperado, sugiriendo ventaja competitiva. |
| TLCC | Tratado de Libre Comercio Colombia-Canada, vigente desde agosto de 2011\. |
| NMF (Nacion Mas Favorecida) | Arancel general que un pais aplica a cualquier otro pais sin un tratado comercial especifico vigente. |
| MIC-CC | Monitor de Inteligencia Comercial Colombia-Canada. Nombre del proyecto. |
| ODEM | Observatorio de Economia y Mercados. Unidad de investigacion de la Universidad EAN. |

Fin del documento  |  ODEM \- Universidad EAN  |  Bogota, junio 2026