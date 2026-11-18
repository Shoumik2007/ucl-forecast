# UCL Forecast 2026-27

Predicts every remaining UEFA Champions League match and each club's chance of winning the 2026-27 title.

**Live dashboard: https://ucl-forecast.vercel.app**

- **Title race:** each club's chance of finishing top 8, reaching each knockout round and winning.
- **Matchdays and what-if:** win/draw/loss odds, expected goals and most likely score for every remaining league-phase match. Enter your own results and re-run the season in the browser.
- **Head to head:** any two of the 36 clubs as a league match, a two-legged tie or a final.

## How it works

1. **Data:** domestic league results from 15 European leagues since 2016 ([football-data.co.uk](https://www.football-data.co.uk)), every Champions League match since 2017-18 ([fixturedownload.com](https://fixturedownload.com)), and club Elo ratings scraped from [clubelo.com](http://clubelo.com) (its API is currently down).
2. **Ratings and features:** one chronological pass over all ~46,000 matches builds the model's own Elo ratings plus pre-match features: domestic form, shots-on-target share, league strength, and Champions League experience and pedigree (knockout games, finals and titles in the previous 3 seasons). Only information available before kick-off is used.
3. **Model selection:** logistic-regression and gradient-boosting candidates, trained on UCL-only or UCL + domestic matches, are compared. The winner is chosen on 2023-24 and tested on 2024-25 to now. The current model is *Elo + pedigree* logistic regression (test log-loss 0.91 vs 1.01 for base rates). ClubElo ratings are compared on the same matches and kept only if they win validation (they don't, currently).
4. **Goals model:** a Poisson model with the same features gives expected goals and scorelines.
5. **Simulation:** 20,000 Monte Carlo runs of the rest of the season. Real knockout draws and results are used as soon as they appear: finished ties are locked, half-played ties simulate only the second leg, and undrawn rounds follow UEFA's bracket rules. A replay of 2025-26 checks the mechanics (11/11 checks pass).

Training and simulation run on Google Colab (CPU); the dashboard re-runs the simulation client-side for what-if scenarios.

## Repository

| Path | What it is |
|---|---|
| `ucl_predictor.ipynb` | The full pipeline: download, ratings, training, simulation, replay test, export. Open in Colab and *Run all*. |
| `dashboard/template.html` | The dashboard page (plain HTML/CSS/JS, no build tooling). |
| `dashboard/build.py` | Merges `dashboard_data.json` + crests into the page; writes `public/index.html` for Vercel. |
| `dashboard/update.sh` | One-command refresh: takes the newest `dashboard_data.json` from Downloads, rebuilds and deploys. |
| `dashboard/public/index.html` | The deployed page. |
| `UCL_Forecast_Update_Guide.pdf` | Step-by-step guide to updating after each matchday. |

## Updating after a matchday

1. Open the notebook in Colab, **Runtime → Run all** (about 5 min).
2. Download `outputs/dashboard_data.json` from Colab's Files pane.
3. Run `dashboard/update.sh`.

Details and troubleshooting: [`UCL_Forecast_Update_Guide.pdf`](UCL_Forecast_Update_Guide.pdf).

## Limits

Ratings are frozen at the time of each run, so later rounds are less certain than they look. Injuries, suspensions and rotation aren't modelled.

---
Unofficial fan project, not affiliated with UEFA or any club. Club crests are trademarks of their clubs (images via ESPN).
