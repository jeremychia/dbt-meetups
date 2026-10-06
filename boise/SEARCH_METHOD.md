# Boise: city notes

This file holds what is specific to Boise. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Boise dbt Meetup](https://www.meetup.com/boise-dbt-meetup/), data in `boise_dbt_companies.json`
- **Region:** Boise and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 17 |
| People | 15 |
| Tier 1 leads | 0 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 8 |
| Spoke at this chapter before | 2 |
| Based in the region | 9 |
| Based elsewhere | 0 |
| Location unknown | 6 |
| With a LinkedIn profile | 1 |
| Job ads mentioning dbt | 7 |
| Past chapter meetups | 2 |
<!-- at-a-glance:end -->

## 1. Where to look in Boise

- **Chapter history:** past speakers come from `enriched/boise-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (43.615, -116.2023).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
16 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (3)</summary>

Blue Cross of Idaho, Clickfunnels.com (local presence not confirmed), Fluensight (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (5)</summary>

Cambia Health Solutions (local presence not confirmed), Carrum Health (local presence not confirmed), Privia Health (local presence not confirmed), SharkNinja (local presence not confirmed), Vanta (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (8)</summary>

Cradlepoint (local presence not confirmed), Data Engineer at Denodo Technologies (local presence not confirmed), Enfuse (local presence not confirmed), J.R. Simplot Company, LinkedIn (local presence not confirmed), Oxford Economics (local presence not confirmed), P3 Adaptive (local presence not confirmed), Snowflake (local presence not confirmed)

</details>

<details><summary><b>Other sources checked</b> (7)</summary>

- [builtin.com Boise data engineering jobs](https://builtin.com/jobs/boise/data-analytics/data-engineering?page=2)
- [builtin.com Boise analytics jobs](https://builtin.com/jobs/boise/data-analytics/analytics?page=2)
- [builtin.com Blue Cross of Idaho jobs](https://builtin.com/company/blue-cross-idaho/jobs) (nothing useful)
- [Snowflake User Group Boise](https://usergroups.snowflake.com/boise-id)
- [Snowflake User Group Boise performance optimization event](https://usergroups.snowflake.com/events/details/snowflake-boise-id-presents-snowflake-user-group-boise-snowflake-performance-optimization)
- [St. Luke's Health System data engineer ad](https://careers-slhs.icims.com/jobs/93842/data-engineer/job) (nothing useful)
- [Clearwater Analytics blog search](https://builtin.com/job/staff-data-engineer/6328087) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 7 companies, 7 dbt job ads and 2 people, no first-time speakers. |
