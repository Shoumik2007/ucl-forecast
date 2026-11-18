# Champions League Forecast dashboard

`index.html` is a single self-contained page (data and crests embedded). It works anywhere static files are served.

## Deploy to Vercel
```bash
cd dashboard
npx vercel login          # once, in your browser
npx vercel deploy --prod  # publishes public/index.html (live at https://ucl-forecast.vercel.app)
```
Vercel deployments are public by default. Turn on "Vercel Authentication" in the project settings if you want it private.

## Refresh after a matchday
1. Re-run the Colab notebook (Runtime → Run all).
2. In Colab's Files pane, download `outputs/dashboard_data.json` into this folder.
3. `python3 build.py`, then redeploy (or ask Claude to republish the artifact).

Files: `template.html` (page), `build.py` (merges data + crests), `team_meta.json` (display names, crest paths), `crests/` (80px crests from ESPN).
