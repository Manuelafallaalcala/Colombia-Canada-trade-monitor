# MIC-CC — Commercial Intelligence Monitor Colombia–Canada

**FX risk model for Colombian SME exporters selling into Canada under the CCoFTA.**

The Colombia–Canada Free Trade Agreement has fully phased out tariffs on the ten products analysed
here, so the binding financial risk is no longer customs duty — it is the exchange rate. This model
quantifies that risk end to end and answers one question per product: **how much of its margin
actually survives a realistic currency shock, and what can be done about it beforehand?**

Built for **ODEM** — Universidad EAN, 2026.
Phase 4 (financial) of the MIC-CC project.

> **Documentation language.** This README is in English. The methodological guide, the audit record,
> the Working Paper section and the pending-data inventory are in Spanish, in [`docs/`](docs/) —
> they are deliverables for a Colombian academic audience.

---

## The finding that reframes the problem

For these ten products, **the adverse scenario is peso *appreciation*, not devaluation.**

That is the opposite of the conventional narrative about FX risk in Colombia, and it follows
directly from what these exporters are: foreign-currency *earners*. They invoice in CAD and pay
their costs in COP, so a stronger peso shrinks their revenue in domestic-currency terms while their
cost base stays put. In the model's historical stress module, the worst of the four documented
episodes is the 2022–2024 peso appreciation (−24.7 % in COP/CAD), not any of the three devaluations.

---

## What the model computes

Twelve sequential modules, orchestrated by a single notebook over a package of pure functions:

| # | Module | Question it answers |
|---|---|---|
| 1 | FX series | Build the daily COP/CAD cross-rate from TRM (COP/USD) and USD/CAD, correcting the one-business-day lag between the two sources |
| 2 | Value at Risk | Historical VaR at 95 %/99 %, Expected Shortfall, multi-horizon empirical quantiles, out-of-sample Kupiec backtest, Jarque-Bera |
| 3 | Prices & cost structure | Ten products, with a per-product cost-ratio **band** and an evidence grade, not a single uniform factor |
| 4 | Preliminary check | The 30-row manual sensitivity table the methodology requires as a control before the model |
| 5 | Margins & breakeven | Gross margin across 10 products × 2 routes × 3 scenarios, and the COP/CAD level at which each product stops being profitable |
| 6 | Natural hedge | How much imported-input costs cushion the margin — measured against the right counterfactual, and reported as the symmetric effect it is |
| 7 | Historical stress | Margins under four real COP/CAD episodes (2014–2024), recomputed on the cross-rate rather than on the TRM |
| 8 | Working capital | Margin erosion from financing the wait for payment at 30/60/90 days |
| 9 | FX hedging | Whether a forward/NDF is worth it, with covered interest parity signed correctly |
| 10 | Plan Vallejo / VAT | The financial value of the VAT float on imported inputs |
| 11 | Sensitivity | Sweeps of the three fragile assumptions, so a conclusion that does not survive the sweep is not reported as one |
| 12 | Executive summary | One row per product: margin band, breakeven, semaphore, FX exposure, hedging priority, evidence grade |

---

## Reading the results responsibly

Every parameter carries an **evidence grade**: **A** hard data from a dated primary source,
**B** trade-association data quantified by reasoned inference, **C** a working assumption — *which is
not evidence*.

**Fourteen of twenty-four inventoried parameters are grade C**, and the inventory deliberately
includes the modelling choices (`pass_through_flete`, `perfil_exportador`, density-class payload)
that move the result as much as any datum does. Consequently:

- Per-product results are reported as a **band**, never as a point.
- The risk semaphore is **robust**: it grants Green only if the product survives at the unfavourable
  end of its own band. Requiring that flips the colour on 6 of 20 product-route combinations.
- **No profitability ranking across products is published.** Seven of the ten cost ratios are
  grade C; a ranking built on them would be an artefact of price per kilogram, not a finding.

