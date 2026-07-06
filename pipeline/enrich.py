"""Incremental enrichment: raw_events/<slug>.json -> enriched/<slug>.json.

Finds raw events whose event_id is neither in the enriched file nor recorded
as skipped in enriched/_enrichment_state.json, and turns each one's raw page
text into the structured event schema (past-meetups.md steps 4-6) by calling
Claude headlessly through the Claude Code CLI (`claude -p`). Excluded events
(cancelled, Coalesce watch parties, empty pages) are recorded in the state
file so reruns don't re-process them — the whole step is idempotent.

Usage:
    python pipeline/enrich.py                     # all chapters
    python pipeline/enrich.py --slugs oslo-dbt-group
    python pipeline/enrich.py --baseline          # mark all current raw/enriched gaps as reviewed
    python pipeline/enrich.py --dry-run
"""
import argparse
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import config

DEFAULT_MODEL = "claude-opus-4-8"

TOPIC_VOCABULARY = [
    "dbt best practices", "dbt fundamentals", "dbt product features",
    "dbt product updates", "dbt migration & adoption", "data modeling",
    "data quality & testing", "data governance", "data mesh",
    "data engineering", "analytics engineering", "business intelligence",
    "semantic layer", "orchestration & ci/cd", "performance & scale",
    "modern data stack", "tools & ecosystem", "developer workflow",
    "project structure", "genai & llm", "team & org design",
    "career development", "community", "industry trends",
    "domain-specific use cases", "data warehouse & platforms",
]

PROMPT_TEMPLATE = """You are extracting structured data about a dbt meetup event from the raw text of its Meetup.com page.

Return ONLY a single JSON object, no markdown fences, no commentary.

If the event should be EXCLUDED — it was cancelled, the page has essentially no event content, or it is a Coalesce conference watch party / an event co-hosted across multiple chapters rather than a regular chapter event — return:
{{"exclude": true, "reason": "<short reason>"}}

Otherwise return an object with exactly these fields (use null when a value is unavailable, never omit a field):
- "event_url": "{event_url}"
- "event_id": {event_id}
- "event_name": event title
- "date": event date, "YYYY-MM-DD"
- "time": start time and duration, e.g. "19:00-21:00" (null if unknown)
- "location": venue name and city, or "Online" if virtual
- "attendees": number of RSVPs/attendees as an integer (null if unknown)
- "agenda": 1-2 sentence description of the event's theme
- "event_description": how the event described itself on Meetup (its own description text)
- "talks": array of talk objects, each with:
    - "title": talk title
    - "speaker_name": speaker name exactly as written on the page
    - "speaker_title": speaker role/company (null if unavailable)
    - "duration_minutes": talk length in minutes (null if unavailable)
    - "description": neutral 1-2 sentence summary of what the talk covers
    - "raw_text_excerpt": verbatim text from the raw page text that describes the talk
    - "topics": 1-3 topics, ordered most-relevant first, chosen ONLY from this vocabulary (never invent new topic strings): {topics}
- "additional_metadata": object with any other useful info (host name, recording link, slides link, notes), or null
- "raw_text": null

Notes:
- A social/networking-only event legitimately has an empty "talks" array — that is not a reason to exclude it.
- Do not tag talks with generic "case study" style topics; pick the actual subject matter.

Event URL: {event_url}
Page title: {page_title}

Raw page text:
---
{raw_text}
---"""

REQUIRED_FIELDS = [
    "event_url", "event_id", "event_name", "date", "time", "location",
    "attendees", "agenda", "event_description", "talks", "additional_metadata",
]


def find_claude_bin() -> str:
    env = os.environ.get("CLAUDE_BIN")
    if env and Path(env).exists():
        return env
    which = shutil.which("claude")
    if which:
        return which
    candidates = sorted(
        glob.glob(str(Path.home() / ".vscode/extensions/anthropic.claude-code-*/resources/native-binary/claude"))
    )
    if candidates:
        return candidates[-1]
    sys.exit("Could not find the `claude` CLI. Set CLAUDE_BIN or install Claude Code.")


def load_state() -> dict:
    if config.ENRICHMENT_STATE_FILE.exists():
        return json.loads(config.ENRICHMENT_STATE_FILE.read_text())
    return {"skipped": {}, "notes": "event_ids deliberately not enriched, per chapter"}


def save_state(state: dict) -> None:
    state["last_updated"] = time.strftime("%Y-%m-%d")
    config.ENRICHMENT_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    config.ENRICHMENT_STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def load_enriched(slug: str) -> dict:
    path = config.ENRICHED_DIR / f"{slug}.json"
    if path.exists():
        return json.loads(path.read_text())
    return {"events": [], "metadata": {"extraction_date": time.strftime("%Y-%m-%d"), "total_events": 0}}


def extract_json(text: str) -> dict:
    """Parse the model output, tolerating markdown fences or stray prose."""
    text = text.strip()
    fenced = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if fenced:
        text = fenced.group(1).strip()
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1:
        raise ValueError(f"no JSON object in output: {text[:200]!r}")
    return json.loads(text[start : end + 1])


def enrich_event(claude_bin: str, model: str, raw_event: dict) -> dict:
    prompt = PROMPT_TEMPLATE.format(
        event_url=raw_event.get("event_url"),
        event_id=raw_event.get("event_id"),
        page_title=raw_event.get("page_title", ""),
        raw_text=(raw_event.get("raw_text") or "")[:30000],
        topics=json.dumps(TOPIC_VOCABULARY),
    )
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT")}
    result = subprocess.run(
        [claude_bin, "-p", "--model", model],
        input=prompt,
        capture_output=True,
        text=True,
        timeout=600,
        env=env,
    )
    if result.returncode != 0:
        raise RuntimeError(f"claude CLI failed: {result.stderr[:500]}")
    return extract_json(result.stdout)


