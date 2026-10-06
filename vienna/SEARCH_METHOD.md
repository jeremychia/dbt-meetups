# Vienna: city notes

This file holds what is specific to Vienna. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Vienna dbt Meetup](https://www.meetup.com/vienna-dbt-meetup/), data in `vienna_dbt_companies.json`
- **Region:** Vienna and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 26 |
| People | 74 |
| Tier 1 leads | 10 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 47 |
| Spoke at this chapter before | 8 |
| Based in the region | 58 |
| Based elsewhere | 0 |
| Location unknown | 16 |
| With a LinkedIn profile | 11 |
| Job ads mentioning dbt | 7 |
| Past chapter meetups | 2 |
<!-- at-a-glance:end -->

## 1. Where to look in Vienna

- **Chapter history:** past speakers come from `enriched/vienna-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (48.2082, 16.3738).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
25 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (13)</summary>

b.telligent (local presence not confirmed), Bitpanda, Bluecode, dbt Labs (local presence not confirmed), GoStudent (local presence not confirmed), happtiq (local presence not confirmed), Helvetia Versicherungen AG, karriere.at (local presence not confirmed), kununu, MeisterLabs (local presence not confirmed), Microsoft Fabric (local presence not confirmed), sclable (local presence not confirmed), VOLKSBANK WIEN AG

</details>

<details><summary><b>Some dbt signal</b> (2)</summary>

Posedio (local presence not confirmed), Siemens Personaldienstleistungen GmbH

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

REWE Group Österreich

</details>

<details><summary><b>Not verified</b> (8)</summary>

Austrian Academy of Sciences (local presence not confirmed), BearingPoint (local presence not confirmed), eversport (local presence not confirmed), Innovative Decisions, Inc. (local presence not confirmed), Radancy (local presence not confirmed), Sphinx IT (local presence not confirmed), United Tech (local presence not confirmed), Wien Energie GmbH (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

R-Ladies Vienna

</details>

<details><summary><b>Other sources checked</b> (7)</summary>

- [devjobs.at (dbt searches)](https://en.devjobs.at/jobs/fivetran)
- [karriere.at](https://www.karriere.at/jobs/7840154)
- [Google Cloud Meetup #27 page](https://gdg.community.dev/events/details/google-gdg-cloud-vienna-presents-google-cloud-meetup-27/)
- [Vienna Data Engineering Meetup, 2nd event](https://www.meetup.com/vienna-data-engineering-meetup/events/292867396/) (nothing useful)
- [University of Vienna Women in Science 2024](https://datascience.univie.ac.at/events/women-in-science-2024) (nothing useful)
- [wearedevelopers Vienna meetup list](https://www.wearedevelopers.com/magazine/223-7-great-tech-meetups-in-vienna)
- [R-Ladies Vienna](https://rladies.org/chapters/austria-vienna)

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
| 2026-10-06 | 3 | Research run: 11 companies, 7 dbt job ads and 5 people, no first-time speakers. |
