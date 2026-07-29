# Build Specification: Product Discovery Harness

## Instructions for Codex

Build a complete, production-quality repository in the current working directory that implements the **Product Discovery Harness** described in this document.

This is not a request for an architecture proposal or a partial prototype. Create the actual repository: skills, scripts, templates, schemas, installer, update/status commands, tests, fixtures, CI configuration, version metadata, changelog, and complete documentation.

Use the public repository below as a **behavioral and structural reference**, especially its operating model, skill packaging, installer behavior, bootstrap/validation approach, and `SKILL.md` conventions:

- `https://github.com/Simon-Initiative/harness`

Do **not** make the Product Discovery Harness depend on private functions or implementation details from that repository. Do not copy code verbatim unless its license clearly permits it. Reimplement the required behavior cleanly.

Before implementing:

1. Inspect the current structure and behavior of `Simon-Initiative/harness`.
2. Write a brief internal implementation plan.
3. Build the repository in coherent increments.
4. Run all tests and validation commands.
5. Fix failures before considering the task complete.
6. Finish with a summary of the repository created, the important design decisions, commands executed, and test results.

Do not leave important behavior as TODOs. Templates may intentionally contain prompts/placeholders because they are templates, but executable behavior, validation, installation, and documentation must be complete.

---

# 1. Product name and purpose

Use the repository/project name:

```text
product-discovery-harness
```

The repository is an **installable, reusable harness for agent-assisted product discovery and product definition**.

It sits conceptually above the engineering Harness:

```text
Product Discovery Harness
    conversation
    current-product archaeology
    product strategy
    experience strategy
    opportunities
    UX concept exploration
    feature crystallization
    release definition
            ↓
      documented handoff
            ↓
Engineering Harness
    PRD
    architecture
    implementation plan
    development
    verification
```

The Product Discovery Harness helps a product owner think through and document:

- what product should exist;
- who it serves;
- what user outcomes it should enable;
- what an existing product currently does;
- what should be kept, removed, redesigned, merged, split, or newly introduced;
- what the product should feel like to use;
- what interaction alternatives should be explored;
- which opportunities should become concrete features;
- how those features should be grouped into outcome-oriented releases;
- when a feature is sufficiently defined to enter the engineering Harness.

The primary interface is **conversation with an agent**. The durable memory and source of truth are **versioned files in the target product repository**.

---

# 2. Core operating model

The Product Discovery Harness must follow this operating model:

1. This repository contains reusable skills, scripts, templates, schemas, personas, and validation logic.
2. It is installed once into the user's agent skill directories.
3. The user opens a separate target repository:
   - a new repository for a new product; or
   - an existing application repository that needs to be understood and redefined.
4. The user invokes Product Discovery Harness skills from inside that target repository.
5. The skills create and maintain product-discovery documents inside the target repository.
6. The target repository becomes the durable system of record.
7. When a feature is ready, the Product Discovery Harness creates a file contract compatible with the engineering Harness.
8. The engineering Harness consumes that handoff and handles product requirements, architecture, planning, implementation, and validation.

The reusable harness repository and target product repository must stay separate:

```text
~/.local/share/product-discovery-harness/
    reusable installed repository

~/projects/example-product/
    application code
    product-discovery documents
    engineering plans
```

Do not install or copy the Product Discovery Harness repository into every target application.

---

# 3. Design principles

The implementation must embody these principles.

## 3.1 Conversation is the interface

The product owner should not need to arrive with a structured specification or fill out a long questionnaire.

The agent must support a long-running, iterative conversation in which the user can provide:

- incomplete thoughts;
- contradictory ideas;
- frustrations;
- references;
- product ambitions;
- doubts;
- descriptions of current behavior;
- possible features;
- desired feelings or qualities;
- examples of products or interactions they admire.

The agent must help organize, challenge, clarify, synthesize, and document those ideas.

## 3.2 Repository files are the memory

The chat transcript is not the canonical product specification.

The target repository must contain:

- stable decisions;
- working hypotheses;
- open questions;
- assumptions;
- session summaries;
- current-product evidence;
- opportunity briefs;
- UX concepts;
- selected product directions;
- feature definitions;
- release definitions;
- handoff documents.

A different agent session must be able to resume the work by reading the repository-local files.

## 3.3 One significant question at a time

Conversational skills must not dump a generic twenty-question survey.

The facilitator should:

1. Read the current context.
2. Identify the highest-leverage uncertainty or contradiction.
3. Ask one meaningful question.
4. Adapt the next question to the user's answer.
5. Periodically summarize its understanding.
6. Ask the user to correct or confirm important synthesis.
7. Update durable documents at appropriate checkpoints.

The conversation should feel like working with a strong product strategist and UX facilitator, not completing a form.

## 3.4 The agent is not merely a scribe

The agent must:

- distinguish problems from proposed solutions;
- detect contradictions;
- expose assumptions;
- challenge inherited features;
- ask counterfactual questions;
- propose genuinely different product or interaction alternatives;
- identify missing users, states, constraints, and outcomes;
- preserve unresolved uncertainty;
- avoid prematurely turning tentative ideas into accepted decisions.

## 3.5 No silent product decisions

The agent may propose decisions, but important product decisions must remain `candidate` or `proposed` until the product owner explicitly accepts them.

The agent must not silently convert its own suggestion into an accepted decision.

## 3.6 Opportunity before feature

The process must not start by prematurely finalizing a feature list.

Use this conceptual sequence:

```text
user situation
    ↓
problem or opportunity
    ↓
desired outcome
    ↓
experience hypotheses
    ↓
alternative interaction models
    ↓
prototype or concept evaluation
    ↓
crystallized feature
    ↓
engineering handoff
```

An opportunity should initially be interface-agnostic.

Bad early definition:

```text
Add a dashboard for important notifications.
```

Better opportunity definition:

```text
Allow the user to understand which events require attention,
why they matter, and what action can be taken.
```

## 3.7 Neither feature-first nor UI-first

Do not enforce a rigid sequence where features are completely defined before UX work, and do not design screens without a clear desired user outcome.

The stable starting point is the **user outcome**. The feature becomes concrete through experience exploration.

## 3.8 Surprise must create value

A surprising or delightful UI/UX direction counts only when it:

- reduces effort;
- improves understanding;
- reveals the next useful action;
- preserves context;
- makes a difficult task feel obvious;
- increases confidence or control;
- meaningfully improves the user's outcome.

Visual spectacle alone is not a product advantage.

## 3.9 Current code is evidence, not the future specification

