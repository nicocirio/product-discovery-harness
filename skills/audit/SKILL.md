---
name: product-audit
description: Reconstruct provisional current product evidence in brownfield mode.
examples: ["$product-audit"]
when_to_use: ["Brownfield reconnaissance is needed."]
when_not_to_use: ["Greenfield mode or application modification."]
---
## Purpose
Produce evidence-based archaeology without changing application code.
## Required Resources
Read `agents/repository-archaeologist.md`, config scope, and current-state templates.
## Preconditions
Brownfield mode and resolved repository scope.
If the target has not been bootstrapped or mode is unknown, route to
`$product-bootstrap` first.
## Workflow
Run static scoped audit; inspect routes, entrypoints, UI, roles, domain, jobs, integrations, tests, flags, and likely dead code. Classify findings and cite paths/confidence.
## Documentation Rules
Refresh `docs/product-discovery/current-state/` as the latest snapshot and write
a dated, immutable report plus index under `docs/product-discovery/audits/`.
Findings are provisional.
## Validation
Validate target and recommend `$product-review-current-state`.
## Output Contract
Report evidence, unknowns, the current snapshot, the historical report, and no application mutation. End with
exactly one `Recommended next focus:`; normally `$product-review-current-state`
to confirm the provisional baseline.
