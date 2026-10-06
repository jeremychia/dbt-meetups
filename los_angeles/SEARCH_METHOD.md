# Los Angeles: city notes

This file holds what is specific to Los Angeles. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Los Angeles dbt Meetup](https://www.meetup.com/los-angeles-dbt-meetup/), data in `los_angeles_dbt_companies.json`
- **Region:** Los Angeles and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 60 |
| People | 121 |
| Tier 1 leads | 0 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 21 |
| Spoke at this chapter before | 2 |
| Based in the region | 117 |
| Based elsewhere | 0 |
| Location unknown | 4 |
| With a LinkedIn profile | 47 |
| Job ads mentioning dbt | 7 |
| Past chapter meetups | 2 |
<!-- at-a-glance:end -->

## 1. Where to look in Los Angeles

- **Chapter history:** past speakers come from `enriched/los-angeles-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (34.0522, -118.2437).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
59 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (8)</summary>

Brainforge (local presence not confirmed), Datafold (local presence not confirmed), Fitment, HourWork (local presence not confirmed), Pacific Life (local presence not confirmed), Prodege LLC, Prosum, Riot Games

</details>

<details><summary><b>Some dbt signal</b> (2)</summary>

Crexi, Slalom

</details>

<details><summary><b>dbt as a nice-to-have</b> (1)</summary>

Sony Pictures Entertainment

</details>

<details><summary><b>Not verified</b> (48)</summary>

3dna (local presence not confirmed), 7Rivers (local presence not confirmed), AEG Sports (local presence not confirmed), ALG (local presence not confirmed), Anaconda Inc (local presence not confirmed), BalanX Bio (local presence not confirmed), Bestow (local presence not confirmed), CBS Interactive (local presence not confirmed), Clerion (local presence not confirmed), Confluent (local presence not confirmed), Connect2u.xyz (local presence not confirmed), CTREES/UCLA (local presence not confirmed), Edwards Lifesciences (local presence not confirmed), Factual (local presence not confirmed), FanDuel (local presence not confirmed), flexanalytics (local presence not confirmed), Gilead Sciences (local presence not confirmed), github (local presence not confirmed), Honey (local presence not confirmed), hpInc (local presence not confirmed), Internet Brands, Avvo (local presence not confirmed), Irvine Company (local presence not confirmed), KickUp (local presence not confirmed), LAist-NPR (local presence not confirmed), Loyola Marymount University (local presence not confirmed), mpavlenk@uci.edu (local presence not confirmed), mpulsemobile (local presence not confirmed), Nakatomi window cleaners (local presence not confirmed), netflix (local presence not confirmed), Nexstar (local presence not confirmed), Planet Art (local presence not confirmed), PriceSpider (local presence not confirmed), Prime Healthcare (local presence not confirmed), PushPress, Inc (local presence not confirmed), Realtor.com (local presence not confirmed), Reason Data Services (local presence not confirmed), Red Bull (local presence not confirmed), Rocketship Financial (local presence not confirmed), skylight-hq (local presence not confirmed), Skyworks Inc (local presence not confirmed), SnowFlake AI Engineer (local presence not confirmed), sonarverse (local presence not confirmed), UC Berkeley (local presence not confirmed), UCLA Baseball (local presence not confirmed), UnitedHealth Group (local presence not confirmed), University of Southern California (local presence not confirmed), USC (local presence not confirmed), willblumrosen@gmail.com (local presence not confirmed)

</details>

<details><summary><b>Other sources checked</b> (8)</summary>

- [Built In LA data engineering jobs (dbt list)](https://www.builtinla.com/jobs/data-analytics/data-engineering)
- [Built In LA data analytics jobs (dbt list)](https://www.builtinla.com/jobs/data-analytics)
- [Built In LA Brainforge analytics engineer](https://www.builtinla.com/job/analytics-engineer/10138472)
- [dbt Labs + Slalom meetup West LA](https://www.getdbt.com/events/dbt-labs-slalom-meetup-west-la)
- [Coalesce on the Road Newport Beach](https://www.getdbt.com/events/roadshow/coalesce-in-newport-beach)
- [WiDS Los Angeles at Cal State LA](https://www.widsworldwide.org/events/event/wids-los-angeles-cal-state-university-la/) (nothing useful)
- [Built In LA Sleep Doctor / Etech / Hex job pages](https://www.builtinla.com/job/analytics-engineer/7050516) (nothing useful)
- [ZipRecruiter dbt data engineer Los Angeles](https://www.ziprecruiter.com/Jobs/Dbt-Data-Engineer/-in-Los-Angeles,CA) (nothing useful)

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
| 2026-10-06 | 3 | Research run: 9 companies, 7 dbt job ads and 4 people, no first-time speakers. |
