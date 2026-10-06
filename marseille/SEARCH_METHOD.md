# Marseille: city notes

This file holds what is specific to Marseille. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Marseille dbt Meetup](https://www.meetup.com/marseille-dbt-meetup/), data in `marseille_dbt_companies.json`
- **Region:** Marseille and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 12 |
| People | 13 |
| Tier 1 leads | 1 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 1 |
| Spoke at this chapter before | 1 |
| Based in the region | 11 |
| Based elsewhere | 0 |
| Location unknown | 2 |
| With a LinkedIn profile | 6 |
| Job ads mentioning dbt | 3 |
| Past chapter meetups | 1 |
<!-- at-a-glance:end -->

## 1. Where to look in Marseille

- **Chapter history:** past speakers come from `enriched/marseille-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (43.2965, 5.3698).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
11 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (3)</summary>

CMA CGM, dbt Labs (local presence not confirmed), HN Services (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (1)</summary>

Gojob

</details>

<details><summary><b>Not verified</b> (6)</summary>

Aix Marseille Université (local presence not confirmed), AXA (local presence not confirmed), BoondManager (local presence not confirmed), STMicroelectronics (local presence not confirmed), TnP-Consultants (local presence not confirmed), Vibe.co (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

Intelligence Artificielle Aix-Marseille

</details>

<details><summary><b>Other sources checked</b> (7)</summary>

- [Welcome to the Jungle: data engineer jobs Marseille](https://www.welcometothejungle.com/fr/pages/emploi-data-engineer-marseille-13001) (nothing useful)
- [Engineering.jobs: data analytics, Provence-Alpes-Cote d'Azur](https://fr.engineering.jobs/fr/emplois/data-analytics/provence-alpes-cote-dazur) (nothing useful)
- [Free-Work: senior data engineer](https://www.free-work.com/fr/tech-it/job-mission/data-engineer/senior-data-engineer-132) (nothing useful)
- [WeLoveDevs: Data Analytics Engineer Aix-en-Provence](https://welovedevs.com/app/job/data-analytics-engineer-aix-en-provence)
- [TieTalent: HN Services Data Engineer Aix](https://tietalent.com/en/jobs/p-534889370/aix-data-engineer-hf) (nothing useful)
- [Meetup: Intelligence Artificielle Aix-Marseille](https://www.meetup.com/intelligence-artificielle-aix-marseille/)
- [CMA CGM careers search (via web search)](https://jobs.cmacgm-group.com/CMACGM/job/Marseille-APPRENTICESHIP-Financial-Data-Analyst/1193943601) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 5 companies, 3 dbt job ads and 1 people, no first-time speakers. |
