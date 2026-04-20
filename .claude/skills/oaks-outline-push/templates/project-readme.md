# {{PROJECT_NAME}}

> {{PROJECT_DESCRIPTION}}
> <!-- e.g. "DMT workspace for Tonda Kmoch — brainstorming, planning, and delivery management at Oaks Lab." -->

## AI setup at a glance

- **CLAUDE.md:** {{PRESENT_OR_MISSING}} — project-level instructions loaded into every conversation.
- **settings.json:** {{PRESENT_OR_MISSING}} — hooks, permissions, MCP servers.
- **Memory:** `.claude/memory/` (private, not pushed to Outline).

## Skills

| Skill | What it does |
|-------|--------------|
{{SKILLS_TABLE_ROWS}}
<!-- Each row: `| [name](./skills/name/) | description from frontmatter | ` -->

## Commands

| Command | What it does |
|---------|--------------|
{{COMMANDS_TABLE_ROWS}}
<!-- Omit the whole section if there are no commands. -->

## How the skills connect

{{FLOW_OR_SEQUENCE}}
<!-- Optional: short description or mermaid diagram showing the typical order
     skills are run in (e.g. brainstorm → plan → push).
     If there's no clear flow, write "Skills are independent — run as needed." -->

---

> **The sections below must be written by a human — not AI.**
> They describe what this project's AI setup actually does in practice, why it's set up this way, and what changed because of it. Leave the `TODO` in place until a real user of this workspace fills them. A project README with any `TODO` here is **not** considered documented.

## When this setup helps

<!-- TODO (human): Concrete moments in the project's work where the AI setup earns its keep.
     E.g. "Every Friday when preparing the product-sync deck", "When a new DMT initiative kicks off".
     Name the trigger and the phase. -->

TODO

## Why this setup exists

<!-- TODO (human): The real reason the skills and config look like this. Origin story in one paragraph.
     What problem were we solving? What was tried before this? -->

TODO

## Impact (real, observed)

<!-- TODO (human): What has actually changed since the setup was put in place?
     Name projects, dates, or rough numbers.
     E.g. "DMT meeting prep went from ~2h to ~30min since 2026-04."
     If nothing yet, write "Not yet measured — baseline on [date]." -->

TODO

## Tips & gotchas

<!-- TODO (human): Things someone joining this workspace should know that aren't in the files.
     Edge cases, manual steps still required, known broken flows, conventions we follow. -->

- TODO
