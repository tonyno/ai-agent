# Design: Outline Local Index + /pull-outline-index Skill

> **Date:** 2026-04-16 | **Author:** Tonda Kmoch | **Status:** Draft

## Problem

This workspace uses Outline as the source of truth for all documentation (DMT topics, methodology, eventually project collections). Claude Code needs to know *what documents exist* in Outline to make smart decisions about when to fetch content via MCP — without fetching everything every conversation.

## Solution

Three components:

1. **`outline-index.md`** — A local index file mapping tracked collections to their documents with rich summaries
2. **`/pull-outline-index` skill** — A Claude Code skill that pulls document metadata from Outline via MCP and regenerates the local index
3. **CLAUDE.md update** — Points Claude to the index and explains the workflow

## Component 1: `outline-index.md`

Location: `/Users/tondakmoch/Documents/GIT.work/dmt-tonda/outline-index.md` (workspace root)

### Format

```markdown
# Outline Index

> **Last pulled:** YYYY-MM-DDTHH:MM:SS
> **Pull method:** /pull-outline-index skill via MCP (GetOutline)

## Tracked Collections

| Collection | Collection ID | URL | Purpose |
|---|---|---|---|
| OAK'S LAB | `ed48f77b-51de-405d-bf34-a4baedf5bda1` | https://oakslab.getoutline.com/collection/oaks-lab-eDPUjDbhSB | Company-wide DMT topics, AI-first operations |
| The OAK'S LAB WAY | `bcc3903f-82d2-4e2a-a7ba-48a7d454d200` | https://oakslab.getoutline.com/collection/the-oaks-lab-way-jYXeZKKxiP | Product development methodology (100 docs) |

---

## Collection: OAK'S LAB

> 4 documents | Last pulled: YYYY-MM-DDTHH:MM:SS

| Document | ID | Rev | Summary |
|---|---|---|---|
| DMT Vision: AI-First Operations | `f2f045c4-...` | 4 | Strategic framing doc. Why AI-first now, human-to-AI workflow shift, OAK'S LAB WAY evolution from docs to skills, three pillars (Outline hub, Meeting Intelligence, AI Architecture). For DMT alignment. |
| ... | ... | ... | ... |

## Collection: The OAK'S LAB WAY

> 100 documents (15 indexed, 85 sub-documents) | Last pulled: YYYY-MM-DDTHH:MM:SS

| Document | ID | Rev | Summary |
|---|---|---|---|
| The OAK'S LAB WAY | `4a9e498c-...` | 3 | Root document. Methodology intro, structure (Roles, Activities, Tools, Health Check), process diagram. Designed for startups, concept to PMF. |
| ... | ... | ... | ... |

> **85 sub-documents** exist under Activities, Roles & Responsibilities, and Tools.
> Use MCP `list_documents` with collectionId `bcc3903f-...` to browse the full list.
```

### Key design decisions

- **Rev column** tracks the Outline revision number. During pull, if the revision hasn't changed, the existing summary is preserved (no need to re-fetch and re-summarize).
- **Summary column** is 1-3 sentences describing what the document covers, what decisions/options it contains, and its purpose. Rich enough to decide whether to fetch the full content.
- **Large collections** (like The OAK'S LAB WAY with 100 docs) index only top-level/structural documents (~10-15) with a note about how many sub-documents exist and how to access them.
- **Adding a collection** is manual: user edits the Tracked Collections table and runs /pull-outline-index.

## Component 2: `/pull-outline-index` Skill

Location: `.claude/skills/pull-outline-index.md` (workspace-level skill)

### Skill behavior

When invoked:

1. **Read** `outline-index.md` to get the list of tracked collections (IDs from the Tracked Collections table)
2. **For each collection**, call `mcp__claude_ai_GetOutline__list_documents` with the collection ID
3. **For each document** in the response:
   - If the document's revision matches the existing index entry → keep the existing summary
   - If the document is new or has a higher revision → fetch the document via `mcp__claude_ai_GetOutline__fetch` and write a new 1-3 sentence summary
   - For large collections (50+ docs): only index documents with `parentDocumentId: null` or those that are direct children of the root. Note the total count and sub-document count.
4. **Regenerate** `outline-index.md` with:
   - Updated "Last pulled" timestamp
   - Updated per-collection document tables
   - Preserved tracked collections config (user-managed)
5. **Report** what changed: new documents, updated documents, removed documents

### Skill file content

The skill markdown will contain:
- Name: `pull-outline-index`
- Description: Pulls document metadata from tracked Outline collections via MCP and regenerates the local index
- Trigger: User runs `/pull-outline-index`
- Full step-by-step instructions for the pull process
- Rules for summary writing (1-3 sentences, focus on topics covered, decisions contained, and document purpose)
- Rules for large collections (index structural docs only, note sub-document count)

## Component 3: CLAUDE.md Update

Add this section to CLAUDE.md:

```markdown
## Outline Integration

This workspace uses Outline as the source of truth for all documentation.
Local file `outline-index.md` is an index of tracked collections and their documents.

**Rules:**
- Always read `outline-index.md` at the start of a conversation to know what's available
- Content always comes from Outline via MCP — never cache document content locally
- Use the index summaries to decide which documents to fetch for the current task
- To refresh the index: run `/pull-outline-index`
- To track a new collection: add it to the Tracked Collections table in `outline-index.md`, then run `/pull-outline-index`
- To fetch a document: use `mcp__claude_ai_GetOutline__fetch` with the document ID from the index
```

## Files to Create/Modify

| File | Action |
|---|---|
| `outline-index.md` | Create — initial index with 2 tracked collections, populated via first sync |
| `.claude/skills/pull-outline-index.md` | Create — the skill definition |
| `CLAUDE.md` | Modify — add Outline Integration section |

## Verification

1. Run `/pull-outline-index` after implementation
2. Verify `outline-index.md` contains correct documents for both collections
3. Verify summaries are meaningful (can you decide whether to fetch a doc based on the summary alone?)
4. Verify revision tracking works: run `/pull-outline-index` again, confirm unchanged docs keep their summaries
5. Test adding a new collection: add a row to Tracked Collections, run `/pull-outline-index`, verify it appears
