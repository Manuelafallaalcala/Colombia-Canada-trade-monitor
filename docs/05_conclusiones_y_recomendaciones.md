# Conclusiones, resultados y recomendaciones

Este documento responde la pregunta que en realidad importa después de correr todo el modelo: ¿y con esto, qué se hace? Los números completos están en `outputs/tables/` y la redacción académica está en `docs/03_working_paper_seccion5.md`; aquí está la lectura práctica, en orden de qué hacer primero.

Todas las cifras de este documento salen de una sola corrida del modelo (`notebooks/mic_cc_modelo_financiero.ipynb`), con la TRM y el USD/CAD del día en que lo ejecuté. Si vuelves a correrlo otro día, el spot cambia y algunos números de este documento —sobre todo los que dependen del spot vigente— se van a mover. Eso no es un defecto, es cómo está diseñado: revisa la sección 1 del cuaderno para saber con qué tasa se generó la corrida que estás leyendo.

## 1. El hallazgo que cambia la conversación

Antes de este modelo, la pregunta que se hacía sobre estos diez productos era "¿qué pasa si el peso se devalúa?". Es la pregunta equivocada. Los diez son generadores de divisas: facturan en CAD y pagan sus costos en COP, así que lo que les pega es el peso *fortaleciéndose*, no debilitándose. De los cuatro episodios históricos que probé (dos devaluaciones grandes, un choque de pandemia y una apreciación), el peor para estos exportadores no fue ninguna devaluación — fue la apreciación de 2022-2024 (-24,7% en la tasa COP/CAD). Ahí es donde el carbón, el producto más expuesto, llega a un margen de -11,8%.

Y esto no es un escenario hipotético lejano: la tasa spot con la que corrí el modelo está a un 87% del camino hacia el escenario pesimista que uso en el resto del análisis. No es un riesgo a vigilar a futuro, es la condición del mercado ahora mismo.

## 2. Cómo quedaron los diez productos

Con el semáforo exigente (verde solo si el producto sobrevive en el extremo desfavorable de su propio rango de costos, no en el punto medio):

**Verdes — margen resiste incluso en el escenario pesimista:**

| Producto | Margen base | Margen pesimista | Colchón sobre el spot actual |
|---|---|---|---|
| Medicamentos corticosteroides | 39,4% | 37,0% | 63,8% |
| Café sin tostar | 32,3% | 26,6% | 34,9% |
| Medias/calcetines de fibra sintética | 20,1% | 16,0% | 31,5% |
| Frutas tropicales (guayaba/mango) | 17,7% | 11,7% | 19,4% |
| Filetes de trucha congelados | 15,2% | 10,8% | 23,0% |

**Rojos — el margen no sobrevive el extremo desfavorable de su propio rango de costos:**

| Producto | Margen base | Margen pesimista | Colchón sobre el spot actual |
|---|---|---|---|
| Accesorios de tubería (hierro/acero) | 15,2% | 9,4% | 16,7% |
| Nueces y semillas preparadas | 11,2% | 6,7% | 15,4% |
| Carbón bituminoso | 8,3% | 0,5% | 2,3% |
| Rosas frescas cortadas | 4,0% | -0,01% | 1,5% |
| Flores otras (pompones/hortensias) | 3,8% | -0,01% | 1,5% |

Léelo así: rosas y pompones no es que vayan mal — es que ya casi no tienen margen que perder. Con el spot de hoy sobran apenas 1,5 puntos porcentuales antes de operar en pérdida. Eso no depende de ningún supuesto grado C: es aritmética de precio menos costo con la tasa de hoy.

No publico esto como un ranking de "qué producto exportar". Siete de los diez ratios de costo son grado C — un supuesto de trabajo, no un dato verificado — así que parte de este orden podría cambiar en cuanto alguien consiga el dato real. Lo que sí es información sólida, porque no depende de esos supuestos: **el tamaño del colchón de rosas y pompones frente al spot actual es una alerta operativa real, hoy**, no una conclusión que dependa de qué tan bien estimé un costo.

## 3. La cobertura natural: quién ya tiene protección y no lo sabe

Los productos que importan un insumo pagan parte de su costo en la misma dirección en que se mueve su ingreso, así que ese costo actúa como amortiguador — sin que nadie contrate nada. Lo cuantifiqué así: comparé el margen de cada producto contra el margen que tendría el mismo producto con cero insumo importado.

Café (25% de insumo importado): en el escenario pesimista, la cobertura natural le recupera 1,9 puntos de margen. Carbón (15% importado): 1,3 puntos. Es simétrico — el mismo mecanismo que amortigua la caída también recorta la subida en el escenario optimista, casi exactamente igual de fuerte. No es gratis ni es magia, es simplemente que una parte del costo también depende del tipo de cambio.

**Esto es aprovechable de inmediato:** un exportador que hoy compra el insumo importado más barato disponible, sin mirar la moneda en que cotiza, está renunciando a este colchón sin saberlo. No hace falta ningún instrumento financiero para usarlo, solo elegir el proveedor pensando en la moneda de cotización.

## 4. ¿Vale la pena cubrirse con un forward/NDF?

Con las tasas de interés reales de Colombia y Canadá que usé (paridad de tasas cubierta, con el signo bien puesto: el forward le paga una prima al exportador cuando la tasa colombiana está por encima de la canadiense, que es el caso actual):

