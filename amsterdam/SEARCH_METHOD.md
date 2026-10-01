# Amsterdam dbt search: method, lessons and replication prompt

This file goes with `amsterdam_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and how to extend it. The shared method and scripts are in [`../research/README.md`](../research/README.md).

- **First built:** 2026-10-01
- **Goal:** find people in the Netherlands who could **speak at** (or attend) the [Netherlands dbt Meetup](https://www.meetup.com/amsterdam-dbt-meetup/), and the local companies that use dbt.
- **Region:** the Netherlands. Amsterdam, Utrecht, Eindhoven and 's-Hertogenbosch all count.

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 61 |
| People | 99 |
| Tier 1 leads | 43 |
| First-time speakers (publish, no talk yet) | 12 |
| Proven speakers | 87 |
| Spoke at this chapter before | 34 |
| Based in the region | 67 |
| Based elsewhere | 3 |
| Location unknown | 29 |
| With a LinkedIn profile | 8 |
| Job ads mentioning dbt | 7 |
| Past chapter meetups | 16 |
<!-- at-a-glance:end -->

## 1. How the search was done

Web search ran out after about 20 calls. The rest of the search used page fetches, feeds and the Meetup data endpoint.

### Step 1: Other Dutch meetups and conferences

- **Meetup's `gql2` endpoint:** it answers a plain POST without a browser, so each group's past events could be pulled and filtered for dbt.
- **[Eindhoven Data Community](https://www.meetup.com/eindhoven-data-community/):** dbt evenings from 2023 to 2026, run with Xebia. It was the densest source of Dutch dbt talks outside the chapter.
- **[PyData Amsterdam](https://www.meetup.com/pydata-nl/) and [Data & Drinks](https://www.meetup.com/data-drinks/)** (Xomnia) came next.
- **Smaller yields:** [DataCouncil Amsterdam](https://www.meetup.com/datacouncil-amsterdam/) (one governance talk), the [DuckDB meetup](https://www.meetup.com/duckdb/) (a Miro talk), [DuckCon #7](https://duckdb.org/events/2026/06/24/duckcon7/) (one Dutch user talk) and the [Snowflake User Group Netherlands](https://usergroups.snowflake.com/netherlands/) event pages.
- **[Xebia's Analytics Engineering Meetup](https://events.xebia.com/cloud-data-modernization/analytics-engineering-meetup):** the 2026-05-27 line-up.
- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** 179 speakers, filtered to Dutch employers. That gave ING, Greenpeace International, Kramp, Xebia and Datafold.
- **No yield:** [Data Engineering NL](https://www.meetup.com/data-engineering-nl/) has had no dbt talks since 2023. [Amsterdam Data Science](https://www.meetup.com/amsterdam-data-science/), R-Ladies Amsterdam, Data Natives Amsterdam and DS Rotterdam had none either. The [dbt World Tour](https://www.getdbt.com/events/roadshow/dbt-world-tour) has only Asia-Pacific stops in 2026.

### Step 2: Company blogs

- **[Xebia blog search feed](https://xebia.com/feed/?s=dbt):** `xebia.com/feed/?s=<term>&paged=N` returns the blog search as RSS with author names. A few fetches listed about 30 dbt posts and most Dutch dbt writers.
- **[Picnic Engineering](https://medium.com/feed/picnic-engineering):** 1 post from 2026.
- **Blocked:** every other Medium feed returned HTTP 429 (too many requests), including Booking, bol and Miro.

### Step 3: Women-in-data communities

This step looks for speakers through women-focused groups' own events. It never labels or guesses anyone's gender.

- **[PyLadies Amsterdam](https://www.meetup.com/pyladiesams/):** hands-on workshops on dbt, DuckDB and dlt. It was the best source of speakers on dbt and data engineering.
- **[Data + Women Amsterdam](https://usergroups.tableau.com/data-women-amsterdam/):** mostly career and AI themes, plus a Data Expo track.
- **Xebia Women in Data meetup:** known only from a search summary, so its talks link to the [Xebia events page](https://events.xebia.com/).
- **Result:** 13 people came from this step.

### Step 4: Job ads

- **Company job boards:** Greenhouse, Lever, Ashby and Recruitee boards for about 90 Dutch companies.
- **Ads found:** 7, at 5 companies.
  - **Mollie:** an [analytics engineering manager](https://jobs.ashbyhq.com/mollie/1bb9f4e2-bc29-4050-afe2-c16796971ef5) and an [analytics engineer](https://jobs.mollie.com/vacancies/aeii).
  - **Xomnia:** a [data analytics engineer](https://careers.xomnia.com/o/data-analytics-engineer) and a [medior data engineer](https://careers.xomnia.com/o/medior-data-engineer).
  - **One each:** [Floryn](https://jobs.floryn.com/o/data-analytics-engineer), [Booking.com](https://nl.engineering.jobs/nl/vacature/data-analytics-engineer-ii-7939174) and [Lightdash](https://jobs.ashbyhq.com/lightdash/309706bc-1081-48b6-89dc-f769bbe17e6d).

### Step 5: Chapter history

- **Past speakers:** every named speaker in `../enriched/amsterdam-dbt-meetup.json` was added, with their talk as evidence. That covers 16 events, from the 1st edition (2023-02-23) to the 16th (2026-06-02).
- **Result:** 34 people in the file have spoken at the chapter.
- **Chapter Sessionize:** the [call for speakers](https://sessionize.com/amsterdam-dbt-meetup) is closed and lists no one.

### Step 6: Location pass and LinkedIn pass

- **Location pass:** people were placed from public pages, by the evidence rules in [`../research/README.md`](../research/README.md).
  - An in-person talk or host role at a chapter event since 2024-10, at an employer with a Dutch office, gave most calls.
  - Event pages for DuckCon #7 and Xebia Data Expo placed Floyd Berndsen and Stefan Bakker.
  - A Sessionize page placed Sam Debruyn in Belgium.
  - Together they placed 15 people: 14 in the Netherlands and 1 elsewhere.
- **LinkedIn pass:** search results only, never a LinkedIn page. 15 people were searched and 8 placed: 6 in the Netherlands and 2 elsewhere (Mysłowice and San Francisco).
- **Yield:** 23 people placed across both passes, and 29 still unknown.

## 2. What we learnt

- **Sources that worked:**
  - **Meetup's `gql2` endpoint** pulls any Dutch group's past events in one call.
  - **The Xebia blog search feed** lists most Dutch dbt writers with their names.
  - **The dbt Summit speaker pages** name each speaker's employer.
  - **LinkedIn search results** placed 7 Xebia authors, whose author boxes state no city.
- **Sources that didn't:**
  - **Medium feeds** returned HTTP 429 after the first fetch. Only Picnic's feed was read.
  - **The [PyData Amsterdam 2024 programme](https://amsterdam2024.pydata.org/cfp/schedule/)** returned HTTP 522 (server down).
  - **The [Coalesce on-demand listing](https://www.getdbt.com/resources/coalesce-on-demand)** had no Dutch employers.
  - **Xebia author pages** return 404, and the post author boxes give no city.
- **Watch out for:**
  - **Xebia dominates.** It provides 22 of the leads. Plan for one speaker per company per event.
  - **Xebia has large teams outside the Netherlands.** A Xebia author is not in the region by default.
  - **Blank titles.** Titles are left empty where the source page did not state one.
  - **Two placeholder employers.** "Independent / employer not stated" and "Independent / no company" hold people whose employer was not given.

## 3. Key leads

- **First-time speakers** (people who publish about dbt but have no talk on record):
  - **Thom van Engelenburg (Xebia):** [slowly changing dimensions (type 2) in dbt](https://xebia.com/blog/a-practical-guide-to-creating-slowly-changing-dimensions-type-2-in-dbt-part-1/).
  - **Bo Lemmers (Xebia):** [why we need dbt if we have DAX](https://xebia.com/blog/questions-were-tired-of-hearing-why-do-we-need-dbt-if-we-have-dax/).
  - **Ramon Vermeulen (Xebia, Utrecht):** [monitoring dbt runs with Elementary](https://xebia.com/blog/monitoring-dbt-model-and-test-executions-using-elementary-data/).
  - **Fanny Kassapian (Xebia):** [Fundamentals of Analytics Engineering](https://xebia.com/books/fundamentals-of-analytics-engineering/), a book.
  - **Anahita Singla (Picnic):** [real-time analytics with Apache Iceberg](https://medium.com/picnic-engineering/leveraging-contextual-data-in-real-time-analytics-with-apache-iceberg-1873586e6730).
- **Anchor speakers** (proven speakers for a line-up):
  - **Jarno Boeijink (ING):** [operationalising dbt across a global bank](https://www.getdbt.com/dbt-summit/speakers/jarno-boeijink), dbt Summit 2026.
  - **Koen Verburg (Greenpeace International):** [a dbt "logic mesh" across 25 organisations](https://www.getdbt.com/dbt-summit/speakers/koen-verburg), dbt Summit 2026.
  - **Henk Pors (ANWB):** [a data platform built around dbt-core](https://www.meetup.com/eindhoven-data-community/events/314211343/).
  - **Katie Scheitzer and Armand Duijen (Studyportals, Eindhoven):** [dbt orchestration with Airflow](https://www.meetup.com/eindhoven-data-community/events/308105203/).
  - **Pádraic Slattery (Xebia):** [dbt-bouncer, a linter for dbt projects](https://www.meetup.com/pydata-nl/events/314861600/). This speaker has given 3 talks at the chapter.
- **Connectors:**
  - **Daan Bakboord (DaAnalytics):** chapter leader of the [Snowflake User Group Netherlands](https://usergroups.snowflake.com/netherlands/).
  - **Timea Toltszeki and Maryse Monen:** organisers at [Data + Women Amsterdam](https://usergroups.tableau.com/data-women-amsterdam/).
  - **Marysia Winkels:** [runs PyLadies Amsterdam workshops](https://www.meetup.com/pyladiesams/events/304664913/). Confirm the current role.

## 4. Before outreach

- **Check most "in region" calls.** Only 20 of the 67 people marked in the Netherlands have a location note with evidence. The rest were placed from an event city or an employer's office during research.
- **Check tier 1.** It holds 43 people, and 23 of them have no item recorded as mentioning dbt. Examples are Anahita Singla, Camila Birocchi and Yannick Bosch.
- **Confirm Xebia locations.** Przemyslaw Baran and Anna Wnuczko are tier 1 with no known location. Marcel Ploska is at Xebia Poland.
- **Check people who have moved:**
  - Camila Birocchi now works at Rituals.
  - Dumky de Wilde wrote the TDD post at Xebia and now works at MotherDuck.
  - Lucas Ortiz and Cor Zuurmond have not been re-checked since their 2023 and 2022 posts.
- **Skip dbt Labs staff.** Bart van Delft is tier 1 under a company named "dbt", which is not marked as excluded.
- **Check two weak leads.** The Holland Casino speakers may be consultants on the project. The Xebia Women in Data talks by Taís Laurindo Pereira and Sohi Sudhir are known only from a search summary.
- **Check people listed elsewhere.** Sam Debruyn is in Belgium. Hamzah Chaudhary is in San Francisco.

## 5. Next run

- **People still without a location:** 29. They include tier-1 leads Oliver Ramsay, Liam McCarty and Jon Su, and most chapter speakers from 2023 and 2024.
- **Conferences:** search the Coalesce 2024 and 2025 agendas and Big Data Expo.
- **Company blogs:** retry the Booking, Adyen, bol and Mollie engineering blogs.
- **PyData Amsterdam 2024:** retry the programme. The group is also moving to [Luma](https://luma.com/pydataamsterdam).
- **LinkedIn:** the PyData, Data & Drinks and PyLadies event pages link most speakers' profiles. Find those people through search results instead.
- **Amir Peres (Yuki):** the Snowflake user group talk was on 2026-10-01. Place Amir Peres once the event page shows the talk was in person.

## 6. Replication prompt

````
You are extending my dataset of Dutch companies that use dbt, and people who could speak
at or attend the Netherlands dbt Meetup. The file is amsterdam/amsterdam_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups. Read amsterdam/SEARCH_METHOD.md first, then
research/README.md, research/raw-format.md, research/location-task.md and
research/linkedin-task.md. Keep the shared schema (berlin_planning/SEARCH_METHOD.md §3).

Try first: new events since metadata.generated_at from Eindhoven Data Community, PyData
Amsterdam, Data & Drinks and PyLadies Amsterdam (Meetup gql2), new Xebia posts
(xebia.com/feed/?s=dbt&paged=N), the Coalesce 2024/2025 agendas and Big Data Expo, and the
Booking, Adyen, bol and Mollie blogs. Then LinkedIn searches for people still without a location.

Rules: never fetch LinkedIn pages, and take LinkedIn URLs only from search results;
public professional information only; never guess gender, and record pronouns only when
self-stated. Assemble with research/assemble.py --base, place people with
research/apply_locations.py, then run research/validate.py and add a change-log row below.
````

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Meetup data for Dutch data groups, the dbt Summit 2026 speakers, the Xebia blog feed, Picnic's Medium feed, women-in-data groups and about 90 company job boards, plus chapter history. 99 people at 61 companies, 34 of them past chapter speakers. 7 job ads. Web search ran out after about 20 calls. |
| 2026-10-01 | 1 | Location pass from public pages: in-person chapter talks, event pages and Sessionize. 15 people placed, 14 in the Netherlands and 1 in Belgium. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 15 people searched, 6 placed in the Netherlands and 2 elsewhere. With the location pass, 23 people placed and 29 still unknown. |
