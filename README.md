# AlgoMonster — Algorithmic Trading Research Laboratory

> **Build the skill to discover whether a trading edge exists — not to manufacture impressive backtests.**

A progressive, research-driven laboratory for building and validating algorithmic trading
strategies in Python. Each project moves through the full scientific workflow:

**Academic Research → Hypothesis → Mathematical Model → Python Implementation → Backtest →
Statistical Validation → Improvement → Paper Trading**

Primary market: **Forex** · Initial instrument: **EUR/USD** · Initial timeframe: **15 minutes** ·
Environment: **Kaggle Notebooks + local Jupyter**

---

## How this repository is organised

```
algo-trading-research/
│
├── README.md                      ← you are here
├── PROJECT_STATUS.md              ← progress tracker (completed / current / next)
├── requirements.txt
├── .gitignore
│
├── research/
│   ├── papers/                    ← PDFs / links to original papers (no fabricated citations)
│   ├── research_notes/            ← per-paper structured notes
│   └── literature_review.md       ← living synthesis of the literature
│
├── notebooks/                     ← main learning interface (numbered, executable)
│   ├── 01_foundations/
│   ├── 02_momentum/
│   ├── 03_mean_reversion/
│   ├── 04_breakout/
│   ├── 05_risk_management/
│   ├── 06_statistical_validation/
│   ├── 07_machine_learning/
│   └── 08_paper_trading/
│
├── src/                           ← reusable, tested code (promoted from notebooks)
│   ├── data/                      ← acquisition, cleaning, validation
│   ├── indicators/
│   ├── strategies/
│   ├── backtesting/
│   ├── risk/
│   └── analytics/
│
├── tests/                         ← pytest suite for src/
│
├── data/
│   ├── raw/                       ← untouched downloads (git-ignored)
│   └── processed/                 ← cleaned, analysis-ready (git-ignored)
│
└── reports/
    ├── charts/
    └── performance/
```

Notebooks are the **learning interface**. Code is promoted to `src/` only when it is
sufficiently developed and tested. Large raw datasets, API keys and credentials are never
committed.

---

## Curriculum — 8 projects

| # | Project | Folder | Core question |
|---|---------|--------|---------------|
| 001 | **Momentum** | `notebooks/02_momentum/` | Does past return predict future return? |
| 002 | **Mean Reversion** | `notebooks/03_mean_reversion/` | Does price revert to a statistical mean? |
| 003 | **Breakout** | `notebooks/04_breakout/` | Do breakouts of range/volatility persist? |
| 004 | **Risk Management** | `notebooks/05_risk_management/` | How do we size, stop and survive drawdowns? |
| 005 | **Statistical Validation** | `notebooks/06_statistical_validation/` | Is the edge real or overfitted? |
| 006 | **Market Regimes** | (within 02–07) | When does each strategy work? |
| 007 | **Machine Learning** | `notebooks/07_machine_learning/` | Can ML find signal without leakage? |
| 008 | **Automated Trading** | `notebooks/08_paper_trading/` | Can the system survive live conditions? |

`notebooks/01_foundations/` contains the shared data foundations every project builds on.

Each project contains multiple lessons and practical deliverables. Lessons are completed
**one at a time** — the next lesson starts only after the current one is reviewed.

---

## Quick start

### Option A — Kaggle (recommended for Lesson 1)

1. Go to [kaggle.com](https://www.kaggle.com) → **Create → New Notebook**.
2. In the notebook, run:
   ```bash
   !pip install -q yfinance pandas numpy matplotlib scipy statsmodels
   ```
3. Upload `notebooks/01_foundations/01_forex_data_analysis.ipynb` via
   **File → Upload Notebook**, or copy its cells into the new notebook.
4. Run cells top to bottom (Kernel → Restart & Run All).

> Kaggle provides pandas, NumPy, matplotlib, scipy and statsmodels pre-installed.
> Only `yfinance` needs installing. No API keys are required for EUR/USD via yfinance.

### Option B — Local Jupyter

```bash
git clone <this-repo-url>
cd algomonster
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab
# open notebooks/01_foundations/01_forex_data_analysis.ipynb
```

### Run tests

```bash
pytest tests/ -v
```

---

## Notebook standard

Every notebook is a valid `.ipynb` file with:

1. Project overview · 2. Research paper · 3. Research question · 4. Financial concepts ·
5. Mathematical formulation · 6. Data acquisition · 7. Data cleaning ·
8. Strategy implementation · 9. Backtesting · 10. Performance evaluation ·
11. Visualizations · 12. Research interpretation · 13. Limitations ·
14. Exercises · 15. References

Small, focused cells — never one giant cell. Clean variable names, comments, type hints
where they help. Fixed random seeds where randomness is involved.

---

## Backtesting & research standards

- Realistic assumptions: spreads, slippage, commissions, swaps, pip values, execution timing.
- **No look-ahead bias**: never use information unavailable at trade time.
- Signal generation, position generation, order execution, risk management and performance
  calculation are kept separate.
- Performance is never judged by profitability alone (Sharpe, Sortino, max drawdown,
  profit factor, expectancy, exposure, recovery factor, …).
- **Never fabricate papers, authors, findings or URLs.** Original papers are preferred over
  secondary summaries. Adaptations are always labelled as adaptations.
- Never claim a notebook was executed unless it was actually executed.
- Never claim a strategy is profitable without evidence.

---

## Current status

See **[PROJECT_STATUS.md](PROJECT_STATUS.md)** for completed lessons, outstanding exercises,
known issues and the next planned task.

| Lesson | Title | Status |
|--------|-------|--------|
| 01.1 | Forex data analysis — EUR/USD 15-min (`01_forex_data_analysis.ipynb`) | ✅ Ready to run |

**Next:** Lesson 1.2 (to be defined after Lesson 1.1 results are reviewed). Do not proceed
automatically.

---

## Research references (verified)

Full structured notes live in `research/research_notes/` and `research/literature_review.md`.

- Moskowitz, T. J., Ooi, Y. H., & Pedersen, L. H. (2012). Time series momentum.
  *Journal of Financial Economics*, 104(2), 228–250.
  https://doi.org/10.1016/j.jfineco.2011.11.003
- Menkhoff, L., Sarno, L., Schmeling, M., & Schrimpf, A. (2012). Currency momentum
  strategies. *Journal of Financial Economics*, 106(3), 660–684.
  https://doi.org/10.1016/j.jfineco.2012.06.009
- Elaut, G., Frömmel, M., & Lampaert, K. (2015). Intraday momentum in FX markets:
  Disentangling informed trading from liquidity provision. SSRN.
  https://ssrn.com/abstract=2694985

> These three papers use **different data and horizons** from our 15-minute EUR/USD
> experiment. The notebook explains exactly how they differ — see Lesson 1, Section 2.

---

## Licence & disclaimer

For research and education. Nothing here is financial advice. Past backtest performance
does not guarantee future results. Paper trade before risking capital.