def validate(event: dict, raw_event: dict) -> list[str]:
    warnings = []
    for field in REQUIRED_FIELDS:
        if field not in event:
            warnings.append(f"missing field {field!r}")
    if event.get("date") and not re.match(r"^\d{4}-\d{2}-\d{2}$", str(event["date"])):
        warnings.append(f"bad date format: {event['date']!r}")
    vocab = set(TOPIC_VOCABULARY)
    for talk in event.get("talks") or []:
        for topic in talk.get("topics") or []:
            if topic not in vocab:
                warnings.append(f"topic outside vocabulary: {topic!r} (talk: {talk.get('title')!r})")
    return warnings


def process_chapter(slug: str, claude_bin: str, model: str, state: dict,
                    dry_run: bool, limit: int | None, processed_count: int) -> int:
    raw_path = config.RAW_EVENTS_DIR / f"{slug}.json"
    raw = json.loads(raw_path.read_text())
    raw_events = {str(e.get("event_id")): e for e in raw.get("events", [])}

    enriched = load_enriched(slug)
    enriched_ids = {str(e.get("event_id")) for e in enriched["events"]}
    skipped = state["skipped"].setdefault(slug, {})

    todo = [eid for eid in raw_events if eid not in enriched_ids and eid not in skipped]
    if not todo:
        return processed_count

    print(f"{slug}: {len(todo)} event(s) to enrich", flush=True)
    changed = False
    for eid in todo:
        if limit is not None and processed_count >= limit:
            break
        raw_event = raw_events[eid]
        if "error" in raw_event or not (raw_event.get("raw_text") or "").strip():
            skipped[eid] = "scrape error or empty raw_text"
            changed = True
            continue
        if dry_run:
            print(f"  [dry-run] would enrich {eid} ({raw_event.get('page_title', '')[:60]})", flush=True)
            processed_count += 1
            continue

        print(f"  enriching {eid} ({raw_event.get('page_title', '')[:60]})...", flush=True)
        try:
            result = enrich_event(claude_bin, model, raw_event)
        except Exception as e:
            print(f"    ERROR: {e} — leaving for next run", flush=True)
            continue

        processed_count += 1
        if result.get("exclude"):
            skipped[eid] = result.get("reason", "excluded by enrichment")
            print(f"    excluded: {skipped[eid]}", flush=True)
            changed = True
            continue

        result["event_id"] = int(eid)
        # Keep the scraped page text on the record for recomputation, as in
        # the original enriched files.
        result["raw_text"] = raw_event.get("raw_text")
        for w in validate(result, raw_event):
            print(f"    WARNING: {w}", flush=True)
        enriched["events"].append(result)
        changed = True
        print(f"    added: {result.get('event_name')} ({result.get('date')}), {len(result.get('talks') or [])} talks", flush=True)

    if changed and not dry_run:
        enriched["events"].sort(key=lambda e: e.get("date") or "", reverse=True)
        enriched["metadata"]["total_events"] = len(enriched["events"])
        enriched["metadata"]["last_enriched"] = time.strftime("%Y-%m-%d")
        config.ENRICHED_DIR.mkdir(parents=True, exist_ok=True)
        out_path = config.ENRICHED_DIR / f"{slug}.json"
        out_path.write_text(json.dumps(enriched, indent=2, ensure_ascii=False))
        save_state(state)
    return processed_count


def run_baseline(state: dict) -> None:
    """Mark every current raw/enriched gap as reviewed so the pipeline only
    processes events that appear after this point."""
    today = time.strftime("%Y-%m-%d")
    added = 0
    for raw_path in sorted(config.RAW_EVENTS_DIR.glob("*.json")):
        if raw_path.name.startswith("_"):
            continue
        slug = raw_path.stem
        raw = json.loads(raw_path.read_text())
        enriched = load_enriched(slug)
        enriched_ids = {str(e.get("event_id")) for e in enriched["events"]}
        skipped = state["skipped"].setdefault(slug, {})
        for e in raw.get("events", []):
            eid = str(e.get("event_id"))
            if eid not in enriched_ids and eid not in skipped:
                skipped[eid] = f"baseline {today}: in raw_events but not enriched before the pipeline existed"
                added += 1
    save_state(state)
    print(f"baseline: marked {added} pre-existing gaps as reviewed")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slugs", help="Comma-separated chapter slugs (raw_events filenames without .json)")
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--limit", type=int, help="Max events to enrich this run")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--baseline", action="store_true",
                        help="Mark all current raw/enriched gaps as reviewed and exit")
    args = parser.parse_args()

    state = load_state()
    if args.baseline:
        run_baseline(state)
        return

    claude_bin = find_claude_bin() if not args.dry_run else ""
    if args.slugs:
        slugs = [s.strip() for s in args.slugs.split(",")]
    else:
        slugs = sorted(
            p.stem for p in config.RAW_EVENTS_DIR.glob("*.json") if not p.name.startswith("_")
        )

    processed = 0
    for slug in slugs:
        processed = process_chapter(slug, claude_bin, args.model, state,
                                    args.dry_run, args.limit, processed)
        if args.limit is not None and processed >= args.limit:
            print(f"limit {args.limit} reached", flush=True)
            break
    print(f"done: {processed} event(s) processed", flush=True)


if __name__ == "__main__":
    main()
