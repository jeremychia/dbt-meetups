# Helsinki: city notes

This file holds what is specific to Helsinki. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Helsinki dbt Meetup](https://www.meetup.com/helsinki-dbt-meetup/), data in `helsinki_dbt_companies.json`
- **Region:** Helsinki and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 58 |
| People | 111 |
| Tier 1 leads | 10 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 67 |
| Spoke at this chapter before | 17 |
| Based in the region | 70 |
| Based elsewhere | 0 |
| Location unknown | 41 |
| With a LinkedIn profile | 13 |
| Job ads mentioning dbt | 2 |
| Past chapter meetups | 6 |
<!-- at-a-glance:end -->

## 1. Where to look in Helsinki

- **Chapter history:** past speakers come from `enriched/helsinki-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (60.1699, 24.9384).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
57 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (18)</summary>

Academic Work, Aiven, Anora (local presence not confirmed), Breakout Labs (local presence not confirmed), Databricks (local presence not confirmed), dbt Labs (local presence not confirmed), Finnair (local presence not confirmed), Kaito Insight (local presence not confirmed), Nordea, reconfigured.io (local presence not confirmed), Smartly.io (local presence not confirmed), SOK (local presence not confirmed), Solita Oy (local presence not confirmed), Supercell (local presence not confirmed), Supermetrics (local presence not confirmed), SYNQ (local presence not confirmed), Twoday, UPM (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (4)</summary>

KONE (local presence not confirmed), Recordly (local presence not confirmed), Tietoevry (local presence not confirmed), Wolt (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (33)</summary>

adikteev (local presence not confirmed), ALM Partners (local presence not confirmed), Argonteq (local presence not confirmed), Biztory (local presence not confirmed), EKAI (local presence not confirmed), Enfuce (local presence not confirmed), Etlia Oy, Fennia (local presence not confirmed), Fiskars Group (local presence not confirmed), HappySignals Oy (local presence not confirmed), Inmeta (local presence not confirmed), Karshk Global Consultants Pvt Ltd (local presence not confirmed), Knowit (local presence not confirmed), Knowit Solutions Oy (local presence not confirmed), Kynsilehto Consulting (local presence not confirmed), LTI (local presence not confirmed), Mainframe Industries (local presence not confirmed), Metacore (local presence not confirmed), Metso (local presence not confirmed), Neste (local presence not confirmed), Nortal (local presence not confirmed), Orion Corporation (local presence not confirmed), Salesforce (local presence not confirmed), Sema4.ai (local presence not confirmed), Semantic Hub (local presence not confirmed), Snowflake (local presence not confirmed), snowharbor (local presence not confirmed), True Diamonds Analytics (local presence not confirmed), University of Oulu (local presence not confirmed), VR (local presence not confirmed), Yleisradio (local presence not confirmed), YousicianGit (local presence not confirmed), Zero (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (2)</summary>

DataTribe Collective, R-Ladies Helsinki (local presence not confirmed)

</details>

<details><summary><b>Other sources checked</b> (12)</summary>

- [duunitori.fi dbt Helsinki search](https://duunitori.fi/tyopaikat?haku=dbt&alue=helsinki) (nothing useful)
- [duunitori.fi Academic Work dbt ad](https://duunitori.fi/tyopaikat/tyo/data-build-tool-developers-helsinki-or-tampere-sasca-20328264)
- [Nordea careers](https://careers.nordea.com/job/Helsinki-Data-Engineer-to-Debt-Collection-Program-in-Nordea-Finance-00500/1389791233/)
- [theirstack.com dbt Finland](https://theirstack.com/hi/technology/dbt/fi)
- [Helsinki Data Week 2026 speakers](https://www.helsinkidataweek.fi/speakers)
- [Snowflake Finland UG April 2026](https://usergroups.snowflake.com/events/details/snowflake-helsinki-presents-snowflake-finland-user-group-helsinki-april-2026-at-twoday/)
- [Snowflake Finland UG September 2026](https://usergroups.snowflake.com/events/details/snowflake-helsinki-presents-snowflake-finland-user-group-helsinki-september-2026-at-etlia/)
- [Snowflake Finland UG February 2026](https://usergroups.snowflake.com/events/details/snowflake-helsinki-presents-snowflake-finland-user-group-helsinki-february-2026-at-epicenter/)
- [Solita dbt Premier Partner news](https://www.solita.fi/news/solita-becomes-the-first-dbt-labs-premier-consulting-partner-in-the-nordics)
- [PyData Helsinki Feb 2026](https://hackers.pub/@pydata_helsinki@fosstodon.org/019c85fe-d6b6-71ce-a890-d247a0331748/quotes) (nothing useful)
- [DataTribe Collective substack](https://substack.com/@datatribe)
- [Aiven analytics ad on duunitori](https://duunitori.fi/tyopaikat/tyo/software-engineer-analytics-scsom-20377060) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **Routes in:** the [Snowflake Finland User Group](https://usergroups.snowflake.com/events/details/snowflake-helsinki-presents-snowflake-finland-user-group-helsinki-september-2026-at-etlia/) and [DataTribe Collective](https://substack.com/@datatribe), a community for new speakers.

## 5. Before outreach

- [ ] Check speakers whose location is unverified: a talk at a local group does not show where someone lives.

## 6. Next run

- **Sources to try first:** a research run with the [central replication prompt](../research/README.md#9-replication-prompt) for companies, dbt job ads and first-time speakers.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-06 | 1 | First build from the chapter history. |
| 2026-10-06 | 3 | Research run: 9 new companies, 2 closed dbt job ads and 6 people, mostly organisers. |
