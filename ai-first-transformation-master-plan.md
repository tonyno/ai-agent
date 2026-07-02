# 🗺️ AI-First Transformation — Master Plan

## Why this page exists

* Linear tickets are great for execution but hard to read as a plan
* Vision docs in Outline are great for direction but don't show progress
* This page sits between the two: workstreams → owners → status, with links back to the granular Linear/Outline items when you need to drill down


---

## The 4 priority workstreams *(*[*All-Hands split, 2026-05-12*](https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-prep-LfmQNc0SOD)*)*


:::info
*The 2 week target (*[*AISG-166*](https://linear.app/oakslab/issue/AISG-166)*) is covered in paragraphs below*

:::

| #   | **Workstream** | **Lead(s)** | **Note** |
|-----|------------|---------|------|
| 1   | **Engineering enablement** | @[Jan Barta](mention://cb9adc67-3426-46b1-afbd-8b912e49f9a6/user/3d44822d-6b6c-4940-b5fd-0247c72d79d6) + @[Jakub Šlambora](mention://1dd0b46c-5de2-401c-8224-e70b6313fd8f/user/33d57b93-f490-47e5-b2a8-dffd5d81ebcb)  |      |
| 2   | **Product discovery improvements** <br>*(incl. design merge)* | @[Matej Novak](mention://81027e53-de27-40e9-bdd7-5901d85d02dc/user/8ab9a6b6-6b83-4aa5-830e-aafdf8f20b5a) + @[Denisa Lorencova](mention://54a3bfdd-7b68-4948-a254-cbef49bc929a/user/8115985c-d547-460f-a1ed-7d01a37a1bee)  |      |
| 3   | **QA AI integration** | @[Kryštof Šraier](mention://074e6aa0-fd95-41cb-b17d-10a12cf327b1/user/f6faa48d-1207-4f34-a5c8-a05e9703917f)  |      |
| 4   | **AI-First Operations & Skill Repository** | @[Tonda Kmoch](mention://66fef18b-b765-4cb3-975a-d26ab264f360/user/ca0de915-7725-4b57-913c-24a1f2fadc10) + @[Andy Powell](mention://fe102cd4-71ef-4749-8dbb-95e2feb52dc2/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe)  |      |

## Phases (sequence)

- [x] **Phase 0 — Vision & alignment** *(Apr–early-May 2026, done)*
  - [x] DMT alignment on pilot-first approach
  - [x] 4 workstreams + owners agreed at All-Hands *(2026-05-12)*
  - [x] Gemini approved as default transcript tool
  - [x] Outline = source of truth for transcripts; curate-in-Outline workflow agreed
- [ ] **Phase 1 — Pre-requisities & Pillars & standards** *(current, May + June 2026)*
  - [x] 5 pilot projects in GetOutline (Learning Spring, OLH Intake, OLH RCM, EPP, NPM)
  - [x] Meeting with all 5 projects and learning how they use AI
  - [ ] Project Briefs generated for all 5 pilots - ==missing Learning Spring==
  - [ ] Skills library push working; common skills published - ==missing OLH RCM==
  - [ ] **Confluence → Outline migration** (open-source vs paid decision)
  - [ ] Engineering AI adoption strategy in draft
  - [ ] All the short-term essential steps (like Product Syncs, how we run DMT more in AS-IS state in Outline+AI, …)
- [ ] **Phase 2 — Planning the work in detail** *(Jun–Jul 2026, next)*
  * Onboard remaining projects to Outline (AISG-165)
  * Automated transcript pipeline live and being used by all teams (recurring skill, no manual run)
  * Kuba at 50% AISG availability and Kuba+Honza planning the AI adoption (AISG-160)
  * Token usage + productivity measurement methodology in place
- [ ] **Phase 3 — First phase of AI-first company** *(Q3 2026+)*
  * OAK'S LAB WAY activities encoded as Claude Code skills
  * Discovery Plugin (AISG-110) operational
  * Design × discovery merged; design × delivery handover defined


---

## Workstream 1 — Engineering enablement (@[Jan Barta](mention://e72ad677-bcdd-41c5-b702-659512351775/user/3d44822d-6b6c-4940-b5fd-0247c72d79d6) )

> **Leads:** Jan Barta + Kuba Šlambora
>
> **Engineering rules (agreed 2026-05-12 All-Hands):**
>
> 
> 1. Every team uses a curated library of AI skills/plugins (open source like [obra/superpowers](https://github.com/obra/superpowers) or team-maintained like OL1)
> 2. Every project has `.md` foundations: architecture · tech stack · folder structure · key patterns · data model — to give LLMs the boundaries they need to "work freely"
> 3. Engineering all-hands runs regularly with two themes: "how we use AI" (1-feature demo) + "how we built this project" (break silos)
>
> **#1 risk:** Kuba's engineering capacity. Plan to free him to 50% AISG via squad roster ([AISG-160](https://linear.app/oakslab/issue/AISG-160), [AISG-134](https://linear.app/oakslab/issue/AISG-134)).
>
> **Next cadence event:** Engineering all-hands **Tuesday 2026-05-19** — Manuel presents the "OpenLoop One" approach.

### Strategy & rollout

- [ ] **==Top priority: ==**[**AISG-134**](https://linear.app/oakslab/issue/AISG-134) Plan Kuba's 50% transition off project after Phase I (Jun 1) — *Andy*
- [ ] **==Top priority: ==**[**AISG-160**](https://linear.app/oakslab/issue/AISG-160) Plan Kuba's path to 50% AISG availability via squad roster — *Honza* *(bring concrete plan to next sync)*
- [ ] Kuba directly works with engineering teams to bring each project to Learning Spring / Open Loop adoption level — *Honza to plan rollout (from 2026-05-12)*
- [ ] One of Kuba's first activities once freed: investigate the specific pushback raised by tech leads about AI tools (carried over from 2026-05-05, never followed up) — *Kuba*
- [ ] [**AISG-147**](https://linear.app/oakslab/issue/AISG-147) Engineering Strategy for AI adoption — *Honza* *(High, in progress)*
- [ ] [**AISG-157**](https://linear.app/oakslab/issue/AISG-157) Build engineering AI adoption strategy — *Honza*
- [ ] [**AISG-159**](https://linear.app/oakslab/issue/AISG-159) Share engineering AI strategy draft for DMT review — *Honza* *(after Kuba green-lights)*
- [ ] [**AISG-149**](https://linear.app/oakslab/issue/AISG-149) Document AI foundations for new projects — *Honza*
- [ ] [**AISG-7**](https://linear.app/oakslab/issue/AISG-7) Plan/next steps for Dev Dept as part of AI Guild — *Honza*
- [ ] [**AISG-137**](https://linear.app/oakslab/issue/AISG-137) Company-wide baseline of pre-approved Claude Code operations — *Honza*

### Measurement

- [ ] [**AISG-94**](https://linear.app/oakslab/issue/AISG-94) Measure AI efficiency for tickets (delivery speed-up) — *Manuel*
- [ ] [**AISG-144**](https://linear.app/oakslab/issue/AISG-144) Methodology to measure AI productivity gains in engineering — *Honza*
- [ ] [**AISG-141**](https://linear.app/oakslab/issue/AISG-141) Track per-person AI token/model usage — *Honza*
- [ ] [**AISG-109**](https://linear.app/oakslab/issue/AISG-109) Token optimization (compact skills + reduce base context) — *Manuel*
- [ ] Document current process for putting engineers on premium plan when they reach usage limits — *Honza* *(from 2026-05-05)*
- [ ] Create usage-visibility script so engineers' AI tool usage is visible to the team — *Honza* *(from 2026-05-05; partly overlaps AISG-141)*
- [ ] Decide: auto-upgrade engineers to premium vs reactive upgrade — *Honza × Andy*

### Experiments & exploration

- [ ] [**AISG-10**](https://linear.app/oakslab/issue/AISG-10) IDE AI feature comparison (Cursor, Antigravity vs Claude Code) — *Honza*
- [ ] [**AISG-91**](https://linear.app/oakslab/issue/AISG-91) Explore TDD approach for development — *Manuel*
- [ ] [**AISG-92**](https://linear.app/oakslab/issue/AISG-92) Explore AI agent memory / improvement feedback loop — *Manuel*
- [ ] [**AISG-73**](https://linear.app/oakslab/issue/AISG-73) EPP: Prototyping through Claude Code — *Anastasiia*
- [ ] [**AISG-51**](https://linear.app/oakslab/issue/AISG-51) Investigate Claude Code × Figma MCP — *Kseniia*


---

## Workstream 2 — Product discovery improvements *(incl. design merge) (*@[Matej Novak](mention://d883d54c-5e1d-4873-951a-1b37a3ea5074/user/8ab9a6b6-6b83-4aa5-830e-aafdf8f20b5a) )

> **Leads:** Matej Novak + Denisa Lorencova
>
> **Three sub-streams:**
>
> 
> 1. Context Window (PRIMARY SUB-STREAM, @[Matej Novak](mention://577e7e35-0f51-4e9a-b289-8fa46593be7f/user/8ab9a6b6-6b83-4aa5-830e-aafdf8f20b5a) @[Denisa Lorencova](mention://1b288ced-cac6-4837-b201-9981c90838b7/user/8115985c-d547-460f-a1ed-7d01a37a1bee) ) 
> 2. Collect discovery skills/plugins/prompts @[Matej Novak](mention://27888479-40fd-45e4-a46c-aa19ea3b8cf4/user/8ab9a6b6-6b83-4aa5-830e-aafdf8f20b5a) @[Denisa Lorencova](mention://f5d23fac-03d8-488c-badd-e85738e82918/user/8115985c-d547-460f-a1ed-7d01a37a1bee) 
> 3. Create skills out of the methodology (OWL plugin) @[Matej Novak](mention://0e34d49c-43fb-484d-9a0a-acfe1bf6312f/user/8ab9a6b6-6b83-4aa5-830e-aafdf8f20b5a) @[Denisa Lorencova](mention://9af50df7-373e-45a4-a869-96c11d3cd42d/user/8115985c-d547-460f-a1ed-7d01a37a1bee) 

### Pillar 1 — Context Window

> **Guiding principle — Context > Skills:** Context is the more valuable lever than skills, and the harder one to build and maintain. Especially true for product work where workflows are less deterministic. Better context → better AI outcomes. *(Matej's framing, reinforced 2026-05-20 — this is THE essential activity for AI-assisted product work.)*
>
> **Mindset shift to drive in the org:** Build the project context window **for AI, not just for people**. Teams today treat context as a static repository dump (decisions, specs, files); we need it to become a living, evolving resource cultivated alongside client meetings, user research, and data updates — and structured so AI can navigate it. *(2026-05-20)*

**Assumption**: between quality skills and quality context, the more valuable (and harder to build and maintain) is the context. This is especially valid for product work because workflows are less defined and deterministic. 

The better context we build at project level, the better AI outcomes

**Goal for next 30 days** - Build guidance for PLs and DLs how to jointly build project context. Work with champions to define good practice.

**How will the output look like**: description of context structure, principles and workflows

**Next Steps**

* Interview colleagues from DMT, Open Loop, EPP (Learning Spring sharing their knowhow at the end of discovery) (add NPM? - Petr + Eda) — Matej (2026-05-20) plans to address this via 1:1s with DMT and project teams to gather inputs on context-window structure; owner + timeline to be confirmed at next sync
* Define "What does a good context look like" + which workflows (and information flow) it needs to support, and how to keep it up to date through regular project work
* Present approach to DMT for broader organizational alignment
* Test principles on a concrete project

### Pillar 2— Collect discovery skills/plugins/prompts

* collection completed for Product, ongoing for Design, part in AI Skills Library
* testing, experimenting

### Pillar 3— Create skills out of methodology (plugin)

* ongoing testing by EPP, Matěj, Vilém

**Next Steps**

* Starting with demand, define skills which should be included, to avoid huge library people would not be familiar with
* Include only skills tested on projects
* Decide: should skills follow methodology flow, or should OLW methodology serve as a checklist on top, allowing for flexibility?

### Merging design + product

- [ ] [**AISG-154**](https://linear.app/oakslab/issue/AISG-154) Merge Design + Product AI initiatives into one workstream — *Denisa, Matej*
- [ ] [**AISG-161**](https://linear.app/oakslab/issue/AISG-161) Data-ready designs for dev handover *(design × delivery — distinct from design × discovery merge above)* — *Denisa, Honza*

### Skills & methodology

- [ ] [**AISG-140**](https://linear.app/oakslab/issue/AISG-140) Compile/document AI Skills for product discovery (with Dani on LS) — *Matej*
- [ ] [**AISG-79**](https://linear.app/oakslab/issue/AISG-79) Product skills — discovery / pm-review → inputs for design — *Kryštof*
- [ ] [**AISG-110**](https://linear.app/oakslab/issue/AISG-110) Discovery Plugin based on OAK'S LAB WAY (Coach agent + activity skills + MCP) — *Vilém*
- [ ] [**AISG-117**](https://linear.app/oakslab/issue/AISG-117) Product Sync skill — *Vilém*

### Design work

- [ ] [**AISG-86**](https://linear.app/oakslab/issue/AISG-86) Product Discovery AI-Agentic workflow — *Kseniia*
- [ ] [**AISG-87**](https://linear.app/oakslab/issue/AISG-87) Design Testing agents (A/B, user testing) — *Kseniia*
- [ ] [**AISG-103**](https://linear.app/oakslab/issue/AISG-103) E2E run on a specific task (PM → Designer → Claude → Figma) — *Val*
- [ ] [**AISG-72**](https://linear.app/oakslab/issue/AISG-72) EPP: PM ↔ Design ↔ Dev context sharing — *Denisa*
- [ ] [**AISG-76**](https://linear.app/oakslab/issue/AISG-76) Document EPP process — *Denisa*

### Project onboarding

- [ ] [**AISG-165**](https://linear.app/oakslab/issue/AISG-165) Onboard remaining projects into product discovery (A4 brief, deal age, etc.) — *Matej*

### Done

- [x] [**AISG-148**](https://linear.app/oakslab/issue/AISG-148) Collect skills/prompts/outputs from Product Leads — *Matej*


---

## Workstream 3 — QA AI integration (@[Kryštof Šraier](mention://b6a23b92-6f6a-4146-9ae0-e8c3d9586cb1/user/f6faa48d-1207-4f34-a5c8-a05e9703917f) )

> **Lead:** Kryštof Šraier **Status:** proposal-shaping stage. Per Andy *(2026-05-12)*: direction matters more than completeness at this point.
>
> **Strategic framing (Andy, 2026-05-12):** QA AI work can also serve as a **PM hatchery** — QA absorbs much of the pressure as soon as the development flywheel accelerates and the role naturally develops product thinking. Worth keeping this in mind as we scope the proposal.


\
- [ ] [**AISG-152**](https://linear.app/oakslab/issue/AISG-152) Develop QA Department AI Integration proposal — *Kryštof* 
- [ ] Prepra plan till thursday EOD, on friday discuss with Tonda.


---

## Workstream 4 — AI-First Operations & Skill Repository (@[Tonda Kmoch](mention://02798caa-c1e3-4f81-ade8-26432785ab88/user/ca0de915-7725-4b57-913c-24a1f2fadc10) )

> **Leads:** @[Tonda Kmoch](mention://15065518-ca4f-4924-955a-3b67d259a7e4/user/ca0de915-7725-4b57-913c-24a1f2fadc10)  + @[Andy Powell](mention://6629ddd6-c5e4-4e03-92c9-fd77db8578f0/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) 
>
> Five pillars below: 
>
> * **Outline as Knowledge Hub**
> * **DMT operations & Product Syncs (**@[Andy Powell](mention://db949031-daa8-4328-b5e0-f29e70117a35/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) **)**
> * **Meeting Intelligence**
> * **AI Skills Library + Knowledge Architecture**
> * **Commercial model — Claude subscription cost recovery (**@[Andy Powell](mention://6629ddd6-c5e4-4e03-92c9-fd77db8578f0/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) **)**

> **Communication stance for AI-first messaging (Andy, 2026-05-05):** Frame AI-first as a shift toward a **builder profile** — not as a failure for those not yet using AI. Roles are evolving toward more empowered building enabled by AI; that is the narrative for all-hands, team comms, and 1:1s.

### Pillar 4.1 — Outline as Knowledge Hub

> **Vision:** [Outline: Structure, Permissions & Migration](https://oakslab.getoutline.com/doc/outline-structure-permissions-migration-HDWixuGhVx) **Standard:** every project = its own collection with the same folder template (Brief / Meetings / Product / Engineering / Design / QA / Management) **Infra status *(2026-05-12 update from Honza)*:** GetOutline self-hosted on GCP via Terraform → easy to spin extra instances. Confluence → Outline import tested with engineering space (images / formatting / tables work; comments lost). DB moving Supabase → GCP managed this week. 2FA verification still pending with Martin/Marketa.

**Done**

- [x] [**AISG-119**](https://linear.app/oakslab/issue/AISG-119) Deploy self-hosted GetOutline on Oaks cloud — *Honza*
- [x] [**AISG-132**](https://linear.app/oakslab/issue/AISG-132) Move NPM + EPP Product Syncs to GetOutline — *Tonda*
- [x] [**AISG-124**](https://linear.app/oakslab/issue/AISG-124) Delegate People Registry maintenance — *Andy → Misa/Cristina*
- [x] [**AISG-153**](https://linear.app/oakslab/issue/AISG-153) Complete A4 intake form (manual) — *Tonda*
- [x] [**AISG-145**](https://linear.app/oakslab/issue/AISG-145) DMT review of Andy's centralized projects/status pages — *Tonda*
- [x] [**AISG-122**](https://linear.app/oakslab/issue/AISG-122) Resolve .gitignore vs Claude-ignore for DMT workspace — *Tonda*
- [x] [**AISG-113**](https://linear.app/oakslab/issue/AISG-113) Project Brief — EPP — *Michal Strapaty*
- [x] [**AISG-115**](https://linear.app/oakslab/issue/AISG-115) Project Brief — NPM — *Kryštof*
- [x] [**AISG-164**](https://linear.app/oakslab/issue/AISG-164) Distribute intake project brief template — *Tonda* *(target: start of this week, pending Masha screenshots + Kate's joining dates)*
- [x] [**AISG-163**](https://linear.app/oakslab/issue/AISG-163) Finalize Confluence → Outline decision (OSS vs paid) — *Tonda* *(decision: open-source — see Decisions log 2026-05-20)*

**In progress**

- [ ] [**AISG-120**](https://linear.app/oakslab/issue/AISG-120) Confluence → Outline migration plan (with Misa) — *Tonda* — see [CNF → GetOutline migration sheet](https://docs.google.com/spreadsheets/d/1Z562Qfko1JxYEP7qAfvQKBPsbfrLuEu-kpLDKh2mRVY/edit)

**Next up — this week** *(w/c 2026-05-18)*

- [ ] Meeting on Wednesday with execs+key CNF/GetOutline stakeholders and get GO/NOGO for the migration. Preparation: [Outline: Structure, Permissions & Migration](/doc/645dfe78-f260-4b7b-8bf5-d93f9433b22f)
  - [ ] [**AISG-155**](https://linear.app/oakslab/issue/AISG-155) GetOutline security/access/backup posture — @[Jan Barta](mention://7d0ce1d2-9cb4-47c7-ab17-36b5d579a300/user/3d44822d-6b6c-4940-b5fd-0247c72d79d6) 
  - [ ] Detailed migration plan:  [🏗️ Outline: Structure, Permissions & Migration](/doc/outline-structure-permissions-migration-HDWixuGhVx#h-9-migration-plan-and-phasing) - @[Tonda Kmoch](mention://f5f456cb-d27c-48f9-9e3b-ad5047aa4da8/user/ca0de915-7725-4b57-913c-24a1f2fadc10) 
- [ ] @[@Matej Novak](mention://8eb5e2b9-74b4-4952-a2fc-22bb7794e481/user/8ab9a6b6-6b83-4aa5-830e-aafdf8f20b5a) @[@Kryštof Šraier](mention://0c606bc0-0a3f-436a-bd17-681b71610b23/user/f6faa48d-1207-4f34-a5c8-a05e9703917f) create Project Brief for following projects (see [slack](https://oaks-lab.slack.com/archives/G0159HZA7LZ/p1779098212452009)):
  - [ ] Reservoir
  - [ ] DealSage
  - [ ] Blackpoint
  - [ ] Storyvine
- [ ] @[@Tonda Kmoch](mention://4c41a259-9fd1-49ab-a38d-4ffe8497569a/user/ca0de915-7725-4b57-913c-24a1f2fadc10) missing Project Brief from Learning Spring
- [ ] Investigate Outline's template feature as a standardization mechanism for project documentation structure (Brief / Meetings / Product / Engineering / Design / QA / Management) — *Tonda* *(from 2026-05-20)*
- [ ] Define Confluence access retention policy post-migration: keep read access for historical reference, revoke seat-based access to reduce costs once migration is confirmed successful — *Tonda* *(from 2026-05-20)*
- [ ] [**AISG-156**](https://linear.app/oakslab/issue/AISG-156) Finalize AI-First Ops Linear template — *==I'd not do this now, I'd use this document instead==*

  \

### Pillar 4.2 - **DMT operations & Product Syncs (**@[@Andy Powell](mention://94c616f4-dd9e-48c1-a08c-65a48b7c6a7c/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) **)**


:::warning
TODO @[Andy Powell](mention://2b47f263-90eb-435c-9952-309e8fd0274f/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) 

- [x] [**AISG-129 **](https://linear.app/oakslab/issue/AISG-129)*(urgent)* Migrate Product Sync tasks + historical transcripts from Asana to GetOutline — *Tonda - **this now goes on Andy  ***
- [ ] [**AISG-158**](https://linear.app/oakslab/issue/AISG-158) Stand up DMT meeting workflow standard — *Tonda* *(default curator: Johan Winberg) - **here as well***
- [x] @[Johan Winberg](mention://df63fe45-17b8-41c2-a760-cc2c29b17f7e/user/4f06362d-e369-462a-be37-622a52f273bd) to process transcripts for OLH Intake + RCM & Learningspring this week as PoC (Move to PMs in future)
- [ ] @[DMT](mention://881029cc-cff0-41a7-b2f2-2b3d747aed23/group/6ee0a023-561c-4264-a7ba-d24efd30b8fb) to provide feedback on what they require from [Projects Dashboard](/doc/dd962141-399b-416a-a57c-f18aea11a420) pages, and what is missing by next Friday
- [ ] @[Johan Winberg](mention://1b961c05-2aaa-4c4a-a4b2-2a25f3d772d1/user/4f06362d-e369-462a-be37-622a52f273bd) & @[Andy Powell](mention://990faadc-865e-4f31-b7ea-50c127bd5227/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) Set up SoPs and processes for meetings and use as a basis for skills. Ops-first, then AI :) 
- [ ] DMT info architecture pattern (Andy, 2026-05-20): two sources of truth by altitude — Project Hub in [Projects Dashboard](/doc/dd962141-399b-416a-a57c-f18aea11a420) at DMT level + Product Sync parent page at team level; "waterboarding" prompt pattern keeps both auto-updated from meeting transcripts so humans don't maintain them by hand. Owners: @[Andy Powell](mention://fe102cd4-71ef-4749-8dbb-95e2feb52dc2/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) (design + rollout) + @[Johan Winberg](mention://520d09b5-4aa1-4b08-b6dd-f878ef3f2cdd/user/4f06362d-e369-462a-be37-622a52f273bd) (default curator / operator)

:::

**Proposed Approach:**

* Source of Truth is Project Hub in [Projects Dashboard](/doc/dd962141-399b-416a-a57c-f18aea11a420) (DMT Level) & [Product Syncs](/collection/1e48494e-e80f-4f5a-b232-f0e479df7bd6) (Team Level)
* PoC from processing Waterboarding yesterday: [Waterboarding— 2026-05-20](/doc/14193069-6df9-49cd-a5d9-6437cda703fa) 
* MVP
  * @[Johan Winberg](mention://520d09b5-4aa1-4b08-b6dd-f878ef3f2cdd/user/4f06362d-e369-462a-be37-622a52f273bd) to process transcripts for OLH Intake+RCM & LearningSpring this week and store in the correct place…

 ![](attachments/f9ab43b6-0d04-4141-8050-a1b045d76bec.png " =1536x1279")

### Pillar 4.3 — Meeting Intelligence

> **Vision:** [Meeting Intelligence Pipeline](https://oakslab.getoutline.com/doc/meeting-intelligence-pipeline-hXloRPcmah) **Standard:** Gemini = default. Granola = fallback for non-Google platforms. Every meeting → transcript → project's Outline `Meetings/` folder. Sensitive meetings stay out of Outline. **Current state:** A script runs every 15 min and pushes meeting notes into SR Meetings, DMT Meetings, and Product Syncs folders. Andy + Tonda are designing a simpler replacement (recurring skill, run per-meeting by curator).

**Done**

- [x] [**AISG-125**](https://linear.app/oakslab/issue/AISG-125) Adopt Gemini as default transcript standard (Granola fallback) — *Tonda*
- [x] [**AISG-130**](https://linear.app/oakslab/issue/AISG-130) Automated transcript → GetOutline pipeline for Product Syncs — *Tonda*
- [x] [**AISG-105**](https://linear.app/oakslab/issue/AISG-105) Granola/Gemini → MD → GetOutline e2e flow (TS script) — *Tonda*

**Next up**

- [ ] [**AISG-162**](https://linear.app/oakslab/issue/AISG-162) I was wrong with expecting that `transcript+get_outline_collection_id@oakslab.com` invite will work. We need to change it to `transcript@oakslab.com` and have the collectionId in the GCalendar invite - @[Tonda Kmoch](mention://9877f884-dc9b-4915-8bff-63efe5fe03b4/user/ca0de915-7725-4b57-913c-24a1f2fadc10) 
- [ ] Replace Gemini generated summary with OAK'S + project specific summary (have own system prompt for every meeting/project) - @[Tonda Kmoch](mention://f2c60865-d1b3-463e-b67b-7148231598a8/user/ca0de915-7725-4b57-913c-24a1f2fadc10) to learn how @[Andy Powell](mention://b571cdcc-9eb2-4415-902d-6c8fee46deb6/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) is doing that. Likely we may use DMT (or even better …. Product Syncs) as first PoC.

**Next steps**

> I think the only thing we should align+insist is: All the project meetings need to get to GetOutline. How it is up to the Leading Trio.

Status:

* Product Sync & DMT meetings - ✅ already using the script
* NPM
* OLH Intake - ✅ already using the script
* OLH RCM - ⏳ waiting for the transcript@oakslab.com fix
* Reservoir
* EPP
* Learning Spring
* Deal Sage
* Blackpoint
* Narwhal

### Pillar 4.4 — AI Skills Library + Knowledge Architecture

> **Vision:** [AI Skills Library](https://oakslab.getoutline.com/doc/ai-skills-library-RT4N6AzxWN) · [AI Knowledge Architecture](https://oakslab.getoutline.com/doc/ai-knowledge-architecture-k4tvpI7UTG) **Standard:** every project pushes `.claude/` to Outline via `/oaks-outline-push`; common skills distributed via git repo `oakslab/claude-skills-library`. Three info tiers: project (public) → DMT (shared) → private (local). Don't try to unify project skills *(decision 2026-05-12)* — share summary + skills across teams instead.

**Done**

- [x] [**AISG-148**](https://linear.app/oakslab/issue/AISG-148) Collect skills/prompts/outputs from Product Leads — *Matej* *(also feeds Workstream 2)*
- [x] [**AISG-133**](https://linear.app/oakslab/issue/AISG-133) Tonda + Kuba 1:1 — AI activities update — *Tonda*
- [x] [**AISG-146**](https://linear.app/oakslab/issue/AISG-146) Review Intake project brief manually — *Tonda*

**Next up**

- [ ] [**AISG-151**](https://linear.app/oakslab/issue/AISG-151) Create signpost/summary docs from team AI usage meetings — @[@Tonda Kmoch](mention://6df3de32-b6c0-4398-a2b1-19fa2ca67ef0/user/ca0de915-7725-4b57-913c-24a1f2fadc10) 
- [ ] [**AISG-111**](https://linear.app/oakslab/issue/AISG-111) *(parent, blocked — children below running)* Project Brief + Document Project AI Skills — *Tonda*
  - [x] [**AISG-112**](https://linear.app/oakslab/issue/AISG-112) OLH Intake — *Vilém* *(urgent, in progress)*
  - [ ] [**AISG-114**](https://linear.app/oakslab/issue/AISG-114) Learning Spring — *Kuba Šlambora* *(urgent, in review)*
  - [ ] [**AISG-116**](https://linear.app/oakslab/issue/AISG-116) OLH RCM — *Anastasiia* *(urgent, todo)*


- [ ] [**AISG-136**](https://linear.app/oakslab/issue/AISG-136) Pick propagation mechanism (sparse checkout) for AI Boilerplate — *Honza*
- [ ] [**AISG-138**](https://linear.app/oakslab/issue/AISG-138) Approval process for skills/commands in AI Boilerplate — *Tonda*

### Pillar 4.5 — Commercial model: Claude subscription cost recovery (@[Andy Powell](mention://6629ddd6-c5e4-4e03-92c9-fd77db8578f0/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) )

> **Lead:** @[Andy Powell](mention://6629ddd6-c5e4-4e03-92c9-fd77db8578f0/user/612827bb-3c41-47aa-ac34-ed1cecf30bbe) *(model agreed with Martin, 2026-05-05)*
>
> **Model:** Double-bill 1–2 people per project to cover the cost of Claude subscriptions used on that project. **Transfer Claude ownership to the client wherever possible** — same pattern we already use for Jira: the subscription is held by the client, not by us. **No real downside** as context and skills remain available locally (in repos / Outline / our own tooling), so handing the subscription seat to the client doesn't fragment our knowledge or process.
>
> **Why it matters:** As AI tool spend scales, we need a clean commercial answer that doesn't eat into margin and doesn't require constant per-project negotiation.

**Next up**

- [ ] Document the model formally (one-pager for PMs and DMT) — *Andy*
- [ ] Define rollout: which existing projects move to client-owned Claude first; how it's framed in MSA / SOW conversations — *Andy*
- [ ] Align with [**AISG-142**](https://linear.app/oakslab/issue/AISG-142) (Methodology for AI tool subscriptions) so internal "who gets what" and external "who pays" are consistent — *Andy*


---

## Operating model — team & capacity

- [ ] [**AISG-142**](https://linear.app/oakslab/issue/AISG-142) Methodology for AI tool subscriptions (who gets what) — *Andy*
- [x] [**AISG-166**](https://linear.app/oakslab/issue/AISG-166) Each workstream owner converts AI priority area into a 2-week deterministic plan with target outcome — *Honza, Matej, Kryštof, Denisa, Tonda* *(superseded by the adopted 2–3 week cadence — see Decisions log 2026-05-20)*


---

## Decisions log (confirmed)

* **2026-04-16** — Start with MD files in Outline; revisit only if scale demands it (no premature RAG)
* **2026-04-16** — Pilot-first rollout (Learning Spring confirmed as first pilot)
* **2026-04-24** — Gemini = default transcript tool company-wide; Granola = fallback for non-Google platforms
* **2026-04-24** — Sensitive meetings (1:1s, performance, hiring) stay out of Outline
* **2026-05-12 (All-Hands)** — Four priority workstreams + owners agreed (Engineering · Product Discovery · QA · AI-First Ops)
* **2026-05-12 (All-Hands)** — Engineering rules: every team uses a curated AI skills library; every project has `.md` foundations (architecture · tech · folder structure · key patterns · data model); engineering all-hands runs regularly with "how we use AI" + "how we built this project" themes
* **2026-05-12** — Don't try to unify project AI skills now; share summary + skills across teams instead
* **2026-05-15** — Outline is the source of truth for meeting transcripts. Curate next steps in Outline first, then propagate to Linear/Asana via skill
* **2026-05-15** — Johan Winberg is the default curator for DMT meetings (Tonda runs it interim)
* **2026-05-15** — calendar-invite-based `transcript+...@oakslab.com` approach abandoned; replaced by a simpler recurring skill (Tonda × Andy Monday sync, AISG-162)
* **2026-05-20** — **Planning rhythm:** 2–3 week deterministic cycles adopted as the standard planning horizon (replaces long-horizon planning). Each cycle has specific deadlines and success criteria. Replaces AISG-166 as a recurring practice.
* **2026-05-20** — **Outline edition:** open-source version of Outline confirmed. Paid version is not needed; 2FA at the Outline level is not required because Google Workspace SSO is sufficient. Migration proceeds on the self-hosted instance.

## Open decisions / blockers

* **#1 risk: Kuba's engineering capacity** — Workstream 1 throughput depends on this. Squad-roster plan in flight ([AISG-160](https://linear.app/oakslab/issue/AISG-160), [AISG-134](https://linear.app/oakslab/issue/AISG-134))
* Andy's "AISG running in circles" concern — addressed by the adopted 2–3 week cadence (Decisions log 2026-05-20)
* Confluence migration content scope — most teams missed the input deadline; Tonda chasing this week
* Hosting for the recurring transcript skill — Cloud Run / cron / on-demand (decision needed from Tonda × Andy Monday sync)
* Retention policy for transcripts in Outline
* GetOutline security / access / backup posture — [AISG-155](https://linear.app/oakslab/issue/AISG-155) *(blocked, Honza)*


---

## Sources

* [DMT Vision: AI-First Operations](https://oakslab.getoutline.com/doc/dmt-vision-ai-first-operations-e9PKZMwV1w)
* [Outline: Structure, Permissions & Migration](https://oakslab.getoutline.com/doc/outline-structure-permissions-migration-HDWixuGhVx)
* [Meeting Intelligence Pipeline](https://oakslab.getoutline.com/doc/meeting-intelligence-pipeline-hXloRPcmah)
* [AI Knowledge Architecture](https://oakslab.getoutline.com/doc/ai-knowledge-architecture-k4tvpI7UTG)
* [AI Skills Library](https://oakslab.getoutline.com/doc/ai-skills-library-RT4N6AzxWN)
* [2026-05-12 — AI DMT Sync prep (All-Hands workstream split)](https://oakslab.getoutline.com/doc/2026-05-12-ai-dmt-sync-prep-LfmQNc0SOD)
* [2026-05-15 — AI DMT Sync prep](https://oakslab.getoutline.com/doc/2026-05-15-ai-dmt-sync-prep-KJClq0yM0z)
* [2026-05-15 — DMT AI Sync (full transcript)](https://oakslab.getoutline.com/doc/2026-05-15-dmt-ai-sync-CqvXbx9dvX)
* [AISG current sprint in Linear](https://linear.app/oakslab/team/AISG/view/current-sprint-e5a50ec2dbfe)
* [CNF → GetOutline migration sheet](https://docs.google.com/spreadsheets/d/1Z562Qfko1JxYEP7qAfvQKBPsbfrLuEu-kpLDKh2mRVY/edit)