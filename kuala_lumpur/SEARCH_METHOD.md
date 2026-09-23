# Kuala Lumpur dbt search: method, lessons and replication prompt

This file goes with `kuala_lumpur_dbt_companies.json`. It explains how the dataset was built, what worked and what didn't, and gives a prompt for re-running and extending the search.

- **First built:** 2026-09-23
- **Dataset version:** 4 (shared schema version 3)
- **Goal:** find people in Malaysia (Kuala Lumpur / Klang Valley first) who could **speak at**, or help **organise**, a first Kuala Lumpur dbt Meetup. Also find the Malaysian companies that use dbt.
- **Sister datasets:** `../berlin_planning/berlin_dbt_companies.json` and `../baltics/lithuania_dbt_companies.json`. All three follow the shared schema in `../berlin_planning/SEARCH_METHOD.md` §3, and the validator in Appendix A checks all three.

Kuala Lumpur differs from Berlin and Vilnius in one important way: **there is no dbt chapter yet, and almost nobody in Malaysia publishes about dbt.** So the search combines both earlier approaches. It starts from public talks at *other* KL data meetups (Berlin's method), and uses job ads to find the companies that run dbt (Lithuania's method). The best speaker leads are data leads at dbt companies who already speak publicly about something else.

---

## 1. How the search was done

### Step 1: Company blogs and case studies (2 sub-agents)

1. **Batch A – large Malaysian and regional companies:** Grab (PJ), AirAsia/Capital A, the incumbent banks, GXBank, Boost, AEON Bank, TNG Digital, Petronas/Setel, the telcos (CelcomDigi, Maxis, TM, Axiata), Carsome, Deriv, Shopee/Lazada/foodpanda MY, Agoda KL, PropertyGuru, MR DIY, Genting and the conglomerates.
2. **Batch B – startups, vendors and consultancies:** StoreHub, Fave, iPrice, Funding Societies, MoneyLion, ShopBack, Xendit, Employment Hero, SEEK/Jobstreet, Experian, Wise; Snowflake, Databricks, Fivetran/dbt Labs, Synogize, G-AsiaPacific and the global dbt partners.
3. For each: tech blog or Medium feed (`medium.com/feed/<publication>`, or `/tagged/dbt`), vendor case studies, conference talks.
4. **Result:** very little dbt writing. The only substantial dbt posts are ShopBack's 2021 series and Wei Jian's 2022 posts. Most Malaysian companies have no public data blog.

### Step 2: Job ads (1 sub-agent)

1. **LinkedIn Jobs, logged out, in the built-in browser:** `linkedin.com/jobs/search?keywords=dbt&location=Malaysia`, scanned with the in-page script from `../baltics/SEARCH_METHOD.md` Appendix A (with `location=Malaysia`).
   - 627 unique listings (pages stop after `start=630`). Only data-titled ads were opened (488).
   - **27 ads at 24 employers contained the whole word "dbt".** Most hits came in the first ~250 results.
   - Two parallel workers at 1.5 s spacing hit 94 HTTP 429s, all recovered by the back-off.
2. **Indeed Malaysia:** `malaysia.indeed.com/q-dbt-jobs.html` (and `?start=10`) is readable with a plain fetch. It found Wilhelmsen, Coforge, Rapsodo, Rotate and a recruiter ad that LinkedIn missed.
3. **freehire.me:** `freehire.me/jobs?countries=my&skills=dbt` lists ~65 Malaysian jobs tagged dbt, often with full ad text. It mirrors Workday/Ashby/Zoho ads that don't render when fetched.
4. `dbt_signal` follows the shared rules: **strong** = dbt required/core; **medium** = among alternatives, board-tagged, or snippet only; **nice-to-have** = a plus.

### Step 3: People and communities (1 sub-agent, then a gap-fill agent)

