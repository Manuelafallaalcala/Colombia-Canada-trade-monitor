# Datos pendientes: qué falta, quién lo tiene y qué desbloquea

**MIC-CC · Fase 4 financiera · ODEM — Universidad EAN**

Este documento existe para separar dos cosas que suelen confundirse al cerrar un proyecto: lo que
está **sin terminar** y lo que está **terminado hasta donde los datos disponibles permiten**.

El modelo está terminado. El código corre de principio a fin, las 66 pruebas pasan, las 21 tablas y
las 6 figuras se generan. Lo que sigue abierto no es programación: son **datos que hay que pedirle a
alguien**, y ninguna cantidad de trabajo sobre el código los produce. Intentar taparlos con supuestos
mejor redactados sería empeorar el modelo, no terminarlo.

---

## Por qué esto importa antes de publicar

Catorce de los veinticuatro parámetros inventariados por `config.resumen_evidencia()` son de
**grado C: supuestos de trabajo, no evidencia**. La regla que el proyecto se impuso es explícita:

> Ninguna conclusión que dependa de un parámetro de grado C debe presentarse como hallazgo.

De ahí vienen tres decisiones de presentación que no son cosméticas:

1. Los resultados por producto se reportan como **banda**, no como punto.
2. El semáforo de riesgo es **robusto**: solo asigna Verde si el producto resiste en el extremo
   desfavorable de su propia banda. Exigirlo cambia el color en 6 de 20 combinaciones producto-ruta.
3. **No se publica ningún ranking de rentabilidad entre productos.**

---

## Inventario de vacíos

### 1. Estructuras de costo sectoriales reales — *el vacío que más pesa*

**Estado.** Siete de los diez ratios costo/precio FOB son grado C. Cuatro son grado B, inferidos de
información gremial cualitativa. **Ninguno es grado A bajo el perfil productor**, que es el que el
modelo usa por defecto.

El único ratio de grado A del proyecto es el del café bajo perfil comercializador, y solo porque la
FNC publica un precio interno de compra: 2.210.000 COP por carga de 125 kg de café pergamino seco
(27-jul-2026), que reexpresado a kilogramo de excelso exportable da un ratio de ~0,94–0,98 según la
TRM vigente.

**A quién pedírselo.**

| Producto | Fuente | Qué pedir |
|---|---|---|
| Café (perfil productor) | Federación Nacional de Cafeteros — Gerencia Técnica | Costo de producción por carga en finca, por rango de altura y tamaño de predio |
| Flores y rosas | Asocolflores | Estructura de costos por tallo o por kilo exportado: mano de obra, frío, transporte, empaque |
| Trucha | Fedeacua / acuicola.co | Costo de producción por kilo, con el peso del alimento balanceado desagregado |
| Farmacéutico | ANDI — Cámara Farmacéutica | Estructura de costos de fabricación local para HS 3004 |
| Siderúrgico | ANDI — Cámara Fedemetal | Estructura de costos para accesorios de tubería HS 7307 |
| Carbón | Fenalcarbón / Agencia Nacional de Minería | Cash cost por tonelada FOB puerto |
| Confección | Inexmoda / ACOLTEX | Costo de confección por docena para calcetería HS 6115 |
| Nueces y semillas | Empresa procesadora del sector | Costo de materia prima importada más transformación |

**Qué desbloquea.** Es la condición necesaria para publicar cualquier ranking de rentabilidad por
producto. Mientras no exista, el modelo puede decir *qué tan expuesto* está cada producto al tipo de
cambio —eso sí lo sabe— pero no *cuál es más rentable*.

**Cómo verificar que ya no hace falta.** Cuando `config.COSTOS_SECTOR` tenga la mayoría de sus
ratios en grado A o B con fuente fechada, y `resumen_evidencia()` baje el conteo de grado C.

---

### 2. Cotización real de flete aéreo y de flete a granel

