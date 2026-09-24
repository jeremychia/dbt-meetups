# Paris dbt search: method, lessons and replication prompt

This file goes with `paris_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and gives a prompt for re-running and extending the search.

- **First built:** 2026-09-24
- **Dataset version:** 1 (shared schema version 3)
- **Goal:** find people in Paris / Île-de-France who post or speak about dbt and data topics, and who could **speak at** (or attend) the Paris dbt Meetup. Also find the Paris companies that use dbt.
- **Sister datasets:** `../berlin_planning/berlin_dbt_companies.json`, `../baltics/lithuania_dbt_companies.json` and `../kuala_lumpur/kuala_lumpur_dbt_companies.json`.
  - All four follow the shared schema in `../berlin_planning/SEARCH_METHOD.md` §3, and the validator there (Appendix A) checks all of them.
  - The shared scoring rules (`lead_type`, `priority_tier`, `meetup_fit`, `watchlist`, the pronoun rule, the line-up balance check) are in that file's §1 Steps 4 and 6. They apply here unchanged unless noted below.

Paris combines the Berlin and Lithuania approaches:

- **Public content, as in Berlin.** Blogs, podcasts, conferences and other meetups' line-ups.
- **Job ads, as in Lithuania.** A logged-out LinkedIn Jobs scan, checking each ad's full text.
- **Our own chapter history.** Every past Paris dbt Meetup speaker is included.

Much of the content is in French. French posts and talks are recorded as they are, with an English description.

---

## 1. How the search was done

Five sub-agents ran in parallel, following one output format: people, companies, jobs, sources checked and lessons. Each wrote a JSON file. One builder script then merged the files and applied the shared schema.

### Step 1: Large Paris companies (blogs, case studies, talks)

- **Companies scanned (2026-09):** Doctolib, BlaBlaCar, Qonto, Back Market, ManoMano, Alan, Swile, Deezer, Criteo, Contentsquare, leboncoin, Mirakl, Vestiaire Collective, PayFit, Pennylane, Ledger, Spendesk, Malt, Lydia/Sumeria, Aircall, Getaround, Brigad, Stuart, Lalilo, Brevo, Decathlon Digital, Carrefour, L'Oréal, LVMH/Sephora, TotalEnergies, SNCF Connect, Galeries Lafayette, Macif, Ornikar, Accor and others.
- **What was checked for each:** its tech blog, or its Medium feed (`medium.com/feed/<publication>`, or `/tagged/dbt`), dbt Labs and cloud-vendor case studies, and conference talks.

### Step 2: dbt partners, vendors and French data media

- **Consultancies:**
  - Ippon Technologies (the best source: 12 dbt posts with named authors)
  - Modeo, Artefact, Theodo, OCTO, Converteo, Devoteam, Infinite Lambda Paris, Zenika, Ekimetrics
- **Vendors:** nao Labs, Kestra, Sifflet, CastorDoc, DataGalaxy, Dataiku, Altertable and others.
- **dbt Labs' Paris-related staff:** they are excluded from outreach, as in Berlin.
- **French data media:**
  - The **DataGen** newsletter and podcast by Robin Conquet (`datageneration.substack.com`). This was the richest single source of named Paris dbt and analytics engineering practitioners: Doctolib, Qonto, Back Market, Ornikar, Decathlon, Swile, Modeo and more.
  - **blef.fr Data News**, by Christophe Blefari.

### Step 3: Other Paris meetups and conferences

- **Forward Data Conference** (`forward-data-conference.com`, 2024–2026). Its static speaker pages give each speaker's role and a full abstract, about 120 speakers across three editions. It was the best source of talk-level leads.
- **Meetups:** Paris Apache Airflow meetup, DuckDB Paris, ClickHouse Paris (hosted by Qonto) and Paris Data Ladies.
- **Low yield:** Modern Data Stack France, Snowflake and Databricks user groups (mostly vendor-led or online) and PyData Paris (scientific Python). The Paris Data Engineers group no longer exists.

### Step 4: Job ads

1. **LinkedIn Jobs, logged out:** search `keywords=dbt&location=Paris, Île-de-France`. From the browser page:
   - list the ads with in-page `fetch()` on `/jobs-guest/jobs/api/seeMoreJobPostings/search?...&start=N`;
   - fetch each ad from `/jobs-guest/jobs/api/jobPosting/<id>`;
   - keep the ads whose text contains the whole word `dbt`.

   The script is in `../baltics/SEARCH_METHOD.md`, Appendix A. On 2026-09-24, 300 ads were listed and 250 checked; 120 mentioned dbt. The run stopped at a 250-ad cap, so 50 were left unchecked.
2. **ATS search:** `site:jobs.lever.co`, `site:job-boards.greenhouse.io` and `site:jobs.ashbyhq.com` with dbt Paris. These added 27 ads from in-house tech companies that LinkedIn's ranking missed (Mistral AI, Pigment, BeReal, Aircall). Their `dbt_snippet` is the search engine's summary, marked "[search summary]".
3. **Welcome to the Jungle** now sends search URLs to a login page. Use `site:welcometothejungle.com` searches instead.
4. **Consultancies dominate** Paris dbt hiring: SKIILS, Devoteam, JAKALA, Talan, CGI, Capgemini and others. For speaker sourcing, filter `type == "employer"`.
   - Employers with several dbt ads: Dashlane, Accor, Leetchi, Joko, Implicity, Leonar and Axway.
   - Employers with one ad include Alan, Shine, Skello, Alma, pass Culture, Aircall and BeReal.

### Step 5: Women-in-data communities

This step follows the Berlin rule: find women by looking in women-focused groups, and never label or guess anyone's gender.

- **Paris Data Ladies** (`meetup.com/paris-data-ladies`) was the only strong source: 22 events since 2023, each with 3–4 data speakers.
  - Its meetup.com group data also lists organisers and event hosts, who are recorded as `connector`.
- **Weak or empty sources:**
  - Paris WiMLDS is almost all ML.
  - PyLadies Paris (`pyladiesparis`) and R-Ladies Paris are mostly Python, ML and R content; only their organisers were kept.
  - Women in Big Data Paris had no named data speakers.
  - WiDS Paris has had no events since 2023.
  - Duchess France, Women Techmakers and Ladies of Code Paris had nothing data-related.
- **Not scanned yet:** Social Builder, Femmes@numérique, Girls in Tech, Women in AI France, Data For Good and Les Pionnières.
- **Note on the sub-agent's picks:** it also picked some Forward Data Conference speakers using wording in their conference bios. Those people are tagged `sourced_via: conference_or_meetup_agenda`, not `women_in_data_community`, and the dataset records no gender for anyone. Next time, tell the sub-agent to take speakers only from the community's own events.

### Step 6: Chapter history

- Every named speaker in `../enriched/paris-dbt-meetup.json` (10 events, Sept 2022 to Sept 2025) was added as a person, with their talk as `speaker_evidence`.
- They are tier 2 unless other evidence puts them in tier 1, and `sourced_via` includes `chapter_meetup_history`.
- Speakers listed by first name only (e.g. "Nolwenn, Taha") were skipped.
- As of 2026-09-24 the chapter had no events after Paris dbt meetup #8 (2025-09-30).

### Step 7: Merge, score and LinkedIn

- **Merging:** people were matched on first and last name with accents removed, and companies on normalised name with a small alias map (e.g. Decathlon Digital → Decathlon, Ippon → Ippon Technologies). Records with a first name only or a placeholder name were dropped.
- **Tier 1 is stricter than in Berlin.** The sub-agents proposed 52 tier-1 people, so tier 1 was kept only for:
  - people in Paris (or not known to be elsewhere) with an item from 2024 onwards that mentions dbt; and
  - emerging voices, under the shared rule.

  Everyone else in the proposed tier 1 moved to tier 2. The result is 37 tier-1 people.
- **LinkedIn:** only 14 of the 105 tier-1/2 people without a profile were searched, because the session hit its web-search limit (200). The rest are `not_searched`. Finish this first on the next run.
- **Pronouns:** none were found that people had stated themselves, so all are `null`.

---

## 2. What we learnt

- **DataGen and Forward Data Conference are Paris's Data Berlin.** Between them they name most of the Paris practitioners who speak publicly about dbt.
- **Ippon's French blog** is full of hands-on dbt posts by consultants: TDD with unit tests, testing macros, GitHub Actions deploys, and Kimball + Data Vault with dbt. Their authors are good emerging voices, but many are not confirmed as being in Paris.
- **The web-search limit (about 200 per session) is the main constraint.** Five research agents used almost all of it. Next time, run the LinkedIn pass in a separate session, or give each agent a search budget.
- **Browser tabs clash when agents run in parallel.** Each agent should open its own tab (`tabs_create`) rather than using the default one.
- **meetup.com:** when browser access isn't granted, fetching group home pages and event pages directly still works. The `/gql2` past-events query needs the browser.
- **Watch out for:**
  - Anouar Hnini is probably in Ireland and may have left dbt Labs.
  - Jason Vazelle (Doctolib) may have moved abroad.
  - leboncoin uses the Coalesce transformation tool, not dbt.
  - Benjamin Joyen and Benjamin Joyen-Conseil (Decathlon) may be one person.
  - William Horel / Horrel: the spelling varies.

### Key findings (2026-09)

- **Strong dbt speaker leads (tier 1):**
  - Tushar Bhasin and Antoine Lefebvre (BlaBlaCar): dbt Core on Airflow at 4,000 tables
  - Thierry Sallé (Malt): migrating to dbt on BigQuery, having rejected SQLMesh
  - Ismail Mezzour (Accor): dbt, Airflow and Cosmos for 80+ engineers
  - Charles André (Qonto): many domain-owned dbt repos, data contracts, an AI on-call agent
  - Romain Fays (Doctolib), Matthieu Colin (Back Market) and Bastien Caunègre (Ornikar): analytics engineering set-ups described on DataGen
  - Hugo Palmer and Benjamin Joyen-Conseil (Decathlon)
  - Emma Wagner (Gorgias): a context layer for analytics agents
  - The Infinite Lambda team behind the Macif migration from Informatica to dbt
- **Emerging voices (write, but no talk yet):**
  - Doctolib: Jason Nathaniel V, Alexandre Guitton
  - Ippon: Jeremy Nadal, Grégoire Naud, Nicolas Hong, Paul Colinmaire, Mathis Le Gall
  - Contentsquare: Corentin Flacher, Pierre Munhoz, Thales Loiola Ravelli
  - Qonto: Maxime Damery, Timothée Dehouck
  - Others: Sebastien de Larquier (Alan), Matthieu Willot (Modeo), Martin-Pierre Roset (Kestra)
- **Women-in-data community leads:**
  - Juliette Chabbal (Ippon): semantic layer
  - Lucille Fargeau (Doctolib)
  - Anaïs Ghelfi (Malt)
  - Sarah Richard and Yasmine Touzene (Aramis Group)
  - Sophie Ly (Decathlon)
  - Kateryna Kolodnytska (Nissan)
  - Organiser and connector: Charlotte Ledoux (Paris Data Ladies)
- **Most common topics:** `genai & llm`, data governance, team & org design and analytics engineering.

---

## 3. Schema

See `../berlin_planning/SEARCH_METHOD.md` §3, shared schema v3. Paris-specific values:

- `metadata.region` is "Paris (Paris dbt Meetup)".
- `sources.checked` lists every source the sub-agents checked, with a `yielded` flag.
- `past_meetups` is copied from `../enriched/paris-dbt-meetup.json`.
- Person `content_id`s have the form `<event-slug>-<title-slug>`.

## 4. How to update the dataset

Follow `../berlin_planning/SEARCH_METHOD.md` §4, using `paris_dbt_companies.v<N>.json` for backups and `../enriched/paris-dbt-meetup.json` for `past_meetups` and `past_chapter_talks`.

## 5. Replication prompt

````
You are updating my dataset of Paris companies that use dbt, and people who could speak at or
attend the Paris dbt Meetup. The dataset is paris_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups/paris. Read paris/SEARCH_METHOD.md first, then
../berlin_planning/SEARCH_METHOD.md for the shared scoring rules, schema (§3), merge rules (§4)
and validator (Appendix A). Keep the schema identical to the other regional files.

The session has about 200 web searches in total, so budget them:
~40 per research sub-agent, ~40 for LinkedIn.

Tasks, in priority order:
1. LINKEDIN: find LinkedIn URLs for tier 1-2 people with linkedin_confidence "not_searched"
   (site:linkedin.com/in "<name>" <company>). Only accept exact name + company/role matches.
2. NEW CONTENT since metadata.generated_at: new DataGen episodes/posts, the latest Forward Data
   Conference programme, new Paris dbt Meetup / Paris Data Ladies / Paris Airflow / DuckDB Paris
   events, and new posts on the blogs in sources.checked (Medium: use medium.com/feed/<publication>).
3. JOB ADS: re-run the LinkedIn Jobs guest scan (keywords=dbt, location Paris, Île-de-France),
   keep ads whose text contains the whole word "dbt"; set last_seen on ads seen again; plus
   Lever/Greenhouse/Ashby site: searches.
4. WOMEN-IN-DATA: new Paris Data Ladies events, and the groups not yet scanned
   (Social Builder, Femmes@numérique, Girls in Tech, Women in AI France, Data For Good). Take
   speakers only from the community's own events; never infer gender.
5. CLASSIFY AND SCORE: 1-3 topics per item from TOPIC_VOCABULARY; lead_type; priority_tier
   (tier 1 = Paris or unknown location + a dbt item from 2024 onwards, or an emerging voice per the
   shared rule); meetup_fit; watchlist; past_chapter_talks.

Rules: public professional information only; never guess LinkedIn URLs; record pronouns only when
self-stated. Back up the old file as paris_dbt_companies.v<N>.json, run the validator, bump the
version and add a change-log entry below.

When finished, tell me briefly what's new: new speakers (with a link to their work), new
companies and dbt roles, people who have moved, and topic trends.
````

---

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First search, with 5 parallel sub-agents covering large companies, partners/vendors/media, meetups and conferences, job ads, and women-in-data communities, plus chapter history. 238 companies (94 on the watchlist), 186 people, 147 dbt job ads at 109 companies, 207 unique content items. Split: 137 proven speakers, 26 emerging voices, 8 featured, 16 with no public content. Tiers: 37 tier 1, 86 tier 2, 54 tier 3, 9 connectors. 17 people had already spoken at the Paris dbt Meetup. The LinkedIn pass is incomplete because the web-search limit was reached; 38 people have LinkedIn URLs. |
