# Denver: city notes

This file holds what is specific to Denver. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Denver dbt Meetup](https://www.meetup.com/denver-dbt-meetup/), data in `denver_dbt_companies.json`
- **Region:** Denver and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 81 |
| People | 128 |
| Tier 1 leads | 0 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 29 |
| Spoke at this chapter before | 4 |
| Based in the region | 115 |
| Based elsewhere | 0 |
| Location unknown | 13 |
| With a LinkedIn profile | 56 |
| Job ads mentioning dbt | 7 |
| Past chapter meetups | 4 |
<!-- at-a-glance:end -->

## 1. Where to look in Denver

- **Chapter history:** past speakers come from `enriched/denver-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (39.7392, -104.9903).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
80 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (7)</summary>

Abnormal Security (local presence not confirmed), dbt Labs (local presence not confirmed), Litera, Nasdaq (local presence not confirmed), Stytch (local presence not confirmed), Summit Utilities, SumUp

</details>

<details><summary><b>Some dbt signal</b> (3)</summary>

Contentful, Neshant Technologies (local presence not confirmed), Slalom

</details>

<details><summary><b>Not verified</b> (68)</summary>

Armstrong Solutions Inc. (local presence not confirmed), Ascend Analytics (local presence not confirmed), Axon (local presence not confirmed), Baseten (local presence not confirmed), Blankfactor (local presence not confirmed), Bright Victory (local presence not confirmed), brooklyn-data (local presence not confirmed), C U Denver (local presence not confirmed), Candid Health (local presence not confirmed), Centura Health (local presence not confirmed), centurylink (local presence not confirmed), Charles Schwab (local presence not confirmed), Charter Communications (local presence not confirmed), Choozle (local presence not confirmed), Cipher Mining (local presence not confirmed), Clear Choice (local presence not confirmed), Cloud Data Consulting (local presence not confirmed), Cloud Data Consulting, Inc. (local presence not confirmed), Colorado Department of Education (local presence not confirmed), Concentrix (local presence not confirmed), Confluent (local presence not confirmed), Connect for Health Colorado (C4HCO) (local presence not confirmed), CU Medicine (local presence not confirmed), Curative (local presence not confirmed), DataTecnica (local presence not confirmed), Denver Broncos (local presence not confirmed), Dispatch Health (local presence not confirmed), Evolve Vacation Rental (local presence not confirmed), Ex-Oracle (local presence not confirmed), Gemini (local presence not confirmed), guzman-energy (local presence not confirmed), homebotapp (local presence not confirmed), Housecall Pro (local presence not confirmed), i4DM (local presence not confirmed), Ibotta (local presence not confirmed), Insight LLC (local presence not confirmed), Jobot Consulting (local presence not confirmed), keith-forpublic, @snowflake-labs, @snowflakedb (local presence not confirmed), L3Harris (local presence not confirmed), LaunchCoderGirlSTL (local presence not confirmed), marketingmaven.llc (local presence not confirmed), Mashey LLC (local presence not confirmed), Mercury Insurance (local presence not confirmed), Messari (local presence not confirmed), Natera (local presence not confirmed), Navajo Inc. (local presence not confirmed), NSF | UCAR | NCAR | CISL (local presence not confirmed), Optum (local presence not confirmed), Pratt & Whitney (local presence not confirmed), Salesforce (local presence not confirmed), SCANDATA LLC (local presence not confirmed), Scopic Analytics International (local presence not confirmed), Shane Co. (local presence not confirmed), Snowflake (local presence not confirmed), snowflakecorp (local presence not confirmed), spencernemer.com (local presence not confirmed), splunk (local presence not confirmed), spotify @markkoh (local presence not confirmed), Studied at DU (local presence not confirmed), TBA (local presence not confirmed), techstars (local presence not confirmed), The Motley Fool (local presence not confirmed), TJH Data (local presence not confirmed), University of Chicago (local presence not confirmed), University of Colorado Denver (local presence not confirmed), Univesity of Colorado Boulder (local presence not confirmed), W. Spann Systems Consulting (local presence not confirmed), Weber Tech (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (2)</summary>

R-Ladies Denver, Women in Data Denver

</details>

<details><summary><b>Other sources checked</b> (7)</summary>

- [Built In Colorado job pages (analytics engineer, dbt data engineer)](https://www.builtincolorado.com/jobs/data-analytics/other)
- [Built In Colorado hybrid data and analytics listing](https://www.builtincolorado.com/jobs/hybrid/data-analytics) (nothing useful)
- [Denver Dev Day 2026 sessionize page](https://sessionize.com/denver-dev-day-2026) (nothing useful)
- [Snowflake Denver user group event, March 2025](https://www.snowflake.com/event/comm-denver-user-group-2025)
- [Women in Data Denver fundraiser page](https://givebutter.com/1000womenindata/amandalong2) (nothing useful)
- [getdbt.com case studies, Colorado search](https://www.getdbt.com/resources) (nothing useful)
- [DenverBricks announcement on Databricks community](https://community.databricks.com/t5/denverbricks/announcing-denverbricks-the-new-denver-databricks-user-group/m-p/132503/highlight/true) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

To fill after the first research run.

## 5. Before outreach

- [ ] Check speakers whose location is unverified: a talk at a local group does not show where someone lives.

## 6. Next run

- **Sources to try first:** a research run with the [central replication prompt](../research/README.md#9-replication-prompt) for companies, dbt job ads and first-time speakers.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-06 | 1 | First build from the chapter history. |
| 2026-10-06 | 3 | Research run: 9 companies, 7 dbt job ads and 1 people, no first-time speakers. |
