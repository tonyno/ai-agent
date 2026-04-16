# AI Skills Sharing Redesign — Two-Skill Architecture

> **Status:** Approved | **Author:** Tonda Kmoch + AI | **Date:** 2026-04-16

---

## Problem

SKILL.md files use YAML frontmatter (`---\nname: ...\ndescription: ...\n---`) that Claude Code requires to recognize skills. Outline's markdown renderer interprets `---` as horizontal rules and mangles the YAML into heading text. This makes round-trip sharing (push to Outline → pull from Outline) destructive — pulled skills are broken.

The original `/oaks-skills-sync` skill tried to use Outline for both browsing and distribution. That approach is fundamentally incompatible with YAML frontmatter preservation.

## Solution

Separate the two concerns into independent skills:

- **`/oaks-outline-push`** — One-way push to Outline for human browsing. Frontmatter can be broken because nobody pulls working files from Outline.
- **`/oaks-skills-pull`** — Pull common skills from a dedicated git repo. Frontmatter stays intact because git handles files as-is.

```
┌──────────────────────────────────────────────────┐
│                   Project Repo                    │
│                                                   │
│  .claude/                                         │
│  ├── README.md            ← auto-generated        │
│  ├── skills/                                      │
│  │   ├── my-skill/SKILL.md + README.md            │
│  │   └── common/          ← pulled from git repo  │
│  │       ├── oaks-outline-push/SKILL.md           │
│  │       ├── oaks-skills-pull/SKILL.md            │
│  │       └── pull-outline-index/SKILL.md          │
│  ├── CLAUDE.md                                    │
│  └── settings.json                                │
└────────┬─────────────────────────┬────────────────┘
         │                         │
         │ /oaks-outline-push      │ /oaks-skills-pull
         ▼                         ▼
┌────────────────┐   ┌───────────────────────────────┐
│   Outline      │   │  oakslab/claude-skills-library  │
│  (browsing)    │   │         (git repo)              │
│                │   │                                 │
│  AI Skills     │   │  common/skills/                 │
│  Library/      │   │  ├── oaks-outline-push/         │
│  ├── proj-A/   │   │  │   └── SKILL.md  (intact)    │
│  ├── proj-B/   │   │  ├── oaks-skills-pull/          │
│  └── common/   │   │  │   └── SKILL.md              │
│   (read-only   │   │  └── pull-outline-index/        │
│    mirror)     │   │      └── SKILL.md               │
└────────────────┘   └───────────────────────────────┘
```

---

## Skill 1: `/oaks-outline-push`

### Purpose

One-way push of the project's `.claude/` configuration to Outline for human-readable browsing. No pull, no self-update, no frontmatter preservation needed.

### Steps

#### 1. Identify the project

- Run `git remote get-url origin`
- Extract the repo name (e.g., `git@github.com:oakslab/olh-monorepo.git` → `olh-monorepo`)

#### 2. Find the AI Skills Library in Outline

- AI Skills Library parent document ID: `4bc544a3-9f7f-4af7-add5-f2b4e29a481b`
- Use `mcp__claude_ai_GetOutline__list_documents` to find or create the project's folder

#### 3. Scan `.claude/` directory

Collect everything to upload:

**Skills and commands:**
- `.claude/skills/*/SKILL.md` (folder-based skills — use folder name as skill name)
- `.claude/skills/*.md` (legacy flat files — use filename without extension)
- `.claude/commands/*/SKILL.md` and `.claude/commands/*.md` (same pattern)

**Config files:**
- `.claude/CLAUDE.md` or `CLAUDE.md` at workspace root
- `.claude/settings.json`

**Skip:**
- `.claude/skills/common/` — pulled content, never push back
- `.claude/memory/` — private
- `.claude/plans/` — ephemeral
- `.claude/projects/` — may contain private memory
- `templates/` directories inside skill folders — supporting files

#### 4. Generate per-skill README.md (if missing)

For each skill folder that does NOT have a `README.md`:

