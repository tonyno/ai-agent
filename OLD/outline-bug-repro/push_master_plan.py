#!/usr/bin/env python3
"""
Push the local Master Plan markdown straight to Outline via the REST API.

We discovered the bullets-dropped bug lives in the claude.ai GetOutline MCP
server, not in Outline's REST API. So if we POST the markdown ourselves the
update lands intact.

What this script does
---------------------
  1. Reads the local master plan markdown.
  2. Strips the first-line H1 title (Outline stores title separately).
  3. Rewrites exported attachment paths (`attachments/<uuid>.png`) back to
     Outline's served path (`/api/attachments.redirect?id=<uuid>`) so the
     image still renders.
  4. Counts plain-bullet items in what we're about to send.
  5. Prints a summary and asks for confirmation.
  6. POST /api/documents.update to push the new body.
  7. POST /api/documents.info to fetch it back and verify the bullet count
     matches what we sent.

Setup
-----
  Uses the same env vars as outline_bug_repro.py:
    OUTLINE_BASE_URL   — e.g. https://oakslab.getoutline.com
    OUTLINE_API_TOKEN  — User Settings → API Tokens

Run
---
  python3 push_master_plan.py            # interactive, asks before pushing
  python3 push_master_plan.py --yes      # non-interactive, push immediately
  python3 push_master_plan.py --dry-run  # show what would be sent, do not push
"""

import argparse
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

# Target: the AI-First Transformation Master Plan in Outline
DOC_ID = "98005973-70d8-4f9f-8ad4-b2ba44336a14"
LOCAL_FILE = (
    Path(__file__).resolve().parent.parent / "ai-first-transformation-master-plan.md"
)

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}


def _post(path, payload):
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


def count_plain_bullets(md):
    n = 0
    for line in md.splitlines():
        s = line.lstrip()
        if (s.startswith("* ") or s.startswith("- ")) and not s.startswith(
            ("* [", "- [")
        ):
            n += 1
    return n


def prepare_body(md):
    """Strip H1 title and rewrite exported attachment paths."""
    lines = md.splitlines()
    if lines and lines[0].lstrip().startswith("# "):
        md = "\n".join(lines[1:]).lstrip("\n")

    # Markdown export turns Outline's attachment URLs into local relative paths:
    #   ![](attachments/<uuid>.png " =WxH")
    # Outline serves them via:
    #   ![](/api/attachments.redirect?id=<uuid> " =WxH")
    md = re.sub(
        r"attachments/([0-9a-f-]{36})\.[a-zA-Z0-9]+",
        r"/api/attachments.redirect?id=\1",
        md,
    )
    return md


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--yes", action="store_true", help="skip confirmation prompt")
    parser.add_argument(
        "--dry-run", action="store_true", help="prepare and print, but do not push"
    )
    args = parser.parse_args()

    if not (BASE_URL and API_TOKEN):
        sys.exit("Set OUTLINE_BASE_URL and OUTLINE_API_TOKEN env vars first.")
    if not LOCAL_FILE.exists():
        sys.exit(f"Local file not found: {LOCAL_FILE}")

    raw = LOCAL_FILE.read_text(encoding="utf-8")
    body = prepare_body(raw)
    sent_bullets = count_plain_bullets(body)

    print(f"Target document: {BASE_URL}/doc/Q9pNFGTOCA  ({DOC_ID})")
    print(f"Source file:     {LOCAL_FILE}")
    print(f"  Raw size:           {len(raw):>6} bytes")
    print(f"  Body after prep:    {len(body):>6} bytes  (H1 stripped, attachments rewritten)")
    print(f"  Plain-bullet items: {sent_bullets:>6}")
    print()

    if args.dry_run:
        print("--dry-run: not pushing. First 500 chars of prepared body:")
        print("-" * 60)
        print(body[:500])
        print("-" * 60)
        return

    if not args.yes:
        confirm = input(
            "About to overwrite the Master Plan in Outline. Proceed? [y/N] "
        ).strip().lower()
        if confirm != "y":
            sys.exit("Aborted.")

    print("Pushing via POST /api/documents.update ...")
    _post("/api/documents.update", {"id": DOC_ID, "text": body, "append": False})
    print("  Update OK.")
    print()

    print("Verifying via POST /api/documents.info ...")
    stored = _post("/api/documents.info", {"id": DOC_ID})["data"]
    stored_md = stored["text"]
    stored_bullets = count_plain_bullets(stored_md)
    print(f"  Stored size:         {len(stored_md)} bytes")
    print(f"  Stored bullet items: {stored_bullets}")
    print()

    print("=" * 60)
    print(f"  Sent:    {sent_bullets} plain-bullet items")
    print(f"  Stored:  {stored_bullets} plain-bullet items")
    print(f"  Dropped: {sent_bullets - stored_bullets}")
    print("=" * 60)
    if stored_bullets >= sent_bullets:
        print("OK — all bullets preserved.")
    else:
        print(
            "WARNING — some bullets were still dropped. The REST API may have its own\n"
            "edge cases with this document. Inspect diff manually."
        )


if __name__ == "__main__":
    main()
