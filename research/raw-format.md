# raw research file format (input to assemble.py)

{
  "city": "London",                                  // label used for person.city defaults
  "chapter_name": "London dbt Meetup",
  "enriched_file": "enriched/london-dbt-meetup.json",
  "chapter_url": "https://www.meetup.com/<slug>/",
  "method": "one line: what you searched, how many searches, what you scanned",
  "lessons": ["Lesson: one sentence each, sources that worked or didn't"],
  "caveats": ["Titles, employers and cities come from public pages/snippets ... verify before outreach.", "..."],
  "sources_checked": [{"name": "...", "url": "...", "yielded": true, "note": "..."}],
  "community_channels": [{"name": "...", "url": "...", "note": "..."}],
  "companies": [
    {
      "name": "Monzo", "type": "employer|consultancy|vendor|outsourcing|recruiter|community|independent|other",
      "cities": ["London"], "local_presence": "confirmed|not_confirmed|none",
      "dbt_signal": "strong|medium|nice-to-have|weak|none",
      "stack_signals": ["dbt", "BigQuery"],
      "job_postings": [{"title": "...", "url": "...", "source": "company careers page", "dbt_mentioned_in_text": true,
                        "dbt_snippet": "...", "posted_date": null, "work_mode": null}],
      "other_evidence": [{"type": "company_blog|case_study|talk|blog_scanned|...", "url": "...", "note": "..."}],
      "notes": "...",
      "people": [
        {
          "name": "Full Name", "title": "Senior Analytics Engineer", "city": "London",
          "based_in_region": true,            // true = evidence in region, false = evidence elsewhere, null = unknown
          "pronouns": null,                   // only if self-stated publicly, never inferred
          "linkedin_urls": [],                // only linkedin.com/in URLs seen word for word in a search result
          "linkedin_confidence": "not_searched|low|medium|high",
          "lead_type": "proven_speaker|emerging_voice|featured|no_public_content",
          "sourced_via": ["conference_or_meetup_agenda|company_blog_scan|newsletter_or_blog|podcast|linkedin_search|women_in_data_community|chapter_meetup_history|other"],
          "priority_tier": "1|2|3|connector",
          "confidence": "High|Medium|Low",
          "suggested_talk_angle": "one line, a talk this person could give at the chapter",
          "notes": null,
          "speaker_evidence": [
            {"type": "talk|panel|podcast|workshop|webinar|blog|article|newsletter|oss|linkedin_post|organiser|host",
             "event": "Coalesce 2025", "title": "...", "date": "YYYY-MM-DD or YYYY-MM or null",
             "url": "...", "co_authors": [], "description": "one line", 
             "topics": ["1 to 3 values from TOPIC_VOCABULARY in pipeline/enrich.py, exact spelling"],
             "url_precision": "direct|overview_page", "confidence": "high|medium|low"}
          ]
        }
      ]
    }
  ]
}

the assembler derives ids, level, meetup_fit, watchlist, mentions_dbt, counts, past_meetups and past_chapter_talks, and adds every past chapter speaker from the enriched file automatically, so do not research or list past chapter speakers unless you found new evidence about them.
put each person under their current employer; one company record per company.
