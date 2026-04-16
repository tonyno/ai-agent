# oaks-outline-push

> One-way push of the project's .claude/ config to Outline AI Skills Library for human browsing. Auto-generates README per skill and a project signpost.

## Usage

```
/oaks-outline-push
```

## What It Does

1. Identifies the project from git remote
2. Scans `.claude/` for all skills, commands, and config files
3. Auto-generates a README.md for each skill that doesn't have one
4. Auto-generates a root `.claude/README.md` signpost (table of all skills, project overview)
5. Uploads everything to Outline under `AI Skills Library / [project-name] /`
6. Each skill appears as one Outline document: README first, then raw SKILL.md below for reference

## Prerequisites

- MCP GetOutline tools must be available
- Project must be a git repository with a remote

## How it connects to other skills

- Run **after** creating or modifying skills to publish them to Outline
- Companion to `/oaks-skills-pull` (which pulls common skills from a shared git repo — separate concern)
- Independent of `/pull-outline-index` (which pulls Outline metadata locally)

## Audience

All team members — especially useful for DMT members who want to share AI configurations across projects.