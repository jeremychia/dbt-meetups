# Detroit: city notes

This file holds what is specific to Detroit. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Detroit dbt Meetup](https://www.meetup.com/detroit-dbt-meetup/), data in `detroit_dbt_companies.json`
- **Region:** Detroit and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 38 |
| People | 56 |
| Tier 1 leads | 0 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 28 |
| Spoke at this chapter before | 0 |
| Based in the region | 39 |
| Based elsewhere | 0 |
| Location unknown | 17 |
| With a LinkedIn profile | 16 |
| Job ads mentioning dbt | 12 |
| Past chapter meetups | 0 |
<!-- at-a-glance:end -->

## 1. Where to look in Detroit

- **Chapter history:** past speakers come from `enriched/detroit-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (42.3314, -83.0458).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
37 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (8)</summary>

Boulder Care (local presence not confirmed), Digible (local presence not confirmed), Eve (local presence not confirmed), Integra Partners, Kaleidoscope Innovation (local presence not confirmed), Ontic (local presence not confirmed), Solace (local presence not confirmed), Underdog (local presence not confirmed)

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

SailPoint (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (25)</summary>

Ally Financial (local presence not confirmed), Application Perfection Ltd (local presence not confirmed), BTD (local presence not confirmed), CardioSounds (local presence not confirmed), CEI (local presence not confirmed), CityOfDetroit (local presence not confirmed), Concentrix (local presence not confirmed), Databricks (local presence not confirmed), Detroit Trading Company (local presence not confirmed), Freelance (local presence not confirmed), General Motors (local presence not confirmed), Ilitch Sports & Entertainment (local presence not confirmed), Johnson & Johnson (local presence not confirmed), Laboredge (local presence not confirmed), Marvel Technologies Inc (local presence not confirmed), Microsoft (local presence not confirmed), Publicis Sapient (local presence not confirmed), Quicken Loans (local presence not confirmed), Salesforce (local presence not confirmed), Somerville Analytics LLC (local presence not confirmed), TABLEAU (local presence not confirmed), TileCorporation (local presence not confirmed), University of Michigan (local presence not confirmed), University of Michigan, School of Public Health (local presence not confirmed), XPO LOGISTICS LTL (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (3)</summary>

Ann Arbor SPARK, Data in the D, Metro Detroit Women in Machine Learning and Data Science

</details>

<details><summary><b>Other sources checked</b> (9)</summary>

- [Built In Detroit analytics jobs (dbt filter)](https://builtin.com/jobs/detroit/data-analytics/analytics?page=7)
- [Built In Detroit data engineering jobs](https://builtin.com/jobs/detroit/data-analytics/data-engineering)
- [Built In job: Integra Partners](https://builtin.com/job/senior-data-engineer/7320647)
- [Data in the D](https://datainthed.org)
- [Data in the D 2026 call for speakers](https://sessionize.com/2026-data-in-the-d-conference) (nothing useful)
- [Data in the D 2025 (MotherDuck page)](https://motherduck.com/events/data-in-the-d-conference-2025-2025) (nothing useful)
- [WiMLDS Metro Detroit team](https://wimlds.org/about-the-metro-detroit-team/)
- [Detroit Low-Key Data Meetup](https://annarborusa.org/event/detroit-low-key-data-meetup/)
- [dbt Labs case studies and Coalesce speaker search](https://www.getdbt.com/casestudies) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 12 companies, 12 dbt job ads and 5 people, no first-time speakers. |
