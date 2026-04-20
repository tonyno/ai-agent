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

---

> **The sections below must be written by a human — not AI.**
> AI-generated claims about impact or tips read as sales copy. Leave the `TODO` in place until someone who has actually run this skill on a real project fills the section. A skill with any `TODO` here does **not** count as documented.

## When to use it

<!-- TODO (Tonda): Concrete situations where reaching for this skill is the right move.
     E.g. "After modifying any skill in .claude/skills/ and before sharing it with other DMT members."
     Name the trigger. Name the project phase. No aspirational statements. -->

TODO

## Why this skill exists

<!-- TODO (Tonda): The real reason we built/use this vs doing it manually or with another tool.
     What pain does it remove? What mistake did it prevent in practice?
     One sentence is fine. If you can't articulate it, the skill probably isn't needed yet. -->

TODO

## Impact (real, observed)

<!-- TODO (Tonda): What has actually changed since we started using it? Name projects, dates, or numbers.
     E.g. "Demoed on Open Loop and dmt-tonda at the 2026-04-17 DMT sync — replaced manual Outline copy-paste for every skill change."
     No hypotheticals. If there's no observed impact yet, write "Not yet measured — first run on [project] on [date]." -->

TODO

## Tips & gotchas

<!-- TODO (Tonda): Things the SKILL.md doesn't say. Edge cases. Surprises.
     What tripped you up the first time? What would you tell a teammate before they run it?
     Bullet list is fine. Keep it short; grow it as you learn. -->

- TODO
