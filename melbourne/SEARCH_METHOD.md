# Melbourne: city notes

This file holds what is specific to Melbourne. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Melbourne dbt Meetup](https://www.meetup.com/melbourne-dbt-meetup/), data in `melbourne_dbt_companies.json`
- **Region:** Greater Melbourne, including Docklands and Port Melbourne. Sydney and Adelaide do not count.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 2, 2026-10-01)

| | Count |
|---|---|
| Companies | 70 |
| People | 56 |
| Tier 1 leads | 13 |
| First-time speakers (publish, no talk yet) | 2 |
| Proven speakers | 51 |
| Spoke at this chapter before | 7 |
| Based in the region | 52 |
| Based elsewhere | 2 |
| Location unknown | 2 |
| With a LinkedIn profile | 12 |
| Job ads mentioning dbt | 35 |
| Past chapter meetups | 4 |
<!-- at-a-glance:end -->

## 1. Where to look in Melbourne

One research run used about 18 web searches, plus a logged-out LinkedIn Jobs scan.

### dbt Labs events

- **[Coalesce on the Road Melbourne 2025](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne)** (2025-11-11): the best single source. It gave RMIT, REA, MECCA, John Holland, Pepperstone, Marketplacer and David Jones speakers.
- **[dbt World Tour Melbourne 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-melbourne)** (2026-10-06, Fortress Melbourne): RMIT, Onyx Gaming and Suncorp speakers.
- **Reading roadshow pages:** the embedded JSON names every speaker, company and title. Change the slug to `coalesce-in-<city>` or `dbt-world-tour-<city>` and parse the `speakersArray` JSON.

### Local meetups and conferences

