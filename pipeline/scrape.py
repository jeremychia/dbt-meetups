"""Incremental scraper for dbt Meetup groups.

For each group it fetches the past-event list via Meetup's GraphQL endpoint,
diffs the event ids against the existing raw_events/<slug>.json, and scrapes
only the event pages that aren't there yet. Running it twice in a row adds
nothing the second time.

Usage:
    python pipeline/scrape.py                          # all groups in dbt-meetup-groups.json
    python pipeline/scrape.py --slugs oslo-dbt-group,taipei-dbt-meetup
    python pipeline/scrape.py --url https://www.meetup.com/berlin-dbt-meetup/ --name "Berlin dbt Meetup"
"""

import argparse
import json
import re
import time
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright

import config

PAST_EVENTS_QUERY_HASH = (
    "321388b1e4a11b17a57efe3ae7a90abfecbc703a4f4e99519772294924c21351"
)


def slug_from_url(url: str) -> str:
    return urlparse(url).path.strip("/").split("/")[0]


def get_past_events(page, slug: str) -> list[dict]:
    """Fetch all past events for a group via the getPastGroupEvents GraphQL query
    (cursor-paginated, returns exact totalCount, avoids DOM scroll/lazy-load timing issues).
    """
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
            "extensions": {
                "persistedQuery": {"version": 1, "sha256Hash": PAST_EVENTS_QUERY_HASH}
            },
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


def load_existing(slug: str) -> dict | None:
    path = config.RAW_EVENTS_DIR / f"{slug}.json"
    if path.exists():
        return json.loads(path.read_text())
    return None


def scrape_group_incremental(context, slug: str, group_name: str) -> None:
    existing = load_existing(slug)
    existing_events = existing["events"] if existing else []
    existing_ids = {str(e.get("event_id")) for e in existing_events}

    page = context.new_page()
    try:
        page.goto(
            f"https://www.meetup.com/{slug}/events/?type=past",
            wait_until="domcontentloaded",
            timeout=45000,
        )
        listed = get_past_events(page, slug)
        new_nodes = [n for n in listed if str(n.get("id")) not in existing_ids]
        print(
            f"{group_name} ({slug}): {len(listed)} past events listed, {len(new_nodes)} new",
            flush=True,
        )

        new_events = []
        for node in new_nodes:
            event_id = node.get("id")
            url = f"https://www.meetup.com/{slug}/events/{event_id}/"
            try:
                new_events.append(scrape_event(page, url))
            except Exception as e:
                new_events.append(
                    {"event_url": url, "event_id": event_id, "error": str(e)}
                )
            time.sleep(1)

        if not new_events and existing is not None:
            return

        # Meetup returns newest-first; keep the file in the same order.
        merged = new_events + existing_events
        out = {
            "group_name": (existing or {}).get("group_name") or group_name,
            "group_slug": slug,
            "events": merged,
            "metadata": {
                "total_events": len(merged),
                "last_scraped": time.strftime("%Y-%m-%d"),
            },
        }
        config.RAW_EVENTS_DIR.mkdir(parents=True, exist_ok=True)
        out_path = config.RAW_EVENTS_DIR / f"{slug}.json"
        out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
        print(f"  -> +{len(new_events)} events -> {out_path}", flush=True)
    except Exception as e:
        print(f"  FAILED {slug}: {e}", flush=True)
    finally:
        page.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--groups-file", default=str(config.GROUPS_FILE))
    parser.add_argument("--slugs", help="Comma-separated group slugs to restrict to")
    parser.add_argument("--url", help="Single group URL")
    parser.add_argument("--name", help="Single group display name (with --url)")
    args = parser.parse_args()

    if args.url:
        slug = slug_from_url(args.url)
        groups = [{"name": args.name or slug, "url": args.url}]
    else:
        groups = json.loads(open(args.groups_file).read())

    if args.slugs:
        wanted = {s.strip() for s in args.slugs.split(",")}
        groups = [g for g in groups if slug_from_url(g["url"]) in wanted]

    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            str(config.PROFILE_DIR), headless=True
        )
        for group in groups:
            scrape_group_incremental(
                context, slug_from_url(group["url"]), group["name"]
            )
        context.close()


if __name__ == "__main__":
    main()