In brownfield mode:

```text
The repository is evidence of the previous product.
It is not the specification of the future product.
```

The existence of code or tests does not prove that a capability is valuable or should remain.

## 3.10 Separate facts, memories, inferences, proposals, and decisions

The system must prevent these categories from becoming conflated.

At minimum support these source/evidence labels:

```text
observed
    Demonstrated by repository evidence or runtime observation.

user_reported
    Stated by the product owner or another human stakeholder.

inferred
    Plausible interpretation that is not directly confirmed.

proposed
    New suggestion that has not been accepted.

decided
    Explicitly accepted as a durable decision.
```

Also support lifecycle states:

```text
raw
exploring
candidate
accepted
rejected
deferred
superseded
```

And record types:

```text
idea
assumption
question
proposal
decision
rejected_idea
```

---

# 4. Two supported discovery modes

The same installable harness must support two entry modes.

## 4.1 Greenfield mode

Use when there is no substantive existing product to inspect.

Flow:

```text
motivation and context
    ↓
target users and situations
    ↓
problems and outcomes
    ↓
product north
    ↓
experience north
    ↓
opportunity map
    ↓
experience exploration
    ↓
features
    ↓
releases
    ↓
engineering handoff
```

The process begins conversationally. It should not create fictional current-state findings.

## 4.2 Brownfield mode

Use when a product already exists in the repository.

Flow:

```text
repository reconnaissance
    ↓
product archaeology
    ↓
UX archaeology
    ↓
provisional current-product inventory
    ↓
conversational human review
    ↓
accepted current-product baseline
    ↓
redefinition of product north
    ↓
experience north
    ↓
opportunities
    ↓
experience exploration
    ↓
features
    ↓
releases
    ↓
engineering handoff
```

Brownfield mode combines two sources:

### Repository evidence

Examples:

- routes and entrypoints;
- screens and navigation;
- schemas, models, migrations;
- roles and permissions;
- jobs and scheduled processes;
- integrations;
- emails and notifications;
- feature flags;
- tests;
- configuration;
- incomplete or dead code;
- runtime behavior when safely available.

### Product-owner knowledge

Examples:

- why something was built;
- what was temporary;
- what never worked;
- what users actually valued;
- what was rarely or never used;
- what ideas never reached the code;
- what should be retained conceptually;
- what should be discarded despite being implemented.

The audit output must remain provisional until human review.

## 4.3 Automatic mode detection

`$product-bootstrap` should accept:

```text
--mode=greenfield
--mode=brownfield
--mode=auto
```

Default to `auto`.

Auto detection may inspect common repository signals such as:

- source directories;
- framework manifests;
- routes;
- UI components;
- tests;
- migrations;
- build files;
- application entrypoints;
- existing product documentation.

Behavior:

- If there is clearly no substantive application, suggest or select greenfield.
- If there is clearly a substantive application, suggest or select brownfield.
- If the repository is mostly boilerplate or ambiguous, record the mode as pending and ask the user to choose.
- Explicit user selection always wins.

Do not classify a framework skeleton as a mature product merely because a manifest exists.

## 4.4 Brownfield legacy stance

Support a configurable `legacy_stance`:

```text
foundation
    The existing product is the base to evolve.

reference
    Understand it, but do not assume it should be retained.

migration
    Replace it while preserving specified capabilities.

salvage
    Only selected concepts or components are likely reusable.

ignore
    The implementation may be technically useful, but should not shape
    future product definition.
```

Default brownfield stance: `reference`.

## 4.5 Repository scope

Support scoped brownfield analysis for monorepos or partial rewrites.

Example:

```yaml
repository_scope:
  include:
    - apps/web
    - apps/core
  exclude:
    - legacy
    - experiments
```

Audit and validation logic must honor scope configuration.

---

# 5. Relationship with the engineering Harness

The Product Discovery Harness and engineering Harness must be independent installable repositories.

Do not import the engineering Harness as a package or invoke private scripts.

Integrate through a versioned document contract.

The Product Discovery Harness produces:

```text
docs/PRODUCT_SENSE.md
docs/EXPERIENCE_SENSE.md
docs/product-specs/
docs/exec-plans/current/<epic>/<feature-slug>/informal.md
```

The engineering Harness can then consume the generated work item:

```text
$harness-analyze docs/exec-plans/current/<epic>/<feature-slug>
```

`$product-handoff` may detect whether engineering Harness skills appear installed and print the recommended next command. It must not require the engineering Harness to continue product discovery.

The Product Discovery Harness must never depend on the engineering Harness being installed.

---

# 6. Required installable repository structure

Create a repository organized approximately as follows. Small changes are acceptable when they improve cohesion, but all responsibilities must be represented and clearly documented.

