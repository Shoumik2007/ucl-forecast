#!/bin/bash
# Update the website with the newest dashboard_data.json from your Downloads folder.
set -e
cd "$(dirname "$0")"
NEW=$(ls -t ~/Downloads/dashboard_data*.json 2>/dev/null | head -1)
if [ -z "$NEW" ]; then
  echo "No dashboard_data.json found in Downloads. Download it from Colab first (Files pane > outputs > dashboard_data.json)."
  exit 1
fi
echo "Using $NEW"
cp "$NEW" dashboard_data.json
python3 build.py
npx --yes vercel deploy --prod --yes
echo "Done: https://ucl-forecast.vercel.app"
