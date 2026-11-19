# Project Status — AlgoMonster

> Single source of truth for progress. Updated after every completed lesson.

**Last updated:** 2026-11-19
**Current branch:** `arena/75da6782-algomonster`
**Primary market / instrument / timeframe:** Forex · EUR/USD · 15 minutes

---

## Completed projects

- _None yet._ Project 001 (Momentum) is in progress.

## Completed lessons

| Lesson | Notebook | Status | Date |
|--------|----------|--------|------|
| 01.1 — Forex data analysis (EUR/USD 15-min) | `notebooks/01_foundations/01_forex_data_analysis.ipynb` | ✅ Created & validated (JSON + syntax). **Awaiting user execution & results.** | 2026-11-19 |

## Current lesson

**Lesson 01.1 — `01_forex_data_analysis.ipynb`**

- Objective: Acquire and analyse EUR/USD 15-minute historical data; test whether the
  previous 30-minute return predicts the subsequent 30-minute return.
- Research question: *"Does recent price momentum contain information about subsequent
  EUR/USD returns?"*
- Status: Notebook delivered. **Waiting for the user to run it (Kaggle or local) and share
  outputs.** Do not proceed to Lesson 2 automatically.

## Outstanding exercises

From Lesson 01.1 (Section 14):

1. Re-run with `period="60d"` vs a shorter window; report how `n`, correlation and p-value change.
2. Compute lag-2 and lag-3 autocorrelations of 30-min returns; plot an autocorrelation function (ACF).
3. Split the sample by hour-of-day (London / New York / Asia) and compare 30-min momentum.
4. Recompute the test using **overlapping** 30-min returns and explain why overlapping biases
   standard errors.
5. Add a simple scatter + OLS regression line and report slope, R² and 95% confidence interval.
6. Write a 5-sentence interpretation: statistical vs economic significance.

## Known bugs / issues

- **yfinance 15-min history is limited to ~60 days** (Yahoo Finance constraint). Lesson 1
  therefore uses `period="60d", interval="15m"`. Longer histories require a different vendor
  or resampling from 1-hour data — addressed in a later lesson.
- **yfinance `Volume` for FX is tick volume, not traded volume.** Do not use it as a liquidity
  or VWAP input. Noted in notebook Section 13.
- **Yahoo may return empty data** (rate limits / network). The notebook handles this with a
  clear error message and a synthetic-data fallback for code-path testing only (labelled as
  such; never presented as real results).
- No other known bugs. Backtesting engine does not exist yet (starts in Project 004/005).

## Next planned task

1. User runs Lesson 01.1 and shares: (a) row count & date range, (b) correlation, p-value,
   slope, (c) plots, (d) exercise answers.
2. Mentor reviews the user's outputs, identifies errors, and only then defines Lesson 01.2
   (proposed: moving-average momentum signal + first honest backtest with costs).
3. Do **not** start Lesson 2 until the user explicitly requests continuation.

## Repository health

- [x] Directory structure created (research / notebooks / src / tests / data / reports)
- [x] `README.md`, `requirements.txt`, `.gitignore`, `PROJECT_STATUS.md` created
- [x] Notebook JSON validated (`python -m json.tool`)
- [x] Notebook code cells syntax-checked (`ast.parse` per cell)
- [x] `pytest tests/` passing (data-validation unit tests)
- [ ] Notebook executed end-to-end with live yfinance data (pending user run — sandbox
      network does not guarantee Yahoo access; see notebook fallback note)
