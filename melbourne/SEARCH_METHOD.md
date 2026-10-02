# Melbourne: city notes

This file holds what is specific to Melbourne. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Melbourne dbt Meetup](https://www.meetup.com/melbourne-dbt-meetup/), data in `melbourne_dbt_companies.json`
- **Region:** Greater Melbourne, including Docklands and Port Melbourne. Sydney and Adelaide do not count.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 4, 2026-10-01)

| | Count |
|---|---|
| Companies | 105 |
| People | 70 |
| Tier 1 leads | 13 |
| First-time speakers (publish, no talk yet) | 2 |
| Proven speakers | 59 |
| Spoke at this chapter before | 7 |
| Based in the region | 56 |
| Based elsewhere | 3 |
| Location unknown | 11 |
| With a LinkedIn profile | 19 |
| Job ads mentioning dbt | 130 |
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
- **[freehire.me API](https://freehire.me/api/v1/jobs/search?skills=dbt&countries=AU):** the JSON API behind freehire.me answers a plain fetch. Four calls return all 365 Australian ads tagged dbt. Many Melbourne ads give only Victoria as the place, so check that the ad is not in Bendigo or Geelong. The search results cut each ad at about 1,000 characters, so read `/api/v1/jobs/<slug>` for the full text. It added La Trobe University, SEEK, PFD Food Services, Angle Auto Finance and the Victorian Department of Justice and Community Safety.
- **[getdbt.com case-study text](https://www.getdbt.com/llms-full-case-studies.txt):** one fetch gives every dbt Labs case study as text, with each company's headquarters. Pepperstone and RMIT University are headquartered in Melbourne.
- **Greenhouse, Lever and Ashby boards:** Xero's Melbourne ads say its stack uses dbt for transformation. Kogan.com's Lever board has a dbt data engineer ad.

### Locations

- **Recent in-person talks:** 3 people spoke in person in Melbourne in the last 2 years, at employers with a Melbourne office. All 3 are placed at medium confidence.
- **GitHub profiles:** Tristan Handy's profile gives Philadelphia.
- **LinkedIn search results:** 5 people were searched. It placed 3 in Melbourne and 1 in Adelaide.
- **Yield:** 8 people placed across both passes, and 2 still unknown. The evidence rules are in [location rules](../research/README.md#6-location-rules).

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published.
- **[Women in Cloud Meetup Group](https://www.meetup.com/women-in-cloud-meetup-group/):** the best source. It has 992 members and monthly talks at Mantel Group and REA. Each event page names the speaker, role and employer. It gave four data talks. Carine Oliveira (Easygo) spoke on [the Easygo data platform](https://www.meetup.com/women-in-cloud-meetup-group/events/310349000/) in August 2025. Anlita Chaisrisukumporn (Easygo) spoke on [the end-to-end data journey](https://www.meetup.com/women-in-cloud-meetup-group/events/313993155/) in April 2026. Gina Bocanegra (REA Group) spoke on [BigQuery telemetry](https://www.meetup.com/women-in-cloud-meetup-group/events/315664762/) in August 2026. Prerna Tiwari (Confluent) spoke on [real-time streaming](https://www.meetup.com/women-in-cloud-meetup-group/events/306749866/) in April 2025. The organisers are listed by first name only.
- **[R-Ladies+ Melbourne](https://www.meetup.com/rladies-melbourne/):** Meetup pages often leave out the speaker. Each event has a repo on [github.com/R-LadiesMelbourne](https://github.com/R-LadiesMelbourne) whose README names the speaker. It gave Elisa Koch and Lauren Boothby (AFL) on [data in sport](https://www.meetup.com/rladies-melbourne/events/304124032/), Kate Saunders (Monash University) on [data-driven decisions](https://www.meetup.com/rladies-melbourne/events/313639240/) and Kirsty McCann (Deakin University) with a ggplotly workshop. The Meetup event hosts gave 5 more organisers as connectors.
- **Women Techmakers Melbourne:** runs International Women's Day events with [GDG Melbourne](https://gdg.community.dev/gdg-melbourne/). The GDG events API (`event_slim/for_chapter/705`) lists every event. Only one data talk since 2023: "Women in Data Science: Challenges & Opportunities" at [IWD 2023](https://gdg.community.dev/e/mja3uz/), by a speaker named only as Thien Anh. Katie Barnett (Bilue) is the ambassador and a connector.
- **Also ask:** R-Ladies+ Melbourne and Women in Cloud take speaker suggestions. Both are routes to more data speakers.

## 2. What didn't work here

- **Sydney roadshows:** [Coalesce on the Road Sydney 2025](https://www.getdbt.com/events/roadshow/coalesce-in-sydney) had one Envato speaker with an unknown city. [dbt World Tour Sydney 2026](https://www.getdbt.com/events/roadshow/dbt-world-tour-sydney) had no Melbourne speakers.
- **[Microsoft Fabric & Power BI Melbourne](https://www.meetup.com/power-bi-melbourne/):** BI only.
- **DataEngBytes 2025 archive:** does not load.
- **Company blogs:** most Melbourne tech companies have no searchable dbt posts. The [EdgeRed](https://edgered.com.au/technology_partner/dbt-solutions-partner/) partner page names no Melbourne authors. Searches for REA, Seek, Culture Amp, Linktree and carsales blogs returned nothing, and realestate.com.au is blocked by the search tool.
- **Women-in-data groups with no data talks:** [Melbourne Women in Machine Learning & Data Science](https://www.meetup.com/Melbourne-Women-in-Machine-Learning-and-Data-Science/) has 1,415 members, but its last event was in February 2022. [Tech Leading Ladies](https://www.meetup.com/Tech-Leading-Ladies/), [Women Coders](https://www.meetup.com/women-coders/) and [Product Women](https://www.meetup.com/women-in-product-melbourne/) run career, coding and AI events only.
- **Women-in-data networks with no Melbourne chapter:** the [PyLadies Melbourne](http://melbourne.pyladies.com/) site returns 404, and no Meetup group was found. [She Loves Data](https://www.shelovesdata.com/) now lists only online AI workshops. [WiDS](https://www.widsworldwide.org/events/) lists no Australian regional event. Women Who Code closed in 2024. Meetup's group search found no Women in Big Data, Data + Women or Girls in Tech group.
- **Head-office locations on LinkedIn:** Mantel's LinkedIn location is its Sydney head office, so it does not place a Melbourne employee.
- **Melbourne, Florida:** a location filter on Melbourne also matches Melbourne in Florida. A Northrop Grumman ad was left out.
- **freehire.me ads placed in the wrong city:** BaptistCare NSW ads and Sydney recruiter ads appear under Victoria. They were left out.
- **Hacker News Who is hiring:** no Melbourne role mentions dbt.
- **GitHub code search:** no public `dbt_project.yml` in the Xero or Culture Amp organisations.

## 3. Companies looked at

- **Mantel dominates:** it hosted every chapter event and several other user groups. Plan for one speaker per company per event.
- **Sydney overlap:** Rob Scriva (Canva) and Margie Iliescu (Mantel) are in both datasets. Rob Scriva is in Adelaide.
- **Customer speakers at dbt Labs events:** RMIT, REA, John Holland and Pepperstone all have dbt talks on record.

<!-- companies:start -->
104 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (29)</summary>

Angle Auto Finance, Avance Consulting, Bendigo Bank, Canva, carsales, Commonwealth Bank, Department of Justice and Community Safety, Victoria, Flo Energy, FourQuarters Recruitment, Heidi, Jenny Barbour IT and Project Recruitment, John Holland Group, Kogan.com, Konnexus, Kraken, La Trobe University, Mantel, MECCA, Motion Recruitment, N2S.Global, Onyx Gaming, Pepperstone, PFD Food Services, Professional Search Group, Quantium, REA Group, RMIT University, SEEK, Xero

</details>

<details><summary><b>Some dbt signal</b> (42)</summary>

Accenture, Agoda, Allume ANZ, Altis Consulting, BGL Corporate Solutions, Capital.com, Cevo, Cevo Australia, Data Engineering Melbourne (meetup), David Jones, Deloitte, Easygo, EdgeRed, Eightcap, Endeavour Group, Fusion Markets, GamblingCareers.com, Global 360, Hawksworth, Intelligen Group, Ippon Technologies, Latitude Financial Services, Leidos, Lyka, Marketplacer, MECCA Brands, NCS Group Australia, Omio, Otic Group, Slalom, Snowflake A/NZ, Synechron, TalentReady, The Commons, Trideca, UpGuard, Vericent, VicRoads Registration and Licensing Services, Vivanti, Wesfarmers, Wex, Xephyr

</details>

<details><summary><b>dbt as a nice-to-have</b> (6)</summary>

Alinta Energy, InfoCentric, Murdoch Children's Research Institute, News Corporation, RACV Limited, Snowflake User Group Melbourne

</details>

<details><summary><b>Not verified</b> (22)</summary>

Acenda Life (local presence not confirmed), Airmaster (local presence not confirmed), Australian Football League (AFL), Austroads (local presence not confirmed), DataEngBytes Melbourne, dbt Labs (local presence not confirmed), Fortress Melbourne, Innablr (local presence not confirmed), InterWorks (local presence not confirmed), Judo Bank (local presence not confirmed), Melbourne Databricks User Group, MYOB, Officeworks (local presence not confirmed), Profectus Group (local presence not confirmed), R-Ladies+ Melbourne, Sahaj.ai (local presence not confirmed), Suncorp (local presence not confirmed), Thoughtworks, Thryv (local presence not confirmed), Tixel (local presence not confirmed), Victorian Department of Transport and Planning (local presence not confirmed), Workwear Group (Wesfarmers) (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (5)</summary>

Bilue (local presence not confirmed), Confluent (local presence not confirmed), Deakin University (local presence not confirmed), Employer not identified (local presence not confirmed), Monash University

</details>

<details><summary><b>Blogs and sites scanned</b> (2)</summary>

- https://cevo.com.au/tech-insights/
- https://www.canva.dev/blog/engineering/

</details>

<details><summary><b>Other sources checked</b> (33)</summary>

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
- [Meetup gql2 groupSearch near Melbourne](https://www.meetup.com/gql2)
- [Women in Cloud Meetup Group (Meetup gql2)](https://www.meetup.com/women-in-cloud-meetup-group/)
- [R-Ladies+ Melbourne (Meetup gql2 and event repos)](https://github.com/R-LadiesMelbourne)
- [GDG Melbourne events API (Women Techmakers)](https://gdg.community.dev/api/event_slim/for_chapter/705/)
- [Melbourne Women in Machine Learning & Data Science](https://www.meetup.com/Melbourne-Women-in-Machine-Learning-and-Data-Science/) (nothing useful)
- [Tech Leading Ladies](https://www.meetup.com/Tech-Leading-Ladies/) (nothing useful)
- [Women Coders (Melbourne)](https://www.meetup.com/women-coders/) (nothing useful)
- [Product Women (Melbourne)](https://www.meetup.com/women-in-product-melbourne/) (nothing useful)
- [PyLadies Melbourne](http://melbourne.pyladies.com/) (nothing useful)
- [She Loves Data](https://www.shelovesdata.com/) (nothing useful)
- [WiDS Worldwide events](https://www.widsworldwide.org/events/) (nothing useful)
- [Women Who Code](https://womenwhocode.com/) (nothing useful)
- [freehire.me API, Australia, skill dbt](https://freehire.me/api/v1/jobs/search?skills=dbt&countries=AU)
- [getdbt.com case studies (llms-full-case-studies.txt)](https://www.getdbt.com/llms-full-case-studies.txt)
- [Greenhouse, Lever and Ashby boards](https://jobs.ashbyhq.com/xero)
- [Hacker News Who is hiring (Algolia)](https://hn.algolia.com/api/v1/search?query=dbt%20melbourne&tags=comment) (nothing useful)

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
  - **Women-in-data:** new Women in Cloud and R-Ladies+ Melbourne events. Try Eventbrite and Luma for She Loves Data and WiDS, which have no reachable Melbourne listing. Ask the Women in Cloud organisers for their full names.
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
| 2026-10-01 | 3 | Women-in-data pass from Women in Cloud, R-Ladies+ Melbourne and Women Techmakers events. 14 people added and 1 extended: 8 speakers, including Easygo, REA and AFL data leads, and 7 organisers as connectors. |
| 2026-10-01 | 4 | Company pass from job ads and case studies: the freehire.me API, Greenhouse, Lever and Ashby boards, and the getdbt.com case-study text. 29 companies and 95 job ads added. 15 companies raised, including Pepperstone, Xero, carsales, Kraken and Heidi to strong. Onyx Gaming, Accenture and Alinta Energy now confirmed in Melbourne. |
