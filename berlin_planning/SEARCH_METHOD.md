# Berlin dbt search: method, lessons and replication prompt

This file goes with `berlin_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and gives a prompt for re-running and extending the search.

- **First built:** 2026-09-23
- **Dataset version:** 5 (shared schema version 3)
- **Goal:** find people in Berlin who post or speak about dbt and data topics, and who could **speak at** (or attend) the Berlin dbt Meetup. Also find the Berlin companies that use dbt.
- **Sister datasets:** `../baltics/lithuania_dbt_companies.json` and `../kuala_lumpur/kuala_lumpur_dbt_companies.json`. All three follow one shared schema (§3). They are named `<region>_dbt_companies.json`, and a validator checks that their keys are identical (Appendix A).

The Lithuania search started from **job ads**: first find which companies use dbt, then look for people there. The Berlin search starts from **public content** (blog posts, talks, case studies, podcasts and other meetups' line-ups) and adds job ads as a second signal. In both files the key record for a speaker is their `speaker_evidence`, and each item is tagged with meetup topics.

---

## 1. How the search was done

### Step 1: Company blogs and case studies

1. **Start from a list of prominent Berlin companies and data vendors.** The 2026-09 list:
   - **Scale-ups and corporates:** GetYourGuide, Delivery Hero, Zalando, HelloFresh, N26, Trade Republic, SumUp, Taxfix, Contentful, Babbel, Omio, Raisin, Personio, Kleinanzeigen, idealo, Auto1, Flink, Choco, Wolt, Blinkist, Urban Sports Club, Forto, Sennder, OneFootball, Ecosia, Enpal, TIER/Dott, Kaufland e-commerce, Billie, SoundCloud and others.
   - **Vendors and consultancies:** Y42, dltHub, Gemma Analytics, diconium, Kestra, Tasman, SYNQ, Xebia.
2. **For each company, scan:**
   - its tech blog or Medium publication (the URLs are in `other_evidence[type=blog_scanned]`);
   - dbt Labs case studies (`getdbt.com/case-studies/*`);
   - cloud vendor case studies (Google Cloud, SELECT, Fivetran);
   - conference talks by its data people.
3. **Record every post found** with title, URL, date, authors, whether dbt is mentioned, a 1–2 sentence neutral summary and a suggested talk angle. Prefer 2024–2026, and keep notable older dbt posts.

### Step 2: The Data Berlin community (added in v3)

Data Berlin is Berlin's largest general data meetup and job board, run by Francesco "mucio" Mucio. It has three useful sources:

1. **Meetup line-ups.**
   - Luma has line-ups since November 2025: `https://lu.ma/data-berlin`.
   - meetup.com has events from May 2023 onwards: `https://www.meetup.com/data-berlin/events/?type=past`.
   - Each event page lists every talk with the speaker's name, role and company.
   - The newsletter (`databerlin.substack.com/p/data-berlin-<N>`) only names events and hosts, never speakers. It is still useful for collecting event URLs.
   - Partner events on the Data Berlin Luma calendar (OSA Community, Metabase × dltHub) are tagged in `speaker_evidence.event` as "(partner event on the Data Berlin calendar)".
   - Every speaker became a person, with the talk as `speaker_evidence`.
     - `priority_tier` **2**: the talk is relevant to a dbt meetup (analytics engineering, BI, modelling, governance, platforms, analytics agents).
     - `priority_tier` **3**: vendor pitches, pure ML/LLM or marketing-science talks.
2. **Job board, dbt skill page:** `https://databerlin.net/skills/dbt`.
   - The board pulls ads directly from company ATS platforms and tags skills automatically from the ad text.
   - The skill page lists every open Berlin role mentioning dbt. On 2026-09-23 that was 89 roles at 70 companies.
   - Each role became a `job_postings` entry with source "Data Berlin job board", `posted_date`, `last_seen`, `job_family` and `work_mode`.
   - Companies not already in the file were added as `employer`, `vendor` or `consultancy`, with `local_presence: confirmed`.
   - `dbt_signal` was raised to at least **medium**. Strong stays strong.
3. **Community channels.** The newsletter, Luma, meetup.com, YouTube and the job board are listed in `community_channels`, and their URLs in `sources.data_berlin`.

### Step 2b: Women-in-data communities (added in v5)

This step makes sure women are well represented among speaker candidates. It works by looking in the right places, **not by labelling or guessing anyone's gender.**

1. **Communities checked (2026-09):**
   - PyLadies Berlin (`meetup.com/pyladies-berlin`). This was the best source: its themed data talk nights (e.g. 12 Nov 2024) had dbt and dlt talks, and its listings show speakers' own pronouns.
   - Women in Big Data Berlin (`meetup.com/women-in-big-data-berlin-meetup-group`)
   - Women Techmakers Berlin (`meetup.com/wtm-berlin`)
   - The Women+ in Data/AI Festival (`women-in-data-ai.tech`, 2023–2024 editions, with a data engineering track)
   - AWS Women's User Group Berlin
   - WomenTech Network Berlin
   - Berlin WiMLDS
   - PyLadies at PyCon DE
2. **Checked but no active Berlin chapter or speaker lists for 2023–26:** R-Ladies Berlin (dormant since about 2019), Women in Data, WiDS, She Loves Data, Women in AI, Girls in Tech and Ladies of Code.
3. **Recording what you find:**
   - Every speaker, panellist and organiser with a data-related talk becomes a person. Their `sourced_via` includes `women_in_data_community`.
   - Organisers such as the PyLadies Berlin co-lead and the WiBD Berlin founder get `priority_tier: connector`. They are the route to more speakers.
   - Tiering follows the usual relevance rule: tier 2 for analytics, BI, data engineering, governance or data mesh talks, and tier 3 for pure ML/LLM or career-only content.
4. **Reading meetup.com past events:** open one meetup.com page in the browser, then query Meetup's `/gql2` endpoint from that page (`groupByUrlname → events(status: PAST)`). It returns every past event with its full description. Search the event text for dbt, analytics, data engineer and data mesh rather than reading every event.

### Step 3: People and their public work

- Every named author or speaker from Steps 1–2 becomes a person.
- Then search for Berlin people directly:
  - conference agendas: dbt Summit, Coalesce, Databricks Data + AI Summit, Berlin Buzzwords, PyCon DE & PyData, and the applydata Data Engineering MeetUp;
  - Substack and Medium newsletters (e.g. Jimmy Pang's Data Biz);
  - YouTube and podcasts (BARC, Modern Data Show).
- **Cross-reference with our own history.** Each person is matched by name against `../enriched/berlin-dbt-meetup.json` to fill `past_chapter_talks` (Appendix B). People who have already spoken are easy to re-invite, though new voices are usually the higher priority.
  - One example is Torsten Glunde, who spoke at Data Berlin in Feb 2026 and at the Berlin dbt Meetup in Apr 2026.

### Step 4: LinkedIn profiles

- For each person, search `"<name>" <company> site:linkedin.com/in`, logged out. Use only what the search results show.
- Accept a URL only when the result's title or snippet matches the **name** and the **company or role**. Never guess URLs.
- `linkedin_confidence` values:
  - **high:** name and company/role both appear in the result title.
  - **medium:** indirect evidence or a name variant.
  - **low:** searched but not found; the URL is `null`.
  - **not_searched:** in v3, only priority-tier-2 Data Berlin speakers were searched.
- Snippets often show location and job moves. Record them in `city`, `based_in_region` and `notes`.
- **`pronouns` (added in v5):** record pronouns only when the person publishes them, for example "(she/her)" on a PyLadies speaker listing, in a speaker bio or in a profile headline. Copy them exactly as written.
  - **Never infer pronouns** from a name, a photo or third-person wording in someone else's article.
  - Otherwise leave the field `null`. It will stay mostly `null`: a check of 80 tier-1/2 people in September 2026 found none in search results. The field records what people have said about themselves. It is not a way to measure balance.

### Step 5: Topic classification

- Each item in `speaker_evidence` gets **1–3 topics, most relevant first**, taken only from `TOPIC_VOCABULARY` in `../pipeline/enrich.py`.
- These are the same rules as `../pipeline/past-meetups.md` Step 6. For example, don't use "case study" as a topic; tag the real subject.
- The validator rejects any topic outside the vocabulary (Appendix A).
- If a new item doesn't fit the vocabulary, propose a new topic to Jeremy. Don't invent one.

### Step 6: Scoring and shaping

These rules are the same in both regional files. They are also written out in `metadata.field_definitions`.

- **`lead_type`**, set by rule (added in v4). It splits leads by whether they have presented before.
  - **proven_speaker:** has given a talk, panel or podcast, or has spoken at this chapter.
  - **emerging_voice:** has written and published something (blog post, article, newsletter, open-source project, LinkedIn post) but has no talk on record. **These are a priority:** the meetup wants to give them their first chance to present.
  - **featured:** only quoted or profiled in someone else's content, such as a vendor case study, an interview or a team feature. Posts titled "Interview…", "A chat with…" or "Meet…" count as featured.
  - **no_public_content:** nothing found.
- **`priority_tier`:**
  - **1:** a strong recent lead. That means either:
    - a proven speaker with a relevant recent talk (set by judgement), or
    - an **emerging_voice** who is in the region (or not known to be outside it) and has authored content from 2024 onwards (set by rule).
  - **2:** a good lead, one that needs verification, an emerging voice whose content is older or undated, or someone who gave a relevant talk at another meetup.
  - **3:** peripheral, off-topic or remote.
  - **organiser**, **backup** (our own Vinted team) and **connector** (e.g. Data Berlin) are special roles.
  - The rule only ever raises an emerging voice's tier. It never lowers anyone.
- **Outreach order:**
  1. Tier-1 emerging voices, to invite as first-time speakers.
  2. Tier-1 proven speakers, as the anchors of a line-up.
  3. Tier 2 of both types.

  Pairing one proven speaker with one or two emerging voices per event makes a balanced line-up.
- **Line-up balance check (added in v5):** before confirming a line-up, the organisers review it together for:
  - gender balance;
  - speakers who are new to the stage vs. experienced;
  - scale-ups vs. enterprises;
  - local vs. international speakers;
  - variety of topics (`topics`).

  This is a judgement made by people who know the speakers. It is not calculated from the dataset. If the draft line-up is unbalanced, go back to the candidates with `sourced_via: women_in_data_community`, and ask the community connectors for introductions. The check is also in `event-planning-template.md`.

  The organiser dashboard (`../dashboard/build_organiser_data.py`) follows this order. It sorts by tier, then by `lead_type` (emerging_voice, then proven_speaker, featured and no_public_content), then by speaker potential. Its Speakers view has a filter for first-time speakers.
- **`meetup_fit`**, set by rule:
  - `speaker_potential` is **high** if the person has given a dbt talk, 2 or more talks, has spoken at this chapter, or is tier 1. It is **medium** if they have some public content, and **low** if none was found.
  - `attendee_potential` is **high** if the person is in the region with dbt content, **medium** if in the region or unknown, and **low** if based outside the region.
- **`level`** is **leadership** when the title contains Head, Director, VP, Chief, Founder, C-level, Manager or Lead. Otherwise it is **working**.
- **`dbt_signal`** has five values:
  - **strong:** a public post, case study or talk shows dbt, or dbt is required in an ad.
  - **medium:** dbt is tagged by the job board, listed among alternatives, or seen only in a snippet.
  - **nice-to-have:** dbt is listed as a plus in an ad.
  - **weak:** not verified.
  - **none:** the company uses a different stack (e.g. Zalando uses Databricks Metric Views; idealo uses Spark and Glue).
- **`watchlist`** is true if `local_presence` isn't confirmed, or `dbt_signal` is weak or none.
- **`excluded_from_outreach`** is true only for dbt Labs, because their Berlin staff already give product updates.
- **`past_meetups`** is copied from `../enriched/berlin-dbt-meetup.json`. Don't maintain it by hand.

### Step 7: Parallel sub-agents

The run used parallel sub-agents for:

1. the first company-blog sweep;
2. the first people sweep;
3. blogs, batch A (large scale-ups);
4. blogs, batch B (vendors, consultancies and smaller scale-ups);
5. LinkedIn URLs, in 3 batches;
6. Data Berlin meetup line-ups.

The job-board page was read directly with one fetch, because it is plain server-rendered HTML. Each sub-agent returned structured records with topics from the vocabulary. The records were merged by one builder script, which then applied the shared schema (`conform()` in Appendix A).

---

## 2. What we learnt

### Sources that worked well

| Source | Why it's useful |
|---|---|
| `databerlin.net/skills/dbt` | Every open Berlin role mentioning dbt on one page, with company, title, date, job family and work mode. It's a clean company signal and needs no LinkedIn scraping. |
| Data Berlin event pages (Luma, meetup.com) | Full line-ups with each speaker's name, role and company. |
| getyourguide.careers/posts | The most active Berlin dbt writer: dbt on Databricks, Cosmos, AI-generated docs. |
| dbt Summit / Data + AI Summit agenda pages | They name the speaker and company and include an abstract. They show who is currently speaking. |
| dbt Labs case studies | They name the data lead and give concrete numbers (Enpal, TIER). |
| Medium RSS feeds (`medium.com/feed/<publication>`) | Medium publication pages don't list posts when fetched; the feed shows the last 8–10. |
| LinkedIn search snippets | Enough to confirm a profile URL, current role and often location, without logging in. |

### Sources that didn't work

| Source | Problem |
|---|---|
| Data Berlin newsletter, for speakers | It names events and hosts only. Plain fetches of Substack return empty pages; read issues through the browser or Substack's JSON API. |
| meetup.com past-events list (plain fetch) | Returns nothing useful. Open it in the browser, or read the `__NEXT_DATA__` block on each event page. |
| Data Berlin YouTube | The channel page and RSS feed returned no videos, so recordings aren't linked yet. |
| LinkedIn post text | Not readable when logged out. |
| dbt Slack #local-berlin, dbt Champions directory | Can't be searched from outside Slack, or the page loads with JavaScript. |
| Most Berlin scale-up blogs | Quiet since 2023: N26, SumUp, Babbel, Omio, Solaris, Auto1, SoundCloud, Urban Sports Club engineering. |

### Things to watch out for

- **Data Berlin talks rarely mention dbt.** None of the 78 talk descriptions did, and the programme is AI/agent-heavy since 2025. Treat it as a pool of Berlin data practitioners, not dbt speakers. Filter by `priority_tier` 2 and topics.
- **Job-board tags come from automatic extraction.** Open the ad before calling dbt "core" for that company. Some roles on the Berlin board are remote or based elsewhere (e.g. Fivetran's Costa Rica role, Grafana's Sweden and Spain roles).
- **Platforms disagree on dates.** Luma and meetup.com can differ (Oct 14 vs Oct 16, 2025). Trust the event page.
- **Same-name people.** There are several people called Steven Xu, and 2 Breno Costas at Delivery Hero. Always check against the company or role.
- **Name variants need normalising** when matching (e.g. "Francesco 'mucio' Mucio" vs "Francesco Mucio"). Match on first and last token after removing accents.
- **Stale roles.**
  - Max Rieger → 7NXT, and Nuno Capeta → Kariisma.
  - Alexander Novikov's headline no longer says Enpal.
  - Angelita Frozza Sanches is now Head of Core Data Platform at Scout24.
- **Speakers at Berlin events who live elsewhere.**
  - Silja Märdla: Tallinn
  - Aman Gupta: Mumbai
  - Faysal Rehmat: New York
  - Torsten Glunde: Hannover region
  - Emanuele Celoria: Turin
- **Links to general pages.** Some items only have a blog homepage or a meetup listing page as their URL (`url_precision: overview_page`). Replace them with direct links when found.
- **Posts with several authors** are repeated under each author with the same `content_id`. Remove duplicates by `content_id` when counting.
- **Vinted people** are flagged `internal_vinted: true`, and are backup speakers rather than outreach targets.

### Key findings (2026-09)

- **Strongest dbt speaker leads:**
  - Giovanni Corsetti Silva, and Danny Burleigh with Lennart Scharmann (GetYourGuide)
  - Waqas Shahid and Uttpesh Vyas (Delivery Hero)
  - Alexander Novikov (Enpal)
  - Andre Wagner (Taxfix)
- **New from Data Berlin, relevant to a dbt meetup:**
  - Michael Gabriel (Enpal): warehouse adoption from 50 to 650 users
  - Aleksandr Zolotukhin and Paula Urrialde (JustWatch): Lightdash, and AI in BI
  - Hamzah Chaudhary (Lightdash): semantic layer to AI analyst
  - Scout24's data platform team
  - Adedeji Rodemade (Adsquare): analytics engineering at scale
  - Christian Hiroz and Tadej Štajner (SumUp): a self-service platform and SumUp's data lake
  - Divya Bokaria (Zattoo): a self-service analytics culture
- **Emerging voices (written, no talk yet), tier 1:**
  - Danny Burleigh and Lennart Scharmann (GetYourGuide): the analytics harness for AI
  - David Förster and Max Rieger (idealo): data contracts
  - Nélson Rangel (OneFootball): dbt models for engineering release metrics
  - Hiba Jamal (dltHub): dlt with dbt's semantic layer
- **Emerging voices, tier 2 (older or undated posts):**
  - Fabian Bücheler and Shaurya Sood (GetYourGuide): Cosmos, and dbt on Databricks
  - Akash Ganguly (HelloFresh)
  - Dolf ter Hofsté (Taxfix)
  - Breno Costa and Steven Xu (Delivery Hero)
- **Companies hiring for dbt most (Data Berlin board):** Fivetran, Statista, Grafana Labs, Redcare Pharmacy, Europace, SumUp, Zendesk, N26 and Alpaca.
- **Most common topics:** dbt migration & adoption, orchestration & ci/cd, performance & scale and analytics engineering. With Data Berlin added, `genai & llm` is now the most frequent topic.

---

## 3. Shared schema (version 3)

`berlin_planning/berlin_dbt_companies.json`, `baltics/lithuania_dbt_companies.json` and `kuala_lumpur/kuala_lumpur_dbt_companies.json` have exactly these keys, in this order. A value can be `null` when it's unknown, but a key is never missing.

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
- **`metadata.counts`** uses the same keys in every file (`standard_counts()` in Appendix A).
- **Definitions** for every value are in `metadata.field_definitions`. That object is identical in every file.
- **Changing the schema:** a schema change goes into every regional file at once. Bump `schema_version`, update the key lists in Appendix A, and update the schema section in every SEARCH_METHOD.md.

---

## 4. How to update the dataset

1. **Commit, then merge. Don't overwrite.**
   - Commit the current file first. Git history keeps old versions, so don't save a `.v<N>.json` copy.
   - Match people by `id`, or by first and last name with accents removed.
   - Match companies by `id` or normalised name, content by `content_id` or `url`, and job ads by `url`.
2. **When a person is already in the file:**
   - Append new `speaker_evidence`.
   - Update `title` or company only when the new evidence is newer and high confidence.
   - Record job moves in `notes`.
3. **When a company is already in the file:**
   - Add new `job_postings`, and set `last_seen` on ads that are still listed.
   - Keep expired ads.
   - Add newly scanned blogs to `other_evidence` as `blog_scanned`.
4. **New content** gets a stable `content_id`:
   - `<company>-<short-slug>` for blog posts and talks;
   - `databerlin-<date>-<slug>` for Data Berlin talks.
   - Tag it with 1–3 topics.
5. **Refresh `past_meetups` and `past_chapter_talks`** from `../enriched/berlin-dbt-meetup.json`. Run `../pipeline/run_pipeline.sh` first so the latest events are included.
6. **Re-score** `meetup_fit`, `level` and `watchlist` using §1 Step 6.
7. **Validate** with Appendix A. It checks the topics, the exact shared keys, and that the Lithuania file still matches.
8. **Update the metadata:** bump `version`, set `generated_at`, recalculate `counts` and `topic_counts`, and add a line to `method`.
9. **Log the run** in the change log below.

---

## 5. Replication prompt

Copy this into a new Cowork session, with the `dbt-meetups` folder connected:

````
You are updating my dataset of Berlin companies that use dbt, and people who could speak at or
attend the Berlin dbt Meetup. The dataset is berlin_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups/berlin_planning. Read SEARCH_METHOD.md in the same
folder first and follow its method, lessons, merge rules and shared schema (§3). The schema must
stay identical to ../baltics/lithuania_dbt_companies.json. I (Jeremy Chia) work at Vinted and
co-organise the meetup; flag Vinted people as internal_vinted.

Tasks, in priority order:

1. JOB ADS
   - Fetch https://databerlin.net/skills/dbt and add every role that isn't in the file yet as a
     job_posting (source "Data Berlin job board"). Set last_seen on roles already in the file.
     Add new companies. Raise dbt_signal to at least "medium" for companies with a role there.

2. NEW CONTENT AND SPEAKERS since the last run (see metadata.generated_at)
   - Data Berlin: check new events on https://lu.ma/data-berlin and
     https://www.meetup.com/data-berlin/events/?type=past. Read each event page for the line-up.
     Add each talk as speaker_evidence (tier 2 if relevant to a dbt meetup, 3 otherwise).
   - Re-scan every blog in sources.company_blogs_scanned (use medium.com/feed/<publication> for
     Medium publications) and the dbt Labs case studies for Berlin companies.
   - Check the latest dbt Summit/Coalesce, Databricks Data + AI Summit, Berlin Buzzwords,
     PyCon DE & PyData and applydata meetup line-ups for Berlin-based speakers on dbt, analytics
     engineering, data modelling, testing, governance, semantic layers, orchestration or
     AI + analytics.

3. PEOPLE
   - Find LinkedIn URLs (site:linkedin.com/in "<name>" <company>) for people with priority_tier
     1-2 where linkedin_confidence is "not_searched" or "low". Re-check "medium" ones.
   - Re-check people with notes like "verify" or "may have left".

4. CLASSIFY AND SCORE
   - Tag each new speaker_evidence item with 1-3 topics, most relevant first, from TOPIC_VOCABULARY
     in ../pipeline/enrich.py only. If nothing fits, propose a new topic to me instead of inventing one.
   - Refresh past_meetups and past_chapter_talks from ../enriched/berlin-dbt-meetup.json.
   - Re-score meetup_fit, level and watchlist using SEARCH_METHOD.md §1 Step 6.

You may run up to 3-4 sub-agents in parallel (e.g. Data Berlin events, blogs, conferences,
LinkedIn). Ask each to return JSON records with the fields from SEARCH_METHOD.md §3.

Rules:
- Only record linkedin.com/in URLs that appear word for word in search results. Never guess.
- Collect only professional information: name, title, company, public talks and posts. No
  personal contact details.
- Every item needs a URL and a confidence rating. Set url_precision to overview_page when the
  link is a listing or homepage rather than the item itself.
- Commit the old file first (no .v<N>.json copy), merge following §4, run the Appendix A
  validator, recalculate counts and bump the version.
- Add a change-log entry to SEARCH_METHOD.md: date, what was added, and any new lessons.

When finished, tell me briefly what's new: new speakers (with a link to their work), new companies
and dbt roles, people who have moved, and any topic trends.
````

---

## Appendix A: Shared-schema validator

Run it from the repo root. It checks every regional file.

```python
import json, sys
sys.path.insert(0, "pipeline")
from enrich import TOPIC_VOCABULARY as V

TOP = ["metadata","companies","sources","past_meetups","community_channels"]
META = ["title","generated_at","prepared_for","purpose","version","schema_version","region","method",
        "field_definitions","caveats","counts","topic_vocabulary_source","topic_vocabulary","topic_counts"]
COMPANY = ["id","name","type","watchlist","excluded_from_outreach","cities","local_presence","dbt_signal",
           "stack_signals","job_postings","other_evidence","people","notes"]
JOB = ["title","url","source","linkedin_company_name","dbt_mentioned_in_text","dbt_snippet","job_poster",
       "posted_date","last_seen","job_family","work_mode"]
PERSON = ["id","name","pronouns","title","city","based_in_region","level","linkedin_urls","has_linkedin",
          "linkedin_confidence","meetup_fit","lead_type","sourced_via","mentions_dbt","speaker_evidence","attendee_signal","evidence",
          "confidence","internal_vinted","priority_tier","suggested_talk_angle","past_chapter_talks","notes"]
EVID = ["type","event","title","date","url","content_id","co_authors","mentions_dbt","description","topics",
        "suggested_talk_angle","url_precision","confidence"]
PAST = ["name","date","venue","url","organisers","attendees","talks"]
PAST_TALK = ["speaker","company","title","topics"]

def keys(obj, expected, where):
    assert list(obj) == expected, (where, set(expected) ^ set(obj))

def check(path):
    d = json.load(open(path))
    keys(d, TOP, "top"); keys(d["metadata"], META, "metadata")
    assert d["metadata"]["topic_vocabulary"] == V, "vocabulary out of date"
    people_ids = set()
    for c in d["companies"]:
        keys(c, COMPANY, c["id"])
        for j in c["job_postings"]: keys(j, JOB, j["url"])
        for p in c["people"]:
            keys(p, PERSON, p["id"])
            assert p["id"] not in people_ids, ("duplicate person", p["id"]); people_ids.add(p["id"])
            for e in p["speaker_evidence"]:
                keys(e, EVID, (p["id"], e["title"]))
                assert 1 <= len(e["topics"]) <= 3 and all(t in V for t in e["topics"]), (p["id"], e["title"])
    for m in d["past_meetups"]:
        keys(m, PAST, m["name"])
        for t in m["talks"]:
            keys(t, PAST_TALK, t["title"])
            assert all(x in V for x in (t["topics"] or [])), t["title"]
    return d

files = ["berlin_planning/berlin_dbt_companies.json", "baltics/lithuania_dbt_companies.json",
         "kuala_lumpur/kuala_lumpur_dbt_companies.json"]
ds = [check(f) for f in files]
for d in ds[1:]:
    assert d["metadata"]["field_definitions"] == ds[0]["metadata"]["field_definitions"], "field_definitions differ"
    assert list(d["metadata"]["counts"]) == list(ds[0]["metadata"]["counts"]), "counts keys differ"
    assert d["metadata"]["schema_version"] == ds[0]["metadata"]["schema_version"]
print("ok")
```

`standard_counts()`, which fills `metadata.counts` the same way in both files:

```python
from collections import Counter
def standard_counts(ds):
    allp = [p for c in ds["companies"] for p in c["people"]]
    return {"companies": len(ds["companies"]), "people": len(allp),
      "job_postings": sum(len(c["job_postings"]) for c in ds["companies"]),
      "companies_with_job_postings": sum(1 for c in ds["companies"] if c["job_postings"]),
      "speaker_evidence_items": sum(len(p["speaker_evidence"]) for p in allp),
      "unique_content_items": len({e["content_id"] for p in allp for e in p["speaker_evidence"]}),
      "people_with_linkedin": sum(p["has_linkedin"] for p in allp),
      "people_who_spoke_at_this_chapter": sum(1 for p in allp if p["past_chapter_talks"]),
      "internal_vinted": sum(p["internal_vinted"] for p in allp),
      "level": dict(Counter(p["level"] for p in allp)),
      "speaker_potential": dict(Counter(p["meetup_fit"]["speaker_potential"] for p in allp)),
      "attendee_potential": dict(Counter(p["meetup_fit"]["attendee_potential"] for p in allp)),
      "priority_tier": dict(Counter(str(p["priority_tier"]) for p in allp)),
      "watchlist_companies": sum(1 for c in ds["companies"] if c["watchlist"]),
      "past_meetups": len(ds["past_meetups"]),
      "lead_type": dict(Counter(p["lead_type"] for p in allp)),   # added in schema v2
      "people_with_self_stated_pronouns": sum(1 for p in allp if p["pronouns"]),   # v3
      "sourced_via": dict(Counter(s for p in allp for s in p["sourced_via"]))}       # v3
```

## Appendix B: Past-speaker cross-reference

```python
import json, re, unicodedata

def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9 ]", "", s)

events = json.load(open("enriched/berlin-dbt-meetup.json"))["events"]

def past_chapter_talks(name):
    toks = norm(name).split()
    first, last = toks[0], toks[-1]
    hits = []
    for e in events:
        for t in e.get("talks", []):
            sn = norm(t.get("speaker_name")).split()
            if last in sn and first in sn:
                hits.append({"date": e["date"], "talk_title": t["title"], "topics": t["topics"]})
    return hits
```

Speaker names can hold several people, e.g. "Marielle Dado & Eva Schreyer", so match on tokens rather than the whole string. Check fuzzy near-misses against `../pipeline/speaker-identities.json`. For Lithuania, run the same function over its own `past_meetups`, using the `speaker` and `title` keys.

---

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-23 | 1 | First search: 43 companies, 49 people, 54 content items tagged with topics. LinkedIn URLs found for 41 people. Cross-referenced with 15 past Berlin meetups (9 people had already spoken). |
| 2026-09-23 | 2 | Restructured to the Lithuania layout (companies → people → speaker_evidence). Added `job_postings`, `watchlist`, `meetup_fit`, `level`, `past_meetups`, `sources` and `community_channels`. |
| 2026-09-23 | 3 | **Data Berlin added:** 79 talk records (72 unique talks) from 26 Data Berlin meetups and 3 partner events, May 2023 – Sep 2026, bringing in 75 new people. 25 of them are tier 2; 22 have LinkedIn profiles, found by searching those 25. Also 89 dbt roles at 70 companies from `databerlin.net/skills/dbt`. **Standardised with Lithuania:** file renamed from `berlin_speaker_candidates.json` to `berlin_dbt_companies.json`. Shared schema v1 with identical keys, `field_definitions` and `counts`. Renamed `berlin_presence` → `local_presence`, `berlin_based` → `based_in_region`, `past_berlin_meetup_talks` → `past_chapter_talks`. Totals: 144 companies, 124 people, 98 job postings. |
| 2026-09-23 | 4 | Shared schema v2 adds `lead_type` (proven_speaker / emerging_voice / featured / no_public_content). 8 emerging voices raised in priority: 4 to tier 1 (David Förster, Max Rieger, Nélson Rangel, Hiba Jamal) and 4 to tier 2 (Danny Burleigh and Lennart Scharmann were already tier 1). Split: 99 proven speakers, 16 emerging voices, 6 featured, 3 with no public content. |
| 2026-09-23 | 5 | Shared schema v3 adds `pronouns` (self-stated only, never inferred) and `sourced_via`. **Women-in-data sourcing (Step 2b):** 28 new people from PyLadies Berlin, Women in Big Data Berlin, Women Techmakers Berlin, the Women+ in Data/AI Festival, AWS Women's User Group, WomenTech Network and WiMLDS, plus new evidence for Katharine Jarmul. 3 people have self-stated pronouns. Added a line-up balance check to the outreach order and to `event-planning-template.md`. Totals: 156 companies, 152 people. Lithuania and Kuala Lumpur moved to schema v3 too (schema-only change). Backup: `berlin_dbt_companies.v4.json`. |
