# contact search

targets: a json file keyed by city folder. each city has its `file`, `region` and `people`; each person has `id`, `name`, `employer`, `title`, `talks` and `evidence_urls`. named leads (people in the city's SEARCH_METHOD.md) come first.
load the tools with ToolSearch "select:WebSearch,WebFetch".

## pace
- run exactly one WebSearch or WebFetch per message. never run several in parallel: bursts trip the rate limit within seconds.
- on too_many_requests, retry the same call. after 5 failed retries in a row, stop.
- write the output file after every 10 people, merged with what is already there.

## per person: up to 3 calls, stop at the first match
1. WebSearch `"<name>" <employer>`, allowed_domains ["linkedin.com"].
2. WebSearch `"<name>" <employer>` with no domain filter. results can include the linkedin profile, a sessionize page, a speaker page or a github profile.
3. WebFetch an `evidence_url` that is an event, speaker or author page (never linkedin.com), and look for a profile link next to the name.

if step 1 already ran in an earlier round (`linkedin_confidence` low), start at step 2, and use a talk or title keyword plus the chapter city instead of the employer in the linkedin search.

## names that are not a full latin name
- a handle (in parentheses, or the whole name): search `"<handle>"` with the employer or community. look for that exact username on x.com, github.com, zenn.dev, qiita.com, connpass.com, note.com, ithelp.ithome.com.tw or medium.
- a chinese, japanese or korean name: search it with the employer or community, then its romanisation if the record gives one.
- a first name or an initial only: search the community event page, not the web.

## accept a match only when
- the name or handle as recorded is in the result title, the profile, or next to the link, AND
- the result or page ties it to the recorded employer, talk or community (a past role there counts), AND
- there is exactly one candidate. two plausible profiles for one name is a miss.

record a miss when:
- the only tie is a data role in the right city.
- the url is a post, an article or a status, not a profile. never build a profile url from it.
- the title shows only a first name and an initial ("Sonny N.").

copy urls exactly as shown, minus `/overlay/...` and `?locale=` suffixes. never fetch linkedin.com.

## record
- linkedin: `{"linkedin_url": "...", "evidence": "<result title, location>", "confidence": "high|medium", "based_in_region": true|false|null, "city": "...|null"}`
- any other profile: `{"profile": {"type": "<a type in validate.PROFILE_TYPES>", "url": "...", "source": "<the page or result that ties it>"}, "evidence": "...", "confidence": "high|medium", "based_in_region": true|false|null, "city": "...|null"}`. `website` is a personal site only, never a company page.
- miss: `{"confidence": "low"}`. a handle you could not search is a miss too.
- confidence high: the name and employer are both in the result title or profile. medium: the tie comes from the snippet, a past role, a name variant or the page around the link.
- location only when the result states it. follow the location rules in README §6.

## output
write `<out dir>/<folder>.json`, keyed by person id. edit no other file and do not commit.

reply in under 120 words: per city, searched / found / missed / not reached, and the person ids of any match you were unsure about.

## apply and check
```sh
python3 research/apply_contacts.py <city file> <out dir>/<folder>.json
python3 research/validate.py
```
read every unsure match against the record before applying. mark it `{"confidence": "low"}` when nothing ties the profile to the recorded employer, talk or community.

## worked case
Konrad Maliszewski, VP Technology at Crisp, talk "Intelligent Snowflake Warehouse Management". the linkedin search title shows another employer, so step 1 is not enough. step 3 fetches his Data Engineers London meetup page, which links `linkedin.com/in/konradmal/` next to "Konrad Maliszewski, VP Technology at Crisp". record it as medium, with the meetup page as the evidence.
