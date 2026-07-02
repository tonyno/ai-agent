#!/usr/bin/env python3
"""
Outline API bug reproduction
============================

Bug: Plain bullet lists (`*` or `-`, *not* `- [ ]` checkboxes) are dropped by
Outline's markdown-to-ProseMirror parser when they appear in certain positions
of a document submitted via the REST API.

What this script does
---------------------
  1. Reads `outline-bug-repro.md` from the same directory.
  2. Creates a new document in your test collection via
     POST /api/documents.create
  3. Fetches the document back via POST /api/documents.info
  4. Prints the markdown you sent vs the markdown Outline stored.
  5. Counts how many plain bullet items were lost.

Endpoints exercised
-------------------
  POST /api/documents.create   — initial write, runs the markdown parser
  POST /api/documents.info     — read back the stored markdown

Note: the same bug also reproduces with POST /api/documents.update on an
existing document — both endpoints feed the same parser.

Setup
-----
  export OUTLINE_BASE_URL='https://your-outline.example.com'   # no trailing slash
  export OUTLINE_API_TOKEN='ol_api_...'                         # User Settings → API Tokens
  export OUTLINE_COLLECTION_ID='<a-test-collection-id>'         # somewhere safe to create a throwaway doc

Run
---
  pip install requests
  python3 outline_bug_repro.py
"""

import os
import re
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    sys.exit("Please run: pip install requests")


BASE_URL = os.environ.get("OUTLINE_BASE_URL", "").rstrip("/")
API_TOKEN = os.environ.get("OUTLINE_API_TOKEN", "")
COLLECTION_REF = os.environ.get("OUTLINE_COLLECTION_ID", "")

if not (BASE_URL and API_TOKEN and COLLECTION_REF):
    sys.exit(
        "Missing env vars. Need OUTLINE_BASE_URL, OUTLINE_API_TOKEN, "
        "OUTLINE_COLLECTION_ID (UUID, URL slug, or full collection URL)."
    )

UUID_RE = re.compile(
    r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I
)

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

SAMPLE_PATH = Path(__file__).parent / "outline-bug-repro.md"
SAMPLE_MD = SAMPLE_PATH.read_text(encoding="utf-8")


def _post(path, payload):
    """POST helper that surfaces the response body on errors."""
    url = f"{BASE_URL}{path}"
    r = requests.post(url, headers=HEADERS, json=payload, timeout=30)
    if not r.ok:
        sys.stderr.write(
            f"\nRequest failed: POST {url}\n"
            f"  status: {r.status_code} {r.reason}\n"
            f"  body:   {r.text[:2000]}\n"
        )
        r.raise_for_status()
    return r.json()


def resolve_collection_uuid(ref):
    """Accept a UUID, a URL slug like 'tondas-GU60nyTqx9', or a full collection URL,
    and return the collection's UUID by listing collections and matching."""
    # Strip a full URL down to its slug, e.g.
    #   https://oakslab.getoutline.com/collection/tondas-GU60nyTqx9/recent
    # -> tondas-GU60nyTqx9
    m = re.search(r"/collection/([^/?#]+)", ref)
    if m:
        ref = m.group(1)

    if UUID_RE.match(ref):
        return ref

    # Slug case: list collections and match by urlId suffix or name.
    # urlId is the trailing token after the last '-' in the slug.
    candidate_urlid = ref.rsplit("-", 1)[-1] if "-" in ref else ref

    print(
        f"  '{ref}' is not a UUID; resolving via POST /api/collections.list ..."
    )
    matches = []
    all_seen = []
    offset = 0
    while True:
        page = _post(
            "/api/collections.list", {"offset": offset, "limit": 100}
        )
        cols = page.get("data", [])
        if not cols:
            break
        for c in cols:
            all_seen.append((c["name"], c["id"], c.get("urlId", "")))
            if c.get("urlId") == candidate_urlid or c.get("urlId") == ref:
                matches.append(c)
        offset += len(cols)
        if len(cols) < 100:
            break

    if len(matches) == 1:
        uuid = matches[0]["id"]
        print(f"  Resolved '{ref}' -> {uuid}  (name: {matches[0]['name']!r})")
        return uuid

    sys.stderr.write(
        f"\nCould not resolve collection '{ref}' to a UUID.\n"
        f"Collections visible to this token:\n"
    )
    for name, uuid, urlid in all_seen:
        sys.stderr.write(f"  - {name!r:40}  UUID={uuid}  urlId={urlid!r}\n")
    sys.exit(
        "\nSet OUTLINE_COLLECTION_ID to the UUID from the list above, or to a "
        "matching urlId / full collection URL."
    )


def create_doc(collection_uuid):
    """Create a new document with our test markdown."""
    payload = {
        "title": "Outline API Bug Repro — Plain Bullets Dropped",
        "text": SAMPLE_MD,
        "collectionId": collection_uuid,
        "publish": True,
    }
    return _post("/api/documents.create", payload)["data"]


def update_doc(doc_id):
    """Re-send the SAME markdown via documents.update.
    This is the endpoint that originally surfaced the bug for us."""
    payload = {
        "id": doc_id,
        "text": SAMPLE_MD,
        "append": False,
    }
    return _post("/api/documents.update", payload)["data"]


