# MIC-CC — Modelo financiero auditado y corregido

Documento del **modelo reconstruido** tras la auditoría cuantitativa del 26–27 de julio de 2026.
No sustituye al `README.md` original, que describe la primera versión del proyecto.

> **Nada del trabajo previo se borró.** El cuaderno original, su respaldo y sus salidas siguen en su
> sitio, sin modificar. Cada versión escribe en su propia carpeta.

---

## Qué hay en el repositorio

| Artefacto | Versión | Estado |
|---|---|---|
| `Notebooks/04_financial_model.ipynb` | original | intacto |
| `Notebooks/04_financial_model.ipynb.bak` | respaldo del original | intacto |
| `outputs/` | salidas del original | intactas |
| `Notebooks/05_financial_model_auditado.ipynb` | **v2** — correcciones aplicadas, cuaderno autocontenido | ejecutado |
| `outputs_v2/` | 16 tablas + 5 figuras | completas |
| `Notebooks/06_financial_model_v3.ipynb` | **v3** — orquesta el paquete, costos por producto | ejecutado |
| `outputs_v3/` | 14 tablas | completas (figuras: ver *Limitación de entorno*) |
| `src/mic_cc/` | paquete con la lógica del modelo | — |
| `tests/test_modelo.py` | 45 pruebas | todas pasan |
| `dataraw/` | datos fuente | **nunca modificados** |

---

## Cómo ejecutar

```bash
python -m venv .venv
.venv\Scripts\activate                # Windows
pip install -r requirements.txt
pip install pytest

python -m pytest tests/ -q            # 45 pruebas

cd Notebooks
jupyter nbconvert --to notebook --execute --inplace 06_financial_model_v3.ipynb
```

El modelo descarga la TRM oficial (Datos Abiertos del Banco de la República) y el USD/CAD del Bank
of Canada. **Si no hay red, cae automáticamente a los archivos de `dataraw/`** — incluido
`USDCAD_2020_2024.xlsx`, que la versión original tenía en el repositorio y nunca leía.

---

## Arquitectura

```
src/mic_cc/
├── config.py    parámetros, overrides de datos, transporte y costos por producto
├── datos.py     adquisición de series FX y construcción de la tasa cruzada COP/CAD
├── riesgo.py    VaR histórico, Expected Shortfall, backtesting, normalidad
└── modelo.py    margen, breakeven, logística, tasas, cobertura, tributario
```

El cuaderno **orquesta; no calcula**. Cada fórmula existe una sola vez: el cuaderno original tenía
la ecuación de margen implementada tres veces de forma independiente.

---

## Correcciones aplicadas

### Errores que invalidaban resultados

| # | Problema | Corrección | Efecto medido |
|---|---|---|---|
| 1 | **Incoherencia de incoterm.** Los 10 precios son FOB y el modelo les restaba el flete internacional. Bajo FOB lo paga el comprador; bajo CFR el exportador lo cobra dentro del precio. | Parámetro `pass_through_flete`. | Origen real del −348% del carbón y del margen negativo de las flores. |
| 2 | **Tipo de cambio obsoleto.** Base FX de dic-2024 con costos, tasas y precios de jul-2026. | Serie reconstruida en vivo 2014→hoy. | El modelo estaba calibrado ~36% por encima del mercado. |
| 3 | **Episodios en la divisa equivocada.** `tabla_B6` los mide en TRM (COP/USD) y se aplicaban al COP/CAD. | Recalculados sobre la serie cruzada real. | Error de **39,1 pp** en el episodio 2014-2016. |
| 4 | **Beneficio de Drawback fantasma.** Se sumaba 19% del costo importado a un margen cuyo costo nunca incluyó IVA; las exportaciones son exentas con derecho a devolución (Arts. 481/485/489/850 ET). | Valor financiero del *float* del IVA. | Sobreestimación de ~17×. |
| 5 | **Signo del forward invertido.** Con i_COP > i_CAD el forward cotiza sobre el spot: el exportador que vende CAD a plazo **cobra prima**. | Paridad cubierta exacta y con signo, más el spread NDF que faltaba. | La conclusión "cubrirse" estaba forzada por construcción. |
| 6 | **Factor de costo 0,60 uniforme.** Volvía `margen% = 1 − factor − accesorios`, idéntico para los 10. | Banda por producto con grado de evidencia. | Cualquier ranking previo por producto era artefacto del precio por kilogramo. |

### Errores metodológicos

| # | Problema | Corrección |
|---|---|---|
| 7 | √T aplicado a **cuantiles** de una distribución cuya normalidad el propio modelo rechaza. | Cuantil empírico multi-horizonte; √T solo como referencia, con sesgo medido y N efectivo por solapamiento. |
| 8 | Retorno logarítmico compuesto con `(1+r)`. | `nivel × exp(r)`. |
| 9 | Desalineación TRM ↔ Bank of Canada: la TRM de *D* refleja el mercado de *D−1*. | Alineación explícita. **Volatilidad 16,55% → 13,93%** (262 pb eran ruido de emparejamiento). |
| 10 | Jarque-Bera con momentos corregidos por sesgo. | Momentos poblacionales, que es como está definido el estadístico. |
| 11 | Backtest de Kupiec in-sample reportado como validación. | Solo fuera de muestra, sin look-ahead. |
| 12 | Escenarios ±10% / −15% arbitrarios. | Cuantiles empíricos a 90 días de la propia serie. |

