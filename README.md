# MIC-CC — Commercial Intelligence Monitor Colombia-Canada

Financial risk model for the Colombia–Canada Comprehensive Economic and Trade Agreement (TLCC), built for the top 10 Colombian export products shipped through the Cartagena–Montreal and Cartagena–Vancouver routes. The project quantifies FX risk (COP/CAD), breakeven exchange rates, historical stress scenarios, natural hedging, working-capital cost, forward-hedging cost-benefit, and the Plan Vallejo / VAT Drawback tax benefit, to answer one question for each product: **how much of its margin actually survives a realistic shock, and what can be done about it before it happens.**

Developed for ODEM (Observatorio de Dinamica Empresarial y Mercados) — Universidad EAN, 2026.

## Model modules

The analysis is organized as 12 sequential stages inside a single notebook, each building on the previous one's output:

| # | Module | What it answers |
|---|--------|------------------|
| 1-4 | Data pipeline | Build the daily COP/CAD cross-rate (2020-2024) from TRM (COP/USD) and USD/CAD, and the product/route/cost dataset for the top 10 exports |
| 5 | Value at Risk (VaR) | Historical VaR at 95%/99%, Expected Shortfall, Kupiec backtest, rolling VaR, Jarque-Bera normality test |
| 6 | Margin scenarios | Gross margin for 10 products x 2 routes x 3 FX scenarios (60 combinations) |
| 7 | Breakeven FX rate | The COP/CAD level at which each product stops being profitable, with a Verde/Amarillo/Rojo risk semaphore |
| 8 | Natural hedge | How much the margin is cushioned by imported-input costs that move with the same exchange rate as revenue |
| 9 | Historical stress testing | Margin under 4 real historical COP/CAD episodes (2014-2024), including the 2022-2024 peso appreciation |
| 10 | Cost of working capital | How much of the margin is eroded by the IBR interest rate while payment is in transit (30/60/90 days) |
| 11 | Hedging cost-benefit | Whether a forward/NDF contract is worth its cost, compared against VaR, Expected Shortfall, and worst historical loss |
| 12 | Drawback / VAT adjustment | The final, most complete margin figure, after adding the Plan Vallejo VAT-recovery benefit on imported inputs |

## Reproducing the analysis

```bash
git clone https://github.com/<your-username>/MIC-CC-ODEM-EAN.git
cd MIC-CC-ODEM-EAN
python -m venv .venv
.venv\Scripts\activate        # Windows (use `source .venv/bin/activate` on macOS/Linux)
pip install -r requirements.txt
cd Notebooks
jupyter nbconvert --to notebook --execute --inplace 04_financial_model.ipynb
```

Source data lives in `dataraw/` (already included in this repository, so the notebook runs end to end with no external downloads). Results are written to `outputs/tables/` (11 tables, `tabla_04` to `tabla_11`) and `outputs/figures/` (5 charts, `figura_04` to `figura_08`). The notebook uses paths relative to `Notebooks/`, so it must be executed from inside that folder (as shown above).

## Key findings

- **COP/CAD annualized volatility is 15.0%**, with a 95% historical VaR of -13.8% over a 90-day horizon — a realistic worst case for an exporter waiting on payment for a quarter.
- **9 of the 10 products carry a wide breakeven safety margin** (Verde risk rating); the exception is **Carbon bituminoso**, whose breakeven FX rate exceeds even the highest COP/CAD ever observed in the 2020-2024 series — a structural cost problem (container freight tariffs applied to a bulk commodity), not a currency one.
- The truly adverse historical scenario for this model is **peso appreciation** (2022-2024), not devaluation — because these are export earners paid in CAD with costs in COP, a stronger peso erodes margin, the opposite of the conventional devaluation narrative.
- **Natural hedging and the forward-hedging cost-benefit decision are largely product-invariant** by construction (both scale with revenue), so the model adds a **relative-vulnerability ranking** (loss as % of each product's own margin) to identify which products should be hedged first under a limited budget.
- The **VAT Drawback benefit** is the one adjustment that meaningfully differentiates products, because it depends on each product's imported-input share (25%-65%) — Medicamentos corticosteroides benefits the most (7.4% of revenue).

## Suggested citation

Manuela Alcala. *MIC-CC: Commercial Intelligence Monitor Colombia-Canada — Financial Risk Model.* ODEM, Universidad EAN, 2026.

## License

See [LICENSE](LICENSE) for usage terms.
