---
name: product-review-current-state
description: Confirm or correct provisional brownfield archaeology with the owner.
examples: ["$product-review-current-state"]
when_to_use: ["A brownfield audit is ready for human review."]
when_not_to_use: ["Audit findings do not exist."]
---
## Purpose
Turn provisional evidence into an explicitly accepted current-product baseline.
## Preconditions
Provisional brownfield audit findings. If they are absent, route to
`$product-audit`; if the target is not bootstrapped, route to
`$product-bootstrap`.
## Required Resources
Read archaeologist guidance, audit artifacts, STATUS, and decisions.
## Workflow
Group capabilities/journeys; ask one question such as who used it or whether it should remain conceptually. Track keep/improve/redesign/merge/split/remove/defer/unknown without finalizing roadmap.
## Documentation Rules
Distinguish observed, human-reported, and aspirational content. Update baseline only after explicit acceptance metadata.
## Output Contract
Update status and identify the next strategic conversation. End with exactly one
`Recommended next focus:`.