def fetch_doc(doc_id):
    """Fetch the document body back as markdown."""
    return _post("/api/documents.info", {"id": doc_id})["data"]


def count_plain_bullets(md):
    """Count plain-bullet lines (excluding checkbox items)."""
    n = 0
    for line in md.splitlines():
        s = line.lstrip()
        if (s.startswith("* ") or s.startswith("- ")) and not s.startswith(
            ("* [", "- [")
        ):
            n += 1
    return n


def main():
    print(f"Outline instance: {BASE_URL}")
    print(f"Sample markdown:  {SAMPLE_PATH}  ({len(SAMPLE_MD)} bytes)")
    print()

    print("Step 0: Resolve collection reference to UUID ...")
    collection_uuid = resolve_collection_uuid(COLLECTION_REF)
    print()

    print("Step 1: POST /api/documents.create with the sample markdown ...")
    doc = create_doc(collection_uuid)
    doc_id = doc["id"]
    url_id = doc["urlId"]
    print(f"  Created document: {BASE_URL}/doc/{url_id}")
    print(f"  Document ID:      {doc_id}")
    print()

    print("Step 2: POST /api/documents.info to read stored markdown after CREATE ...")
    after_create = fetch_doc(doc_id)["text"]
    print(f"  Got {len(after_create)} bytes back.")
    print()

    print("Step 3: POST /api/documents.update with the SAME markdown ...")
    update_doc(doc_id)
    print("  Update OK.")
    print()

    print("Step 4: POST /api/documents.info to read stored markdown after UPDATE ...")
    after_update = fetch_doc(doc_id)["text"]
    print(f"  Got {len(after_update)} bytes back.")
    print()

    sent_bullets = count_plain_bullets(SAMPLE_MD)
    after_create_bullets = count_plain_bullets(after_create)
    after_update_bullets = count_plain_bullets(after_update)

    print("=" * 78)
    print(f"SENT MARKDOWN  ({sent_bullets} plain-bullet items)")
    print("=" * 78)
    print(SAMPLE_MD)
    print()

    print("=" * 78)
    print(f"STORED AFTER documents.create  ({after_create_bullets} plain-bullet items)")
    print("=" * 78)
    print(after_create)
    print()

    print("=" * 78)
    print(f"STORED AFTER documents.update  ({after_update_bullets} plain-bullet items)")
    print("=" * 78)
    print(after_update)
    print()

    print("=" * 78)
    print("RESULT")
    print("=" * 78)
    print(f"  Plain-bullet items sent:                  {sent_bullets}")
    print(f"  Plain-bullet items after documents.create:{after_create_bullets:>4}  (lost: {sent_bullets - after_create_bullets})")
    print(f"  Plain-bullet items after documents.update:{after_update_bullets:>4}  (lost: {sent_bullets - after_update_bullets})")
    print()
    stored_bullets = min(after_create_bullets, after_update_bullets)

    if stored_bullets < sent_bullets:
        print("  >>> BUG REPRODUCED <<<")
        print()
        print("  EXPECTED")
        print("  --------")
        print("  Every plain bullet list in the sent markdown round-trips intact.")
        print("  CommonMark allows a bullet list to follow any block element (heading,")
        print("  paragraph, hr, table, admonition, etc.) so all of Sections 1–7")
        print("  should be present in the stored markdown.")
        print()
        print("  ACTUAL")
        print("  ------")
        print("  Plain `*` / `-` bullet lists are dropped by the markdown parser")
        print("  when they appear in these positions:")
        print("    - directly after an H2 heading mid-document  (Section 4)")
        print("    - directly after a bold-only paragraph        (Section 5)")
        print("    - directly after a 'Label:' plain paragraph   (Section 6)")
        print("    - directly after an H3 heading                (Section 7)")
        print()
        print("  Bullet lists that survive in the same upload:")
        print("    - the very first list at the top of the document  (Section 1)")
        print("    - lists inside a `> blockquote`                   (Section 2)")
        print("    - checkbox lists (`- [ ]` / `- [x]`)              (Section 3)")
        print()
        print("  Notes")
        print("  -----")
        print("    - The output normalises `-` to `*`, so this is not about the")
        print("      bullet character used in the source markdown.")
        print("    - The bug is order-dependent: the same `## H2 + *bullets`")
        print("      pattern works in Section 1 (top of doc) but fails in")
        print("      Section 4 (mid-doc). Something earlier in the document")
        print("      appears to corrupt parser state.")
        print("    - Suspected upstream tokens that may flip the state: `:::info` /")
        print("      `:::warning` admonitions, GFM tables, `==highlight==` runs,")
        print("      `\\` hard line breaks.")
    else:
        print("  All bullets preserved.")
        print("  Either the bug is fixed on this instance, or this minimal repro")
        print("  is not triggering it on your setup. Try inserting the failing")
        print("  patterns into a larger document that already contains admonitions,")
        print("  tables, or highlights.")


if __name__ == "__main__":
    main()