**Estado.** `flete_aereo_usd_kg = 2,80` (rango 2,00–4,00) y `flete_granel_usd_kg` de 0,015–0,022 son
estimaciones de orden de magnitud declaradas grado C. La primera afecta a los dos productos de
flores, que son el 20 % del Top 10 y los dos que quedan más al límite; la segunda afecta al carbón.

**A quién pedírselo.** Un agente de carga con operación Bogotá–Canadá (Avianca Cargo, Kuehne+Nagel,
DHL Global Forwarding) para el aéreo; un bróker de granel sólido para el carbón, o la tarifa Panamax
publicada por Baltic Exchange como referencia secundaria.

**Qué pedir.** Cotización en firme para un embarque de tamaño típico de PYME, con fecha, recargos
desagregados (combustible, seguridad, manejo) y validez.

**Qué desbloquea.** El semáforo de rosas y pompones. Ambos tienen hoy un colchón de 1,5 % contra el
spot, así que un error de tarifa aérea del tamaño del rango declarado los mueve de color.

---

### 3. Precios de mercado 2026 de los nueve productos distintos del café

**Estado.** Nueve de los diez precios son **valores unitarios de Trade Map 2024**, que son un
promedio contable de exportaciones registradas, no un precio de mercado vigente. Solo el café tiene
precio de mercado con fecha (FNC/ICE, 27-jul-2026).

**Por qué importa más de lo que parece.** El precio entra en el numerador y en el denominador del
margen, pero **no se cancela**: el costo se calcula como `precio × ratio`, así que un precio
desactualizado desplaza el costo en la misma proporción y deja el margen porcentual casi intacto —
mientras que el breakeven, los costos accesorios y el peso relativo del flete sí se mueven. Un precio
de 2024 con costos de 2026 es exactamente la incoherencia temporal que la auditoría corrigió en el
tipo de cambio y que aquí sigue presente.

**A quién pedírselo.** Precios spot o de contrato de 2026 por partida: Trade Map con corte 2026 en
cuanto publique, gremios sectoriales, o cotizaciones directas de exportadores.

---

### 4. Spread real del NDF para el ticket típico de una PYME

**Estado.** `spread_ndf_pyme = 0,0075` (75 pb ida y vuelta), grado C, con rango declarado 30–150 pb.

**Por qué importa.** Es lo único que puede volver negativo el valor esperado de cubrirse. A 30 días
la prima del forward es de 0,752 % y el spread supuesto de 0,750 %: el valor esperado neto queda en
**0,002 %**, es decir, prácticamente cero. Un spread real de 100 pb en vez de 75 invierte el signo de
la recomendación a ese horizonte. A 60 y 90 días el margen es más holgado y la conclusión aguanta.

**A quién pedírselo.** Mesa de dinero de Bancolombia, Davivienda, BBVA o Banco de Bogotá: spread
bid-ask cotizado para un NDF COP/CAD o COP/USD de USD 10.000–50.000 a 30, 60 y 90 días.

**Nota adicional.** El monto mínimo de operación conocido es de ~USD 10.000 (Davivienda, Tarea 7).
El modelo trabaja por kilogramo, así que **no puede determinar si un exportador concreto alcanza ese
mínimo**: eso depende del volumen total del embarque, que el proyecto no tiene. Es una restricción de
accesibilidad real que ninguna cifra del modelo captura.

---

### 5. Incoterm efectivo de cada operación

**Estado.** `pass_through_flete = 1,0`, grado C. Los diez precios de `tabla_B4` están cotizados
`Kilogramo (FOB)`, lo que justifica el supuesto, pero no se verificó contra contratos reales qué
proporción de las operaciones se pacta FOB, CFR o CIF, ni cuánto flete se traslada de hecho al
comprador cuando se negocia.

