# Copenhagen dbt search: method, lessons and replication prompt

This file goes with `copenhagen_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in Denmark who could **speak at** (or attend) the [Copenhagen dbt Meetup](https://www.meetup.com/copenhagen-dbt-meetup/), and the local companies that use dbt.
- **Region:** the Copenhagen metro area, including Ballerup and Hørsholm. Commuter towns are local for this chapter, so Aarhus counts too. The rest of Denmark counts as outside.

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 73 |
| People | 90 |
| Tier 1 leads | 21 |
| First-time speakers (publish, no talk yet) | 6 |
| Proven speakers | 71 |
| Spoke at this chapter before | 32 |
| Based in the region | 71 |
| Based elsewhere | 7 |
| Location unknown | 12 |
| With a LinkedIn profile | 8 |
| Job ads mentioning dbt | 11 |
| Past chapter meetups | 11 |
<!-- at-a-glance:end -->

## 1. How the search was done

Web search ran out after about 15 calls. Most of the search used page fetches, the Meetup data endpoint and the GitHub user search.

### Step 1: Other Danish meetups

- **Meetup's `gql2` endpoint:** queried with `curl`, it returned every past event for 14 Danish data groups. Its `eventSearch` query also found the chapter's next event, which is not yet in the chapter history.
- **[Copenhagen Data Engineering](https://www.meetup.com/copenhagen-data-engineering/):** 6 events from 2025-03 to 2026-05, with 17 speakers. Its event pages name every speaker with an employer. It was the best source of Danish speakers.
- **[Databricks User Group Denmark](https://www.meetup.com/databricks-user-group-denmark/):** the same detail, and one dbt talk (Vipps MobilePay, 2025-09).
- **[Snowflake User Group Denmark](https://usergroups.snowflake.com/denmark/):** its event pages list speakers and organisers.
- **[PyData Copenhagen](https://www.meetup.com/pydata-copenhagen/):** mostly machine learning and LLM talks.
- **No yield:** the [Fabric & Power BI User Group Denmark](https://www.meetup.com/denmark-powerbi-user-group/) has mostly online speakers from other countries. [Analytics Pioneers Copenhagen](https://www.meetup.com/analytics-pioneers-copenhagen/) runs online trainings by a German agency.

### Step 2: GitHub user search

- **Method:** a [GitHub user search](https://github.com/search?q=location%3ACopenhagen+dbt&type=users) for Copenhagen or Denmark in the bio or location. Then each profile's repositories were checked for dbt in the name. About 130 profiles were scanned.
- **Yield:** 11 people. It found the only real first-time speakers, including an open-source dbt docs tool on PyPI.
- **Learning repositories:** a "dbt-learn" or "dbt-training" repo is not published content. Those people are recorded with no public content.

### Step 3: Vendor stories and newsletters

- **[SYNQ customer stories](https://www.synq.io/customers):** the [Lunar](https://www.synq.io/customers/lunar) case (about 1,500 dbt models) and Better Collective.
- **[Mikkel Dengsøe's Substack](https://mikkeldengsoe.substack.com/archive):** posts from 2025 on dbt with AI.
- **Blocked:** every Medium feed returned HTTP 429 (too many requests), including Pleo, Lunar, Trustpilot and Too Good To Go. No company-blog authors were found.
- **No dbt content:** the [Intellishore insights](https://intellishore.dk/insights/) and the [LEAP website](https://leap-consulting.dk/).

### Step 4: Women-in-data communities

This step looks for speakers through women-focused groups' own events. It never labels or guesses anyone's gender.

- **[TechWomen Cph](https://www.meetup.com/techwomen-cph/):** panels with data leaders, and a 2026-09 masterclass with Women in Data & Analytics. The topics are mostly AI and careers.
- **Dormant:** [R-Ladies Copenhagen](https://www.meetup.com/rladies-copenhagen/) and [Copenhagen Women in Machine Learning & Data Science](https://www.meetup.com/copenhagen-women-in-machine-learning-and-data-science/) have had no events since 2019.
- **Result:** 8 people came from this step.

### Step 5: Job ads and LinkedIn search

- **[Jobindex search for dbt](https://www.jobindex.dk/jobsoegning?q=dbt):** 12 ads. The results embed a JSON list of ads, but each ad links off-site. Only [Dagrofa's ad](https://www.jobindex.dk/vis-job/r14003203) visibly says dbt.
- **[TheirStack](https://theirstack.com/en/technology/dbt/dk):** it shows 10 of the 116 Danish companies it lists as using dbt.
- **[thehub.io](https://thehub.io/jobs?search=dbt):** it loads results in the browser, so a fetch saw only 3 ads from outside Denmark.
- **LinkedIn search results:** 6 people came from posts about dbt work or dbt hiring.

### Step 6: Chapter history

- **Past speakers:** every named speaker in `../enriched/copenhagen-dbt-meetup.json` was added, with their talk as evidence. That covers 11 events, from 2023-02-22 to 2026-09-16.
- **Result:** 32 people in the file have spoken at the chapter.
- **Next event:** [vol. 11](https://www.meetup.com/copenhagen-dbt-meetup/events/316677743/) on 2026-10-21. Its three speakers are in the file as leads, with a note saying they are booked.

### Step 7: Location pass and LinkedIn pass

- **Location pass:** people were placed from public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
  - An in-person talk or host role at a chapter event since 2024-10, at an employer with a Copenhagen office, gave 9 medium-confidence calls.
  - A Sessionize page placed Kshitij Aranke in London.
  - Meetup member profiles tied to a person placed Johan Baltzar in Stockholm and Ernesto Ongaro in Dublin. Each member had joined, by RSVP, the Stockholm dbt meetup where that person spoke.
  - Together they placed 12 people: 9 in Copenhagen and 3 elsewhere.
- **LinkedIn pass:** search results only, never a LinkedIn page. 10 people were searched and 2 placed: Petr Janda in Copenhagen and Stephen O'Kennedy in Dublin.
- **Yield:** 14 people placed across both passes. 3 more (Erica Louie, Hicham Babahmed and Benoit Perigaud) are placed from the same person's record in another city's file. 12 are still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **Meetup's `gql2` endpoint** returns every past event for a group. `eventSearch` also finds upcoming chapter events.
  - **Copenhagen Data Engineering and Databricks User Group Denmark** name every speaker with an employer.
  - **The GitHub user search** found the first-time speakers that blogs could not.
  - **Snowflake User Group Denmark** pages are rendered on the server, so a fetch returns the speakers.
- **Sources that didn't:**
  - **Medium feeds** returned HTTP 429 from the start. Danish company engineering blogs were not reachable.
  - **The [dbt Summit speakers page](https://www.getdbt.com/dbt-summit/speakers)** now shows only the 2027 waitlist.
  - **Jobindex ads** link off-site, so the dbt wording was visible for one ad only.
- **Watch out for:**
  - **Few first-time speakers.** Most Danish leads are proven speakers from Databricks, Snowflake and data engineering meetups, where dbt rarely appears in titles.
  - **Aarhus counts as local.** Several speakers at Databricks and Snowflake user group events work in Aarhus. Commuter towns are local for this chapter, so they are marked in the region.
  - **dbt Labs staff are labelled.** Seven past chapter speakers work at dbt Labs. They can speak, but check the line-up has practitioners first.

## 3. Key leads

- **First-time speakers** (people who publish about dbt but have no talk on record):
  - **Alin Preda (group.one):** [docbt](https://github.com/aleenprd/docbt), an open-source tool on PyPI that writes dbt model documentation. Also a [dbt project on Bilka To Go data](https://github.com/aleenprd/bilka2go-dbt).
  - **Måns Strömer (Quiver):** [an end-to-end dbt and Metabase project](https://github.com/Mansstromer/lundahoj-analytics) on live bike-rental data.
  - **Jasper Alblas (Sparekassen Sjælland):** a [data engineering for beginners series](https://www.jalblas.com/blog/category/data-engineering/) and a [dbt tutorial](https://github.com/JAlblas/dbt-tutorial).
  - **Jens Otto Moeller (Coelacanth Company):** [a dbt shop project with fake Airbyte data](https://github.com/jensottomoeller/dbt-fakerairbyte-shop).
- **Anchor speakers:**
  - **Mihail Alexandru Teodosiu (Vipps MobilePay, Aarhus):** [Vipps MobilePay's dbt and Databricks blueprint](https://www.meetup.com/databricks-user-group-denmark/events/310627895/).
  - **Mikkel Dengsøe (SYNQ):** [analytical data products](https://www.meetup.com/copenhagen-data-engineering/events/305897123/), and a Substack on [AI for data modelling in dbt](https://mikkeldengsoe.substack.com/p/using-ai-for-data-modeling-in-dbt).
  - **Kilian Tscherny (Heyra):** [agentic data engineering](https://www.meetup.com/copenhagen-data-engineering/events/314765565/). A past chapter speaker with new evidence.
  - **Frederik Juhl Pedersen (Veo Technologies):** [a dbt Data Vault that scales with AI](https://www.meetup.com/copenhagen-dbt-meetup/events/313402013/), at chapter vol. 9.
- **Connectors:**
  - **Martin Birk Andreasen (LEAP):** co-organises the [Snowflake User Group Denmark](https://usergroups.snowflake.com/denmark/). LEAP also organises and hosts the chapter.
  - **Kathrine Sofie Rasmussen (LEAP):** part of the chapter's organising team.
  - **Rune Bendix Wittchen (Devoteam) and Sukru Gursoy (Snowflake):** lead the Snowflake User Group Denmark.
  - **Dilovan Celik:** organiser of [Copenhagen Data Engineering](https://www.meetup.com/copenhagen-data-engineering/), with 1,483 members.
  - **Anders Bogsnes (Nordea Asset Management):** organiser of [PyData Copenhagen](https://www.meetup.com/pydata-copenhagen/).
  - **Farzad Bonabi (twoday):** runs the Databricks User Group Denmark meetups hosted at twoday.

## 4. Before outreach

- **Check the "Denmark" calls.** 4 people marked in the region give only "Denmark" as their city.
- **Check most "in region" calls.** Only 10 of the 71 people marked in the region have a location note with evidence. The rest were placed from an event city or an employer's office during research.
- **Don't invite the vol. 11 speakers for that event.** Rasmus Rottwitt, Ernesto Ongaro and Hicham Babahmed speak on 2026-10-21.
- **dbt Labs staff are labelled.** Benoit Perigaud, Nina Anderson and Rachel Ryan are tier 1 and work there. They can speak, but check the line-up has practitioners first.
- **Check people who have moved:**
  - Kilian Tscherny spoke at vol. 6 for Skatteguiden and now leads data engineering at Heyra.
  - Henrik Varmer is now Head of Data Engineering at VELUX.
  - Stephen O'Kennedy's search result names Kinertic, not ZeroNorth.
  - Van Bui has a second GitHub account that names Ageras.
- **Treat Jobindex ads as medium.** Only Dagrofa's ad visibly says dbt.
- **Check one weak location.** Martha Scheffler is tier 1. Qarma's Danish office is in Aarhus, which counts as local, but Martha Scheffler's own location is unconfirmed.

## 5. Next run

- **People still without a location:** 15, mostly chapter speakers and dbt Labs staff.
- **Company blogs:** retry the Pleo, Lunar, Trustpilot and Too Good To Go feeds before the Medium rate limit starts.
- **LinkedIn URLs:** the Snowflake User Group Denmark pages link many profiles. Find those people through search results instead.
- **Job ads:** open the Jobindex ads to read the dbt wording. Try thehub.io in a browser.
- **Women-in-data:** ask TechWomen Cph for introductions to data and analytics engineering speakers.
- **Chapter history:** after 2026-10-21, refresh the chapter history so vol. 11 is included.
- **dbt Slack:** check the [#local-denmark](https://slack.getdbt.com/) channel by hand.

## 6. Replication prompt

````
You are extending my dataset of Danish companies that use dbt, and people who could speak
at or attend the Copenhagen dbt Meetup. The file is copenhagen/copenhagen_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read copenhagen/SEARCH_METHOD.md first, then
research/README.md, research/raw-format.md, research/location-task.md and
research/linkedin-task.md. Keep the shared schema (berlin_planning/SEARCH_METHOD.md §3).
The region is the Copenhagen metro area; Aarhus counts as local, since commuter towns are
local for this chapter.

Try first: new events since metadata.generated_at from Copenhagen Data Engineering,
Databricks User Group Denmark, Snowflake User Group Denmark and TechWomen Cph (Meetup gql2),
the GitHub user search for dbt repos, the Pleo, Lunar and Trustpilot Medium feeds, and the
Jobindex ads opened one by one. Then LinkedIn searches for people still without a location.

Rules: never fetch LinkedIn pages, and take LinkedIn URLs only from search results;
public professional information only; never guess gender, and record pronouns only when
self-stated. Assemble with research/assemble.py --base, place people with
research/apply_locations.py, then run research/validate.py and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Meetup data for 14 Danish data groups, Snowflake User Group Denmark, SYNQ customer stories, a Jobindex dbt search, TheirStack and a GitHub user search, plus chapter history. 90 people at 73 companies, 32 of them past chapter speakers. 11 job ads. Web search ran out after about 15 calls. |
| 2026-10-01 | 1 | Location pass from public pages: in-person chapter talks, Sessionize and tied Meetup member profiles. 12 people placed, 9 in Copenhagen and 3 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 10 people searched, 1 placed in Copenhagen and 1 in Dublin. With the location pass, 14 people placed and 15 still unknown. |
