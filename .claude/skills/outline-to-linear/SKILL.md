---
name: outline-to-linear
description: Reads the "Next steps" (or similar) section of an Outline meeting doc and creates Linear tickets for each action item in a user-specified team's current cycle. Skips items that already have a Linear link or issue ID. Writes the new ticket links back into the Outline doc next to each item. Use when the user says "/outline-to-linear", or asks to "create Linear tickets from this Outline doc", "turn next steps into Linear tickets", or similar.
---

# Outline to Linear

Convert action items from the "Next steps" section of an Outline meeting note into Linear tickets in a specified team's current cycle, and write the ticket links back into the Outline doc.

The skill is idempotent: re-running on the same doc after a successful pass will create zero new tickets, because each previously-created ticket leaves a `linear.app` URL and an issue identifier next to its source bullet.

## Inputs

Two URLs, taken from the user's prompt (or asked for if missing):

| Input | Example |
|---|---|
| Outline document URL | `https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-VMvYSEJT43` |
| Linear team URL | `https://linear.app/oakslab/team/AISG/active` |

- The Outline document ID is the trailing segment after the LAST `-` in the doc URL path (e.g., `VMvYSEJT43`).
- The Linear team key is the `team/<KEY>/...` segment (e.g., `AISG`).

If either input is missing, ask the user for it before doing anything else.

## Steps

### 1. Parse inputs

Extract the Outline document ID and the Linear team key from the URLs. If either is missing, ask.

### 2. Fetch the Outline document

Call `mcp__claude_ai_GetOutline__fetch` with `resource: "document"` and `id` set to the parsed document ID. Keep the full markdown `text`, the document `id`, `urlId`, and `title`. Build the full document URL by combining the Outline workspace origin with the `urlId` path (used later for the backlink in ticket descriptions).

### 3. Locate the action-items section

Scan the document for the FIRST heading (any level: `#`, `##`, `###`, …) whose text — case-insensitive and whitespace-normalized — matches any of:

- "next steps"
- "action items"
- "action points"
- "follow-ups" / "follow ups"

The section runs from that heading down to the next heading of EQUAL OR HIGHER level (or end of document). If no matching heading exists, stop and tell the user which headings WERE found.

### 4. Extract candidate bullets

Within the section, identify the indentation of the first bullet line (`-`, `*`, or `+` after any leading spaces). That indentation defines "top-level". Each top-level bullet line is one candidate; any deeper-indented bullet lines or non-bullet continuation lines that follow before the next top-level bullet belong to that candidate as sub-content.

### 5. Classify each candidate

For each candidate, classify as one of:

- **`already_linked`** — the top-level bullet line contains either a `linear.app/...` URL or an issue identifier matching `\[?[A-Z]{2,}-\d+\]?` (e.g., `AISG-123`, `[AISG-42]`). Skip — do not create a new ticket.
- **`action_item`** — Claude judges this is a real commitment, assignment, or directive. Continue processing below.
- **`noise`** — transcript excerpt, general prose, or discussion that happens to be in the section as a bullet (e.g., a bullet like `- Tonda Kmoch: Uh when it comes to the product sync…`). Skip — but show it on the approval table so the user can override.

For each `action_item`, additionally:

- **Propose an assignee** by parsing a leading `[Name]` bracketed token or a leading `Name:` segment from the bullet text, if present. If the bullet has no leading name token, the assignee proposal is empty (will be resolved at the approval gate).
- **Propose a title:** a short imperative summary of the action, target ~60 characters.

### 6. Resolve the Linear team and cycle

- Call `mcp__claude_ai_Linear__list_teams`. Find the team whose `key` equals the parsed team key (case-insensitive). If not found, ask the user.
- Call `mcp__claude_ai_Linear__list_cycles` for that team. Pick the cycle where `startsAt <= now < endsAt`.
- If NO active cycle exists, do NOT silently fall back. Ask the user: (a) create the tickets without a cycle, (b) pick a specific cycle from the available list, or (c) abort. Use the answer for all tickets in this run.

### 7. Resolve assignees

Call `mcp__claude_ai_Linear__list_users` once. For each `action_item` candidate that has a proposed assignee name, do a case-insensitive full-name match against active users:

