# Copenhagen: city notes

This file holds what is specific to Copenhagen. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Copenhagen dbt Meetup](https://www.meetup.com/copenhagen-dbt-meetup/), data in `copenhagen_dbt_companies.json`
- **Region:** the Copenhagen metro area, including Ballerup and Hørsholm. Commuter towns are local for this chapter, so Aarhus counts too. The rest of Denmark counts as outside.
- **First built:** 2026-10-01

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-01)

| | Count |
|---|---|
| Companies | 82 |
| People | 99 |
| Tier 1 leads | 21 |
| First-time speakers (publish, no talk yet) | 6 |
| Proven speakers | 72 |
| Spoke at this chapter before | 32 |
| Based in the region | 75 |
| Based elsewhere | 8 |
| Location unknown | 16 |
| With a LinkedIn profile | 45 |
| Job ads mentioning dbt | 24 |
| Past chapter meetups | 11 |
<!-- at-a-glance:end -->

## 1. Where to look in Copenhagen

### Meetups

- **Meetup data for 14 Danish data groups:** every past event was pulled. The `eventSearch` query also found the chapter's next event, which is not yet in the chapter history.
- **[Copenhagen Data Engineering](https://www.meetup.com/copenhagen-data-engineering/):** 6 events from 2025-03 to 2026-05, with 17 speakers. Its event pages name every speaker with an employer. It was the best source of Danish speakers.
- **[Databricks User Group Denmark](https://www.meetup.com/databricks-user-group-denmark/):** the same detail, and one dbt talk (Vipps MobilePay, 2025-09).
- **[Snowflake User Group Denmark](https://usergroups.snowflake.com/denmark/):** its event pages are rendered on the server, so a fetch returns the speakers and organisers.
- **[PyData Copenhagen](https://www.meetup.com/pydata-copenhagen/):** mostly machine learning and LLM talks.

### GitHub

- **[GitHub user search](https://github.com/search?q=location%3ACopenhagen+dbt&type=users):** Copenhagen or Denmark in the bio or location, then each profile's repositories checked for dbt in the name. About 130 profiles were scanned and 11 people found. It found the only real first-time speakers, including an open-source dbt docs tool on PyPI.

### Vendor stories and newsletters

- **[SYNQ customer stories](https://www.synq.io/customers):** the [Lunar](https://www.synq.io/customers/lunar) case (about 1,500 dbt models) and Better Collective.
- **[Mikkel Dengsøe's Substack](https://mikkeldengsoe.substack.com/archive):** posts from 2025 on dbt with AI.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[TechWomen Cph](https://www.meetup.com/techwomen-cph/):** the only active women-in-data group in Copenhagen, with 1,154 members. It runs panels with data leaders, and a 2026-09 masterclass with Women in Data & Analytics. The topics are mostly AI and careers. The first build took 8 people from it. This pass added Corie Tilly, a digital analytics engineer on the [October 2025 panel](https://www.meetup.com/techwomen-cph/events/311082320/), and 5 organisers and hosts as connectors, led by Meriem Manouchi.
- **[Women Techmakers Copenhagen](https://www.meetup.com/wtm-copenhagen/):** 887 members, but no events since November 2023 and no data talks. Its organisers, Aurora Melchor and Sherry List, are connectors.
- **Also ask:** Meriem Manouchi for data and analytics engineering speakers from TechWomen Cph.

### Job ads

- **[Jobindex search for dbt](https://www.jobindex.dk/jobsoegning?q=dbt):** 12 ads. The results embed a JSON list of ads, but each ad links off-site. Only [Dagrofa's ad](https://www.jobindex.dk/vis-job/r14003203) visibly says dbt.
- **[TheirStack](https://theirstack.com/en/technology/dbt/dk):** it shows 10 of the 116 Danish companies it lists as using dbt.
- **LinkedIn search results:** 6 people came from posts about dbt work or dbt hiring.
- **[thehub.io search API](https://thehub.io/api/v2/jobsandfeatured?search=dbt&countryCode=DK):** 10 Danish ads, and each ad page carries the full text. It added Skatteguiden (Snowflake, Dagster and dbt), Landfolk in Aarhus, Dreamdata and TimeLog.
- **Jobindex ads on Emply:** the [LB Forsikring ad](https://lbforsikring.career.emply.com/ad/data-engineer-med-solide-dbt-og-snowflake-kompetencer/9ralma/da) asks for solid dbt and Snowflake experience.
- **Company job boards:** the Greenhouse, Lever and Ashby boards of about 75 Danish employers. Only Pleo and Too Good To Go had a Copenhagen ad that says dbt.
- **[dbt Labs case studies](https://www.getdbt.com/case-studies/mcdonalds-nordics):** McDonald's Nordics (Food Folk) runs Data Vault on dbt Cloud. The page does not say which office the data team works from.
- **GitHub organisation repositories:** Pleo publishes [a fork of dbt-checkpoint](https://github.com/pleo-io/dbt-checkpoint-pleo) with its own dbt checks.

### Chapter history and locations

- **Chapter history:** every named speaker in `../enriched/copenhagen-dbt-meetup.json` was added, with their talk as evidence. That covers 11 events, from 2023-02-22 to 2026-09-16. 32 people in the file have spoken at the chapter.
- **Next event:** [vol. 11](https://www.meetup.com/copenhagen-dbt-meetup/events/316677743/) on 2026-10-21. Its three speakers are in the file as leads, with a note saying they are booked.
- **In-person chapter talks:** an in-person talk or host role at a chapter event since 2024-10, at an employer with a Copenhagen office, gave 9 medium-confidence calls.
- **Sessionize:** a Sessionize page placed Kshitij Aranke in London.
- **Meetup member profiles:** profiles tied to a person placed Johan Baltzar in Stockholm and Ernesto Ongaro in Dublin. Each member had joined, by RSVP, the Stockholm dbt meetup where that person spoke.
- **LinkedIn search results:** 10 people searched and 2 placed, Petr Janda in Copenhagen and Stephen O'Kennedy in Dublin.
- **Other city files:** Erica Louie, Hicham Babahmed and Benoit Perigaud are placed from the same person's record in another city's file.

## 2. What didn't work here

- **Web search:** ran out after about 15 calls. Page fetches, the Meetup data and the GitHub user search covered the rest.
- **Medium feeds:** HTTP 429 (too many requests) from the start, including Pleo, Lunar, Trustpilot and Too Good To Go. No company-blog authors were found.
- **[Intellishore insights](https://intellishore.dk/insights/) and the [LEAP website](https://leap-consulting.dk/):** no dbt content.
- **[Fabric & Power BI User Group Denmark](https://www.meetup.com/denmark-powerbi-user-group/):** mostly online speakers from other countries.
- **[Analytics Pioneers Copenhagen](https://www.meetup.com/analytics-pioneers-copenhagen/):** online trainings by a German agency.
- **[R-Ladies Copenhagen](https://www.meetup.com/rladies-copenhagen/) and [Copenhagen Women in Machine Learning & Data Science](https://www.meetup.com/copenhagen-women-in-machine-learning-and-data-science/):** no events since 2019.
- **Other women-in-data networks:** [Ascend - Women in Data & Analytics](https://www.meetup.com/women-in-data-analytics/) shows up in a Copenhagen search, but it meets at Wise in London. The [GDG Copenhagen](https://gdg.community.dev/gdg-copenhagen/) events API (`event_slim/for_chapter/1018`) has no women-in-tech or data events since 2023. pyladies.com lists no Danish chapter. She Loves Data lists no Copenhagen events. Women Who Code closed in 2024. Meetup's group search found no WiDS, Women in Big Data or Girls in Tech group.
- **[thehub.io](https://thehub.io/jobs?search=dbt) search page:** it loads results in the browser, so a fetch saw only 3 ads from outside Denmark. Use the search API in section 1 instead.
- **HN Who is hiring:** no Danish ad since 2023 mentions dbt.
- **Workable boards:** Ageras, Keepit, LEO Pharma, Qarma and Monta had no open ads, so their Copenhagen presence is still not confirmed. ZeroNorth, TDC Net, Steep and Mrs Wordsmith have no Greenhouse, Lever, Ashby, Workable, Recruitee or SmartRecruiters board.
- **GitHub code search:** it hit the shared rate limit. Listing each organisation's repositories found dbt only at Pleo.
- **Jobindex ads:** they link off-site, so the dbt wording was visible for one ad only.
- **[dbt Summit speakers page](https://www.getdbt.com/dbt-summit/speakers):** it now shows only the 2027 waitlist.
- **GitHub learning repositories:** a "dbt-learn" or "dbt-training" repo is not published content. Those people are recorded with no public content.

## 3. Companies looked at

- **LEAP organises and hosts the chapter.** LEAP also co-organises the Snowflake User Group Denmark.
- **Proven speakers outnumber first-time speakers.** Most Danish leads are proven speakers from Databricks, Snowflake and data engineering meetups, where dbt rarely appears in titles.
- **Aarhus employers count as local.** Several speakers at Databricks and Snowflake user group events work in Aarhus, so they are marked in the region.
- **dbt Labs staff are labelled.** Seven past chapter speakers work at dbt Labs.

<!-- companies:start -->
81 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (31)</summary>

Ageras (local presence not confirmed), Better Collective, Dagrofa, dbt Labs (local presence not confirmed), DUOS, group.one, Intellishore, Keepit (local presence not confirmed), Landfolk, LB Forsikring, LEAP, LEGO Group, LEO Pharma (local presence not confirmed), Lunar, Lundbeck, McDonald's Nordics (Food Folk) (local presence not confirmed), Mrs Wordsmith (local presence not confirmed), Novo Holdings, Omni (local presence not confirmed), Pas Normal Studios, Pleo, Qarma (local presence not confirmed), Skatteguiden, Steep (local presence not confirmed), SYNQ, TDC Net (local presence not confirmed), TooGoodToGo, VELUX, Veo Technologies, Vipps MobilePay, ZeroNorth (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (24)</summary>

7N, Ascendis Pharma, BESTSELLER, Coelacanth Company (local presence not confirmed), DK Company (local presence not confirmed), Dreamdata, Flatpay, Genmab, GoWish, Hamamatsu Photonics, HelloFresh (local presence not confirmed), Heyra, Inspari, Knowit (local presence not confirmed), Quiver, ROCKWOOL Group, Santander Nordics (local presence not confirmed), Saxo Bank, Scania Danmark (local presence not confirmed), Snowflake, Spirii, TimeLog, Trustpilot, Udviklings- og Forenklingsstyrelsen (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (21)</summary>

3Shape, ADAMATICS (local presence not confirmed), Alipes (local presence not confirmed), cloud2 (local presence not confirmed), COWI, Devoteam, DSV, Electricity Maps, Everllence (local presence not confirmed), Implement Consulting Group, Maersk, Milestone Systems (local presence not confirmed), Nordea, Nordea Asset Management, Norlys, SimCorp, Sparekassen Sjælland (local presence not confirmed), Topsøe, twoday, Unity, Ørsted

</details>

<details><summary><b>Uses a different stack</b> (5)</summary>

Copenhagen Data Engineering, Employer not identified (local presence not confirmed), Monta (local presence not confirmed), TechWomen Cph, Women Techmakers Copenhagen

</details>

<details><summary><b>Other sources checked</b> (30)</summary>

- Local chapter history (enriched/copenhagen-dbt-meetup.json): `enriched/copenhagen-dbt-meetup.json`
- [Copenhagen dbt Meetup vol. 11 (upcoming)](https://www.meetup.com/copenhagen-dbt-meetup/events/316677743/)
- [Copenhagen Data Engineering (meetup.com)](https://www.meetup.com/copenhagen-data-engineering/)
- [Databricks User Group Denmark](https://www.meetup.com/databricks-user-group-denmark/)
- [Snowflake User Group Denmark](https://usergroups.snowflake.com/denmark/)
- [PyData Copenhagen](https://www.meetup.com/pydata-copenhagen/)
- [TechWomen Cph](https://www.meetup.com/techwomen-cph/)
- [R-Ladies Copenhagen](https://www.meetup.com/rladies-copenhagen/) (nothing useful)
- [Copenhagen Women in Machine Learning & Data Science](https://www.meetup.com/copenhagen-women-in-machine-learning-and-data-science/) (nothing useful)
- [Fabric & Power BI User Group Denmark](https://www.meetup.com/denmark-powerbi-user-group/) (nothing useful)
- [Analytics Pioneers Copenhagen](https://www.meetup.com/analytics-pioneers-copenhagen/) (nothing useful)
- [SYNQ customer stories](https://www.synq.io/customers)
- [Mikkel Dengsøe Substack](https://mikkeldengsoe.substack.com/archive)
- [Jobindex search 'dbt'](https://www.jobindex.dk/jobsoegning?q=dbt)
- [TheirStack companies using dbt in Denmark](https://theirstack.com/en/technology/dbt/dk)
- [GitHub user search (dbt / analytics engineer, Denmark)](https://github.com/search?q=location%3ACopenhagen+dbt&type=users)
- [dbt Summit 2026 speakers](https://www.getdbt.com/dbt-summit/speakers) (nothing useful)
- [Medium publication feeds (Pleo, Lunar, Trustpilot, Too Good To Go and others)](https://medium.com/feed/pleo) (nothing useful)
- [thehub.io dbt search](https://thehub.io/jobs?search=dbt) (nothing useful)
- [Intellishore insights](https://intellishore.dk/insights/) (nothing useful)
- [LEAP website](https://leap-consulting.dk/) (nothing useful)
- [Meetup gql2 groupSearch near Copenhagen](https://www.meetup.com/gql2)
- [Women Techmakers Copenhagen (Meetup gql2)](https://www.meetup.com/wtm-copenhagen/)
- [Ascend - Women in Data & Analytics (Meetup gql2)](https://www.meetup.com/women-in-data-analytics/) (nothing useful)
- [GDG Copenhagen events API (Women Techmakers)](https://gdg.community.dev/api/event_slim/for_chapter/1018/) (nothing useful)
- [PyLadies chapter list](https://pyladies.com/locations/) (nothing useful)
- [She Loves Data](https://www.shelovesdata.com/) (nothing useful)
- [Women Who Code](https://womenwhocode.com/) (nothing useful)
- [thehub.io search API](https://thehub.io/api/v2/jobsandfeatured?search=dbt&countryCode=DK)
- [HN Who is hiring (Algolia)](https://hn.algolia.com/api/v1/search?query=dbt&tags=comment) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
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
  - **Martin Birk Andreasen (LEAP):** co-organises the [Snowflake User Group Denmark](https://usergroups.snowflake.com/denmark/).
  - **Kathrine Sofie Rasmussen (LEAP):** part of the chapter's organising team.
  - **Rune Bendix Wittchen (Devoteam) and Sukru Gursoy (Snowflake):** lead the Snowflake User Group Denmark.
  - **Dilovan Celik:** organiser of [Copenhagen Data Engineering](https://www.meetup.com/copenhagen-data-engineering/), with 1,483 members.
  - **Anders Bogsnes (Nordea Asset Management):** organiser of [PyData Copenhagen](https://www.meetup.com/pydata-copenhagen/).
  - **Farzad Bonabi (twoday):** runs the Databricks User Group Denmark meetups hosted at twoday.

## 5. Before outreach

- [ ] **Check the "Denmark" calls.** 4 people marked in the region give only "Denmark" as their city.
- [ ] **Check most "in region" calls.** Only 10 of the 71 people marked in the region have a location note with evidence. The rest were placed from an event city or an employer's office during research.
- [ ] **Don't invite the vol. 11 speakers for that event.** Rasmus Rottwitt, Ernesto Ongaro and Hicham Babahmed speak on 2026-10-21.
- [ ] **dbt Labs staff are labelled.** Benoit Perigaud, Nina Anderson and Rachel Ryan are tier 1 and work there. They can speak, but check the line-up has practitioners first.
- [ ] **Check people who have moved:**
  - Kilian Tscherny spoke at vol. 6 for Skatteguiden and now leads data engineering at Heyra.
  - Henrik Varmer is now Head of Data Engineering at VELUX.
  - Stephen O'Kennedy's search result names Kinertic, not ZeroNorth.
  - Van Bui has a second GitHub account that names Ageras.
- [ ] **Treat Jobindex ads as medium.** Only Dagrofa's ad visibly says dbt.
- [ ] **Check one weak location.** Martha Scheffler is tier 1. Qarma's Danish office is in Aarhus, which counts as local, but Martha Scheffler's own location is unconfirmed.

## 6. Next run

- **Sources to try first:**
  - **Meetups:** new events from Copenhagen Data Engineering, Databricks User Group Denmark, Snowflake User Group Denmark and TechWomen Cph.
  - **GitHub:** re-run the user search for dbt repos.
  - **Company blogs:** retry the Pleo, Lunar, Trustpilot and Too Good To Go feeds before the Medium rate limit starts.
  - **Job ads:** open the Jobindex ads one by one to read the dbt wording. Try thehub.io in a browser.
  - **Women-in-data:** ask Meriem Manouchi at TechWomen Cph for introductions to data and analytics engineering speakers. Find the Women in Data & Analytics group that co-ran the 2026-09 masterclass; it has no Meetup page. Try WiDS through its community site in the browser.
  - **Chapter history:** after 2026-10-21, refresh the chapter history so vol. 11 is included.
  - **dbt Slack:** check the [#local-denmark](https://slack.getdbt.com/) channel by hand.
- **People to locate:** 12 people have no known location, mostly chapter speakers and dbt Labs staff. The Snowflake User Group Denmark pages link many LinkedIn profiles, so find those people through search results.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `copenhagen/copenhagen_dbt_companies.json`, the Copenhagen dbt Meetup, `../enriched/copenhagen-dbt-meetup.json` and the region the Copenhagen metro area, with Aarhus counted as local.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-01 | 1 | First build. Meetup data for 14 Danish data groups, Snowflake User Group Denmark, SYNQ customer stories, a Jobindex dbt search, TheirStack and a GitHub user search, plus chapter history. 90 people at 73 companies, 32 of them past chapter speakers. 11 job ads. Web search ran out after about 15 calls. |
| 2026-10-01 | 1 | Location pass from public pages: in-person chapter talks, Sessionize and tied Meetup member profiles. 12 people placed, 9 in Copenhagen and 3 elsewhere. |
| 2026-10-01 | 1 | LinkedIn pass from search results: 10 people searched, 1 placed in Copenhagen and 1 in Dublin. With the location pass, 14 people placed and 15 still unknown. |
| 2026-10-01 | 2 | Women-in-data pass over TechWomen Cph, Women Techmakers Copenhagen and other networks. 9 people added: 1 digital analytics engineer and 8 organisers and hosts as connectors. |
| 2026-10-01 | 3 | Company pass from the thehub.io API, Jobindex, company job boards, dbt Labs case studies and GitHub. 6 companies added: LB Forsikring, Skatteguiden and Landfolk (strong), Dreamdata and TimeLog (medium), and McDonald's Nordics (strong, office not confirmed). Intellishore's Copenhagen presence is confirmed. 13 job ads added, now 24. |