```text
product-discovery-harness/
├── README.md
├── README.es.md
├── CHANGELOG.md
├── LICENSE
├── version.json
├── install.sh
├── pyproject.toml
├── Makefile
├── .gitignore
├── .editorconfig
├── .github/
│   └── workflows/
│       └── test.yml
│
├── bin/
│   ├── product-harness-install
│   ├── product-harness-update
│   ├── product-harness-status
│   └── product-harness-validate
│
├── agents/
│   ├── product-facilitator.md
│   ├── repository-archaeologist.md
│   ├── experience-strategist.md
│   └── product-editor.md
│
├── skills/
│   ├── bootstrap/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   ├── resume/
│   │   └── SKILL.md
│   ├── audit/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   ├── review_current_state/
│   │   └── SKILL.md
│   ├── talk/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── focus/
│   │   └── SKILL.md
│   ├── synthesize/
│   │   └── SKILL.md
│   ├── review/
│   │   └── SKILL.md
│   ├── opportunity_map/
│   │   └── SKILL.md
│   ├── opportunity_explore/
│   │   └── SKILL.md
│   ├── experience_north/
│   │   └── SKILL.md
│   ├── experience_explore/
│   │   ├── SKILL.md
│   │   ├── references/
│   │   └── assets/
│   ├── experience_evaluate/
│   │   └── SKILL.md
│   ├── feature_crystallize/
│   │   └── SKILL.md
│   ├── slice/
│   │   └── SKILL.md
│   ├── handoff/
│   │   ├── SKILL.md
│   │   └── assets/
│   └── validate/
│       └── SKILL.md
│
├── templates/
│   ├── target/
│   │   ├── product-harness.yml
│   │   ├── PRODUCT_SENSE.md
│   │   ├── EXPERIENCE_SENSE.md
│   │   └── product-discovery/
│   │       ├── README.md
│   │       ├── STATUS.md
│   │       ├── CURRENT_PRODUCT_BASELINE.md
│   │       ├── open-questions.md
│   │       ├── assumptions.yml
│   │       ├── sessions/
│   │       │   ├── index.md
│   │       │   └── session-template.md
│   │       ├── current-state/
│   │       │   ├── repository-map.md
│   │       │   ├── product-overview.md
│   │       │   ├── feature-inventory.yml
│   │       │   ├── journey-inventory.yml
│   │       │   ├── roles-and-permissions.md
│   │       │   ├── domain-map.md
│   │       │   ├── integrations.md
│   │       │   ├── experience-map.md
│   │       │   ├── friction-log.md
│   │       │   └── unknowns.md
│   │       ├── strategy/
│   │       │   ├── product-north.md
│   │       │   ├── target-users.md
│   │       │   ├── jobs-and-outcomes.md
│   │       │   ├── product-principles.md
│   │       │   ├── experience-principles.md
│   │       │   ├── success-model.md
│   │       │   └── non-goals.md
│   │       ├── opportunities/
│   │       │   ├── index.yml
│   │       │   └── opportunity-template/
│   │       │       ├── brief.md
│   │       │       ├── assumptions.yml
│   │       │       ├── questions.md
│   │       │       ├── concepts/
│   │       │       ├── prototypes.md
│   │       │       ├── evaluation.md
│   │       │       └── decision.md
│   │       ├── features/
│   │       │   ├── index.yml
│   │       │   └── feature-template/
│   │       │       ├── feature.md
│   │       │       ├── experience-contract.md
│   │       │       ├── evidence.md
│   │       │       └── handoff.md
│   │       ├── roadmap/
│   │       │   ├── releases.md
│   │       │   └── dependencies.md
│   │       └── decisions/
│   │           ├── decision-log.md
│   │           └── rejected-ideas.md
│   └── external-design/
│       ├── vendor-neutral-design-brief.md
│       ├── claude-design-prompt.md
│       ├── figma-make-prompt.md
│       └── code-prototype-prompt.md
│
├── schemas/
│   ├── product-harness.schema.json
│   ├── feature-inventory.schema.json
│   ├── opportunity-index.schema.json
│   ├── feature-index.schema.json
│   ├── assumptions.schema.json
│   └── handoff-frontmatter.schema.json
│
├── src/
│   └── product_discovery_harness/
│       ├── __init__.py
│       ├── cli.py
│       ├── config.py
│       ├── paths.py
│       ├── detection.py
│       ├── seeding.py
│       ├── validation.py
│       ├── records.py
│       ├── ids.py
│       ├── sessions.py
│       ├── handoff.py
│       └── installer_support.py
│
└── tests/
    ├── fixtures/
    │   ├── empty-repo/
    │   ├── boilerplate-repo/
    │   └── existing-app-repo/
    ├── test_detection.py
    ├── test_seeding.py
    ├── test_preservation.py
    ├── test_validation.py
    ├── test_ids.py
    ├── test_handoff.py
    └── test_installation.py
```

Do not create empty directories that Git cannot track without adding an explanatory `.gitkeep` or index file.

---

# 7. Skill format

Every skill must use the same general `SKILL.md` style as the reference engineering Harness:

```yaml
---
name: product-bootstrap
description: ...
examples:
  - "$product-bootstrap"
when_to_use:
  - "..."
when_not_to_use:
  - "..."
---
```

Each `SKILL.md` should then contain the relevant sections:

```text
## Purpose
## Required Resources
## Preconditions
## Workflow
## Conversation Protocol
## Documentation Rules
## Validation
## Output Contract
```

Not every skill needs every heading, but each skill must be operationally complete.

All installed skill names must be prefixed clearly to avoid collision with engineering Harness skills.

Use these skill names:

```text
product-bootstrap
product-resume
product-audit
product-review-current-state
product-talk
product-focus
product-synthesize
product-review
product-opportunity-map
product-opportunity-explore
product-experience-north
product-experience-explore
product-experience-evaluate
product-feature-crystallize
product-slice
product-handoff
product-validate
```

Directory names may use underscores while frontmatter names use hyphens.

---

# 8. Required skill behavior

## 8.1 `$product-bootstrap`

### Purpose

Seed a target repository with the Product Discovery Harness contract and establish greenfield, brownfield, or pending mode.

### Required behavior

1. Resolve the target repository, defaulting to the current working directory.
2. Accept mode and scope parameters when supplied.
3. Detect whether the target appears greenfield or brownfield.
4. Never overwrite substantive existing files without explicit user instruction.
5. Seed the required target structure.
6. Create `product-harness.yml`.
7. Preserve existing `docs/PRODUCT_SENSE.md`, `docs/EXPERIENCE_SENSE.md`, and `docs/product-specs/`.
8. Record the selected or pending mode in `STATUS.md`.
9. In brownfield mode, set the initial phase to repository reconnaissance.
10. In greenfield mode, set the initial phase to product-purpose exploration.
11. Validate the seeded contract.
12. Recommend the correct next skill.

### Conversational behavior

If the mode is ambiguous, explain the evidence briefly and ask the user to choose greenfield or brownfield. Do not fabricate certainty.

### Output

Report:

- target repository;
- detected/selected mode;
- files created;
- existing files preserved;
- validation result;
- recommended next command.

## 8.2 `$product-resume`

### Purpose

Resume a long-running discovery effort from repository-local context.

### Required behavior

Read at minimum:

```text
product-harness.yml
docs/product-discovery/STATUS.md
docs/product-discovery/open-questions.md
docs/product-discovery/decisions/decision-log.md
docs/PRODUCT_SENSE.md
docs/EXPERIENCE_SENSE.md
```

Also inspect active opportunity or feature documents referenced by `STATUS.md`.

Produce a concise re-entry summary:

- current mode;
- current phase;
- accepted decisions;
- working hypotheses;
- active tensions;
- open questions;
- last session;
- recommended focus.

Then continue by asking one high-leverage question or recommending the next specialized skill.

## 8.3 `$product-audit`

### Purpose

Reconstruct the current product from an existing repository.

### Preconditions

- Brownfield mode.
- Repository scope resolved.
- No source-code modification is allowed.

### Required behavior

Perform systematic evidence-based archaeology:

- repository map;
- likely application boundaries;
- routes and entrypoints;
- screens, pages, components, and navigation;
- actors, roles, and permissions;
- domain concepts;
- schemas and migrations;
- integrations;
- background jobs;
- notifications and emails;
- feature flags and configuration;
- tests;
- runtime commands;
- incomplete or dead-looking code;
- current UX journeys and friction.

Classify discovered items. Do not label every technical mechanism as a user-facing feature.

Suggested classifications:

```text
user_feature
admin_capability
internal_capability
integration
operational_behavior
constraint
technical_debt
incomplete_feature
possibly_dead_code
```

Every important current-state claim must include evidence references where possible:

```yaml
evidence:
  routes:
    - path/to/router:line
  modules:
    - path/to/module
  tests:
    - path/to/test
  runtime_verified: false
```

Use confidence levels:

```text
high
medium
low
```

Mark inferences explicitly.

The skill may safely execute read-only inspection or standard non-destructive commands when appropriate. It must not:

- alter product code;
- run destructive migrations;
- mutate production systems;
- assume deployment credentials;
- make network calls to private services without user authorization.

### Output

Populate `docs/product-discovery/current-state/`.

Create a provisional inventory, not an accepted baseline.

Update `STATUS.md` to recommend `$product-review-current-state`.

## 8.4 `$product-review-current-state`

### Purpose

Review the provisional brownfield audit conversationally with the product owner.

### Required behavior

Group findings into understandable product capabilities and journeys.

Ask questions such as:

- Was this central, secondary, temporary, or accidental?
- Who actually used it?
- Did it work as intended?
- Was anything important missing from the code?
- Would this still be built from scratch?
- Should the concept remain even if the interface changes completely?

Keep these distinctions:

```text
observed in repository
remembered/reported by human
aspirational future idea
```

Allow future disposition values for existing capabilities:

```text
keep
improve
redesign
merge
split
remove
defer
unknown
```

Do not finalize the future roadmap during current-state review.

Once the user explicitly accepts the reconstructed understanding, create or update:

```text
docs/product-discovery/CURRENT_PRODUCT_BASELINE.md
```

The baseline describes the agreed previous/current product, not the future north.

## 8.5 `$product-talk`

### Purpose

Run an open-ended product discovery conversation.

### Conversation protocol

- Read current status before asking anything.
- Ask one significant question at a time.
- Adapt questions to the user's previous answer.
- Separate user outcomes from interface solutions.
- Detect contradictions with accepted decisions or principles.
- Surface assumptions.
- Offer synthesis checkpoints.
- Do not force closure.
- Preserve the user's language and tone.
- Use the configured documentation language.
- When enough material has accumulated, update a session document and relevant working documents.
- Before marking an important item accepted, obtain explicit confirmation.

The skill should support long sessions and repeated invocations.

### Suggested initial greenfield question

A suitable first question is conceptually:

```text
What situation or motivation led you to want this product to exist?
```

Do not hardcode only this question. Choose based on context.

### Session documents

Create a dated, uniquely named session file containing:

```text
Focus
Context entering the session
Discussion summary
Ideas raised
Assumptions identified
Candidate decisions
Accepted decisions
Rejected alternatives
Open questions
Contradictions or tensions
Documents updated
Recommended next focus
```

Avoid treating raw chat transcription as the canonical spec.

## 8.6 `$product-focus <topic-or-id>`

Same facilitation protocol as `$product-talk`, but scoped to:

- a topic;
- a user group;
- a product principle;
- an opportunity ID;
- an existing capability ID;
- an experience tension;
- a feature candidate.

It must resolve references and update `STATUS.md` with the active focus.

## 8.7 `$product-synthesize`

### Purpose

Turn accumulated conversation into a coherent candidate product synthesis.

### Required behavior

Read relevant sessions, current state, assumptions, decisions, and open questions.

Produce candidate updates for:

- product north;
- target users;
- jobs and outcomes;
- product principles;
- non-goals;
- success model;
- major tensions.

Do not silently mark candidate content accepted.

Clearly identify:

- well-supported conclusions;
- weak assumptions;
- contradictions;
- missing decisions;
- alternative interpretations.

Ask the product owner to confirm or revise major synthesis before promoting it to stable documents.

## 8.8 `$product-review`

### Purpose

Audit the overall discovery corpus for quality and consistency.

Check:

- stale or contradictory documents;
- accepted decisions not reflected in summaries;
- proposals incorrectly represented as decisions;
- unresolved high-impact assumptions;
- orphaned IDs or broken links;
- duplicated opportunities;
- features without source opportunities;
- UI solutions defined before outcomes;
- opportunities disguised as features;
- missing non-goals;
- missing edge states;
- release slices that are technical layers rather than user outcomes;
- handoffs that are not ready.

Produce a prioritized review report and update `STATUS.md`.

## 8.9 `$product-opportunity-map`

### Purpose

Build and maintain the product opportunity portfolio.

An opportunity must include:

- user or actor;
- situation;
- problem;
- desired outcome;
- current alternative;
- evidence;
- assumptions;
- constraints;
- importance;
- open experience questions;
- relationships to current capabilities;
- lifecycle status.

The opportunity must not require a predetermined screen or control.

Support merging, splitting, rejecting, deferring, and superseding opportunities with traceability.

## 8.10 `$product-opportunity-explore <OPP-ID>`

Facilitate a focused conversation around one opportunity.

Questions should cover:

- who experiences it;
- frequency and severity;
- triggering situation;
- current workaround;
- desired outcome;
- consequences of doing nothing;
- product alignment;
- constraints;
- uncertainty;
- edge cases;
- evidence still needed.

Update the opportunity directory and session history.

## 8.11 `$product-experience-north`

### Purpose

Define how the product should feel and behave globally.

Create or refine:

```text
docs/EXPERIENCE_SENSE.md
docs/product-discovery/strategy/experience-principles.md
```

Cover:

- experience promise;
- desired qualities;
- interaction principles;
- complexity and progressive disclosure;
- guidance versus freedom;
- automation versus control;
- learnability;
- repeat-use efficiency;
- feedback and recovery;
- trust and explainability;
- accessibility expectations;
- explicit anti-patterns.

This is not a visual style guide. Do not focus on colors, typography, or component tokens unless they express a product-level experience principle.

## 8.12 `$product-experience-explore <OPP-ID>`

### Purpose

Generate and document genuinely different interaction models for an opportunity.

### Required behavior

Before proposing concepts, read:

- the opportunity brief;
- product north;
- experience north;
- relevant current-state evidence;
- constraints;
- target users;
- realistic example data.

Generate three to five divergent concepts.

They must differ materially in:

- mental model;
- navigation;
- information hierarchy;
- interaction sequence;
- degree of automation;
- user control;
- discoverability;
- handling of complexity.

Do not submit superficial variants such as:

- light versus dark;
- sidebar versus top navigation;
- cards with different styling;
- cosmetic rearrangements of the same workflow.

Possible interaction paradigms include, when appropriate:

- command center;
- guided workflow;
- contextual actions;
- proactive assistant;
- direct manipulation;
- object-centered workspace;
- timeline;
- collaborative canvas;
- automation with review;
- conversational support only where conversation adds value.

For each concept document:

- concept summary;
- user mental model;
- main flow;
- first-use experience;
- repeated-use experience;
- empty state;
- loading state;
- error or ambiguity;
- permission limitation;
- large-data state;
- mobile considerations when relevant;
- advantages;
- risks;
- product assumptions;
- technical questions, without designing the full architecture.

Generate a vendor-neutral design brief and optional prompt variants for:

- Claude Design;
- Figma Make;
- a code-adjacent prototyping tool.

Do not require any vendor-specific service to be available.

Store external prototype links, exported images, or handoff references in `prototypes.md`. The repository remains the source of truth; external tools are exploration surfaces.

## 8.13 `$product-experience-evaluate <OPP-ID>`

### Purpose

Compare concepts and record the selection or next experiment.

Use a scorecard with at least:

```text
outcome fit
learnability
repeat-use efficiency
cognitive load
discoverability
feedback
error recovery
trust
accessibility
delight
extensibility
feasibility
```

A numeric score may support discussion, but must not mechanically determine the winner.

Record:

- tradeoffs;
- user feedback if available;
- assumptions behind the evaluation;
- selected concept, combined concept, or need for further exploration;
- rejected alternatives and rationale;
- experience invariants discovered.

Do not mark a concept selected without explicit product-owner confirmation.

## 8.14 `$product-feature-crystallize <OPP-ID>`

### Purpose

Convert an explored opportunity and selected experience direction into a feature candidate.

The feature must include:

- stable feature ID;
- source opportunity IDs;
- current capability references, if any;
- target users;
- problem;
- desired outcome;
- why now;
- selected experience;
- core interaction model;
- key journey;
- required states;
- experience invariants;
- flexible design areas;
- scope;
- non-goals;
- success signals;
- dependencies;
- constraints;
- unresolved technical questions;
- prototype references;
- rejected alternatives;
- lifecycle status.

Do not include detailed architecture, module names, migration designs, or implementation steps. Those belong to the engineering Harness.

A feature is not automatically `accepted`; it begins as `candidate` unless explicitly approved.

## 8.15 `$product-slice`

### Purpose

Organize accepted features into outcome-oriented releases.

Releases must be vertical user-value slices.

Avoid:

```text
Release 1: database
Release 2: backend
Release 3: frontend
```

Prefer:

```text
Release 1: a specific user can complete one valuable outcome
from beginning to end with intentionally limited scope.
```

Each release should include:

- target user;
- enabled outcome;
- included features;
- explicit exclusions;
- dependencies;
- risks;
- learning goals;
- success signals;
- condition for moving to the next release.

## 8.16 `$product-handoff <FEATURE-ID>`

### Purpose

Create an engineering-ready informal feature input without performing engineering design.

### Definition of Ready

Require:

```text
[ ] Stable feature ID
[ ] Accepted feature status
[ ] Product-north alignment
[ ] Identified user
[ ] Problem statement
[ ] Desired outcome
[ ] Selected experience direction
[ ] Core interaction model
[ ] Scope
[ ] Non-goals
[ ] Experience invariants
[ ] Required states
[ ] Known dependencies
[ ] Success signals
[ ] No blocking strategic product questions
[ ] Links to source opportunities and decisions
```

If not ready, fail clearly and list missing items. Do not manufacture answers.

### Output path

Generate:

```text
docs/exec-plans/current/<epic>/<feature-slug>/informal.md
```

Allow a non-epic form when no epic is appropriate:

```text
docs/exec-plans/current/<feature-slug>/informal.md
```

### Required frontmatter

```yaml
---
document_type: product-feature-handoff
contract_version: 1
feature_id: FEATURE-007
opportunity_ids:
  - OPP-004
product_harness_version: 0.1.0
status: ready-for-analysis
---
```

### Required sections

```text
# Feature name

## Product context
## Target users
## Problem
## Desired outcome
## Why now
## Product alignment
## Selected experience
## Core interaction model
## Key journey
## Required states
## Experience invariants
## Scope
## Non-goals
## Dependencies
## Constraints
## Success signals
## Risks
## Open technical questions
## Prototype references
## Source references
## Decisions and rejected alternatives
```

Also update or create an appropriate feature-level file under:

```text
docs/product-specs/
```

Do not duplicate large amounts of text unnecessarily; use explicit links where appropriate.

When engineering Harness appears installed, print:

```text
$harness-analyze docs/exec-plans/current/<...>
```

Do not invoke private engineering Harness scripts.

## 8.17 `$product-validate`

Validate:

- target contract structure;
- `product-harness.yml`;
- required documents for the selected mode;
- record schemas;
- unique IDs;
- cross-references;
- accepted decision integrity;
- opportunity/feature links;
- release links;
- handoff frontmatter and required sections;
- no invalid lifecycle transitions;
- no accepted feature without required fields.

Support focused checks and full validation.

---

# 9. Target repository contract

The bootstrap skill must create or preserve this target structure.

```text
target-product/
├── product-harness.yml
└── docs/
    ├── PRODUCT_SENSE.md
    ├── EXPERIENCE_SENSE.md
    ├── product-specs/
    ├── exec-plans/
    │   └── current/
    └── product-discovery/
        ├── README.md
        ├── STATUS.md
        ├── CURRENT_PRODUCT_BASELINE.md
        ├── open-questions.md
        ├── assumptions.yml
        ├── sessions/
        ├── current-state/
        ├── strategy/
        ├── opportunities/
        ├── features/
        ├── roadmap/
        └── decisions/
```

For greenfield mode, current-state documents may explicitly say there is no implemented product. They must not contain invented findings.

For brownfield mode, current-state documents remain separate from future strategy documents.

Never rewrite current-state history so it looks like the future product.

---

# 10. `product-harness.yml`

Create a clear, versioned, machine-readable config.

Use YAML and validate it against JSON Schema.

Suggested shape:

```yaml
version: 1

mode: brownfield
mode_detection:
  status: confirmed
  evidence:
    - application source and routes detected

legacy_stance: reference

repository_scope:
  include:
    - .
  exclude:
    - .git
    - node_modules
    - deps
    - build
    - dist
    - tmp
    - vendor

languages:
  interaction: auto
  documentation: auto

discovery:
  current_phase: current-state-review
  require_explicit_acceptance_for_decisions: true
  preserve_session_summaries: true
  ask_one_primary_question_at_a_time: true

integration:
  engineering_harness:
    enabled: true
    contract_version: 1
    work_items_path: docs/exec-plans/current
    product_specs_path: docs/product-specs

paths:
  status: docs/product-discovery/STATUS.md
  product_sense: docs/PRODUCT_SENSE.md
  experience_sense: docs/EXPERIENCE_SENSE.md
  discovery_root: docs/product-discovery

tooling:
  product_discovery_harness_version: 0.1.0
```

The actual schema may improve this shape, but retain these concepts.

Interaction and documentation languages should default to `auto`. Agents should normally preserve the language used by the product owner. Machine-readable keys and IDs should remain stable English identifiers.

---

# 11. Durable document semantics

## 11.1 `STATUS.md`

This is the primary re-entry point.

It must summarize:

```text
Mode
Legacy stance
Current phase
Active focus
Current-product baseline status
Product north status
Experience north status
Stable decisions
Working hypotheses
Active tensions
Open questions
Active opportunities
Active feature candidates
Recommended next session
Last updated
Last session
```

Skills that materially advance discovery must update it.

## 11.2 Session summaries

Use filenames like:

```text
2026-07-29-01-product-purpose.md
```

or another deterministic unique convention.

Do not use an unstructured full chat dump as the source of truth.

Session records should preserve useful history while summarizing noise.

## 11.3 Decision log

Each important decision should include:

```text
ID
Title
Status
Date
Decision
Rationale
Alternatives considered
Consequences
Source sessions
Accepted by
Supersedes or superseded by
```

## 11.4 Assumptions

Each assumption should include:

```text
ID
Statement
Source
Status
Confidence
Impact if wrong
Validation approach
Related opportunities/features
```

## 11.5 Open questions

Questions should have IDs, priority, status, source, related records, and resolution when closed.

## 11.6 Existing capabilities

Use IDs:

```text
CURRENT-001
CURRENT-002
```

Each record should separate:

- observed implementation;
- product assessment;
- experience assessment;
- future disposition.

## 11.7 Opportunities

Use IDs:

```text
OPP-001
OPP-002
```

## 11.8 Features

Use IDs:

```text
FEATURE-001
FEATURE-002
```

## 11.9 Decisions and assumptions

Use:

```text
DEC-001
ASSUMPTION-001
QUESTION-001
```

IDs must be stable, unique, monotonic within the target repository, and never silently reused after deletion.

Implement an ID registry or robust index strategy.

---

# 12. Product and experience summaries

## 12.1 `docs/PRODUCT_SENSE.md`

This should be the concise, stable summary that downstream engineering agents can read.

Include:

- product promise;
- target users;
- primary situations;
- core outcomes;
- priorities;
- product principles;
- non-goals;
- success model;
- decision guidance;
- links to detailed discovery documents.

It should not contain every conversation detail.

## 12.2 `docs/EXPERIENCE_SENSE.md`

This should summarize:

- experience promise;
- desired qualities;
- interaction principles;
- automation/control stance;
- complexity strategy;
- feedback/recovery principles;
- accessibility expectations;
- trust and explainability;
- explicit anti-patterns;
- the rule that surprise should reduce effort or improve understanding.

These two documents are durable interfaces to the engineering process.

---

# 13. UX concept exploration and external design tools

The Product Discovery Harness is not itself a visual design application.

It must orchestrate and document design exploration in a tool-neutral way.

## Required external-design artifacts

Generate a reusable vendor-neutral brief containing:

- opportunity;
- user;
- situation;
- desired outcome;
- current alternatives;
- constraints;
- product principles;
- experience principles;
- realistic data;
- edge states;
- explicit request for divergent interaction models;
- evaluation criteria.

Also provide optional prompt adapters for:

- Claude Design;
- Figma Make;
- code-generating prototyping tools.

Prompt adapters must instruct the tool not to produce mere aesthetic variants.

A representative instruction is:

```text
Generate four materially different interaction models for the same
user outcome. They must differ in mental model, navigation, hierarchy,
decision sequence, and degree of automation. Do not produce visual
skins of the same solution.
```

The prompts must request, where relevant:

- primary flow;
- first-use state;
- repeat-use state;
- empty state;
- loading;
- errors;
- ambiguity;
- permission restrictions;
- high-volume data;
- responsive/mobile behavior;
- explanation of the model;
- prototype or interaction demonstration.

External links and artifacts must be referenced from repository documents so discoveries are not trapped inside a design tool.

---

# 14. Installer and global skill installation

Mirror the strong operating model of the reference Harness.

## Required commands

```text
./bin/product-harness-install
./bin/product-harness-install latest
./bin/product-harness-update
./bin/product-harness-status
./bin/product-harness-validate
```

Also include a curl-friendly `install.sh`.

Suggested environment overrides:

```text
PRODUCT_HARNESS_REPO_URL
PRODUCT_HARNESS_REPO_PATH
PRODUCT_HARNESS_CHANNEL
```

Default local repository path:

```text
~/.local/share/product-discovery-harness
```

## Installation targets

Support:

```text
~/.agents/skills
~/.claude/skills
```

Behavior:

- install into a target when it already exists;
- install into both when both exist;
- create both roots when neither exists;
- use a collision-safe namespace directory;
- create symlinks for each installed skill using the `name` from `SKILL.md`;
- be idempotent;
- repair broken links;
- avoid replacing unrelated skills;
- store local installation metadata;
- report repository version, selected channel, installed version, targets, and broken links.

Use a namespace such as:

```text
~/.agents/skills/product-discovery-harness/
```

with symlinks inside for:

```text
product-bootstrap
product-talk
...
```

## Channels

Implement behavior analogous to:

```text
stable
    newest release tag

latest
    default branch
```

## Python environment

The implementation may use a local virtual environment under the installed repository to support YAML and JSON Schema validation.

Prefer a small, explicit dependency set.

Suggested runtime dependencies:

```text
PyYAML
jsonschema
```

Do not require a globally polluted Python environment.

Ensure skill scripts can reliably resolve the installed repository root and its Python environment rather than assuming the current working directory.

---

