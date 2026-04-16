# pull-outline-index

> Pulls document metadata from tracked Outline collections via MCP and regenerates the local outline-index.md file.

## Usage

```
/pull-outline-index
```

## What It Does

1. Reads `outline-index.md` to find tracked collections and their IDs
2. Pulls document metadata (titles, IDs, revisions) from each collection via MCP
3. For new or updated documents, fetches content and generates a 1-3 sentence summary
4. Regenerates `outline-index.md` with updated document tables
5. Reports what's new, updated, or removed

## Prerequisites

- MCP GetOutline tools must be available
- `outline-index.md` must exist with at least one tracked collection

## How it connects to other skills

- Run **before** any task that needs to know what documents exist in Outline
- The generated `outline-index.md` is read by Claude at conversation start (per CLAUDE.md instructions)
- Independent of `/oaks-outline-push` (which pushes .claude/ config to Outline)

## Audience

All team members who use Outline as a knowledge source for AI-assisted work.