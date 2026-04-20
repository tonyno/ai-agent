# {Project Name} — Project Brief

> **Last updated:** {YYYY-MM-DD} | **Author:** {name}

<!--
  HOW TO USE THIS TEMPLATE
  ========================
  This is the canonical Project Brief template for the startup studio.
  Every project should have exactly one Project Brief file that serves as the entry point
  for anyone — CEO, PM, designer, engineer, QA — wanting to understand the project.

  FILLING RULES:
  - Replace every {placeholder} with real content from project documentation.
  - If information is not available, write "TBD" — never leave a field blank.
  - If a whole section does not apply (e.g., no testing for a discovery project),
    write "N/A — project is in discovery phase" under the section heading.
  - Keep each field scannable: 1-2 sentences max unless the annotation says otherwise.
  - The entire document should be readable in under 5 minutes.

  AUDIENCE GUIDE (which sections matter most for each role):
  - CEO / COO / Investor  → 1, 2, 8, 9, 10
  - Product Manager       → 1, 2, 3, 4, 5, 6, 7, 8, 9
  - Designer              → 3, 4, 5, 6, 14
  - Tech Lead / Engineer  → 5, 12, 13, 15
  - QA                    → 5, 13, 15
-->

---

## 1. Project Identity

<!--
  The "business card" of the project. A reader should understand
  what this project is after reading just this table.
-->

| Field              | Value |
|--------------------|-------|
| **One-liner**      | {What the product does + for whom + why it matters, in 1 sentence. Good: "HIPAA-compliant no-code funnel builder for telehealth patient intake." Bad: "A platform for healthcare."} |
| **Industry**       | {Sector slash tags — e.g., "B2B / Telehealth / SaaS" or "Consumer / Family Tech / Digital Preservation"} |
| **Client**         | {Company name + relationship type. Types: agency / direct client / partnership / own product. E.g., "OpenLoop — direct client" or "Internal — own product". If the client has a website, add the link here} |
| **Platform**       | {Where the product runs — e.g., "Web (mobile-first)" or "Web + iOS + Android" or "SaaS multi-tenant web app"} |
| **Initial Market** | {Geography and/or customer segment — e.g., "US telehealth providers" or "Czech Republic, Czech-speaking families"} |
| **Stage**          | {One of: Pre-MVP / MVP / Post-launch / Growth / Maintenance / On Hold / Completed} |
| **Current Phase**  | {What is happening right now — e.g., "Phase 2 of 3 — Enhancement sprint" or "Product Discovery — survey validated, pre-MVP"} |

---

## 2. Problem Statement

<!--
  The "why" of the project. 2-4 sentences answering:
  - What pain exists?
  - Who feels it?
  - Why do current solutions fail?

  Source this from: product briefs, README, kick-off decks, discovery docs.
  If no formal problem statement exists, write what is known and mark gaps.
-->

{Core problem description. E.g., "Telehealth companies use fragmented, non-compliant tools (Google Forms, TypeForm) for patient intake. Each new client requires custom development, costing weeks of engineering time. No existing solution combines clinical protocol compliance, white-labeling, and no-code configuration."}

### Validated Problems

<!--
  List 2-4 top problems, ranked by evidence strength.
  - "Evidence" = how you know this is real (survey data, interview count, client feedback, or "assumed").
  - "Status" = Validated (strong evidence) / Partially Validated (some evidence) / Assumed (no direct evidence).
  If the project has no formal research, mark all as "Assumed" — that's still useful information.
-->

| # | Problem | Evidence | Status |
|---|---------|----------|--------|
| 1 | {Problem statement — 1 sentence} | {Data source — e.g., "75% top-2-box in survey (n=309)" or "3 client interviews" or "stakeholder assertion"} | {Validated / Partially Validated / Assumed} |
| 2 | {Problem} | {Evidence} | {Status} |

---

## 3. Target Audience

### Primary Persona

<!--
  The single most important user archetype. Fill from persona docs, user research,
  or product briefs. If multiple personas exist, pick the one whose satisfaction
  determines product success.
-->

