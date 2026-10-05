# Amsterdam: city notes

This file holds what is specific to Amsterdam. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Netherlands dbt Meetup](https://www.meetup.com/amsterdam-dbt-meetup/), data in `amsterdam_dbt_companies.json`
- **Region:** the Netherlands. Amsterdam, Utrecht, Eindhoven and 's-Hertogenbosch all count.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 67 |
| People | 116 |
| Tier 1 leads | 43 |
| First-time speakers (publish, no talk yet) | 11 |
| Proven speakers | 97 |
| Spoke at this chapter before | 33 |
| Based in the region | 80 |
| Based elsewhere | 7 |
| Location unknown | 29 |
| With a LinkedIn profile | 77 |
| Job ads mentioning dbt | 12 |
| Past chapter meetups | 16 |
<!-- at-a-glance:end -->

## 1. Where to look in Amsterdam

### Meetups and conferences

- **[Eindhoven Data Community](https://www.meetup.com/eindhoven-data-community/):** dbt evenings from 2023 to 2026, run with Xebia. It was the densest source of Dutch dbt talks outside the chapter.
- **[PyData Amsterdam](https://www.meetup.com/pydata-nl/) and [Data & Drinks](https://www.meetup.com/data-drinks/)** (Xomnia) came next.
- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** 179 speakers, filtered to Dutch employers. That gave ING, Greenpeace International, Kramp, Xebia and Datafold. The speaker pages name each speaker's employer.
- **[Xebia's Analytics Engineering Meetup](https://events.xebia.com/cloud-data-modernization/analytics-engineering-meetup):** the 2026-05-27 line-up.
- **Smaller yields:** [DataCouncil Amsterdam](https://www.meetup.com/datacouncil-amsterdam/) (one governance talk), the [DuckDB meetup](https://www.meetup.com/duckdb/) (a Miro talk), [DuckCon #7](https://duckdb.org/events/2026/06/24/duckcon7/) (one Dutch user talk) and the [Snowflake User Group Netherlands](https://usergroups.snowflake.com/netherlands/) event pages.

### Company blogs

- **[Xebia blog search feed](https://xebia.com/feed/?s=dbt):** `xebia.com/feed/?s=<term>&paged=N` returns the blog search as RSS with author names. A few fetches listed about 30 dbt posts and most Dutch dbt writers.
- **[Picnic Engineering](https://medium.com/feed/picnic-engineering):** 1 post from 2026.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[PyLadies Amsterdam](https://www.meetup.com/pyladiesams/):** hands-on workshops on dbt, DuckDB and dlt. It was the best source of speakers on dbt and data engineering. Its 2025 and 2026 events added Merel Theisen (QuantumBlack, [Kedro pipelines](https://www.meetup.com/pyladiesams/events/310249357/)) and Felicity Fan ([coding agents with a Streamlit dashboard](https://www.meetup.com/pyladiesams/events/315542536/)). The event hosts, Una Galyeva and Nancy Irisarri Méndez, are recorded as connectors.
- **[Xebia Women in Data](https://www.meetup.com/xebia-women-in-data/):** its own Meetup group at Xebia's Amsterdam office, with 3 editions since September 2025. [Edition 2](https://www.meetup.com/xebia-women-in-data/events/310612027/) had Marlous Been on Odido's data backbone and Doortje de Wiljes, likely Rituals' head of data. [Edition 3](https://www.meetup.com/xebia-women-in-data/events/311855231/) had Anya Prosvetova on Snowflake Intelligence and Larisse Pinto on community. [Edition 4](https://www.meetup.com/xebia-women-in-data/events/315676995/) confirmed the talks by Taís Laurindo Pereira and Sohi Sudhir. The group asks for speakers.
- **[Dutch Women in Tech](https://www.meetup.com/dutch-women-in-tech/):** monthly meetups in Dutch, mostly on careers. Its [December 2025 Power BI evening](https://www.meetup.com/dutch-women-in-tech/events/311120452/) gave Marjolein Opsteegh and Karianne de Dood (Ilionx). Its 5 regular hosts are recorded as connectors.
- **[Rotterdam Women in Tech](https://www.meetup.com/rotterdam-women-in-tech/):** co-working days and workshops. It gave Maryna Makavetskaya ([Intro to SQL](https://www.meetup.com/rotterdam-women-in-tech/events/312386496/)), Mingjue Liu ([Power BI with Claude](https://www.meetup.com/rotterdam-women-in-tech/events/315352580/)) and the organiser Akemi Micallef.
- **[Data + Women Amsterdam](https://usergroups.tableau.com/data-women-amsterdam/):** mostly career and AI themes, plus a Data Expo track.
- **Result:** 30 people came from these groups.

### Job ads

- **Company job boards:** Greenhouse, Lever, Ashby and Recruitee boards for about 90 Dutch companies gave 7 ads at 5 companies.
  - **Mollie:** an [analytics engineering manager](https://jobs.ashbyhq.com/mollie/1bb9f4e2-bc29-4050-afe2-c16796971ef5) and an [analytics engineer](https://jobs.mollie.com/vacancies/aeii).
  - **Xomnia:** a [data analytics engineer](https://careers.xomnia.com/o/data-analytics-engineer) and a [medior data engineer](https://careers.xomnia.com/o/medior-data-engineer).
  - **One each:** [Floryn](https://jobs.floryn.com/o/data-analytics-engineer), [Booking.com](https://nl.engineering.jobs/nl/vacature/data-analytics-engineer-ii-7939174) and [Lightdash](https://jobs.ashbyhq.com/lightdash/309706bc-1081-48b6-89dc-f769bbe17e6d).
- **Company job boards, second run:** about 85 Dutch employers on Greenhouse, Lever, Ashby and Recruitee. Only Mollie, Xomnia, Floryn, Snowflake and Databricks had a Dutch ad whose text has the word dbt. The Snowflake ads confirm its Amsterdam office.
- **HN Who is hiring:** the Algolia API, queried once per monthly thread since January 2023. It gave 3 ads at 2 new companies: [DataChef](https://news.ycombinator.com/item?id=43251524) (hybrid, Netherlands) and [Return](https://news.ycombinator.com/item?id=46134504) (remote, battery storage in the Netherlands).
- **GitHub code search:** the godatadriven (Xebia) organisation has 26 public dbt projects, mostly training material.

### Chapter history and locations

- **Chapter history:** every named speaker in `../enriched/amsterdam-dbt-meetup.json` was added, with their talk as evidence. That covers 16 events, from the 1st edition (2023-02-23) to the 16th (2026-06-02). 34 people in the file have spoken at the chapter.
- **In-person chapter talks:** an in-person talk or host role at a chapter event since 2024-10, at an employer with a Dutch office, placed most people from public pages.
- **Event pages:** DuckCon #7 and Xebia Data Expo placed Floyd Berndsen and Stefan Bakker.
- **Sessionize:** a Sessionize page placed Sam Debruyn in Belgium.
- **LinkedIn search results:** 15 people searched and 8 placed, 6 in the Netherlands and 2 elsewhere (Mysłowice and San Francisco). They placed 7 Xebia authors, whose author boxes state no city.

## 2. What didn't work here

- **Medium feeds:** HTTP 429 (too many requests) after the first fetch, including Booking, bol and Miro. Only Picnic's feed was read.
- **Web search:** ran out after about 20 calls. Page fetches, feeds and the Meetup data covered the rest.
- **[Data Engineering NL](https://www.meetup.com/data-engineering-nl/):** no dbt talks since 2023.
- **[Amsterdam Data Science](https://www.meetup.com/amsterdam-data-science/), R-Ladies Amsterdam, Data Natives Amsterdam and DS Rotterdam:** no dbt talks.
- **[dbt World Tour](https://www.getdbt.com/events/roadshow/dbt-world-tour):** only Asia-Pacific stops in 2026.
- **[PyData Amsterdam 2024 programme](https://amsterdam2024.pydata.org/cfp/schedule/):** HTTP 522 (server down).
- **[Coalesce on-demand listing](https://www.getdbt.com/resources/coalesce-on-demand):** no Dutch employers.
- **Xebia author pages:** they return 404, and the post author boxes give no city.
- **Women-in-data groups with no data talks:** [SheSharp](https://www.meetup.com/shesharp/) (co-working and careers), [Girl Code](https://www.meetup.com/girlcode/) (software engineering), [WeCode](https://www.meetup.com/wecode/) (security and code), and Women in Tech Network and AI Woman Space (no events).
- **Women Techmakers:** the [GDG Amsterdam events API](https://gdg.community.dev/api/event_slim/for_chapter/1358/?status=Completed&page_size=100) lists only Coffee Coding and AppDevCon since 2024.
- **[WiDS](https://www.widsworldwide.org/) and [She Loves Data](https://www.shelovesdata.com/events):** no Netherlands event since 2020, and no European She Loves Data events.
- **Chapter Sessionize:** the [call for speakers](https://sessionize.com/amsterdam-dbt-meetup) is closed and lists no one.
- **Job boards under the obvious name:** Picnic, bol, Coolblue, bunq, Booking.com, WeTransfer, Ohpen, Otrium and TicketSwap are not on Greenhouse, Lever, Ashby or Recruitee under that name. Adyen, Elastic, Catawiki and Miro have boards, but no Dutch ad mentions dbt.
- **GitHub code search:** no public dbt projects for the City of Amsterdam or Picnic.
- **dbt Labs case-study file:** it has no Dutch company.

## 3. Companies looked at

- **Xebia dominates.** It provides 22 of the leads. Plan for one speaker per company per event.
- **Xebia has large teams outside the Netherlands.** A Xebia author is not in the region by default.
- **Two placeholder employers.** "Independent / employer not stated" and "Independent / no company" hold people whose employer was not given. Titles are left empty where the source page did not state one.

<!-- companies:start -->
64 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (37)</summary>

ANWB, Avo (local presence not confirmed), Curative (local presence not confirmed), Databao / JetBrains (local presence not confirmed), DataChef, Datafold (local presence not confirmed), dataroots (local presence not confirmed), dbt (local presence not confirmed), Eindhoven Data Community, Floryn, Greenpeace International, Holland Casino, i-spark (local presence not confirmed), ING, Instapro Group (local presence not confirmed), Kramp, Lightdash (local presence not confirmed), Miele X (local presence not confirmed), Mollie, MotherDuck, Nimbus Intelligence (local presence not confirmed), Omni (local presence not confirmed), Otrium (local presence not confirmed), Picnic, reconfigured (local presence not confirmed), Return, Schiphol (local presence not confirmed), Snowflake, Snowplow (local presence not confirmed), Studyportals, SYNQ (local presence not confirmed), Tasman Analytics (local presence not confirmed), Teradata (local presence not confirmed), The Future Group (local presence not confirmed), TicketSwap Data Engineering Team (local presence not confirmed), Xebia, Xomnia

</details>

<details><summary><b>Some dbt signal</b> (6)</summary>

Aimpoint Digital (local presence not confirmed), Booking.com, Databricks, Miro, PyData Amsterdam, PyLadies Amsterdam

</details>

<details><summary><b>Not verified</b> (11)</summary>

Albert Heijn, AllOptions (local presence not confirmed), Aurai, DaAnalytics, HEMA, IKEA (local presence not confirmed), Manychat (local presence not confirmed), UMC Utrecht, Weheat, Yuki (local presence not confirmed), Zilveren Kruis

</details>

<details><summary><b>Uses a different stack</b> (10)</summary>

Cargill (local presence not confirmed), Data + Women Amsterdam, Ilionx, Odido (local presence not confirmed), QuantumBlack (local presence not confirmed), Rituals (local presence not confirmed), Sandvik (local presence not confirmed), Teva (local presence not confirmed), UWV, Watson+Holmes (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (2)</summary>

- https://medium.com/feed/picnic-engineering
- https://xebia.com/feed/?s=dbt

</details>

<details><summary><b>Other sources checked</b> (33)</summary>

- [dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers)
- [dbt World Tour](https://www.getdbt.com/events/roadshow/dbt-world-tour) (nothing useful)
- [Coalesce on demand](https://www.getdbt.com/resources/coalesce-on-demand) (nothing useful)
- [Xebia blog search feed](https://xebia.com/feed/?s=dbt)
- [Picnic Engineering Medium](https://medium.com/feed/picnic-engineering)
- [Other Medium feeds (Booking, bol, Miro, TicketSwap, tag/dbt)](https://medium.com/feed/booking-com-development) (nothing useful)
- [PyData Amsterdam meetups](https://www.meetup.com/pydata-nl/)
- [PyData Amsterdam 2024 programme](https://amsterdam2024.pydata.org/cfp/schedule/) (nothing useful)
- [PyLadies Amsterdam](https://www.meetup.com/pyladiesams/)
- [Data & Drinks (Xomnia)](https://www.meetup.com/data-drinks/)
- [Eindhoven Data Community](https://www.meetup.com/eindhoven-data-community/)
- [DataCouncil Amsterdam](https://www.meetup.com/datacouncil-amsterdam/)
- [DuckDB meetups](https://www.meetup.com/duckdb/)
- [DuckCon #7 Amsterdam](https://duckdb.org/events/2026/06/24/duckcon7/)
- [Data Engineering NL](https://www.meetup.com/data-engineering-nl/) (nothing useful)
- [Amsterdam Data Science, R-Ladies Amsterdam, Data Natives Amsterdam, DS Rotterdam](https://www.meetup.com/amsterdam-data-science/) (nothing useful)
- [Analytics Engineering Meetup (Xebia)](https://events.xebia.com/cloud-data-modernization/analytics-engineering-meetup)
- [Snowflake User Group Netherlands](https://usergroups.snowflake.com/netherlands/)
- [Data + Women Amsterdam](https://usergroups.tableau.com/data-women-amsterdam/)
- [Company job boards (Greenhouse, Lever, Ashby, Recruitee)](https://jobs.ashbyhq.com/mollie)
- [chapter Sessionize](https://sessionize.com/amsterdam-dbt-meetup) (nothing useful)
- [Meetup gql2 groupSearch near Amsterdam (women-in-data queries)](https://www.meetup.com/gql2#groupSearch-amsterdam-wid)
- [Xebia Women in Data (Meetup gql2 past events)](https://www.meetup.com/xebia-women-in-data/)
- [PyLadies Amsterdam 2025-2026 events (Meetup gql2)](https://www.meetup.com/pyladiesams/events/?type=past)
- [Dutch Women in Tech (Meetup gql2)](https://www.meetup.com/dutch-women-in-tech/)
- [Rotterdam Women in Tech (Meetup gql2)](https://www.meetup.com/rotterdam-women-in-tech/)
- [SheSharp (Meetup gql2)](https://www.meetup.com/shesharp/) (nothing useful)
- [Girl Code (Meetup gql2)](https://www.meetup.com/girlcode/) (nothing useful)
- [WeCode, Women in IT network at KVK (Meetup gql2)](https://www.meetup.com/wecode/) (nothing useful)
- [Women in Tech Network Amsterdam and AI Woman Space (Meetup gql2)](https://www.meetup.com/women-in-tech-network/) (nothing useful)
- [GDG Amsterdam events API (Women Techmakers)](https://gdg.community.dev/api/event_slim/for_chapter/1358/?status=Completed&page_size=100) (nothing useful)
- [WiDS Worldwide site search (Amsterdam, Netherlands)](https://www.widsworldwide.org/wp-json/wp/v2/search?search=Amsterdam) (nothing useful)
- [She Loves Data events](https://www.shelovesdata.com/events) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Thom van Engelenburg (Xebia):** [slowly changing dimensions (type 2) in dbt](https://xebia.com/blog/a-practical-guide-to-creating-slowly-changing-dimensions-type-2-in-dbt-part-1/).
  - **Bo Lemmers (Xebia):** [why we need dbt if we have DAX](https://xebia.com/blog/questions-were-tired-of-hearing-why-do-we-need-dbt-if-we-have-dax/).
  - **Ramon Vermeulen (Xebia, Utrecht):** [monitoring dbt runs with Elementary](https://xebia.com/blog/monitoring-dbt-model-and-test-executions-using-elementary-data/).
  - **Fanny Kassapian (Xebia):** [Fundamentals of Analytics Engineering](https://xebia.com/books/fundamentals-of-analytics-engineering/), a book.
  - **Anahita Singla (Picnic):** [real-time analytics with Apache Iceberg](https://medium.com/picnic-engineering/leveraging-contextual-data-in-real-time-analytics-with-apache-iceberg-1873586e6730).
- **Anchor speakers:**
  - **Jarno Boeijink (ING):** [operationalising dbt across a global bank](https://www.getdbt.com/dbt-summit/speakers/jarno-boeijink), dbt Summit 2026.
  - **Koen Verburg (Greenpeace International):** [a dbt "logic mesh" across 25 organisations](https://www.getdbt.com/dbt-summit/speakers/koen-verburg), dbt Summit 2026.
  - **Henk Pors (ANWB):** [a data platform built around dbt-core](https://www.meetup.com/eindhoven-data-community/events/314211343/).
  - **Katie Scheitzer and Armand Duijen (Studyportals, Eindhoven):** [dbt orchestration with Airflow](https://www.meetup.com/eindhoven-data-community/events/308105203/).
  - **Pádraic Slattery (Xebia):** [dbt-bouncer, a linter for dbt projects](https://www.meetup.com/pydata-nl/events/314861600/). Pádraic Slattery has given 3 talks at the chapter.
- **Connectors:**
  - **Daan Bakboord (DaAnalytics):** chapter leader of the [Snowflake User Group Netherlands](https://usergroups.snowflake.com/netherlands/).
  - **Timea Toltszeki and Maryse Monen:** organisers at [Data + Women Amsterdam](https://usergroups.tableau.com/data-women-amsterdam/).
  - **Marysia Winkels:** [runs PyLadies Amsterdam workshops](https://www.meetup.com/pyladiesams/events/304664913/). Confirm the current role.

## 5. Before outreach

- [ ] **Check most "in region" calls.** Only 27 of the 74 people marked in the Netherlands have a location note with evidence. The rest were placed from an event city or an employer's office during research.
- [ ] **Check tier 1.** It holds 43 people, and 23 of them have no item recorded as mentioning dbt. Examples are Anahita Singla, Camila Birocchi and Yannick Bosch.
- [ ] **Confirm Xebia locations.** Przemyslaw Baran and Anna Wnuczko are tier 1 with no known location. Marcel Ploska is at Xebia Poland.
- [ ] **Check people who have moved:**
  - Camila Birocchi now works at Rituals.
  - Dumky de Wilde wrote the TDD post at Xebia and now works at MotherDuck.
  - Lucas Ortiz and Cor Zuurmond have not been re-checked since their 2023 and 2022 posts.
- [ ] **dbt Labs staff are labelled.** Bart van Delft is tier 1 under a company named "dbt", which the cockpit does not label as dbt Labs. Bart van Delft can speak, but check the line-up has practitioners first.
- [ ] **Check weak leads.** The Holland Casino speakers may be consultants on the project. Taís Laurindo Pereira now works as a product analyst, and the employer is not stated. Doortje de Wiljes is probably Rituals' head of data, but the event page does not say so directly.
- [ ] **Check people listed elsewhere.** Sam Debruyn is in Belgium, Hamzah Chaudhary in San Francisco and Amir Peres (Yuki) in Israel.

## 6. Next run

- **Sources to try first:**
  - **Meetups:** new events from Eindhoven Data Community, PyData Amsterdam, Data & Drinks and PyLadies Amsterdam.
  - **Xebia posts:** `xebia.com/feed/?s=dbt&paged=N`.
  - **Conferences:** the Coalesce 2024 and 2025 agendas and Big Data Expo.
  - **Company blogs:** retry the Booking, Adyen, bol and Mollie engineering blogs.
  - **Women-in-data groups:** new editions of Xebia Women in Data, and the Power BI or SQL sessions at Dutch Women in Tech and Rotterdam Women in Tech. Nothing was reachable for Women Techmakers, WiDS or She Loves Data in the Netherlands, so check again only if a chapter appears.
  - **PyData Amsterdam 2024:** retry the programme. The group is also moving to [Luma](https://luma.com/pydataamsterdam).
- **People to locate:** 19 people have no known location. They include tier-1 leads Oliver Ramsay, Liam McCarty and Jon Su, and most chapter speakers from 2023 and 2024. The PyData, Data & Drinks and PyLadies event pages link most speakers' LinkedIn profiles, so find those people through search results.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `amsterdam/amsterdam_dbt_companies.json`, the Netherlands dbt Meetup, `../enriched/amsterdam-dbt-meetup.json` and the region the Netherlands.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Meetup data for Dutch data groups, the dbt Summit 2026 speakers, the Xebia blog feed, Picnic's Medium feed, women-in-data groups and about 90 company job boards, plus chapter history. 99 people at 61 companies, 34 of them past chapter speakers. 7 job ads. Web search ran out after about 20 calls. |
| 2026-10-01 | 1 | Location pass from public pages: in-person chapter talks, event pages and Sessionize. 15 people placed, 14 in the Netherlands and 1 in Belgium. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 15 people searched, 6 placed in the Netherlands and 2 elsewhere. With the location pass, 23 people placed and 29 still unknown. |
| 2026-10-01 | 2 | Women-in-data pass from Meetup data: Xebia Women in Data, PyLadies Amsterdam, Dutch Women in Tech and Rotterdam Women in Tech. 17 people added (9 speakers, 8 organisers as connectors) and 3 updated with new talks. SheSharp, Girl Code, WeCode, GDG Amsterdam, WiDS and She Loves Data had no data talks. |
| 2026-10-01 | 3 | Company pass from fetches: company job boards, HN Who is hiring, the dbt Labs case-study file and GitHub code search. Companies went from 65 to 67, and job ads from 7 to 12. DataChef and Return are new with a strong dbt signal. Snowflake now has a confirmed Amsterdam office. |
