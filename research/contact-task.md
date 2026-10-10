# contact search

targets: a json file keyed by city folder. each city has its `file`, `region` and `people`; each person has `id`, `name`, `employer`, `title`, `talks` and `evidence_urls`. named leads (people in the city's SEARCH_METHOD.md) come first.
load the tools with ToolSearch "select:WebSearch,WebFetch".

## pace
- run exactly one WebSearch or WebFetch per message. never run several in parallel: bursts trip the rate limit within seconds.
- on too_many_requests, retry the same call. after 5 failed retries in a row, stop.
- if a search is refused or blocked by a permission check, stop, write what you have and say so. never work around it.
- write the output file after every 10 people, merged with what is already there.

## per person: up to 3 calls, stop at the first match
1. WebSearch `"<name>" <employer>`, allowed_domains ["linkedin.com"].
2. WebSearch `"<name>" <employer>` with no domain filter. results can include the linkedin profile, a sessionize page, a speaker page or a github profile.
3. WebFetch an `evidence_url` that is an event, speaker or author page (never linkedin.com), and look for a profile link next to the name.

with no employer, put the city in the query. the city only narrows the search; it is never a tie on its own.

## people an earlier round missed (`linkedin_confidence` low)
do not repeat the employer queries. search the talk instead:
1. WebSearch `"<distinctive 4-6 words of the talk title>" <name>` with no domain filter. this finds the recording, the slides, the speaker page or a write-up of the event.
2. WebFetch the best speaker page, agenda entry, event write-up, slides page, video page or post by the person, and look for a profile link next to the name or in the description.
3. WebSearch `"<name>" <chapter city>`, allowed_domains ["linkedin.com"], and accept only a result tied to the talk, the event, the community or the employer.

## names that are not a full latin name
- a handle (in parentheses, or the whole name): search `"<handle>"` with the employer or community. look for that exact username on x.com, github.com, zenn.dev, qiita.com, connpass.com, note.com, ithelp.ithome.com.tw or medium.
- a chinese, japanese or korean name: search it with the employer or community, then its romanisation if the record gives one.
- a first name or an initial only: search the community event page, not the web. accept the full name that page gives next to the talk.

## accept a match only when
- the name or handle as recorded is in the result title, the profile, or next to the link, AND
- one of these ties it to the person:
  - the recorded employer, current or past.
  - the recorded talk, event or community.
  - a school, project or other detail the record states.
  - the profile address equals the person's github username, or their own github profile lists it.
  - an event page or write-up of their talk links the profile next to their name.
- AND there is exactly one candidate. two plausible profiles for one name is a miss, unless only one carries a tie above.

record a miss when:
- the only tie is a data role in the right city, even for a rare name.
- the only tie is the subject of the talk.
- the url is a post, an article or a status, not a profile. never build a profile url from it.
- the url appears only in a search summary and never as a result or a link on a page.
- the result title shows only a first name and an initial ("Sonny N."), unless the profile address carries the full surname and the recorded employer is in the title.
- the url is listed for that person in `research/rejected_matches.json`.
- the result places the person outside the region while the record places them inside it. say so in the reply instead.

copy urls exactly as shown, minus `/overlay/...`, `?locale=`, `?utm_...` and other query suffixes. never fetch linkedin.com.

## record
- linkedin: `{"linkedin_url": "...", "evidence": "<result title, location>", "confidence": "high|medium", "based_in_region": true|false|null, "city": "...|null"}`
- any other profile: `{"profile": {"type": "<a type in validate.PROFILE_TYPES>", "url": "...", "source": "<the page or result that ties it>"}, "evidence": "...", "confidence": "high|medium", "based_in_region": true|false|null, "city": "...|null"}`. `website` is a personal site only, never a company page.
- miss: `{"confidence": "low"}`. a handle you could not search is a miss too.
- confidence high: the name and employer are both in the result title or profile. medium: the tie comes from the snippet, a past role, a name variant or the page around the link.
- location only when the result states it. follow the location rules in README §6.

## output
write `<out dir>/<folder>.json`, keyed by person id. name any helper file so it does not end in `.json`. edit no other file and do not commit.

reply in under 120 words: per city, searched / found / missed / not reached, and the person ids of any match you were unsure about.

## apply and check
```sh
python3 research/apply_contacts.py <city file> <out dir>/<folder>.json
python3 research/validate.py
```
read every unsure match against the record before applying. to turn one down, replace its entry with `{"reject": {"url": "<the url>", "reason": "<why>"}}`. apply_contacts.py records it in `research/rejected_matches.json` and marks the person searched, so no later pass offers that profile again.

## worked cases
- **past role at the employer:** Konrad Maliszewski, VP Technology at Crisp, talk "Intelligent Snowflake Warehouse Management". the linkedin search title shows another employer, so step 1 is not enough. step 3 fetches his Data Engineers London meetup page, which links `linkedin.com/in/konradmal/` next to "Konrad Maliszewski, VP Technology at Crisp". record it as medium, with the meetup page as the evidence.
- **github username:** Keith Y., github `yayekit`, bio "Data Engineer, domain in Bioinformatics". the result `linkedin.com/in/yayekit/` shows "Keith Yemelianovskyi - Data Engineer, Toronto". the address equals the github username, so record it as medium.
- **event write-up:** Naiwen Chiang, talk at WiDS Taipei 2026. the event's write-up on medium links her profile under her name. record it as medium, with the write-up as the evidence.
- **city only:** Juan Felipe Valencia Toro, github bio "Senior Data Engineer", Medellín. the result shows a data engineer in Antioquia at an employer the record does not give. nothing else ties it, so record a miss.
- **initial in the result:** Abiodun Shomoye, recorded at Deloitte Nigeria. the result title reads "Abiodun S. - Manager, Data Analytics and AI at Deloitte Nigeria" at `linkedin.com/in/shomoye/`. the address carries the surname and the title names the employer, so record it as medium.
