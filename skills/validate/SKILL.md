---
name: product-validate
description: Validate Product Discovery Harness target contracts and records.
examples: ["$product-validate", "$product-validate docs/product-discovery/features"]
when_to_use: ["Before handoff or after material discovery edits."]
when_not_to_use: ["The target has not been bootstrapped."]
---
## Purpose
Check structure, config/schema, IDs, lifecycle transitions, accepted decisions,
opportunity/feature/release links, index path/date metadata, baseline review
metadata, and handoff readiness.
## Preconditions
A bootstrapped target. If it is absent, route to `$product-bootstrap` rather
than interpreting missing structure as a product failure.
## Workflow
Run `product-harness validate <target>` and convert diagnostics into remediation actions.
## Output Contract
Return CI-useful success/failure exit status and human-readable paths. End with
exactly one `Recommended next focus:`; name the highest-priority remediation or
the appropriate next discovery activity after a clean validation.
