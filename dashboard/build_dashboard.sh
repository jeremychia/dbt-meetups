#!/bin/bash
# Regenerates dashboard_data.json and world_path.txt, then embeds both into index.html
# (index.template.html is a complete HTML document, so no wrapping is needed).
# Run this after enriched/*.json or speaker-identities.json change.
set -euo pipefail
cd "$(dirname "$0")"

python3 build_dashboard_data.py
[ -f world_path.txt ] || python3 build_world_map.py

python3 - <<'PYEOF'
import json

with open('dashboard_data.json') as f:
    data = json.load(f)
with open('world_path.txt') as f:
    world_path = f.read().strip()

with open('index.template.html') as f:
    html = f.read()

# escape "</" so a string in the data can't close the <script> tag
html = html.replace('__DATA_JSON__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))
html = html.replace('__WORLD_PATH__', world_path)

with open('index.html', 'w') as f:
    f.write(html)

print('index.html regenerated')
PYEOF
