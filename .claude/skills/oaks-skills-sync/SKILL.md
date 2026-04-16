---
name: oaks-skills-sync
description: Pushes the project's .claude/ config to Outline AI Skills Library and pulls common skills. Run this to share your AI setup and get the latest common skills. Self-updates on every run.
---

# Oaks Skills Sync

Synchronizes this project's Claude Code configuration with the Oaks Lab AI Skills Library in Outline. Pushes project config up, pulls common skills down, and self-updates.

## Prerequisites

- MCP GetOutline tools must be available
- Project must be a git repository with a remote (used to derive project name)

## Steps

### 1. Identify the project

Read the git remote URL to derive the project name:
- Run `git remote get-url origin`
- Extract the repo name (e.g., `git@github.com:oakslab/olh-monorepo.git` → `olh-monorepo`)
- This becomes the project's folder name in Outline

### 2. Find the AI Skills Library in Outline

The AI Skills Library is a document in the OAK'S LAB collection:
- Parent document ID: `4bc544a3-9f7f-4af7-add5-f2b4e29a481b` (AI Skills Library)
- Common folder document ID: `8643fbbc-4869-412d-8f84-c145a8f1cefc` (common)

Use `mcp__claude_ai_GetOutline__list_documents` to find the project's folder under the AI Skills Library. If it doesn't exist, create it.

### 3. Self-update

Before doing anything else, check if a newer version of this skill exists in Outline:
- Fetch `common / skills / oaks-skills-sync` from Outline
- Compare with the local file at `.claude/skills/oaks-skills-sync/SKILL.md`
- If Outline version is different, overwrite the local file silently
- Also check for supporting files (e.g., `templates/skill-readme.md`) and update if needed

### 4. Push: Upload project config to Outline

Scan the `.claude/` directory and upload everything to Outline under `AI Skills Library / [project-name] /`:

**What to scan:**
- `.claude/skills/*/SKILL.md` (folder-based skills — use the folder name as the skill name)
- `.claude/skills/*.md` (legacy flat skill files — use the file name without extension)
- `.claude/commands/*/SKILL.md` and `.claude/commands/*.md` (same pattern as skills)
- `.claude/CLAUDE.md` or `CLAUDE.md` at workspace root
- `.claude/settings.json` (upload as a code-block document)

**What to skip:**
- `.claude/skills/common/` — this is pulled content, never push it back
- `.claude/memory/` — private, never share
- `.claude/plans/` — ephemeral, not useful to share
- `.claude/projects/` — project-scoped Claude config, may contain private memory
- `README.md` files inside skill folders — these are auto-generated, not source content
- `templates/` directories inside skill folders — these are supporting files managed by the skill itself

**How to upload:**
- Mirror the folder structure as nested Outline documents
- For each skill: if a document with the same title exists under the project folder, update it. Otherwise, create it.
- Use the skill folder name as the document title
- Upload the SKILL.md content as the document body

### 5. Generate per-skill README files

For each skill folder that does NOT already have a `README.md`:

1. Read the README template from `.claude/skills/oaks-skills-sync/templates/skill-readme.md`
   (or fetch from Outline if not locally available)
2. Read the skill's `SKILL.md` to extract: name, description, steps/what it does, prerequisites
3. Fill in the template with the extracted information
4. Present the generated README to the user for review: "I've generated a README for [skill-name]. Please review:"
5. After user confirms (or edits), write it to the skill's folder as `README.md`

For each skill, also upload the README content to Outline as the body of the skill's document (appended after the SKILL.md content under a `---` separator). This makes each skill self-documenting in Outline.

### 6. Pull: Download common skills

Fetch all documents under `AI Skills Library / common /` from Outline:

1. List all documents with `parentDocumentId` = `8643fbbc-4869-412d-8f84-c145a8f1cefc` (common folder)
2. For documents under `common / skills /`: download to `.claude/skills/common/[name]/SKILL.md`
3. For documents under `common / commands /`: download to `.claude/commands/common/[name]/SKILL.md`
4. Create the directories if they don't exist
5. Overwrite existing files — common folder is Outline-authoritative

### 7. Report

After completion, report to the user:
- Project name identified
- Number of skills/commands pushed to Outline
- Whether per-skill READMEs were generated or updated
- Number of common skills pulled
- Whether self-update occurred
- Link to the project's folder in Outline

## Important Rules

- **Never push `.claude/skills/common/`** — this is pulled content
- **Never push `.claude/memory/`** — private data
- **Never push `.claude/plans/`** — ephemeral
- **Never push `.claude/projects/`** — may contain private memory
- **Self-update is silent** — don't ask the user, just replace
- **README generation requires user review** — always show before writing
- **Use `editMode: "replace"` for updates** — skill content should be fully replaced, not patched
- **Derive project name from git remote** — don't ask the user
- **Prefer folder-based skills** — when encountering legacy flat `.md` files, still handle them but the canonical format is `skill-name/SKILL.md`
