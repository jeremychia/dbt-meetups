# dbt Meet Up - [Quarter/Year, e.g. Q3 2025]

## Event Setup

**Location:** *(required)*
- Venue name
- Full address
- Maps link
- Area within venue used for event (e.g. Common Area)
- Area within venue used for food/catering

**Proposed Date(s):** *(required)*
- Option 1
- Option 2
- Option 3 ✅ (confirmed)

**Point of Contacts:** *(required — the two people who can make on-the-spot decisions if something goes wrong on the day: venue access issues, catering no-shows, AV problems)*
- From host company: [Name] — Slack channel: #[channel] (Private)
- From dbt: [Name] — Slack channel: #[channel] (Private)

**Participants:** *(required)*
- Estimated capacity: ~[N] people — *past events have run 60–200; a company-office venue is usually 60–130, larger dedicated venues (e.g. Umspannwerk Ampere) can hold ~200*
- Sign-up: event page on [City] dbt Meetup
- Entrance/exit logistics (which doors, escort requirements — *some office venues require a host to walk guests up from the lobby/reception rather than badge access; check with host company's point of contact*)
- Building/security registration required (e.g. Proxyclick) — register under "[Company Name]" (*the name the venue's front desk/security system expects — usually the host company, not "dbt" or "dbt Meetup"*)
- Guest data to collect: first name, last name, company, email
- Data retention: guest list used only for building registration + attendance; delete after [N] days
- Doors close time: [time] — *typically 30–40 min after start (e.g. 6:40 PM for a 6:00 PM start)* — communicate on event page (attendees book out quickly; encourage RSVP updates so waitlist can fill)
- Waitlist: enabled on [City] dbt Meetup page once capacity reached

**Emergency & Safety:** *(required — confirm with venue host before the event, not on the day)*
- Fire exits / evacuation route: [location] — confirm with venue host
- First-aid kit location: [location]
- Emergency contact on-site: [Name], [phone]

**Session Direction:** *(optional — skip if this is a standard-format edition)*
- [e.g. Smaller session / larger session, more networking vs. more content, topics not yet covered]

**Agenda:** *(required — this is the source of truth; the Meetup.com Event Page template below must match these times exactly, so fill this in first)*

| Time | Item | Presented by |
|---|---|---|
| 6:00 PM | Check in/registration | |
| 6:30 PM | Welcome Remarks | [Host/Company] |
| 6:40 PM | Updates from dbt | [Speaker], dbt Labs |
| 6:55 PM | Talk 1 | [Speaker], [Company] |
| 7:15 PM | Break | |
| 7:30 PM | Talk 2 / Panel | [Speaker], [Company] |
| 7:50 PM | Networking / Closing Remarks | |

*(Example times shown are the standard pattern across past events — a 6:00–9:00 PM slot with doors closing ~40 min in. Adjust only if this edition deliberately runs differently.)*

**Options for Talks:** *(required)*
- [Candidate talk/topic ideas]
- Avoid topics already extensively covered in past sessions (check Past Sessions log)
- Candidates: `berlin_dbt_companies.json`. Start with tier-1 `emerging_voice` leads (first-time speakers), then tier-1 `proven_speaker` leads.

**Line-up balance check:** *(required — review together with the co-organisers before confirming speakers)*
- [ ] Gender balance: if the draft line-up is all men, go back to the leads with `sourced_via: women_in_data_community` and ask the community connectors (PyLadies Berlin, Women in Big Data Berlin) for introductions
- [ ] At least one first-time speaker (`emerging_voice`) alongside an experienced one
- [ ] A mix of scale-ups and enterprises, and of local and international speakers
- [ ] Topics don't repeat the last 2–3 events (compare the `topics` tags)
- *This is the organisers' judgement, not a number worked out from the dataset. The dataset doesn't record or infer anyone's gender.*

**Notes:** *(required)*
- Slides shared with participants? [Y/N]
- Recording? [Y/N]

---

## Pre-Session

| Task | Responsible | Status |
|---|---|---|
| Order food (budget: $[amount]) — ensure vegetarian/vegan + non-alcoholic options | | |
| Create event on [City] dbt Meetup page | | |
| Provide guest list (first name, last name, company, email) for building registration | | |
| Create guests in building security system (e.g. Proxyclick) | | |
| Communicate session details to speakers; coordinate slide submission | | |
| Liaise with IT on equipment setup (microphones, screen/projector, clicker) | | |
| Prepare company/host presentation | | |
| Prepare feedback form | | |
| Prepare swag (stickers, bags, etc.) | | |
| Prepare name tags + "no photos" opt-out stickers | | |

---

## On Day of Session

| Task | Manpower | Responsible |
|---|---|---|
| Coordinate food arrival (by [time]) | 1–2 people | |
| Arrange chairs/tables | 3+ people | |
| Coordinate with speakers | 1 person | |
| Host welcome/closing remarks — include photo-consent note, code of conduct link, "sit in back if avoiding photos" note | 1 person | |
| Welcome guests at street/building entrance | 1 person | |
| Welcome guests at lift/lobby | 1 person | |
| Welcome guests at reception/check-in — hand out name tags, explain opt-out stickers | 1 person | |
| Take event photos | 1 person | |

---

## After Session

| Task | Responsible |
|---|---|
| Collate feedback | |
| Return chairs/tables to original layout | |
| Post event summary in community Slack channel | |
| Submit reimbursement request for food (see running-a-meetup reference doc) | |

---

## Past Sessions

*(Append a new entry after each event — date, venue, talk titles)*

- **[Date], [Venue]**
  1. Talk: [Title]
  2. Talk: [Title]

---

## Resources
- Slides template: [link] (make a fresh copy per event — do not copy past slides)
- Running-a-meetup reference guide: [link]

---

## Meetup.com Event Page — Copy-Paste Template

*(Fill in from the sections above, then paste into the event page on [City] dbt Meetup.)*

**Event Name:** `Berlin dbt Meetup` (add a suffix for special editions, e.g. `- Post-Coalesce edition`)

**Date & Time:** `[Day], [Month] [DD], [YYYY], 6:00 PM – 9:00 PM CET/CEST` (standard slot — deviate only deliberately)

**Location:** Venue name, full address, entrance note if non-obvious, building access window if restricted

**Description:**
```
Networking events open to all folks working with data — data analysts, scientists,
engineers, architects, and more. Focus on community experiences with dbt and related
topics like analytics engineering, data operations, and team structures.
```

**Agenda (paste into description):** *(copy directly from the Agenda table in Event Setup above — do not re-derive times here; if you need to change a time, change it in that table first)*
```
[Time] – Check-in / Registration
[Time] – Welcome remarks ([Host/Company])
[Time] – dbt Labs updates ([Speaker], dbt Labs)
[Time] – Talk 1: [Title] ([Speaker], [Company])
[Time] – Break
[Time] – Talk 2 / Panel: [Title] ([Speaker], [Company])
[Time] – Networking, food & drinks

Doors close at [same time as Agenda table] — attendees are urged to update their RSVP if plans
change so waitlisted members can join. This event typically reaches capacity
quickly.

Health & safety: please don't attend if you're feeling unwell. Alcohol is
served — non-alcoholic options are available and drink responsibly. Venue
fire exits and first-aid location will be pointed out during welcome remarks.

Join the conversation in the dbt Slack #local-berlin channel: [link]
```

**Pre-publish checklist:**
- [ ] Event name set (+ edition suffix if applicable)
- [ ] Date/time set — default 6:00–9:00 PM
- [ ] Venue + address + entrance/access notes filled in
- [ ] Doors-close time matches the Event Setup Agenda table above (not re-entered independently)
- [ ] Speaker names, titles, and talk titles filled in
- [ ] Health & safety note included (illness/alcohol/exits)
- [ ] #local-berlin Slack channel link included
- [ ] Capacity set; waitlist enabled
- [ ] Talk topics cross-checked against Past Sessions log above to avoid repeats (2–3 talks is the norm; 4+ has historically run long)
