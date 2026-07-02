# outline-to-linear Skill Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship a Claude Code skill at `.claude/skills/outline-to-linear/` that turns the "Next steps" bullets of an Outline meeting note into Linear tickets in a user-specified team's current cycle, and writes the resulting issue links back into the Outline doc.

**Architecture:** Single-skill, single-flow. Two procedural markdown files — `SKILL.md` (the procedure Claude follows) and `README.md` (human-facing). Skill consumes two URLs, fetches the Outline doc via the GetOutline MCP, uses LLM judgment to classify bullets, gates on user approval, then writes via the Linear MCP (`save_issue`) and one Outline MCP write (`update_document`). No code outside the markdown files; the "implementation" is the procedure that Claude follows at runtime.

**Tech Stack:** Markdown (skill authoring), GetOutline MCP (`fetch`, `update_document`), Linear MCP (`list_teams`, `list_cycles`, `list_users`, `save_issue`).

**Reference spec:** `docs/superpowers/specs/2026-05-13-outline-to-linear-design.md`

---

## File Structure

| Path | Action | Responsibility |
|---|---|---|
| `.claude/skills/outline-to-linear/SKILL.md` | Create | The procedure Claude follows when the skill is invoked. Frontmatter + numbered steps. Single source of behavior. |
| `.claude/skills/outline-to-linear/README.md` | Create | Human-facing description: what it does, how to invoke, prerequisites, examples. |
| `.claude/README.md` | Modify | Add the new skill to the "Skills" table so it shows up alongside the existing two. |

No other files change. No code, no tests-as-code, no dependencies to install.

---

## Verification approach

Because the artifact is a procedural prompt (not code), TDD becomes:

1. **Define the observable behaviors up front** (Task 1) — a flat checklist of "given/when/then" scenarios that the skill must satisfy.
2. **Author SKILL.md to satisfy them** (Task 2).
3. **Verify by walkthrough** (Task 3) — read the SKILL.md and tick off the behaviors.
4. **Author README.md** (Task 4).
5. **Wire up the discovery surfaces** (Task 5) — `.claude/README.md`.
6. **End-to-end smoke test** (Task 6) — invoke the new skill against the real Outline doc the user already has (`https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-VMvYSEJT43`) and the team `https://linear.app/oakslab/team/AISG/active` and confirm tickets get created and the doc is updated.

Each task ends with a commit so progress is recoverable.

---

## Task 1: Define observable behaviors

**Files:**
- Create: `.claude/skills/outline-to-linear/.behaviors.md` (working file, will be deleted at end of Task 3)

This is the "failing test": a checklist of every behavior the SKILL.md must produce. We write it first so Task 3 has something concrete to verify against.

- [ ] **Step 1: Create the behaviors file**

Write `.claude/skills/outline-to-linear/.behaviors.md` with the following content verbatim:

