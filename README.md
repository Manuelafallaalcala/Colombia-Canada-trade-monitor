# Colombia–Canada Trade Monitor

MIC-CC, Phase 4 — a model that prices the currency risk Colombian exporters carry when they sell into Canada under the CCoFTA.

## Why this exists

The Colombia–Canada trade agreement already zeroed out tariffs on the products I'm looking at here — the ten export lines with the strongest revealed comparative advantage toward Canada. So the question that's actually still open for them isn't "how much tariff protection is left" (none, it's fully phased out), it's how much of the margin on these products survives the exchange rate, and what an exporter can do about it before it happens. That's what this project answers, product by product.

I built this as the financial module (Phase 4) of ODEM's Colombia–Canada trade intelligence project, at Universidad EAN.

## The result I wasn't expecting

Going in, I assumed the risk was the peso devaluing — that's the story everyone tells about Colombian exporters and FX. It's backwards for this group. These ten products are foreign-currency earners: they invoice in CAD and pay their costs in COP. So a *stronger* peso is what actually hurts them, because revenue shrinks in COP terms while the cost base doesn't move. When I ran the model against the four real COP/CAD episodes since 2014, the worst one for these exporters wasn't a devaluation at all — it was the 2022–2024 appreciation, -24.7%.

## What the notebook actually does

One notebook, `notebooks/mic_cc_modelo_financiero.ipynb`. Twelve sections, each doing one job, none of them recomputing what another section already computed:

1. Build the daily COP/CAD rate from the TRM (COP/USD, Banco de la República) and USD/CAD (Bank of Canada) — lining up a one-business-day publication lag between the two sources that, left uncorrected, adds noise that isn't real volatility.
2. Value at risk: historical VaR at 95%/99%, Expected Shortfall, multi-horizon quantiles computed empirically instead of with the usual √T shortcut, which stops holding once you actually check it against the data. Backtested out of sample with Kupiec's test.
3. Prices and cost structure for the ten products, each with a cost-ratio range and a grade for how solid the number behind it is, instead of one uniform cost factor.
4. A manual check against the worked example in the original methodology, so a mistake upstream shows up here before it quietly propagates through everything downstream.
5. Margins and breakeven, across two routes and three scenarios per product.
6. Natural hedge — how much buying imported inputs cushions a producer's margin, measured against the right counterfactual (the same producer with zero imported input, not something else).
7. The historical stress test on those four episodes.
8. Working-capital cost from financing the wait to get paid, at 30/60/90 days.
9. Whether hedging with a forward or NDF is worth it, given the actual COP and CAD interest rates, signed correctly — a forward pays the exporter a premium when Colombian rates run above Canadian ones, not the other way around.
10. Plan Vallejo / VAT drawback — what the deferred VAT is worth as a financing benefit, not its 19% face value.
11. Sensitivity sweeps on the three assumptions the result leans on most, so a conclusion that doesn't survive the sweep doesn't get reported as one.
12. One summary table, per product: margin range, breakeven, risk rating, FX exposure, hedging priority, evidence grade.

## Why the numbers come with a grade, not just a value

Every input is graded A, B or C depending on where it actually came from: A is a dated figure from a primary source, B is trade-association data I had to quantify through reasoned inference, C is a working assumption I haven't been able to verify yet. Right now **14 of the 24 inputs I inventoried are grade C** — and that count includes modelling choices, not just data: how much of the freight cost actually reaches the exporter, which exporter profile applies, the density class used for payload. Those move the result as much as any number does, so I didn't leave them out of the count just because they're not, technically, a dataset.

That's why:

- Results are reported as ranges, never as a single number.
- The green/yellow/red rating for each product only comes out green if it survives the worst end of its own range, not the midpoint. Just requiring that flips the color on 6 of 20 product-route combinations.
- I'm not publishing a ranking of which product is more profitable than which. Seven of the ten cost ratios are grade C, so a ranking built on them would mostly measure who sells at a higher price per kilo, not who's actually better off.

What's missing to close most of this isn't more code, it's people to call — `docs/04_datos_pendientes.md` lists exactly what's missing, who holds it, and what it would unlock.

One more thing worth knowing before you trust a number out of this: the FX series is pulled live every time the notebook runs, so the spot rate and the scenario values move with the run date. If you're going to quote a figure from this project somewhere, say when it was run.

## Running it

```bash
git clone <URL-de-tu-repositorio>
cd Colombia-Canada-trade-monitor

python -m venv .venv
.venv\Scripts\activate          # Windows; on Mac/Linux run source .venv/bin/activate instead
pip install -r requirements.txt

pytest tests/ -q                # 67 tests, should all pass

cd notebooks
jupyter nbconvert --to notebook --execute --inplace mic_cc_modelo_financiero.ipynb
```

The notebook finds the repository root on its own, so it works whether you run it from `notebooks/` or from the top level. It tries to download the TRM and USD/CAD series live; with no connection it falls back to the copies saved in `data/raw/`, and that fallback path is actually exercised by the test suite, not just assumed to work. Section 1 of every run prints which source it actually used.

## Layout

```
data/raw/          the 9 source files everything is built from, each with its source URL
                    and the date I pulled it
data/processed/    the COP/CAD series the model builds from those sources
notebooks/         the one notebook — it calls functions, it doesn't compute anything itself
src/mic_cc/        the actual logic
  config.py            parameters, data overrides, cost structure per product
  datos.py             FX acquisition and the COP/CAD cross-rate
  riesgo.py            historical VaR, Expected Shortfall, backtesting, normality
  modelo.py            margin, breakeven, logistics, rates, hedging, tax
tests/test_modelo.py    67 tests
outputs/tables/    21 result tables (.xlsx), already generated
outputs/figures/   6 charts (.png), already generated
docs/              methodology guide, audit log, Working Paper section, pending-data
                   list — these are in Spanish, they're written for my readers at EAN
```

Every formula lives in exactly one place, inside `src/mic_cc/`. It didn't used to — an earlier version of this notebook had the margin formula written out three separate times, so fixing anything meant finding it in three places and hoping I'd caught all of them. I'm not repeating that.

## About the tests

The rule I held myself to: a test that can't fail isn't telling you anything. An earlier version of this project had checks that were true by construction no matter what — a 60-day financing cost divided by a 30-day one always coming out to exactly 2.000, because the formula is linear in days and of course it does. That's not a test, it's arithmetic restating itself.

The 67 tests here are four kinds: solve something two independent ways and check they agree; run a case where I already know the answer by hand; make sure a detector actually detects the thing it's supposed to catch; and pin down every concrete bug the audit found, so none of them can quietly come back.

## Docs

- [`docs/01_guia_metodologica_fase4.md`](docs/01_guia_metodologica_fase4.md) — the methodology explained from scratch, with a glossary.
- [`docs/02_auditoria_y_correcciones.md`](docs/02_auditoria_y_correcciones.md) — the 23 errors I found auditing the earlier version, what each one was doing to the numbers, and how I fixed it.
- [`docs/03_working_paper_seccion5.md`](docs/03_working_paper_seccion5.md) — the results written up as Section 5 of the Working Paper, references included.
- [`docs/04_datos_pendientes.md`](docs/04_datos_pendientes.md) — what's still missing and who to ask for it.

## Citation

Alcalá, M. (2026). *MIC-CC: Monitor de Inteligencia Comercial Colombia-Canadá — Modelo financiero de riesgo cambiario* (Fase 4). ODEM, Universidad EAN.

## License

MIT — see [`LICENSE`](LICENSE). It also spells out that this is a research model and not financial advice, and the terms that apply to the source data.
