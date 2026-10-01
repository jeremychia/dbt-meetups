# location pass

for each person in your files whose based_in_region is null, find where they are based. work in this order:
priority_tier 1, then 2, then everyone else, and within a tier people with past_chapter_talks first.

list them with:
  python3 -c "import json,sys;d=json.load(open(sys.argv[1]));[print(p['priority_tier'],p['id'],'|',p['name'],'|',p['title'],'|',c['name'],'|',[e['url'] for e in p['speaker_evidence']][:3]) for c in d['companies'] for p in c['people'] if p['based_in_region'] is None]" <file>

## the web-search allowance for this session is used up. do not call WebSearch. use fetches:
- the person's own evidence urls first: speaker bios on event pages, blog author boxes, sessionize speaker pages.
- github: https://api.github.com/users/<login> has a "location" field (unauthenticated limit is about 60 calls an hour, shared with other agents; use it only when the person has a known github login, and stop if you get 403).
- meetup.com gql2 endpoint (plain curl POST works) for speaker and organiser member profiles that show a city.
- zenn.dev/<handle> and qiita.com/<handle> profiles (and their APIs) for tokyo.
- company team or author pages that name the person's office.
- never fetch linkedin.com, and never infer a location from a person's name.

## evidence ladder
- high: the person's own profile or bio states a city or country (github location, speaker bio, author box, personal site).
- medium: an in-person talk or organiser role at an in-region event within the last 2 years, AND the employer has an office in the region. an online talk is not evidence.
- a meetup member profile is high only when the member is tied to the person (the rsvp or host of the event they spoke at, or a matching github login). a match on name alone is medium at best and never supports false.
- based_in_region false needs the same standard: a profile that states a city outside the region.
- if neither applies, leave the person out of the patch. unknown is a valid answer.
- the region is the chapter's metro area (or country, for belgium, the netherlands and lithuania).

## output
write <scratch>/locations/<city>.json as {"<person id>": {"based_in_region": true|false, "city": "<city as stated>", "evidence_url": "...", "evidence": "<short quote or description>", "confidence": "high|medium"}}
then run from the repo root: python3 research/apply_locations.py <city file> <scratch>/locations/<city>.json
then: python3 research/validate.py <city file>   (must print ok)
the script only fills unknown locations and never overwrites a known one. edit no other file and do not commit.

reply with, per city: unknown before and after, how many true / false, and which sources worked.
