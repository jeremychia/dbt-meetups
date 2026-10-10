"""Profiles a reviewer turned down for a person, kept in rejected_matches.json so no later search offers them again.

the file is keyed "<city folder>/<person id>", each with a list of {"url", "reason"}. delete an entry when new evidence ties that profile to the person.
"""

import json, os, re

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rejected_matches.json")


def key(url):
    """compares linkedin links by profile slug, so country subdomains, query strings and trailing slashes do not matter."""
    url = re.sub(r"[?#].*$", "", url.strip()).rstrip("/").lower()
    m = re.search(r"linkedin\.com/in/([^/]+)", url)
    return "li:" + m.group(1) if m else url


def load_rejected():
    return json.load(open(PATH)) if os.path.exists(PATH) else {}


def is_rejected(rejected, folder, pid, url):
    return key(url) in {key(r["url"]) for r in rejected.get(f"{folder}/{pid}", [])}


def add_rejected(rejected, folder, pid, url, reason):
    if not is_rejected(rejected, folder, pid, url):
        rejected.setdefault(f"{folder}/{pid}", []).append({"url": url, "reason": reason})
        json.dump(dict(sorted(rejected.items())), open(PATH, "w"), ensure_ascii=False, indent=1)
        open(PATH, "a").write("\n")
