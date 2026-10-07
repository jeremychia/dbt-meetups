# Barcelona: city notes

This file holds what is specific to Barcelona. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Barcelona dbt Meetup](https://www.meetup.com/barcelona-dbt-meetup/), data in `barcelona_dbt_companies.json`
- **Region:** Barcelona and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 94 |
| People | 176 |
| Tier 1 leads | 11 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 76 |
| Spoke at this chapter before | 34 |
| Based in the region | 124 |
| Based elsewhere | 4 |
| Location unknown | 48 |
| With a LinkedIn profile | 85 |
| Job ads mentioning dbt | 9 |
| Past chapter meetups | 14 |
<!-- at-a-glance:end -->

## 1. Where to look in Barcelona

- **Chapter history:** past speakers come from `enriched/barcelona-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (41.3874, 2.1686).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
93 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (26)</summary>

Barcelona Supercomputing Center (local presence not confirmed), Caravelo, Carta Europe (local presence not confirmed), dbt (local presence not confirmed), dbt Labs (local presence not confirmed), Entravision, Euno (local presence not confirmed), Factorial, IFCO (local presence not confirmed), Infinite Lambda (local presence not confirmed), Landbot (local presence not confirmed), Lifull Connect (local presence not confirmed), Lovys (local presence not confirmed), Metaloop (local presence not confirmed), Omni Analytics (local presence not confirmed), Payfit (local presence not confirmed), Scopely (local presence not confirmed), Shalion (local presence not confirmed), Spaulding Ridge (local presence not confirmed), Synq (local presence not confirmed), Tamarind Intelligence, Tier Mobility (local presence not confirmed), Tous (local presence not confirmed), TravelPerk (local presence not confirmed), Wallbox (local presence not confirmed), Wallbox Chargers (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (4)</summary>

Robert Walters Spain (local presence not confirmed), Splio, TRG Consulting (Tenth Revolution) (local presence not confirmed), WhyHireWrong

</details>

<details><summary><b>Not verified</b> (62)</summary>

Adevinta (local presence not confirmed), Aimpoint Digital (local presence not confirmed), ALOHAS2020 (local presence not confirmed), Altostratus Cloud Consulting (local presence not confirmed), Amenitiz (local presence not confirmed), AstraZeneca (local presence not confirmed), Aubay Spain (local presence not confirmed), BASE Life Science (local presence not confirmed), BaseTIS (local presence not confirmed), Bluetab, an IBM Company (local presence not confirmed), Boehringer Ingelheim (local presence not confirmed), Boehringer-Ingelheim (local presence not confirmed), Boerhinger Ingelheim (local presence not confirmed), CIRSA (local presence not confirmed), Coalesce.IO (local presence not confirmed), ContentSquare (local presence not confirmed), Data Scientist (local presence not confirmed), Data Warrior LLC (local presence not confirmed), DataversoSolutions (local presence not confirmed), desidedatum (local presence not confirmed), Digital Legends (local presence not confirmed), Digitl Cloud GmbH (local presence not confirmed), ERNI (local presence not confirmed), Exoticca (local presence not confirmed), Freelancer (local presence not confirmed), Glovo, Glovo @deliveryhero (local presence not confirmed), Google Cloud (local presence not confirmed), HP (local presence not confirmed), Hub4Retail (local presence not confirmed), InAtlas (local presence not confirmed), International Airlines Group (local presence not confirmed), isolutionsag (local presence not confirmed), kraken-tech (local presence not confirmed), Lemonade Software Development SL (local presence not confirmed), mad-collective (local presence not confirmed), MediaMarktSaturn (local presence not confirmed), MIPT, Harbour.Space University (local presence not confirmed), regaeteio (local presence not confirmed), Relato (local presence not confirmed), Restb.ai (local presence not confirmed), Roche Diagnostics Spain (local presence not confirmed), RubyLabs (local presence not confirmed), Sanofi (local presence not confirmed), SDG Group (local presence not confirmed), seatcode (local presence not confirmed), Seidor (local presence not confirmed), Senior Data Analyst (local presence not confirmed), SIRIS Academic (local presence not confirmed), Snowflake (local presence not confirmed), SqlDBM (local presence not confirmed), Symphony Solutions (local presence not confirmed), T2C (local presence not confirmed), Telefónica Digital, B2B Market Intelligence (local presence not confirmed), Trakken Web Services GmbH (local presence not confirmed), Tripledot (local presence not confirmed), Universidad Francisco de Vitoria (local presence not confirmed), Universitat Politècnica de Catalunya, University of Barcelona (local presence not confirmed), UPC (local presence not confirmed), Women Tech Makers Barcelona (local presence not confirmed), Zurich - Banc Sabadell (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

Barcelona Data Engineering Community

</details>

<details><summary><b>Other sources checked</b> (9)</summary>

- [jobfluent Barcelona analytics engineer pages](https://jobfluent.com/jobs/senior-analytics-engineer-barcelona-c91957)
- [Factorial careers](https://careers.factorialhr.com/job_posting/analytics-engineer-269903)
- [Robert Walters Spain data jobs](https://www.robertwalters.es/ittelecomunicaciones/jobs/dataanalytics/1897573-data-platform-engineer.html)
- [StudentJob Barcelona](https://www.studentjob.es/ofertas/5059012-data-engineer-en-barcelona)
- [Built In Glovo roles](https://builtin.com/job/senior-analytics-engineer-quick-commerce/7106696) (nothing useful)
- [Snowflake Barcelona user group events](https://usergroups.snowflake.com/barcelona) (nothing useful)
- [techbarcelona DataBeers](https://www.techbarcelona.com/en/event/18th-databeers-barcelona/) (nothing useful)
- [WiDS Barcelona 2026](https://websk.upc.edu/wids-2026-en/)
- [dbt Barcelona meetup events](https://www.meetup.com/es-es/barcelona-dbt-meetup/events/313908423/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **Connector and speaker:** Riddhi Kedia organises the Barcelona Data Engineering Community and has spoken there on dbt.

## 5. Before outreach

- [ ] Check speakers whose location is unverified: a talk at a local group does not show where someone lives.

## 6. Next run

- **Sources to try first:** a research run with the [central replication prompt](../research/README.md#9-replication-prompt) for companies, dbt job ads and first-time speakers.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-06 | 1 | First build from the chapter history. |
| 2026-10-06 | 3 | Research run: 11 companies, 10 dbt job ads (Factorial, Tamarind Intelligence and others) and 3 people, including Riddhi Kedia of the Barcelona Data Engineering Community. |
