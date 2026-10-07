# Salt Lake City: city notes

This file holds what is specific to Salt Lake City and the Wasatch Front. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Salt Lake City dbt Meetup](https://www.meetup.com/salt-lake-city-dbt-meetup/), 55 members and no local event yet. Its only events were two dbt Labs online sessions posted to every group. The goal is the people and companies who could start a first local meetup: speakers, co-organisers, venues and co-hosts. Data in `salt_lake_city_dbt_companies.json`.
- **Region:** Salt Lake City and the Wasatch Front within about an hour: Ogden, Layton, Sandy, Draper, Lehi, American Fork, Orem, Provo and Park City. Logan and St. George do not count.
- **First built:** 2026-10-05

<!-- at-a-glance:start -->
**At a glance** (version 5, 2026-10-06)

| | Count |
|---|---|
| Companies | 130 |
| People | 209 |
| Tier 1 leads | 6 |
| First-time speakers (publish, no talk yet) | 1 |
| Proven speakers | 82 |
| Spoke at this chapter before | 0 |
| Based in the region | 162 |
| Based elsewhere | 2 |
| Location unknown | 45 |
| With a LinkedIn profile | 122 |
| Job ads mentioning dbt | 19 |
| Past chapter meetups | 0 |
<!-- at-a-glance:end -->

## 1. Where to look in Salt Lake City

- **Utah Data Engineering Meetup:** [meetup.com/utah-data-engineering-meetup](https://www.meetup.com/utah-data-engineering-meetup/). The main local pool, with 92 past events and a monthly in-person slot in Salt Lake City or Lehi. Joe Reis and dbt Labs already ran a dbt event here in 2023. The event text never names the speaker, but Meetup's `speakerDetails` field does, often with a LinkedIn link: query it through `gql2` for every event.
- **GitHub user search by location:** `dbt location:Utah`, `"analytics engineer" location:Utah` and `"data engineer" location:"Salt Lake City"` find local practitioners with a stated city, which is high-confidence location evidence. Drop accounts whose bio reads "Data engineer by day, homelab tinkerer by night": they are generated.
- **Big Data Utah:** [meetup.com/bigdatautah](https://www.meetup.com/bigdatautah/). Its event text carries a speaker bio.
- **Other local groups found by `groupSearch`:** [MLOps and AI Utah](https://www.meetup.com/machine-learning-utah/) (monthly in Lehi), the [Utah SQL Server Group](https://www.meetup.com/Utah-SQL-Server-Group/), [Salt Lake PyLadies](https://www.meetup.com/Salt-Lake-Pyladies/), SLC Python and Python at the Point. Their hosts are connectors. Most of their talks are on ML or Python, so their speakers are tier 3.
- **Lehi Tableau User Group:** [usergroups.tableau.com/lehi-tableau-user-group](https://usergroups.tableau.com/lehi-tableau-user-group/), new in July 2026, a BI crowd close to analytics engineering.
- **Utah Snowflake User Group:** [usergroups.snowflake.com/utah](https://usergroups.snowflake.com/utah/). About 300 members. `api/event_slim/for_chapter/37/?status=Completed` lists every past event, and each event page holds speaker and host records with title, employer and LinkedIn. It is also the best route to venues: Pluralsight in Draper, Vivint in Lehi, CHG Healthcare in Midvale and Crumbl HQ.
- **Built In Salt Lake City:** [analytics](https://builtin.com/jobs/salt-lake-city/data-analytics/analytics) and [data engineering](https://builtin.com/jobs/salt-lake-city/data-analytics/data-engineering) listings show a dbt skill tag and need one fetch each.
- **Investor job boards:** the DCVC and Accel boards keep closed ads readable with the data stack. They gave the Recursion and Podium roles.
- **Salt Lake City R User Group:** [the R Consortium interview with Julia Silge](https://r-consortium.org/posts/julia-silge-on-fostering-a-technical-inclusive-r-community-in-salt-lake-city/) names its organisers, Julia Silge and Andrew Redd.
- **Meetup `groupSearch`:** a latitude and longitude search lists the whole local data calendar in one call: Big Data Utah, the Salt Lake Valley Fabric User Group, SLC Python, PyLadies and the Postgres group.

## 2. What didn't work here

- **Built In job listings:** most dbt-tagged roles tagged "Salt Lake City" are remote, at companies based elsewhere, such as Toast, Jellyfish and SharkNinja. They don't show a local employer.
- **dbt Labs, Snowflake and Fivetran case studies:** no Utah company has one that search surfaced.
- **Women-in-data communities:** no WiDS event in Utah, and [Women Tech Council](https://www.womentechcouncil.com/) runs general tech events, not data ones. There is no R-Ladies chapter.
- **Big Mountain Data & Dev, Utah Geek Events and Silicon Slopes Summit:** no speaker list found.
- **dbt Summit speaker pages:** none of the 178 in the getdbt.com sitemap mentions Utah.
- **Utah Tableau and Power BI user groups:** no local leader or events found.
- **Job boards that block fetches:** careerbuilder.com and edtech.com answer 403, and Greenhouse boards and builtin single-job pages return nothing.

## 3. Companies looked at

- **Strongest dbt employers:** Recursion, Podium (Lehi) and Lucid Software all list dbt in data ads, but none of their analytics engineers is named on a public page yet. Pluralsight and Instructure also list dbt.
- **No company case study:** the named people come from meetups, the Snowflake user group and dbt Labs pages, not from company blogs.
- **Local data startups:** Buster (AI agents for dbt, Y Combinator W24) and Aero (Snowflake cost tool) are both dbt-adjacent.

<!-- companies:start -->
128 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (8)</summary>

Buster, dbt Labs, Instructure (local presence not confirmed), Lucid Software, Okta (local presence not confirmed), Pluralsight, Podium, Recursion

</details>

<details><summary><b>Some dbt signal</b> (11)</summary>

Affirm (local presence not confirmed), ConsultNet, Engine (local presence not confirmed), Health Catalyst, Hercules (local presence not confirmed), Jellyfish (local presence not confirmed), LangChain (local presence not confirmed), MetLife (local presence not confirmed), Runpod (local presence not confirmed), SharkNinja (local presence not confirmed), Toast (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (107)</summary>

3M (local presence not confirmed), Adobe (local presence not confirmed), Alianza (local presence not confirmed), Analyst (local presence not confirmed), Aptive Environmental (local presence not confirmed), ASI (local presence not confirmed), Astrodata (local presence not confirmed), Autodesk (local presence not confirmed), Avantlink (local presence not confirmed), Axios-HQ (local presence not confirmed), BENlabs (local presence not confirmed), Big Fish Games (local presence not confirmed), Brigham Young University (local presence not confirmed), Bunked (local presence not confirmed), BYUIDSS (local presence not confirmed), Capital One (local presence not confirmed), CareLife (local presence not confirmed), CareXM (local presence not confirmed), CDW (local presence not confirmed), CHG Healthcare, Clicklease LLC (local presence not confirmed), Cotiviti, Inc. (local presence not confirmed), CrossCountry Consulting (local presence not confirmed), Crumbl HQ, Databricks (local presence not confirmed), Deseret Book (local presence not confirmed), Dickinson College (local presence not confirmed), Domo, doxy.me (local presence not confirmed), Elevate PFS (local presence not confirmed), Employer not found, Ensign College (local presence not confirmed), Entrata (local presence not confirmed), Etsy (local presence not confirmed), Extra Space Storage (local presence not confirmed), FirstEnergy (local presence not confirmed), Fivetran (local presence not confirmed), Goldman Sachs (local presence not confirmed), Google (local presence not confirmed), Highland Analytics (local presence not confirmed), Imagine Learning (local presence not confirmed), Imply (local presence not confirmed), In Project LLC (local presence not confirmed), Institute of Outdoor Recreation and Tourism at Utah State University (local presence not confirmed), JourneyTeam (local presence not confirmed), KUBRA (local presence not confirmed), Leavitt Group Enterprises (local presence not confirmed), Lendio (local presence not confirmed), LexisNexis Risk Solutions (local presence not confirmed), LGCY Power (local presence not confirmed), Life Line Screening (local presence not confirmed), Lockheed Martian (local presence not confirmed), Lucid (local presence not confirmed), Lumio HX (local presence not confirmed), Lynd Bacon & Assoc. Ltd. DBA Loma Buena Associates (local presence not confirmed), Macabacus (local presence not confirmed), MarketDial (local presence not confirmed), Melody-Global (local presence not confirmed), MinIO (local presence not confirmed), MotherDuck (local presence not confirmed), MScienceLLC (local presence not confirmed), N/A (local presence not confirmed), nearmap (local presence not confirmed), O.C. Tanner (local presence not confirmed), OODA Health (local presence not confirmed), Open to Work! (local presence not confirmed), Paradime (local presence not confirmed), Pattern (local presence not confirmed), PCF-BI (local presence not confirmed), Penske Logistics (local presence not confirmed), PepsiCo (local presence not confirmed), Pillpack (local presence not confirmed), Pittsburgh Pirates (local presence not confirmed), PointClickCare (local presence not confirmed), Purple (local presence not confirmed), Redo (local presence not confirmed), Reef Capital Partners (local presence not confirmed), RevGen Partners (local presence not confirmed), SchoolAI (local presence not confirmed), SelectHealth (local presence not confirmed), Snowflake (local presence not confirmed), Sofi (local presence not confirmed), Sotheby's (local presence not confirmed), Streamkap (local presence not confirmed), Strider (local presence not confirmed), Swire Coca-Cola (local presence not confirmed), TaxHawk, Inc. (local presence not confirmed), Ternary Data, Thumbtack (local presence not confirmed), Topgolf (local presence not confirmed), torusco (local presence not confirmed), TripleTen (local presence not confirmed), Trustyy (local presence not confirmed), University of Utah, Utah Data Engineering Meetup, Utah Snowflake User Group, UtahCommunityCreditUnion (local presence not confirmed), Vasion (local presence not confirmed), VEOX (local presence not confirmed), Vivint, Voxel51 (local presence not confirmed), Weave, WFRCAnalytics (local presence not confirmed), www.neo4j.com (local presence not confirmed), Xcelerate (local presence not confirmed), Y2 Analytics (local presence not confirmed), Zions Bancorporation (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (2)</summary>

Posit (local presence not confirmed), Utah Geek Events

</details>

<details><summary><b>Blogs and sites scanned</b> (2)</summary>

- https://usergroups.snowflake.com/utah/
- https://www.getdbt.com/dbt-summit/speakers

</details>

<details><summary><b>Other sources checked</b> (37)</summary>

- [builtin.com Salt Lake City analytics jobs](https://builtin.com/jobs/salt-lake-city/data-analytics/analytics)
- [builtin.com Salt Lake City data engineering jobs](https://builtin.com/jobs/salt-lake-city/data-analytics/data-engineering)
- [Podium analytics engineer ad](https://jobs.accel.com/companies/podium/jobs/78630747-analytics-engineer)
- [Recursion data ads](https://jobs.dcvc.com/companies/recursion-pharmaceuticals-2-ccbe89ca-ec35-439d-885e-ca59051ce93b/jobs/54214851-engineering-manager-data)
- [Lucid Greenhouse board](https://job-boards.greenhouse.io/lucidsoftware/jobs/6017710004) (nothing useful)
- [Utah Snowflake User Group](https://usergroups.snowflake.com/salt-lake-city)
- [Meetup gql2 groupSearch near Salt Lake City](https://www.meetup.com/gql2)
- [Utah Data Engineering Meetup past events](https://www.meetup.com/utah-data-engineering-meetup/)
- [Big Data Utah, Utah SQL Server, SLC Python, Python at the Point, Salt Lake Fabric, Postgres, Elastic past events](https://www.meetup.com/bigdatautah/) (nothing useful)
- [Snowflake Utah User Group](https://usergroups.snowflake.com/salt-lake-city)
- [Big Mountain Data & Dev and Utah Geek Events](https://utahgeekevents.com) (nothing useful)
- [dbt Summit speaker pages](https://www.getdbt.com/dbt-summit/speakers)
- [Utah Tableau and Power BI user groups](https://usergroups.tableau.com) (nothing useful)
- [Silicon Slopes Summit](https://siliconslopes.com) (nothing useful)
- [Utah Snowflake User Group](https://usergroups.snowflake.com/utah/)
- [Built In Salt Lake City analytics jobs](https://builtin.com/jobs/salt-lake-city/data-analytics/analytics) (nothing useful)
- [dbt Summit speakers](https://www.getdbt.com/dbt-summit/speakers)
- [dbt Labs and Snowflake case study search for Utah companies](https://www.getdbt.com/case-studies) (nothing useful)
- [WiDS regional events Utah](https://www.widsworldwide.org/) (nothing useful)
- [Women Tech Council](https://www.womentechcouncil.com/) (nothing useful)
- [PyLadies / R-Ladies Salt Lake City](https://r-consortium.org/posts/julia-silge-on-fostering-a-technical-inclusive-r-community-in-salt-lake-city/)
- [Utah Data Engineering Meetup](https://meetup.com/utah-data-engineering-meetup) (nothing useful)
- [Utah Data Engineering Meetup, Beyond Clicks event](https://www.meetup.com/utah-data-engineering-meetup/events/314536482/) (nothing useful)
- [Snowflake User Group: August meetup at Crumbl HQ](https://usergroups.snowflake.com/events/details/snowflake-salt-lake-city-presents-august-snowflake-meetup-at-crumbl-hq/)
- [Snowflake User Group: Apr 14 2025 kickoff](https://usergroups.snowflake.com/events/details/snowflake-salt-lake-city-presents-apr-14-slc-snowflake-user-group-kickoff-amp-networking) (nothing useful)
- [Snowflake User Group: Unstuck round table](https://usergroups.snowflake.com/events/details/snowflake-utah-presents-snowflake-unstuck-a-community-round-table-amp-ama/) (nothing useful)
- [Snowflake User Group: Dec 2022 meeting at Podium](https://usergroups.snowflake.com/events/details/snowflake-salt-lake-city-presents-utah-user-group-meeting-in-person-1) (nothing useful)
- [Snowflake Data for Breakfast Salt Lake City](https://www.snowflake.com/events/data-for-breakfast/salt-lake-city/)
- [Big Data Utah](https://meetup.com/BigDataUtah)
- [Big Mountain Data and Dev 2026 on Sessionize](https://sessionize.com/big-mountain-data-and-dev-conference_202)
- [Practical Data Summit](https://www.practicaldatasummit.com/) (nothing useful)
- [Salt Lake City Python event](https://www.meetup.com/slcpython/events/308394877) (nothing useful)
- [dbt Summit speaker page for Jessica Stayton](https://www.getdbt.com/dbt-summit/speakers/jessica-stayton) (nothing useful)
- [dbt community spotlight search](https://docs.getdbt.com/community/spotlight) (nothing useful)
- [Utah Snowflake User Group past events (bevy api)](https://usergroups.snowflake.com/api/event_slim/for_chapter/37/?status=Completed)
- [GitHub user search by Utah location](https://github.com/search?q=dbt+location%3AUtah&type=users)
- [dbt Summit speaker pages (sitemap)](https://www.getdbt.com/sitemap-0.xml) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **Data modelling speakers already giving local talks:**
  - Mary Welsh, on [star schemas](https://www.meetup.com/utah-data-engineering-meetup/events/310486417/) and [data warehousing](https://www.meetup.com/utah-data-engineering-meetup/events/305920674/), 2025. Employer and location not found.
  - Jake Anderson (Autodesk, Saratoga Springs), on [conceptual data modelling](https://www.meetup.com/utah-data-engineering-meetup/events/305920437/) in 2025 and learning the business in 2026.
  - John Kerley-Weeks (SelectHealth), on [achieving data quality](https://www.meetup.com/utah-data-engineering-meetup/events/305920616/), 2025.
  - Ben Castleton (CDW), on [minimum viable governance](https://www.meetup.com/utah-data-engineering-meetup/events/302041807/), 2024.
- **First-time speaker leads:** Xander Bennett, an analytics engineer in Salt Lake City who [publishes analytics engineering projects](https://xander-bennett.com/), and Johnathan Brooks (Astrodata), a dbt Champion.
- **Anchor speakers:**
  - Joe Reis (Ternary Data), co-author of *Fundamentals of Data Engineering*, who has spoken at the Utah Data Engineering Meetup several times, including [a dbt Labs event in 2023](https://www.meetup.com/utah-data-engineering-meetup/events/291827521/).
  - Dallin Bentley (Buster), who [presented building an AI data engineer](https://www.meetup.com/utah-data-engineering-meetup/events/311226999/) in January 2026. His talk risks becoming a product pitch, so ask for one about practice.
- **dbt Labs staff:** Brandon Thomson, Manager of Analytics Engineering, writes on [cutting dbt Labs' own compute costs](https://www.getdbt.com/authors/brandon-thomson). His location is unverified.
- **Connectors:**
  - Miriah Peterson hosts every Utah Data Engineering Meetup event.
  - Nathan Giullian (JourneyTeam) and Iurii Iurchenko (Life Line Screening) run the Salt Lake Valley Fabric User Group.
  - Pat Wright runs Big Data Utah and Utah Geek Events.
  - Noah Goodrich and Chandu Yaramasu run the Utah Snowflake User Group.
  - Julia Silge (Posit) co-runs the Salt Lake City R User Group.

## 5. Before outreach

- [ ] Confirm Brandon Thomson is based in Utah. Search summaries say so, but the page they cite returns 404.
- [ ] Confirm Miriah Peterson's employer. Weave comes from an older profile snippet.
- [ ] Find Mary Welsh's employer. Her LinkedIn is linked from her own event page.
- [ ] Find Chandu Yaramasu's employer. Noah Goodrich is now at LimbleCMMS, per his Snowflake event record.
- [ ] Note that Safiyy Momen is also in the New York file. His only Utah tie is a January 2024 lightning talk.
- [ ] Check the speakers who travelled in, such as vendor speakers from MinIO, Imply, MotherDuck and Streamkap. They are tier 3.

## 6. Next run

- **Sources to try first:**
  - Meetup `speakerDetails` and the Snowflake user group API for events since this run.
  - LinkedIn searches for analytics engineers at Recursion, Podium, Lucid and Pluralsight.
- **People to locate:** Brandon Thomson, Pooja Crahen and Jake Van Hecke.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with this city's file, the chapter, `enriched/salt-lake-city-dbt-meetup.json` and the region above.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-05 | 1 | First build: 31 companies, 15 people and 19 dbt job ads, from three research runs. Every link was checked before assembling. |
| 2026-10-05 | 2 | 6 more people from a second search run, mostly Snowflake event speakers and organisers. |
| 2026-10-05 | 3 | 59 more people without web search: speakers from Meetup `speakerDetails` and the Snowflake user group's event records, and Utah data people from GitHub, each then looked up once on LinkedIn. |
| 2026-10-05 | 4 | 62 more people from `find_local_speakers.py`: hosts of 9 more local groups, in-person speakers at MLOps and AI Utah and the Lehi Tableau User Group, and 27 working data people from GitHub. |