1. Read the skill's `SKILL.md`
2. Auto-generate a README covering: name, description, usage, what it does, prerequisites, audience
3. Write the README to the skill's folder

If generation fails for any reason, create a placeholder:
```markdown
# [skill-name]

> README not yet documented. Please describe what this skill does.
```

If `README.md` already exists, skip — use it as-is.

#### 5. Generate root `.claude/README.md` (if missing)

If `.claude/README.md` does not exist, auto-generate a project signpost:

- Project name and description
- Table of all skills (name, description, link hint)
- Table of all commands
- Notes about CLAUDE.md and settings.json
- How skills connect / recommended flow

If `.claude/README.md` already exists, skip — use it as-is.

#### 6. Upload to Outline

**Root document** (project landing page):
- Title: `[project-name]`
- Content: the `.claude/README.md` content
- Parent: AI Skills Library document

**Per-skill documents:**
- Title: `[skill-name]`
- Content: README.md content first, then `---` separator, then full SKILL.md content below
- Parent: the project's root document

**Config documents:**
- `CLAUDE.md` — uploaded as-is
- `settings.json` — wrapped in a code block

For each document: if it already exists (same title under same parent), update it. Otherwise create it.

#### 7. Report

- Project name identified
- Number of skills/commands pushed
- Which READMEs were auto-generated
- Link to the project's folder in Outline

### Outline document structure

```
AI Skills Library /
├── 📄 my-project              ← root README (signpost)
│   ├── 📄 skill-alpha         ← README + SKILL.md merged
│   ├── 📄 skill-beta          ← README + SKILL.md merged
│   ├── 📄 CLAUDE.md           ← project config
│   └── 📄 settings.json       ← code block
```

### Important rules

- **Never pull from Outline** — this skill is push-only
- **Never push `.claude/skills/common/`** — that's pulled content
- **Never push `.claude/memory/`, `.claude/plans/`, `.claude/projects/`**
- **Skip README generation if README already exists** — respect manual edits
- **Skip root README generation if `.claude/README.md` already exists**
- **Use `editMode: "replace"` for updates** — full replacement, not patching

---

## Skill 2: `/oaks-skills-pull`

### Purpose

Pull common/shared skills from the `oakslab/claude-skills-library` git repository into `.claude/skills/common/`. Preserves YAML frontmatter perfectly because git handles files as-is.

### Steps

#### 1. Pull common skills from git

Default method — **sparse checkout** (no extra dependencies):

```bash
tmp=$(mktemp -d)
git clone --filter=blob:none --no-checkout --depth=1 \
  git@github.com:oakslab/claude-skills-library.git "$tmp"
cd "$tmp" && git sparse-checkout set common/skills && git checkout
cp -r "$tmp/common/skills/"* "<project>/.claude/skills/common/"
rm -rf "$tmp"
```

#### 2. Report

- List of skills pulled
- Any new skills (not previously in `.claude/skills/common/`)
- Any updated skills (files changed)

### Alternative git distribution methods

The skill should document these alternatives for teams who prefer them:

#### Option A: Sparse checkout (default — recommended)

```bash
tmp=$(mktemp -d)
git clone --filter=blob:none --no-checkout --depth=1 \
  git@github.com:oakslab/claude-skills-library.git "$tmp"
cd "$tmp" && git sparse-checkout set common/skills && git checkout
cp -r "$tmp/common/skills/"* .claude/skills/common/
rm -rf "$tmp"
```

**Pros:**
- No extra dependencies — pure git
- Works with SSH auth automatically
- Downloads only the target folder (minimal data)
- No git metadata left in the destination

**Cons:**
- ~5 lines of scripting vs a one-liner
- Temporary directory management

#### Option B: degit

```bash
npx degit oakslab/claude-skills-library/common/skills .claude/skills/common
```

**Pros:**
- One-liner, dead simple
- No git metadata in destination
- Purpose-built for this exact use case

