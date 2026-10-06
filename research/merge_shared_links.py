"""Resolves people in one city file who share a LinkedIn or profile link, which validate.py rejects.

usage, from the repo root: python3 research/merge_shared_links.py [<city file> ...]   (no files: every city file)

two records with the same link are one person when every part of the shorter name is in the longer one: a middle
name added or the order swapped ("Rasmus Nes" and "Rasmus Nikolai Nes", "Sofia Alevizopoulou" and "Alevizopoulou Sofia"). they are merged with merge_people.py, keeping the record not sourced
from github. otherwise they are two people, and an event page gave one of them the other's link, so the link is removed
from the second record. sharing a first and last name is not enough: Maria Alejandra Franco and Maria Isabel Arcila
Franco are two people.
"""

import glob, json, re, subprocess, sys, unicodedata
from collections import Counter
from assemble import standard_counts


def tokens(name):
    return [x for x in re.sub(r"[^a-z ]", " ", unicodedata.normalize("NFKD", re.sub(r"\(.*?\)", "", name)).encode("ascii", "ignore").decode().lower()).split() if len(x) > 1]


def same_person(a, b):
    """every part of the shorter name is in the longer one: a middle name added, or the order swapped."""
    short, long = sorted((set(tokens(a)), set(tokens(b))), key=len)
    return len(short) >= 2 and short <= long


def keys(p):
    return ["li:" + re.sub(r"^.*linkedin\.com/in/", "", u).split("?")[0].strip("/").lower() for u in p["linkedin_urls"]] + \
           ["pu:" + u["url"].lower().rstrip("/") for u in p["profile_urls"]]


def first_shared(d):
    owner, people = {}, {}
    for c in d["companies"]:
        for p in c["people"]:
            people[p["id"]] = p
            for k in keys(p):
                if k in owner and owner[k] != p["id"]:
                    return people[owner[k]], p, k
                owner.setdefault(k, p["id"])
    return None


def resolve(path):
    merged = unlinked = 0
    for _ in range(200):
        d = json.load(open(path))
        found = first_shared(d)
        if not found:
            break
        a, b, k = found
        if same_person(a["name"], b["name"]):
            keep, drop = (a, b) if "github" not in a["sourced_via"] else (b, a)
            subprocess.run(["python3", "research/merge_people.py", path, keep["id"], drop["id"]], capture_output=True, check=True)
            print(f"{path}: merged {drop['name']} into {keep['name']}")
            merged += 1
        else:
            raw = open(path).read()
            for c in d["companies"]:
                for p in c["people"]:
                    if p["id"] == b["id"]:
                        p["linkedin_urls"] = [u for u in p["linkedin_urls"] if "li:" + re.sub(r"^.*linkedin\.com/in/", "", u).split("?")[0].strip("/").lower() != k]
                        p["profile_urls"] = [u for u in p["profile_urls"] if "pu:" + u["url"].lower().rstrip("/") != k]
                        p["has_linkedin"] = bool(p["linkedin_urls"])
            d["metadata"]["counts"] = standard_counts(d)
            open(path, "w").write(json.dumps(d, ensure_ascii=False, indent=2) + ("\n" if raw.endswith("\n") else ""))
            print(f"{path}: {k[3:]} kept on {a['name']}, removed from {b['name']}")
            unlinked += 1
    return merged, unlinked


if __name__ == "__main__":
    files = sys.argv[1:] or sorted(glob.glob("*/*_dbt_companies.json"))
    totals = Counter()
    for f in files:
        m, u = resolve(f)
        totals.update(merged=m, unlinked=u)
    print(f"{totals['merged']} merged, {totals['unlinked']} links removed")
