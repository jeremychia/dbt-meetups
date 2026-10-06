# Central search method

This is the one method behind every `<folder>/<city>_dbt_companies.json` research file. Those files feed the [organiser cockpit](../README.md#organiser-cockpit). The scripts in this folder build, extend and check them. Each city also has its own `SEARCH_METHOD.md` with city notes: where to look there, what didn't work, the key leads and a change log. New city notes start from [city-method-template.md](city-method-template.md).

| Area | Chapter | City notes |
|---|---|---|
| Europe | Amsterdam | [amsterdam](../amsterdam/SEARCH_METHOD.md) |
| Europe | Belgium | [belgium](../belgium/SEARCH_METHOD.md) |
| Europe | Berlin | [berlin_planning](../berlin_planning/SEARCH_METHOD.md) |
| Europe | Copenhagen | [copenhagen](../copenhagen/SEARCH_METHOD.md) |
| Europe | Düsseldorf | [dusseldorf](../dusseldorf/SEARCH_METHOD.md) |
| Europe | London | [london](../london/SEARCH_METHOD.md) |
| Europe | Munich | [munich](../munich/SEARCH_METHOD.md) |
| Europe | Paris | [paris](../paris/SEARCH_METHOD.md) |
| Europe | Stockholm | [stockholm](../stockholm/SEARCH_METHOD.md) |
| Europe | Sofia (no chapter yet) | [sofia](../sofia/SEARCH_METHOD.md) |
| Europe | Vilnius | [baltics](../baltics/SEARCH_METHOD.md) |
| North America | Atlanta | [atlanta](../atlanta/SEARCH_METHOD.md) |
| North America | Boston | [boston](../boston/SEARCH_METHOD.md) |
| North America | Montreal | [montreal](../montreal/SEARCH_METHOD.md) |
| North America | New York | [new_york](../new_york/SEARCH_METHOD.md) |
| North America | Salt Lake City (no local event yet) | [salt_lake_city](../salt_lake_city/SEARCH_METHOD.md) |
| North America | San Francisco | [san_francisco](../san_francisco/SEARCH_METHOD.md) |
| North America | Seattle | [seattle](../seattle/SEARCH_METHOD.md) |
| North America | Toronto | [toronto](../toronto/SEARCH_METHOD.md) |
| Asia-Pacific | Kuala Lumpur | [kuala_lumpur](../kuala_lumpur/SEARCH_METHOD.md) |
| Asia-Pacific | Melbourne | [melbourne](../melbourne/SEARCH_METHOD.md) |
| Asia-Pacific | Seoul | [seoul](../seoul/SEARCH_METHOD.md) |
| Asia-Pacific | Singapore | [singapore](../singapore/SEARCH_METHOD.md) |
| Asia-Pacific | Sydney | [sydney](../sydney/SEARCH_METHOD.md) |
| Asia-Pacific | Taipei | [taipei](../taipei/SEARCH_METHOD.md) |
| Asia-Pacific | Tokyo | [tokyo](../tokyo/SEARCH_METHOD.md) |
| Europe | Athens (built from chapter history) | [athens](../athens/SEARCH_METHOD.md) |
| Europe | Barcelona (built from chapter history) | [barcelona](../barcelona/SEARCH_METHOD.md) |
| Europe | Bratislava (built from chapter history) | [bratislava](../bratislava/SEARCH_METHOD.md) |
| Europe | Budapest (built from chapter history) | [budapest](../budapest/SEARCH_METHOD.md) |
| Europe | Cluj (built from chapter history) | [cluj](../cluj/SEARCH_METHOD.md) |
| Europe | Dublin (built from chapter history) | [dublin](../dublin/SEARCH_METHOD.md) |
| Europe | Helsinki (built from chapter history) | [helsinki](../helsinki/SEARCH_METHOD.md) |
| Europe | Madrid (built from chapter history) | [madrid](../madrid/SEARCH_METHOD.md) |
| Europe | Marseille (built from chapter history) | [marseille](../marseille/SEARCH_METHOD.md) |
| Europe | Milan (built from chapter history) | [milan](../milan/SEARCH_METHOD.md) |
| Europe | Northern Germany (built from chapter history) | [northern_germany](../northern_germany/SEARCH_METHOD.md) |
| Europe | Oslo (built from chapter history) | [oslo](../oslo/SEARCH_METHOD.md) |
| Europe | Prague (built from chapter history) | [prague](../prague/SEARCH_METHOD.md) |
| Europe | Switzerland (built from chapter history) | [switzerland](../switzerland/SEARCH_METHOD.md) |
| Europe | Vienna (built from chapter history) | [vienna](../vienna/SEARCH_METHOD.md) |
| North America | Austin (built from chapter history) | [austin](../austin/SEARCH_METHOD.md) |
| North America | Boise (built from chapter history) | [boise](../boise/SEARCH_METHOD.md) |
| North America | Chicago (built from chapter history) | [chicago](../chicago/SEARCH_METHOD.md) |
| North America | Dallas (built from chapter history) | [dallas](../dallas/SEARCH_METHOD.md) |
| North America | Denver (built from chapter history) | [denver](../denver/SEARCH_METHOD.md) |
| North America | Detroit (built from chapter history) | [detroit](../detroit/SEARCH_METHOD.md) |
| North America | Halifax (built from chapter history) | [halifax](../halifax/SEARCH_METHOD.md) |
| North America | Houston (built from chapter history) | [houston](../houston/SEARCH_METHOD.md) |
| North America | Los Angeles (built from chapter history) | [los_angeles](../los_angeles/SEARCH_METHOD.md) |
| North America | Minneapolis (built from chapter history) | [minneapolis](../minneapolis/SEARCH_METHOD.md) |
| North America | Philadelphia (built from chapter history) | [philadelphia](../philadelphia/SEARCH_METHOD.md) |
| North America | Phoenix (built from chapter history) | [phoenix](../phoenix/SEARCH_METHOD.md) |
| North America | Portland (built from chapter history) | [portland](../portland/SEARCH_METHOD.md) |
| North America | Raleigh (built from chapter history) | [raleigh_durham](../raleigh_durham/SEARCH_METHOD.md) |
| North America | Vancouver (built from chapter history) | [vancouver](../vancouver/SEARCH_METHOD.md) |
| North America | Washington DC (built from chapter history) | [washington_dc](../washington_dc/SEARCH_METHOD.md) |
| Latin America | Bogotá (built from chapter history) | [bogota](../bogota/SEARCH_METHOD.md) |
| Latin America | Buenos Aires (built from chapter history) | [buenos_aires](../buenos_aires/SEARCH_METHOD.md) |
| Latin America | Floripa (built from chapter history) | [florianopolis](../florianopolis/SEARCH_METHOD.md) |
| Latin America | Medellín (built from chapter history) | [medellin](../medellin/SEARCH_METHOD.md) |
| Latin America | São Paulo (built from chapter history) | [sao_paulo](../sao_paulo/SEARCH_METHOD.md) |
| Asia-Pacific | Bangalore (built from chapter history) | [bangalore](../bangalore/SEARCH_METHOD.md) |
| Asia-Pacific | Brisbane (built from chapter history) | [brisbane](../brisbane/SEARCH_METHOD.md) |
| Asia-Pacific | China (built from chapter history) | [china](../china/SEARCH_METHOD.md) |
| Asia-Pacific | Ho Chi Minh City (built from chapter history) | [ho_chi_minh_city](../ho_chi_minh_city/SEARCH_METHOD.md) |
| Asia-Pacific | Manila (built from chapter history) | [manila](../manila/SEARCH_METHOD.md) |
| Asia-Pacific | Perth (built from chapter history) | [perth](../perth/SEARCH_METHOD.md) |
| Asia-Pacific | Wellington (built from chapter history) | [wellington](../wellington/SEARCH_METHOD.md) |
| Middle East & Africa | Abuja (built from chapter history) | [abuja](../abuja/SEARCH_METHOD.md) |
| Middle East & Africa | Dubai (built from chapter history) | [dubai](../dubai/SEARCH_METHOD.md) |
| Middle East & Africa | Lagos (built from chapter history) | [lagos](../lagos/SEARCH_METHOD.md) |
| Middle East & Africa | Riyadh (built from chapter history) | [riyadh](../riyadh/SEARCH_METHOD.md) |
| Middle East & Africa | Tel Aviv (built from chapter history) | [tel_aviv](../tel_aviv/SEARCH_METHOD.md) |
| Middle East & Africa | Uyo (built from chapter history) | [uyo](../uyo/SEARCH_METHOD.md) |

## 1. What the research is for

- **Goal:** find people in a chapter's region who could **speak at** or attend its next dbt Meetup. Also find the local companies that use dbt.
- **First-time speakers first:** the meetups want to give people who publish about dbt their first chance to present. The search looks hardest for them.
- **Evidence for every claim:** each person, talk, post and job ad carries a link and a confidence rating. An organiser can check it before outreach.
- **Professional information only:** name, title, employer, public talks and posts. No personal contact details.

## 2. What to look for

Work through these sources in order. Each city's notes say which local sources mattered most. Some cities start from job ads: first find who uses dbt, then look for people there. Others start from public content and add job ads as a second signal. Either way, the key record for a speaker is their `speaker_evidence`.

### Chapter history

- **Past speakers come for free:** the assembler adds everyone who has spoken at the chapter, from `enriched/<chapter>.json`. Don't research them unless you find new evidence about them.
- **Re-inviting is easy:** people who have already spoken are simple to bring back. New voices are usually the higher priority.

### Other local meetups and conferences

- **General data meetups:** read each event page for the line-up. Luma and meetup.com pages list every talk with the speaker's name, role and company. A meetup's newsletter usually names only events and hosts. It is still useful for collecting event URLs.
- **Every speaker becomes a person,** with the talk as `speaker_evidence`. Score them as in [§3](#3-scoring-rules).
- **Partner events** on another community's calendar are tagged in `speaker_evidence.event`, for example "(partner event on the <community> calendar)".
- **meetup.com past events:** query Meetup's `/gql2` endpoint (`groupByUrlname → events(status: PAST)`). It returns every past event with its full description. Search the event text for dbt, analytics, data engineer and data mesh rather than reading every event.
- **Conference agendas:** dbt Summit and Coalesce, Databricks Data + AI Summit, and the region's own data and Python conferences. The getdbt.com sitemap lists every dbt Summit speaker page. Agenda pages name the speaker and company and include an abstract, so they show who is speaking now.
- **Newsletters, YouTube and podcasts:** Substack and Medium newsletters, and data podcasts with local guests.

### Company and consultancy blogs

- **Start from a list** of prominent local companies, scale-ups, data vendors and consultancies.
- **For each company, scan:** its tech blog or Medium publication, dbt Labs case studies (`getdbt.com/case-studies/*`), cloud vendor case studies (Google Cloud, SELECT, Fivetran) and conference talks by its data people. Record each scanned blog in `other_evidence` with type `blog_scanned`.
- **Medium publications:** the publication page lists no posts when fetched. Use the feed instead, `medium.com/feed/<publication>`, which shows the last 8–10 posts. Its rate limit is in [§10](#10-what-we-learnt).
- **Record every post** with title, URL, date, authors, whether dbt is mentioned, a 1–2 sentence neutral summary and a suggested talk angle. Prefer posts from the last 2 years, and keep notable older dbt posts.
- **Author boxes** on company blogs were the best source of first-time speakers.

### Women-in-data communities

- **Purpose:** make sure women are well represented among speaker candidates. It works by looking in the right places, **not by labelling or guessing anyone's gender.**
- **Source people through the community's own events:** PyLadies, Women in Big Data, Women Techmakers, WiMLDS, R-Ladies, Women in Data, WiDS, She Loves Data, Women in AI, AWS women's user groups and women-in-data festivals. Note which ones have no active local chapter.
- **Recording:** every speaker, panellist and organiser with a data-related talk becomes a person. Their `sourced_via` includes `women_in_data_community`.
- **Organisers** get `priority_tier: connector`. They are the route to more speakers.
- **Tiering** follows the usual relevance rule in [§3](#3-scoring-rules).
- **Pronouns:** record them only when the person publishes them. Examples are "(she/her)" on a speaker listing, in a speaker bio or in a profile headline. Copy them exactly as written.
- **Never infer pronouns** from a name, a photo or third-person wording in someone else's article. Otherwise leave `pronouns` as `null`. The field records what people have said about themselves. It is not a way to measure balance.

### Job ads

- **Local job boards** with a dbt skill page are the cleanest company signal. They often list every open local role that mentions dbt on one page.
- **Each role** becomes a `job_postings` entry with `source`, `posted_date`, `last_seen`, `job_family` and `work_mode`.
- **New companies** from job ads are added as `employer`, `vendor` or `consultancy`, with `local_presence: confirmed`. Raise their `dbt_signal` to at least **medium**. Strong stays strong.
- **Never use the LinkedIn jobs API** or fetch LinkedIn pages.

### Public profiles

A person counts as reachable when an organiser can message them: a LinkedIn profile, or a Meetup, X or Bluesky profile in `profile_urls` (`reachable()` in [validate.py](validate.py)). Other profiles, such as GitHub, Zenn or Qiita, show the person's work and are kept, but don't count. `people_with_contact` and the cockpit's "people you can message" use this rule. Run the scripts first, since they cost no searches. Then search.

1. **Profiles the evidence already proves:** `python3 research/derive_profiles.py`. It adds author pages on Zenn, Qiita, note, velog, Medium and dev.to, Meetup and sessionize pages, and GitHub owners.
2. **Meetup members:** `python3 research/match_meetup_members.py`. It adds the Meetup profile of a speaker who hosted or RSVP'd to their own event. With `--city-pool`, it also matches people still without a contact against everyone who RSVP'd to any past event of the meetup groups the city file mentions, but only for a name that is unique there and rare on GitHub.
3. **Links on the person's own pages:** `python3 research/harvest_profiles.py fetch <cache>`, then `check <cache>`, then `apply <cache>`. It reads evidence pages, the speaker or author page each one links from the person's name, the speaker and host records inside Bevy and Luma pages, and the accounts a person lists on their own GitHub, Qiita or Zenn profile. It takes LinkedIn, X, Bluesky, sessionize and GitHub links. A link counts when it names the person, equals their recorded handle, sits on their own page, or is the closest profile link to their name with a slug that fits it. `check` lists every match and how often the rules agree with links already on file. Run it before `apply`.
4. **GitHub search:** `python3 research/find_github_profiles.py [<city folder> ...]`. It tries the recorded handle as a login, then a full-name search. It keeps a profile only when it names the employer, or the city with a data bio.
5. **Search:** brief the runs with [contact-task.md](contact-task.md) and apply with [`apply_contacts.py`](apply_contacts.py). Named leads go first, then everyone `not_searched`, then a wider pass and a talk-title pass on everyone `low`.
6. **Copy across cities:** a person in two city files can take the profile from their other record when the name and the employer or title match.

- **Search, don't fetch LinkedIn:** use only what the search result shows, logged out.
- **Accept a URL** only when the result ties the **name** to the **employer, talk or community**, and it is the only candidate. Never guess or build a URL.
- **`linkedin_confidence` high:** the name and the company or role both appear in the result title.
- **`linkedin_confidence` medium:** indirect evidence or a name variant.
- **`linkedin_confidence` low:** searched but not found. The URL is `null`.
- **`linkedin_confidence` not_searched:** nobody has searched yet.
- **Snippets often show location and job moves.** Record them in `city`, `based_in_region` and `notes`. The location rules are in [§6](#6-location-rules).

### Topics

- **1–3 topics per item,** most relevant first, taken only from `TOPIC_VOCABULARY` in `../pipeline/enrich.py`.
- **Same rules as** `../pipeline/past-meetups.md` Step 6. For example, don't use "case study" as a topic. Tag the real subject.
- **The validator rejects** any topic outside the vocabulary.
- **If nothing fits,** propose a new topic to Jeremy. Don't invent one.

### Splitting the work

- **Run sources in parallel:** for example, one run for the company-blog sweep, one for people, one per batch of blogs, one for LinkedIn URLs and one for other meetups' line-ups.
- **Read plain pages directly:** a server-rendered job-board page needs one fetch, not a separate run.
- **Return structured records** in [raw-format.md](raw-format.md), with topics from the vocabulary. One assembler run merges them and applies the shared schema.

## 3. Scoring rules

These rules are the same in every city file. They are also written out in `metadata.field_definitions`.

- **`lead_type`,** set by rule. It splits leads by whether they have presented before.
  - **proven_speaker:** has given a talk, panel or podcast, or has spoken at this chapter.
  - **emerging_voice:** has written and published something (blog post, article, newsletter, open-source project, LinkedIn post) but has no talk on record. **These are a priority:** the meetup wants to give them their first chance to present. The cockpit calls them first-time speakers.
  - **featured:** only quoted or profiled in someone else's content, such as a vendor case study, an interview or a team feature. Posts titled "Interview…", "A chat with…" or "Meet…" count as featured.
  - **no_public_content:** nothing found.
- **`priority_tier`:**
  - **1:** a strong recent lead. That is a proven speaker with a relevant recent talk, set by judgement. Or it is an emerging voice who has authored content from 2024 onwards and is not known to live outside the region, set by rule.
  - **2:** a good lead that needs verification, an emerging voice whose content is older or undated, or someone who gave a relevant talk at another meetup.
  - **3:** peripheral, off-topic or remote.
  - **organiser**, **backup** (our own Vinted team) and **connector** (a community organiser who can introduce people) are special roles.
- **First-time speakers outside the region:** a first-time speaker known to live outside the region is tier 2, not tier 1.
- **The rule only raises.** It raises an emerging voice's tier and never lowers anyone.
- **Past chapter speakers** added by the assembler are tier 1 if they spoke in 2025 or later. Otherwise they are tier 2.
- **Speakers from other meetups:** tier 2 when the talk is relevant to a dbt meetup. Relevant means analytics engineering, BI, modelling, governance, platforms or analytics agents. Tier 3 is for vendor pitches, pure ML or LLM talks, marketing-science talks and career-only content.
- **Outreach order:**
  1. Tier-1 emerging voices, to invite as first-time speakers.
  2. Tier-1 proven speakers, as the anchors of a line-up.
  3. Tier 2 of both types.
- **Balanced line-up:** pair one proven speaker with one or two emerging voices per event.
- **Cockpit order:** the organiser cockpit (`../dashboard/build_organiser_data.py`) follows the outreach order. It sorts by tier, then by `lead_type`, then by speaker potential. The `lead_type` order is emerging_voice, proven_speaker, featured, then no_public_content. Its Speakers view has a filter for first-time speakers.
- **Line-up balance check:** before confirming a line-up, the organisers review it together. They check gender balance, new vs. experienced speakers, scale-ups vs. enterprises, local vs. international speakers, and variety of topics. People who know the speakers make this judgement. It is not calculated from the data. If the draft is unbalanced, go back to the candidates with `sourced_via: women_in_data_community`. Ask the community connectors for introductions. The check is also in [event-planning-template.md](../berlin_planning/event-planning-template.md).
- **`meetup_fit`,** set by rule:
  - `speaker_potential` is **high** if the person has given a dbt talk, 2 or more talks, has spoken at this chapter, or is tier 1. It is **medium** with some public content, and **low** with none.
  - `attendee_potential` is **high** if the person is in the region with dbt content. It is **medium** if in the region or unknown, and **low** if based outside the region.
- **`level`** is **leadership** when the title contains Head, Director, VP, Chief, Founder, a C-level title, Manager or Lead. Otherwise it is **working**.
- **`dbt_signal`** has five values:
  - **strong:** a public post, case study or talk shows dbt, or an ad requires dbt.
  - **medium:** a job board tags dbt, an ad lists it among alternatives, or it appears only in a snippet.
  - **nice-to-have:** an ad lists dbt as a plus.
  - **weak:** not verified.
  - **none:** the company uses a different stack.
- **`watchlist`** is true if `local_presence` isn't confirmed, or `dbt_signal` is weak or none. Communities and independents are never on the watchlist.
- **`excluded_from_outreach`** is true only for internal records (Vinted). dbt Labs and Fivetran staff are labelled in the cockpit instead, and a checkbox hides them.
- **`past_meetups`** is copied from `enriched/<chapter>.json` by the assembler. Don't maintain it by hand.

## 4. Shared schema (version 3)

Every `<region>_dbt_companies.json` has exactly these keys, in this order. A value can be `null` when it's unknown, but a key is never missing.

```
metadata            title, generated_at, prepared_for, purpose, version, schema_version, region,
                    method[], field_definitions{}, caveats[], counts{}, topic_vocabulary_source,
                    topic_vocabulary[], topic_counts{}
companies[]         id, name, type, watchlist, excluded_from_outreach, cities[], local_presence,
                    dbt_signal, stack_signals[], job_postings[], other_evidence[], people[], notes
  job_postings[]    title, url, source, linkedin_company_name, dbt_mentioned_in_text, dbt_snippet,
                    job_poster, posted_date, last_seen, job_family, work_mode
  other_evidence[]  type, url, note
  people[]          id, name, pronouns, title, city, based_in_region, level, linkedin_urls[],
                    has_linkedin, linkedin_confidence, meetup_fit{speaker_potential, attendee_potential},
                    lead_type, sourced_via[], mentions_dbt, speaker_evidence[], attendee_signal, evidence[]{url, note},
                    confidence, internal_vinted, priority_tier, suggested_talk_angle,
                    past_chapter_talks[]{date, talk_title, topics}, notes
    speaker_evidence[]  type, event, title, date, url, content_id, co_authors[], mentions_dbt,
                        description, topics[], suggested_talk_angle, url_precision, confidence
sources             free-form object of source URLs (differs by region)
past_meetups[]      name, date, venue, url, organisers[], attendees, talks[]{speaker, company, title, topics}
community_channels[] name, url, note
```

- **Ids:** company and person `id`s are kebab-case ASCII names (e.g. `giovanni-corsetti-silva`). Keep them stable across runs.
- **`metadata.counts`** uses the same keys in every file (`standard_counts()` in [assemble.py](assemble.py)).
- **Definitions** for every value are in `metadata.field_definitions`. That object is identical in every file. The Berlin file holds the reference copy, and the assembler copies it from there.
- **Changing the schema:** a schema change goes into every regional file at once. Bump `schema_version`, update the key lists in [validate.py](validate.py) and [assemble.py](assemble.py), and update this section.

## 5. Building a city

| Step | What it does | Brief | Script |
|---|---|---|---|
| 1. Research | One run per city finds companies using dbt and people who could speak | [raw-format.md](raw-format.md) | — |
| 2. Assemble | Turns the loose research records into a valid file | — | [assemble.py](assemble.py) |
| 3. Location | Finds where each person is based, from public pages | [location-task.md](location-task.md) | [apply_locations.py](apply_locations.py) |
| 4. LinkedIn | Fills the remaining locations from LinkedIn search results | [linkedin-task.md](linkedin-task.md) | [apply_locations.py](apply_locations.py) |
| 5. Contacts | Finds a public profile for everyone, scripts first and then search | [contact-task.md](contact-task.md) | [apply_contacts.py](apply_contacts.py), [harvest_profiles.py](harvest_profiles.py) |

Then validate, fill the city notes and rebuild the cockpit:

```sh
python3 research/validate.py            # every city file; prints ok
python3 research/write_at_a_glance.py   # fills the generated blocks in every city's notes
dashboard/build_organiser.sh
```

- **City notes:** copy [city-method-template.md](city-method-template.md) to `<folder>/SEARCH_METHOD.md` and fill it in. Keep its two marker pairs. The script above fills them.
- **Older cities:** Berlin, Vilnius, Kuala Lumpur and Paris were built by hand before these scripts existed.

### Step 1: research

- **Give each run one city** and about 25 web searches. Point it at [raw-format.md](raw-format.md) and at [§2](#2-what-to-look-for).
- **Look for, in order:** first-time speakers (people who publish about dbt but have no talk on record), proven speakers, women-in-data communities sourced through their own events, and job ads that mention dbt.
- **Skip past chapter speakers.** The assembler adds everyone who has spoken at the chapter, from `enriched/<chapter>.json`.
- **Never fetch LinkedIn pages** or the LinkedIn jobs API. LinkedIn is used only through search results, in step 4.

### Step 2: assemble

```sh
python3 research/assemble.py <raw.json> <city>/<city>_dbt_companies.json                       # new city
python3 research/assemble.py <raw.json> <city>/<city>_dbt_companies.json --base <city>/<city>_dbt_companies.json   # add to a city
```

- **What it derives:** ids, `level`, `meetup_fit`, `watchlist`, counts, `past_meetups` and `past_chapter_talks`.
- **Extending a city:** it merges by id or name, and only re-scores the records the new research touched. Run it against the committed file, so a failed run can be undone with `git checkout`.
- **Non-Latin names** need an explicit ASCII `id` (a romanised name or a handle). The script stops and asks for one.
- **Lead type:** an existing first-time speaker who gains a talk becomes a proven speaker.

## 6. Location rules

Location decides the cockpit's "in region only" filter and the attendee ranking, so it needs evidence.

- **High:** the person's own profile states a city. That means a GitHub location, a speaker bio, an author box, a Meetup profile tied to the person, or a LinkedIn search result that shows their name, employer and location.
- **Medium:** an in-person talk or organiser role at a local event in the last 2 years, and the employer has a local office.
- **Outside the region:** needs the same standard, a stated city elsewhere.
- **Commuter towns count as local.** A town within about an hour of the chapter city is in the region. Examples are Potsdam for Berlin, Uppsala for Stockholm, Santa Cruz for San Francisco, Münster for Düsseldorf, Aarhus for Copenhagen, Taoyuan for Taipei, Olympia and Mount Vernon for Seattle, Providence for Boston, and Oxford and Brighton for London. A town in a different country does not count.
- **Otherwise unknown.** Never infer a location from a name, a hometown, a university or a company's head office alone.
- **Meetup member profiles** count only when the member is tied to the person: the RSVP or host of the event they spoke at. A name match alone is medium at best, and never supports "outside the region".

```sh
python3 research/apply_locations.py <city file> <patch.json>        # fills unknown locations only
python3 research/revert_locations.py <city file> <person id> ...    # sets people back to unknown
```

Each applied location adds a note and an evidence link to the person, so every call can be checked.

## 7. Updating a city

1. **Commit, then merge. Don't overwrite.** Commit the current file first. Git history keeps old versions, so don't save a `.v<N>.json` copy.
2. **Merge with the assembler:** `python3 research/assemble.py <raw.json> <city file> --base <city file>`. It matches people by `id`, or by first and last name with accents removed. It matches companies by `id` or normalised name.
3. **When a person is already in the file:** append new `speaker_evidence`. Update `title` or company only when the new evidence is newer and high confidence. Record job moves in `notes`.
4. **When a company is already in the file:** add new `job_postings`, and set `last_seen` on ads that are still listed. Keep expired ads. Add newly scanned blogs to `other_evidence` as `blog_scanned`. Match content by `content_id` or `url`, and job ads by `url`.
5. **New content** gets a stable `content_id`. Use `<company>-<short-slug>` for blog posts and talks, and `<community>-<date>-<slug>` for talks at another meetup. Tag it with 1–3 topics.
6. **Past meetups:** run `pipeline/run_pipeline.sh` first, so the latest chapter events are in `enriched/<chapter>.json`. The assembler then refreshes `past_meetups` and `past_chapter_talks` from that file.
7. **Past-speaker matching** is done by the assembler. It matches on the first and last name tokens, so a talk with several speakers ("Marielle Dado & Eva Schreyer") still matches each person. Check near misses against `pipeline/speaker-identities.json`.
8. **Re-scoring** of `meetup_fit`, `level` and `watchlist` by [§3](#3-scoring-rules) is done by the assembler, for the records the new research touched.
9. **Duplicates:** merge two records for the same person with `python3 research/merge_people.py <city file> <keep id> <drop id>`. The kept record gains the other's evidence, talks, links and notes.
10. **Validate** as in [§8](#8-validating).
11. **Update the metadata:** bump `version`, set `generated_at`, recalculate `counts` and `topic_counts`, and add a line to `method`.
12. **Refresh the city notes:** run `python3 research/write_at_a_glance.py` after any edit to a city file. Then add a line to the change log in the city's `SEARCH_METHOD.md`.

## 8. Validating

```sh
python3 research/validate.py                 # every city file
python3 research/validate.py <city file>     # one file
```

- **What it checks:** the exact shared keys and their order, unique person ids, and that every item has 1–3 topics from the vocabulary.
- **Across files:** `field_definitions`, the `counts` keys and `schema_version` must match the Berlin file.
- **It must print `ok`** before a city file is committed.

## 9. Replication prompt

Copy this into a new session with the `dbt-meetups` folder connected. Fill in the placeholders, and add the city's own sources from its notes.

````
You are updating my dataset of <City> companies that use dbt, and people who could speak at or
attend the <chapter name>. The dataset is <folder>/<city>_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read research/README.md (the central search
method) and <folder>/SEARCH_METHOD.md (the city notes) first, and follow them. The region is
<region>. I (Jeremy Chia) work at Vinted and co-organise dbt meetups; flag Vinted people as
internal_vinted.

Tasks, in priority order:

1. JOB ADS
   - Check the job sources in the city notes. Add every role that isn't in the file yet as a
     job_posting. Set last_seen on roles already in the file. Add new companies. Raise
     dbt_signal to at least "medium" for companies with a dbt role.

2. NEW CONTENT AND SPEAKERS since the last run (see metadata.generated_at)
   - Check these city-specific sources: <city-specific sources>.
   - Check new events at other local data meetups and read each event page for the line-up.
   - Re-scan every blog in other_evidence[type=blog_scanned] (use medium.com/feed/<publication>
     for Medium publications) and the dbt Labs case studies for local companies.
   - Check the latest dbt Summit/Coalesce agendas and the region's conferences for local
     speakers on dbt, analytics engineering, data modelling, testing, governance, semantic
     layers, orchestration or AI + analytics.
   - Check women-in-data communities through their own events.

3. PEOPLE
   - Find a public profile for everyone without one: run the scripts in central method
     section 2 (public profiles), then search with research/contact-task.md, one search at a time.
   - Fill unknown locations by the location rules (central method section 6).
   - Re-check people with notes like "verify" or "may have left".

4. CLASSIFY, ASSEMBLE AND SCORE
   - Tag each new speaker_evidence item with 1-3 topics, most relevant first, from
     TOPIC_VOCABULARY in pipeline/enrich.py only. If nothing fits, propose a new topic to me.
   - Write the new records in the format in research/raw-format.md and merge them with
     python3 research/assemble.py <raw.json> <folder>/<city>_dbt_companies.json --base <folder>/<city>_dbt_companies.json
     It refreshes past_meetups and past_chapter_talks from <enriched file> and re-scores.

You may split the work into 3-4 parallel runs (e.g. other meetups, blogs, conferences,
LinkedIn). Ask each to return records in the format in research/raw-format.md.

Rules:
- LinkedIn: never fetch linkedin.com pages or the jobs API. Only record linkedin.com/in URLs
  that appear word for word in a search result, or on a page tied to the person (event,
  speaker or author page, GitHub social accounts). Never guess.
- Collect only professional information: name, title, company, public talks and posts. No
  personal contact details.
- Every item needs a URL and a confidence rating. Set url_precision to overview_page when the
  link is a listing or homepage rather than the item itself.
- Commit the old file first (no .v<N>.json copy). Run python3 research/validate.py; it must
  print ok. Bump the version and recalculate counts.
- Run python3 research/write_at_a_glance.py. Update <folder>/SEARCH_METHOD.md (sources, key
  leads, next run) and add a change-log line: date, what was added, and any new lessons.

When finished, tell me briefly what's new: new speakers (with a link to their work), new
companies and dbt roles, people who have moved, and any topic trends.
````

## 10. What we learnt

### Sources that worked

- **Meetup's `gql2` endpoint** answers a plain `curl` POST. It returns past events with full descriptions, whether each event was in person, the venue, and the hosts and RSVPs with their profile city. `groupSearch` with a latitude and longitude lists a city's data groups in one call.
- **LinkedIn search results** show a person's location next to their name and employer. No other source does this as reliably. They also confirm a profile URL and current role without logging in.
- **GitHub profiles** have a location field. The unauthenticated API allows about 60 calls an hour, shared by every parallel run. The HTML profile page still shows the location after that.
- **Sessionize speaker pages** often state a city.
- **`find_local_speakers.py` gathers the three sources below in one run:** `python3 research/find_local_speakers.py <city folder> <out.json> --lat <lat> --lon <lon> --places "<town>,<town>"`. It lists each local data group's speakers and hosts, each Bevy chapter's speaker records, and GitHub data people in the listed towns, and marks who is already on file. It writes no city file: look the new people up, then merge them with `assemble.py`. A country in `--places` widens the GitHub search, but a country alone is no evidence of living in a metro region.
- **`add_local_people.py` turns the finder's candidates into people without lookups:** `python3 research/add_local_people.py <candidates.json> <city folder> "<town>,<town>" <raw.json>`, then merge with `assemble.py --base`. Speakers keep an unverified location, organisers become connectors, and GitHub people are ranked by how close their bio is to analytics engineering and capped at 100 per city. It splits a free-text speaker field into people, titles and self-stated pronouns.
- **Meetup's `speakerDetails` field** names the speaker, often with a LinkedIn link, even when the event text names nobody. Query `event(id){speakerDetails{name socialNetworks{url}}}` through `gql2` for every past event of a local data group.
- **Bevy's past-event API** (`<host>/api/event_slim/for_chapter/<id>/?status=Completed`, the chapter id is in the group page) lists every past event of a Snowflake, Tableau or Google Developer Group chapter. Each event page holds speaker and host records with title and employer.
- **GitHub user search by location** (`dbt location:Utah`, `"analytics engineer" location:"Salt Lake City"`) finds local practitioners with a stated city when web search returns only global results. Drop accounts whose bio reads "Data engineer by day, homelab tinkerer by night": they are generated.
- **Bevy and Luma event pages** (Snowflake, Tableau and Google Developer Group user groups, and Luma events) store each speaker's or host's LinkedIn and X username in the page data, even when the page shows no link.
- **Event and speaker pages link profiles next to each name.** Meetup descriptions, Tableau and Snowflake user-group pages, and sessionize pages carry LinkedIn and X links that a name search misses, such as `konradmal` for Konrad Maliszewski.
- **Company blogs with author boxes** were the best source of first-time speakers. Examples are adesso and ORAYLIS (Rhein-Ruhr), Xebia (Amsterdam), dataroots (Belgium), b.telligent and synvert (Munich), Brooklyn Data (New York) and The Information Lab (London).
- **dbt Labs case studies** name the data lead and give concrete numbers.
- **Conference agenda pages** (dbt Summit, Data + AI Summit) name the speaker and company and include an abstract.
- **Local job boards with a dbt skill page** give every open role with company, title, date, job family and work mode. They need no LinkedIn scraping.
- **Zenn and Qiita APIs** (Tokyo) and **velog** (Seoul) list dbt authors with their employers. A Zenn or Qiita user's own profile data also lists the X or LinkedIn account they chose to show, which is how most Tokyo authors can be messaged.
- **The getdbt.com sitemap** lists every dbt Summit speaker page.

### Sources that didn't

- **Medium feeds** return HTTP 429 after a few calls, from both curl and WebFetch.
- **JavaScript-rendered pages** return nothing to a fetch. These include the Coalesce on-demand listing, the DataEngBytes speakers page, connpass, the dbt Champions directory and most Japanese company sites.
- **Substack:** plain fetches return empty pages. Read issues through the browser or Substack's JSON API.
- **meetup.com past-events lists:** a plain fetch returns nothing useful. Use `gql2`, or read the `__NEXT_DATA__` block on each event page.
- **LinkedIn post text** is not readable when logged out.
- **iThome and Medium article pages** answer 403 or 429 to fetches, so their author links are out of reach. Taipei handles stay hard to match.
- **dbt Slack local channels** can't be searched from outside Slack.
- **Old talks:** most chapter talks before late 2024 give no location evidence.

### Limits and traps

- **Web search limits bursts, not totals.** Thirteen runs searching in parallel were all stopped within their first 10 searches. Four runs making one search at a time, and retrying on `too_many_requests`, finished more than 900 searches in one session. Tell every LinkedIn run to search one person at a time.
- **The tier-1 rule is generous.** Any first-time speaker with a post from 2024 onwards is raised to tier 1. That includes vendor bloggers and authors whose post doesn't mention dbt. Check them before outreach.
- **One consultancy can dominate a city.** Examples are Xebia in Amsterdam, Brooklyn Data in New York, The Information Lab in London and adesso in Rhein-Ruhr. Plan for one speaker per company per event.
- **General data meetups rarely mention dbt.** Treat their speakers as a pool of local data practitioners, not dbt speakers. Filter by tier and topics.
- **Job-board tags come from automatic extraction.** Open the ad before calling dbt core for that company. Some roles on a local board are remote or based elsewhere.
- **Platforms disagree on dates.** Luma and meetup.com can differ for the same event. Trust the event page.
- **Past speakers' employers** come from the Meetup talk text. A talk with several speakers can produce a company record named after a job title. Check `companies` for those after assembling.
- **People who share a link:** `python3 research/merge_shared_links.py` resolves what `validate.py` rejects. It merges two records when every part of the shorter name is in the longer one ("Rasmus Nes" and "Rasmus Nikolai Nes"), and otherwise removes the link from the second record, since an event page can give a speaker a co-speaker's link. A shared first and last name is not enough: Maria Alejandra Franco and Maria Isabel Arcila Franco are two people.
- **Duplicate people:** the same person can appear under two spellings or two employers. Search each city for near-duplicate names before outreach. Merge them with `merge_people.py`.
- **Company publications look like author pages.** A Zenn, note or dev.to company publication puts its articles under the company's name, so `zenn.dev/pixiv/articles/...` reads like a personal page. A Medium post can be someone else writing about the talk. `derive_profiles.py` asks Zenn's article API for each article's real author, skips other pages that name the employer or that several people share, and `validate.py` fails when two people in one file share a profile link.
- **The same person can sit in two city files.** Copy a profile across when the name and employer or title match.
- **Same-name people** are common. Always check a match against the company or role.
- **Search runs pick one of two profiles** when told to find a match. Ask them to flag every unsure match by id, and check each one before applying. About one flagged match in three had nothing tying it to the record.
- **Second and third search rounds find less.** The first LinkedIn search found about 40% of people. The wider pass on those it missed found about 20%, and a pass on the talk title after that found about 12%.
- **Slides and podcast pages carry profile links.** Speaker Deck pages, podcast show notes and conference schedules often list the speaker's X, Zenn or LinkedIn next to the talk.
- **Name variants need normalising** when matching, for example a nickname in quotes. Match on the first and last token after removing accents.
- **Stale roles:** titles and employers go out of date. Check the latest search snippet before outreach.
- **Speakers at local events can live elsewhere.** A talk in the city does not show where someone lives. The location rules are in [§6](#6-location-rules).
- **Links to general pages:** some items only have a blog homepage or a listing page as their URL (`url_precision: overview_page`). Replace them with direct links when found.
- **Posts with several authors** are repeated under each author with the same `content_id`. Remove duplicates by `content_id` when counting.
- **Vinted people** are flagged `internal_vinted: true`. They are backup speakers rather than outreach targets.
