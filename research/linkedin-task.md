# linkedin location pass

targets: <scratch>/linkedin_targets.json, keyed by city. each city has its file and up to 12 people, best-ranked first.
load the search tool with ToolSearch "select:WebSearch".

## per person: one search
WebSearch(query='"<name>" <employer>', mode="standard", allowed_domains=["linkedin.com"])
- if the name is only a handle (no real name, e.g. a zenn/qiita handle), skip the person.
- if the first search finds nothing that matches, you may try once more with '"<name>" <title keyword> <city>'. never more than 2 searches per person.
- never fetch linkedin.com pages. use only what the search result returns.
- if WebSearch is refused or says the limit is reached, stop searching and write what you have.

## accept a result only when
- the result title has the person's full name, AND
- it names the recorded employer, or the result text ties the profile to that employer or to the recorded talk (e.g. previous role at that employer).
- the result states a location (city, area or country) for that profile.
when the name matches but nothing ties it to the employer or talk, skip the person; a common name is not evidence.

## record
- confidence "high" when name + recorded employer + location are all in the result; "medium" when the profile has moved on but the result still ties it to the recorded employer.
- based_in_region: true if the stated location is inside the chapter's region, false if outside. a country alone (e.g. "Canada", "Australia") is not enough for a metro region: skip unless the region is a country (belgium, netherlands, lithuania).
- city: the location as the result states it. evidence: the result title plus the location, e.g. "linkedin search result: Kevin Dang - EdgeRed, Docklands, Victoria, Australia".
- evidence_url and linkedin_url: the linkedin.com/in url exactly as it appears in the result.
- docklands, victoria is melbourne, not sydney. greater/metro areas count for the metro city ("Greater Seattle Area" is seattle).

## output, per city
write <scratch>/locations/<city>_linkedin.json:
{"<person id>": {"based_in_region": true|false, "city": "...", "evidence_url": "<linkedin url>", "linkedin_url": "<same url>", "evidence": "...", "confidence": "high|medium"}}
apply with: python3 research/apply_locations.py <city file> <scratch>/locations/<city>_linkedin.json
validate with: python3 research/validate.py <city file>   (must print ok)
the apply script only fills unknown locations. edit no other file and do not commit.

reply with a table per city: searched, located true, located false, skipped; then any result you were unsure about.
