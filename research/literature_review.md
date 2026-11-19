# Literature Review — Momentum in FX (living document)

> Every entry below was verified against the publisher / SSRN / DOI record.
> **Never add a paper you have not verified.** Record title, authors, year, source,
> DOI/SSRN/arXiv URL, research question, methodology, findings, limitations, and how it
> translates into a testable hypothesis. Distinguish the original methodology from our
> adaptations.

---

## 1. Moskowitz, Ooi & Pedersen (2012) — Time series momentum

- **Title:** Time series momentum
- **Authors:** Tobias J. Moskowitz, Yao Hua Ooi, Lasse Heje Pedersen
- **Year / source:** 2012, *Journal of Financial Economics*, 104(2), 228–250
- **DOI:** https://doi.org/10.1016/j.jfineco.2011.11.003
- **Research question:** Does an asset's own past return predict its future return
  (time-series / trend-following), across many markets?
- **Methodology (original):** For 58 futures markets (including FX futures), form a signal
  from the past 12-month return (long if positive, short if negative), hold for 1 month,
  volatility-scale positions. Test profitability and risk properties.
- **Findings (original):** Time-series momentum earns positive average returns across
  asset classes; returns are largely uncorrelated across markets and with other factors;
  the effect is strongest at 12-month formation and decays at longer horizons.
- **Limitations:** Daily/monthly futures data, not spot intraday FX; 12-month horizon is
  far from our 30-minute horizon; transaction costs and live implementability are discussed
  but not the focus.
- **Translation to our hypothesis:** If past returns predict future returns at 12-month
  horizon in FX futures, it is worth testing whether *short-horizon* past returns predict
  *short-horizon* future returns in spot EUR/USD. **This is an adaptation** — different
  horizon, different instrument (spot vs futures), different market structure. It does not
  imply our 30-minute test will find momentum.

## 2. Menkhoff, Sarno, Schmeling & Schrimpf (2012) — Currency momentum strategies

- **Title:** Currency momentum strategies
- **Authors:** Lukas Menkhoff, Lucio Sarno, Maik Schmeling, Andreas Schrimpf
- **Year / source:** 2012, *Journal of Financial Economics*, 106(3), 660–684
- **DOI:** https://doi.org/10.1016/j.jfineco.2012.06.009
- **Research question:** Do past winner/loser currencies continue to win/lose
  (cross-sectional momentum in FX)?
- **Methodology (original):** Monthly data, up to 48 currencies, 1976–2010. Rank currencies
  by past USD excess return over a formation window (1–12 months), go long top quintile /
  short bottom quintile, hold 1–12 months.
- **Findings (original):** Winner-minus-loser spread of up to ~10% p.a.; not explained by
  traditional risk factors; distinct from the carry trade; consistent with investor
  over-/under-reaction; limits to arbitrage make it hard to exploit after costs.
- **Limitations:** Cross-sectional (needs many currencies), monthly horizon, spot rates
  with USD excess returns — none of which matches a single-pair 15-minute test.
- **Translation to our hypothesis:** Currency momentum exists at monthly, cross-sectional
  level. Our test is **time-series, single-pair, intraday** — a different question. We cite
  this paper for the *existence* of FX momentum, not as evidence for 30-minute EUR/USD
  predictability.

## 3. Elaut, Frömmel & Lampaert (2015) — Intraday momentum in FX markets

- **Title:** Intraday momentum in FX markets: Disentangling informed trading from
  liquidity provision
- **Authors:** Gert Elaut, Michael Frömmel, Kevin Lampaert
- **Year / source:** 2015, SSRN (working paper)
- **URL:** https://ssrn.com/abstract=2694985
- **Research question:** Is there intraday momentum in FX (first half-hour return predicts
  last half-hour return), and is it driven by informed trading or liquidity provision?
- **Methodology (original):** Tick-by-tick transaction data for RUB/USD on the Moscow
  Interbank Currency Exchange (MICEX), 2005–2014. Regress last-half-hour return on
  first-half-hour return.
- **Findings (original):** Significant positive intraday momentum (first half-hour →
  last half-hour). For this dataset, momentum is **not** explained by informed trading;
  it is consistent with risk aversion for overnight holdings among liquidity providers.
- **Limitations:** Single emerging-market pair (RUB/USD), single exchange with a defined
  trading day and overnight gap, tick data — very different from 24-hour spot EUR/USD.
  Findings may not generalise to major pairs.
- **Translation to our hypothesis:** This is the **closest** paper to our experiment:
  intraday, FX, short-horizon return predictability. **Our adaptation differs in:**
  (a) pair (EUR/USD vs RUB/USD), (b) market (24h decentralised spot vs single-exchange
  session with open/close), (c) definition (adjacent 30-min blocks vs first-vs-last
  half-hour of the day), (d) data (15-min OHLC candles vs tick data). We test the
  *spirit* of the hypothesis — short-horizon continuation — not their exact specification.

---

## How to add a new paper

1. Verify the DOI/SSRN/arXiv URL resolves to the claimed title/authors.
2. Create `research/research_notes/<slug>.md` with the 8 fields above.
3. Add a summary row here and a BibTeX entry in the notebook References section.
4. State explicitly what is original vs adapted in our implementation.
