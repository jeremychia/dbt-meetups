# Wellington: city notes

This file holds what is specific to Wellington. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Wellington dbt Meetup](https://www.meetup.com/wellington-dbt-meetup/), data in `wellington_dbt_companies.json`
- **Region:** Wellington and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 22 |
| People | 44 |
| Tier 1 leads | 1 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 27 |
| Spoke at this chapter before | 1 |
| Based in the region | 35 |
| Based elsewhere | 0 |
| Location unknown | 9 |
| With a LinkedIn profile | 5 |
| Job ads mentioning dbt | 5 |
| Past chapter meetups | 1 |
<!-- at-a-glance:end -->

## 1. Where to look in Wellington

- **Chapter history:** past speakers come from `enriched/wellington-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (-41.2865, 174.7762).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
21 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (2)</summary>

dbt Labs (local presence not confirmed), Xero

</details>

<details><summary><b>Some dbt signal</b> (2)</summary>

Kiwibank, Potentia

</details>

<details><summary><b>Not verified</b> (16)</summary>

Accident Compensation Corporation, dbt-labs (local presence not confirmed), Earth Sciences New Zealand (local presence not confirmed), FarmIQ (local presence not confirmed), Fire and Emergency NZ (local presence not confirmed), internetarchive (local presence not confirmed), NZ Post (local presence not confirmed), Oranga Tamariki (local presence not confirmed), Oranga Tamariki-Ministry for Children (local presence not confirmed), Oranga Tamariki/Qrious (local presence not confirmed), PartsTrader (local presence not confirmed), Sharesies (local presence not confirmed), Snowflake, Telicent Ltd (@Telicent-io) (local presence not confirmed), TradeMe (local presence not confirmed), Wellington City Council

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

Databricks

</details>

<details><summary><b>Other sources checked</b> (8)</summary>

- [Snowflake User Group Wellington](https://usergroups.snowflake.com/wellington/)
- [Databricks Wellington meetups](https://usergroups.databricks.com/events/details/databricks-user-groups-new-zealand-databricks-user-group-presents-databricks-wellington-meet-up/)
- [dbt Zero to dbt workshop Wellington](https://www.getdbt.com/events/zertodbt-wellington)
- [WiDS NZ 2024 speakers](https://ecs.wgtn.ac.nz/Events/WiDSNZ2024/Speakers) (nothing useful)
- [TheirStack dbt in New Zealand](https://theirstack.com/en/technology/dbt/nz)
- [Seek NZ](https://nz.seek.com/Analytics-Engineer-jobs-in-information-communication-technology/database-development-administration) (nothing useful)
- [Potentia job pages](https://potentia.co.nz/job/58681789-senior-data-engineer) (nothing useful)
- [Trade Me Jobs IT](https://www.trademe.co.nz/jobs/it/data-warehousing-bi/listing-5885304396.htm)

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
| 2026-10-06 | 3 | Research run: 6 companies, 5 dbt job ads and 6 people, no first-time speakers. |