```markdown
# outline-to-linear — Observable Behaviors

These are the testable behaviors the skill must produce. Tick each off after reading SKILL.md.

## Input parsing
- [ ] B1. Given a user prompt containing an Outline doc URL like `…/doc/<slug>-<id>`, extracts `<id>` as the document ID (token after the LAST `-`).
- [ ] B2. Given a user prompt containing a Linear team URL like `…/team/<KEY>/…`, extracts `<KEY>` as the team key (case-insensitive).
- [ ] B3. If the Outline URL is missing, asks the user for it before doing anything else.
- [ ] B4. If the Linear team URL is missing, asks the user for it before doing anything else.

## Document fetch + section detection
- [ ] B5. Calls `mcp__claude_ai_GetOutline__fetch` with `resource: "document"` and the parsed ID.
- [ ] B6. Searches headings (any level) for the FIRST case-insensitive match of: "next steps", "action items", "action points", "follow-ups", "follow ups".
- [ ] B7. The section runs from that heading to the next heading of equal-or-higher level (or end of doc).
- [ ] B8. If no matching heading is found, stops and reports which headings DO exist.

## Bullet extraction
- [ ] B9. Collects only top-level bullets in the section. "Top-level" indentation = indentation of the FIRST bullet in the section.
- [ ] B10. Sub-bullets and continuation lines are kept WITH their parent bullet as one "candidate".

## Classification
- [ ] B11. Each candidate is classified `already_linked`, `action_item`, or `noise`.
- [ ] B12. `already_linked` = the parent bullet line contains either a `linear.app/...` URL OR an identifier matching `\[?[A-Z]{2,}-\d+\]?`.
- [ ] B13. Distinguishes `action_item` (commitment/directive) from `noise` (transcript prose) by LLM judgment.
- [ ] B14. For each `action_item`, attempts to parse a leading `[Name]` token OR a leading `Name:` segment as the proposed assignee.
- [ ] B15. For each `action_item`, generates a short imperative title (~60 chars).

## Linear resolution
- [ ] B16. Calls `mcp__claude_ai_Linear__list_teams` and finds the team by key (case-insensitive). Asks user if not found.
- [ ] B17. Calls `mcp__claude_ai_Linear__list_cycles` and picks the cycle where `startsAt <= now < endsAt`.
- [ ] B18. If no active cycle, asks the user to choose: (a) create without cycle, (b) pick a specific cycle, (c) abort. Does NOT silently fall back.
- [ ] B19. Calls `mcp__claude_ai_Linear__list_users` once. Case-insensitive full-name match. Single match → use; zero or multiple → batch-ask at the approval gate.

## Approval gate
- [ ] B20. Before any Linear write, shows a table with one row per candidate: # | Status | Bullet (truncated) | Proposed title | Assignee.
- [ ] B21. The user can reclassify items (include something marked noise, skip something marked action_item) and resolve ambiguous/missing assignees before proceeding.

## Ticket creation
- [ ] B22. Calls `mcp__claude_ai_Linear__save_issue` per approved item with: teamId, cycleId, title (AI-summarized), description (full bullet text + Outline backlink), assigneeId (or omitted).
- [ ] B23. Description backlink format: `\n\n---\nSource: [<doc title>](<full Outline URL>) — section "<matched heading>"`.
- [ ] B24. No labels, no priority, no Linear Project, no status overrides — Linear defaults for everything else.
- [ ] B25. If a single creation fails, logs and continues with the rest of the batch.

## Writeback
- [ ] B26. Builds an updated document text: for each successfully-created ticket, appends ` → [<identifier>](<linear url>)` to the END of that bullet's original parent line.
- [ ] B27. Untouched bullets (skipped / failed) are left exactly as they were.
- [ ] B28. Calls `mcp__claude_ai_GetOutline__update_document` ONCE with the new text.
- [ ] B29. If the writeback fails, writes the would-be suffixes to `outline-to-linear-writeback-<ISO-timestamp>.md` in the project root AND prints them to the console.

## Reporting
- [ ] B30. Final report includes: N created (identifier + URL + bullet), M skipped (with reason), K failures (bullet + error), Outline writeback success/failure.

## Idempotency
- [ ] B31. Re-running on the same doc after a successful run produces 0 new tickets (all bullets now have `linear.app` URLs / identifiers from B26).
```

- [ ] **Step 2: Verify the file was written**

Run: `wc -l /Users/tondakmoch/Documents/GIT.work/dmt-tonda/.claude/skills/outline-to-linear/.behaviors.md`
Expected: ~50 lines.

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/outline-to-linear/.behaviors.md
git commit -m "Add behavior checklist for outline-to-linear skill"
```

---

## Task 2: Write SKILL.md

**Files:**
- Create: `.claude/skills/outline-to-linear/SKILL.md`

- [ ] **Step 1: Write SKILL.md**

Write the file with exactly this content:

````markdown
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
- No `labelIds`, no `priority`, no `stateId`, no `projectId`. Linear defaults for everything else.

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
- **Linear defaults for everything except** team, cycle, title, description, and assignee.
````

- [ ] **Step 2: Verify the file was written correctly**

Run: `head -3 /Users/tondakmoch/Documents/GIT.work/dmt-tonda/.claude/skills/outline-to-linear/SKILL.md`
Expected output starts with `---` then `name: outline-to-linear`.

Run: `grep -c '^### ' /Users/tondakmoch/Documents/GIT.work/dmt-tonda/.claude/skills/outline-to-linear/SKILL.md`
Expected: `11` (one per numbered step).

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/outline-to-linear/SKILL.md
git commit -m "Add SKILL.md for outline-to-linear"
```

---

## Task 3: Walkthrough — verify SKILL.md covers all behaviors

**Files:**
- Read: `.claude/skills/outline-to-linear/SKILL.md`
- Read + tick off: `.claude/skills/outline-to-linear/.behaviors.md`
- Delete (at end): `.claude/skills/outline-to-linear/.behaviors.md`

- [ ] **Step 1: Read SKILL.md fully and tick each behavior in `.behaviors.md`**

