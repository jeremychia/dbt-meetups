# Berlin dbt Meetup: Vision & Forward Strategy

## Where the Meetup Has Been

Berlin dbt Meetup has run 14 events from November 2021 through April 2026, evolving across three distinct phases:

**Phase 1 (2021-22): Foundations & Pandemic Era**
- Online-only due to COVID; talks centered on dbt fundamentals (data modeling, incremental models, modern data stack architecture). Audience was learning the discipline from first principles.

**Phase 2 (2023-24): Maturation & Rigor**
- Shifted to in-person; talks moved upstream from "how to use dbt" to "how to run dbt at scale." Themes: project structure (Contentful, Taxfix, Enpal), CI/CD pipeline patterns (Berghain-quoted talk on "Tougher Than Berghain Bouncers"), data testing strategies, dbt vs. alternative tools. By this phase, the meetup was attracting practitioners from named Berlin companies (Vinted, Contentful, Enpal, GetYourGuide, TIER Mobility, Ecosia).

**Phase 3 (2025-2026): Governance & Platform Thinking**
- Talks increasingly about operating dbt at organizational scale: cost optimization, team management, junior engineer training, platform automation, enterprise regulatory compliance. The "what to build" question gave way to "how to organize humans and governance around it."

**Through all three phases**, the meetup's unique contribution has been hosting in-depth, peer-to-peer practitioner talks — not vendor marketing. Speakers are drawn from the local analytics engineering community itself, grounded in lived problems at real Berlin companies.

---

## The Berlin Landscape (July 2026)

Berlin's data/AI meetup scene is crowded and increasingly agent-focused:

| Meetup | Format | Size | Recent Programming | Niche |
|--------|--------|------|-------------------|-------|
| **Berlin DataTalksClub** | Online-first, weekly | 8,900+ members | "Ingesting Agent Traces," "Engineering Your Own AI Assistant," career development | Broad, high-volume, generic content |
| **Data Berlin** | In-person monthly | 2,600 members | "Agentic Analytics Meetup," data transformation/ops | Broad, in-person but no specialization |
| **dltHub Community (Berlin)** | In-person, occasional | ~100-200 | Data pipeline ingestion, AI agent data capture (Feb 2026 event featured Babbel, AVIV Group, Gemma Analytics) | Data pipelines + AI agents; local companies |
| **AI Agent Meetup Berlin** | Luma, focus on context engineering | Emerging | Agentic AI with focus on context/information architecture | AI agents in applied contexts |
| **AI Tinkerers Berlin** | In-person | Active | AI agents, voice interfaces, RAG, production AI infrastructure | Agents + infrastructure |
| **Berlin AI Developers** | Online + in-person | Active | LLMs, agentic AI, MLOps | General AI engineering |
| **Data Council Berlin** | Was active | 900+ members | Last event: "AI Council" (May 2025); no upcoming events | **Dormant** |

**Key observation:** Nearly *every* active Berlin data meetup has already pivoted its recent programming toward AI agents and agentic workflows. This is not a future trend — it's the current dominant topic across the whole ecosystem, right now. The only group not visibly colonizing this space is **Berlin dbt Meetup**.

---

## The Gap & The White Space

Berlin's analytics engineering community (the ~70% of the local AE/BI job market that uses dbt day to day) is currently underserved in one specific way:

**No one is running a deep, recurring, in-person practitioner venue that treats AI-in-the-data-stack as a *discipline problem* — trust, governance, testing, ownership — rather than as a demos-and-hype topic.**

