"""
Scrape past events for one or more dbt Meetup groups using an authenticated
persistent browser session (see login.py).

Usage:
    python scrape.py --slug abuja-dbt-meetup --name "Abuja dbt Meetup"
    python scrape.py --groups-file dbt-meetup-groups.json --out-dir jd_data
"""
import argparse
import json
import re
import time
from pathlib import Path
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

PROFILE_DIR = Path(__file__).parent / ".browser-profile"

PAST_EVENTS_QUERY_HASH = "321388b1e4a11b17a57efe3ae7a90abfecbc703a4f4e99519772294924c21351"


def slug_from_url(url: str) -> str:
    return urlparse(url).path.strip("/").split("/")[0]


def get_past_events(page, slug: str) -> list[dict]:
    """Fetch all past events for a group via Meetup's getPastGroupEvents GraphQL query
    (cursor-paginated, returns exact totalCount, avoids DOM scroll/lazy-load timing issues)."""
    all_events = []
    after = None
    before_datetime = time.strftime("%Y-%m-%dT%H:%M:%S.000Z", time.gmtime())

    for _ in range(50):
        variables = {"urlname": slug, "beforeDateTime": before_datetime}
        if after:
            variables["after"] = after
        payload = {
            "operationName": "getPastGroupEvents",
            "variables": variables,
            "extensions": {"persistedQuery": {"version": 1, "sha256Hash": PAST_EVENTS_QUERY_HASH}},
        }
        result = page.evaluate(
            """async (payload) => {
                const res = await fetch('/gql2', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify(payload),
                });
                return await res.json();
            }""",
            payload,
        )
        events_data = (result.get("data") or {}).get("groupByUrlname") or {}
        events_data = events_data.get("events") or {}
        edges = events_data.get("edges", [])
        page_info = events_data.get("pageInfo", {})

        all_events.extend(e["node"] for e in edges)
        if not page_info.get("hasNextPage") or not edges:
            break
        after = page_info.get("endCursor")

    return all_events


def scrape_event(page, event_url: str) -> dict:
    page.goto(event_url, wait_until="networkidle", timeout=30000)
    page.wait_for_timeout(1500)

    title = page.title()
    body_text = page.inner_text("body")

    event_id_match = re.search(r"/events/(\d+)/", event_url)
    event_id = int(event_id_match.group(1)) if event_id_match else None

    return {
        "event_url": event_url,
        "event_id": event_id,
        "page_title": title,
        "raw_text": body_text,
    }


def scrape_group(context, slug: str, group_name: str) -> dict:
    last_error = None
    for attempt in range(2):
        page = context.new_page()
        try:
            page.goto(f"https://www.meetup.com/{slug}/events/?type=past", wait_until="networkidle", timeout=45000)
            past_events = get_past_events(page, slug)
            events = []
            for pe in past_events:
                event_id = pe.get("id")
                url = f"https://www.meetup.com/{slug}/events/{event_id}/"
                try:
                    events.append(scrape_event(page, url))
                except Exception as e:
                    events.append({"event_url": url, "event_id": event_id, "error": str(e)})
                time.sleep(1)

            return {
                "group_name": group_name,
                "group_slug": slug,
                "events": events,
                "metadata": {
                    "total_events": len(events),
                },
            }
        except Exception as e:
            last_error = str(e)
            print(f"  attempt {attempt + 1} failed for {slug}: {last_error}", flush=True)
        finally:
            page.close()

    return {
        "group_name": group_name,
        "group_slug": slug,
        "events": [],
        "metadata": {
            "total_events": 0,
            "error": last_error,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--slug", help="Single group slug, e.g. abuja-dbt-meetup")
    parser.add_argument("--name", help="Single group display name")
    parser.add_argument("--url", help="Single group URL (overrides --slug)")
    parser.add_argument("--groups-file", help="Path to dbt-meetup-groups.json for batch mode")
    parser.add_argument("--out-dir", default="jd_data", help="Output directory for per-group JSON files")
    parser.add_argument("--resume", action="store_true", help="Skip groups that already have an output file")
    args = parser.parse_args()

    out_dir = Path(__file__).parent / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(str(PROFILE_DIR), headless=True)

        if args.groups_file:
            groups = json.loads(Path(args.groups_file).read_text())
        elif args.url or args.slug:
            slug = slug_from_url(args.url) if args.url else args.slug
            groups = [{"name": args.name or slug, "url": args.url or f"https://www.meetup.com/{slug}/"}]
        else:
            parser.error("Provide --groups-file or --slug/--url")
            return

        for group in groups:
            slug = slug_from_url(group["url"])
            out_path = out_dir / f"{slug}.json"
            if args.resume and out_path.exists():
                print(f"Skipping {group['name']} ({slug}), already scraped", flush=True)
                continue
            print(f"Scraping {group['name']} ({slug})...", flush=True)
            result = scrape_group(context, slug, group["name"])
            out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False))
            print(f"  -> {len(result['events'])} events -> {out_path}", flush=True)

        context.close()


if __name__ == "__main__":
    main()
