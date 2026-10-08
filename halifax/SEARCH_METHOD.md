# Halifax: city notes

This file holds what is specific to Halifax. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Halifax dbt Meetup](https://www.meetup.com/halifax-dbt-meetup/), data in `halifax_dbt_companies.json`
- **Region:** Halifax and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 18 |
| People | 29 |
| Tier 1 leads | 0 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 12 |
| Spoke at this chapter before | 4 |
| Based in the region | 19 |
| Based elsewhere | 1 |
| Location unknown | 9 |
| With a LinkedIn profile | 12 |
| Job ads mentioning dbt | 2 |
| Past chapter meetups | 5 |
<!-- at-a-glance:end -->

## 1. Where to look in Halifax

- **Chapter history:** past speakers come from `enriched/halifax-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (44.6488, -63.5752).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
17 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (4)</summary>

Analytics Engineer (local presence not confirmed), Brooklyn Data Co (local presence not confirmed), Modern (modern.inc) (local presence not confirmed), Vetsource (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (1)</summary>

Dalhousie University

</details>

<details><summary><b>Not verified</b> (11)</summary>

BDO (local presence not confirmed), Dalhousie University, NS, Canada (local presence not confirmed), Data Analyst || Business Intelligence Analyst (local presence not confirmed), databricks (local presence not confirmed), larixsw (local presence not confirmed), Nova Scotia Health (local presence not confirmed), Outshine (local presence not confirmed), Royal Bank of Canada (RBC), Saint Mary's University (local presence not confirmed), Skills For Hire Atlantic (local presence not confirmed), tem (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

Halifax Women in Machine Learning & Data Science (WiMLDS)

</details>

<details><summary><b>Other sources checked</b> (6)</summary>

- [Halifax Databricks User Group](https://usergroups.databricks.com/halifax-databricks-user-group/) (nothing useful)
- [WiMLDS Halifax chapter page](https://wimlds.org/?p=4156)
- [Digital Nova Scotia job portal](https://digitalnovascotia.com/job-posts) (nothing useful)
- [CareerBeacon RBC Senior Data Engineer GFT Halifax](https://www.careerbeacon.com/en/job-4/3295279/rbc/senior-data-engineer-gft-halifax)
- [NTT DATA Halifax Data Engineer](https://careers-inc.nttdata.com/job/Halifax-Data-Engineer-NS/1253635400) (nothing useful)
- [Wellfound Dalhousie Junior Data Engineer](https://wellfound.com/jobs/4645312-junior-data-engineer) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 2 companies, 2 dbt job ads and 1 people, no first-time speakers. |