Closing that gap is **data collection, not programming**. The full inventory — every missing datum,
which institution holds it and what it would unlock — is in
[`docs/04_datos_pendientes.md`](docs/04_datos_pendientes.md).

The FX series is downloaded **live**, so the spot rate, the scenarios and therefore the semaphore
depend on the run date. Any figure quoted outside the notebook needs its cut-off date attached.

---

## Reproducing the analysis

```bash
git clone <repository-url>
cd mic-cc-finanzas

python -m venv .venv
.venv\Scripts\activate            # Windows  (source .venv/bin/activate on macOS/Linux)
pip install -r requirements.txt

python -m pytest tests/ -q        # 66 tests

cd notebooks
jupyter nbconvert --to notebook --execute --inplace mic_cc_modelo_financiero.ipynb
```

The notebook locates the repository root itself, so it runs from either `notebooks/` or the root.

It downloads the TRM from Colombia's open-data portal and USD/CAD from the Bank of Canada Valet
API, and **falls back automatically to the files in `data/raw/` when there is no network** — the
fallback is exercised by the test suite, not just claimed. Which source was actually used is printed
in section 1 of every run.

---

## Repository layout

```
.
├── data/
│   ├── raw/           9 source files from Block A, each with source URL and consultation date
│   └── processed/     fx_copcad.xlsx — the daily cross-rate the model builds
├── notebooks/
│   └── mic_cc_modelo_financiero.ipynb    the single notebook: it orchestrates, it does not compute
├── src/mic_cc/
│   ├── config.py      parameters, data overrides, transport and per-product cost structure
│   ├── datos.py       FX acquisition and construction of the COP/CAD cross-rate
│   ├── riesgo.py      historical VaR, Expected Shortfall, backtesting, normality
│   └── modelo.py      margin, breakeven, logistics, rates, hedging, tax
├── tests/
│   └── test_modelo.py 66 tests: inversion, control, detection, and regression on every audit error
├── outputs/
│   ├── tables/        21 result tables (.xlsx)
│   └── figures/       6 charts (.png, 150 dpi)
├── docs/              methodological guide, audit record, Working Paper section, pending data
├── requirements.txt
└── LICENSE
```

Every formula exists exactly **once**, in `src/mic_cc/`. The original notebook had the margin
equation implemented three times independently, which meant any correction had to be applied in
three places or the three would silently disagree.

---

## Test suite

`tests/test_modelo.py` holds 66 tests, and the design criterion is that **every test must be able to
fail**. The first version of the project reported passing "verifications" that were algebraic
identities — a 60-day/30-day cost ratio of exactly 2.000 (the formula is linear in days), a
correlation of 1.000 that its own comment predicted before measuring it. Those validate nothing.

The tests here are of four kinds: **inversion** (solve one way, verify by an independent path),
**control** (cases with a known answer), **detection** (check that the detectors detect), and
**regression** (pin every concrete error found in the audit so it cannot come back).

---

## Documentation

| File | Contents |
|---|---|
| [`docs/01_guia_metodologica_fase4.md`](docs/01_guia_metodologica_fase4.md) | Step-by-step methodological guide to Phase 4, with concept explanations and a glossary |
| [`docs/02_auditoria_y_correcciones.md`](docs/02_auditoria_y_correcciones.md) | The 23 errors the quantitative audit found, what each one was doing to the results, and how it was fixed |
| [`docs/03_working_paper_seccion5.md`](docs/03_working_paper_seccion5.md) | Section 5 of the academic Working Paper, with APA 7 references |
| [`docs/04_datos_pendientes.md`](docs/04_datos_pendientes.md) | What is still missing, who holds it, and what each datum would unlock |

---

## Suggested citation

> Alcalá, M. (2026). *MIC-CC: Monitor de Inteligencia Comercial Colombia-Canadá — Modelo financiero
> de riesgo cambiario* (Fase 4). ODEM, Universidad EAN.

## License

MIT — see [LICENSE](LICENSE). The licence text also carries the research-use disclaimer and the
terms governing the source data.
