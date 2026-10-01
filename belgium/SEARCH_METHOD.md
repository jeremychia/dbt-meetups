# Belgium: city notes

This file holds what is specific to Belgium. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Belgium dbt Meetup](https://www.meetup.com/analytics-engineering-belgium/), data in `belgium_dbt_companies.json`
- **Region:** Belgium. Brussels, Antwerp, Ghent, Leuven, Mechelen, Hasselt and Ottignies-Louvain-la-Neuve all count.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 56 |
| People | 106 |
| Tier 1 leads | 34 |
| First-time speakers (publish, no talk yet) | 13 |
| Proven speakers | 87 |
| Spoke at this chapter before | 34 |
| Based in the region | 77 |
| Based elsewhere | 6 |
| Location unknown | 23 |
| With a LinkedIn profile | 23 |
| Job ads mentioning dbt | 3 |
| Past chapter meetups | 14 |
<!-- at-a-glance:end -->

## 1. Where to look in Belgium

### Meetups and conferences

- **Meetup group search:** one `groupSearch` call with a latitude and longitude listed every Belgian data group. Past events for 15 groups were pulled and filtered for dbt.
- **[Databricks User Group Belgium](https://www.meetup.com/databricks-user-group-belgium/events/?type=past):** 14 events. It had the dbt talks from IBA and Volvo Trucks. With dataMinds.be, it is the richest Belgian source of dbt talks outside the chapter.
- **[dataMinds.be](https://www.meetup.com/dataminds-ai/events/?type=past):** 116 events, with 3 dbt sessions in 2025 and 2026. It is a Microsoft data user group.
- **[PyData Belgium](https://www.meetup.com/pydata-belgium/events/?type=past):** 2 dbt talks in 2026.
- **[Data Science Leuven](https://www.meetup.com/data-science-leuven/events/?type=past):** 2 dbt talks in 78 events.
- **[Belgium Snowflake User Group](https://usergroups.snowflake.com/belgium/):** 4 events and 5 organisers. Its December 2025 evening at Telenet was held jointly with the chapter.
- **[dataMinds Connect 2025](https://element61.be/en/node/44093):** element61's sessions at the Mechelen conference.

### Consultancy and company blogs

- **[dataroots blog](https://dataroots.io/blog):** 8 dbt or data quality posts with named authors. Each post names its authors, so fetch the posts rather than the listing. Most of the first-time speakers came from it.
- **[Data Minded on Medium](https://medium.com/feed/datamindedbe):** 10 posts from 2026.
- **[Biztory blog](https://www.biztory.com/blog):** 2 dbt posts.

### Women-in-data communities

- **[WiDS Belgium](https://www.widsworldwide.org/?p=17492):** it lists 4 event ambassadors but no speakers. The ambassadors are recorded as connectors. They are the whole women-in-data pool so far.

### Job ads

- **[TheirStack](https://theirstack.com/en/technology/dbt/be):** it shows 10 of the 167 Belgian companies it lists as using dbt.
- **Ads found:** 3, at [Datashift](https://careers.datashift.eu/o/analytics-engineer), [Lighthouse](https://startup.jobs/senior-analytics-engineer-lighthouse-8769874) and [Deliverect](https://careers.redpoint.com/companies/deliverect/jobs/59856833-analytics-engineer).

### Chapter history and locations

- **Chapter history:** every named speaker in `../enriched/analytics-engineering-belgium.json` was added, with their talk as evidence. That covers 14 events, from meetup #1 (2023-03-23) to meetup #14 (2026-05-12). 34 people in the file have spoken at the chapter.
- **Sessionize speaker pages:** they state a city for most Belgian speakers, and gave 11 high-confidence calls.
- **In-person chapter talks:** an in-person talk or host role at a chapter event since 2024-10, at an employer with a Belgian office, gave 14 medium-confidence calls.
- **Public pages together:** 25 people placed, 21 in Belgium and 4 elsewhere (Zagreb, Aarhus, Naaldwijk and Ilioúpoli).
- **LinkedIn search results:** 14 people searched and 11 placed, 10 in Belgium and 1 in Paris. They placed most dataroots authors, whose posts link only to LinkedIn.

## 2. What didn't work here

- **Web search:** ran out after about 25 calls. Page fetches and the Meetup data covered the rest.
- **Medium feeds:** HTTP 429 (too many requests) after a few calls. Fetch the known Belgian publications first.
- **[Datashift](https://www.datashift.eu/insights), element61, Lytix, Plainsight and Aivix blogs:** 404 errors or images only.
- **Plain web searches for Lytix and element61:** they returned pages about dialectical behaviour therapy. Search the company site instead.
- **dbt Labs pages:** the [dbt Summit 2026 sessions](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role) and the [dbt developer blog authors](https://docs.getdbt.com/blog/authors) had no Belgian employers.
- **[PyLadies Brussels](https://www.meetup.com/pyladies-brussels/):** beginner Python workshops with no named speakers.
- **[R-Ladies Brussels](https://www.meetup.com/R-Ladies-Brussels/):** no events since 2023.
- **Belgian job boards:** a [Stepstone search](https://www.stepstone.be/emplois/dbt/a-gand) returned 0 results, and the aijobs pages redirected. Job-ad coverage is thin.

## 3. Companies looked at

- **dataroots leads the first-time speakers.** Most of them wrote on the dataroots blog.
- **Duplicate company records.** "Xebia Data" and the GoDataDriven/Xebia record are one company.
- **One placeholder employer.** 8 speakers whose employer the event page did not name sit under "Unstated employer (Belgium)".

<!-- companies:start -->
56 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (27)</summary>

Astrafy (local presence not confirmed), Biztory, Bmatix (local presence not confirmed), Dataminded, dataroots, Datashift, dbt Labs (local presence not confirmed), Devoteam G Cloud (local presence not confirmed), Digital Hive (local presence not confirmed), DPG Media (local presence not confirmed), element61, GoDataDriven/Xebia (local presence not confirmed), IBA, Immoscoop (local presence not confirmed), Infofarm (local presence not confirmed), Lighthouse, Orfium (local presence not confirmed), OTA Insight (local presence not confirmed), POLITICO (local presence not confirmed), Qover (local presence not confirmed), reconfigured (local presence not confirmed), Snowflake (local presence not confirmed), Streamz (local presence not confirmed), SYNQ (local presence not confirmed), Telenet, Volvo Trucks, Xebia Data (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (12)</summary>

AE, Agoya (local presence not confirmed), Cegeka, Deliverect, Inspari (local presence not confirmed), Luminus, ML6, Showpad, Solvership (local presence not confirmed), team.blue, Umicore, Valtech (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (16)</summary>

Aivix (local presence not confirmed), Beyond Data Group (local presence not confirmed), Brussels Airlines, Collibra, Datasense, delaware, DPD Belgium, Ghent University, imec, Nordsky (local presence not confirmed), Plainsight, Proximus, Raito (local presence not confirmed), Tinder, Torfs, Unstated employer (Belgium) (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

WiDS Belgium

</details>

<details><summary><b>Blogs and sites scanned</b> (4)</summary>

- https://dataroots.io/blog
- https://medium.com/feed/datamindedbe
- https://medium.com/feed/dataroots
- https://www.biztory.com/blog

</details>

<details><summary><b>Other sources checked</b> (17)</summary>

- [dataroots blog](https://dataroots.io/blog)
- [Data Minded on Medium](https://medium.com/feed/datamindedbe)
- [Biztory blog](https://www.biztory.com/blog)
- [Belgium Snowflake User Group](https://usergroups.snowflake.com/belgium/)
- [Databricks User Group Belgium (meetup gql2)](https://www.meetup.com/databricks-user-group-belgium/events/?type=past)
- [dataMinds.be (meetup gql2)](https://www.meetup.com/dataminds-ai/events/?type=past)
- [PyData Belgium (meetup gql2)](https://www.meetup.com/pydata-belgium/events/?type=past)
- [Data Science Leuven (meetup gql2)](https://www.meetup.com/data-science-leuven/events/?type=past)
- [PyLadies Brussels (meetup gql2)](https://www.meetup.com/pyladies-brussels/events/?type=past) (nothing useful)
- [R-Ladies Brussels (meetup gql2)](https://www.meetup.com/R-Ladies-Brussels/events/?type=past) (nothing useful)
- [WiDS Belgium](https://www.widsworldwide.org/?p=17492)
- [dataMinds Connect 2025 (element61)](https://element61.be/en/node/44093)
- [theirstack dbt in Belgium](https://theirstack.com/en/technology/dbt/be)
- [dbt Summit 2026 search](https://www.getdbt.com/blog/dbt-summit-2026-sessions-by-role) (nothing useful)
- [Stepstone dbt Ghent](https://www.stepstone.be/emplois/dbt/a-gand) (nothing useful)
- [Datashift, element61, Lytix, Plainsight, Aivix blogs](https://www.datashift.eu/insights) (nothing useful)
- [dbt developer blog authors](https://docs.getdbt.com/blog/authors) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Stijn Dolphen (dataroots, Brussels):** [SQLMesh vs dbt Core](https://dataroots.io/blog/sqlmesh-vs-dbt-core-is-a-new-challenger-emerging-in-analytics-engineering), plus a post on dbt Copilot.
  - **Amaury Fouville and Corentin De Ro (dataroots):** [lessons from a one-year migration to Fabric and dbt](https://dataroots.io/blog/lessons-learned-from-a-one-year-migration-towards-fabric-dbt). It would suit a joint talk.
  - **Kristy Broekmans (Biztory, Antwerp):** [the dbt and Snowflake CI/CD workflow](https://www.biztory.com/blog/the-dbt-and-snowflake-ci-cd-workflow).
  - **Mustafa Kurtoglu (dataroots, Leuven):** [open-source Unity Catalog with dbt and DuckDB](https://dataroots.io/blog/open-source-unity-catalog-with-dbt-duckdb). The post was written during an internship.
  - **Paolo Léonard and Nemish Mehta (formerly dataroots, Brussels):** [the state of data quality tools in 2024](https://dataroots.io/blog/state-of-data-quality-tools-2024-q1), including the dbt-native ones.
- **Anchor speakers** (proven dbt speakers who have not spoken at the chapter):
  - **Samuël Delefortrie (Volvo Trucks, Ghent):** [scaling dbt and Databricks across 20+ teams](https://www.meetup.com/databricks-user-group-belgium/events/313956684/).
  - **Flavien Hancart (IBA):** [dbt, Dagster and Databricks](https://www.meetup.com/databricks-user-group-belgium/events/306531852/).
  - **Senne Vanstraelen and Tom Van de Velde (Datashift):** [dbt on Fabric](https://www.meetup.com/dataminds-ai/events/305988682/).
  - **Geert Vinck and David Mat (Telenet):** [dbt and Snowflake at Telenet](https://usergroups.snowflake.com/events/details/snowflake-belgium-presents-belgium-snowflake-user-group-telenet-data-amp-ai-journey/).
  - **Jonas Crevecoeur (Data Minded, Leuven):** [pipelines where Polars and dbt work together](https://www.meetup.com/pydata-belgium/events/315298608/).
- **Connectors:**
  - **Lise Kerckhove (OTA Insight):** [co-hosted the chapter meetup at Lighthouse](https://www.meetup.com/analytics-engineering-belgium/events/303680207/) in Ghent.
  - **Jeroen Wijnants, Kris Van der Biest, Willem Dullaart and Joy Muttai:** the [Belgium Snowflake User Group](https://usergroups.snowflake.com/belgium/) organisers.
  - **Murilo Cunha (dataroots):** [runs PyData Belgium community sessions](https://www.meetup.com/pydata-belgium/events/308607098/).
  - **Setareh Tasdighian, Yanou Ramon, Edith Heiter and Sofie Goethals:** [WiDS Belgium](https://www.widsworldwide.org/?p=17492) event ambassadors.
  - **Bart Smeets (dataroots co-founder):** a likely sponsor contact.

## 5. Before outreach

- [ ] **Check most "in region" calls.** Only 31 of the 77 people marked in Belgium have a location note with evidence. The rest were placed from an event city or an employer's office during research.
- [ ] **Check tier 1.** It holds 34 people, and 17 of them have no item recorded as mentioning dbt. Examples are David Backx, Raghid Bsat and Tim Dries.
- [ ] **Check 12 LinkedIn URLs.** They were copied from the organiser's Meetup event pages, not taken from search results. Each person has a note saying so, and the confidence is medium. Remove them if only search results should count.
- [ ] **Check online speakers.** dataMinds.be runs online talks with speakers from other countries, for example Inspari in Denmark and Solvership in Croatia.
- [ ] **Check people who have moved:**
  - Florian Thoen now works in Paris.
  - Paolo Léonard is now at NEO, Nemish Mehta at IBA and Katarina Milosevic at Datanesis.
- [ ] **Fill missing employers and titles.** Titles marked "(title not stated)" are placeholders. Murilo Cunha's employer is inferred from co-hosting the dataroots podcast.
- [ ] **dbt Labs staff are labelled.** Bart van Delft is tier 1 and works there. Bart van Delft can speak, but check the line-up has practitioners first.
- [ ] **Check people listed in other chapters.** Mikkel Dengsøe, Bart van Delft, Pádraic Slattery, Juan Manuel Perafán and Niko Korvenlaita also appear in other city files.
- [ ] **Read the 2025-12-04 chapter entry** as the joint Snowflake user group evening at Telenet.

## 6. Next run

- **Sources to try first:**
  - **Meetups:** new events from Databricks User Group Belgium, dataMinds.be, PyData Belgium and Data Science Leuven.
  - **Blogs:** new dataroots and Data Minded posts. Retry Datashift, element61, Lytix, Plainsight and Aivix through a site search.
  - **Medium:** fetch other Belgian company publications before the rate limit starts.
  - **Job ads:** run the ATS searches (`site:jobs.lever.co`, `site:job-boards.greenhouse.io`, `site:jobs.ashbyhq.com` with dbt Belgium).
  - **Women-in-data:** ask the WiDS Belgium ambassadors for introductions, and look for named speakers at WiDS Belgium itself.
  - **Data Professionals - Belgium:** its [quarterly data drinks](https://www.meetup.com/data-professionals-belgium/) in Brussels were not scanned for speakers.
- **People to locate:** 23 people have no known location. They include tier-1 leads Arthur Chionh and Johannes Lootens, and most chapter speakers from 2023 and 2024.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `belgium/belgium_dbt_companies.json`, the Belgium dbt Meetup, `../enriched/analytics-engineering-belgium.json` and the region Belgium.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Meetup data for 15 Belgian data groups, the dataroots, Data Minded and Biztory blogs, the Snowflake user group, WiDS Belgium and job boards, plus chapter history. 106 people at 56 companies, 34 of them past chapter speakers. 3 job ads. Web search ran out after about 25 calls. |
| 2026-10-01 | 1 | Location pass from public pages: Sessionize speaker pages and in-person chapter talks. 25 people placed, 21 in Belgium and 4 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 14 people searched, 10 placed in Belgium and 1 in Paris. With the location pass, 36 people placed and 24 still unknown. |