# 15. Seeding and preservation rules

Bootstrap must be idempotent and safe.

Rules:

1. Never overwrite substantive target files by default.
2. Create missing directories and files.
3. Recognize files previously seeded by this harness.
4. Update empty or placeholder-only files safely.
5. When templates evolve, provide validation or migration guidance rather than destructive replacement.
6. Preserve user wording and accepted decisions.
7. Back up a file before explicit overwrite.
8. Report every material write.
9. Product discovery skills may read application code but must not modify it.
10. Only documentation and harness-local metadata may be changed during discovery.
11. Handoff may create engineering work-item directories and product specs, but not application implementation.

Include marker metadata or another reliable strategy to distinguish seeded boilerplate from substantive content.

---

# 16. Validation and schemas

Use JSON Schema for machine-readable YAML documents.

Validation must produce human-readable errors with paths and actionable remediation.

Validate at least:

- config shape;
- allowed modes;
- legacy stances;
- lifecycle states;
- unique IDs;
- required opportunity fields;
- required feature fields;
- accepted feature readiness;
- handoff frontmatter;
- target directory contract;
- references to real records;
- no duplicate active IDs;
- no feature referencing a nonexistent opportunity;
- no release referencing a nonexistent feature;
- no accepted decision without acceptance metadata;
- no brownfield baseline marked accepted before human review metadata exists.

Provide:

```text
product-harness-validate <target-repo>
```

and a skill-level `$product-validate`.

Exit codes must be useful for CI.

---

# 17. Tests and fixtures

Build meaningful automated tests.

At minimum test:

## Mode detection

- empty repo → greenfield;
- substantive fixture app → brownfield;
- boilerplate fixture → ambiguous/pending;
- explicit mode overrides detection.

## Seeding

- creates required structure;
- greenfield documents do not invent current state;
- brownfield status starts in the correct phase;
- rerunning is idempotent.

## Preservation

- existing substantive `PRODUCT_SENSE.md` is not overwritten;
- existing opportunity and decision files remain unchanged;
- placeholder files can be upgraded safely.

## IDs

- monotonic IDs;
- no reuse;
- concurrency-safe enough for normal local use;
- invalid IDs rejected.

## Validation

- valid fixture passes;
- broken references fail;
- invalid lifecycle fails;
- missing accepted-feature fields fail;
- bad config fails clearly.

## Handoff

- valid accepted feature produces exact path;
- frontmatter validates;
- required sections exist;
- missing Definition-of-Ready items prevent handoff;
- engineering Harness is optional.

## Installation

Use a temporary `HOME` and verify:

- Codex target installation;
- Claude target installation;
- both targets;
- neither target initially exists;
- idempotent reinstall;
- broken symlink repair;
- status output.

Use standard temporary directories and avoid touching the developer's real home in tests.

---

# 18. Documentation requirements

## 18.1 Main README

`README.md` must be complete and usable without reading the source.

Include:

1. What Product Discovery Harness is.
2. What problem it solves.
3. Relationship to engineering Harness.
4. Core concept: reusable skills, durable context in target repo.
5. Greenfield versus brownfield.
6. Installation:
   - local checkout;
   - curl install;
   - stable/latest;
   - update/status.
7. How to bootstrap a target repository.
8. Exact recommended skill sequence for each mode.
9. A skill catalog with purpose, inputs, outputs, and when to use.
10. Conversation model.
11. Target repository file layout.
12. Opportunity → UX exploration → feature → handoff flow.
13. External design-tool workflow.
14. Example end-to-end greenfield session.
15. Example end-to-end brownfield session.
16. Engineering Harness handoff example.
17. Validation commands.
18. Preservation and safety guarantees.
19. Configuration reference.
20. Troubleshooting.
21. FAQ.
22. Development and test commands.
23. Versioning and release process.
24. Uninstallation instructions.

## 18.2 Spanish README

Create `README.es.md` with equivalent, complete Spanish documentation—not a short summary.

The main `README.md` may be English. Link both language versions at the top.

## 18.3 Examples in README

Greenfield:

```text
cd ~/projects/new-product
$product-bootstrap --mode=greenfield
$product-talk
$product-synthesize
$product-experience-north
$product-opportunity-map
$product-opportunity-explore OPP-001
$product-experience-explore OPP-001
$product-experience-evaluate OPP-001
$product-feature-crystallize OPP-001
$product-slice
$product-handoff FEATURE-001
```

Brownfield:

```text
cd ~/projects/existing-product
$product-bootstrap --mode=brownfield
$product-audit
$product-review-current-state
$product-talk
$product-synthesize
$product-experience-north
$product-opportunity-map
...
```

Explain that this is a recommended flow, not a rigid wizard. `$product-resume` should determine the next useful step from status.

---

# 19. Agent personas and shared reference guidance

Create reusable persona/reference files loaded by relevant skills.

## Product facilitator

Behaviors:

- curious;
- structured;
- non-dogmatic;
- asks one primary question;
- notices contradictions;
- separates problem and solution;
- summarizes periodically;
- does not force closure;
- seeks explicit confirmation for durable decisions.

## Repository archaeologist

Behaviors:

- evidence-driven;
- stack-agnostic;
- conservative with inference;
- separates user capabilities from technical mechanisms;
- records confidence and paths;
- never treats code as future product truth.

## Experience strategist

Behaviors:

- outcome-led;
- explores divergent interaction models;
- tests edge states;
- values learnability and repeat efficiency;
- distinguishes delight from decoration;
- remains tool-neutral.

## Product editor

Behaviors:

- converts discussion into concise durable documentation;
- keeps traceability;
- avoids duplicated canonical text;
- identifies stale summaries;
- preserves rejected alternatives and rationale.

Skills should reference these files rather than duplicating all persona guidance.

---

# 20. Conversational documentation protocol

Implement the following protocol in `product-talk`, `product-focus`, `product-review-current-state`, and opportunity/experience conversation skills.

## Start

1. Read `STATUS.md`.
2. Read the last relevant session.
3. Read accepted decisions and open questions.
4. State the current understanding concisely.
5. Ask one high-leverage question.

## During discussion

Continuously distinguish:

```text
new idea
assumption
question
candidate proposal
accepted decision
rejected alternative
deferred topic
```

When a conflict appears, say so explicitly.

Example behavior:

```text
Earlier we accepted that first use should require almost no
configuration. This proposal introduces a multi-step setup flow.
Which principle should dominate, or is there a third approach?
```

## Checkpoint

After a meaningful amount of discussion:

```text
Here is my current understanding...
```

Summarize and allow correction.

## Persistence

At a checkpoint or session end:

- write/update session summary;
- update working documents;
- update decisions only when accepted;
- update assumptions and questions;
- update `STATUS.md`;
- report changed files.

## Session end

Summarize:

- decisions;
- candidate decisions;
- ideas;
- assumptions;
- open questions;
- contradictions;
- files changed;
- recommended next focus.

Do not require the user to manually maintain these documents.

---

# 21. State transitions

Define and validate sensible transitions.

Example:

```text
raw → exploring
exploring → candidate
candidate → accepted
candidate → rejected
candidate → deferred
accepted → superseded
deferred → exploring
rejected → exploring only with an explicit reopening record
```

Do not allow the agent to mark its own proposal accepted without human acceptance metadata.

Record transition history for important entities when practical.

---

# 22. Separation of current, future, and execution truth

The target structure must preserve three independent layers:

```text
CURRENT EVIDENCE
    What the existing product does or appears to do.

FUTURE PRODUCT
    What has been decided about the desired product and experience.

EXECUTION
    How an accepted feature will be specified and implemented.
```

Map them to:

```text
docs/product-discovery/current-state/
docs/product-discovery/strategy/
docs/product-discovery/opportunities/
docs/product-discovery/features/
docs/product-specs/
docs/exec-plans/
```

Never mutate the current-state record to hide that a feature was removed or redesigned.

Traceability example:

```yaml
feature_id: FEATURE-009
source_opportunities:
  - OPP-006
supersedes_current_capabilities:
  - CURRENT-014
```

---

# 23. Non-goals

The repository must explicitly document these non-goals:

- It does not implement application features.
- It does not replace the engineering Harness.
- It does not make unconfirmed product decisions automatically.
- It does not require a visual design vendor.
- It does not treat a prototype as the final product specification.
- It does not infer product value from code volume or test coverage.
- It does not force a linear waterfall process.
- It does not use the entire chat transcript as canonical documentation.
- It does not require a particular technology stack.
- It does not modify production code during discovery.
- It does not make network calls to private systems without authorization.
- It does not reduce UX exploration to visual styling.

---

# 24. Initial version scope

Set the initial repository version to:

```json
{
  "version": "0.1.0"
}
```

Version `0.1.0` must still be end-to-end usable.

The following are mandatory in the first version:

- global installer/update/status;
- all named skills;
- greenfield bootstrap;
- brownfield bootstrap and audit workflow;
- conversational protocols;
- complete target templates;
- schemas and validation;
- ID generation;
- session creation;
- opportunity and feature records;
- experience exploration briefs;
- release slicing documentation;
- engineering handoff generation;
- automated tests;
- CI;
- English and Spanish README.

Do not postpone essential behavior to a future version.

Optional enhancements may be documented in a roadmap, but must not substitute for the mandatory implementation.

---

# 25. Implementation quality requirements

- Prefer clear, small modules.
- Use type hints.
- Include useful error messages.
- Avoid hidden global state.
- Resolve repository roots robustly.
- Work on macOS and Linux.
- Quote shell paths correctly.
- Handle spaces in paths.
- Use atomic writes for generated metadata when practical.
- Preserve newline and file encoding.
- Use UTC or local ISO dates consistently and document the choice.
- Avoid unnecessary dependencies.
- Do not depend on a running web service.
- Keep machine-readable files deterministic for clean diffs.
- Sort generated index entries stably.
- Make validation suitable for CI.
- Include docstrings and comments where behavior is not obvious.
- Ensure scripts are executable.
- Ensure the installer can locate skills even when invoked through symlinks.
- Ensure the installed skill scripts never resolve paths relative to the target repository by mistake.

---

# 26. Acceptance criteria

The implementation is complete only when all of the following are true.

## Repository

- [ ] All required files are present.
- [ ] No important executable behavior is a placeholder.
- [ ] `version.json` reports `0.1.0`.
- [ ] License and changelog exist.
- [ ] README documentation is complete in English and Spanish.

## Installation

- [ ] Local installer works.
- [ ] Curl entrypoint is implemented.
- [ ] Stable/latest channel behavior is implemented.
- [ ] Codex and Claude skill targets are supported.
- [ ] Reinstall is idempotent.
- [ ] Update and status commands work.
- [ ] Installation tests use a temporary home.

## Greenfield

- [ ] Bootstrap creates the target contract.
- [ ] Mode is recorded correctly.
- [ ] Current-state docs do not invent a product.
- [ ] Status recommends a conversational next step.
- [ ] Validation passes.

## Brownfield

- [ ] Bootstrap recognizes a substantive fixture.
- [ ] Audit writes evidence-based current-state docs.
- [ ] Source code is not modified.
- [ ] Findings remain provisional.
- [ ] Human review is required before baseline acceptance.
- [ ] Current and future product docs remain separate.

## Conversation

- [ ] Skills instruct the agent to ask one high-value question at a time.
- [ ] Sessions are summarized and persisted.
- [ ] Important decisions require explicit acceptance.
- [ ] Contradictions and assumptions are tracked.
- [ ] `$product-resume` can reconstruct context from files.

## Product and UX

- [ ] Opportunities precede crystallized features.
- [ ] Experience north is supported.
- [ ] UX exploration requires divergent interaction models.
- [ ] Edge states and evaluation scorecard are included.
- [ ] External design prompts are vendor-neutral at the core.
- [ ] Delight is evaluated as functional user value, not decoration.

## Handoff

- [ ] Definition of Ready is enforced.
- [ ] `informal.md` is generated at the correct path.
- [ ] Frontmatter and required sections validate.
- [ ] Product specs are linked or updated.
- [ ] Engineering Harness remains optional and decoupled.
- [ ] The next `$harness-analyze` command is printed when appropriate.

## Quality

- [ ] Tests pass.
- [ ] CI is configured.
- [ ] Full validation passes on valid fixtures.
- [ ] Invalid fixtures fail with actionable errors.
- [ ] Shell scripts handle paths safely.
- [ ] The final Codex response reports test and validation results honestly.

---

# 27. Expected final deliverable from Codex

At completion, Codex should provide:

1. A concise description of the repository implemented.
2. The final directory tree.
3. Important architectural decisions.
4. Installation commands.
5. A greenfield quick-start.
6. A brownfield quick-start.
7. The engineering handoff command.
8. Tests and validation commands run.
9. Exact results, including any remaining limitations.

The actual repository—not only this explanation—is the deliverable.