**Cons:**
- Requires Node.js (all Oaks projects have it, but it's still a dependency)
- Private repo support needs token configuration
- `degit`/`tiged` package must be available

#### Option C: git subtree

```bash
# First time:
git subtree add --prefix=.claude/skills/common \
  git@github.com:oakslab/claude-skills-library.git main --squash

# Updates:
git subtree pull --prefix=.claude/skills/common \
  git@github.com:oakslab/claude-skills-library.git main --squash
```

**Pros:**
- Built into git, no extra tools
- Files become regular tracked files in the project repo
- Merge history preserved

**Cons:**
- Brings commit history (squashed, but still adds merge commits)
- More complex mental model
- Overkill for syncing a handful of skill files

#### Option D: GitHub API / gh CLI

```bash
# List files in the folder
gh api repos/oakslab/claude-skills-library/contents/common/skills \
  --jq '.[].name' | while read skill; do
    gh api repos/oakslab/claude-skills-library/contents/common/skills/$skill/SKILL.md \
      --jq '.content' | base64 -d > .claude/skills/common/$skill/SKILL.md
done
```

**Pros:**
- Works anywhere `gh` is installed
- No git clone needed

**Cons:**
- Awkward for nested directories (must iterate)
- Rate-limited
- Requires `gh auth login`

### Important rules

- **Never interact with Outline** — this skill is git-only
- **Overwrite `.claude/skills/common/`** — the git repo is authoritative
- **Never modify project-specific skills** — only touch `common/`
- **Preserve file structure** — each skill keeps its directory (e.g., `common/skill-name/SKILL.md`)

---

## Shared Git Repository

### Repository

`oakslab/claude-skills-library` (GitHub, private)

### Structure

```
oakslab/claude-skills-library/
├── README.md                         ← Repo docs: what this is, how to use
├── docs/
│   └── git-distribution-options.md   ← Detailed comparison of pull methods
└── common/
    └── skills/
        ├── oaks-outline-push/
        │   ├── SKILL.md
        │   └── templates/
        │       └── skill-readme.md
        ├── oaks-skills-pull/
        │   └── SKILL.md
        └── pull-outline-index/
            └── SKILL.md
```

### Conventions

- `common/skills/` — skills intended for all projects
- Each skill is a directory with `SKILL.md` as the entrypoint
- YAML frontmatter must be present and valid in every SKILL.md
- `main` branch is the source of truth (no tagged releases for now)
- Changes to common skills go through PR review

---

## Migration from `/oaks-skills-sync`

1. Build and test both new skills in this repo (`dmt-tonda`)
2. Push them to the shared git repo
3. Replace `oaks-skills-sync` with the two new skills on pilot projects
4. Update Outline documentation (AI Skills Library, AI Knowledge Architecture)
5. Retire `oaks-skills-sync`

---

## Outline Documentation Updates

### AI Skills Library document

Update to reflect:
- Two skills instead of one (`/oaks-outline-push` + `/oaks-skills-pull`)
- Outline is browsing-only (no pull from Outline)
- Common skills distributed via git repo
- Getting Started guide: download both skills, run push and pull separately
- Mermaid diagram updated to show two separate flows

### AI Knowledge Architecture document

Update the "Shared AI Configuration — Approved Approach" section:
- Acknowledge the frontmatter limitation discovered
- Updated architecture: Outline for browsing, git for distribution
- Reference the new skill names

### AI Skills Sharing — Action Items document

Already created with the full task list and open decisions.

---

## Open Decisions

| # | Decision | Recommendation | Status |
|---|----------|----------------|--------|
| D1 | Shared git repo name | `oakslab/claude-skills-library` | To confirm |
| D2 | Repo visibility | Private (contains internal skills) | To confirm |
| D3 | Initial common skills | `oaks-outline-push`, `oaks-skills-pull`, `pull-outline-index` | To confirm |
| D4 | Versioning strategy | Just `main` branch, no tagged releases | To confirm |
| D5 | Bootstrap script in repo | Optional shell script that projects can curl | To decide |
