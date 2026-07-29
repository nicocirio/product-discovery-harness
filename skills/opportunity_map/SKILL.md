---
name: product-opportunity-map
description: Maintain outcome-led product opportunities.
examples: ["$product-opportunity-map"]
when_to_use: ["Problems and desired outcomes should become a portfolio."]
when_not_to_use: ["A UI solution is being treated as the opportunity."]
---
## Purpose
Create interface-agnostic opportunity briefs with actor, situation, problem, outcome, alternatives, evidence, assumptions, constraints, importance, questions, capability links, and lifecycle.
## Preconditions
An owner has identified a durable problem/outcome, not merely a raw idea or UI
solution. Route a raw thought to `$product-talk`; route a possible duplicate to
`$product-reconcile` before creating a record.
## Workflow
Allocate OPP IDs; create `docs/product-discovery/opportunities/<OPP-ID>/brief.md`
from the opportunity template; then add the canonical index record with title,
target-relative path, created_at, last_updated_at, and last_reviewed_at. Support
merge, split, reject, defer, and supersede with traceability.
Before creating a new opportunity from a session idea, use `$product-reconcile`
to compare it with active/differed records, decisions, and current evidence.
## Documentation Rules
Do not require a predetermined screen or control.
## Output Contract
Update index and affected briefs, preserving lifecycle history. After a material
human review, update `last_reviewed_at` and regenerate `$product-landscape`. End
with exactly one `Recommended next focus:`; normally explore the newly confirmed
opportunity or resolve the reconciliation question.
