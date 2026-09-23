# Lithuania dbt search: method, lessons and replication prompt

This file goes with `lithuania_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and gives a prompt for re-running and extending the search.

- **First built:** 2026-09-23
- **Dataset version:** 7 (shared schema version 3)
- **Goal:** find companies in Lithuania that use dbt, and people there who could **speak at** or **attend** the Baltic dbt Meetup (Vilnius).
- **Sister dataset:** `../berlin_planning/berlin_dbt_companies.json`. Both files follow one shared schema, described in §3. The full definition and the validator are in `../berlin_planning/SEARCH_METHOD.md` §3 and Appendix A.

---

## 1. How the search was done

### Step 1: Companies that use dbt (from job ads)

Job ads are the most reliable sign that a company uses dbt, because companies list their real tools.

1. **LinkedIn Jobs: the main source.**
   - Search `https://www.linkedin.com/jobs/search?keywords=dbt&location=Lithuania`. This works without logging in.
   - LinkedIn's keyword search is loose. It returned **415** ads, but only **43** mentioned dbt in the ad text.
   - So each ad's full description has to be fetched and checked for the whole word `dbt`. The snippet in Appendix A does this.
   - Each ad page also shows who posted it ("Meet the hiring team"), which can give a named contact.
2. **CVbankas.lt:** `https://www.cvbankas.lt/?keyw=dbt` searches the ad text. It found Artea bankas, Lietuvos bankas, IKI and Ltintus.
3. **Web search, in English and Lithuanian:**
   - English: `dbt data engineer Vilnius`, `analytics engineer Vilnius dbt`, `data scientist Kaunas dbt`
   - Lithuanian: `dbt duomenų analitikas`, `"dbt" duomenų inžinierius`, `duomenų mokslininkas dbt`
   - Job platforms: `"dbt" Vilnius site:teamtailor.com OR site:greenhouse.io OR site:jobs.lever.co OR site:ashbyhq.com`
4. **Rating each company's dbt signal:**
   - **strong:** dbt is required or part of the core stack.
   - **medium:** dbt is listed as one of several options, or the company only matched a keyword search.
   - **nice-to-have:** dbt is listed as a plus.
   - **weak:** not verified.

### Step 2: People at those companies

- Searches such as `site:lt.linkedin.com/in "Analytics Engineer" "<Company>"` and `site:linkedin.com/in "<Company>" dbt Vilnius`.
- theorg.com team pages, and company careers blogs (for example career.oxylabs.io).
- A person was kept only if a search result tied them to the company in a data role. LinkedIn URLs were **never guessed**; only URLs that appeared word for word in results were recorded.
- Confidence:
  - **High:** name, title and company all appear in the result.
  - **Medium:** the link to the company is indirect.
  - **Low:** weak identification.

### Step 3: Speakers and likely attendees

- **Past Baltic dbt Meetup agendas:** event pages at `meetup.com/vilnius-dbt-meetup` (events 303809378 and 306239130).
- **Conference speaker lists:**
  - PyCon Lithuania 2024–2026 on pretalx.com (the most useful source)
  - Big Data Conference Europe (bigdataconference.eu)
  - PyData Vilnius
  - Coalesce on-demand talks (getdbt.com)
- **Community content:** the Uncle Data newsletter and podcast (Tomas Peluritis), Medium, LinkedIn posts, and the podcast guests.
- **LinkedIn profiles that mention dbt or dbt certification** (`site:lt.linkedin.com/in dbt ...`).
- Each person is then rated with `meetup_fit`:
  - `speaker_potential: high` means they have given talks on dbt or analytics engineering, or at least two public talks.
  - `attendee_potential: high` means their profile mentions dbt, they have published dbt content, or they are a confirmed practitioner at a company with a strong dbt signal.

### Step 3b: Emerging voices, meaning people who publish but haven't presented (added in v6)

The meetup wants to give first-time speakers a chance, so this step looks for people who **write** about dbt but have no talk on record. Two sub-agents ran in parallel:

1. **Writers and open source.** Covered Medium, Substack, dev.to and Hashnode, company engineering blogs (Kilo Health, Nord Security, Oxylabs, Surfshark, Hostinger, Omnisend, TransferGo, Eneba, PVcase), Lithuanian-language content, GitHub dbt projects by Lithuania-based developers, and the dbt Community forum.
2. **LinkedIn posts.** Used `site:linkedin.com/posts` with dbt plus Vilnius, Kaunas or a company name; Lithuanian phrases (`"dbt" duomenų`); "dbt Certified"; and posts about attending a past Baltic dbt Meetup or Coalesce.

Every person is checked quickly for talks. Content is recorded as `speaker_evidence` with `type` set to `article`, `post` or `oss`. `lead_type` and `priority_tier` then follow the shared rule in `../berlin_planning/SEARCH_METHOD.md` §1 Step 6:

