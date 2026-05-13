# outline-to-linear — Design Spec

**Date:** 2026-05-13
**Author:** Tonda Kmoch (with Claude)
**Status:** Draft, awaiting review

## Summary

A Claude Code skill that reads the "Next steps" (or similarly named) section of a meeting note in Outline, creates a Linear ticket for each action item in a user-specified Linear team's current cycle, and writes the new Linear issue links back into the Outline document next to each item. Items that already have a Linear link or issue identifier on their bullet line are skipped, making re-runs idempotent.

## Goal

Turn manually-taken meeting follow-ups into tracked Linear work without context switching, while keeping the Outline doc as the canonical record of what was decided.

## Non-goals

- Two-way sync between Outline and Linear (status, comments, etc.).
- Parsing meeting transcripts that are NOT formatted as bulleted "Next steps" lists.
- Creating Linear Projects, labels, or workflow states.
- Replacing fields on existing Linear tickets if found.

## Inputs

| Input | Required | How obtained | Example |
|---|---|---|---|
| Outline document URL | Yes | Slash command argument, or asked if missing | `https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-VMvYSEJT43` |
| Linear team URL | Yes | Slash command argument, or asked if missing | `https://linear.app/oakslab/team/AISG/active` |

The Outline document ID is the trailing token after the last `-` in the doc URL path (e.g., `VMvYSEJT43`). The Linear team key is the `team/<KEY>/...` segment (e.g., `AISG`).

## Invocation

- Primary: `/outline-to-linear <outline-url> <linear-team-url>`
- If either argument is missing, the skill asks for it before proceeding.
- Natural-language prompts that match the skill description (e.g., "create Linear tickets from this Outline doc") also activate it.

## Skill file layout

Created at `.claude/skills/outline-to-linear/`, matching the existing skill convention used by `pull-outline-index` and `oaks-outline-push`:

```
.claude/skills/outline-to-linear/
├── SKILL.md     — frontmatter + procedural steps Claude follows
└── README.md    — short user-facing description and examples
```

`SKILL.md` frontmatter:

```yaml
name: outline-to-linear
description: Reads the "Next steps" (or similar) section of an Outline meeting doc and creates Linear tickets for each action item in a user-specified team's current cycle. Skips items that already have a Linear link or issue ID. Writes the ticket links back into the Outline doc. Use when user says "/outline-to-linear", or asks to "create Linear tickets from this Outline doc", "turn next steps into Linear tickets", etc.
```

## Procedural flow

### 1. Parse inputs

- Extract the Outline document ID from the URL path (segment after the last `-`).
- Extract the Linear team key from the team URL (`team/<KEY>/...`).
- If either is missing, prompt the user with a focused question.

### 2. Fetch the Outline document

Call `mcp__claude_ai_GetOutline__fetch` with `resource: "document"` and the parsed document ID. Keep the full markdown `text`, the document `id`, `urlId`, and `title`.

### 3. Locate the action-items section

Scan the document for the first heading (any level) whose text — case-insensitive, whitespace-normalized — matches any of:

- "next steps"
- "action items"
- "action points"
- "follow-ups" / "follow ups"

The section spans from that heading down to the next heading of equal or higher level (or end of document). If no heading matches, stop and report this to the user.

### 4. Extract candidate bullets

Within the matched section, collect only top-level bullets. A bullet line is identified by a leading `-`, `*`, or `+` (optionally preceded by spaces). The "top-level" indentation is defined as the indentation of the **first** bullet line found inside the section; any bullet line at exactly that indentation is a candidate, and any bullet line indented further is treated as a sub-bullet of the most recent top-level bullet above it. Each top-level bullet, together with its sub-bullets and any non-bullet continuation lines that follow before the next top-level bullet, is one "candidate".

### 5. Classify candidates

For each candidate, classify as:

- **`already_linked`** — the bullet line contains either:
  - a `linear.app/...` URL, or
  - an issue identifier matching `\[?[A-Z]{2,}-\d+\]?` (e.g., `AISG-123`, `[AISG-123]`).
- **`action_item`** — Claude judges it to be an actual action point (an assignment, commitment, or directive).
- **`noise`** — transcript excerpts, prose, or general discussion that happen to land in the section as bullets.

For `action_item` candidates:

- Pull a likely assignee name from a leading `[Name]` token or a leading `Name:` segment, if present.
- Generate a proposed short imperative title (~60 chars) summarizing the action.

### 6. Resolve Linear team and cycle

