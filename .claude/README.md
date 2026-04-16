# ai-agent — Claude Code Configuration

This project is used for DMT (Digital Management Team) brainstorming and delivery management work at Oaks Lab. It contains Claude Code skills for managing AI knowledge sharing across projects.

## Skills

| Skill | Description | Status |
|-------|-------------|--------|
| [oaks-outline-push](skills/oaks-outline-push/) | One-way push of `.claude/` config to Outline AI Skills Library for human browsing | Active |
| [pull-outline-index](skills/pull-outline-index/) | Pulls document metadata from Outline collections to regenerate the local `outline-index.md` | Active |

## Typical Flow

1. **`/pull-outline-index`** — Refresh local awareness of what's in Outline
2. Work on skills, brainstorming, or documentation
3. **`/oaks-outline-push`** — Publish your `.claude/` setup to the AI Skills Library in Outline

## Configuration

- **CLAUDE.md** — Project instructions and context (at workspace root)
- **settings.json** — Not present in this project

## Outline Integration

This project uses Outline as the source of truth for documentation. The `outline-index.md` file at the workspace root serves as a local index of tracked collections. See CLAUDE.md for details on how Outline integration works.