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
