---
name: pull-outline-index
description: Pulls document metadata from tracked Outline collections via MCP and regenerates the local outline-index.md file. Use when user wants to refresh the local index of what exists in Outline.
---

# Pull Outline Index

Regenerate the local `outline-index.md` by pulling document metadata from all tracked Outline collections via MCP. This is a one-way pull — Outline is the source of truth, the local file is an index for awareness only.

## Steps

### 1. Read the current index

Read `outline-index.md` from the workspace root. Parse the **Tracked Collections** table to get collection names, IDs, URLs, and purposes. If the file doesn't exist, stop and tell the user to create it with at least one tracked collection.

Also parse the existing per-collection document tables to get current document IDs, revisions, and summaries. These will be used for revision comparison.

### 2. Pull documents for each collection

For each tracked collection, call `mcp__claude_ai_GetOutline__list_documents` with the collection ID and `limit: 100`.

If the result is too large (overflows to a file), use a subagent to parse the JSON and extract: document title, ID, revision, parentDocumentId, and language.

### 3. Determine which documents to index

**Small collections (under 50 documents):**
- Index ALL documents with full summaries

**Large collections (50+ documents):**
- Index only **top-level documents** (`parentDocumentId: null`) and **direct children of top-level documents** that serve as structural category pages
- Count the total number of documents and the number of sub-documents not indexed
- Add a note at the bottom: "> **N sub-documents** exist under [parent names]. Use MCP `list_documents` with collectionId `xxx` to browse the full list."

### 4. Generate summaries

For each document to be indexed:
- **If the document ID exists in the current index AND the revision matches** → keep the existing summary (no MCP fetch needed)
- **If the document is new or has a higher revision** → fetch via `mcp__claude_ai_GetOutline__fetch` using the document ID, then write a summary

**Summary rules:**
- 1-3 sentences
- Describe what topics the document covers
- Mention key decisions, options, or proposals it contains
- State the document's purpose (e.g., "For DMT alignment", "Methodology reference", "Operational checklist")
- Be specific enough that someone can decide whether they need to read the full document

### 5. Regenerate outline-index.md

Write the updated `outline-index.md` with:
- **Header** with "Last pulled" timestamp (ISO 8601, current time)
- **Tracked Collections** table — preserved exactly as the user configured it (do not modify)
- **Per-collection sections** — one section per tracked collection with:
  - Collection name as heading
  - Document count and "Last pulled" timestamp
  - Document table with columns: Document | ID | Rev | Summary
  - For large collections: sub-document count note at the bottom

### 6. Report changes

After regenerating, report to the user:
- How many documents were found per collection
- Which documents are **new** (not in the previous index)
- Which documents were **updated** (higher revision)
- Which documents were **removed** (in old index but not in Outline anymore)
- Total time taken

## Important Rules

- **Never cache document content locally** — only titles, IDs, revisions, and summaries
- **Preserve the Tracked Collections table** — the user manages it manually
- **Use parallel MCP calls** where possible (e.g., fetch multiple collections simultaneously)
- **If MCP fails for a collection**, report the error but continue with other collections
- **Full document IDs** in the index — no truncation (they're needed for MCP fetch calls)
