# Vancouver: city notes

This file holds what is specific to Vancouver. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Vancouver dbt Meetup](https://www.meetup.com/vancouver-dbt-meetup/), data in `vancouver_dbt_companies.json`
- **Region:** Vancouver and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 53 |
| People | 149 |
| Tier 1 leads | 0 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 47 |
| Spoke at this chapter before | 2 |
| Based in the region | 139 |
| Based elsewhere | 0 |
| Location unknown | 10 |
| With a LinkedIn profile | 53 |
| Job ads mentioning dbt | 8 |
| Past chapter meetups | 1 |
<!-- at-a-glance:end -->

## 1. Where to look in Vancouver

- **Chapter history:** past speakers come from `enriched/vancouver-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (49.2827, -123.1207).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
52 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (5)</summary>

Dutch Vet, FORM, Infostrux, Materialize (local presence not confirmed), Two Circles

</details>

<details><summary><b>Some dbt signal</b> (4)</summary>

Badal.io, Insight Global, PSL Group (local presence not confirmed), SOCi

</details>

<details><summary><b>Not verified</b> (42)</summary>

Amazon & Analytixia (local presence not confirmed), Amazon Web Services (local presence not confirmed), amzn (local presence not confirmed), Analytic Labs (local presence not confirmed), Aritzia, AssureCKD (local presence not confirmed), AWS (local presence not confirmed), Beatdapp (local presence not confirmed), Cavallo Technologies (local presence not confirmed), Clio (local presence not confirmed), cmd (local presence not confirmed), Coast Capital Savings (local presence not confirmed), Data Analyst Jr (local presence not confirmed), Databricks (local presence not confirmed), DD Labs (local presence not confirmed), dialpad (local presence not confirmed), DoubleZero Foundation (local presence not confirmed), Dueck Auto group (local presence not confirmed), Envo Drive System Inc (local presence not confirmed), Gametime (local presence not confirmed), GINQO Consulting Ltd. (local presence not confirmed), HSBC Canada (local presence not confirmed), Improving (local presence not confirmed), Infoblox (local presence not confirmed), Klue (local presence not confirmed), Lululemon (local presence not confirmed), Minesense Technologies Ltd. (local presence not confirmed), mozilla (local presence not confirmed), OutdoorRD (local presence not confirmed), Perfect Company LLC (local presence not confirmed), Saje Natural Wellness (local presence not confirmed), Scotiabank (local presence not confirmed), Shopify (local presence not confirmed), Slalom Inc. (local presence not confirmed), Snowflake (local presence not confirmed), StreetLight Data (local presence not confirmed), The Brick (local presence not confirmed), University Canada West (local presence not confirmed), University of British Columbia (local presence not confirmed), Vancouver Coastal Health (local presence not confirmed), Vectux Analytics (local presence not confirmed), WithYouWithMe (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

PyLadies Vancouver

</details>

<details><summary><b>Other sources checked</b> (7)</summary>

- [Built In Vancouver job pages](https://builtinvancouver.org/job/lead-dbtanalytics-engineer/2505758)
- [Workable job page for FORM](https://jobs.workable.com/jobs/685346d3-c84f-41e2-a5d5-a297c29ccb52.md)
- [Luma Vancouver Data Engineering Meetup with ClickHouse](https://luma.com/jr8tc94e) (nothing useful)
- [PyLadies Vancouver](https://vancouver.pyladies.com/)
- [Snowflake User Group Vancouver](https://usergroups.snowflake.com/vancouver)
- [Sessionize Venkatesh Sekar](https://sessionize.com/venkatesh-sekar) (nothing useful)
- [dbt Labs case study searches](https://www.getdbt.com/dbt-assets/business-case-guide-dbt-cloud) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 7 companies, 8 dbt job ads and 3 people, no first-time speakers. |