Open `.behaviors.md` and SKILL.md side by side. For each of B1–B31, find the exact line(s) in SKILL.md that produce that behavior, and tick the box. If any behavior cannot be ticked, STOP — do not delete the behaviors file. Instead, go back to Task 2 and amend SKILL.md to cover the missing behavior, then re-run this step.

- [ ] **Step 2: Confirm zero unchecked boxes**

Run: `grep -c '^- \[ \]' /Users/tondakmoch/Documents/GIT.work/dmt-tonda/.claude/skills/outline-to-linear/.behaviors.md`
Expected: `0`.

If non-zero, return to Task 2 and fix SKILL.md.

- [ ] **Step 3: Delete the behaviors file**

```bash
rm /Users/tondakmoch/Documents/GIT.work/dmt-tonda/.claude/skills/outline-to-linear/.behaviors.md
```

- [ ] **Step 4: Commit**

```bash
git add -u .claude/skills/outline-to-linear/
git commit -m "Verify outline-to-linear SKILL.md against behavior checklist"
```

---

## Task 4: Write README.md

**Files:**
- Create: `.claude/skills/outline-to-linear/README.md`

- [ ] **Step 1: Write README.md**

Write the file with this content:

````markdown
# outline-to-linear

> Reads the "Next steps" section of an Outline meeting note and creates Linear tickets for each action item in a specified team's current cycle. Writes the resulting Linear links back into the Outline doc.

## Usage

```
/outline-to-linear <outline-doc-url> <linear-team-url>
```

Example:

```
/outline-to-linear https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-VMvYSEJT43 https://linear.app/oakslab/team/AISG/active
```

If you omit either URL, the skill will ask for it. You can also trigger it with natural language like "create Linear tickets from this Outline doc: <url> in team <team-url>".

## What it does

1. Fetches the Outline doc.
2. Finds the first heading matching "Next steps" / "Action items" / "Action points" / "Follow-ups".
3. Classifies each top-level bullet as `action_item`, `noise`, or `already_linked`.
4. Shows you a confirmation table — you can reclassify items and resolve any missing/ambiguous assignees.
5. Creates one Linear ticket per approved item in the team's CURRENT cycle, with the original bullet text and a backlink to the Outline doc in the description.
6. Writes ` → [AISG-123](https://linear.app/...)` next to each source bullet in the Outline doc (one update call).

## What gets skipped automatically

A bullet is skipped if it already has either of these on its line:

- a `linear.app/...` URL, or
- an issue identifier like `AISG-123` or `[AISG-123]`.

This makes re-runs safe — running the skill twice on the same doc produces zero duplicates.

## What it does NOT do

- No labels, priority, status, or Linear Project assignment — Linear defaults only.
- No two-way sync — Linear status changes are not pushed back to Outline.
- No multi-doc batch invocation.

## Prerequisites

