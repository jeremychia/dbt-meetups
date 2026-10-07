# Philadelphia: city notes

This file holds what is specific to Philadelphia. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Philadelphia dbt Meetup](https://www.meetup.com/philadelphia-dbt-meetup/), data in `philadelphia_dbt_companies.json`
- **Region:** Philadelphia and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 52 |
| People | 125 |
| Tier 1 leads | 0 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 63 |
| Spoke at this chapter before | 8 |
| Based in the region | 95 |
| Based elsewhere | 0 |
| Location unknown | 30 |
| With a LinkedIn profile | 40 |
| Job ads mentioning dbt | 5 |
| Past chapter meetups | 4 |
<!-- at-a-glance:end -->

## 1. Where to look in Philadelphia

- **Chapter history:** past speakers come from `enriched/philadelphia-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (39.9526, -75.1652).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
51 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (8)</summary>

Children's Hospital of Philadelphia, dbt Labs (local presence not confirmed), FutureFit AI (local presence not confirmed), NTT DATA, Penn Interactive, Project Delivery Team (local presence not confirmed), Slalom (local presence not confirmed), Spotify (local presence not confirmed)

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Insomniac Design (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (39)</summary>

Apple (local presence not confirmed), Aramark (local presence not confirmed), Best Egg (local presence not confirmed), Cittabase Solutions (local presence not confirmed), CityOfPhiladelphia (local presence not confirmed), Comcast (local presence not confirmed), Data2Vizuals (local presence not confirmed), Databricks (local presence not confirmed), DemandLane (local presence not confirmed), Dolente Consulting LLC (local presence not confirmed), Drexel University (local presence not confirmed), Eigen X (local presence not confirmed), Entelligent (local presence not confirmed), ERM (local presence not confirmed), Freedom Mortgage (local presence not confirmed), Freedompay (local presence not confirmed), goPuff (local presence not confirmed), herodigital (local presence not confirmed), https://linkedin.com/in/seth-kalkstein (local presence not confirmed), Lumenalta (local presence not confirmed), mmtechtsoft (local presence not confirmed), Next-Level Tableau (local presence not confirmed), Old Republic Commercial Risk (local presence not confirmed), Oracle (local presence not confirmed), Pinnacle Treatment Centers, Inc. (local presence not confirmed), Projxon (local presence not confirmed), Redis (local presence not confirmed), Rula (local presence not confirmed), Salesforce (local presence not confirmed), Snowflake ❄️ (local presence not confirmed), Spark Therapeutics (local presence not confirmed), TD Bank (local presence not confirmed), Tegra Analytics (local presence not confirmed), The Carlyle Group (local presence not confirmed), The Wharton School: @wharton (local presence not confirmed), TJ McDowell LLC (local presence not confirmed), University of Pennsylvania (local presence not confirmed), US Federal Reserve Bank (local presence not confirmed), ZIP Code Wilmington (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (3)</summary>

Prostate Cancer Clinical Trials Consortium (local presence not confirmed), R-Ladies Philly, Snowflake Philadelphia User Group

</details>

<details><summary><b>Other sources checked</b> (6)</summary>

- [builtin.com Philadelphia analytics jobs](https://builtin.com/jobs/remote/philadelphia/data-analytics/analytics?page=3)
- [builtin.com Philadelphia data engineering jobs](https://builtin.com/jobs/philadelphia/data-analytics/data-engineering)
- [Snowflake Greater Philadelphia user group Nov 2025](https://usergroups.snowflake.com/events/details/snowflake-philadelphia-presents-snowflake-greater-philadelphia-user-group-november-20th-2025-event/)
- [R-Ladies Philly](https://rladies.org/chapters/rladies-philly)
- [PhillyBricks](https://usergroups.databricks.com/phillybricks-philadelphia-databricks-user-group/) (nothing useful)
- [getdbt Northeast events network page](https://www.getdbt.com/events/roadshow/join-the-dbt-northeast-events-network) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 7 companies, 5 dbt job ads and 5 people, no first-time speakers. |
