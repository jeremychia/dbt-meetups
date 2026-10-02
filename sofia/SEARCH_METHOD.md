# Sofia: city notes

This file holds what is specific to Sofia and Bulgaria. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** none yet. The goal is the people and companies who could start a first Sofia dbt Meetup: speakers, co-organisers, venues and co-hosts. Data in `sofia_dbt_companies.json`.
- **Region:** Sofia and the commuter towns within about an hour, such as Pernik, Bozhurishte, Elin Pelin and Samokov. Plovdiv is about two hours away and does not count.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 1, 2026-10-01)

| | Count |
|---|---|
| Companies | 43 |
| People | 22 |
| Tier 1 leads | 3 |
| First-time speakers (publish, no talk yet) | 2 |
| Proven speakers | 8 |
| Spoke at this chapter before | 0 |
| Based in the region | 17 |
| Based elsewhere | 1 |
| Location unknown | 4 |
| With a LinkedIn profile | 9 |
| Job ads mentioning dbt | 22 |
| Past chapter meetups | 0 |
<!-- at-a-glance:end -->

## 1. Where to look in Sofia

Nobody in Sofia has given a public dbt talk that this search could find. So the search starts from job ads to find the companies that run dbt. It then uses the local data communities to find organisers, venues and speakers who already present on nearby topics.

### Job ads

