# São Paulo: city notes

This file holds what is specific to São Paulo. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [São Paulo dbt Meetup](https://www.meetup.com/sao-paulo-dbt-meetup-group/), data in `sao_paulo_dbt_companies.json`
- **Region:** São Paulo and towns within about an hour.
- **First built:** 2026-10-06

<!-- at-a-glance:start -->
**At a glance** (version 3, 2026-10-06)

| | Count |
|---|---|
| Companies | 81 |
| People | 149 |
| Tier 1 leads | 13 |
| First-time speakers (publish, no talk yet) | 5 |
| Proven speakers | 45 |
| Spoke at this chapter before | 22 |
| Based in the region | 112 |
| Based elsewhere | 2 |
| Location unknown | 35 |
| With a LinkedIn profile | 80 |
| Job ads mentioning dbt | 4 |
| Past chapter meetups | 7 |
<!-- at-a-glance:end -->

## 1. Where to look in São Paulo

- **Chapter history:** past speakers come from `enriched/sao-paulo-dbt-meetup-group.json`.
- **Local data groups, Bevy chapters and GitHub:** `research/find_local_speakers.py` with this city's coordinates (-23.5505, -46.6333).

## 2. What didn't work here

Nothing recorded yet.

## 3. Companies looked at

No company research yet. The list below is generated from the data.

<!-- companies:start -->
80 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (14)</summary>

Afya (local presence not confirmed), ASAAS (local presence not confirmed), Banco BV (local presence not confirmed), Compass.uol (local presence not confirmed), DP6 (local presence not confirmed), Indicium (local presence not confirmed), Infinite Lambda (local presence not confirmed), Lambda3 - Tivit (local presence not confirmed), Portal Telemedicina (local presence not confirmed), Remote (local presence not confirmed), TRACTIAN (local presence not confirmed), Upwork (local presence not confirmed), Warren Investimentos (local presence not confirmed), X-Team (local presence not confirmed)

</details>

<details><summary><b>Some dbt signal</b> (3)</summary>

CI&T (local presence not confirmed), Infosys (local presence not confirmed), Nubank

</details>

<details><summary><b>Not verified</b> (62)</summary>

3 Corações (local presence not confirmed), Agibank (local presence not confirmed), Alice (local presence not confirmed), arco-cv (local presence not confirmed), Azul Linhas Aéreas (local presence not confirmed), Banco Bradesco (local presence not confirmed), Booster-Data-Intelligence (local presence not confirmed), Bossabox (local presence not confirmed), Brasol Soluções Energéticas (local presence not confirmed), BTG Pactual (local presence not confirmed), Capgemini (local presence not confirmed), Cogna Educação (local presence not confirmed), Data Super Hero Snowflake (local presence not confirmed), Deloitte Touche Tohmatsu Limited (local presence not confirmed), factored.ai (local presence not confirmed), Federal University of São Paulo - UNIFESP (local presence not confirmed), Fioplast (local presence not confirmed), Foursys (local presence not confirmed), Freelancer (local presence not confirmed), Freto (local presence not confirmed), georgemendonca (local presence not confirmed), GOL (local presence not confirmed), Google (local presence not confirmed), green4T (local presence not confirmed), Grupo Comolatti (local presence not confirmed), grupo Urca Energia (local presence not confirmed), GrupoCasasBahiaTecnologia (local presence not confirmed), iClinic - Afya (local presence not confirmed), iFood (local presence not confirmed), IMILLION (local presence not confirmed), Indicium AI (local presence not confirmed), inloco (local presence not confirmed), Inter Bank (local presence not confirmed), Itaú BBA (local presence not confirmed), LinkedIn (local presence not confirmed), Magalu (local presence not confirmed), MarketData | Banco Santander (local presence not confirmed), microsoft (local presence not confirmed), moises-ai (local presence not confirmed), Natura (local presence not confirmed), NTT DATA Europe & LATAM (local presence not confirmed), PicPay (local presence not confirmed), Pipo Saude (local presence not confirmed), Raizen (local presence not confirmed), Rede de Farmácias São João (local presence not confirmed), RW Consultoria ME (local presence not confirmed), Safra Bank (local presence not confirmed), Saint-Gobain (local presence not confirmed), Ser Mais Digital (local presence not confirmed), Shopee (local presence not confirmed), Snowflake (local presence not confirmed), Solvd (local presence not confirmed), Stech Soluções Tecnológicas (local presence not confirmed), Sympla (local presence not confirmed), Technogym (local presence not confirmed), Torra-Cartoes (local presence not confirmed), TriggoAI (local presence not confirmed), Univesp - São Paulo State University (local presence not confirmed), V.tal (local presence not confirmed), XP Investimentos (local presence not confirmed), zamp (local presence not confirmed), Zig - Global Funtech (local presence not confirmed)

</details>

<details><summary><b>Uses a different stack</b> (1)</summary>

Mulheres em Dados (local presence not confirmed)

</details>

<details><summary><b>Other sources checked</b> (8)</summary>

- [web search: vaga engenheiro de analytics dbt São Paulo](https://empregandobrasil.com.br/vagas/fbs-associate-analytics-engineer-sao-paulo-sp/) (nothing useful)
- [CI&T, Infosys, Nubank job ads](https://jobs.lever.co/ciandt/)
- [dbt docs author pages (Indicium)](https://docs.getdbt.com/author/christian_vanbellen)
- [TDC São Paulo 2025 data engineering track](https://thedevconf.com/tdc/2025/sao-paulo/trilha-engenharia-de-dados)
- [SQL Saturday São Paulo 2026 on Sessionize](https://sessionize.com/sqlsaturday-sao-paulo-2026/) (nothing useful)
- [Databricks DevConnect São Paulo](https://usergroups.databricks.com/events/details/databricks-user-groups-databricks-devconnect-presents-databricks-devconnect-i-sao-paulo/) (nothing useful)
- [Snowflake World Tour São Paulo speakers](https://www.snowflake.com/pt_br/world-tour/sao-paulo/speakers/) (nothing useful)
- [dbt Labs partner directory](https://partners.getdbt.com/english/directory/partner/1731459/brf-consulting) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:** the Indicium authors on the dbt developer blog, such as [Christian van Bellen](https://docs.getdbt.com/author/christian_vanbellen), and Igor Cleto, who [writes on data modelling with dbt](https://igorcletotech.substack.com/p/modelagem-de-dados-dbt).

## 5. Before outreach

- [ ] Check speakers whose location is unverified: a talk at a local group does not show where someone lives.

## 6. Next run

- **Sources to try first:** a research run with the [central replication prompt](../research/README.md#9-replication-prompt) for companies, dbt job ads and first-time speakers.

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-10-06 | 1 | First build from the chapter history. |
| 2026-10-06 | 3 | Research run: 3 new companies, 4 dbt job ads from search summaries (CI&T, Nubank, Infosys) and 7 people, 5 of them first-time speakers. |
