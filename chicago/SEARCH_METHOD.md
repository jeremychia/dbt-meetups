# Chicago: city notes

This file holds what is specific to Chicago. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Chicago dbt Meetup](https://www.meetup.com/chicago-dbt-meetup/), data in `chicago_dbt_companies.json`
- **Region:** Chicago and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 80 |
| People | 178 |
| Tier 1 leads | 3 |
| First-time speakers (publish, no talk yet) | 0 |
| Proven speakers | 76 |
| Spoke at this chapter before | 21 |
| Based in the region | 147 |
| Based elsewhere | 1 |
| Location unknown | 30 |
| With a LinkedIn profile | 75 |
| Job ads mentioning dbt | 8 |
| Past chapter meetups | 12 |
<!-- at-a-glance:end -->

## 1. Where to look in Chicago

- **Chapter history:** past speakers come from `enriched/chicago-dbt-meetup.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (41.8781, -87.6298).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
79 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (20)</summary>

2023 dbt Community Champion (local presence not confirmed), Analytics8, Chicago Fire (local presence not confirmed), Datafold (local presence not confirmed), dbt Labs (local presence not confirmed), Eve (local presence not confirmed), Fi (local presence not confirmed), Fleetio (local presence not confirmed), Jarvus Innovations (local presence not confirmed), Keystone Cooperative (local presence not confirmed), M1 (local presence not confirmed), Mammoth Growth (local presence not confirmed), NinjaTrader, Ollion (local presence not confirmed), Slalom (local presence not confirmed), SpotOn (local presence not confirmed), Sprout Social, The Scion Group, Upside, Velir (Brooklyn Data Company) (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (1)</summary>

CrowdStrike (local presence not confirmed)

</details>

<details><summary><b>Not verified</b> (55)</summary>

Affine (local presence not confirmed), Alas (local presence not confirmed), Atrius | Acuity Inc (local presence not confirmed), Bitwise (local presence not confirmed), Blackhawk Network (local presence not confirmed), Blue.cloud (local presence not confirmed), Cameo (local presence not confirmed), Caterpillar (local presence not confirmed), CC Industries (local presence not confirmed), Central States Funds (local presence not confirmed), ClearStreet (local presence not confirmed), code629 (local presence not confirmed), CVS Health (local presence not confirmed), Databricks (local presence not confirmed), DataMan62 (local presence not confirmed), DePaul University (local presence not confirmed), Discover (local presence not confirmed), Dscout (local presence not confirmed), Egen (local presence not confirmed), Elmhurst University (local presence not confirmed), EY (local presence not confirmed), Fetch (local presence not confirmed), FIS (local presence not confirmed), Foundant (local presence not confirmed), Foxconn (local presence not confirmed), github (local presence not confirmed), Grafana Labs (local presence not confirmed), Grubhub (local presence not confirmed), Guild (local presence not confirmed), https://statumconsulting.com/ (local presence not confirmed), https://teamsparq.com (local presence not confirmed), iD Lab (local presence not confirmed), Illinois Institute of Technology (local presence not confirmed), IMC (local presence not confirmed), Master's Student (local presence not confirmed), Meta (local presence not confirmed), Mustapha Abdelkarim SBA (local presence not confirmed), Northern Illinois University (local presence not confirmed), Options Clearing Corporation (local presence not confirmed), PAK Digital Inc. (local presence not confirmed), Qualus (local presence not confirmed), reality-defender (local presence not confirmed), Self (local presence not confirmed), Shore Capital Partners (local presence not confirmed), StoneX (local presence not confirmed), Streeterval Art (local presence not confirmed), The Emerson Group (local presence not confirmed), The Kraft Heinz Company (local presence not confirmed), Truss Health (local presence not confirmed), University of Chicago (local presence not confirmed), University of Illinois at Chicago (local presence not confirmed), University of Illinois at Urbana-Champaign (local presence not confirmed), University of Illinois Chicago (local presence not confirmed), Uptake Technology (local presence not confirmed), Walgreens (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (3)</summary>

Box (local presence not confirmed), Semaphor (local presence not confirmed), WiDS Chicago

</details>

<details><summary><b>Other sources checked</b> (7)</summary>

- [Built In Chicago dbt job ads](https://www.builtinchicago.org/jobs/data-analytics/data-engineering)
- [Built In Chicago mobile data jobs](https://www.builtinchicago.org/jobs/data-analytics/mobile?page=2) (nothing useful)
- [dbt Labs partner directory (Analytics8)](https://partners.getdbt.com/english/directory/partner/1517840/analytics8)
- [WiDS Chicago event pages](https://www.widsworldwide.org/events/event/wids-chicago-2/)
- [Chicago Data & Databases Meetup (Luma)](https://luma.com/c5evgnbc)
- [Databricks DevConnect Chicago 2025](https://community.databricks.com/t5/chicagoland/databricks-devconnect-chicago-il-august-19/td-p/125729) (nothing useful)
- [dbt Summit speaker pages](https://www.getdbt.com/dbt-summit/speakers) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **Connectors:** the [WiDS Chicago](https://www.widsworldwide.org/events/event/wids-chicago-2/) ambassadors.

## 5. Before outreach

- [ ] Check speakers whose location is unverified: a talk at a local group does not show where someone lives.

## 6. Next run

- **Sources to try first:** a research run with the [central replication prompt](../research/README.md#9-replication-prompt) for companies, dbt job ads and first-time speakers.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-06 | 1 | First build from the chapter history. |
| 2026-10-06 | 3 | Research run: 12 companies, 8 dbt job ads (Upside and NinjaTrader are hybrid in Chicago) and 4 people, including the WiDS Chicago ambassadors. |