- Call `mcp__claude_ai_Linear__list_teams`. Find the team where `key` equals the parsed team key (case-insensitive). If not found, ask the user.
- Call `mcp__claude_ai_Linear__list_cycles` for that team. Pick the cycle where `startsAt <= now < endsAt` (the active one).
- If no active cycle exists, ask the user how to proceed: (a) create without a cycle, (b) pick a specific cycle from the list, (c) abort. Do not silently fall back — the user explicitly required current-cycle placement.

### 7. Resolve assignees

- Call `mcp__claude_ai_Linear__list_users` once for the workspace.
- For each `action_item`, attempt a case-insensitive full-name match against active users. Exactly one match → use it. Zero or multiple matches, or no name parsed → mark for batch disambiguation in step 8.

### 8. Approval gate

Render a table to the user with one row per candidate:

| # | Status | Bullet (truncated to ~80 chars) | Proposed title | Assignee |
|---|---|---|---|---|

`Status` is one of: `will create`, `already linked → <identifier>`, `noise (skip)`, `needs assignee`.

Ask the user:

- Any items to reclassify? (Force-include something marked noise, or skip something marked action item.)
- For each `needs assignee` row, who should it be assigned to? (Or "unassigned".)

Wait for confirmation before any Linear write.

### 9. Create Linear tickets

For each item the user approved for creation, call `mcp__claude_ai_Linear__save_issue` with:

- `teamId` — the resolved team
- `cycleId` — the resolved cycle (omitted only if the user chose option (a) under "no active cycle")
- `title` — the AI-summarized short imperative
- `description` — the full original bullet text (including any sub-bullets, verbatim), followed by:
  ```
  ---
  Source: [<doc title>](<full Outline doc URL>) — section "<matched heading>"
  ```
- `assigneeId` — resolved Linear user, or omitted if the user chose unassigned
- All other fields: Linear defaults

Collect each new issue's `identifier` (e.g., `AISG-123`) and `url`.

If a single ticket creation fails, log the failure and continue with the rest. Do not abort the batch.

### 10. Write the links back into Outline

Build an updated copy of the document's markdown:

- For each successfully created ticket, locate its original bullet line and append ` → [<identifier>](<linear url>)` at the end of that line. The bullet's existing text and any sub-bullets are otherwise untouched.
- Items that were skipped (`already_linked`, `noise`, user-skipped) are not modified.
- Items where ticket creation failed are not modified.

Call `mcp__claude_ai_GetOutline__update_document` once with the new text and the document ID, in a single update.

### 11. Report

Print a summary including:

- N tickets created — with identifier, URL, and which bullet
- M items skipped — with reason (already linked / classified noise / user-skipped)
- K failures — with the bullet text and the error message
- Whether the Outline writeback succeeded

## Failure handling

| Failure mode | Behavior |
|---|---|
| Outline `fetch` fails | Stop. No state changed. Surface the error. |
| No matching action-items heading | Stop. Report headings found, ask user how to proceed. |
| No active cycle on the team | Ask user: (a) create without cycle, (b) pick specific cycle, (c) abort. |
| Ambiguous / missing assignee | Batch-ask in the approval gate (step 8), not per-ticket. |
| Single Linear ticket creation fails | Log, continue with the batch. Report at the end. |
| Outline writeback fails after tickets created | Print the would-be suffixes to console AND save them to `outline-to-linear-writeback-<ISO-timestamp>.md` in the project root so the user can paste manually. Re-running the skill is also safe — the `already_linked` skip signal will catch tickets that already exist if their identifier somehow made it into the doc. |
| User aborts at approval gate | No tickets created, no doc changes. Clean exit. |

## Idempotency

Re-running the skill on the same document is safe:

- The `already_linked` detection (Linear URL or `[A-Z]{2,}-\d+` identifier on the bullet line) catches every bullet that was processed in a previous run, because step 10 always appends one of those.
- The classification + approval gate (step 8) means duplicate creation requires explicit user confirmation.

## Open questions (resolved during clarifying)

- **Should we also link tickets to a Linear Project?** No. User confirmed Linear defaults only; team + current cycle is the scope.
- **Should the skill set labels, priority, or status?** No. Linear defaults only.
- **What does "current cycle" mean if none is active?** The user did not pre-decide; the skill asks at runtime (see step 6).

## Out of scope for this spec

- Configuring a default Linear team to skip the team-URL argument.
- Bulk-running across multiple Outline docs in one invocation.
- Updating an existing Linear ticket if the action-item bullet's wording changes.
- Syncing Linear status changes back into the Outline doc.

Any of these may be addressed in a follow-up spec.
