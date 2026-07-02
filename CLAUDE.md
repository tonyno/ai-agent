# DMT — Tonda Kmoch @ OAK'S LAB

This workspace supports **Antonín (Tonda) Kmoch, Head of Delivery** at OAK'S LAB, in his work on
the **DIGITAL Management Team (DMT)** and on the projects he supports. Use it as a second brain:
help process meetings, prep for DMT sessions, draft updates, track actions, and manage the
projects Tonda owns.

> **How this file relates to Outline.** OAK'S LAB runs its management information system in
> **Outline** (`outline.oakslab.com`), a living, constantly-changing space. This file captures
> only the **stable** parts — roles, information architecture, conventions, routing rules, and
> entry-point links. **Anything that changes — project status, risks, open actions, transcripts,
> team assignments — is NOT copied here. Fetch it live from Outline** (via the Outline MCP tools)
> whenever a task needs it. If this file and Outline ever disagree, Outline wins; re-verify and
> flag the drift.

---

## Working principles (read before acting on DMT tasks)

1. **Always ground in recent meetings first.** Before discussing any DMT topic or project,
   fetch and read the relevant **recent transcripts / Hub "Recent Context"** from Outline to
   understand what was discussed, decided, and suggested. Never reason from memory alone — the
   situation moves week to week. The [Meeting Transcript List](https://outline.oakslab.com/doc/meeting-transcript-list-Tk8zugBbdr)
   is the entry point for finding any transcript (search by project tag or date).
2. **Resolve every name against the People Registry** before writing it anywhere (see
   [Name resolution](#name-resolution-critical)). Transcript tools mangle Czech/Turkish/
   Ukrainian/Portuguese names — never propagate a wrong one.
3. **Respect the source-of-truth rules.** Each fact has exactly one canonical home (see
   [Information architecture](#the-dmt-information-system)). Write to the source, not a derived view.
4. **Keep it simple and focused.** Prioritize the urgent/important; don't overwhelm with
   exhaustive lists. Mirror the narrative, prose-first tone of the Playbook when briefing
   or drafting client-facing material.
5. **Confirm before finalizing Hub updates** — see the [AI Hub Update Confirmation Protocol](#ai-hub-update-confirmation-protocol).

---

## Essential Outline documents (living sources — fetch fresh)

**Playbook & operating manual**
- [Playbook](https://outline.oakslab.com/doc/playbook-tfce68p3cQ) — index/router for "how OAK'S LAB works". Load the specific sub-doc that matches the task:
  - [Company Overview](https://outline.oakslab.com/doc/company-overview-juAbeyzc49) · [Business Development](https://outline.oakslab.com/doc/business-development-MgHboKzfQd) · [Client Management](https://outline.oakslab.com/doc/client-management-003BXKpPc8) · [SOW & Financial Management](https://outline.oakslab.com/doc/sow-financial-management-PpoQymhx81) · [Squad Roster & Team Allocation](https://outline.oakslab.com/doc/squad-roster-team-allocation-wWOwy58mV4)
- [DMT Information System — Processing Rules](https://outline.oakslab.com/doc/dmt-information-system-processing-rules-hC9AyE24ZU) — **the operating manual** for how meetings get processed, where info goes, page conventions, routing, weekly rhythm. This file is a local distillation of it; re-sync from it when in doubt.
- [People Registry & Slack Map](https://outline.oakslab.com/doc/people-registry-slack-map-ZZT2ZVSnJb) — canonical names, Slack IDs, and AI name-resolution rules.

**Derived / cross-project views** (generated from Hubs — never edit as a primary source)
- [Projects Dashboard](https://outline.oakslab.com/doc/projects-dashboard-2M8sX41vNQ) — one row per project: health, sentiment, DMT owner, revenue, SOW expiry.
- [All Actions](https://outline.oakslab.com/doc/all-actions-uNNYg1bSpR) — every open action across projects, grouped by person (+ cross-cutting section).
- [Waterboarding Prep Doc](https://outline.oakslab.com/doc/waterboarding-CsQvnLvPBj) — generated each Monday; each DMT member fills their section before Tuesday.
- [Meeting Transcripts](https://outline.oakslab.com/doc/meeting-transcripts-tdeWJ9lwvN) — where DMT-meeting transcripts land for processing.
- [Meeting Transcript List](https://outline.oakslab.com/doc/meeting-transcript-list-Tk8zugBbdr) — auto-generated index of **all** transcripts (date, meeting, project, link). Start here to find any transcript. (Auto-generated — manual edits are overwritten.)

**Templates**
- [Project Hub Template](https://outline.oakslab.com/doc/project-hub-template-EcPG4UKPLD) · [Product Sync Template](https://outline.oakslab.com/doc/product-sync-template-project_name-product-sync-yyyy-mm-dd-w4UhFsHSoy)

**Collections** (for MCP `list_collection_documents` / navigation)
- **DMT** — `c5f6177e-3348-44e7-a590-505fbb00405f` (slug `dmt-luEGhTE3lw`) — Hubs, Dashboard, All Actions, Playbook, Meetings, Transcripts. *Access: DMT + Johan.*
- **Product Syncs** — `90475a8f-37a1-4a19-aebf-89acc8b27600` (slug `product-syncs-RIjdenzKfV`) — PS Hub per project + meeting sub-pages. *Access: all project teams.*
- **1:1s** — slug `11s-ubh4dZ9sUV` — 1:1 docs per direct report. *Restricted per relationship.*
- **The OAK'S LAB WAY** — collection `bcc3903f` — company methodology docs (~100 docs).

---

## The DMT information system

### Two-Hub model — every project has up to two Hub pages

| | **DMT Project Hub** | **Product Sync (PS) Hub** |
|---|---|---|
| Collection | DMT (DMT members + Johan only) | Product Syncs (team-visible) |
| Audience | Management source of truth | Team-facing view |
| Contains | Status, DMT actions, SOW, commitments, risks, decisions, recent context | Team actions, status, team risks, ongoing directives, items flagged for DMT |
| Excludes | — | Salary, performance, confidential client discussion |
| Updated by | Johan (from meeting processing), Andy (from waterboarding/1:1s) | The project's PM / Product Lead |

- **DMT actions** (owned by DMT) live ONLY on the DMT Hub. **Team actions** (PMs, TLs, engineers, designers) live ONLY on the PS Hub.
- The DMT Hub **links** to the PS Hub for team detail — it does not duplicate it.
- **Escalation:** a PM flags a management-level item (SOW concerns, client-relationship issues, staffing risk, budget overrun) in the PS Hub's `⬆️ Flagged for DMT` section; **Johan** routes it to the DMT Hub during his daily scan.

### Source-of-truth rules

| Information | Canonical home | Also appears in | Sync owner |
|---|---|---|---|
| 🎯 DMT Actions | DMT Hub | All Actions | Johan |
| 👷 Team Actions | PS Hub | All Actions | PM owns; Johan aggregates |
| 📅 Commitments | DMT Hub | — | Johan |
| 📝 Key Decisions | DMT Hub | — | Processor |
| ⚠️ DMT-level Risks | DMT Hub | — | Johan |
| ⚠️ Team Risks | PS Hub | Escalated to DMT Hub if needed | PM flags; Johan escalates |
| 📊 Project Status | DMT Hub | Dashboard | Johan |
| 🏢 Cross-cutting Actions | All Actions (top) | — | Any DMT member / Johan |

---

## Projects

Stable skeleton below. **For live status, risks, and actions, always fetch the Hub** — do not
assume anything here is current. **Tonda's DMT-owned projects: OpenLoop and Learning Spring.**

| Project | DMT Owner | DMT Hub | PS Hub | PM / PL | Leads channel |
|---|---|---|---|---|---|
| NPM | Kryštof | [npm-project-hub-NBOfQjSJaU](https://outline.oakslab.com/doc/npm-project-hub-NBOfQjSJaU) | [npm-ps-hub-cFMWhRgqcm](https://outline.oakslab.com/doc/npm-ps-hub-cFMWhRgqcm) | Eda / Tamás | `#npm_leads` |
| **OpenLoop (Intake)** | **Tonda** | [openloop-project-hub-jc9nvMWRIl](https://outline.oakslab.com/doc/openloop-project-hub-jc9nvMWRIl) | [openloop-intake-ps-hub-UCRhG4fMg7](https://outline.oakslab.com/doc/openloop-intake-ps-hub-UCRhG4fMg7) | Kyle | `#openloop_leads` |
| **OpenLoop RCM** | (Tonda / DMT) | (see OpenLoop Hub) | [openloop-rcm-ps-hub-Zk9j1f3qzr](https://outline.oakslab.com/doc/openloop-rcm-ps-hub-Zk9j1f3qzr) | Vilém | `#openloop_2_leads` |
| **Learning Spring** | **Tonda** | [learning-spring-project-hub-uKFrfjDoCa](https://outline.oakslab.com/doc/learning-spring-project-hub-uKFrfjDoCa) | [learning-spring-ps-hub-ze5VfsAc9e](https://outline.oakslab.com/doc/learning-spring-ps-hub-ze5VfsAc9e) | Dani | — |
| Blackpoint | Andy | [blackpoint-project-hub-t1kdwn0RVC](https://outline.oakslab.com/doc/blackpoint-project-hub-t1kdwn0RVC) | [blackpoint-ps-hub-OcFT3HnbTA](https://outline.oakslab.com/doc/blackpoint-ps-hub-OcFT3HnbTA) | Oleksii | `#blackpoint_leads` |
| Reservoir | Kryštof | [reservoir-project-hub-1DN073st7N](https://outline.oakslab.com/doc/reservoir-project-hub-1DN073st7N) | [reservoir-ps-hub-DJ65l8tqjY](https://outline.oakslab.com/doc/reservoir-ps-hub-DJ65l8tqjY) | TBD | — |
| DealSage | Matěj | [dealsage-project-hub-wLBKg5iOhG](https://outline.oakslab.com/doc/dealsage-project-hub-wLBKg5iOhG) | [dealsage-ps-hub-CLbu0Tl7BH](https://outline.oakslab.com/doc/dealsage-ps-hub-CLbu0Tl7BH) | TBD | `#dealsage_leads` |
| EPP (Exam Papers Plus) | Denisa | [epp-project-hub-7ZicRMTYg4](https://outline.oakslab.com/doc/epp-project-hub-7ZicRMTYg4) | [exam-papers-plus-ps-hub-J47xLpanaN](https://outline.oakslab.com/doc/exam-papers-plus-ps-hub-J47xLpanaN) | Michal | `#exampapersplus_leads` |
| Miri | TBD | — | [miri-ps-hub-yCjC9AHofF](https://outline.oakslab.com/doc/miri-ps-hub-yCjC9AHofF) | — | — |

**Not yet on Hub format:** Narwhal (Andy), Future Mortgage (Kryštof), Storyvine (Andy), Stadium Travel (TBD).

Each PS Hub has **PS Documents** (processed summaries) and **PS Meetings** (raw transcripts) sub-pages.
To enumerate the current tree, use `list_collection_documents` on the Product Syncs collection.

---

## Team (DMT & key contacts)

Full roster with Slack IDs and diacritics is in the [People Registry](https://outline.oakslab.com/doc/people-registry-slack-map-ZZT2ZVSnJb) —
**always look there for anyone not listed below, and before @mentioning anyone in Slack.**
Source of truth for team composition: [DIGITAL Team Overview sheet](https://docs.google.com/spreadsheets/d/1kNbMisMa4c9CC6hk9NKzHiMnHx5JuWcrwtIOC2o0GQI/edit#gid=1750675590). Registry owner: **Cristina Attina**.

**DMT (DIGITAL Management Team)** — Andy's leadership team, channel `#management_digital` (`G0159HZA7LZ`):

| Name | Role | Slack |
|---|---|---|
| Andy Powell | COO (DMT lead, owner of the info system) | `ULPS9KG6Q` |
| Kryštof Šraier | Delivery Director | `U055Q1XUV1T` |
| **Antonín (Tonda) Kmoch** | **Head of Delivery** *(this workspace)* | `U02J1DQQ867` |
| Denisa Lorencová | Head of Design | `U086UQ1SZF0` |
| Jan (Honza) Bárta | Head of Engineering | `D09FEF0T6DU` |
| Matěj Novak | Head of Product | `D0APSQDQ7JB` |
| Cristina Attina | People Ops Manager | `U089FLM977W` |
| **Johan Winberg** | I.T Project coordinator — **processes meetings & maintains Hubs** | `D0B33FVGJVA` |

**Leadership / founders:** Jake Dluhy-Smith (CEO), Theo Dluhy-Smith (Exec Director & Co-Founder), Martin Klikar (CFO).

**Disambiguation traps** (from the registry — always confirm which one):
- Two **Jaroslav** — Málek and Smolík ("Jarda" is ambiguous).
- Two **Jan** — Bárta (Head of Eng) and Korych (Product Lead).
- Two **Petr** on NPM — Bartoň (designer) and Mácal (engineer).
- **Masha** — could be Mariia Boiko (our QA) or a client-side person on OpenLoop.
- **Igor** — Starcheus (QA) or a contractor.

---

## Name resolution (CRITICAL)

Before writing **any** person's name into a document, message, or note, resolve it against the
People Registry. Transcript tools (Granola, Otter, Google Meet) routinely mangle non-English
names (e.g. "Kristoff" → Kryštof, "Kooba" → Kuba, "Denisa Lorenzo" → Denisa Lorencová).

1. **Canonical spelling with diacritics** in formal contexts: `Kryštof Šraier`, not `Krystof Sraier`; `Tomáš Necuda`, not `Tomas Necuda`.
2. **Short forms are fine in prose / Slack / informal notes:** Kuba, Honza, Tonda, Dani, Meli, Eda, Val, Ed.
3. **Full canonical names** in action items, rosters, headers, tables.
4. **Slack @mentions:** `<@SLACK_ID>` using the ID from the registry. If the ID is `TBD`, spell the name and flag it.
5. **Outline @mentions:** `@[Display Name](mention://user/userId)` — use `list_users` (Outline MCP) to find the user ID.
6. **Never** write an ASCII-stripped version of a name with diacritics into a formal doc (URLs/emails excepted).
7. **If a transcript name doesn't match any registry entry — STOP and ask. Don't guess.**

---

## Format conventions

- **Action items** (all pages):
  `- [ ] @[Person Name](mention://...) — description — due YYYY-MM-DD — (source: meeting YYYY-MM-DD)`
  Every action needs an @mention, description, due date, and source meeting. **Completed → remove it** (don't leave checked boxes). Overdue → flag ⚠️ / ⏰.
- **Dates:** always `YYYY-MM-DD`. No exceptions.
- **Health:** 🟢 On Track · 🟡 At Risk · 🔴 Off Track.
- **Client sentiment:** 🟢 Happy · 🟡 Mixed · 🔴 Unhappy.
- **Recent Context:** max **3** entries per Hub; adding a 4th drops the oldest. Format:
  `### YYYY-MM-DD — [Meeting Name]` then `**Key points**`, `**New actions**`, `**Sentiment change**`.
- **Transcript status:** 🔲 Unprocessed · ✅ Processed. Nothing stays 🔲 for more than 24h.

---

## Processing workflows

| Meeting | When | Processor | Outputs to |
|---|---|---|---|
| Waterboarding | Tuesday | Andy / Johan | DMT Hubs → All Actions → Dashboard |
| DMT Friday | Friday | Johan | DMT Hubs → All Actions → Dashboard |
| Product Syncs | Wed–Thu | PM / PL | PS Hub; flags → DMT Hub via Johan |
| Prep Doc (generation) | Monday | Johan | Waterboarding Prep Doc |

**Processing a DMT meeting:** read transcript → resolve names → per project, route 🎯 actions, 📝 decisions, ⚠️ risk changes, 📅 commitments, 💬 summary (max 3), 📊 status, 🏢 cross-cutting → update All Actions → update Dashboard if health/sentiment changed → mark ✅.

**Processing a Product Sync (PM):** route 👷 team actions, ⚠️ team risks, 📋 ongoing directives, 💬 summary, ⬆️ items for DMT → mark ✅. Johan picks up flags.

**Processing a Management Check-In / client update (relationship owner):** find transcript via the Meeting Transcript List → resolve names → create a sub-page under the project's **DMT Hub** titled `YYYY-MM-DD — Management Check-In ({Client First Name})` (attendees + transcript link, summary, topics, action items, risk-updates table) → route to the parent Hub (🎯/📝/⚠️/📅/💬/📊) → team follow-ups get flagged to the PM for the PS Hub.

### AI Hub Update Confirmation Protocol

After updating any DMT Hub or PS Hub, before considering it complete, confirm three things with the operator:
1. **What remains** — open actions, active risks, live commitments still standing.
2. **What should be cleaned** — completed actions to remove, resolved/stale risks, Recent Context beyond 3, superseded decisions to strike through, overdue items needing a new date or escalation.
3. **Updated project health** — proposed 🟢🟡🔴 + client sentiment with a one-line justification. Operator confirms before the header (and Dashboard) change.

### Weekly rhythm

Mon: Johan generates prep doc from Hubs → shares with DMT. · Tue: Waterboarding, then process. ·
Wed–Thu: Product syncs, PMs process. · Fri: DMT meeting, then process. ·
Daily: Johan scans for 🔲 transcripts (none >24h) and PS-Hub flags.

---

## Tooling & skills

- **Outline MCP** — `fetch`, `list_documents`, `list_collection_documents`, `list_collections`, `list_users`, `create_document`, `update_document`, `create_comment`, `move_document`. Primary interface to the info system. (Large fetches may exceed the token cap and get saved to a file — handle in a subagent when that happens.)
- **Other connected MCP:** Linear, Slack, Granola (meeting transcripts), Gmail, Google Calendar/Drive, Asana, Figma, Miro, Notion, Excalidraw, PostHog.
- **Project skills** (`.claude/`): `outline-to-linear` (turn a doc's "Next steps" into Linear tickets), `pull-outline-index` (refresh local index of tracked collections), `generate-project-brief`, `oaks-outline-push` (publish `.claude/` config to the Outline AI Skills Library), `excalidraw-diagram*`, `deep-research`.

---

## About OAK'S LAB (reference)

Outsourced software development company founded **2016 in Prague** by Czech-American brothers
**Jake & Theo Dluhy-Smith**. Connects American companies with elite Czech (and broader EU)
dev talent; bootstrapped (no investors); 85+ team members, 65+ products launched, ~80% US clients.
**Mission:** empower innovators to improve life and the world. **Vision:** a hub of groundbreaking global innovation.

- **Services:** Product Discovery & Design · Full-stack JS/TS Development (Next.js, React, React Native, Node) · AI & Agentic Systems (LLM, RAG, orchestration; Python).
- **Engagement models:** Autonomous Teams (cross-functional PM/design/eng/QA) · Staff Augmentation.
- **Industries:** FinTech, Cybersecurity, FoodTech, EdTech, HR Tech, PropTech, E-commerce, Real Estate & Investment, Media & Entertainment.
- **Tech:** TS/React/Next/Material UI/Firebase · Node/Prisma/tRPC · GCP/PostgreSQL/Docker/GitHub CI · Claude/ChatGPT/Vertex · Figma/Adobe/Webflow/Lovable · Jira/Confluence/Miro · QASE/Playwright/Postman.
- **Values:** strive for excellence · outcomes over outputs · deliver quality · practice honesty · demonstrate kindness · positivity through challenges.
- **Credentials:** ISO 27001 · 5.0/5.0 Clutch (31 reviews) · 89% post-contract retention · top 0.4% of applicants hired · clients raised $200M+ · TechCrunch Disrupt 2023.

For deeper detail load the [Company Overview](https://outline.oakslab.com/doc/company-overview-juAbeyzc49) playbook doc rather than expanding this section.