- An **emerging_voice** in the region (or not known to be outside it) with content dated 2024 or later becomes **tier 1**.
- An emerging voice whose content is older or undated becomes **tier 2**.

**How the organiser dashboard ranks them.** Within each tier, emerging voices come first, then proven speakers, then featured people, then people with no public content. The Speakers view has a "First-time speakers" filter.

### Step 4: Parallel sub-agents

The people search was split across 3 sub-agents running in parallel, each covering 6–8 companies or one source type. Each returned a JSON array, which was merged and de-duplicated by name with accents removed (see §4).

---

## 2. What we learnt

### Sources that worked well

| Source | Why it's useful |
|---|---|
| LinkedIn Jobs (logged out), with each ad's text checked | The best company signal. It also sometimes names the person who posted the job. |
| pretalx.com (PyCon LT schedules and speaker pages) | Full speaker bios, often including the tools they use. |
| Past meetup agendas on meetup.com | Past speakers are proven and easy to invite back. |
| Uncle Data (Substack and podcast) | The centre of Lithuania's data community; the guests are good leads. |
| theorg.com | Org charts for data teams (Surfshark, twoday, Eldorado.gg). |
| CVbankas `?keyw=` | Searches ad text and catches Lithuanian-language ads. |

### Sources that didn't work

| Source | Problem |
|---|---|
| CV-Online and CVMarket keyword search | Only matches job titles, so a dbt search returns nothing. |
| meetup.com attendee lists | Need a login. |
| LinkedIn people search | Needs a login. Search engines index only a small share of profiles. |
| `site:linkedin.com/posts dbt ...` | Noisy: returns worldwide results and therapy "DBT" (dialectical behaviour therapy). |
| Big Data Conference Europe speaker pages | Loaded by script, so plain fetches get nothing. Use the browser. |
| The fetch tool on job boards | Timed out. The built-in browser plus in-page `fetch()` worked instead. |

### Things to watch out for

- **LinkedIn rate limits.** Fetching ads in parallel hits HTTP 429 almost at once. Fetch one at a time, about 2–2.5 seconds apart, and back off for 15 seconds or more after a 429. Scanning around 415 ads takes about 20 minutes.
- **Web search cap.** There is a limit of about **200 web searches per session**, shared by all sub-agents. Spend it on the highest-value searches first: speakers, then gaps in the people list.
- **Duplicate profiles.** One person can have several LinkedIn URLs (for example Tomas Peluritis, Laima Plėšnytė, Martynas Jočys, Rytis Ulys). Keep them all in `linkedin_urls`.
- **Stale titles.** Search snippets can be years old. Several people have since changed jobs (Laima: Oxylabs → Eldorado.gg; Valentinas Mitalauskas: Hostinger → Shopify).
- **Wrong titles.** People-data sites like RocketReach sometimes get titles wrong. Martynas Manikas turned out to be a recruiter, not an analytics engineer.
- **Open leadership roles.** Many "no leader found" gaps are real vacancies: Head of Data roles are open at Hostinger, Eneba, Nord (Saily), Barbora and Oxylabs.
- **Scrambly** uses Dataform, not dbt. **Bolt**'s analytics engineers are mostly in Tallinn.
- **Vinted people** are flagged `internal_vinted: true` rather than removed.
- **Emerging voices are hard to find by search in Lithuania (v6).** About 110 searches found only 6 new people:
  - Search engines rarely connect Medium, dev.to and Substack authors, or LinkedIn posts, to Lithuania.
  - None of the big dbt employers publishes dbt engineering-blog posts. Omnisend's Feb 2026 post was the exception.
  - No Lithuanian-language dbt content turned up.
  - What worked: company blog posts that name the author (Omnisend), GitHub repos whose profiles list Vilnius (`vilnius-pub`), and LinkedIn posts in which a data leader lists the team's stack (Ignitis).
  - A call for first-time speakers through the meetup's own channels (the Meetup group and dbt Slack `#local-baltics`) will probably find more people than search.
- **Employer-branding quotes are "featured", not authored.** Examples are the Oxylabs "Behind The Code" quotes and "A chat with…" interviews.
- **Agent reports can be wrong about who has presented.** Check whether someone counted as an emerging voice has already spoken somewhere. Rytis Ulys turned out to have Build Stuff and OxyCon talks.

### Key findings (2026-09)

