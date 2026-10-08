# Austin: city notes

This file holds what is specific to Austin. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Austin dbt Meetup](https://www.meetup.com/austin-dbt-meetup/), data in `austin_dbt_companies.json`
- **Region:** Austin and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 81 |
| People | 151 |
| Tier 1 leads | 7 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 49 |
| Spoke at this chapter before | 8 |
| Based in the region | 127 |
| Based elsewhere | 5 |
| Location unknown | 19 |
| With a LinkedIn profile | 72 |
| Job ads mentioning dbt | 9 |
| Past chapter meetups | 8 |
<!-- at-a-glance:end -->

## 1. Where to look in Austin

- **Chapter history:** past speakers come from `enriched/austin-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (30.2672, -97.7431).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
80 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (10)</summary>

Brainforge, dbt Labs (local presence not confirmed), Givebutter, Setpoint, SolarWinds, Thatch, TruDataRx, Inc., Under Armour (local presence not confirmed), Upside, Zello (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (2)</summary>

Aceable, Applied Curiosity Inc

</details>

<details><summary><b>Not verified</b> (68)</summary>

7Rivers, Inc. (local presence not confirmed), AECOM (local presence not confirmed), AgencyPMG (local presence not confirmed), AISOFT LLC (local presence not confirmed), amazon (local presence not confirmed), Amazon.com (local presence not confirmed), AMD (local presence not confirmed), Anuvu (local presence not confirmed), Apex Systems (local presence not confirmed), Articulate Global (local presence not confirmed), AssemblyAI (local presence not confirmed), athenahealth (local presence not confirmed), Austin Pets Alive! (local presence not confirmed), babylonhealth (local presence not confirmed), Baker Tilly US (local presence not confirmed), Bestow (local presence not confirmed), BluePeak Analytics (local presence not confirmed), Branch (local presence not confirmed), brownchickenbrowncow (local presence not confirmed), Civitas Learning (local presence not confirmed), Community Dreams Foundation (local presence not confirmed), CVS Health (local presence not confirmed), Dataiku (local presence not confirmed), Double Line, Inc (local presence not confirmed), eero (local presence not confirmed), Encoura (local presence not confirmed), Enverus (local presence not confirmed), EVgo (local presence not confirmed), Expedia (local presence not confirmed), Expedia Group (local presence not confirmed), General Motors (local presence not confirmed), Georgetown Water Utility (local presence not confirmed), GoodRx (local presence not confirmed), Google (local presence not confirmed), Group1001 (local presence not confirmed), halcyon-ai (local presence not confirmed), HormelFoods (local presence not confirmed), Laborie Medical Technologies (local presence not confirmed), leading2lean (local presence not confirmed), Lovelytics (local presence not confirmed), Lulus.com (local presence not confirmed), Meld Networks (local presence not confirmed), Nutrabolt (local presence not confirmed), Proactive Talent (local presence not confirmed), Procore (local presence not confirmed), Pyramid Analytics and Consulting Corp (local presence not confirmed), Q2 (local presence not confirmed), ReUp Education (local presence not confirmed), RigUp (local presence not confirmed), Snowflake (local presence not confirmed), Solvenna (local presence not confirmed), Sonos (local presence not confirmed), Strategic Analysis Enterprises (local presence not confirmed), Tesla (local presence not confirmed), Texas A&M University (local presence not confirmed), The University of Texas at Austin (local presence not confirmed), TikTok (local presence not confirmed), Triple Ten (local presence not confirmed), University of Texas at Dallas (local presence not confirmed), Visa (local presence not confirmed), Welltower Inc (local presence not confirmed), Wipro (local presence not confirmed), www.gofurther.com (local presence not confirmed), Xeomatrix Inc, Data Divers LLC, and USF (local presence not confirmed), YETI (local presence not confirmed), Yuki (local presence not confirmed), Zebec Protocol (local presence not confirmed), ZeniMax Media (local presence not confirmed)

</details>

<details><summary><b>Other sources checked</b> (5)</summary>

- [Built In Austin analytics engineer jobs](https://builtinaustin.com/jobs/data-analytics/search/analytics-engineer)
- [Data Day Texas 2026](https://datadaytexas.com/) (nothing useful)
- [Snowflake Austin user group events](https://usergroups.snowflake.com/events/details/snowflake-austin-presents-austin-user-group-meeting-1)
- [dbt Summit 2026 speaker pages](https://www.getdbt.com/dbt-summit/speakers/ryan-ballman)
- [Austin WiMLDS meetup](https://www.meetup.com/austin-women-in-machine-learning-data-science/) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 11 companies, 9 dbt job ads and 4 people, no first-time speakers. |