| Attribute | Detail |
|-----------|--------|
| **Name / Archetype** | {A memorable label — e.g., "Family Champion" or "Client Configurer (Alastor)". If the project has named personas, use those names.} |
| **Demographics**     | {Age range, role, context in 1 sentence — e.g., "Mid-level marketing/ops person at a digital health company, manages 1-5 funnels"} |
| **Digital Literacy**  | {One of: Power user / Comfortable / Basic smartphone user — helps calibrate UX expectations} |
| **Primary Goal**      | {What they want to achieve — e.g., "Get a compliant, branded intake funnel live without engineering help"} |
| **Key Frustration**   | {What blocks them today — e.g., "Can't tell if a funnel is ready to publish; template updates cause anxiety"} |

### Secondary Personas

<!--
  1-3 additional user types. Only include personas that meaningfully
  differ in goals or behavior from the primary. One row each.
-->

| Persona | Who They Are | Primary Goal |
|---------|--------------|--------------|
| {name/archetype}  | {1 sentence: role + context} | {their goal} |

### Ideal Customer Profile (ICP)

<!--
  For B2B: describe the buying organization (size, industry, maturity).
  For B2C: describe the ideal individual customer.
  Include market size estimate if known.
-->

{1-2 sentences — e.g., "US digital health companies running 10+ clinical programs, needing HIPAA-compliant patient onboarding at scale. Estimated TAM: ~200 companies." or "Czech families 30-65 with children, ~185K individuals. At 2% conversion = ~3,700 paying families."}

---

## 4. Product Vision 

<!--
  The north star — not features, but the aspiration.
  2-3 sentences describing what the product is trying to become.
  Explicitly state what the product is NOT to prevent scope drift.
  Source: kick-off deck, product brief, README.
-->

{E.g., "A white-labeled, no-code platform where telehealth clients configure and publish compliant patient intake funnels without engineering support. The product is NOT an EHR, NOT a scheduling tool, and NOT a CRM." or "A private, family-only story archive. NOT a social network, NOT a genealogy tool, NOT a photo gallery."}


---

## 5. Key Features

<!--
  The 5-7 features that define the product's core value.
  For pre-MVP projects: what the MVP will include.
  For live products: what's live today.
  Each row = 1 sentence. Think "feature tour for a new stakeholder."
-->

| # | Feature | Description |
|---|---------|-------------|
| 1 | {name}  | {What it does in 1 sentence — e.g., "No-code funnel builder — drag-and-drop page editor with clinical protocol templates"} |
| 2 | {name}  | {description} |
| 3 | {name}  | {description} |
| 4 | {name}  | {description} |
| 5 | {name}  | {description} |

### Out of Scope

<!--
  What the product explicitly does NOT do. This is as important as what it does.
  Prevents scope creep, aligns expectations, saves time in planning discussions.
  Source: README scope section, product brief, kick-off decisions.
-->

- {What is excluded and why — e.g., "No direct EHR integration — data flows through Patient 360 middleware"}
- {What is excluded and why — e.g., "No in-app messaging — patients communicate through their provider's existing channels"}

---

## 6. Screenshots

<!-- 
if any screenshots are available, put them here. If not, put here annotation/instructions what screenshots to put here}
--> 

---

## 7. Competitive Landscape

<!--
  3-5 closest alternatives the target audience might use instead.
  Be honest about where competitors are strong — credibility matters.
  Source: product brief, market research, stakeholder conversations.
  If no competitive analysis exists, write "TBD — no formal competitive analysis conducted" and list known alternatives.
-->

| Competitor | Positioning | Key Weakness vs. This Product |
|------------|-------------|-------------------------------|
| {name}     | {What they do — 1 sentence} | {Why they fall short for our specific use case} |

**Our differentiators:**

