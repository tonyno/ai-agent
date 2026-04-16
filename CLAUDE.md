# DMT - Tonda Kmoch @ Oaks Lab

This workspace is used for brainstorming and digital management team (DMT) work at Oaks Lab.

## About Oaks Lab

**Oaks Lab** is an outsourced software development company founded in 2016 in Prague, Czech Republic, by Czech-American brothers **Jake and Theo Dluhy-Smith**. The company connects American companies with elite Czech development talent. Built without investor backing, it has grown to 85+ team members and launched 65+ client products (80% US-based clients).

**Mission:** Empower innovators to improve life and the world.
**Vision:** Become a hub of groundbreaking global innovation.

### Core Services

1. **Product Discovery & Design** - Market analysis, user research, product requirements, competitive analysis, high-fidelity Figma designs
2. **Software Development** - Full-stack JavaScript/TypeScript specialization: Next.js, React.js, React Native, Node.js
3. **AI & Agentic Systems** - LLM integration, RAG, AI orchestration, autonomous workflows (Python)

### Engagement Models

- **Autonomous Teams** - Cross-functional units (PM, design, engineering, QA) handling end-to-end product development
- **Staff Augmentation** - Individual specialists embedded into client teams

### Industries Served

FinTech, Cybersecurity, FoodTech, EdTech, HR Tech, PropTech, E-commerce, Real Estate & Investment, Media & Entertainment

### Tech Stack

- **Frontend:** TypeScript, React, Next.js, Material UI, Firebase
- **Backend:** Node.js, TypeScript, Prisma, tRPC, Firebase
- **DevOps:** Google Cloud, PostgreSQL, Docker, GitHub CI/CD
- **AI:** Claude, ChatGPT, Llama, Hugging Face, Stable Diffusion, Google Vertex
- **Design:** Figma, Adobe Creative Cloud, Webflow, Lovable
- **PM Tools:** Jira, Confluence, Miro, Google Workspace
- **QA:** QASE, Playwright, Postman

### Leadership

| Name | Role |
|------|------|
| Jake Dluhy-Smith | CEO & Co-Founder |
| Theo Dluhy-Smith | Executive Director & Co-Founder |
| Andy Powell | Partner & COO |
| Martin Klikar | Partner & CFO |
| Tonda Kmoch | Delivery |
| Denisa Lorencova | Design |
| Vladimir Rehor | Engineering |
| Igor Tadic | Product Management |
| Sean Smyth | Talent Acquisition |

### Company Values

1. Strive for excellence
2. Prioritize outcomes over outputs
3. Deliver quality
4. Practice honesty
5. Demonstrate kindness
6. Maintain positivity through challenges

### Key Credentials

- ISO 27001 certified
- 5.0/5.0 Clutch rating (31 reviews)
- 89% client retention post-contract
- Top 0.4% of job applicants hired
- Helped startup clients raise over $200M
- Featured at TechCrunch Disrupt (2023)

## The OAK'S LAB WAY (Methodology)

The OAK'S LAB WAY is our product development methodology designed for empowered product teams to take a startup's product from initial concept to product-market fit and scale. It is a living document built from know-how gained building 65+ startups.

Full documentation: https://oakslab.getoutline.com/collection/the-oaks-lab-way-jYXeZKKxiP

### Product Principles

These are the guiding values for how all standards in the methodology should be applied:

1. **User obsession** - Constantly striving to deliver great products for users as fast as possible. Always ensure a path to gain customer insights quickly and leverage them when building.
2. **Success equals outcomes, not outputs** - Success is defined by startups' success. Build to deliver highest value to users, and through that, highest business value. Function over form.
3. **Stay lean & don't reinvent the wheel** - Be lean, run fast without sacrificing long-term scalability. Leverage reusability and component-based development. Use proven technologies. Leading edge, not bleeding edge.
4. **Relentless focus** - The main thing is to keep the main thing, the main thing. Use goals as north star, prioritize ruthlessly.
5. **Discipline fosters innovation** - Leverage battle-tested processes to build great products. Committing to methodology creates time and space for innovative solutions.

### Structure

The methodology is organized into four pillars:

- **Roles & Responsibilities** - Expectations for each core team member
- **Activities** - All potential project activities with standards, ownership, templates, and examples
- **Tools** - Supporting software and best practices
- **Project Health Check** - Weighted measurement of adherence to highest-priority activities (scored 0-3 per activity, measured each sprint)

### Team Composition

The core team is a leading trio: **Product Manager (PM)**, **Tech Lead (TL)**, and **Design Lead (DL)**. PM holds ultimate accountability for the stakeholder's product success. The trio joins first during the Foundation Phase, then **QA Analyst** and **Software Engineers** are added.

### Development Process & Project Phases

1. **Sales Process & Kick-Off** - Entry analysis, team onboarding, virtual office setup, documentation setup, initial project plan, kick-off call
2. **Foundation Phase** - Business & user understanding, strategic direction, product requirements & scope capture, technical setup, design setup, planning remaining phases. Each foundation milestone must be **reviewed and approved by a DMT member**.
3. **Dual-Track Agile (Discovery & Delivery)** - Continuous discovery alongside delivery. Sprint-based work with velocity checks, milestone tracking, and regular stakeholder alignment via steering committees.
4. **UAT & Rollout** - Cyclical testing with stakeholder, rollout preparation
5. **Production Support / Maintenance** - Scaled-down team, pre-agreed SLA

### Activity Categories

- **Project Setup** - Planning and kicking off new projects
- **Managing the Project** - Project plan/roadmap, sprint planning, progress tracking, reporting & stakeholder alignment, velocity, SOW management, documentation, decision log, cross-company collaboration
- **Discovery** - Business & user understanding, business & product strategy, scope discovery (user journeys + wireframes), specifications & tickets, product design, foundation-specific activities
- **Product Design** - Design activities spanning discovery and delivery
- **Delivery** - Developing, testing, and releasing working software (code quality, code review, PRs, branching model, CI/CD, release model, testing strategy, DevOps, security, cloud configuration)

### Key Milestones (Dual-Track Phase)

- Review of first high-fidelity designs (end of Foundation)
- First Steering Committee (end of Foundation)
- Scope/Roadmap approved by stakeholder (end of Foundation)
- Velocity check (2 sprints into delivery)
- Staging environment setup (2 sprints into delivery)
- Test Strategy created (1 sprint after QA joins)
- SOW 2 plan defined (75 days before end of SOW)
- Rollout Strategy finalized (1 month before UAT/Rollout)
- Development complete, Release date, End of SOW

### Project Health Check

Measures current and future project success against OAK'S LAB WAY standards. 20 categories measured each sprint, weighted by importance. Scoring scale:
- **0** - Not following standards, situation is critical
- **1** - Not following standards, no large risk yet
- **2** - Following most standards, acceptable but could be better
- **3** - Following standards, situation is good (or credible alternative fulfilling the goal)

Measured prior to each product sync by the product's leadership team.

## Outline Integration

This workspace uses Outline as the source of truth for all documentation.
Local file `outline-index.md` is an index of tracked collections and their documents.

**Rules:**
- Always read `outline-index.md` at the start of a conversation to know what's available in Outline
- Content always comes from Outline via MCP — never cache document content locally
- Use the index summaries to decide which documents to fetch for the current task
- To refresh the index: run `/pull-outline-index`
- To track a new collection: add it to the Tracked Collections table in `outline-index.md`, then run `/pull-outline-index`
- To fetch a document: use `mcp__claude_ai_GetOutline__fetch` with the document ID from the index

## Role Context

**Tonda Kmoch** - Delivery lead and member of the Digital Management Team (DMT). This workspace supports brainstorming, planning, and execution of DMT responsibilities including delivery management, process improvement, methodology oversight, and team coordination. DMT members review and approve Foundation Phase milestones on projects.

## Working Conventions

- Language: English (default), Czech when requested
- Focus on actionable outcomes, not just ideas
- When brainstorming, explore multiple angles before converging
- Keep outputs practical and aligned with Oaks Lab's services and the OAK'S LAB WAY methodology
- For methodology details, reference the Outline collection via MCP when deeper context is needed