- A 30 días: valor esperado neto de la cobertura ≈ +0,00002%. Prácticamente cero.
- A 60 días: ≈ +0,0076%.
- A 90 días: ≈ +0,0152%, y evita hasta 0,12 puntos porcentuales de la cola de pérdida (Expected Shortfall).

El valor esperado por sí solo casi no justifica el trámite. **La razón real para cubrirse no es ganar en promedio, es recortar la cola** — y eso sí es un beneficio genuino, más claro mientras más largo el horizonte. Mi lectura: tiene sentido para los productos con menos colchón (rosas, pompones, carbón, nueces), donde el escenario de cola es justo el que ya está cerca de ocurrir; no vale la pena el trámite para los productos verdes con colchón amplio, donde el forward cuesta un spread real (0,75%) para evitar una cola que de todas formas no los toca.

Este número (0,75% de spread) es una cotización de referencia, no una cotización bancaria real — está en la lista de `docs/04_datos_pendientes.md` como el dato más urgente de conseguir, porque a partir de 100 puntos básicos de spread la recomendación se puede invertir.

## 5. Lo que de verdad le pesa al margen: no es el IVA, es el capital de trabajo

Dos mecanismos financieros que se suelen confundir:

- **Plan Vallejo / drawback del IVA:** el beneficio real (el valor financiero de tener el IVA diferido, no su 19% nominal) mueve el margen entre 0,00 y 0,50 puntos porcentuales. El máximo es nueces (+0,50 pp) y trucha (+0,48 pp); carbón y accesorios de tubería quedan en 0,00 porque `tabla_B3` marca su tratamiento como "no está claro" — otro pendiente de `docs/04`.
- **Costo financiero de esperar el pago (capital de trabajo) a 90 días:** erosiona el margen entre 2,7 y 4,3 puntos porcentuales, según el producto.

Es decir, **el costo de financiar la espera del pago pesa entre 6 y 9 veces más que todo el beneficio del drawback del IVA junto**. Si el objetivo es mejorar el margen de estos exportadores con una intervención puntual, negociar mejores plazos de pago o acceso a factoring más barato tiene más impacto que cualquier trámite alrededor del IVA.

## 6. Cómo se debería usar este código y esta investigación

**Sí sirve para:**
- Ver, producto por producto, cuánto margen queda después de un choque cambiario realista, con la lógica completa a la vista en `src/mic_cc/` — no es una caja negra.
- Monitorear: como la serie de tipo de cambio se descarga en vivo, correr el cuaderno cada cierto tiempo da una foto actualizada del colchón de cada producto sin tener que rehacer nada.
- Priorizar en qué datos vale la pena invertir tiempo: `docs/04_datos_pendientes.md` ya identifica qué parámetro cambia más el resultado por unidad de esfuerzo en conseguirlo (el incoterm efectivo de las rosas mueve el margen entre +0,5% y -97%; ningún otro dato tiene esa palanca).
- Enseñar el método: cada fórmula es una función pura en `src/mic_cc/modelo.py`, documentada y con pruebas, así que sirve como referencia de cómo se construye correctamente un modelo de riesgo cambiario de exportación.

**No sirve para:**
- Publicar un ranking de rentabilidad entre los diez productos, por lo ya explicado en la sección 2: siete de los diez costos son un supuesto, no un dato.
- Tomar sola una decisión de cobertura real. El spread del NDF que usé es de referencia; antes de contratar algo, esa cifra hay que reemplazarla por una cotización bancaria real.
- Asumir que el incoterm de cada operación es FOB solo porque así está parametrizado por defecto. Para rosas y pompones en particular, revisar el incoterm real de cada contrato es el paso obligatorio antes de creer cualquier número de margen.

**Para extenderlo:** todos los supuestos están centralizados en `src/mic_cc/config.py` — para actualizar un dato real (una cotización de flete, un spread bancario, un precio de mercado 2026), se cambia ahí y se vuelve a correr el cuaderno; ninguna fórmula necesita tocarse. Los 67 tests en `tests/test_modelo.py` están para que, si algo se rompe al cambiar un dato, se note de inmediato y no tres tablas más adelante.

## 7. Lo positivo y aprovechable, resumido

Si solo te llevas cinco cosas de este proyecto:

1. **Cinco de los diez productos (medicamentos, café, medias, frutas tropicales, trucha) mantienen margen positivo incluso en el escenario cambiario más adverso que probé.** Eso es una base sólida, no un resultado frágil.
2. **La cobertura natural es real y se puede usar hoy, sin pagar por ningún instrumento**, con tal de escoger el proveedor del insumo importado pensando en la moneda de cotización.
3. **Cubrirse con NDF a 90 días tiene valor esperado positivo y reduce la cola de pérdida**, especialmente para los productos con menos colchón — es una recomendación concreta y accionable, no solo un diagnóstico.
4. **El capital de trabajo pesa mucho más que el IVA en el margen final** — ahí está la palanca de mejora más grande que no depende de ningún supuesto grado C.
5. **El modelo es reproducible y queda vivo**: se puede volver a correr con datos actualizados en cualquier momento, y el resultado de hoy ya está guardado en `outputs/` para no depender de tener que ejecutarlo para consultarlo.

Lo que sigue pendiente — y que depende de conseguir datos, no de programar más — está priorizado en [`04_datos_pendientes.md`](04_datos_pendientes.md).
