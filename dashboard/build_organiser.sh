#!/bin/bash
# Regenerates organiser/organiser_data.json from every */*_dbt_companies.json, then embeds it into organiser/index.html.
# Run this after any <region>_dbt_companies.json changes. It is separate from the Meetup pipeline.
set -euo pipefail
cd "$(dirname "$0")"

python3 build_organiser_data.py

python3 - <<'PYEOF'
import json

with open('organiser/organiser_data.json') as f:
    data = json.load(f)
with open('organiser/index.template.html') as f:
    html = f.read()

# escape "</" so a string in the data can't close the <script> tag
html = html.replace('__ORGANISER_DATA__', json.dumps(data, ensure_ascii=False).replace('</', '<\\/'))

with open('organiser/index.html', 'w') as f:
    f.write(html)

print('organiser/index.html regenerated')
PYEOF