- **Data Council KL (DCKL)** on Luma was the best source: event pages (`lu.ma/dckl8`, `luma.com/t5fcsqb6`, `lu.ma/ykeg7loq`, `lu.ma/aufuyvtq`, `luma.com/m3nydr6r`) give each speaker's name, role, company and host venue. Open `luma.com/dckl` in the browser, then fetch event pages from inside the tab.
- **Snowflake User Group KL** (`usergroups.snowflake.com/kuala-lumpur/`) and **Snowflake World Tour / Data for Breakfast KL**. Agenda pages don't name customer speakers; the names came from LinkedIn post snippets.
- **Other communities checked:** PyData KL, PyCon MY, AWS User Groups MY, GDG KL / DevFest KL, Microsoft Fabric Community MY, KL Data Science.
- **Singapore dbt Meetup speakers** (`../enriched/singapore-dbt-meetup.json`) were checked; none is KL-based.
- **Gap-fill:** named data leads at the strong-dbt employers (Ryt Bank, GXBank, foodpanda, Funding Societies, Deriv, Intrepid Asia, Star Media, TIME dotCom, Synogize…).

### Step 4: LinkedIn profiles

- Same rule as Berlin: `"<name>" <company> site:linkedin.com/in`, and only URLs that appear word for word in results.
- **`my.linkedin.com/in/...`** (Malaysian subdomain) is a useful stand-in for "based in Malaysia" when no city is shown.
- v1 hit the session's **200-web-search cap** during this step. v2 (a fresh session) searched the remaining 16 plus 3 medium matches: 14 URLs found. Only the organiser is still `not_searched`.
- In v2, third-party profile sites (Apollo, Datanyze) and GitHub gave location and job history where LinkedIn had no match (Wei Jian: Penang, still at ShopBack; Syakeer Rahman: Putrajaya).

### Step 5: Topics, scoring and shaping

- Topics: 1–3 per `speaker_evidence` item from `TOPIC_VOCABULARY` in `../pipeline/enrich.py`, as in Berlin.
- `priority_tier`, `meetup_fit`, `level`, `dbt_signal`, `watchlist` and `excluded_from_outreach`: the shared rules in `../berlin_planning/SEARCH_METHOD.md` §1 Step 6. Two KL-specific choices:
  - **Tier 1** = in Malaysia, spoke publicly in 2025–26, and leads a team whose ads require dbt, or has given a dbt talk.
  - **connector** is used a lot here: community organisers (DCKL, PyData KL, AWS UG, Fabric), vendor staff (Snowflake, AWS) and senior sponsors. They are the route to venues and co-hosts.