### Errores de datos y supuestos

| # | Problema | Corrección |
|---|---|---|
| 13 | Precio del café a 1,45 USD/lb, contradiciendo la fuente ICO/FNC citada. | **Fuente primaria FNC** (27-jul-2026): NY 324,55 USc/lb + prima ≈ **7,817 USD/kg**. |
| 14 | USD/CAD a 1,33 sin fecha coherente. | Bank of Canada, dato vigente. |
| 15 | Flores por vía marítima: el 92% se exporta **por aire** desde El Dorado. Carbón en contenedor siendo granel. | Dimensión `modo_transporte`, clase de densidad y recargo reefer. |
| 16 | IBR (tasa **interbancaria**) como costo de fondeo de una PYME, dividido entre 365 siendo nominal base 360. | Conversión nominal→E.A. correcta y tasa de fondeo PYME (IBC 19,19% E.A.) con el IBR como piso. |
| 17 | Costos accesorios de exportación ausentes. | `costos_accesorios_pct_fob` (flete interno, THC, agenciamiento, seguro, GMF). |
| 18 | Perfil del exportador indefinido. | `perfil_exportador`. Para el café, dato duro FNC: ratio 0,943 comercializando vs. ~0,62 produciendo. |

### Arquitectura y verificación

| # | Problema | Corrección |
|---|---|---|
| 19 | Todo en el espacio global de un kernel; 82 celdas; `productos` mutado en sitio; shadowing de nombres entre celdas. | Paquete con separación de intereses; funciones puras. |
| 20 | Fórmula de margen duplicada en tres celdas. | Una sola implementación. |
| 21 | `clasificar_riesgo` con umbrales ligados como defaults en tiempo de definición. | Umbrales explícitos + `semaforo_robusto` sobre toda la banda. |
| 22 | "Verificaciones" que no podían fallar (`razón 60d/30d = 2.000`, correlación 1.000 predicha de antemano, ratio constante por construcción). | Suite `pytest` de inversión, control, detección y **regresión sobre cada error de la auditoría**. |
| 23 | README afirmaba que el cuaderno corría sin descargas externas mientras llamaba a una API en vivo. | Respaldo local funcional. |

---

## Grados de evidencia

Cada parámetro lleva un grado. `config.resumen_evidencia()` los inventaría.

- **A** — dato duro de fuente primaria, verificable y fechado.
- **B** — dato gremial o sectorial cualitativo, cuantificado por inferencia razonada.
- **C** — **supuesto de trabajo. No es evidencia.**

Reparto actual: **A** 5 · **B** 4 · **C** 12.

**Regla de lectura:** ninguna conclusión que dependa de un parámetro de grado C debe presentarse
como hallazgo. Por eso los resultados por producto se reportan como **banda**, no como punto, y el
semáforo solo asigna Verde si el producto resiste en el extremo desfavorable de su propia banda.

---

## Lo que sigue abierto

Todo esto es **recolección de datos, no programación**:

1. **Siete de los diez ratios de costo son grado C.** Solo el café alcanza grado A. Antes de
   publicar cualquier ranking de rentabilidad por producto hacen falta estructuras de costo reales:
   FNC (café, perfil productor), Asocolflores (flores), Fedeacua (trucha), ANDI (farmacéutico y
   siderúrgico), Fenalcarbón (carbón), Inexmoda (confección).
2. **Flete aéreo Bogotá–Canadá** y **flete a granel del carbón**: estimaciones de orden de magnitud,
   declaradas como grado C. Requieren cotización real.
3. **Precios de los nueve productos distintos del café**: valores unitarios de Trade Map 2024, no
   precios de mercado de 2026.
4. **Spread real del NDF** cotizado por un banco para el ticket típico de una PYME.
5. **Incoterm efectivo** de cada operación y grado real de traslado del flete al comprador.
6. **Segunda cotización Cartagena–Vancouver 20 pies**: la única disponible es más cara que la de 40
   pies, lo que sugiere que no es una tarifa FCL comparable.
7. **`requirements.txt` incluye `nest-asyncio2`**; el paquete canónico es `nest-asyncio`. Verificar
   su procedencia antes de publicar el repositorio.

---

## Limitación de entorno

Las figuras de la v3 no se generaron porque una directiva de **Windows Application Control** bloquea
la DLL nativa de matplotlib (`_backend_agg`) en esta máquina. Es una restricción del sistema, no del
modelo: las 5 figuras de la v2 se generaron correctamente en el mismo repositorio antes de que la
política entrara en vigor.

El cuaderno detecta la condición, informa el motivo y **continúa**: las 14 tablas se calculan igual.
Al levantar el bloqueo basta reejecutarlo, sin ningún cambio de código.

---

## Citación

Manuela Alcalá. *MIC-CC: Monitor de Inteligencia Comercial Colombia-Canadá — Modelo financiero de
riesgo, versión auditada.* ODEM, Universidad EAN, 2026.
