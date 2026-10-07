# Boston: city notes

This file holds what is specific to Boston. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Boston dbt Meetup](https://www.meetup.com/boston-dbt-meetup/), data in `boston_dbt_companies.json`
- **Region:** Greater Boston. Boston, Cambridge and Burlington count. Commuter towns are local for this chapter, so Providence counts too.
- **First built:** 2026-09-24

<!-- at-a-glance:start -->
**At a glance** (version 7, 2026-10-06)

| | Count |
|---|---|
| Companies | 257 |
| People | 493 |
| Tier 1 leads | 6 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 87 |
| Spoke at this chapter before | 21 |
| Based in the region | 476 |
| Based elsewhere | 4 |
| Location unknown | 13 |
| With a LinkedIn profile | 287 |
| Job ads mentioning dbt | 79 |
| Past chapter meetups | 12 |
<!-- at-a-glance:end -->

## 1. Where to look in Boston

The first build used about 18 web searches, plus a logged-out LinkedIn Jobs scan. Leads are scored by the [central scoring rules](../research/README.md#3-scoring-rules).

### Chapter history

- **Past chapter speakers:** every named speaker in `../enriched/boston-dbt-meetup.json`, with the talk. 12 meetups, from 2020-05-08 to 2025-06-18, gave 21 people who have spoken at the chapter and the 3 organisers of the 2024–25 events. The last three meetups were at Klaviyo, 125 Summer Street. The chapter has had no event since 2025-06-18.

### dbt conferences

- **[dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers):** the best source. Filtered to Boston employers, the index gave 3 WHOOP speakers, plus CarGurus, HubSpot and Datadog. Each speaker page (`getdbt.com/dbt-summit/speakers/<slug>`) gives the session title, for about one fetch per lead.
- **[Coalesce 2025 on-demand](https://www.getdbt.com/resources/coalesce-on-demand):** a WHOOP session.
- **[Coalesce 2025 sessions preview](https://www.getdbt.com/blog/what-to-expect-from-sessions-at-coalesce-2025):** a Datadog session.

### Local meetups and conferences

- **[Snowflake User Group Boston](https://usergroups.snowflake.com/boston/):** the April and July 2026 events gave 2 speakers and the 3 organisers. The group meets at Microsoft NERD in Cambridge. The Bevy pages list speakers, bios and organisers in static HTML, so they find local dbt-on-Snowflake practitioners and possible co-hosts.
- **[Boston Data and AI Saturday 2026](https://sessionize.com/sql-saturday-boston-2026/):** 137 talk submissions for 3 October 2026, in Burlington. These are submissions, not accepted sessions.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published.
- **[PyLadies Boston](https://www.meetup.com/pyladies-boston/):** the most active source. It gave a Women in Data Boston representative, a regular presenter and a careers panel. Its venues include CarGurus and Kensho. The 2026-10-01 pass added 3 more hosts as connectors.
- **[WEST](https://www.meetup.com/westorg/):** WEST is Women in the Enterprise of Science & Technology, a Cambridge women-in-STEM association. Its [September 2026 career panel](https://www.meetup.com/westorg/events/316625224/) on AI, data and computational science named 2 biotech data leaders. Marie-Aude Guié (X-Chem) and Yurong Xin (Arbor Biotechnologies) are recorded. Most other WEST events are on careers and leadership.
- **[WiDS Boston](https://www.widsworldwide.org/events/event/wids-boston-northeastern-university/):** this is separate from WiDS Cambridge. The WiDS site search API (`wp-json/wp/v2/search?search=Boston`) found 3 event pages and a round-up. Kavana Venkatesh ran a 2024 generative AI workshop at Northeastern. The [late-2025 round-up](https://www.widsworldwide.org/get-inspired/blog/october-december-2025-ambassador-event-highlights/) describes a Boston University panel of analytics leaders, but the panellists are not named. The ambassadors and Louvere Walker-Hannon (MathWorks, WiDS Advisory Committee) are recorded as connectors.
- **Women Techmakers through GDG Boston and GDG Cloud Boston:** both chapters run International Women's Day events each year. The GDG events API covers them (chapters 269 and 458). The [IWD Boston 2025 page](https://gdg.community.dev/e/mgwcv2/) gave Reen Lepatan (MIT, business analytics) and a talk on data and storytelling. The [IWD 2024 page](https://gdg.community.dev/e/mm79mj/) at the Broad Institute had AI and career talks only. 3 organisers are recorded as connectors.
- **New groups, organisers only:** [Metro Boston Data Ladies](https://www.meetup.com/metro-boston-data-ladies/) started in Waltham in 2026 and holds informal data project meetups. [AWS User Group Women in AI Cambridge](https://www.meetup.com/aws-user-group-women-in-ai-cambridge/) launched online in July 2026. Its launch speakers joined from Seoul and Warsaw, so they are not recorded.

### Company blogs and job ads

- **[Klaviyo Engineering](https://klaviyo.tech/):** the only dbt posts are a CI series by Corey Angers, a past chapter speaker.
- **[LinkedIn Jobs](https://www.linkedin.com/jobs/search?keywords=dbt), logged out:** up to 150 Boston-area ads checked for the whole word "dbt". 62 ads at 48 companies mention it. WHOOP, MFS Investment Management and Dynatrace have 3 ads each. Xometry, IDEXX, Prenuvo, Northeastern University, Counsel Health, SmithRx, Grant Thornton and Tata Consultancy Services have 2 each.
- **[HN Who is hiring](https://hn.algolia.com/api/v1/search?query=dbt&tags=comment):** the Algolia API searched each monthly thread since January 2023 for dbt, one call per thread. Posts were kept when the header names the Boston area and the text uses the whole word dbt. Gave Tive and meQuilibrium as new strong leads, and raised Connie Health and Global Partners LP to strong.
- **Company job boards (open JSON):** the Greenhouse, Lever and Ashby APIs return every open ad with its full text. About 40 employers were checked, and ads located in the Boston area that use the word dbt were kept. Gave Toast and Agero as new strong leads. Their dbt ads are remote, but the boards show a Boston office and a Medford headquarters. EverQuote and Hometap list dbt as a plus. Starburst Data has a Boston role that lists dbt as a plus.
- **GitHub code search for `dbt_project.yml`:** the WhoopInc org holds a public repo that builds Snowflake semantic views from a dbt project.

### Locations

- **Location pass (2026-10-01):** page fetches placed 8 people, 7 in the region and 1 outside. The Meetup `gql2` endpoint gave the profile city of each chapter event's hosts and RSVPs, and placed most past chapter speakers. GitHub profiles and recent in-person talks at an employer with a Boston office gave the rest.
- **LinkedIn pass (2026-10-01):** LinkedIn search results placed 5 people, 4 in the region and 1 outside. No LinkedIn page was opened.

## 2. What didn't work here

- **[Coalesce 2025 agenda](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/agenda-at-a-glance):** renders with JavaScript, so a fetch returns nothing.
- **[dbt World Tour](https://www.getdbt.com/events/roadshow/dbt-world-tour):** no Boston stop in 2026.
- **[PyData Boston - Cambridge](https://www.meetup.com/pydata-boston-cambridge/):** AI and agent topics only.
- **[Data Engineering Boston](https://www.meetup.com/data-engineering-boston/):** 2 events since 2024.
- **[Data, Cloud and AI in Boston](https://www.meetup.com/Big-Data-Developers-in-Boston/):** IBM agent talks.
- **Guessed Meetup group names:** nothing found for Boston Airflow, Databricks, Tableau or WiMLDS.
- **[R-Ladies Boston](https://www.meetup.com/rladies-boston/):** runs socials only.
- **[WiDS Cambridge 2026](https://www.widscambridge.org/featured-speakers-2026):** academic and policy speakers. WiDS means Women in Data Science.
- **Dormant women-in-data groups:** [Boston WiMLDS](https://www.meetup.com/Boston-Women-in-Machine-Learning-and-Data-Science/) last met in November 2022. [Women in Big Data Boston](https://www.meetup.com/women-in-big-data-boston/) last met in June 2020.
- **No named speakers:** [Girl Develop It Boston](https://www.meetup.com/Girl-Develop-It-Boston/) runs national online classes. The [Boston Tableau User Group](https://usergroups.tableau.com/boston-tableau-user-group/) has no Data + Women events.
- **Not found:** She Loves Data, Girls in Tech and Lesbians Who Tech have no Boston Meetup group. [Women in Data](https://www.womenindata.org/) lists no Boston chapter.
- **[Wayfair tech blog](https://www.aboutwayfair.com/careers/tech-blog):** BigQuery and ML content, with no dbt. No local company blog had new dbt authors.
- **Old chapter talks:** give no location evidence. Most talks from 2020–23 could not be placed.
- **GitHub code search for `dbt_project.yml`:** found nothing in 15 other Boston orgs, among them HubSpot, wayfair, toasttab, klaviyo, cargurus, rapid7 and tripadvisor.
- **Meetup venue scan:** Data, Cloud and AI in Boston and Data Engineering Boston events since 2024 were held at IBM, Moderna and Microsoft. None of the events mentions dbt.
- **Job boards with no open JSON:** hubspot, wayfair, ezcater, datarobot, devotedhealth, rapid7, chewy, draftkings and flywire answered none of the three APIs. SimpliSafe, Formlabs, Tripadvisor and Motional had no ad that uses the word dbt.
- **HN posts skipped:** posts that name dbt only as an investor or as a product integration, and posts with no company name, were not counted as dbt users.

## 3. Companies looked at

- **Chapter host:** Klaviyo hosted the last three meetups. Cleartelligence organised the 2024–25 events.
- **WHOOP and CarGurus** give the most conference speakers. Their speakers are placed by the employer's Boston head office, not by a personal profile.
- **No first-time speakers yet.** Boston has none, so the list leans on people who already speak.

<!-- companies:start -->
256 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (13)</summary>

Agero, CarGurus, Cleartelligence, Connie Health, EF Education First (local presence not confirmed), Global Partners LP, HubSpot, Klaviyo, meQuilibrium, Ratio PBC (local presence not confirmed), Tive, Toast, WHOOP

</details>

<details><summary><b>Some dbt signal</b> (49)</summary>

AAA Northeast, ABCorp, Agoda, Alexander Technology Group, Analog Devices, Arbor, Axon, Beacon Biosignals, Bevi, Coforge, CommunityScale (local presence not confirmed), Counsel Health, Curaleaf, Datadog, Delfina, Dynatrace, Flywire, Geode Capital Management, Grant Thornton (US), IDEXX, InvestM Technology LLC, JobGet, Keystone, Leader Bank, LinkSquares, MathWorks, MCS Group - USA, MFS Investment Management, Northeastern University, Patient Funding Alternatives, Perimeter, Plymouth Rock Assurance, Prenuvo, Purple Carrot, Rapid7, SDL Tech Search, SharkNinja, Slalom, SmithRx, Snowflake User Group Boston, Spoiler Alert, Stellix, Strategic Employment Partners (SEP), Tata Consultancy Services, Tenable, Topline Pro, Vero, Xometry, Zelis

</details>

<details><summary><b>dbt as a nice-to-have</b> (3)</summary>

EverQuote, Hometap, Starburst Data

</details>

<details><summary><b>Not verified</b> (182)</summary>

Abbott (local presence not confirmed), AdifiPro LLC (local presence not confirmed), Advent International (local presence not confirmed), AI Engineer (local presence not confirmed), Akamai (local presence not confirmed), Alexion Pharmaceuticals (local presence not confirmed), Alltrna (local presence not confirmed), Alt Sports Data (local presence not confirmed), AltaPotentia (local presence not confirmed), Amazon (local presence not confirmed), Appfolio Inc (local presence not confirmed), Arbella Insurance Group (local presence not confirmed), Arc Analytics (local presence not confirmed), Arizona State University (local presence not confirmed), Arm (local presence not confirmed), Aspire Analytics (local presence not confirmed), AstraZeneca (local presence not confirmed), Atheon Analytics (local presence not confirmed), axioscode (local presence not confirmed), Battery Ventures (local presence not confirmed), BCG (local presence not confirmed), Beacon Bank (local presence not confirmed), Boehringer Ingelheim (local presence not confirmed), Bose Corporation (local presence not confirmed), Boston Children's Hospital, Harvard Medical School (local presence not confirmed), Boston University (local presence not confirmed), Boston-Geospatial (local presence not confirmed), Brandeis University (local presence not confirmed), Broad Institute (local presence not confirmed), broadinstitute (local presence not confirmed), Brown and Caldwell (local presence not confirmed), Bryant University (local presence not confirmed), Canadian Tire Coroporation (local presence not confirmed), Candex, Indigo Ag, Chewy, Northeastern University (local presence not confirmed), Carrum Health (local presence not confirmed), Cellarity (local presence not confirmed), Center for Astrophysics | Harvard & Smithsonian (local presence not confirmed), Centerpoint Transportation (local presence not confirmed), Cervello (local presence not confirmed), Charles River Analytics (local presence not confirmed), Citizens Bank (local presence not confirmed), clariumhealth (local presence not confirmed), Clark University (local presence not confirmed), Clark University | School of Business (local presence not confirmed), clarkuniversity (local presence not confirmed), Coherent Path/Movable Ink (local presence not confirmed), Commonwealth Care Alliance (local presence not confirmed), CoreLogic (local presence not confirmed), cruxclimate (local presence not confirmed), Cumming Group (local presence not confirmed), CVS Health (local presence not confirmed), Data Science Student @ Boston University (local presence not confirmed), Data Scientist at Neuraflash (local presence not confirmed), Databricks (local presence not confirmed), dbt Labs (local presence not confirmed), Demoulas Super Markets, Inc (local presence not confirmed), Dick's Sporting Goods (local presence not confirmed), DraftKings (local presence not confirmed), Drizly (local presence not confirmed), eClinicalworks (local presence not confirmed), Eli Lilly and Company (local presence not confirmed), Elsevier (local presence not confirmed), Emberion (local presence not confirmed), EMD Serono (local presence not confirmed), Exemplar Luxury Group (formerly Saks Global) (local presence not confirmed), Fidelity Investments (local presence not confirmed), FM Global (local presence not confirmed), Free Agent (local presence not confirmed), Fresenius Medical Care (local presence not confirmed), Frontline Analytics (local presence not confirmed), Genpact (local presence not confirmed), GMO LLC (local presence not confirmed), Google (local presence not confirmed), Graduate Stduent at Northeastern University (local presence not confirmed), Graduate Student at Northeastern University (local presence not confirmed), Grand Circle Corp. (local presence not confirmed), GSK (local presence not confirmed), Heyday (local presence not confirmed), https://www.databricks.com (local presence not confirmed), Hult International Business School (local presence not confirmed), Humatics (local presence not confirmed), IBM (local presence not confirmed), Indigo Ag (local presence not confirmed), InformedK12 (local presence not confirmed), Infosys Limited (local presence not confirmed), Inroads Advisory (local presence not confirmed), InterSystems (local presence not confirmed), JLL (local presence not confirmed), Jobble Inc (local presence not confirmed), John Hancock Investments (local presence not confirmed), Kensho, Kevinleary-net (local presence not confirmed), Knapp Consulting LLC (local presence not confirmed), Knode.ai (local presence not confirmed), Known Global (local presence not confirmed), Kraft Analytics Group (local presence not confirmed), LatentView Analytics (local presence not confirmed), Lehigh University (local presence not confirmed), LG Energy Solution (local presence not confirmed), LifeCanvas Technologies (local presence not confirmed), lovepopcards (local presence not confirmed), Mass General Brigham (local presence not confirmed), MassMutual (local presence not confirmed), McK-Internal (local presence not confirmed), Microsoft (local presence not confirmed), Microsoft New England (NERD Center), MIT Sloan IDE (local presence not confirmed), MIT-CAVE (local presence not confirmed), mms-analytics (local presence not confirmed), Moderna, Moody's Analytics (local presence not confirmed), National Geographic Society (local presence not confirmed), National Tire Distributors (local presence not confirmed), NOAA Fisheries, NEFSC (local presence not confirmed), northeastern (local presence not confirmed), NYU Langone Health (local presence not confirmed), OneDigital (local presence not confirmed), Open to Financial Analyst, Business Analyst, Operations Analyst, and FinTech Analyst roles (local presence not confirmed), pairity (local presence not confirmed), Patterns and Predictions (local presence not confirmed), PayPal (local presence not confirmed), Payroc (local presence not confirmed), PhiKonnect Solutions (local presence not confirmed), Philips NA (local presence not confirmed), procter-gamble (local presence not confirmed), Proteotype Diagnostics (local presence not confirmed), Putnam (local presence not confirmed), PyData Boston - Cambridge, PyLadies Boston, R-Ladies Boston, Ratio Therapeutics (local presence not confirmed), Raytheon Technologies (local presence not confirmed), Real Chemistry (local presence not confirmed), Scientific Consultant @ DeepBio Analytics (local presence not confirmed), SeatGeek (local presence not confirmed), Seceon Inc (local presence not confirmed), Seven Bridges Genomics (local presence not confirmed), Shipt (local presence not confirmed), SimpliSafe (local presence not confirmed), Simply Business (local presence not confirmed), Sonrai Analytics (local presence not confirmed), ST Microelectronics (local presence not confirmed), Staples (local presence not confirmed), Stratdigy (formerly DataOps.live) (local presence not confirmed), Strategic Data Insights, LLC (local presence not confirmed), Student (local presence not confirmed), symplr (local presence not confirmed), The Kraft Group (local presence not confirmed), The Legacy Companies (local presence not confirmed), theinkart.com (local presence not confirmed), Think Labs @thinklabs-ai (local presence not confirmed), tsaxena@ampersand.bio (local presence not confirmed), umich (local presence not confirmed), unionstreetmedia (local presence not confirmed), University of Maryland - College Park (local presence not confirmed), University Of Massachusetts (local presence not confirmed), University of Massachusetts Boston (local presence not confirmed), University of Vermont (local presence not confirmed), USAA (local presence not confirmed), utilitywarehouse (local presence not confirmed), VALT Health (local presence not confirmed), VaultSpeed (local presence not confirmed), Verisk Inc. (local presence not confirmed), Versetal Information Systems (local presence not confirmed), Vertex Pharmaceuticals (local presence not confirmed), Virsolus Limited (local presence not confirmed), Wayfair (local presence not confirmed), Weaviate (local presence not confirmed), Wellington Management (local presence not confirmed), Wentworth Institute of Technology (local presence not confirmed), WiDS Cambridge, WilmerHale (local presence not confirmed), Wimoxez (local presence not confirmed), Wistia (local presence not confirmed), Women in Data (Boston), Worcester Polytechnic Institute (local presence not confirmed), Workfabric AI (local presence not confirmed), www.linkedin.com/in/ikrabagwan (local presence not confirmed), Xolix.AI Research Labs (local presence not confirmed), Y-PROC (local presence not confirmed), Zing Data (local presence not confirmed), ZoomInfo (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (9)</summary>

Arbor Biotechnologies (local presence not confirmed), AWS User Group Women in AI Cambridge, Boston Children's Hospital, Metro Boston Data Ladies, MIT, WiDS Boston, Women in the Enterprise of Science & Technology (WEST), Women Techmakers Boston (GDG Boston and GDG Cloud Boston), X-Chem (local presence not confirmed)

</details>

<details><summary><b>Blogs and sites scanned</b> (6)</summary>

- https://klaviyo.tech/
- https://usergroups.snowflake.com/boston/
- https://www.meetup.com/pydata-boston-cambridge/
- https://www.meetup.com/pyladies-boston/
- https://www.meetup.com/rladies-boston/
- https://www.widscambridge.org/featured-speakers-2026

</details>

<details><summary><b>Other sources checked</b> (48)</summary>

- [dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers)
- [Coalesce 2025 on-demand](https://www.getdbt.com/resources/coalesce-on-demand)
- [Coalesce 2025 sessions preview blog](https://www.getdbt.com/blog/what-to-expect-from-sessions-at-coalesce-2025)
- [Coalesce 2025 Cvent agenda](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/agenda-at-a-glance) (nothing useful)
- [dbt World Tour](https://www.getdbt.com/events/roadshow/dbt-world-tour) (nothing useful)
- [Boston dbt Meetup past events (meetup gql2)](https://www.meetup.com/boston-dbt-meetup/)
- [Klaviyo Engineering blog](https://klaviyo.tech/) (nothing useful)
- [Snowflake User Group Boston](https://usergroups.snowflake.com/boston/)
- [PyData Boston - Cambridge (meetup gql2)](https://www.meetup.com/pydata-boston-cambridge/) (nothing useful)
- [Data Engineering Boston (meetup)](https://www.meetup.com/data-engineering-boston/) (nothing useful)
- [Data, Cloud and AI in Boston (meetup)](https://www.meetup.com/Big-Data-Developers-in-Boston/) (nothing useful)
- [PyLadies Boston (meetup gql2)](https://www.meetup.com/pyladies-boston/)
- [R-Ladies Boston (meetup gql2)](https://www.meetup.com/rladies-boston/) (nothing useful)
- [WiDS Cambridge 2026 featured speakers](https://www.widscambridge.org/featured-speakers-2026) (nothing useful)
- [Boston Data and AI Saturday 2026 (Sessionize)](https://sessionize.com/sql-saturday-boston-2026/)
- [Wayfair tech blog](https://www.aboutwayfair.com/careers/tech-blog) (nothing useful)
- [Meetup urlname guesses (Boston Snowflake/Airflow/Databricks/Tableau/WiMLDS/Women in Data)](https://www.meetup.com/) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Boston-area)](https://www.linkedin.com/jobs/search?keywords=dbt)
- [Meetup gql2 groupSearch near Boston](https://www.meetup.com/gql2)
- [WEST past events (Meetup gql2)](https://www.meetup.com/westorg/)
- [Metro Boston Data Ladies (Meetup gql2)](https://www.meetup.com/metro-boston-data-ladies/)
- [AWS User Group Women in AI Cambridge (Meetup gql2)](https://www.meetup.com/aws-user-group-women-in-ai-cambridge/)
- [GDG Boston events API](https://gdg.community.dev/api/event_slim/for_chapter/269/?status=Completed&page_size=300)
- [GDG Cloud Boston events API](https://gdg.community.dev/api/event_slim/for_chapter/458/?status=Completed&page_size=300)
- [International Women's Day Boston 2025 (GDG Boston)](https://gdg.community.dev/e/mgwcv2/)
- [International Women's Day Boston 2024 (GDG Cloud Boston)](https://gdg.community.dev/e/mm79mj/)
- [International Women's Day Boston 2025 (GDG Cloud Boston)](https://gdg.community.dev/e/mmuzvz/) (nothing useful)
- [WiDS Boston @ Northeastern University 2024](https://www.widsworldwide.org/events/event/wids-boston-northeastern-university/)
- [WiDS Boston 2023 event pages](https://www.widsworldwide.org/events/event/wids-boston/)
- [WiDS October–December 2025 ambassador round-up](https://www.widsworldwide.org/get-inspired/blog/october-december-2025-ambassador-event-highlights/)
- [WiDS profile: Louvere Walker-Hannon](https://www.widsworldwide.org/get-inspired/blog/celebrating-louvere-walker-hannon-from-wids-ambassador-to-advisory-committee-member/)
- [Boston WiMLDS (Meetup gql2)](https://www.meetup.com/Boston-Women-in-Machine-Learning-and-Data-Science/) (nothing useful)
- [Women in Big Data Boston (Meetup gql2)](https://www.meetup.com/women-in-big-data-boston/) (nothing useful)
- [Girl Develop It Boston (Meetup gql2)](https://www.meetup.com/Girl-Develop-It-Boston/) (nothing useful)
- [Women in Data (womenindata.org)](https://www.womenindata.org/) (nothing useful)
- [Boston Tableau User Group (Data + Women check)](https://usergroups.tableau.com/boston-tableau-user-group/) (nothing useful)
- [She Loves Data, Girls in Tech and WiMLDS Boston Meetup names](https://www.meetup.com/she-loves-data-boston/) (nothing useful)
- [dbt Analytics Engineering Roundup: dispatches from the frontiers](https://roundup.getdbt.com/p/dispatches-from-the-frontiers)
- [Jenna Jordan: City of Boston reflection](https://jennajordan.me/blog/cob-reflection)
- [dbt Summit speaker page: Jenna Jordan](https://www.getdbt.com/dbt-summit/speakers/jenna-jordan)
- [GitHub user search dbt location:Boston](https://api.github.com/search/users?q=dbt+location:Boston&per_page=30) (nothing useful)
- [Snowflake User Group Boston 2022 event](https://usergroups.snowflake.com/events/details/snowflake-boston-presents-boston-user-group-meeting-lessons-learned-building-a-low-latency-data-warehouse-in-person-4) (nothing useful)
- [DBTA Data Summit 2026 Boston (Luma)](https://luma.com/3u9uklwd) (nothing useful)
- [DuckDB Boston Meetup 2026-09-03](https://duckdb.org/events/2026/09/03/duckdb-boston-meetup/)
- [dbt Summit speaker page: Derek Andres](https://www.getdbt.com/dbt-summit/speakers/derek-andres) (nothing useful)
- [dbt Summit speaker page: David Drummond](https://www.getdbt.com/dbt-summit/speakers/david-drummond) (nothing useful)
- [Databricks community Boston Women in Data panel](https://community.databricks.com/t5/boston/women-in-data-panel/ev-p/91494) (nothing useful)
- [Northeastern DATA Initiative Women in Analytics event](https://damore-mckim.northeastern.edu/events/data-detox-cleansing-your-way-to-accurate-machine-learning) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers at this chapter:**
  - **Samyuktha Kapoor**, analytics engineer. Spoke in person at the Snowflake User Group on reliable Snowflake and dbt pipelines: [April 2026 event](https://usergroups.snowflake.com/events/details/snowflake-boston-presents-april-meetup-community-case-studies/). Early career, with a dbt talk ready to give.
  - **William Tsu**, **Madhura Pharande** and **Sophia Scaglioni Melegari**, WHOOP. dbt Summit 2026 talk on bridging dbt models and Snowflake semantic views: [session](https://www.getdbt.com/dbt-summit/agenda/how-whoop-bridges-dbt-models-and-snowflake-semantic-views).
  - **Jordan Morgan**, Principal Data Analytics Engineer, CarGurus. dbt Summit 2026 talk on moving 80 developers from dbt Core to Fusion: [speaker page](https://www.getdbt.com/dbt-summit/speakers/jordan-morgan).
  - **John Miner** submitted a dbt introduction to Boston Data and AI Saturday: [submissions](https://sessionize.com/sql-saturday-boston-2026/).
- **Anchor speakers:**
  - **Kasey Mazza**, HubSpot. Manages analytics engineering teams and led a dbt Summit 2026 session on positioning them: [session](https://www.getdbt.com/dbt-summit/agenda/beyond-the-bottleneck-position-your-analytics-engineering-team-as-a-strategic-force). Also a route to HubSpot as a host.
  - **Matt Luizzi**, Senior Director Business Analytics, WHOOP. Coalesce 2025 talk on decisions with dbt and Snowflake: [recording](https://www.getdbt.com/resources/coalesce-on-demand/coalesce-2025-how-whoop-unlocks-smarter-decisions-with-dbt-and-snowflake).
  - **Corey Angers**, Klaviyo. Two chapter talks in 2024, on observability and CI with GitHub Actions: [July 2024 event](https://www.meetup.com/boston-dbt-meetup/events/301705215/).
  - **Kevin Hu**, Datadog (formerly Metaplane). A borderline vendor talk, co-presented with Ramp: [Coalesce 2025 preview](https://www.getdbt.com/blog/what-to-expect-from-sessions-at-coalesce-2025).
- **Connectors:**
  - **Chitra Sundaram**, **Riddhima Shukla** and **Stefan Mitrano** (Cleartelligence) organised the 2024–25 chapter events. Contact Cleartelligence first about a restart: [chapter page](https://www.meetup.com/boston-dbt-meetup/).
  - **Evan Cover**, Director of BI Engineering, Klaviyo. The likely sponsor for hosting at Klaviyo again: [dbt Labs post](https://www.getdbt.com/blog/new-dbt-cloud-enhancements-empower-organizations-with-trustworthy-data-at-scale).
  - **Keith Belanger**, **David Garrison** and **Elizabeth Rosso** organise the Snowflake User Group, which has about 2,575 members: [group page](https://usergroups.snowflake.com/boston/).
  - **Kaveesha Shah** represents Women in Data Boston: [PyLadies event](https://www.meetup.com/pyladies-boston/events/313918889/).

## 5. Before outreach

- [ ] **Confirm the tier-1 locations.** All 6 tier-1 people are placed by employer or event, not by a personal profile. Jordan Morgan may work remotely from Maine.
- [ ] **Confirm the 7 unknown locations.** William Kuan's LinkedIn results point to Rapid7 and to Greater Boston separately. Athena Casarotto's Greater Boston profile is a different one from the Drizly profile, and mentions Providence.
- [ ] **Check the weak location calls.** Sabin Thomas was placed by a name match to a chapter member only. Jason Ganz is placed outside the region by a Meetup name match to Washington only.
- [ ] **Skip or re-rank people outside the region.** Divyakumar Savla is in the San Francisco Bay Area, and Adrien Ledoux is in Zurich.
- [ ] **Check Kasey Mazza's chapter talk** against the Meetup page before treating it as a repeat invite. The record cites a March 2023 chapter talk, but the chapter history has no event that month.
- [ ] **Treat Boston Data and AI Saturday entries as unconfirmed** until the schedule for 3 October 2026 is out.
- [ ] **Check the line-up has practitioners first.** Stephen Thibeault, Jason Ganz, Grace Goheen and Jeremy Cohen work at dbt Labs and are labelled.

## 6. Next run

- **Sources to try first:**
  - **LinkedIn pass:** 20 tier-1 and tier-2 people are still `not_searched`.
  - **GitHub user search** (`dbt location:Boston`) for first-time speakers with public dbt work. It was the best source of first-time speakers in Atlanta.
  - **Meetup `gql2` `groupSearch`** with Boston's latitude and longitude, instead of guessing group names. Then read the past events (`sort: DESC`) of the data groups it finds.
  - **Boston Data and AI Saturday:** read the accepted schedule after 3 October 2026. Check new Snowflake User Group events too.
  - **Women in Data Boston:** its own event page was not found. Ask Kaveesha Shah for it, and scan the PyLadies Boston events since the last run.
  - **WiDS x BU panel:** the November 2025 panellists are not named on the WiDS site. Ask the ambassador, Ming Hua Tsai.
  - **LinkedIn Jobs:** re-run the guest scan (keywords=dbt, Boston), keeping ads with the whole word dbt.
- **People to locate:** the 7 unknown locations in section 5, starting with William Kuan and Athena Casarotto.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `boston/boston_dbt_companies.json`, the chapter `boston-dbt-meetup`, `../enriched/boston-dbt-meetup.json` and the region "Greater Boston (Boston, Cambridge, Burlington and nearby), with commuter towns such as Providence". Budget about 25 web searches.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First build: dbt Summit 2026 and Coalesce 2025 agendas filtered to local employers, local meetups and user groups, PyLadies Boston and other women-in-data communities, company blogs, and a LinkedIn Jobs scan. Past chapter speakers added from `../enriched/boston-dbt-meetup.json`. 78 companies (18 on the watchlist), 43 people, 62 job ads at 48 companies, 12 past meetups. Split: 37 proven speakers, 6 featured. Tiers: 6 tier 1, 25 tier 2, 4 tier 3, 8 connectors. 21 people had already spoken at the chapter. |
| 2026-10-01 | 2 | Location pass: 8 people placed from Meetup host and RSVP profiles, GitHub and recent in-person talks, 7 in the region and 1 outside. |
| 2026-10-01 | 2 | LinkedIn pass: 5 people placed from LinkedIn search results, 4 in the region and 1 outside. 9 people are still unknown. |
| 2026-10-01 | 3 | Women-in-data pass: WEST, WiDS Boston, Women Techmakers through GDG Boston and GDG Cloud Boston, Metro Boston Data Ladies, AWS User Group Women in AI Cambridge and new PyLadies Boston hosts. 18 new people: 4 speakers and panellists, and 14 organisers as connectors. |
| 2026-10-01 | 4 | Company pass with fetches only: HN Who is hiring, company job boards, dbt Labs case studies, GitHub code search and Meetup venues. 85 to 93 companies. 8 added, 4 with a strong dbt signal (Tive, meQuilibrium, Toast, Agero). Connie Health and Global Partners LP raised to strong. Starburst Data raised to nice-to-have, with Boston presence confirmed. Job ads 62 to 79. |
| 2026-10-05 | 5 | 2 more people: Jenna Jordan (Ratio PBC), who led dbt adoption at the City of Boston, and Dan Gottlieb (Boston Children's Hospital). |
| 2026-10-05 | 6 | 141 more people from `find_local_speakers.py`: 8 local speakers, 35 organisers of local data groups, 98 data people from GitHub with a town in the region. Speakers count only when a LinkedIn lookup placed them in the region. |