- GetOutline MCP tools available (`mcp__claude_ai_GetOutline__fetch`, `mcp__claude_ai_GetOutline__update_document`)
- Linear MCP tools available (`list_teams`, `list_cycles`, `list_users`, `save_issue`)
- The Linear team must have an active cycle (or you'll be asked how to proceed)

## How it connects to other skills

- Independent of `/pull-outline-index` and `/oaks-outline-push`. No shared state.
- Each successful run mutates one Outline doc once — re-run safely.

## Audience

Anyone in the DMT who runs meetings and tracks follow-ups in Linear.
````

- [ ] **Step 2: Verify**

Run: `head -1 /Users/tondakmoch/Documents/GIT.work/dmt-tonda/.claude/skills/outline-to-linear/README.md`
Expected: `# outline-to-linear`

- [ ] **Step 3: Commit**

```bash
git add .claude/skills/outline-to-linear/README.md
git commit -m "Add README for outline-to-linear skill"
```

---

## Task 5: Update `.claude/README.md` skills table

**Files:**
- Modify: `.claude/README.md`

- [ ] **Step 1: Add a row to the Skills table**

Use Edit on `/Users/tondakmoch/Documents/GIT.work/dmt-tonda/.claude/README.md`.

old_string:
```
| [oaks-outline-push](skills/oaks-outline-push/) | One-way push of `.claude/` config to Outline AI Skills Library for human browsing | Active |
| [pull-outline-index](skills/pull-outline-index/) | Pulls document metadata from Outline collections to regenerate the local `outline-index.md` | Active |
```

new_string:
```
| [oaks-outline-push](skills/oaks-outline-push/) | One-way push of `.claude/` config to Outline AI Skills Library for human browsing | Active |
| [outline-to-linear](skills/outline-to-linear/) | Turns the Next-steps section of an Outline meeting doc into Linear tickets in the team's current cycle, with links written back to Outline | Active |
| [pull-outline-index](skills/pull-outline-index/) | Pulls document metadata from Outline collections to regenerate the local `outline-index.md` | Active |
```

- [ ] **Step 2: Verify the edit**

Run: `grep -c outline-to-linear /Users/tondakmoch/Documents/GIT.work/dmt-tonda/.claude/README.md`
Expected: `1`

- [ ] **Step 3: Commit**

```bash
git add .claude/README.md
git commit -m "List outline-to-linear in .claude/README.md skills table"
```

---

## Task 6: End-to-end smoke test

This is a live, idempotent test against real services. The user supplied a real Outline doc URL and Linear team URL during brainstorming; we use those.

**Inputs:**
- Outline doc: `https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-VMvYSEJT43`
- Linear team: `https://linear.app/oakslab/team/AISG/active`

**Files:**
- Read: `/Users/tondakmoch/Documents/GIT.work/dmt-tonda/2026-04-28_ai-dmt-sync.md` (local copy of a similar meeting note — useful for pre-checking the parsing rules without writing anywhere)

- [ ] **Step 1: Pre-flight dry parse against the LOCAL meeting note**

Read `/Users/tondakmoch/Documents/GIT.work/dmt-tonda/2026-04-28_ai-dmt-sync.md` and manually apply steps 3–5 of SKILL.md to it (locate section, extract bullets, classify). Confirm the classification table looks sensible (action items separated from transcript excerpts). This catches gross errors in SKILL.md before any MCP call.

- [ ] **Step 2: Pause for user confirmation**

Ask the user: "Pre-flight dry parse looks good. Ready to do a real run against the Outline doc `2026-05-12-ai-dmt-sync` and create tickets in team AISG's current cycle?"

If yes, continue. If no, stop and report.

- [ ] **Step 3: Invoke the skill**

In the running Claude Code session, run:

```
/outline-to-linear https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-VMvYSEJT43 https://linear.app/oakslab/team/AISG/active
```

Expected behavior:

1. Skill fetches the doc.
2. Renders the approval-gate table.
3. Asks any disambiguation questions.
4. Creates the approved tickets.
5. Updates the Outline doc.
6. Prints the final report.

- [ ] **Step 4: Verify the tickets exist in Linear**

For each `identifier` in the report, open its `url`. Confirm:

- It's in team AISG.
- Its cycle is the currently-active one.
- Title is a sensible imperative summary.
- Description contains the original bullet text and a backlink to the Outline doc.
- Assignee matches the approval-gate selection.

- [ ] **Step 5: Verify the Outline doc was updated**

Refetch the doc via `mcp__claude_ai_GetOutline__fetch` and confirm each created ticket's source bullet now ends with ` → [<identifier>](<linear url>)`.

- [ ] **Step 6: Verify idempotency — run the skill again**

Run the same command again:

```
/outline-to-linear https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-VMvYSEJT43 https://linear.app/oakslab/team/AISG/active
```

Expected: the approval table shows every previously-created item as `already linked → <identifier>` (skip). `Created` count in the final report should be `0` (unless new action items have been added to the doc since).

- [ ] **Step 7: No commit needed**

This task verifies the deployed skill end-to-end; it doesn't modify any tracked files. The Outline doc and Linear tickets are the artifacts. Mark the task done.

---

## Self-review notes

- **Spec coverage:** All 11 procedural steps in the spec map to numbered steps in SKILL.md (Task 2). All 8 failure modes in the spec are reflected in the "Failure handling reference" table in SKILL.md. The behaviors checklist in Task 1 enumerates the spec's expectations explicitly.
- **Placeholders:** None. Every step contains the actual content (file paths, URLs, exact commands, exact code/text blocks).
- **Type/name consistency:** The MCP tool names used here (`mcp__claude_ai_GetOutline__fetch`, `mcp__claude_ai_GetOutline__update_document`, `mcp__claude_ai_Linear__list_teams`, `mcp__claude_ai_Linear__list_cycles`, `mcp__claude_ai_Linear__list_users`, `mcp__claude_ai_Linear__save_issue`) match the names listed in the deferred-tools list at session start.
- **No code-as-test gap:** The skill is markdown only, so traditional unit tests don't apply. Task 1 (behavior checklist), Task 3 (walkthrough) and Task 6 (live smoke test) substitute for that, in the same TDD spirit: define-then-verify.
