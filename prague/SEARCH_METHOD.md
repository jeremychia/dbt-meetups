# Prague: city notes

This file holds what is specific to Prague. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Prague dbt Meetup](https://www.meetup.com/prague-dbt-meetup-group/), data in `prague_dbt_companies.json`
- **Region:** Prague and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 51 |
| People | 79 |
| Tier 1 leads | 5 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 41 |
| Spoke at this chapter before | 13 |
| Based in the region | 52 |
| Based elsewhere | 0 |
| Location unknown | 27 |
| With a LinkedIn profile | 38 |
| Job ads mentioning dbt | 3 |
| Past chapter meetups | 4 |
<!-- at-a-glance:end -->

## 1. Where to look in Prague

- **Chapter history:** past speakers come from `enriched/prague-dbt-meetup-group.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (50.0755, 14.4378).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
50 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (11)</summary>

dbt Champion & Microsoft MVP (local presence not confirmed), dbt Labs (local presence not confirmed), EssenceMediacom (local presence not confirmed), GAMEE (local presence not confirmed), golemio.cz (local presence not confirmed), Keboola, MSD (local presence not confirmed), Philip Morris International (local presence not confirmed), Productboard (local presence not confirmed), RevoltBI (local presence not confirmed), STRV (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (2)</summary>

Siemens s.r.o., T-Mobile Czech Republic

</details>

<details><summary><b>dbt as a nice-to-have</b> (2)</summary>

Sky, Zásilkovna (Packeta Group)

</details>

<details><summary><b>Not verified</b> (34)</summary>

ABSA (local presence not confirmed), Adastra (local presence not confirmed), Alma Career (local presence not confirmed), Billigence (local presence not confirmed), blindspot-ai (local presence not confirmed), Databricks (local presence not confirmed), DataBrothers (local presence not confirmed), Datamole (local presence not confirmed), datamole-ai (local presence not confirmed), Datasentics (local presence not confirmed), Denik (local presence not confirmed), Deutsche Bank (local presence not confirmed), DHL Supply Chain (local presence not confirmed), Economia (local presence not confirmed), Economia Publishing House (local presence not confirmed), EIT (local presence not confirmed), Etnetera Activate (local presence not confirmed), Everpure (local presence not confirmed), Evropa v datech, Index prosperity Česka (local presence not confirmed), futureproof s.r.o. (local presence not confirmed), Immunai (local presence not confirmed), KBC (local presence not confirmed), L'Oréal & Sympulse (local presence not confirmed), mcl (local presence not confirmed), Merck (local presence not confirmed), Merkle (local presence not confirmed), Mews (local presence not confirmed), Open to opportunities (local presence not confirmed), Principal s.r.o. (local presence not confirmed), Seznam.cz, a.s. (local presence not confirmed), Silpo (local presence not confirmed), Snowflake (local presence not confirmed), Targito (local presence not confirmed), Teradata (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

WiDS Prague

</details>

<details><summary><b>Other sources checked</b> (9)</summary>

- [jobs.cz dbt filter](https://www.jobs.cz/prace/praha/?q%5B%5D=dbt)
- [Siemens careers](https://jobs.siemens.com/cs_CZ/externaljobs/JobDetail/514655)
- [builtin.com Sky ad](https://builtin.com/job/data-analyst/6485791)
- [startupjobs.cz](https://www.startupjobs.cz/nabidky?q=dbt) (nothing useful)
- [Databricks Meetup, FIT CTU 2026-04-21](https://fit.cvut.cz/en/life-at-fit/fit-live/events/24631-databricks-meetup) (nothing useful)
- [Analytics Pioneers Prague meetup](https://www.meetup.com/de-de/analytics-pioneers-prague/) (nothing useful)
- [Data Point Prague 2026 sessionize](https://sessionize.com/data-point-prague-2026/) (nothing useful)
- [WiDS Prague conference on Luma](https://luma.com/wids-prague-conference)
- [Keboola dbt workshop](https://www.keboola.com/webinars/workshop-dbt-for-experts)

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
| 2026-10-06 | 3 | Research run: 6 companies, 3 dbt job ads and 2 people, no first-time speakers. |