- DataTalksClub and Data Berlin are online-heavy or broad-topic, good for reach but weak for sticky, same-faces, recurring relationships.
- dltHub and AI-agent meetups are chasing the "how to build with agents" question (legitimate topic, but not dbt's specialty).
- The gap isn't "AI agents aren't being discussed" — they're being discussed everywhere. The gap is: **no one is discussing what happens to analytics engineering discipline and governance when AI agents touch your data pipeline.**

This is dbt Labs' own headline finding from their [2026 State of Analytics Engineering Report](https://www.getdbt.com/resources/state-of-analytics-engineering-2026):
- 72% prioritize AI-assisted coding, but trust/governance concerns also rose sharply (66% → 83% year-over-year).
- 71% worry about hallucinated or incorrect data reaching stakeholders.
- 41% cite ambiguous data ownership as an ongoing challenge.
- **Success in 2026 won't come from building faster with AI; it will come from scaling trust alongside output.**

---

## Why This Meetup Matters

**Berlin's analytics engineering market requires dbt as a baseline skill.**

From `analysis/job_descriptions/jd_data/` (132-record corpus, filtered to Berlin):
- **35 Berlin-based job postings; 25 (71%) explicitly require dbt**
- Among roles specifically typed as analytics-engineering/BI: **20 of 28 (71%) require dbt**
- Companies spanning fintech (Trade Republic, SumUp, N26-adjacent), travel/marketplace (GetYourGuide, Wolt, Vinted, AVIV), scale-ups (Smoobu/HomeToGo, Getsafe, Cosuno, Adsquare), and others all list dbt as a non-negotiable baseline expectation for AE/BI hires.

**This meetup doesn't need to invent relevance. It needs to lean into the fact that dbt is already load-bearing for local careers.**

---

## Vision Statement

**Berlin dbt Meetup is where Berlin's analytics engineers — the ~70% of the local job market living inside dbt every day — go to work out, together, what's actually true and trustworthy about AI in the data stack, as practitioners rather than vendors or hype-chasers.**

The meetup's differentiator is not "we discuss AI before anyone else" (everyone already does). It's **"we treat AI-in-data-work as a discipline problem, grounded in governance, testing, and trust — the hard questions dbt Labs' own 2026 research says matter most."**

---

## Concrete Shifts (Next 2–3 Editions)

### 1. Editorial Throughline: Trust vs. Speed

Every other Berlin data meetup is in demo mode on agents. Program 1-2 talks per edition explicitly through a trust/governance lens:

**Example topics:**
- "AI-Assisted dbt Development in Practice: What Actually Works" (retrospective, not promotional)
- "Evaluating dbt Agents Before You Trust Them to Affect Prod Data"
- "Who Owns a Metric If dbt Agents Helped Define It? Data Ownership Models in 2026"
- "From Speed to Trust: How We Rolled Out AI-Assisted Coding Without Breaking Our Governance"
- "Hallucinated Data in Analytics: Detection, Prevention, and Recovery"

This differentiates by depth and practitioner honesty, not by topic avoidance. You're not saying "we don't do AI" — you're saying "we do AI discipline, which nobody else here is doing."

### 2. Format: Keep What Works, Expand Room for Ecosystem Voices

**Keep:**
- The proven 2–3 talk + networking structure (5 years of data says it works)
- dbt Labs' "What's new with dbt?" opening slot as a guaranteed, fixed fixture (this is a dbt meetup; dbt gets to talk)

**Open question (for organizers to decide):**
- Should you also create an *additional*, occasional slot where adjacent tools (a testing tool like Great Expectations, a BI layer, an orchestrator) can share short updates? This widens relevance to the modern data stack without touching dbt Labs' airtime. Not every edition needs it, but 1–2 per year could build goodwill across the ecosystem.

### 3. Continuity: Build Institutional Memory

Introduce light-touch continuity mechanisms so the meetup doesn't feel like a series of one-off talks:

- **"Revisit" slot (1–2 times per year):** Someone follows up on a topic from 6–12 months ago with what actually happened. Example: "We Adopted dbt Agents in Q1 2026 — Here's What Changed" (given by someone who talked about *plans* for dbt Agents at a previous meetup).

- **Public open-questions backlog:** Maintain a low-friction Slack thread or doc (the `#local-berlin` dbt Slack channel already exists) tracking questions the community cares about:
  - "How do we test AI-assisted models in dbt?"
  - "Who owns a metric when AI helped define it?"
  - "What does 'data ownership' mean at our company?"
  
  Returning members will feel like there's an accumulated thread across events, not just isolated talks.

- **Ecosystem collaboration:** Reach out to dltHub and Gemma Analytics for one joint or cross-promoted edition per year. You're not competitors for the same 100–200 Berlin practitioners — you're different venues for the same community. Joint editions reduce fragmentation and signal maturity.

---

## Anchor for Recruiting Speakers & Sponsors

When pitching to speakers or sponsors, lead with the hiring-demand data:

> "dbt is in 71% of Berlin analytics engineering job postings. This meetup is the community around the tool Berlin's data teams are required to know. We're recruiting practitioners from Wolt, Vinted, Trade Republic, GetYourGuide, SumUp, Getsafe, Cosuno, and dozens of other Berlin companies — people making real decisions about how to integrate AI safely into their data platforms."

This frames the meetup as a hub for a real, deep local market need — not a niche interest group.

---

## Next Actions

1. **Finalize the 2026–27 event calendar** anchored on the "trust vs. speed" throughline. Pick 1–2 topics per edition that explicitly address governance/trust in the context of AI-agents-in-dbt.

2. **Recruit speakers** from Berlin companies (Vinted, Trade Republic, Wolt, GetYourGuide, SumUp, Getsafe, etc.) who've actually shipped dbt + AI tooling together. Prioritize retrospective, honest talks over promotional ones.

3. **Set up the Slack backlog doc** in `#local-berlin` to capture open questions from the community. Make it visible — reference it in the opening remarks at the next event.

4. **Consider one cross-promotion with dltHub Berlin** for late 2026. Coordinate on shared audience; avoid scheduling conflicts.

5. **Optional:** Reach out to dbt Labs to confirm they're comfortable with dbt Labs' "What's new" slot staying fixed, and gauge openness to occasional ecosystem-partner updates alongside it (if you choose to explore that direction).

---

## Sources & Reference Data

- **dbt Labs 2026 State of Analytics Engineering Report:** https://www.getdbt.com/resources/state-of-analytics-engineering-2026
- **Fivetran + dbt Labs Merger (June 2026):** https://www.fivetran.com/press/fivetran-dbt-labs-complete-merger-to-create-the-data-infrastructure-for-trusted-ai-agents
- **Berlin Job Postings Analysis:** 132-record corpus from `analysis/job_descriptions/jd_data/`, 71% of 35 Berlin-based AE/BI roles require dbt.
- **Past Events:** 14 documented events in `analysis/dbt-meetups/berlin/events.json` (2021–2026).
