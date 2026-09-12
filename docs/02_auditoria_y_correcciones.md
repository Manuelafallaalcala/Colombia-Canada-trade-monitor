# Auditoría cuantitativa y correcciones aplicadas

**MIC-CC · Fase 4 financiera · ODEM — Universidad EAN**

Registro de los 23 errores que la auditoría cuantitativa del 26–27 de julio de 2026 encontró en la
primera versión del modelo, qué le estaba haciendo cada uno a los resultados, y cómo quedó corregido
en la versión consolidada.

Se documenta con este nivel de detalle por una razón concreta: varios de estos errores no producían
un fallo visible. Producían un número plausible y equivocado, y un modelo que se equivoca en
silencio es peor que uno que se rompe.

---

## Estado del repositorio

Las tres generaciones del cuaderno —el original de la Fase 4, la versión auditada y la
refactorización a paquete— están **consolidadas en una sola**. El árbol de trabajo tiene un cuaderno,
una carpeta de salidas y una de documentación.

Nada se perdió: el estado previo a la consolidación está en el primer commit del repositorio y se
recupera con `git show` o `git checkout` sobre ese commit. Mantener tres versiones vivas en paralelo
tenía sentido mientras la auditoría estaba en curso y había que poder contrastar; una vez cerradas
las correcciones, solo generaba ambigüedad sobre cuál era la buena.

| Artefacto | Estado |
|---|---|
| `notebooks/mic_cc_modelo_financiero.ipynb` | Cuaderno único, ejecutado de principio a fin |
| `src/mic_cc/` | Paquete con toda la lógica del modelo |
| `tests/test_modelo.py` | 66 pruebas, todas pasan |
| `outputs/tables/` | 21 tablas |
| `outputs/figures/` | 6 figuras |
| `data/raw/` | 9 fuentes del Bloque A, **nunca modificadas** |
| `data/processed/fx_copcad.xlsx` | Serie cruzada COP/CAD construida por el modelo |

---

## Cómo verificar las correcciones

Cada error de esta lista tiene una prueba de regresión que lo fija:

```bash
python -m pytest tests/ -q            # 66 pruebas
```

El criterio de diseño de la suite es que **toda prueba debe poder fallar**. La primera versión del
proyecto reportaba "verificaciones" que eran identidades algebraicas —que la razón de costo
financiero a 60 días sobre 30 días diera exactamente 2,000 (la fórmula es lineal en días), que una
correlación diera 1,000 cuando el propio comentario la predecía antes de medirla, que una razón
constante por construcción resultara constante—. Contar eso como validación es contarse una
historia.

---

## A. Errores que invalidaban resultados

| # | Problema | Corrección | Efecto medido |
|---|---|---|---|
| 1 | **Incoherencia de incoterm.** Los diez precios están cotizados FOB y el modelo les restaba el flete internacional. Bajo FOB lo paga el comprador; bajo CFR el exportador lo cobra dentro del precio. En ninguno de los dos casos destruye margen: se estaba cobrando dos veces. | Parámetro explícito `pass_through_flete`, con barrido de sensibilidad 0,0 / 0,5 / 1,0. | Origen real del −348 % del carbón y del margen negativo de las flores. No era la economía de esos productos. |
| 2 | **Tipo de cambio obsoleto.** Base FX de diciembre de 2024 combinada con costos, tasas y precios de 2026. | Serie reconstruida en vivo desde 2014 hasta la fecha de ejecución. | El modelo estaba calibrado ~36 % por encima del mercado. |
| 3 | **Episodios en la divisa equivocada.** `tabla_B6` mide los episodios en TRM (COP/USD) y el modelo aplicaba esos porcentajes al COP/CAD, que es otra divisa. | Recalculados sobre la serie cruzada real, tomando el COP/CAD vigente en las fechas de inicio y fin. | Error de **39,1 pp** en el episodio 2014-2016. |
| 4 | **Beneficio de Drawback fantasma.** Se sumaba el 19 % del costo importado a un margen cuya base de costos nunca cargó IVA. Las exportaciones son exentas con derecho a devolución (Arts. 481, 485, 489 y 850 del ET), así que ese IVA se recupera de todos modos. | Valor financiero del *float* del IVA mientras se tramita la devolución. El 19 % bruto se conserva como cota superior declarada. | Sobreestimación de ~17×. |
| 5 | **Signo del forward invertido.** Con `i_COP > i_CAD` el forward COP/CAD cotiza *sobre* el spot: el exportador que vende CAD a plazo **cobra prima**. El modelo tomaba el valor absoluto de los puntos forward y lo llamaba "costo de cobertura". | Paridad cubierta exacta y con signo, más el spread del NDF, que faltaba por completo. | La conclusión "cubrirse" estaba forzada por construcción, no obtenida de los datos: con \|puntos forward\| ∝ T y \|VaR\| ∝ √T la desigualdad no podía invertirse a ningún horizonte. |
| 6 | **Factor de costo 0,60 uniforme.** Al ser idéntico para los diez, volvía `margen% = 1 − factor − accesorios` igual para todos. | Banda `[min, base, max]` por producto, con grado de evidencia, y semáforo robusto sobre toda la banda. | Cualquier ranking previo de rentabilidad por producto era un artefacto del precio por kilogramo. |

---

## B. Errores metodológicos

