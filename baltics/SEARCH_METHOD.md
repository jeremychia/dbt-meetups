# Vilnius: city notes

This file holds what is specific to Vilnius. The method, scoring rules, schema and replication prompt are in the [central search method](../research/README.md).

- **Chapter:** [Baltic dbt Meetup](https://www.meetup.com/vilnius-dbt-meetup/), data in `lithuania_dbt_companies.json`
- **Region:** Lithuania, mainly Vilnius and Kaunas.
- **First built:** 2026-09-23
- **Language:** search in English and Lithuanian.

<!-- at-a-glance:start -->
**At a glance** (version 10, 2026-10-01)

| | Count |
|---|---|
| Companies | 61 |
| People | 120 |
| Tier 1 leads | 15 |
| First-time speakers (publish, no talk yet) | 5 |
| Proven speakers | 27 |
| Spoke at this chapter before | 5 |
| Based in the region | 62 |
| Based elsewhere | 2 |
| Location unknown | 56 |
| With a LinkedIn profile | 108 |
| Job ads mentioning dbt | 62 |
| Past chapter meetups | 2 |
<!-- at-a-glance:end -->

## 1. Where to look in Vilnius

### Job ads

Job ads are the most reliable sign that a Lithuanian company uses dbt, because companies list their real tools. Most Lithuanian leads came from this search.

- **LinkedIn Jobs, logged out:** the best company signal. Search [linkedin.com/jobs/search?keywords=dbt&location=Lithuania](https://www.linkedin.com/jobs/search?keywords=dbt&location=Lithuania), which works without logging in. The keyword search is loose: it returned 415 ads, but only 43 mentioned dbt in the ad text. So fetch each ad's full description and check it for the whole word `dbt` with the scanner below. Each ad page also shows who posted it ("Meet the hiring team"), which can give a named contact.
- **CVbankas.lt:** [cvbankas.lt/?keyw=dbt](https://www.cvbankas.lt/?keyw=dbt) searches the ad text and catches Lithuanian-language ads. It found Artea bankas, Lietuvos bankas, IKI and Ltintus.
- **CVMarket.lt:** [the dbt keyword search](https://www.cvmarket.lt/joboffers.php?op=search&search%5Bkeyword%5D=dbt) now searches the ad text. It returned 30 ads, and each ad page gives the full text and the posting date. It added Wargaming's Vilnius analytics engineer ad, which owns dbt Cloud. Some ads come from a sister company with the same text, such as Tesonet Global for Oxylabs and UAB Helis Play for Eneba.
- **Company job boards:** the Greenhouse, Lever and Ashby boards of about 60 Lithuanian employers. Eneba, Oxylabs, Surfshark, Welltech, Ruby Labs and Mediatech had Lithuanian ads that say dbt.
- **Meetup hosts:** Meetup gql2 past events of the Vilnius Snowflake, PyData, SEB Talks IT and Danske Tech groups. They confirm Infotrust, SEB and Danske Bank in Vilnius, with no dbt seen. A [PyData Vilnius talk](https://www.meetup.com/pydata-vilnius/events/299190786/) (2024-02) covers dbt Python models at Surfshark.
- **GitHub organisation repositories:** TransferGo publishes [a fork of dbt-checkpoint](https://github.com/TransferGo/dbt-checkpoint).
- **Web search in English:** `dbt data engineer Vilnius`, `analytics engineer Vilnius dbt`, `data scientist Kaunas dbt`.
- **Web search in Lithuanian:** `dbt duomenų analitikas`, `"dbt" duomenų inžinierius`, `duomenų mokslininkas dbt`.
- **Job platforms:** `"dbt" Vilnius site:teamtailor.com OR site:greenhouse.io OR site:jobs.lever.co OR site:ashbyhq.com`.
- **LinkedIn rate limits:** fetching ads in parallel hits HTTP 429 almost at once. Fetch one at a time, about 2–2.5 seconds apart, and back off for 15 seconds or more after a 429. Scanning about 415 ads takes about 20 minutes.

<details><summary><b>LinkedIn job-ad scanner</b> (run inside the browser on a linkedin.com page)</summary>

```js
// Runs in the background. Check progress with: JSON.stringify({n:Object.keys(_S.jobs).length, checked:_S.checked, hits:_S.hits.length, done:_S.done})
window._S = {jobs:{}, hits:[], done:false, checked:0, log:[]};
const sleep = ms => new Promise(r => setTimeout(r, ms));
async function get(u){ for (let i=0;i<6;i++){ const r = await fetch(u); if (r.status==200) return await r.text();
  _S.log.push(r.status+' '+u.slice(0,60)); await sleep(15000*(i+1)); } return ''; }
(async () => {
  for (let s=0; s<=990; s+=10) {                       // list pages
    const t = await get(`/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=dbt&location=Lithuania&start=${s}`);
    const d = new DOMParser().parseFromString(t,'text/html'); const lis = d.querySelectorAll('li');
    if (!lis.length) break;
    lis.forEach(li => { const u = li.querySelector('a.base-card__full-link')?.href?.split('?')[0];
      const id = u?.match(/(\d+)$/)?.[1];
      if (id) _S.jobs[id] = {id, u, c: li.querySelector('.base-search-card__subtitle')?.innerText.trim(),
                                   t: li.querySelector('.base-search-card__title')?.innerText.trim()}; });
    await sleep(2500);
  }
  for (const j of Object.values(_S.jobs)) {            // each ad's text
    const t = await get(`/jobs-guest/jobs/api/jobPosting/${j.id}`); _S.checked++;
    const d = new DOMParser().parseFromString(t,'text/html');
    const txt = d.querySelector('.show-more-less-html__markup')?.innerText || '';
    const m = txt.match(/.{0,100}\bdbt\b.{0,100}/i);
    if (m) { j.snip = m[0].replace(/\s+/g,' ');
      const rec = d.querySelector('.message-the-recruiter');
      j.poster = rec ? rec.innerText.replace(/\s+/g,' ').trim() : null;
      j.posterUrl = rec?.querySelector('a[href*="/in/"]')?.href.split('?')[0] || null;
      _S.hits.push(j); }
    await sleep(2000);
  }
  _S.done = true;
})();
```

The meetup event pages can be read the same way: open any meetup.com page, then `fetch('/vilnius-dbt-meetup/events/<id>/')` and read `#event-details`.

</details>

### People at the dbt companies

- **LinkedIn search results:** searches such as `site:lt.linkedin.com/in "Analytics Engineer" "<Company>"`, `site:linkedin.com/in "<Company>" dbt Vilnius` and `site:lt.linkedin.com/in dbt ...` for profiles that mention dbt or dbt certification.
- **theorg.com:** org charts for data teams (Surfshark, twoday, Eldorado.gg).
- **Company careers blogs:** for example [career.oxylabs.io](https://career.oxylabs.io).

### Meetups and conferences

- **Past Baltic dbt Meetup agendas:** event pages at [meetup.com/vilnius-dbt-meetup](https://www.meetup.com/vilnius-dbt-meetup/) (events 303809378 and 306239130). Past speakers are proven and easy to invite back.
- **PyCon Lithuania 2024–2026 on pretalx.com:** the most useful conference source. Speaker pages give full bios, often with the tools the speaker uses.
- **Others:** Big Data Conference Europe ([bigdataconference.eu](https://bigdataconference.eu)), PyData Vilnius and Coalesce on-demand talks (getdbt.com).

### Community content and first-time speakers

- **Uncle Data newsletter and podcast:** by Tomas Peluritis. It is the centre of Lithuania's data community, and the guests are good leads.
- **Company blog posts that name the author:** Omnisend's Feb 2026 post was the only dbt engineering-blog post by a big Lithuanian dbt employer.
- **GitHub repos whose profiles list Vilnius:** for example `vilnius-pub`.
- **LinkedIn posts in which a data leader lists the team's stack:** for example Ignitis.
- **Other places searched for first-time speakers:** Medium, Substack, dev.to and Hashnode; the engineering blogs of Kilo Health, Nord Security, Oxylabs, Surfshark, Hostinger, Omnisend, TransferGo, Eneba and PVcase; Lithuanian-language content; the dbt Community forum; `site:linkedin.com/posts` with dbt plus Vilnius, Kaunas or a company name, Lithuanian phrases (`"dbt" duomenų`) and "dbt Certified"; and posts about attending a past Baltic dbt Meetup or Coalesce.

### Women-in-data communities

- **How people are found:** speakers and organisers come from these communities' own events and are tagged `sourced_via: women_in_data_community`. Nobody's gender is recorded. Pronouns are recorded only when self-published, and none were.
- **[PyLadies Lithuania](https://www.meetup.com/pyladies-lithuania/):** the only women-in-data group on Meetup in Lithuania, with 128 members since 2024. It runs meetups at Oxylabs and Flo, and workshops at PyCon Lithuania. Its [2026 web scraping workshop](https://www.meetup.com/pyladies-lithuania/events/313810308/) gave two Oxylabs speakers, Karolina Šarauskaitė and Ieva Šataitė. Its organisers Inga Pliavgo and Enrika Vyšniauskaitė are connectors.
- **[Women Go Tech](https://www.womengotech.com/):** a Lithuanian mentoring organisation with Data & Analytics and Data Science mentor tracks. Its [about page](https://www.womengotech.com/about-us/) gave 5 team members as connectors. Ieva Šūmakarytė spoke for it at [PyLadies Lithuania](https://www.meetup.com/pyladies-lithuania/events/303387292/) in 2024. Its public events since 2025 are two online AI webinars, read through `/wp-json/tribe/events/v1/events`.
- **Also ask:** PyLadies Lithuania and Women Go Tech for women in data roles at the dbt employers. Women Go Tech's mentor pages list data engineers and analysts without employers.

## 2. What didn't work here

- **CV-Online keyword search:** only matches job titles, so a dbt search returns nothing. CVMarket now works (section 1).
- **HN Who is hiring:** no Lithuanian ad since 2023 mentions dbt.
- **GitHub code search:** it hit the shared rate limit. Repository lists of 16 Lithuanian organisations found dbt only at TransferGo.
- **meetup.com attendee lists:** need a login.
- **LinkedIn people search:** needs a login, and search engines index only a small share of profiles.
- **`site:linkedin.com/posts dbt ...`:** noisy. It returns worldwide results and therapy "DBT" (dialectical behaviour therapy).
- **Big Data Conference Europe speaker pages:** loaded by script, so plain fetches get nothing. Use the browser.
- **The fetch tool on job boards:** timed out. The built-in browser plus in-page `fetch()` worked instead.
- **Other groups found by the search:** [Tech Kinship](https://www.meetup.com/tech-kinship/) has 3,028 members but runs Lithuanian-language talks on leadership and work culture. PyLadies Lithuania's 2025 Python data workshop does not name its instructors.
- **Women-in-data networks with no Lithuanian chapter:** Meetup's group search found no R-Ladies, Women Techmakers, WiDS, WiMLDS, She Loves Data, Women in Big Data or Girls in Tech group near Vilnius or Kaunas. The GDG chapter pages tried for Vilnius and Kaunas do not exist, so no Women Techmakers events were found. pyladies.com lists no Lithuanian chapter. The Women in AI Lithuania page returns 404. [Rails Girls Vilnius](https://railsgirls.com/vilnius.html) last ran in 2014. Women Who Code closed in 2024.
- **Searching for first-time speakers:** about 110 searches found only 6 new people. Search engines rarely connect Medium, dev.to and Substack authors, or LinkedIn posts, to Lithuania. None of the big dbt employers except Omnisend publishes dbt engineering-blog posts. No Lithuanian-language dbt content turned up.

## 3. Companies looked at

- **Heaviest dbt use:** Kilo Health, Nord Security, Surfshark, Oxylabs, Hostinger, CoinGate, Eneba, IKI, Telia, TransferGo, Omnisend, PVcase, Ovoko, Artea bankas and Lietuvos bankas.
- **Venue and partner contacts:** TeraSky (the dbt partner), Oxylabs (hosted #1) and Vinted (hosted #2).
- **A different stack or place:** Scrambly uses Dataform, not dbt. Bolt's analytics engineers are mostly in Tallinn.
- **Open leadership roles:** many "no leader found" gaps are real vacancies. Head of Data roles are open at Hostinger, Eneba, Nord (Saily), Barbora and Oxylabs.

<!-- companies:start -->
61 companies and communities were looked at. A company is local when it has people or roles in the region.

<details><summary><b>Strong dbt use</b> (22)</summary>

Artea bankas (ex-Šiaulių bankas), CoinGate, Eldorado.gg, Eneba, Hostinger, IKI Lietuva, Intetics, Kilo Health (Kilo / Kiloverse), Lietuvos bankas (Bank of Lithuania), Nord Security (NordVPN, Saily, NordLayer), Omnisend, Ovoko / RRR.LT, Oxylabs, PVcase, Scoris, Surfshark (incl. Incogni), Telia Lietuva, TeraSky Europe, TransferGo, Vinted, Wargaming (Vilnius), Welltech

</details>

<details><summary><b>Some dbt signal</b> (14)</summary>

Bonapolia, DATAHEAD, EPAM Systems (Lithuania), foxity.io, Luminor, Mediatech (Cybernews), MWDN, Nasdaq (Vilnius), OAG (ex-Infare), PAYSTRAX, Ruby Labs, Tesonet, Topo grupė, twoday Lithuania

</details>

<details><summary><b>dbt as a nice-to-have</b> (4)</summary>

BARBORA Lietuva, Cast AI, ECOSERVICE grupė, Macaw Lithuania

</details>

<details><summary><b>Not verified</b> (19)</summary>

Adform (local presence not confirmed), Beyond Analysis, BITĖ Lietuva, Bolt (local presence not confirmed), BURGA (local presence not confirmed), Danske Bank (Vilnius), Flo Health, Genius Sports (Vilnius), HomeToGo (Kaunas), Ignitis Group, Infotrust, Other / independent, Paysera (local presence not confirmed), Revolut (Vilnius), Scrambly, SEB (Vilnius), Shopify (remote) (local presence not confirmed), UAB Ltintus (local presence not confirmed), Wix (Vilnius)

</details>

<details><summary><b>Uses a different stack</b> (2)</summary>

PyLadies Lithuania, Women Go Tech

</details>

<details><summary><b>Other sources checked</b> (11)</summary>

- [Meetup gql2 groupSearch near Vilnius and Kaunas](https://www.meetup.com/gql2)
- [PyLadies Lithuania (Meetup gql2)](https://www.meetup.com/pyladies-lithuania/)
- [Women Go Tech site and events API](https://www.womengotech.com/wp-json/tribe/events/v1/events)
- [Tech Kinship (Meetup gql2)](https://www.meetup.com/tech-kinship/) (nothing useful)
- [GDG chapters in Lithuania (Women Techmakers)](https://gdg.community.dev/) (nothing useful)
- [PyLadies chapter sites](https://pyladies.com/locations/) (nothing useful)
- [Women in AI Lithuania](https://www.womeninai.co/lithuania) (nothing useful)
- [Rails Girls Vilnius](https://railsgirls.com/vilnius.html) (nothing useful)
- [Women Who Code](https://womenwhocode.com/) (nothing useful)
- [CVMarket.lt dbt search](https://www.cvmarket.lt/joboffers.php?op=search&search%5Bkeyword%5D=dbt)
- [HN Who is hiring (Algolia)](https://hn.algolia.com/api/v1/search?query=dbt&tags=comment) (nothing useful)

</details>
<!-- companies:end -->

## 4. Key leads

- **First-time speakers:**
  - **Simas Janušas (Omnisend):** tier 1. The post covers AI-assisted dbt development.
  - **Martynas Mickevičius:** maintains the `vilnius-pub` project (dbt + DuckDB + Evidence.dev).
  - **Paulius Alaburda (Ignitis Head of Data Analytics):** posts about the team's dbt stack.
  - **Albinas Plesnys:** Medium dbt tutorials and dbt CI/CD articles.
- **Anchor speakers:**
  - **Tomas Peluritis:** runs Uncle Data.
  - **Augustinas Karvelis:** spoke at Coalesce.
  - **Others:** Mantas Satkevičius, Antanas Baltrušaitis, Ernestas Babachinas, and past meetup speakers Gediminas Krištopaitis, Laima Plėšnytė, Valerija Životkevič and Marius Žukauskas.
- **Connectors:**
  - **Rytis Ulys (Oxylabs):** could put forward one of the dbt-certified analytics engineers on the Oxylabs team.
  - **Meetup channels:** a call for first-time speakers through the Meetup group and dbt Slack `#local-baltics` will probably find more people than search.

## 5. Before outreach

- [ ] **Confirm where Simas Janušas is based.** Simas Janušas is tier 1 with no known location.
- [ ] **Check who has already presented.** Rytis Ulys was first counted as a first-time speaker but has Build Stuff and OxyCon talks.
- [ ] **Check stale titles.** Search snippets can be years old. Laima Plėšnytė moved from Oxylabs to Eldorado.gg, and Valentinas Mitalauskas from Hostinger to Shopify.
- [ ] **Check wrong titles.** People-data sites like RocketReach sometimes get titles wrong. Martynas Manikas turned out to be a recruiter, not an analytics engineer.
- [ ] **Keep duplicate profiles together.** Tomas Peluritis, Laima Plėšnytė, Martynas Jočys and Rytis Ulys each have several LinkedIn URLs. Keep them all in `linkedin_urls`.
- [ ] **Treat employer-branding quotes as "featured".** Examples are the Oxylabs "Behind The Code" quotes and "A chat with…" interviews.
- [ ] **Vinted people are internal.** They are flagged `internal_vinted: true` rather than removed.
- [ ] **Pronouns:** none were found for tier-1/2 people, so all are `null`.

## 6. Next run

- **Sources to try first:**
  - **Job ads:** the LinkedIn Jobs scan, CVbankas and the English and Lithuanian web searches. Set `last_seen` on ads seen again.
  - **Speakers:** new events at meetup.com/vilnius-dbt-meetup, and the latest PyCon Lithuania, Big Data Conference Europe, PyData Vilnius, Coalesce and Tallinn Data Week speaker lists. New Uncle Data episodes and guests.
  - **First-time speakers:** new Lithuania-based authors since the last run, and new content or talks by the existing ones.
  - **Women-in-data groups:** new PyLadies Lithuania events, and the PyCon Lithuania workshop pages that name the 2025 PyLadies instructors. Women Go Tech mentors in data tracks need employers before they can be leads.
  - **People gaps:** for every company with `dbt_signal` "strong" and fewer than 3 people, look for analytics engineers, data engineers, data analysts and BI developers. Re-check people with confidence "Low" or notes like "may have left".
- **People to locate:** 49 people have no known location, mostly people found through the job-ad company search with only a LinkedIn profile as evidence. The tier-1/2 leads among them are Simas Janušas, Aurimas Griciunas, Dovilė Bakšytė and Rytis Jonas Zolubas.
- **Data conventions:** person ids were `pNNN` until v3. Each person's old id is kept in `notes` as "(v3 id: pNNN)".
- **Prompt:** use the [central replication prompt](../research/README.md#9-replication-prompt) with `baltics/lithuania_dbt_companies.json`, the Baltic dbt Meetup (Vilnius), `../enriched/vilnius-dbt-meetup.json` and the region Lithuania. Add: "Search in English and Lithuanian. Flag Vinted people as `internal_vinted` rather than treating them as outreach targets. Commit the old file first; git history keeps old versions, so don't save a `.v<N>.json` copy."

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-23 | 1 | First search: 30 companies, 43 verified dbt job ads, 40 working-level and 17 leadership contacts. |
| 2026-09-23 | 2 | Deeper search for speakers and attendees: 49 companies, 103 people (15 with high speaker potential, 41 with high attendee potential), past meetup agendas, community channels, watchlist. |
| 2026-09-23 | 3 | Topics from `TOPIC_VOCABULARY` added to 46 `speaker_evidence` items and 6 `past_meetups` talks. |
| 2026-09-23 | 4 | Moved to the shared schema v1, the same as Berlin. Person ids changed from `pNNN` to kebab-case names (old ids kept in `notes`). Added `local_presence`, `based_in_region`, `linkedin_confidence`, `priority_tier`, `suggested_talk_angle`, `past_chapter_talks`, the job-ad fields `posted_date`, `last_seen`, `job_family` and `work_mode`, and the evidence fields `content_id`, `co_authors`, `mentions_dbt`, `description`, `url_precision` and `confidence`. `field_definitions` and `counts` are now the same in both files. 55 companies, 104 people. |
| 2026-09-23 | 5 | Shared schema v2 adds `lead_type`. Emerging voices, meaning people who publish but have no talk yet, are prioritised for first-time speaker invitations; the rule is in `../berlin_planning/SEARCH_METHOD.md` §1 Step 6. Split: 23 proven speakers, 1 emerging voice (Albinas Plesnys, dbt CI/CD articles), 1 featured, 79 with no public content. Most Lithuanian leads came from job-ad searches, so the next run should look for people who post (Medium, LinkedIn posts, Uncle Data guests). |
| 2026-09-23 | 6 | Search for emerging voices (Step 3b). Added 6 people: Simas Janušas (tier 1), Martynas Mickevičius, Paulius Alaburda, Žymantė Guogaitė (tier 2), Jurgita Zukauskaite and Kaloyan Todorov Hristov. Added new content for Rytis Ulys (now `proven_speaker`), Tomas Peluritis, Aurimas Griciūnas and Dovilė Bakšytė. Now 110 people: 24 proven speakers, 5 emerging voices, 2 featured. The organiser dashboard now ranks emerging voices first within each tier and has a lead-type filter. `metadata.counts` puts `lead_type` last, to match Berlin and KL. Backup: `lithuania_dbt_companies.v5.json`. |
| 2026-09-23 | 7 | Shared schema v3 adds `pronouns` and `sourced_via` (schema-only change). `pronouns` records only pronouns people publish themselves; none were found for tier-1/2 people, so all are `null`. `sourced_via` is derived from each person's evidence; people found through the job-ad company search are `job_ad_company_search`. For women-in-data sourcing and the line-up balance check, see `../berlin_planning/SEARCH_METHOD.md` Step 2b and §1 Step 6. Next run: check Vilnius women-in-data groups (e.g. PyLadies Vilnius, Women Go Tech). Backup: `lithuania_dbt_companies.v6.json`. |
| 2026-10-01 | 8 | Location pass and LinkedIn pass, by the evidence rules in `../research/README.md`. Public pages placed no one, because most unknown people have no evidence link other than a LinkedIn profile. LinkedIn search results placed 9 people: 7 in Lithuania and 2 elsewhere (Paris and Chicago). 49 people are still unknown. |
| 2026-10-01 | 9 | Women-in-data pass from PyLadies Lithuania and Women Go Tech. 10 people added: 2 Oxylabs workshop speakers, and 8 organisers and staff as connectors. |
| 2026-10-01 | 10 | Company pass from CVMarket, CVbankas, company job boards, Meetup hosts and GitHub. 4 companies added: Wargaming (strong), and Infotrust, SEB and Danske Bank as Vilnius meetup hosts with no dbt seen. EPAM rose from weak to medium. 19 job ads added, now 62. |
