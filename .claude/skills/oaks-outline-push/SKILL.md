---
name: oaks-outline-push
description: One-way push of the project's .claude/ config to Outline AI Skills Library for human browsing. Auto-generates README per skill and a project signpost.
---

# Oaks Outline Push

One-way push of the project's `.claude/` configuration to Outline for human-readable browsing. No pull, no self-update.

## Prerequisites

- MCP GetOutline tools must be available
- Project must be a git repository with a remote

## Steps

### 1. Identify the project

- Run `git remote get-url origin`
- Extract the repo name (e.g., `git@github.com:oakslab/olh-monorepo.git` → `olh-monorepo`)

### 2. Find or create the project folder in Outline

- AI Skills Library document ID: `4bc544a3-9f7f-4af7-add5-f2b4e29a481b`
- Use `mcp__claude_ai_GetOutline__list_documents` with `parentDocumentId` to find existing project folder
- If not found, create it with `mcp__claude_ai_GetOutline__create_document`

### 3. Scan `.claude/` directory

Collect everything to upload:

**Skills:** `.claude/skills/*/SKILL.md` (folder-based) and `.claude/skills/*.md` (legacy flat files)
**Commands:** `.claude/commands/*/SKILL.md` and `.claude/commands/*.md`
**Config:** `CLAUDE.md` (check `.claude/CLAUDE.md` first, then workspace root), `.claude/settings.json`

**Skip these — never upload:**
- `.claude/skills/common/` — pulled content

- `.claude/memory/` — private
- `.claude/plans/` — ephemeral
- `.claude/projects/` — may contain private memory
- `templates/` directories inside skill folders
- `README.md` files inside skill folders (these get merged into the skill document, not uploaded separately)

### 4. Generate per-skill README.md (if missing)

For each skill folder that does NOT have a `README.md`:

1. Read the skill's `SKILL.md`
2. Read the README template from `.claude/skills/oaks-outline-push/templates/skill-readme.md`
3. Auto-generate a README by filling the **upper, AI-safe sections only**: name, description, usage, what it does (steps summary), prerequisites, how it connects, audience
4. **Leave the human-only sections untouched** — the template ships with `TODO` placeholders under *When to use it / Why this skill exists / Impact / Tips & gotchas*. Never fill these from model inference; they must be authored by someone who has actually run the skill on a real project (per Andy's 2026-04-17 DMT feedback).
5. Write it to the skill's folder as `README.md`

If generation fails, write a placeholder:
```markdown
# [skill-name]

> README not yet documented. Please describe what this skill does.
```

If `README.md` already exists, skip it.

### 5. Generate root `.claude/README.md` (if missing)

If `.claude/README.md` does NOT exist, auto-generate a project signpost:

1. Read the project README template from `.claude/skills/oaks-outline-push/templates/project-readme.md`
2. Auto-fill the **upper, AI-safe sections**:
   - Project name (from git remote) and a brief description of the project's AI setup
   - `CLAUDE.md` and `settings.json` presence
   - **Table of all skills** (name → link, description from frontmatter or first paragraph)
   - **Table of all commands** (if any — omit the section otherwise)
   - Any visible flow or sequence between skills, or "Skills are independent — run as needed."
3. **Leave the human-only sections untouched** — *When this setup helps / Why this setup exists / Impact / Tips & gotchas* ship with `TODO`. Do not fill them from inference.
4. Write the file to `.claude/README.md`.

If `.claude/README.md` already exists, skip it — use as-is.

### 6. Upload to Outline

Upload in this order:

**6a. Root document (project signpost):**
- Title: the project name (from step 1)
- Content: the `.claude/README.md` content
- Parent: AI Skills Library document (`4bc544a3-9f7f-4af7-add5-f2b4e29a481b`)
- If a document with this title already exists under the parent, update it with `editMode: "replace"`

**6b. Per-skill documents:**
For each skill, create one merged document:
- Title: the skill name (folder name or filename without extension)
- Content: README.md content, then `---`, then the full SKILL.md content (including frontmatter — it will look broken in Outline but that's fine, it's for reference only)
- Parent: the project's root document from step 6a
- If exists, update with `editMode: "replace"`

**6c. Config documents:**
- `CLAUDE.md` — title: "CLAUDE.md", content: uploaded as-is, parent: project root
- `settings.json` — title: "settings.json", content: wrapped in a json code block, parent: project root

### 7. Report

Tell the user:
- Project name identified
- Number of skills uploaded
- Number of commands uploaded
- Which README.md files were auto-generated (list them)
- Whether root `.claude/README.md` was generated
- Link to the project folder in Outline
- **Documentation completeness check:** list every uploaded README (per-skill and root) that still contains a `TODO` in the human-only sections (*When / Why / Impact / Tips*). Flag them as **"not yet documented — human sections pending"**. Per Andy's 2026-04-17 DMT feedback, a skill only counts as documented once a person has filled those sections on a real project.

## Important Rules

- **Push only** — never pull or download anything from Outline
- **Never push `common/`, `memory/`, `plans/`, `projects/`**
- **Skip README generation if file exists** — respect manual edits
- **Skip root README generation if `.claude/README.md` exists**
- **Use `editMode: "replace"` for updates** — full replacement, not patching
- **Derive project name from git remote** — don't ask the user
- **Merge README + SKILL.md into one Outline document** — README first, separator, then SKILL.md
- **Never auto-fill the human-only README sections** (*When / Why / Impact / Tips*) — leave `TODO` placeholders so a real user has to write them. Report them as pending in step 7.