- Exactly one match → resolved.
- Zero matches, multiple matches, or no name proposed → mark as "needs assignee" and resolve at the approval gate (step 8).

### 8. Approval gate (REQUIRED — no Linear writes before this)

Render a table to the user with one row per candidate:

| # | Status | Bullet (truncated to ~80 chars) | Proposed title | Assignee |
|---|---|---|---|---|

Where `Status` is one of:

- `will create` (action item, assignee resolved)
- `needs assignee` (action item, assignee unresolved or ambiguous)
- `already linked → <identifier>` (skip)
- `noise (skip)` (Claude classified as noise — user may override)

Ask the user to:

1. Confirm or override the classifications (include any "noise" they want as tickets; skip any "will create" they don't want).
2. Resolve every "needs assignee" row (pick a Linear user, or explicitly "unassigned").

Do NOT proceed to step 9 until the user has responded.

### 9. Create Linear tickets

For each item the user approved for creation, call `mcp__claude_ai_Linear__save_issue` with:

- `teamId` — the resolved team ID
- `cycleId` — the resolved cycle ID (OMITTED only if the user chose option (a) "create without cycle" in step 6)
- `title` — the proposed imperative title
- `description` — the FULL ORIGINAL bullet text (including sub-bullets, verbatim), followed by:

  ```
  ---
  Source: [<doc title>](<full Outline doc URL>) — section "<matched heading>"
  ```

- `assigneeId` — the resolved Linear user ID, OR omitted if the user chose "unassigned"
- `state: "Todo"` — always create tickets in the Todo state, not in the team's default initial state.
- No `labelIds`, no `priority`, no `projectId`. Linear defaults for everything else.

Collect each successful response's `identifier` (e.g., `AISG-123`) and `url`.

If a single ticket creation fails, log the error and CONTINUE with the rest of the batch. Do not abort.

### 10. Write the links back into the Outline doc

Build an updated copy of the document's full markdown:

- For each SUCCESSFULLY created ticket, locate its original top-level bullet line and append ` → [<identifier>](<linear url>)` at the end of THAT line. Sub-bullets and other lines stay exactly as they were.
- Skipped candidates (already_linked, noise, user-skipped) are not modified.
- Failed-creation candidates are not modified.

Call `mcp__claude_ai_GetOutline__update_document` ONCE with `id` = the document ID and `text` = the new markdown.

If the writeback fails, do BOTH of the following:

1. Print all the would-be suffixes to the console in the format: `<original bullet> → <identifier> (<linear url>)`, one per line.
2. Save those same lines to `outline-to-linear-writeback-<ISO-timestamp>.md` in the project root.

This guarantees no information is lost even if the doc update fails; the user can paste manually, and a re-run is still safe because `already_linked` detection catches any identifier already in the doc.

### 11. Report

Print a final summary:

- **Created (N):** for each, `<identifier> <url> — <bullet text truncated>`
- **Skipped (M):** for each, `<bullet text truncated> — reason (already linked / noise / user-skipped)`
- **Failed (K):** for each, `<bullet text truncated> — <error message>`
- **Outline writeback:** success / failure (with fallback file path if failed)

## Failure handling reference

| Failure | Behavior |
|---|---|
| Outline `fetch` fails | Stop. No state changed. Report the error. |
| No matching action-items heading | Stop. Show user the headings that DO exist. |
| No active cycle on the team | Ask user: (a) no cycle, (b) pick a cycle, (c) abort. |
| Ambiguous / missing assignee | Resolve at the approval gate (step 8), batched. |
| Single Linear ticket creation fails | Log, continue. Report at end. |
| Outline writeback fails | Print suffixes + save to fallback file. |
| User aborts at approval gate | No tickets created, no doc changes. Clean exit. |

## Important rules

- **No Linear writes before the approval gate.** Always render the table and wait for confirmation.
- **One Outline write only.** All link-backs go in a single `update_document` call.
- **Idempotent re-runs.** Trust the `already_linked` skip signal; do not try to dedupe by ticket title.
- **Linear defaults for everything except** team, cycle, title, description, assignee, and state (always `Todo`).