- **[dev.bg dbt search](https://dev.bg/?s=dbt&post_type=job_listing):** the best source. It is server-rendered and lists every active Bulgarian ad with dbt in the text, over two pages. It gave 26 ads at 20 employers, consultancies and recruiters. Four Xebia ads mention dbt only as a partner and are kept as evidence, not as roles. Read each ad's location from the search card. The ad page's sidebar lists every city, so it can't be used for location.
- **[dev.bg analytics engineer search](https://dev.bg/?s=analytics+engineer&post_type=job_listing):** found 6 more data ads at Experian, Insurify, Dreamix, TechPods and Capital.com. None of the 6 mention dbt.
- **Strongest dbt ads:** Capital.com, Nion, DataArt, People and Places and Gamito require dbt. SoftServe, Dataciders ROITI, CreateFuture, Customertimes and Xebia list it among alternatives.

### Meetups and conferences

- **[Meetup gql2](https://www.meetup.com/gql2) group search:** a plain curl POST near latitude 42.6977, longitude 23.3219 listed 57 Sofia groups in one call. Past events of 12 data and tech groups were read since 2023. Host profiles give each host's city.
- **[Bulgarian SQL & BI User Group "Let's SQL Together!"](https://www.meetup.com/bg-sql-bi-user-group-lets-sql-together/) and [Azure Analytics User Group Bulgaria](https://www.meetup.com/azure-analytics-user-group-bulgaria/):** the largest Sofia data user group, with 896 members. It runs [Discovery Day Sofia](https://www.discoverydaysofia.com) at Capital Fort every June. Its focus is the Microsoft data platform. Margarita Naumova and Vili Koleva of INSPIRIT lead it.
- **[PyData Sofia](https://www.meetup.com/pydata-sofia/):** 763 members. It meets with the [Data Science Society](https://www.datasciencesociety.net/events/) about once a month. Talks are mostly ML and LLMs. The March 2026 panel on LLM judges for BI-style SQL tasks gave Yordan Darakchiev.
- **[Paysafe Talks](https://www.meetup.com/paysafetalks-fintech-innovation-collaboration/):** 2,065 members, at Capital Fort or online. The [February 2026 webinar](https://www.meetup.com/paysafetalks-fintech-innovation-collaboration/events/313278042/) gave Miroslav Dimitrov and Martines Angeliev, both Paysafe data engineers.
- **[AWS Bulgaria User Group](https://www.meetup.com/aws-bulgaria/):** 2,273 members. It gave the organisers, the usual venues and one data architecture talk by Peter Mendev of Adastra (2023).
- **[Sofia Microsoft Fabric Meetup](https://www.meetup.com/sofia-fabric-meetup/):** runs [Data Saturday Sofia](https://www.meetup.com/sofia-fabric-meetup/events/311252354/) (October 2025, Sofia Tech Park). Mihail Mateev organises it.
- **[Sofia Low-Key Data Meetup](https://www.meetup.com/sofia-low-key-data-meetup/):** a new informal monthly social for data people. The first event was on 17 September 2026. It has no agenda and no sponsor.

### People

- **[GitHub repo search](https://github.com/search?q=dbt+sofia&type=repositories):** found two public dbt projects: Ivan Krumov's Sofia air quality pipeline and Dimitar Hadzhiev's fintech BI project. Neither profile states a location.
- **[GitHub user search](https://github.com/search?q=%22data+engineer%22+location%3ASofia&type=users):** 17 data engineers state Sofia. None has a dbt repo. The three at Fourth and Dataciders ROITI are recorded, because both employers' ads mention dbt.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded.
- **No active women-in-data community was found in Sofia.** No one was added through this route.
- **[Women in Agile Bulgaria](https://www.meetup.com/women-in-agile-bulgaria/):** 318 members and 7 events since 2023, none on data. Kept as a community channel.
- **Women-in-IT panels:** [Paysafe Talks (March 2024)](https://www.meetup.com/paysafetalks-fintech-innovation-collaboration/events/299792697/) and [Progress "She Leads" (March 2024)](https://www.meetup.com/progressbulgaria/events/299629214/). The panellists work in mobile, frontend and product, not data.

### Locations

- **Meetup host profiles:** a host of an in-person Sofia event whose profile says Sofia is recorded as high.
- **GitHub profiles:** a stated "Sofia, Bulgaria" is high.
- **Speaker bios:** Miroslav Dimitrov's bio names a course at Sofia University, so the location is medium.

## 2. What didn't work here

- **ATS job boards:** Greenhouse, Lever, Ashby and Workable were tried for about 50 Sofia employers. Boards exist for SumUp, Tide, Coherent Solutions, SiteGround, Trading 212 and LucidLink. None of their Sofia roles mention dbt. SumUp's dbt roles are in Berlin. Payhawk, Paysafe, Uber, Experian, Endava, VMware, SAP Labs, Bosch, Shelly and Nexo have no board under the obvious slug.
- **[HN Who is hiring](https://hn.algolia.com/api/v1/search?query=dbt%20Sofia&tags=comment):** 147 hits, none naming both dbt and Sofia or Bulgaria.
- **[Discovery Day speakers](https://discoverydaysofia.com/speakers/):** 20 speakers, all international except the organiser.
- **Data Science Conference:** [DSC Europe](https://www.datasciconference.com/speakers) is in Belgrade, not Sofia. The Data Science Society in Sofia runs meetups, not a conference.
- **[AWS Community Day Bulgaria](https://www.aws-community-day.bg/speakers-2025):** a Wix site that loads by JavaScript, so the speaker list is empty to a fetch.
- **[Data Saturday Sofia 2025 on Eventbrite](https://www.eventbrite.com/e/data-saturdays-sofia-2025-tickets-1071745723309):** no schedule on the page.
- **GDG Sofia:** not listed on gdg.community.dev any more. Only GDG Plovdiv is listed for Bulgaria. So Women Techmakers Sofia events could not be read.
- **PyLadies, R-Ladies, Women Who Code:** no Sofia group on Meetup or on [pyladies.com](https://pyladies.com/locations/). Women Who Code closed in 2024. The Women in Tech Bulgaria domains did not resolve.
- **Infinite Lambda:** a dbt partner, but the website returned HTTP 403. Its GitHub contributors are in Vietnam and the UK. No Sofia office was confirmed.
- **Other meetups:** Python Meetup at Sofia, dxTechTalk, Progress Connect and Nortal Tech Talks had no analytics talks.

## 3. Companies looked at

- **No Sofia dbt meetup or dbt talk has ever run.** The data communities are either Microsoft-platform (Let's SQL Together, Fabric, Data Saturday) or ML-focused (PyData Sofia with the Data Science Society). A dbt meetup would fill the gap between them.
- **Clearest dbt use:** Capital.com, Nion and DataArt, plus two recruiters with unnamed clients. Consultancies (SoftServe, Xebia, Dataciders ROITI, CreateFuture, B EYE) make up much of the rest.
- **Best venues and hosts:** Capital Fort (Paysafe Talks, Discovery Day), SiteGround HQ (PyData Sofia), Barter Community Hub (Python Meetup, Data Science Society) and WorkBetter (AWS Bulgaria).
- **Large employers with no dbt evidence:** Paysafe runs Snowflake and Databricks. SumUp uses dbt only in Berlin. Tide and Trading 212 show none. They are on the watchlist.

<!-- companies:start -->
42 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (6)</summary>

Capital.com, DataArt (Bulgaria), Gamito, Infinite Lambda (local presence not confirmed), Nion, People and Places

</details>

<details><summary><b>Some dbt signal</b> (7)</summary>

CreateFuture, Customertimes Bulgaria, Dataciders ROITI, SoftServe Bulgaria, SumUp (Sofia), Talent Hunter, Xebia (Bulgaria)

</details>

<details><summary><b>dbt as a nice-to-have</b> (9)</summary>

A1 Bulgaria, B EYE, Betty Technology, CADABRA, DSK Bank, Fourth (Sofia), Ocado Technology (Sofia), OpenTag, Sqilline

</details>

<details><summary><b>Not verified</b> (19)</summary>

Adastra Bulgaria, AWS Bulgaria User Group, Bulgarian SQL & BI User Group "Let's SQL Together!" and Azure Analytics User Group Bulgaria, Coherent Solutions, Dreamix, Experian (Sofia), Insurify (Sofia), Large Sofia employers checked, no public job board found (Payhawk, Uber, Experian, Endava, VMware/Broadcom, SAP Labs Bulgaria, Bosch, Shelly, Nexo, Progress, Playtech, MentorMate, HedgeServ) (local presence not confirmed), LucidLink, Paysafe (Sofia), PyData Sofia and Data Science Society, Python Meetup at Sofia (HackBulgaria), SiteGround, Sofia Low-Key Data Meetup, Sofia Microsoft Fabric Meetup and Data Saturday Sofia, TechPods, Tide (Sofia), Trading 212, Women in Agile Bulgaria

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

INSPIRIT

</details>

<details><summary><b>Other sources checked</b> (30)</summary>

- [Meetup gql2 groupSearch near Sofia](https://www.meetup.com/gql2)
- [Bulgarian SQL & BI User Group past events (Meetup gql2)](https://www.meetup.com/bg-sql-bi-user-group-lets-sql-together/)
- [Azure Analytics User Group Bulgaria past events (Meetup gql2)](https://www.meetup.com/azure-analytics-user-group-bulgaria/)
- [PyData Sofia past events (Meetup gql2)](https://www.meetup.com/pydata-sofia/)
- [Paysafe Talks past events (Meetup gql2)](https://www.meetup.com/paysafetalks-fintech-innovation-collaboration/)
- [AWS Bulgaria User Group past events (Meetup gql2)](https://www.meetup.com/aws-bulgaria/)
- [Sofia Microsoft Fabric Meetup past events (Meetup gql2)](https://www.meetup.com/sofia-fabric-meetup/)
- [Sofia Low-Key Data Meetup (Meetup gql2)](https://www.meetup.com/sofia-low-key-data-meetup/)
- [Python Meetup at Sofia past events (Meetup gql2)](https://www.meetup.com/sofia-python-meetup-group/) (nothing useful)
- [dxTechTalk Sofia past events (Meetup gql2)](https://www.meetup.com/dxttsofia/) (nothing useful)
- [Progress Connect: Bulgaria past events (Meetup gql2)](https://www.meetup.com/progressbulgaria/) (nothing useful)
- [Nortal Tech Talks Sofia past events (Meetup gql2)](https://www.meetup.com/nortal-tech-meetups-sofia/) (nothing useful)
- [Women in Agile Bulgaria past events (Meetup gql2)](https://www.meetup.com/women-in-agile-bulgaria/) (nothing useful)
- [dev.bg job search: dbt](https://dev.bg/?s=dbt&post_type=job_listing)
- [dev.bg job search: analytics engineer](https://dev.bg/?s=analytics+engineer&post_type=job_listing)
- [Greenhouse, Lever, Ashby and Workable boards (about 50 Sofia employers)](https://boards-api.greenhouse.io/v1/boards/sumup/jobs?content=true) (nothing useful)
- [HN Who is hiring (dbt Sofia)](https://hn.algolia.com/api/v1/search?query=dbt%20Sofia&tags=comment) (nothing useful)
- [Discovery Day Sofia speakers](https://discoverydaysofia.com/speakers/) (nothing useful)
- [DSC Europe speakers](https://www.datasciconference.com/speakers) (nothing useful)
- [Data Science Society events](https://www.datasciencesociety.net/events/)
- [AWS Community Day Bulgaria speakers](https://www.aws-community-day.bg/speakers-2025) (nothing useful)
- [Data Saturday Sofia 2025 (Eventbrite)](https://www.eventbrite.com/e/data-saturdays-sofia-2025-tickets-1071745723309) (nothing useful)
- [GitHub user search: data engineer, location Sofia](https://github.com/search?q=%22data+engineer%22+location%3ASofia&type=users)
- [GitHub repo search: dbt with Sofia or Bulgaria](https://github.com/search?q=dbt+sofia&type=repositories)
- [Infinite Lambda GitHub contributors](https://github.com/infinitelambda) (nothing useful)
- [GDG chapters API (Bulgaria)](https://gdg.community.dev/api/chapter_slim/) (nothing useful)
- [PyLadies locations](https://pyladies.com/locations/) (nothing useful)
- [Women in Tech Bulgaria sites](https://womenintech.bg) (nothing useful)
- [Meetup gql2 women-in-tech groups near Sofia](https://www.meetup.com/gql2) (nothing useful)
- [Paysafe Talks and Progress women-in-IT panels](https://www.meetup.com/paysafetalks-fintech-innovation-collaboration/events/299792697/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Ivan Krumov**, employer unknown: [a Sofia air quality pipeline with BigQuery and dbt](https://github.com/IvanKrumov/sofia-air-quality-pipeline) (November 2025).
  - **Dimitar Hadzhiev**, employer unknown: [a fintech BI project with a tested dbt layer and a Power BI semantic model](https://github.com/hadzhiev96/fintech-bi) (May 2026).
- **Anchor speakers:**
  - **Miroslav Dimitrov**, Senior Manager of Data Engineering, Paysafe: presented [AI-Driven Engineering Documentation](https://www.meetup.com/paysafetalks-fintech-innovation-collaboration/events/313278042/) for data teams (February 2026). Also teaches a SQL Server course at Sofia University.
  - **Martines Angeliev**, Senior Data Engineer, Paysafe: co-presented the same webinar. Works on Snowflake and GCP pipelines.
  - **Yordan Darakchiev**, data scientist and trainer: ran a [PyData Sofia panel on LLM judges for BI-style SQL tasks](https://www.meetup.com/pydata-sofia/events/313537093/) (March 2026).
  - **Peter Mendev**, Adastra: gave [Modern Data Architecture with AWS](https://www.meetup.com/aws-bulgaria/events/293545484/) at AWS Bulgaria (2023).
- **Connectors:**
  - **Margarita Naumova**, INSPIRIT: founder of Let's SQL Together and Discovery Day Sofia. The strongest co-host candidate.
  - **Yasen Kiprov** and **Milen Chechev**, PyData Sofia: run the monthly meetup with the Data Science Society.
  - **Mihail Mateev**, Sofia Microsoft Fabric Meetup and Data Saturday Sofia.
  - **Hristina Hristova**, Paysafe Talks: the route to the Capital Fort venue.
  - **Daniel Rankov**, AWS Bulgaria User Group.
  - **"Ian"**, Sofia Low-Key Data Meetup: a new monthly data social. Only a first name is public, so no person record was made.

## 5. Before outreach

- [ ] **Check the two tier-1 first-time speakers.** Ivan Krumov and Dimitar Hadzhiev are raised by the rule from GitHub projects alone. Their location and employer are unknown.
- [ ] **Ask Paysafe whether it uses dbt.** The Paysafe speakers talk about Snowflake and Databricks, not dbt.
- [ ] **Confirm locations.** Martines Angeliev, Peter Mendev and Yordan Darakchiev have no location evidence. Peter Mendev's only talk is from 2023.
- [ ] **Find the people behind the dbt ads.** Capital.com, Nion and DataArt have no named data lead yet.
- [ ] **Treat recruiter ads with care.** People and Places, Gamito, CADABRA and Talent Hunter do not name the client.
- [ ] **Krasi Donchev is in Oslo.** Krasi Donchev co-hosts the Azure Analytics group from Oslo and is not local.

## 6. Next run

- **Sources to try first:**
  - **dev.bg:** re-run the dbt search, and add searches for "Snowflake" and "data engineer" to find more companies.
  - **Named data leads:** at Capital.com, Nion, DataArt Bulgaria, Fourth, Ocado Technology Sofia and DSK Bank.
  - **Company careers pages:** Payhawk, Paysafe, Uber Sofia, Experian and SAP Labs, which have no public ATS board.
  - **Conference agendas in a browser:** AWS Community Day Bulgaria 2025 and 2026, and the Data Saturday Sofia 2025 schedule.
  - **dbt Slack:** look for a `#local-bulgaria` or `#local-sofia` channel by hand.
  - **Community leads:** ask Margarita Naumova, PyData Sofia and the Low-Key Data Meetup whether their members use dbt.
- **Women-in-data communities not yet reachable:**
  - **Women Techmakers Sofia:** GDG Sofia is off gdg.community.dev. Find its new home.
  - **Women in Tech Bulgaria and Women in AI Bulgaria:** no working site was found.
  - **Data Science Society:** ask for women speakers from past meetups and datathons.
- **People to locate:** Ivan Krumov, Dimitar Hadzhiev, Martines Angeliev, Peter Mendev and Yordan Darakchiev.
- **LinkedIn profiles still missing:** everyone except Margarita Naumova and Denis Alekov. Run the LinkedIn pass in its own session.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `sofia/sofia_dbt_companies.json`, no chapter or enriched file yet, and the region above. Add: "There is no chapter yet, so look for co-organisers, venues and co-hosts as well as speakers. Start from the dev.bg dbt search and read each ad's location from the search card."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. 43 companies (14 on the watchlist), 22 people, 22 job postings at 20 companies. 3 tier-1 leads (Miroslav Dimitrov, Ivan Krumov, Dimitar Hadzhiev), 13 connectors. LinkedIn URLs for 2 people. No women-in-data community found with data events. |