**Por qué importa.** Es el supuesto de mayor palanca del modelo. El barrido de `tabla_12` lo
muestra sin ambigüedad: para las rosas, el margen al FX vigente pasa de **+0,5 % con traslado
completo a −97,1 % si el exportador absorbe todo el flete**. Ningún otro parámetro mueve un resultado
en ese rango.

**A quién pedírselo.** Analistas de comercio exterior, o una muestra de facturas de exportación
hacia Canadá por partida.

---

### 6. Segunda cotización Cartagena–Vancouver de 20 pies

**Estado.** La única cotización disponible para Vancouver 20 pies (5.281 USD) es **más cara que la
de 40 pies**, lo que sugiere que no es una tarifa FCL comparable con la de Montreal (1.046 USD), sino
posiblemente una tarifa LCL o con recargos incluidos.

**Impacto actual.** Acotado: con `pass_through_flete = 1,0` el breakeven no depende de la ruta por
álgebra, así que la anomalía no contamina el semáforo. Sí afecta al margen porcentual, porque el
flete entra en el denominador del ingreso.

**Qué pedir.** Una segunda cotización FCL 20 pies Cartagena–Vancouver, de naviera distinta y con
fecha, para poder descartar o confirmar la primera.

---

### 7. Perfil real del exportador objetivo

**Estado.** `perfil_exportador = 'productor'`, grado C. Es una decisión de modelado, no un dato.

**Por qué importa.** Para el café, el único producto donde se puede medir, la diferencia entre
producir y comercializar cambia el ratio de costo de ~0,62 a ~0,94–0,98 — un factor cercano a 2 en el
margen resultante. Nada garantiza que la PYME exportadora típica de cada uno de los otros nueve
productos sea productora.

**Qué desbloquea.** Definir a quién está dirigido el monitor. Si el destinatario típico es un
comercializador, los márgenes de todo el modelo están sobreestimados de forma sistemática.

---

## Lo que sí está cerrado

Para que el inventario no se lea como una lista de todo lo que falta:

- La serie COP/CAD se construye de fuente primaria, en vivo, con respaldo local ejercitado por
  pruebas, y con el rezago temporal entre las dos fuentes corregido.
- Los indicadores de riesgo (volatilidad, VaR, ES, backtest, normalidad) son metodológicamente
  correctos y están validados fuera de muestra.
- Los episodios históricos están recalculados en la divisa correcta.
- El tratamiento del Plan Vallejo, del forward y de la tasa de fondeo es correcto en signo y en
  magnitud.
- La exposición cambiaria por producto (`tabla_14`) y la vulnerabilidad relativa (`tabla_10b`) **no
  dependen de ningún ratio de costo de grado C en su ordenamiento**: se apoyan en `pct_importado`,
  que es dato por producto de `tabla_B9`. Son los dos indicadores del modelo que pueden ordenar
  productos hoy mismo.

---

## Prioridad sugerida

| Orden | Vacío | Esfuerzo | Impacto |
|---|---|---|---|
| 1 | Incoterm efectivo (#5) | Bajo — una consulta a comercio exterior | Muy alto: mueve un margen de +0,5 % a −97 % |
| 2 | Ratios de costo sectoriales (#1) | Alto — ocho gremios distintos | Muy alto: desbloquea el ranking por producto |
| 3 | Spread real del NDF (#4) | Bajo — una llamada a una mesa de dinero | Alto a 30 días: invierte la recomendación |
| 4 | Flete aéreo (#2) | Bajo — una cotización | Alto para flores: mueve el semáforo |
| 5 | Precios 2026 (#3) | Medio | Medio: coherencia temporal del modelo |
| 6 | Perfil del exportador (#7) | Bajo — es una decisión, no un dato | Medio: define el destinatario |
| 7 | Cotización Vancouver (#6) | Bajo | Bajo: acotado por álgebra |

Los puntos 1, 3 y 4 son cuatro llamadas telefónicas y cambian más el modelo que semanas de trabajo
sobre el código.

---

*ODEM · Universidad EAN · 2026*