- **[Snowflake User Group Melbourne](https://usergroups.snowflake.com/melbourne/):** 932 members and 145 to 250 RSVPs per event. Its pages fetch cleanly.
- **[Data Engineering Melbourne](https://www.meetup.com/data-engineering-melbourne/):** 6,890 members and a monthly talk. Mantel hosted it until 2025-05, then Thoughtworks, MYOB, Fabric Group and Vivanti.
- **[Melbourne Databricks User Group](https://www.meetup.com/melbourne-databricks-user-group/):** 1,359 members, mostly Databricks platform speakers.
- **[DataEngBytes Melbourne 2026](https://dataengbytes.com/2026/melbourne):** read through `/api/2026/users`, which includes self-stated pronouns and LinkedIn URLs.
- **[PyCon AU 2025](https://pretalx.com/pycon-au-2025/schedule/):** held in Melbourne. Titles were cut short, and only one talk was clearly relevant.
- **Chapter history:** every named speaker from `../enriched/melbourne-dbt-meetup.json` was added. That covers 4 events, from 2024-02-15 to 2025-06-24. Every chapter event was held at Mantel's Melbourne office, 452 Flinders St.

### Blogs and job ads

- **[Cevo blog](https://cevo.com.au/tech-insights/):** one dbt article, from 2026-02.
- **[Canva engineering blog](https://www.canva.dev/blog/engineering/):** a Snowflake monitoring post from 2024-11.
- **[Pipeline To Insights](https://pipeline2insights.substack.com/about):** a Melbourne-written Substack with a dbt series.
- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt), logged out:** search `keywords=dbt` for the Melbourne area. Up to 150 ads were checked for the whole word dbt. That gave 35 job ads at 31 companies, for example REA, carsales, Xero, Kogan.com and MECCA Brands. Recruiters are recorded with type `other` and a "RECRUITER" note.

### Locations

- **Recent in-person talks:** 3 people spoke in person in Melbourne in the last 2 years, at employers with a Melbourne office. All 3 are placed at medium confidence.
- **GitHub profiles:** Tristan Handy's profile gives Philadelphia.
- **LinkedIn search results:** 5 people were searched. It placed 3 in Melbourne and 1 in Adelaide.
- **Yield:** 8 people placed across both passes, and 2 still unknown. The evidence rules are in [location rules](../research/README.md#6-location-rules).

## 2. What didn't work here

- **Sydney roadshows:** [Coalesce on the Road Sydney 2025](https://www.getdbt.com/events/roadshow/coalesce-in-sydney) had one Envato speaker with an unknown city. [dbt World Tour Sydney 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-sydney) had no Melbourne speakers.
- **[Microsoft Fabric & Power BI Melbourne](https://www.meetup.com/power-bi-melbourne/):** BI only.
- **DataEngBytes 2025 archive:** does not load.
- **Company blogs:** most Melbourne tech companies have no searchable dbt posts. The [EdgeRed](https://edgered.com.au/technology_partner/dbt-solutions-partner/) partner page names no Melbourne authors. Searches for REA, Seek, Culture Amp, Linktree and carsales blogs returned nothing, and realestate.com.au is blocked by the search tool.
- **Women-in-data groups:** none names speakers, so the line-up needs introductions instead. [R-Ladies+ Melbourne](https://www.meetup.com/rladies-melbourne/) has 2,583 members, but event pages do not name speakers. PyLadies, She Loves Data, WiDS and Women in Data have no Melbourne Meetup groups under the names tried. No candidate came from this step.
- **Head-office locations on LinkedIn:** Mantel's LinkedIn location is its Sydney head office, so it does not place a Melbourne employee.

## 3. Companies looked at

- **Mantel dominates:** it hosted every chapter event and several other user groups. Plan for one speaker per company per event.
- **Sydney overlap:** Rob Scriva (Canva) and Margie Iliescu (Mantel) are in both datasets. Rob Scriva is in Adelaide.
- **Customer speakers at dbt Labs events:** RMIT, REA, John Holland and Pepperstone all have dbt talks on record.

<!-- companies:start -->
69 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (7)</summary>

Canva, John Holland Group, Mantel, MECCA, Onyx Gaming (local presence not confirmed), REA Group, RMIT University

</details>

<details><summary><b>Some dbt signal</b> (36)</summary>

Agoda, Bendigo Bank, BGL Corporate Solutions, Capital.com, carsales, Cevo, Cevo Australia, Commonwealth Bank, Data Engineering Melbourne (meetup), David Jones, Deloitte, Easygo, EdgeRed, Eightcap, Flo Energy, Fusion Markets, GamblingCareers.com, Hawksworth, Heidi, Jenny Barbour IT and Project Recruitment, Kogan.com, Kraken, Latitude Financial Services, Leidos, Lyka, Marketplacer, MECCA Brands, Omio, Otic Group, Pepperstone, Slalom, Synechron, Trideca, UpGuard, Wesfarmers, Xero

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Snowflake User Group Melbourne

</details>

<details><summary><b>Not verified</b> (25)</summary>

Accenture (local presence not confirmed), Acenda Life (local presence not confirmed), Airmaster (local presence not confirmed), Alinta Energy (local presence not confirmed), Austroads (local presence not confirmed), DataEngBytes Melbourne, dbt Labs (local presence not confirmed), Fortress Melbourne, Innablr (local presence not confirmed), InterWorks (local presence not confirmed), Judo Bank (local presence not confirmed), Melbourne Databricks User Group, MYOB, Officeworks (local presence not confirmed), Profectus Group (local presence not confirmed), R-Ladies+ Melbourne, Sahaj.ai (local presence not confirmed), Snowflake A/NZ (local presence not confirmed), Suncorp (local presence not confirmed), Thoughtworks, Thryv (local presence not confirmed), Tixel (local presence not confirmed), Victorian Department of Transport and Planning (local presence not confirmed), Vivanti, Workwear Group (Wesfarmers) (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (2)</summary>

- https://cevo.com.au/tech-insights/
- https://www.canva.dev/blog/engineering/

</details>

<details><summary><b>Other sources checked</b> (17)</summary>

- [dbt World Tour Melbourne 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-melbourne)
- [dbt World Tour Sydney 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-sydney) (nothing useful)
- [Coalesce on the Road Melbourne 2025](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne)
- [Coalesce on the Road Sydney 2025](https://www.getdbt.com/events/roadshow/coalesce-in-sydney) (nothing useful)
- [Melbourne dbt Meetup (past events)](https://www.meetup.com/melbourne-dbt-meetup/)
- [Data Engineering Melbourne meetup](https://www.meetup.com/data-engineering-melbourne/)
- [Melbourne Databricks User Group](https://www.meetup.com/melbourne-databricks-user-group/)
- [Snowflake User Group Melbourne](https://usergroups.snowflake.com/melbourne/)
- [DataEngBytes Melbourne 2026](https://dataengbytes.com/2026/melbourne)
- [PyCon AU 2025 schedule](https://pretalx.com/pycon-au-2025/schedule/)
- [Microsoft Fabric & Power BI Melbourne](https://www.meetup.com/power-bi-melbourne/)
- [R-Ladies+ Melbourne](https://www.meetup.com/rladies-melbourne/) (nothing useful)
- [Cevo blog](https://cevo.com.au/tech-insights/)
- [EdgeRed](https://edgered.com.au/technology_partner/dbt-solutions-partner/) (nothing useful)
- [Canva engineering blog](https://www.canva.dev/blog/engineering/)
- [Pipeline To Insights (Substack)](https://pipeline2insights.substack.com/about)
- [LinkedIn Jobs guest API (keywords=dbt, Melbourne-area)](https://www.linkedin.com/jobs/search?keywords=dbt)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Domenico Campagnolo (Cevo):** wrote [on-demand dbt execution in secure cloud set-ups](https://cevo.com.au/post/on-demand-dbt-execution-rethinking-analytics-engineering-in-secure-cloud-environments/), with dbt-core containers on ECS Fargate. A LinkedIn result places Domenico Campagnolo in Greater Melbourne.
- **Ready for a first dbt talk** (proven speakers whose talks so far are not about dbt):
  - **Erfan Hesami (Airmaster):** writes the [dbt in Action series](https://pipeline2insights.substack.com/p/dbt-in-action-1-fundamentals) on Pipeline To Insights. The only talk on record is on dlt.
  - **Calvin Wang (Canva):** a Staff Analytics Engineer and 2026 Snowflake Data Superhero, on a [Snowflake user group panel](https://usergroups.snowflake.com/events/details/snowflake-melbourne-presents-snowflake-user-group-melbourne-march-2026/).
- **Anchor speakers:**
  - **Sarah Taylor and Dan Lawson (RMIT):** [the day we broke dbt Platform](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne), at Coalesce Melbourne 2025. Sarah Taylor also spoke on RMIT's data mesh at [DataEngBytes 2026](https://dataengbytes.com/2026/melbourne).
  - **Lachlan Clulow and Leandro Bezerra Silva (REA Group):** [lessons from moving to dbt Platform](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne).
  - **David Zmood, Nick Stansfield and Steve Preece (John Holland):** a [three-person dbt journey talk](https://www.getdbt.com/events/roadshow/coalesce-in-melbourne).
  - **Samuel Ellett (Pepperstone):** spoke at the [2024-05 chapter event](https://www.meetup.com/melbourne-dbt-meetup/events/299757694/) and in a Coalesce Melbourne 2025 fireside chat.
- **Connectors:**
  - **Margie Iliescu (Mantel):** organised the [2024 chapter events](https://www.meetup.com/melbourne-dbt-meetup/). The first contact for bringing the venue back.
  - **Priyanka Srivastava (Slalom):** leads the [Snowflake User Group Melbourne](https://usergroups.snowflake.com/melbourne/), a natural co-host.
  - **Emily Melhuish and Choonyin Yeap:** organise [DataEngBytes Melbourne](https://dataengbytes.com/2026/melbourne).
  - **[Data Engineering Melbourne](https://www.meetup.com/data-engineering-melbourne/):** a good co-host partner. Thoughtworks (360 Collins St) is its main venue.

## 5. Before outreach

- [ ] **Check most "in region" calls:** only 6 of the people marked in Greater Melbourne have a location note with evidence. The rest were placed from the employer or event during the first build.
- [ ] **Check people already booked:** RMIT (Vishesh Jain and Will Chan), Onyx Gaming (Aaron Pratt and Edmond Yeo) and Suncorp (Sudheer Chalamcharla) speak at dbt World Tour Melbourne on 2026-10-06.
- [ ] **Merge duplicate companies:** examples are MECCA and MECCA Brands, Cevo and Cevo Australia, and Wesfarmers and Workwear Group (Wesfarmers).
- [ ] **Check one spelling:** the dbt Labs page spells Samuel Ellett as "Samuel Ellet".
- [ ] **Balance dbt Labs staff:** Tristan Handy and Pat Kearns work there and are labelled. Both can speak, but check the line-up has practitioners first.
- [ ] **Use pronouns only where recorded:** 6 people stated pronouns on DataEngBytes. Everyone else has none.

## 6. Next run

- **Sources to try first:**
  - **After 2026-10-06:** add the dbt World Tour Melbourne recordings and any new speakers, from the `speakersArray` JSON on getdbt.com roadshow pages.
  - **Local groups:** new Snowflake User Group Melbourne, Data Engineering Melbourne and Melbourne Databricks User Group events, and DataEngBytes `/api/<year>/users`.
  - **Women-in-data:** try Eventbrite and Luma directly for She Loves Data, WiDS and PyLadies Melbourne, and ask R-Ladies+ Melbourne for its speakers.
  - **Blogs:** try REA, Seek, Culture Amp and carsales blogs through direct fetches instead of web search.
  - **Job ads:** add the Lever, Greenhouse and Ashby `site:` searches for dbt Melbourne.
- **People to locate:**
  - **Evan Williams:** the LinkedIn result shows only Mantel's Sydney head office.
  - **Pat Kearns:** works at dbt Labs and is labelled.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `melbourne/melbourne_dbt_companies.json`, the Melbourne dbt Meetup, `../enriched/melbourne-dbt-meetup.json` and Greater Melbourne. Add: "Count Docklands as Melbourne, and never place someone from a head-office location alone."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build. dbt Labs roadshow agendas, local meetups and user groups, company blogs, women-in-data communities and a LinkedIn Jobs scan, plus chapter history. 56 people at 70 companies, 7 of them past chapter speakers. 35 dbt job ads at 31 companies. |
| 2026-10-01 | 2 | Location pass from public pages: in-person talks at employers with a Melbourne office, and a GitHub profile. 4 people placed, 3 in Melbourne and 1 elsewhere. |
| 2026-10-01 | 2 | LinkedIn pass from search results: 4 people placed, 3 in Melbourne and 1 in Adelaide. With the location pass, 8 people placed and 2 still unknown. |
