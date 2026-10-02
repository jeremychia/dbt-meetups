# Paris: city notes

This file holds what is specific to Paris. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Paris dbt Meetup](https://www.meetup.com/paris-dbt-meetup/), data in `paris_dbt_companies.json`
- **Region:** Paris and Île-de-France.
- **First built:** 2026-09-24
- **Language:** much of the content is in French. French posts and talks are recorded as they are, with an English description.
- **Approach:** public content (blogs, podcasts, conferences and other meetups' line-ups), a job-ad scan, and every past Paris dbt Meetup speaker.

<!-- at-a-glance:start -->
**At a glance** (version 5, 2026-10-01)

| | Count |
|---|---|
| Companies | 250 |
| People | 207 |
| Tier 1 leads | 34 |
| First-time speakers (publish, no talk yet) | 26 |
| Proven speakers | 144 |
| Spoke at this chapter before | 17 |
| Based in the region | 174 |
| Based elsewhere | 12 |
| Location unknown | 21 |
| With a LinkedIn profile | 145 |
| Job ads mentioning dbt | 160 |
| Past chapter meetups | 10 |
<!-- at-a-glance:end -->

## 1. Where to look in Paris

### Media and conferences

- **DataGen newsletter and podcast:** [datageneration.substack.com](https://datageneration.substack.com), by Robin Conquet. This was the richest single source of named Paris dbt and analytics engineering practitioners: Doctolib, Qonto, Back Market, Ornikar, Decathlon, Swile, Modeo and more.
- **Forward Data Conference:** [forward-data-conference.com](https://forward-data-conference.com) (2024–2026). Its static speaker pages give each speaker's role and a full abstract, about 120 speakers across three editions. It was the best source of talk-level leads.
- **Both together:** DataGen and Forward Data Conference name most of the Paris practitioners who speak publicly about dbt.
- **blef.fr Data News:** the newsletter by Christophe Blefari.
- **Other meetups:** the Paris Apache Airflow meetup, DuckDB Paris, ClickHouse Paris (hosted by Qonto) and Paris Data Ladies.

### Company and consultancy blogs

- **Ippon Technologies:** the best consultancy source, with 12 dbt posts with named authors. The French blog is full of hands-on dbt posts by consultants: TDD with unit tests, testing macros, GitHub Actions deploys, and Kimball + Data Vault with dbt. The authors are good first-time speakers, but many are not confirmed as being in Paris.
- **Other consultancies:** Modeo, Artefact, Theodo, OCTO, Converteo, Devoteam, Infinite Lambda Paris, Zenika and Ekimetrics.
- **Vendors:** nao Labs, Kestra, Sifflet, CastorDoc, DataGalaxy, Dataiku, Altertable and others.
- **Large Paris companies (2026-09):** Doctolib, BlaBlaCar, Qonto, Back Market, ManoMano, Alan, Swile, Deezer, Criteo, Contentsquare, leboncoin, Mirakl, Vestiaire Collective, PayFit, Pennylane, Ledger, Spendesk, Malt, Lydia/Sumeria, Aircall, Getaround, Brigad, Stuart, Lalilo, Brevo, Decathlon Digital, Carrefour, L'Oréal, LVMH/Sephora, TotalEnergies, SNCF Connect, Galeries Lafayette, Macif, Ornikar, Accor and others. For each, the search checked its tech blog or Medium feed (`medium.com/feed/<publication>`, or `/tagged/dbt`), dbt Labs and cloud-vendor case studies, and conference talks.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **Paris Data Ladies:** [meetup.com/paris-dataladies](https://www.meetup.com/paris-dataladies/) was the only strong source: 22 events since 2023, each with 3–4 data speakers. Its meetup.com group data also lists organisers and event hosts, who are recorded as `connector`. Its [November 2025 event at Thales](https://www.meetup.com/paris-dataladies/events/311778883/) added Louise Rodriguez (Thales) and Linh Tran and Anaïs Faussadier (DGFiP), on AI and data sovereignty. Two more co-hosts, Justine Deshais and Rima Hajou, are recorded as connectors.
- **[Women in Big Data Paris](https://www.meetup.com/women-in-big-data-paris-meetup-group/):** its [June 2025 afterwork with iAdvize](https://www.meetup.com/women-in-big-data-paris-meetup-group/events/308007050/) was held in Nantes. It gave Francesca Iannuzzi (Chief Data Officer, iAdvize), Camille Salin (iAdvize), Emeline Daviau (Head of Data Analytics, Maisons du Monde) and Line Ton That (Groupe La Poste). The network's France director, Andrea Lavergne, is recorded as a connector.
- **Organisers of Python, R and ML groups:** the Meetup event hosts of [PyLadies Paris](https://www.meetup.com/pyladiesparis/) (Simona Bottani, Chiara Biscaro, Mojdeh Rastgoo, Anuradha Kar), [RLadies+ Paris](https://www.meetup.com/rladies-paris/) (Mouna Belaid) and [Paris WiMLDS](https://www.meetup.com/paris-women-in-machine-learning-data-science/) (Caroline Chavier, Juliette Bassnagel) are recorded as connectors. PyLadies Paris also gave one data-science tooling talk, by Marie Sacksick of probabl.
- **[Women in AI France](https://www.womeninai.co/france):** the team page gives 3 connectors with data and AI roles: Léa El Samarji (Avanade), Alix Barel (Microsoft) and Ania Kaci (IBM). It lists no dated events.

### Job ads

- **LinkedIn Jobs, logged out:** search `keywords=dbt&location=Paris, Île-de-France`. From the browser page, list the ads with in-page `fetch()` on `/jobs-guest/jobs/api/seeMoreJobPostings/search?...&start=N`, fetch each ad from `/jobs-guest/jobs/api/jobPosting/<id>`, and keep the ads whose text contains the whole word `dbt`. The script is in the [Baltic city notes](../baltics/SEARCH_METHOD.md#job-ads). On 2026-09-24, 300 ads were listed and 250 checked, and 120 mentioned dbt. The run stopped at a 250-ad cap, so 50 were left unchecked.
- **ATS search:** `site:jobs.lever.co`, `site:job-boards.greenhouse.io` and `site:jobs.ashbyhq.com` with dbt Paris. These added 27 ads from in-house tech companies that LinkedIn's ranking missed (Mistral AI, Pigment, BeReal, Aircall). Their `dbt_snippet` is the search engine's summary, marked "[search summary]".
- **Welcome to the Jungle:** use `site:welcometothejungle.com` searches, because search URLs on the site now go to a login page.
- **Company job boards:** the open JSON boards at Greenhouse, Lever and Ashby, tried for about 90 Paris employers. 39 boards answered, and 12 had a Paris ad whose text has the word dbt. They raised Pigment, Voodoo and Pennylane to strong and confirmed Snowflake's Paris office. They found no new companies, because the LinkedIn pass had already listed them.
- **GitHub code search:** `filename:dbt_project.yml org:<org>` found public dbt projects at [beta.gouv.fr](https://github.com/betagouv), the ecological transition ministry's digital team ([MTES-MCT](https://github.com/MTES-MCT)), [GIP Plateforme de l'inclusion](https://github.com/gip-inclusion) and [pass Culture](https://github.com/pass-culture/data-gcp). French public-sector teams publish their code, so their GitHub organisations are worth checking.
- **Meetup hosts:** gql2 past events of Modern Data Stack France and Databricks France name the hosts. dcube presented a client architecture built on dbt in [June 2024](https://www.meetup.com/modern-data-stack-france/events/301317296/). Data Reply France and I-Shane hosted Databricks evenings.

### Chapter history

- **Past speakers:** every named speaker in `../enriched/paris-dbt-meetup.json` (10 events, Sept 2022 to Sept 2025) was added as a person, with their talk as `speaker_evidence`. They are tier 2 unless other evidence puts them in tier 1, and `sourced_via` includes `chapter_meetup_history`.
- **First names only:** speakers listed by first name only (e.g. "Nolwenn, Taha") were skipped.
- **No recent events:** as of 2026-09-24 the chapter had no events after Paris dbt meetup #8 (2025-09-30).

## 2. What didn't work here

- **Low-yield meetups:** Modern Data Stack France, the Snowflake and Databricks user groups (mostly vendor-led or online) and PyData Paris (scientific Python).
- **Paris Data Engineers:** the group no longer exists.
- **Welcome to the Jungle search URLs:** they go to a login page.
- **Paris WiMLDS:** almost all ML.
- **PyLadies Paris (`pyladiesparis`) and R-Ladies Paris:** mostly Python, ML and R content. Only their organisers and one tooling talk were kept.
- **Women in Big Data Paris:** its masterclasses and the November 2025 10-year event named no speakers. Only the June 2025 afterwork did.
- **WiDS Paris:** the [Meetup group](https://www.meetup.com/Women-in-Data-Science-WiDS-Paris/) has held no event since 2017.
- **[Social Builder](https://socialbuilder.org/evenements/) and [Girls in Tech France](https://girlsintech.org/france/):** the events page returned almost no content, and the Girls in Tech request timed out.
- **Duchess France, Women Techmakers and Ladies of Code Paris:** nothing data-related.
- **Speakers picked from conference bios:** some Forward Data Conference speakers were picked using wording in their conference bios. Those people are tagged `sourced_via: conference_or_meetup_agenda`, not `women_in_data_community`, and the dataset records no gender for anyone. Take women-in-data speakers only from the community's own events.
- **HN Who is hiring:** no Paris ad since 2023 mentions dbt.
- **dbt Labs case-study file:** it has no Paris company. The French-language Groupe Holder case study is not in it.
- **Job boards under the obvious name:** leboncoin, Criteo, Dailymotion, ManoMano, Deezer, Spendesk, Mirakl, Brevo, PayFit, Photoroom and Sorare have no open Greenhouse, Lever or Ashby board under that name.
- **Small user groups:** the Paris Snowflake User Group has had 3 events since 2024, all at Devoteam. DuckDB Paris has none.

## 3. Companies looked at

- **Consultancies dominate Paris dbt hiring:** SKIILS, Devoteam, JAKALA, Talan, CGI, Capgemini and others. For speaker sourcing, filter `type == "employer"`.
- **Employers with several dbt ads:** Dashlane, Accor, Leetchi, Joko, Implicity, Leonar and Axway. Employers with one ad include Alan, Shine, Skello, Alma, pass Culture, Aircall and BeReal.
- **A different stack:** leboncoin uses the Coalesce transformation tool, not dbt.
- **Labelled staff:** dbt Labs' Paris-related staff and Fivetran staff are labelled in the cockpit. `excluded_from_outreach` is true only for internal records (Vinted).

<!-- companies:start -->
249 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (112)</summary>

1G-LINK, Accor, Actinvision, Aircall, Alan, Alma, ALTEN, Altertable, Artefact, Aubay, Back Market, BeReal, beta.gouv.fr, Bigblue, BlaBlaCar, Capgemini Invent, Caprikorn, Cartelis, CGI, Contentsquare, Cozi, Dashlane, DataGen (Robin Conquet), Dataworks, Davidson consulting, dbt Labs, dcube, Decathlon / Decathlon Digital, DEODIS, Devoteam, Doctolib, DPD France, Ekwateur, Elax Energie, EY, Fabrique numérique du ministère de la Transition écologique (MTES-MCT), Fitness Park, Free2move, FullEnrich, GazelTech, GIP Plateforme de l'inclusion (local presence not confirmed), GLOBE GROUPE SHOPPER HOUSE, Groupe EOLEN, Havas Media France, ICADE, Implicity, In Tandem, Infinite Lambda, INFOGENE, Innoha, Innova Solutions, Ippon Technologies, JAKALA, Jems Group, Joko, Kaino, Key Performance Consulting (KPC), Kiiro, Ledger, Leetchi, Lenstra, Leonar, Luxurynsight, M13h, Macif (local presence not confirmed), Malt, Manutan Group, Mediaperformances, MeltOne Advisory, Modeo, mym, nao Labs, Neosoft, NEXTON, Odaseva, Onepoint, Optimize matter, Ornikar, Orus, Oventi, pass Culture, Pennylane, Pigment, PREREQUIS, Pretto, Pyl.Tech, QOLIBRIS, Qonto, Qover (local presence not confirmed), Sancare, SEVETYS, Shift Technology, Shine, Sia, Skello, SKIILS, Smartpoint, Smile, STORM GROUP, Swile, Talan, The Information Lab, Trade Republic, TRIMANE, Valtech, VISEO, Voodoo, WeeFin, WHIZE, Yuri & Neil, Zefir, Édifice

</details>

<details><summary><b>Some dbt signal</b> (36)</summary>

Agoda, Axway, blef.fr (Data News), Blent.ai (local presence not confirmed), Brevo, BROTHER FRANCE, Capgemini, CastorDoc (Coalesce), Catalina Marketing France, Converteo, Datadog (Paris), Decathlon, Emeria, Equativ, eXalt Value, Gorgias, Kestra, Keyrus, Kolecto, Lacoste, LineUP7, Mirakl, Mistral AI, Quickscale AI, Riot, SFEIR, Sifflet, Snowflake, Spendesk, Stuart (local presence not confirmed), Tellent, Theodo Data & AI (ex-Sicara), Vestiaire Collective, Vibe.co, Xebia France, Yield Studio & Advisory

</details>

<details><summary><b>Not verified</b> (95)</summary>

AB Tasty, Agicap / Libeo, Air France-KLM, Airbyte (local presence not confirmed), Ankorstore, Aquila Data Enabler, Aramis Group, BearingPoint, Believe, BNP Paribas / AXA / Société Générale, Brigad (local presence not confirmed), Brigad / Side, Carbonfact, Carrefour, Clean Data Architecture, Clever Cloud, Count (local presence not confirmed), Criteo, Dailymotion, Data Reply France, Data Value Consulting (local presence not confirmed), DataGalaxy, Dataiku, Deezer, Dust, Département du Gard (local presence not confirmed), Ekimetrics, ENGIE, Eurazeo, Evaneos, ex-Galeries Lafayette (local presence not confirmed), Fifty-five, Freelance (Back Market mission) (local presence not confirmed), Galeries Lafayette, Getaround, GitGuardian, GRDF (at time of talk) (local presence not confirmed), Groupe La Poste, Hightouch (local presence not confirmed), Hivebrite, Hubvisor (local presence not confirmed), Hugging Face, Hymaïa, I-Shane, Jolimoi, L'Oréal, Lalilo (local presence not confirmed), leboncoin (Adevinta), Lightdash (local presence not confirmed), Luko / Leocare / Lalilo, LVMH / Sephora, Lydia / Sumeria, Maketools, ManoMano, Metabase (local presence not confirmed), Mooncard, MotherDuck (local presence not confirmed), Neo4j (ex-Sifflet) (local presence not confirmed), Nibble (local presence not confirmed), Nissan United AMIEO (local presence not confirmed), Numberly (1000mercis Group), OCTO Technology (Accenture), Omni (local presence not confirmed), Open Value, Optic 2000, Owkin (at time of 2024 talk) (local presence not confirmed), Paris Data Ladies, Paris Women in Machine Learning & Data Science, PayFit, Photoroom, Pigment / Yousign / Payplug, Positive Thinking Company (local presence not confirmed), PyLadies Paris, R-Ladies Paris, Scaleway, Selfr (local presence not confirmed), Sicara, SNCF Connect & Tech, Social Good Accelerator, Sopht, Sorare, Stellantis, Supabase (local presence not confirmed), Taktile (local presence not confirmed), TotalEnergies, TotalEnergies Renewables, Toucan, Ubisoft / Dailymotion / Le Monde / Radio France, Van Cleef & Arpels, Veesion, Welcome to the Jungle, Weld (local presence not confirmed), Women in Big Data Paris, Ynsect, Zenika

</details>

<details><summary><b>Uses a different stack</b> (6)</summary>

DGFiP (Ministère de l'Économie et des Finances), iAdvize (local presence not confirmed), Maisons du Monde (local presence not confirmed), probabl, Thales, Women in AI France

</details>

<details><summary><b>Blogs and sites scanned</b> (66)</summary>

- Amplitude case study (search only)
- Amplitude webinar recap
- Coalesce case study
- DataGen newsletter
- DataGen podcast
- DataGen podcast episodes #142, #184, #211, #255
- Fivetran case study (search summary)
- Infinite Lambda webinar page
- Monte Carlo case study (search summary)
- Tasmane case study (search only)
- https://airbyte.com/blog-authors/michel-tricot
- https://blent.ai/thematique/data-engineering
- https://blog.malt.engineering/ (feed tagged dbt)
- https://blog.octo.com/tag/data
- https://converteo.com/blog/
- https://data-ai.theodo.com/blog-technique
- https://datageneration.substack.com/
- https://datageneration.substack.com/archive
- https://deezer.io/ (search only)
- https://ekimetrics.github.io/blog/
- https://engineering.contentsquare.com/
- https://engineering.hivebrite.io/
- https://engineering.pigment.com/
- https://engineering.pigment.com/ (search only)
- https://getnao.io/blog/
- https://infinitelambda.com/blog/
- https://kestra.io/blogs
- https://keyrus.com/fr/actualites
- https://medium.com/accor-digital-and-tech (feed tagged dbt)
- https://medium.com/alan (feed tagged data)
- https://medium.com/artefact-engineering-and-data-science
- https://medium.com/blablacar (feed tagged dbt)
- https://medium.com/decathlondigital (feed tagged dbt: empty)
- https://medium.com/doctolib (feeds tagged data, dbt)
- https://medium.com/gorgias-engineering/building-a-context-layer-from-the-ground-up-d6f72713915a
- https://medium.com/leboncoin-tech-blog (feed tagged dbt: empty)
- https://medium.com/manomano-tech (feed tagged dbt: empty)
- https://medium.com/payfit (search only)
- https://medium.com/pennylane-engineering (search only)
- https://medium.com/qonto-way (feed tagged data)
- https://medium.com/stuart-engineering (feed tagged dbt: empty)
- https://medium.com/swile-engineering
- https://medium.com/wttj-tech (search only)
- https://medium.com/yousign-engineering-product (search only)
- https://mirakl.tech/subpage/tech (search only)
- https://shows.acast.com/data-gen
- https://shows.acast.com/data-gen/episodes
- https://www.aquiladata.fr/
- https://www.blef.fr/blog/
- https://www.castordoc.com/blog-category/data-tooling
- https://www.clever-cloud.com/blog/tag/data/
- https://www.datagalaxy.com/en/category/events/
- https://www.dataiku.com/blog/tech-blog
- https://www.devoteam.com/expert-view/
- https://www.meetup.com/paris-dataladies/
- https://www.meetup.com/paris-women-in-machine-learning-data-science/
- https://www.meetup.com/pyladiesparis/
- https://www.meetup.com/rladies-paris/
- https://www.meetup.com/women-in-big-data-paris-meetup-group/
- https://www.modeo.ai/articles
- https://www.siffletdata.com/blog
- https://www.theodo.com/en-fr/blog
- https://www.toucantoco.com/en/tech-blog
- https://zenika.com/
- jobs.lydia-app.com (search only)
- search only

</details>

<details><summary><b>Other sources checked</b> (69)</summary>

- [Medium RSS feeds (publication/tagged/<tag>)](https://medium.com/feed/<publication>/tagged/dbt)
- [DataGen newsletter (Substack)](https://datageneration.substack.com/)
- [DataGen podcast (Acast/Spotify)](https://shows.acast.com/data-gen)
- [Contentsquare Engineering Blog](https://engineering.contentsquare.com/)
- [Coalesce (CastorDoc) customer stories](https://coalesce.io/customer-stories/)
- [Infinite Lambda / dbt Labs webinar](https://infinitelambda.com/business-events/modernisation-et-migration-data-webinar-macif/)
- [Forward Data Conference site](https://www.forward-data-conference.com/) (nothing useful)
- [Medium publication web pages](https://medium.com/alan/tagged/data-engineering) (nothing useful)
- [getdbt.com case studies](https://www.getdbt.com/case-studies) (nothing useful)
- [Blog Ippon dbt tag](https://blog.ippon.fr/tag/dbt/)
- [Modeo blog](https://www.modeo.ai/articles)
- [Theodo blog](https://www.theodo.com/en-fr/blog)
- [Artefact Medium](https://medium.com/artefact-engineering-and-data-science)
- [Converteo blog](https://converteo.com/blog/)
- [Infinite Lambda events](https://infinitelambda.com/migrating-informatica-to-dbt-meetup/)
- [DataGen podcast (Acast) / substack](https://shows.acast.com/data-gen)
- [blef.fr talks](https://www.blef.fr/talks/) (nothing useful)
- [Kestra blog](https://kestra.io/blogs)
- [Sifflet blog / Luma](https://luma.com/b3ng9yzj)
- [Devoteam expert view](https://www.devoteam.com/expert-view/data-documentation-approach-for-your-snowflake-and-dbt-stack/) (nothing useful)
- [OCTO Talks](https://blog.octo.com/) (nothing useful)
- [Hivebrite / Pigment engineering blogs](https://engineering.pigment.com/) (nothing useful)
- [Paris dbt Meetup (meetup.com)](https://www.meetup.com/paris-dbt-meetup/) (nothing useful)
- [Forward Data Conference 2026 talks and speakers](https://forward-data-conference.com/en/program/talks/2026)
- [Forward Data Conference 2025 talks and speakers](https://forward-data-conference.com/en/program/talks/2025)
- [Forward Data Conference 2024 talks and speakers](https://forward-data-conference.com/en/program/talks/2024)
- [Paris Apache Airflow Meetup](https://www.meetup.com/paris-apache-airflow-meetup/)
- [Paris Data Ladies](https://www.meetup.com/paris-dataladies/)
- [DuckDB Paris Meetup (duckdb.org / Luma)](https://duckdb.org/events/2026/09/24/duckdb-paris-meetup/)
- [ClickHouse Meetup Paris (Luma, hosted by Qonto)](https://luma.com/phsg70v9)
- [Snowflake User Group Paris](https://usergroups.snowflake.com/paris/)
- [Modern Data Stack France (meetup.com)](https://www.meetup.com/modern-data-stack-france/) (nothing useful)
- [Databricks France Meetup](https://www.meetup.com/databricks-france-meetup/) (nothing useful)
- [Paris Data Engineers (meetup.com)](https://www.meetup.com/paris-data-engineers/) (nothing useful)
- [PyData Paris 2025 (pretalx schedule)](https://pretalx.com/pydata-paris-2025/talk/) (nothing useful)
- [DataGen podcast (Acast)](https://shows.acast.com/data-gen/episodes)
- [blef.fr Data News](https://www.blef.fr/data-news-dbt-coalesce-2025)
- [Paris Data and AI Product Management meetup (Luma)](https://luma.com/paris-dpm-meetup) (nothing useful)
- [Big Data & AI Paris](https://www.bigdataparis.com/en-gb.html) (nothing useful)
- [Coalesce / dbt Summit speakers from Paris](https://coalesce.getdbt.com/event/21662b38-2c17-4c10-9dd7-964fd652ab44/speakers) (nothing useful)
- [meetup.com via browser pane](https://www.meetup.com/) (nothing useful)
- [LinkedIn Jobs guest API (keywords=dbt, Paris, Île-de-France)](https://www.linkedin.com/jobs/search?keywords=dbt&location=Paris%2C%20%C3%8Ele-de-France%2C%20France)
- [Welcome to the Jungle job search](https://www.welcometothejungle.com/fr/jobs?query=dbt&refinementList%5Boffices.country_code%5D%5B%5D=FR&aroundQuery=Paris) (nothing useful)
- [Web search: "dbt" "analytics engineer" Paris](https://fr.indeed.com/q-analytics-engineer-dbt-emplois.html) (nothing useful)
- [Web search: site:welcometothejungle.com dbt Paris (DE + AE queries)](https://www.welcometothejungle.com/fr/companies/dashlane/jobs/analytics-engineer_paris_b7zkyuds)
- [Web search: site:jobs.lever.co dbt Paris](https://jobs.lever.co/)
- [Web search: site:job-boards.greenhouse.io dbt Paris](https://job-boards.greenhouse.io/)
- [Web search: site:jobs.ashbyhq.com dbt Paris](https://jobs.ashbyhq.com/)
- [Web search: site:apply.workable.com dbt Paris](https://apply.workable.com/) (nothing useful)
- [Web search: site:jobs.smartrecruiters.com dbt Paris](https://jobs.smartrecruiters.com/AccorCorpo/744000124376311-tech-lead-data-analytics-snowflake-dbt-tableau-f-h-x)
- [Paris Data Ladies (Meetup, gql2 past events)](https://www.meetup.com/paris-dataladies/)
- [Paris WiMLDS (Meetup)](https://www.meetup.com/paris-women-in-machine-learning-data-science/)
- [PyLadies Paris (Meetup urlname 'pyladiesparis')](https://www.meetup.com/pyladiesparis/) (nothing useful)
- [R-Ladies Paris (Meetup)](https://www.meetup.com/rladies-paris/) (nothing useful)
- [Women in Big Data Paris (Meetup)](https://www.meetup.com/women-in-big-data-paris-meetup-group/) (nothing useful)
- [WiDS Paris (Meetup)](https://www.meetup.com/women-in-data-science-wids-paris/) (nothing useful)
- [Duchess France](https://www.duchess-france.fr/) (nothing useful)
- [Women Techmakers Paris / Ladies of Code Paris](https://luma.com/joisxg95) (nothing useful)
- [Data For Good](https://www.meetup.com/fr-fr/data-for-good-fr/) (nothing useful)
- [Forward Data Conference speakers 2024-2026](https://forward-data-conference.com/program/speakers/)
- [Coalesce speakers from Paris](https://sessionize.com/coalesce-2024/) (nothing useful)
- [Meetup gql2 groupSearch near Paris (women-in-data queries)](https://www.meetup.com/gql2#groupSearch-paris-wid)
- [Paris Data Ladies 2025-2026 events (Meetup gql2)](https://www.meetup.com/paris-dataladies/events/?type=past)
- [PyLadies Paris (Meetup gql2 past events)](https://www.meetup.com/pyladiesparis/events/?type=past)
- [Paris WiMLDS 2024-2026 events (Meetup gql2)](https://www.meetup.com/paris-women-in-machine-learning-data-science/events/?type=past)
- [WiDS Paris (Meetup gql2, urlname Women-in-Data-Science-WiDS-Paris)](https://www.meetup.com/Women-in-Data-Science-WiDS-Paris/) (nothing useful)
- [Women in AI France team page](https://www.womeninai.co/france)
- [Social Builder events page](https://socialbuilder.org/evenements/) (nothing useful)
- [Girls in Tech France](https://girlsintech.org/france/) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

Tier 1 is stricter here than the central rule. The first build proposed 52 tier-1 people, so tier 1 was kept only for people in Paris (or not known to be elsewhere) with an item from 2024 onwards that mentions dbt, and for first-time speakers under the shared rule. Everyone else moved to tier 2, which left 37 tier-1 people in the first build. The most common topics are `genai & llm`, data governance, team & org design and analytics engineering.

- **First-time speakers** (people who write but have no talk yet):
  - **Doctolib:** Jason Nathaniel V and Alexandre Guitton.
  - **Ippon:** Jeremy Nadal, Grégoire Naud, Nicolas Hong, Paul Colinmaire and Mathis Le Gall.
  - **Contentsquare:** Corentin Flacher, Pierre Munhoz and Thales Loiola Ravelli.
  - **Qonto:** Maxime Damery and Timothée Dehouck.
  - **Others:** Sebastien de Larquier (Alan), Matthieu Willot (Modeo) and Martin-Pierre Roset (Kestra).
- **Anchor speakers** (strong tier-1 dbt speakers):
  - **Tushar Bhasin and Antoine Lefebvre (BlaBlaCar):** dbt Core on Airflow at 4,000 tables.
  - **Thierry Sallé (Malt):** migrating to dbt on BigQuery, having rejected SQLMesh.
  - **Ismail Mezzour (Accor):** dbt, Airflow and Cosmos for 80+ engineers.
  - **Charles André (Qonto):** many domain-owned dbt repos, data contracts and an AI on-call agent.
  - **Romain Fays (Doctolib), Matthieu Colin (Back Market) and Bastien Caunègre (Ornikar):** analytics engineering set-ups described on DataGen.
  - **Hugo Palmer and Benjamin Joyen-Conseil (Decathlon).**
  - **Emma Wagner (Gorgias):** a context layer for analytics agents.
  - **Infinite Lambda:** the team behind the Macif migration from Informatica to dbt.
- **Women-in-data community leads:**
  - **Juliette Chabbal (Ippon):** semantic layer.
  - **Others:** Lucille Fargeau (Doctolib), Anaïs Ghelfi (Malt), Sarah Richard and Yasmine Touzene (Aramis Group), Sophie Ly (Decathlon) and Kateryna Kolodnytska (Nissan).
- **Connectors:**
  - **Charlotte Ledoux:** organiser of Paris Data Ladies.

## 5. Before outreach

- [ ] **Check Anouar Hnini.** Anouar Hnini is probably in Ireland and may have left dbt Labs.
- [ ] **Check Jason Vazelle (Doctolib).** Jason Vazelle may have moved abroad.
- [ ] **Check a possible duplicate.** Benjamin Joyen and Benjamin Joyen-Conseil (Decathlon) may be one person.
- [ ] **Check a spelling.** William Horel's surname also appears as Horrel.
- [ ] **Confirm Ippon authors are in Paris.** Jeremy Nadal and Mathis Le Gall are placed in Bordeaux, and Nicolas Hong near Nantes.
- [ ] **dbt Labs and Fivetran staff are labelled.** They can speak, but check the line-up has practitioners first.
- [ ] **Pronouns:** none were found that people had stated themselves, so all are `null`.

## 6. Next run

- **Sources to try first:**
  - **LinkedIn pass:** 127 people are still `not_searched`. In the first build only 14 of the 105 tier-1/2 people without a profile were searched before the web-search limit. Finish this first, in its own session.
  - **New content since `metadata.generated_at`:** new DataGen episodes and posts, the latest Forward Data Conference programme, new Paris dbt Meetup, Paris Data Ladies, Paris Airflow and DuckDB Paris events, and new posts on the blogs in `sources.checked`.
  - **Job ads:** re-run the LinkedIn Jobs guest scan and the Lever, Greenhouse and Ashby searches, including the 50 ads left over by the cap.
  - **Women-in-data groups not yet scanned:** Femmes@numérique, Data For Good and Les Pionnières. Social Builder and Girls in Tech France were not reachable, so retry them in a browser. Women in AI France lists no events, so look for #WAITalks speakers on its news page.
  - **Women-in-data events:** new Paris Data Ladies and Women in Big Data Paris events with named speakers.
- **People to locate:** 15 people have no known location, including Willis Nana, whose LinkedIn result had nothing tying it to the recorded talk. The 4 tier-1 leads among them are Grégoire Naud, Paul Colinmaire, Thales Loiola Ravelli and Martin-Pierre Roset.
- **Data conventions:** `metadata.region` is "Paris (Paris dbt Meetup)". `sources.checked` lists every source checked, with a `yielded` flag. `past_meetups` is copied from `../enriched/paris-dbt-meetup.json`. Person `content_id`s have the form `<event-slug>-<title-slug>`.
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `paris/paris_dbt_companies.json`, the Paris dbt Meetup, `../enriched/paris-dbt-meetup.json` and the region Paris / Île-de-France. Add: "Content is often in French, so search in French too and record French titles as they are, with an English description. Tier 1 = Paris or unknown location plus a dbt item from 2024 onwards, or a first-time speaker under the shared rule. Back up the old file as `paris_dbt_companies.v<N>.json`."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-24 | 1 | First search, with 5 parallel sub-agents covering large companies, partners/vendors/media, meetups and conferences, job ads, and women-in-data communities, plus chapter history. 238 companies (94 on the watchlist), 186 people, 147 dbt job ads at 109 companies, 207 unique content items. Split: 137 proven speakers, 26 emerging voices, 8 featured, 16 with no public content. Tiers: 37 tier 1, 86 tier 2, 54 tier 3, 9 connectors. 17 people had already spoken at the Paris dbt Meetup. The LinkedIn pass is incomplete because the web-search limit was reached; 38 people have LinkedIn URLs. |
| 2026-09-24 | 2 | Rebuilt with the same merge rules; adds 3 job ads the v1 build had dropped (150 in total), otherwise unchanged. Backup: `paris_dbt_companies.v1.json`. |
| 2026-10-01 | 3 | Location pass and LinkedIn pass, by the evidence rules in `../research/README.md`. Public pages placed 4 people: co-written Ippon posts and in-person talks at the chapter. LinkedIn search results placed 5 more. Of the 9 placed, 3 are in Paris and 6 elsewhere (Bordeaux, Nantes, Lille, Niort and Lyon). 18 people are still unknown. |
| 2026-10-01 | 4 | Women-in-data pass from Meetup data and the Women in AI France team page. 21 people added: 8 speakers and panellists from Paris Data Ladies, Women in Big Data Paris and PyLadies Paris, plus 13 organisers as connectors. WiDS Paris is inactive. Social Builder and Girls in Tech France were not reachable. |
| 2026-10-01 | 5 | Company pass from fetches: company job boards, HN Who is hiring, the dbt Labs case-study file, GitHub code search and Meetup hosts. Companies went from 244 to 250, and job ads from 150 to 160. 4 new companies have a strong dbt signal, 3 of them public-sector teams with public dbt projects. Pigment, Voodoo and Pennylane were raised to strong. |