1. {What we do that competitors don't — e.g., "Clinical protocol templates with locked structure — competitors offer generic forms without compliance guardrails"}
2. {differentiator}
3. {differentiator}

---

## 8. Business Model & Metrics

### Revenue Model

<!--
  How money flows. For client projects: how the client pays us.
  For own products: how the product generates revenue.
  "Key Assumptions" = what must be true for this model to work.
-->

| Field | Value |
|-------|-------|
| **Model**           | {E.g., "B2B SaaS" or "Fixed-price delivery" or "T&M engagement" or "B2C freemium subscription"} |
| **Pricing**         | {Structure, not exact numbers — e.g., "Per-client tiered pricing" or "Annual per-family subscription" or "T&M at agreed day rate"} |
| **Key Assumptions** | {E.g., "Clients self-serve after initial onboarding" or "Seasonal users will pay annual subscriptions"} |

### Success Metrics

<!--
  2-5 metrics that define whether this project is succeeding.
  "Target" = the goal. "Current" = latest known value.
  If no metrics are formally defined, write the most logical ones and mark targets as "TBD".
-->

| Metric | Target | Current |
|--------|--------|---------|
| {E.g., "Patient conversion rate"} | {E.g., "> 60%"} | {E.g., "58%" or "TBD — not yet measured"} |
| {E.g., "Template adoption rate"}  | {target} | {current or "TBD"} |

---

## 9. Key Risks

<!--
  Top 3-5 risks that could derail the project. Be candid — this section
  is most valuable when it's honest. Include business, product, and technical risks.
  "Mitigation" = what is being done (or should be done) to reduce the risk.
  Source: project retrospectives, stakeholder concerns, README constraints, your own assessment.
-->

| Risk | Severity | Mitigation |
|------|----------|------------|
| {What could go wrong — e.g., "Key stakeholder (Scott) leaves OpenLoop — he holds most implementation context"} | {High / Medium / Low} | {What we're doing — e.g., "Documentation in repo, regular knowledge sharing sessions"} |

---

## 10. Project Approach & Timeline

### Phases

<!--
  How the project is structured over time. Include all phases: past, current, future.
  This gives a reader the full arc of the project.
-->

| # | Phase | Status |
|---|-------|--------|
| 1 | {Phase name — e.g., "Phase 1 — Core platform (5 months)"} | {Done / In Progress / Planned} |
| 2 | {Phase name — e.g., "Phase 2 — Landing page templates (4 months)"} | {status} |

### Contract

<!--
  Engagement terms. For own products, use "Internal" for client-specific fields.
  Never include exact dollar amounts unless explicitly appropriate.
-->

| Field                  | Value |
|------------------------|-------|
| **SOW Start**          | {YYYY-MM-DD or "N/A" for own products} |
| **SOW End**            | {YYYY-MM-DD — note extensions: e.g., "2026-07-01 (extended 4 months from March 2026)"} |
| **Scope Estimation**   | {E.g., "Phase 1 = 133 engineering MDs" or "MVP = 3 months, 2 engineers"} |
| **Renewal / Extension**| {E.g., "Phase 3 under negotiation" or "Auto-renews annually" or "N/A"} |

### Milestones

*Add the link to the project timeline here*

---

## 11. People

### Internal Team

<!--
  The studio team working on this project.
  Roles: PM (project/product manager), TL (tech lead), DL (design lead),
  QA (quality assurance), EN (engineers). Omit roles with no assignee.
-->

| Role | Name | Start date - End date |
|------|------|-------|
| PM   | {name} | {when that person started, when unknown, put just dash} |
| TL   | {name} | {when that person started, when unknown, put just dash}  |
| DL   | {name} | {when that person started, when unknown, put just dash}  |
| QA   | {name} | {when that person started, when unknown, put just dash}  |
| EN   | {names, comma-separated} | {when that person started, when unknown, put just dash}  |

### Key Client / Stakeholder Contacts

<!--
  External people the team interacts with regularly.
  "Decision Domain" = what this person owns or can approve.
-->

| Name | Role | Decision Domain |
|------|------|-----------------|
| {name} | {title at their company} | {E.g., "Product requirements and feature sign-off" or "Technical integration decisions"} |

---

## 12. Architecture & Tech Stack

<!--
  For live or in-development products only.
  For discovery/pre-MVP projects, write "TBD — architecture not yet decided"
  and list any known technical constraints or preferences.
-->

### Stack

| Layer          | Technology |
|----------------|------------|
| **Frontend**   | {E.g., "Next.js 15, React 18, TypeScript, Tailwind CSS, shadcn/ui"} |
| **Backend**    | {E.g., "tRPC 11, Prisma ORM, PostgreSQL"} |
| **Auth**       | {E.g., "Firebase (email, magic links, Google OAuth, TOTP)"} |
| **Payments**   | {E.g., "Stripe" or "N/A"} |
| **Infra**      | {E.g., "GCP (Cloud Run, Cloud SQL), Terraform" or "Vercel"} |
| **Analytics**  | {E.g., "PostHog, GTM" or "N/A"} |
| **CI/CD**      | {E.g., "GitHub Actions" or "Vercel auto-deploy"} |
| **Monorepo**   | {E.g., "Turborepo + pnpm" or "single repo" or "N/A"} |

### Key Integrations

<!--
  External systems the product connects to.
  "Direction" = which way data flows.
  Omit for projects with no integrations.
-->

| Integration | Purpose | Direction |
|-------------|---------|-----------|
| {E.g., "Stripe"} | {E.g., "Payments, subscriptions, and webhooks"} | {Bidirectional / Outbound / Inbound} |

### Repo Structure

<!--
  Abbreviated top-level directory tree, 10-15 lines max.
  Helps engineers orient quickly. Omit for pre-MVP / discovery projects.
-->

```
{top-level directory tree}
```

---

## 13. Environments & Testing

<!--
  For live or in-development products only.
  For discovery/pre-MVP: write "N/A — no deployed environments yet."
-->

### Environments

| Environment | URL | Notes |
|-------------|-----|-------|
| Production  | {url or "N/A"} | {E.g., "Client-facing, requires auth"} |
| Staging     | {url or "N/A"} | {E.g., "Internal testing, mirrors prod"} |
| Dev / Local | {setup instructions link or brief command — e.g., "See README, `pnpm dev`"} | |

### Testing Approach

<!--
  How quality is ensured. Include tools, process, and who is responsible.
-->

| Aspect                | Value |
|-----------------------|-------|
| **E2E Tool**          | {E.g., "Playwright" or "N/A for discovery phase"} |
| **Unit / Integration**| {E.g., "Jest + React Testing Library" or "N/A"} |
| **Test Environments** | {Where tests run — e.g., "CI on every PR, nightly against staging"} |
| **QA Process**        | {1-2 sentences — e.g., "Manual QA on staging per ticket, E2E regression in CI, release validation by QA lead before deploy"} |

---

## 14. Design & Brand

<!--
  Links to design assets. Designers and engineers both need these.
  For projects without design work yet, mark as "TBD".
-->

| Resource          | Link |
|-------------------|------|
| **Figma**         | {Link to main Figma file or design space — e.g., "https://figma.com/file/..."} |
| **Design System** | {Link to component library, or "embedded in Figma", or "uses shadcn/ui defaults"} |
| **Brand Guide**   | {Link to brand guidelines, or "see Figma", or "N/A — no brand yet"} |
| **Typography**    | {Font names — e.g., "Inter (UI), Merriweather (content)" or "see Figma"} |
| **Website**       | {Product URL or client's marketing website} |

---

## 15. Key Links

<!--
  Master reference table. The "bookmarks bar" for this project.
  Remove rows that don't apply. Add project-specific rows if needed.
-->

| Resource              | Link |
|-----------------------|------|
| **Project Tracker**   | {Linear / Jira / Asana URL — e.g., "https://linear.app/org/team/..."} |
| **GitHub Repo**       | {repo URL} |
| **GDrive**            | {Shared folder URL} |
| **Confluence / Wiki** | {URL or "N/A"} |
| **Proposal / SOW**    | {Link to contract document} |
| **Architecture Docs** | {Link — e.g., "docs/architecture.md in repo" or external URL} |
| **API Docs**          | {Link, or "tRPC self-documenting", or "Swagger at /api-docs"} |
| **Release Notes**     | {Link to release notes — in-app or in-repo} |
| **Client Docs**       | {Link to client-facing documentation} |
| **Kick-off Deck**     | {Link to kick-off presentation} |
| **Miro / Whimsical**  | {Link to collaboration boards, or "N/A"} |
| **User Research**     | {Link to survey results, interview notes, discovery docs, or "N/A"} |