| # | Problema | Corrección |
|---|---|---|
| 7 | √T aplicado a **cuantiles** de una distribución cuya normalidad el propio modelo rechaza con Jarque-Bera. | Cuantil empírico multihorizonte como método primario; √T solo como referencia, con su sesgo medido y el N efectivo por solapamiento reportado. |
| 8 | Retorno logarítmico compuesto con `(1+r)`. | `nivel × exp(r)`. |
| 9 | Desalineación TRM ↔ Bank of Canada: la TRM del día *D* refleja el mercado de *D−1*. | Alineación explícita. **Volatilidad 16,55 % → 13,93 %**: 262 pb eran ruido de emparejamiento, no riesgo. |
| 10 | Jarque-Bera calculado con momentos corregidos por sesgo (`pandas.skew()`, `pandas.kurt()` devuelven G1 y G2). | Momentos poblacionales (g1, g2), que es como está definido el estadístico. |
| 11 | Backtest de Kupiec in-sample reportado como validación. Comparar una muestra contra su propio percentil arroja ~5 % de violaciones por construcción. | Solo fuera de muestra, sin look-ahead: el VaR pronosticado para *t* usa únicamente los retornos anteriores a *t*. |
| 12 | Escenarios ±10 % / −15 % arbitrarios. | Cuantiles empíricos a 90 días de la propia serie, que es el horizonte de cobro típico. |

---

## C. Errores de datos y supuestos

| # | Problema | Corrección |
|---|---|---|
| 13 | Precio del café a 1,45 USD/lb, contradiciendo la fuente ICO/FNC que el propio archivo citaba. | **Fuente primaria FNC** (27-jul-2026): cierre NY 324,55 USc/lb + prima Colombia ≈ **7,817 USD/kg**. |
| 14 | USD/CAD fijado en 1,33 sin una fecha coherente con su fecha de consulta. | Bank of Canada, dato vigente, con la serie legacy IEXE0101 para el tramo anterior a 2017 sin la cual los episodios de 2014-2016 no se pueden reexpresar. |
| 15 | Flete marítimo aplicado a las flores, de las que ~92 % se exportan **por aire** desde El Dorado, y tarifa de contenedor aplicada al carbón, que es **granel**. | Dimensión `modo_transporte`, clase de densidad para el payload útil, y recargo reefer. |
| 16 | IBR —tasa **interbancaria**— usado como costo de fondeo de una PYME, y dividido entre 365 siendo nominal base 360. | Conversión nominal→E.A. correcta y tasa de fondeo PYME (IBC crédito ordinario, 19,19 % E.A.) con el IBR como piso. |
| 17 | Costos accesorios de exportación ausentes por completo. | `costos_accesorios_pct_fob`: flete interno a puerto, THC, agenciamiento aduanero, DEX, seguro de carga y GMF. |
| 18 | Perfil del exportador indefinido: producir no cuesta lo mismo que comprar para revender. | Parámetro `perfil_exportador`. Para el café hay dato duro de la FNC: el ratio costo/FOB de un comercializador es ~0,94–0,98 según la TRM vigente, frente a ~0,62 asumido para un productor. |

---

## D. Arquitectura y verificación

| # | Problema | Corrección |
|---|---|---|
| 19 | Todo en el espacio global de un kernel: 82 celdas, `productos` mutado en sitio, nombres sombreados entre celdas. | Paquete con separación de intereses y funciones puras. El cuaderno orquesta; no calcula. |
| 20 | Fórmula de margen duplicada en tres celdas independientes. | Una sola implementación en `modelo.margen()`. |
| 21 | `clasificar_riesgo` con los umbrales ligados como argumentos por defecto en tiempo de definición, lo que congelaba el tipo de cambio de clasificación en silencio ante cualquier recalibración. | Umbrales explícitos, más `semaforo_robusto` evaluado sobre toda la banda de costos. |
| 22 | "Verificaciones" que no podían fallar. | Suite `pytest` de inversión, control, detección y **regresión sobre cada error de esta auditoría**. |
| 23 | El README afirmaba que el cuaderno corría sin descargas externas mientras llamaba a una API en vivo, y el repositorio traía un archivo `USDCAD_2020_2024.xlsx` que el modelo nunca leía. | Respaldo local funcional, y ejercitado por la suite de pruebas en vez de solo afirmado. |

---

## Puntos abiertos al cierre de la auditoría: estado actual

La auditoría dejó siete puntos abiertos. Dos se cerraron; cinco siguen abiertos y son **recolección
de datos, no programación**.

### Cerrados

**Figuras de la versión 3.** Al cierre de la auditoría no se generaron porque una directiva de
Windows Application Control bloqueaba la extensión nativa de matplotlib en la máquina de trabajo. La
restricción ya no está vigente: **las seis figuras se generan correctamente** y la verificación final
del cuaderno las exige con una aserción. El cuaderno conserva la degradación elegante —si matplotlib
vuelve a fallar, calcula las 21 tablas igual e informa el motivo— porque el núcleo analítico no
depende de poder dibujar.

**Procedencia de `nest-asyncio2`.** La auditoría marcó este paquete para verificar antes de publicar
el repositorio, porque el canónico es `nest-asyncio`. Verificado: es un fork mantenido
(`Chaoses-Ib/nest-asyncio2`) que `ipykernel` 7.x instala como dependencia transitiva, no un paquete
añadido por error. Por ser transitiva no corresponde declararla en `requirements.txt`, que ahora
lista solo dependencias directas.

### Siguen abiertos

Los cinco restantes —ratios de costo sectoriales, flete aéreo y a granel, precios de mercado 2026 de
los nueve productos distintos del café, spread real del NDF, e incoterm efectivo por operación—
están inventariados con su fuente concreta en
[`04_datos_pendientes.md`](04_datos_pendientes.md).

---

*ODEM · Universidad EAN · 2026*