- **`lead_type`** (shared schema v2): proven_speaker / emerging_voice / featured / no_public_content, set by rule. Emerging voices in Malaysia (or not known to be elsewhere) with content from 2024 onwards are raised to tier 1, as first-time speaker invitations. In v2 that raised Syakeer Rahman, Zi Qin Yeow and Feng Cheng to tier 1, and Katie Huang and Azwan Zuharimi to tier 2.
- **Women in data to highlight** are marked in `notes` with the prefix `HIGHLIGHT – woman in data`, not with a schema field (Jeremy's choice, v3). Only tag someone when a public source describes her that way; never infer it from a name. Current: Bee Teng Lim, Goh Pei Xuan, Katie Huang Xiemin (speakers) and Caroline Chong (sponsor). Leads for more: PyLadies KL (kl.pyladies.com), MMU TechGirls, and asking data leads at dbt companies to suggest women on their teams.
- `past_meetups` and `past_chapter_talks` are empty because there is no KL chapter. Once the first meetup runs and the pipeline scrapes it, fill them from `../enriched/<kl-group>.json`.
- `watchlist` is true for 51 of 89 companies, mostly large Malaysian firms checked without finding dbt. They are kept so they are not re-researched.

### Step 6: Build

The sub-agents returned JSON records, and one builder script merged them, applied the shared schema and scored people. The file is also picked up by `../dashboard/build_organiser_data.py` (chapter key `kuala_lumpur`, goal `speakers`).

---

## 2. What we learnt

### Sources that worked well

| Source | Why it's useful |
|---|---|
| Data Council KL event pages on Luma | Full speaker bios, committee names and host companies. The main KL data community. |
| LinkedIn Jobs (logged out, in-page script) | 27 verified dbt ads. The first ~250 results hold almost all hits. |
| `freehire.me/jobs?countries=my&skills=dbt` | ~65 Malaysian dbt-tagged jobs in four fetches, with full text where ATS pages don't render. |
| Indeed Malaysia (`q-dbt-jobs.html`) | Plain-fetchable; catches ads LinkedIn misses. |
| Snowflake User Group KL pages | Named speakers with titles; led to MoneyLion and CelcomDigi. |
| LinkedIn post snippets about Snowflake events | The only way to name customer speakers at World Tour / Data for Breakfast KL. |
| Personal blogs and GitHub | Found the only KL dbt talk (Lee Boon Keong, DCKL 2020) and an OSS dbt platform (Syakeer Rahman). |

### Sources that didn't work

| Source | Problem |
|---|---|
| PyCon MY (`cfp.pycon.my/pyconmy-2025/`, `pycon.my`) | pretalx pages load by JavaScript; the browser was refused and plain fetches were empty. Note the slug is `pyconmy-2025`, not `pycon-my-2025`. |
| JobStreet (`my.jobstreet.com/dbt-jobs`) | JavaScript-only. |
| getdbt.com case studies and partner directory | JavaScript-only; no Malaysian partner list. |
| Generic searches ("dbt Kuala Lumpur speaker", "analytics engineer Malaysia dbt") | The search tool mostly ignores the location words and returns global results. |
| Private meetup.com groups (DCKL, KL Data Science) | Speakers hidden; use Luma instead. |
| Company blogs | Grab has no dbt content; Deriv's blog now redirects to an AI Substack; most Malaysian startups have no blog. |
| dbt Community Forum, Coalesce speakers, "dbt certified" searches | No Malaysians found. |

### Things to watch out for

- **Search snippets swap employers.** A snippet credited GXBank's "dbt within Snowflake" ad to AirAsia. Always open the ad.
- **Snippet summaries go stale; result titles don't.** Lee Boon Keong's summary still said MoneyLion; the title said Lance Data.
- **Stale roles and moves:** Yudhiesh Ravindranath MoneyLion → One Credit; Au Yong Min Hao MoneyLion → Ryt Bank; Piyush Palkar's Carsome CDO role is from 2023.
- **The ex-MoneyLion network** runs through KL data: Au Yong Min Hao, Lee Boon Keong, Shawn Loh and Yudhiesh all came from MoneyLion.
- **"Malaysian" companies with teams elsewhere:** Grab, Shopee, Lazada and Xendit data teams are mostly in Singapore, Indonesia or China.
- **"dbt or SQLMesh" / "dbt or Dataform":** MoneyLion and Deriv list alternatives. Ask which one runs in production.
- **Same-name people:** Goh Pei Xuan (another at Apave SG), Wei Jian (very common), Laxman Damodar (two profiles).
- **The search cap is shared** by all sub-agents: 200 per session. This run used it up in the second wave. Budget roughly 50 per agent, and do the LinkedIn pass for tier 1–2 people first.

### Key findings (2026-09)

- **No KL dbt meetup or Coalesce watch party has ever run.** The only dbt talk found in KL was at Data Council KL in May 2020.
- **Both general KL data communities have gone quiet:** DCKL (last event Jun 2025) and the Snowflake User Group KL (last event Apr 2025). There is room for a new meetup, and both are natural co-hosts.
- **Strongest speaker leads:**
  - Lee Boon Keong (Lance Data): gave the 2020 dbt talk, still builds dbt projects, and sits on the DCKL committee. First person to approach, as speaker and co-organiser.
  - Au Yong Min Hao (Head of Data, Ryt Bank): Ryt Bank's ads require dbt + Snowflake; he writes about hiring analytics engineers.
  - Bee Teng Lim (GXBank): presented GXBank's BI Bytes story at Snowflake World Tour KL 2026; GXBank's ads require dbt on Snowflake.
  - MoneyLion's data engineers (Wilbert Chong, Dafuallah Esameldien, Goh Pei Xuan): experienced speakers; ask whether they use dbt or SQLMesh.
- **Best venues/hosts:** MoneyLion (TRX), Xendit (KL Sentral), SEEK (Cap Square), Setel (Bangsar South), AWS (Mid Valley). All have hosted DCKL or the Snowflake UG.
- **Companies with the clearest dbt use:** Ryt Bank, GXBank, foodpanda KL, Funding Societies, Intrepid Asia, Star Media, TIME dotCom, Wilhelmsen, ROCKWOOL, Nitka (Johor), onsemi.
- **Most common topics:** data warehouse & platforms, genai & llm, data governance. Topics tagged with dbt itself are rare, which confirms the gap.

---

## 3. Dataset schema

Shared schema version 3 (v2 added `lead_type`; v3 added `pronouns` and `sourced_via`). See `../berlin_planning/SEARCH_METHOD.md` §3 for the full key list. Keys, `field_definitions` and `counts` keys are identical across all three regional files. Person and company `id`s are kebab-case ASCII names; keep them stable.

---

## 4. How to update the dataset

1. **Commit, then merge.** Commit the current file first. Git history keeps old versions, so don't save a `.v<N>.json` copy. Match people by `id` or by first and last name with accents removed; companies by `id`; content by `content_id` or `url`; job ads by `url`.
2. **Existing people:** append new `speaker_evidence`; update title or company only on newer, high-confidence evidence; record moves in `notes`.
3. **Existing companies:** add new `job_postings`, set `last_seen` on ads still listed, keep expired ones.
4. **New content** gets `content_id` `<company-or-event>-<slug>` (e.g. `dckl-13-<slug>`) and 1–3 topics.
5. **After the first KL meetup:** add the group to `../pipeline/dbt-meetup-groups.json`, run `../pipeline/run_pipeline.sh`, then fill `past_meetups` and `past_chapter_talks` from `../enriched/<kl-group>.json` (Berlin Appendix B).
6. **Re-score** `meetup_fit`, `level` and `watchlist` with the shared rules.
7. **Validate** with Appendix A.
8. **Update the metadata:** bump `version`, set `generated_at`, recalculate `counts` (`standard_counts()` in Berlin Appendix A) and `topic_counts`, add a line to `method`.
9. **Log the run** in the change log below.

### Open items

- No LinkedIn profile found for Wei Jian, Syakeer Rahman, Ng Ser Jie or Michael Rorig; try other name spellings, or ask Lee Boon Keong / DCKL for introductions.
- Confirm where Feng Cheng (Grab) is based: the `lead_type` rule raised him to tier 1 only because his location is unknown; Grab's data authors are mostly in Singapore.
- PyCon MY 2024/2025 schedules: open in a browser.
- dbt Slack `#local-malaysia` / `#local-kuala-lumpur`: check by hand.
- Named data leads at foodpanda KL, Funding Societies MY, Deriv, Intrepid Asia (Head of Data role open) and Star Media.

---

## 5. Replication prompt

Copy this into a new Cowork session, with the `dbt-meetups` folder connected:

````
You are updating my dataset of Malaysian companies that use dbt, and people who could speak at or
help organise a Kuala Lumpur dbt Meetup. The dataset is kuala_lumpur_dbt_companies.json in
/Users/jeremychia/Documents/Github/dbt-meetups/kuala_lumpur. Read SEARCH_METHOD.md in the same
folder first and follow its method, lessons and merge rules. The schema must stay identical to
../berlin_planning/berlin_dbt_companies.json and ../baltics/lithuania_dbt_companies.json
(shared schema in ../berlin_planning/SEARCH_METHOD.md §3). I (Jeremy Chia) work at Vinted; flag
Vinted people as internal_vinted.

The session has about 200 web searches in total, shared by all sub-agents. Budget ~50 per agent.

Tasks, in priority order:

1. OPEN ITEMS from SEARCH_METHOD.md §4 (LinkedIn for tier 1-2 people with linkedin_confidence
   "low", PyCon MY schedules in the browser).

2. JOB ADS (built-in browser for LinkedIn)
   - Scan https://www.linkedin.com/jobs/search?keywords=dbt&location=Malaysia with the in-page
     script in ../baltics/SEARCH_METHOD.md Appendix A (location=Malaysia), opening only
     data-titled ads. Keep ads whose text has the whole word "dbt" (exclude therapy "DBT").
   - Fetch https://freehire.me/jobs?countries=my&skills=dbt and
     https://malaysia.indeed.com/q-dbt-jobs.html.
   - Add new companies and ads; set last_seen on ads seen again.

3. SPEAKERS since the last run (see metadata.generated_at)
   - Data Council KL (https://luma.com/dckl), Snowflake User Group KL, Snowflake World Tour /
     Data for Breakfast KL, PyData KL, PyCon MY, AWS Community Day MY, GDG KL, and any new KL
     dbt meetup events. Read each event page for the line-up.
   - For strong-dbt employers with no named people, look for data leads who speak publicly.

4. CLASSIFY AND SCORE
   - Tag each new speaker_evidence item with 1-3 topics from TOPIC_VOCABULARY in
     ../pipeline/enrich.py only. If nothing fits, propose a new topic to me.
   - Re-score meetup_fit, level and watchlist with the shared rules.

You may run up to 3-4 sub-agents in parallel (e.g. job ads, communities, LinkedIn). Ask each to
return JSON records with the shared-schema fields.

Rules:
- Only record linkedin.com/in URLs that appear word for word in search results. Never guess.
- Collect only professional information: name, title, company, public talks and posts.
- Every item needs a URL and a confidence rating; url_precision overview_page for listings.
- Commit the old file first (no .v<N>.json copy), merge following §4, run the
  Appendix A validator, recalculate counts and bump the version.
- Add a change-log entry to SEARCH_METHOD.md: date, what was added, and any new lessons.

When finished, tell me briefly what's new: new speakers (with a link to their work), new companies
and dbt roles, people who have moved, and anything that changes who to approach first.
````

---

## Appendix A: Validator (all three regional files)

Run from the repo root. It reuses the key lists from `../berlin_planning/SEARCH_METHOD.md` Appendix A.

```python
import json, sys, re
sys.path.insert(0, "pipeline")
from enrich import TOPIC_VOCABULARY as V

# copy TOP, META, COMPANY, JOB, PERSON, EVID, PAST, PAST_TALK, keys() and check()
# from berlin_planning/SEARCH_METHOD.md Appendix A, then:

files = ["kuala_lumpur/kuala_lumpur_dbt_companies.json",
         "berlin_planning/berlin_dbt_companies.json",
         "baltics/lithuania_dbt_companies.json"]
ds = [check(f) for f in files]
for d in ds[1:]:
    assert d["metadata"]["field_definitions"] == ds[0]["metadata"]["field_definitions"]
    assert list(d["metadata"]["counts"]) == list(ds[0]["metadata"]["counts"])
    assert d["metadata"]["schema_version"] == ds[0]["metadata"]["schema_version"]
# company ids must be unique too
ids = [c["id"] for c in ds[0]["companies"]]
assert len(ids) == len(set(ids))
print("ok")
```

---

## Change log

| Date | Version | Change |
|---|---|---|
| 2026-09-23 | 1 | First search. 89 companies (51 on the watchlist), 44 people, 50 job postings at 36 companies, 43 unique content items. 3 tier-1 leads (Lee Boon Keong, Au Yong Min Hao, Bee Teng Lim), 14 tier-2, 12 connectors. LinkedIn URLs for 26 people; 16 not searched after the session hit the 200-web-search cap. Chapter `kuala_lumpur` added to `dashboard/build_organiser_data.py`. |
| 2026-09-23 | 2 | Moved to shared schema v2 (`lead_type`): 26 proven speakers, 8 emerging voices, 1 featured, 9 with no public content; tier 1 now 6. LinkedIn pass in a new session: 18 people searched, 14 URLs found (38 of 44 people now have one). Location fixes: Yun Fei Choo and Harvey Li are Singapore-based; Zi Qin Yeow is Malaysia-based; Wei Jian is in Penang; Syakeer Rahman is in Putrajaya. Backup of v1 at `kuala_lumpur_dbt_companies.v1.json`. |
| 2026-09-23 | 3 | Marked 4 women in data to highlight in `notes` (prefix `HIGHLIGHT`): Bee Teng Lim, Goh Pei Xuan, Katie Huang Xiemin, Caroline Chong. No schema change. Organiser page rebuilt with the Kuala Lumpur chapter. |
| 2026-09-23 | 4 | Shared schema v3 adds `pronouns` (self-stated only, never inferred; none recorded yet) and `sourced_via`, which is derived from evidence (e.g. `women_in_data_community` for the PyLadies x PyData KL speaker). The field list is in `../berlin_planning/SEARCH_METHOD.md` §3. For women-in-data sourcing and the line-up balance check, see that file's Step 2b and §1 Step 6. Backup: `kuala_lumpur_dbt_companies.v3.json`. |