- **Companies with the heaviest dbt use:** Kilo Health, Nord Security, Surfshark, Oxylabs, Hostinger, CoinGate, Eneba, IKI, Telia, TransferGo, Omnisend, PVcase, Ovoko, Artea bankas and Lietuvos bankas.
- **Proven dbt speakers:** Tomas Peluritis, Augustinas Karvelis (spoke at Coalesce), Mantas Satkevičius, Antanas Baltrušaitis, Ernestas Babachinas, and past meetup speakers (Gediminas Krištopaitis, Laima Plėšnytė, Valerija Životkevič, Marius Žukauskas).
- **Venue and partner contacts:** TeraSky (the dbt partner), Oxylabs (hosted #1) and Vinted (hosted #2).
- **Emerging voices to invite as first-time speakers (v6):**
  - **Tier 1:** Simas Janušas (Omnisend). His post covers AI-assisted dbt development; check where he's based.
  - **Tier 2:** Martynas Mickevičius (maintains the `vilnius-pub` project: dbt + DuckDB + Evidence.dev), Paulius Alaburda (Ignitis Head of Data Analytics; posts about the team's dbt stack) and Albinas Plesnys (Medium dbt tutorials).
  - **Worth asking:** Rytis Ulys (Oxylabs) could put forward one of his dbt-certified analytics engineers.

---

## 3. Shared schema (version 3)

`baltics/lithuania_dbt_companies.json` and `berlin_planning/berlin_dbt_companies.json` have exactly these keys, in this order. A value can be `null` when it's unknown, but a key is never missing.

```
metadata            title, generated_at, prepared_for, purpose, version, schema_version, region,
                    method[], field_definitions{}, caveats[], counts{}, topic_vocabulary_source,
                    topic_vocabulary[], topic_counts{}
companies[]         id, name, type, watchlist, excluded_from_outreach, cities[], local_presence,
                    dbt_signal, stack_signals[], job_postings[], other_evidence[], people[], notes
  job_postings[]    title, url, source, linkedin_company_name, dbt_mentioned_in_text, dbt_snippet,
                    job_poster, posted_date, last_seen, job_family, work_mode
  other_evidence[]  type, url, note
  people[]          id, name, pronouns, title, city, based_in_region, level, linkedin_urls[],
                    has_linkedin, linkedin_confidence, meetup_fit{speaker_potential, attendee_potential},
                    lead_type, sourced_via[], mentions_dbt, speaker_evidence[], attendee_signal, evidence[]{url, note},
                    confidence, internal_vinted, priority_tier, suggested_talk_angle,
                    past_chapter_talks[]{date, talk_title, topics}, notes
    speaker_evidence[]  type, event, title, date, url, content_id, co_authors[], mentions_dbt,
                        description, topics[], suggested_talk_angle, url_precision, confidence
sources             free-form object of source URLs (differs by region)
past_meetups[]      name, date, venue, url, organisers[], attendees, talks[]{speaker, company, title, topics}
community_channels[] name, url, note
```

- **Ids:** person `id`s are kebab-case ASCII names (e.g. `tomas-peluritis`). Until v3 they were `pNNN`; each person's old id is kept in `notes` as "(v3 id: pNNN)".
- **Values filled in when moving to the shared schema (v4):**
  - `priority_tier` is taken from `speaker_potential`: high → 1, medium → 2, low → 3, and Vinted people → `backup`.
  - `local_presence` is `confirmed` when a company has a Lithuanian city in `cities`.
  - `based_in_region` is true when a person's `city` is in Lithuania. It is null for unknown or "assumed" cities.
- **Topics:** every `speaker_evidence` item and every `past_meetups` talk has 1–3 topics from `TOPIC_VOCABULARY` in `../pipeline/enrich.py`.
- **Definitions** are in `metadata.field_definitions`, which is identical in both regional files. `metadata.counts` uses the same keys in both.
- **Checking the schema:** run the validator in `../berlin_planning/SEARCH_METHOD.md` Appendix A. It checks both files.

---

## 4. How to update the dataset

1. **Don't overwrite. Merge.**
   - Load the existing JSON first.
   - Match people by name with accents removed and letters lower-cased (for example "Plėšnytė" becomes "plesnyte").
   - Match companies by `id`.
2. **When a person is already in the file:**
   - Add any new LinkedIn URLs and evidence.
   - Update the title or company only if the new evidence is newer and has High confidence.
   - Record job moves in `notes`, for example "moved from X to Y (source, date)".
3. **New people** get a kebab-case ASCII `id` made from their name (e.g. `laima-plesnyte`). New companies also get a short kebab-case `id`.
   - Tag each new `speaker_evidence` item with 1–3 topics from `TOPIC_VOCABULARY`.
   - Fill in every field in the shared schema (§3), using `null` when unknown.
4. **Job ads expire.** On each run:
   - Add new ads.
   - Keep old ones, but add `"last_seen": "YYYY-MM-DD"`.
   - A company stays in the dataset even when it has no current ads.
5. **Re-score after merging.** Recalculate `meetup_fit`, `priority_tier` and `past_chapter_talks` (matched against `past_meetups`), using the rules in `metadata.field_definitions`. Then run the shared-schema validator (§3).
6. **Update the metadata:**
   - Bump `metadata.version`.
   - Set `generated_at`.
   - Recalculate `counts`.
   - Add a line to `metadata.method` describing what the new run added.
7. **Log the run** in the change log at the bottom of this file.

---

## 5. Replication prompt

Copy this into a new Cowork session, with the `baltics` folder connected:

````
You are updating my dataset of Lithuanian companies that use dbt, and people who could speak at or
attend the Baltic dbt Meetup (Vilnius). The dataset is lithuania_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups/baltics. Read SEARCH_METHOD.md in the same folder
first and follow its method, lessons and merge rules. I work at Vinted, so flag Vinted people as
internal_vinted rather than treating them as outreach targets.

Tasks, in priority order (the session has about 200 web searches in total, so spend them wisely):

1. JOB ADS (use the built-in browser, not web_fetch)
   - Open https://www.linkedin.com/jobs/search?keywords=dbt&location=Lithuania. Using the
     in-page fetch script in SEARCH_METHOD.md Appendix A, collect every ad, fetch each
     description one at a time (about 2.5 s apart, back off on HTTP 429), and keep only ads whose
     text contains the whole word "dbt". Also record the job poster where shown.
   - Check https://www.cvbankas.lt/?keyw=dbt.
   - Run web searches in English and Lithuanian for data analyst / data engineer / data scientist /
     analytics engineer + dbt in Vilnius and Kaunas (e.g. "dbt duomenų analitikas",
     "dbt duomenų inžinierius", "duomenų mokslininkas dbt").
   - Add new companies and ads. Set last_seen on ads you see again.

2. SPEAKERS
   - Check meetup.com/vilnius-dbt-meetup for new events since the last run, and add their agendas to
     past_meetups and their speakers to people.
   - Check the latest PyCon Lithuania (pretalx.com), Big Data Conference Europe, PyData Vilnius,
     Coalesce and Tallinn Data Week speaker lists for Lithuania-based speakers on dbt, analytics
     engineering, data modelling, testing, orchestration or data platforms.
   - Check new Uncle Data newsletter and podcast episodes and guests.

2b. EMERGING VOICES (people who publish about dbt but have no talk yet; a priority for first-time
    speaker invitations, see SEARCH_METHOD.md §1 Step 3b)
   - Look for new Lithuania-based authors of dbt / analytics-engineering content since the last run:
     LinkedIn posts (site:linkedin.com/posts + dbt + Vilnius/Kaunas/company names, Lithuanian
     phrases), company blog posts that name their author (Omnisend, Kilo, Nord, Oxylabs, Surfshark,
     Hostinger, TransferGo, Telia...), Medium/Substack/dev.to, GitHub dbt projects whose owners list
     Lithuania, and posts about attending the Baltic dbt Meetup or Coalesce.
   - For each person, check whether they have given a talk. Record content as speaker_evidence
     (type article / post / oss) with a suggested_talk_angle.
   - Re-check existing emerging voices for new content (and for talks: if they have now presented,
     they become proven_speaker).
   - Apply the lead_type and priority_tier rules (tier 1 = emerging voice in region with content
     from 2024 onwards).

3. PEOPLE: fill the gaps
   - For every company with dbt_signal "strong" and fewer than 3 people, look for working-level
     practitioners (Analytics Engineer, Data Engineer, Data Analyst, BI Developer).
   - Try to find LinkedIn URLs for people where has_linkedin is false.
   - Re-check people with confidence "Low" or notes like "may have left".
   - You may run up to 3 sub-agents in parallel (split by company group or source type). Tell them
     the shared search budget and ask each to return a JSON array.

Rules:
- Only record linkedin.com/in URLs that appear word for word in search results. Never guess.
- Collect only professional information: name, title, company, public talks and posts.
- Give every person a confidence rating and an evidence URL.
- Merge into the existing JSON following SEARCH_METHOD.md §4. Commit the old file first; git
  history keeps old versions, so don't save a .v<N>.json copy.
- Re-score meetup_fit, recalculate counts and bump the version.
- Add a change-log entry to SEARCH_METHOD.md: date, what was added, and any new lessons.

- Run the shared-schema validator (../berlin_planning/SEARCH_METHOD.md Appendix A), then rebuild the
  organiser dashboard with ../dashboard/build_dashboard.sh.

When finished, tell me briefly what's new: new first-time speaker candidates (emerging voices, with a
link to their content), new proven speakers, new companies, new likely attendees, and anything that
has changed (job moves, companies that stopped hiring).
````

---

## Appendix A: LinkedIn job-ad scanner (run inside the browser on a linkedin.com page)

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

The meetup event pages can be read the same way: open any meetup.com page, then
`fetch('/vilnius-dbt-meetup/events/<id>/')` and read `#event-details`.

---

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
