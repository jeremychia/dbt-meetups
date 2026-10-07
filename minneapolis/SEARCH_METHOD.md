# Minneapolis: city notes

This file holds what is specific to Minneapolis. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Minneapolis dbt Meetup](https://www.meetup.com/minneapolis-dbt-meetup/), data in `minneapolis_dbt_companies.json`
- **Region:** Minneapolis and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 42 |
| People | 89 |
| Tier 1 leads | 1 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 33 |
| Spoke at this chapter before | 1 |
| Based in the region | 85 |
| Based elsewhere | 0 |
| Location unknown | 4 |
| With a LinkedIn profile | 25 |
| Job ads mentioning dbt | 7 |
| Past chapter meetups | 3 |
<!-- at-a-glance:end -->

## 1. Where to look in Minneapolis

- **Chapter history:** past speakers come from `enriched/minneapolis-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (44.9778, -93.265).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
41 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (5)</summary>

Airbyte (local presence not confirmed), dbt Labs (local presence not confirmed), Eve (local presence not confirmed), Horizon3.ai (local presence not confirmed), Insight Global

</details>

<details><summary><b>Some dbt signal</b> (4)</summary>

Affirm (local presence not confirmed), Airbnb (local presence not confirmed), Jellyfish (local presence not confirmed), Toast (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (31)</summary>

3M (local presence not confirmed), Actively searching Data Scientist/Analyst job (local presence not confirmed), Astrin Biosciences Inc. (local presence not confirmed), Cargill (local presence not confirmed), Carlson School of Management (local presence not confirmed), Carlson School of Management - UMN (local presence not confirmed), Carlson Wagonlit Travels (local presence not confirmed), Centro Benefits (local presence not confirmed), CH Robinson (local presence not confirmed), Coloplast (local presence not confirmed), CWT (Carlson wagonlit Travel) (local presence not confirmed), Deloitte (local presence not confirmed), EVEREVE (local presence not confirmed), HealthPartners (local presence not confirmed), Huntington Bank (local presence not confirmed), Incite.ag (local presence not confirmed), Mayo Clinic (local presence not confirmed), MS in Business Analytics in UMN (local presence not confirmed), Northeastern University (local presence not confirmed), Optum (local presence not confirmed), Ovative Group (local presence not confirmed), Securian Financial (local presence not confirmed), Target (local presence not confirmed), Target Corporation (local presence not confirmed), Travelers Insurance (local presence not confirmed), Truepill (local presence not confirmed), TruStage (local presence not confirmed), UnitedHealth Group (local presence not confirmed), University of Minnesota (local presence not confirmed), University of Minnesota, Carlson School of Management (local presence not confirmed), www.projectinfuse.com (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

Databricks

</details>

<details><summary><b>Other sources checked</b> (7)</summary>

- [Built In Minneapolis analytics jobs](https://builtin.com/jobs/minneapolis-saint-paul/data-analytics/analytics)
- [Built In Minneapolis remote data jobs](https://builtin.com/jobs/remote/minneapolis-saint-paul/data-analytics)
- [Insight Global job 556892](https://insightglobal.com/jobs/find_a_job/minnesota/arden-hills/sr-data-engineer-analytics/job-556892/) (nothing useful)
- [Dice SIAL data engineer ad](https://www.dice.com/job-detail/1bbe555f-941f-4bcf-837f-1028a8cb6b76) (nothing useful)
- [Twin Cities Databricks User Group](https://usergroups.databricks.com/twin-cities-databricks-user-group/)
- [HER+Data meetup](https://meetup.com/her-data) (nothing useful)
- [dbt community spotlight](https://docs.getdbt.com/community/spotlight) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 9 companies, 7 dbt job ads and 2 people, no first-time speakers. |
