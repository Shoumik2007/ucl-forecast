"""Build index.html: template + dashboard_data.json (exported by the notebook) + embedded crests."""
import base64, json, pathlib
here = pathlib.Path(__file__).parent
d = json.loads((here / 'dashboard_data.json').read_text())
meta = json.loads((here / 'team_meta.json').read_text())
for t in d['teams']:
    m = meta.get(t['name'], {})
    t['display'] = m.get('display', t['name'])
    crest = here / m['crest'] if m.get('crest') else None
    t['crest'] = ('data:image/png;base64,' + base64.b64encode(crest.read_bytes()).decode()) if crest and crest.exists() else ''
blob = json.dumps(d, separators=(',', ':'), ensure_ascii=False).replace('</', '<\\/')
html = (here / 'template.html').read_text().replace('__DATA__', blob)
(here / 'index.html').write_text(html)              # artifact version (host adds the document skeleton)
site = here / 'public'; site.mkdir(exist_ok=True)       # standalone version for Vercel / any static host
(site / 'index.html').write_text(
    '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}'
    'body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    '</head>\n<body>\n' + html + '\n</body>\n</html>\n')
print(f"index.html: {len(html) / 1024:.0f} KB, {sum(1 for t in d['teams'] if t['crest'])}/36 crests")
