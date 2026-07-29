---
name: product-review
description: Audit discovery corpus quality, consistency, and readiness.
examples: ["$product-review"]
when_to_use: ["A portfolio or handoff needs quality review."]
when_not_to_use: ["Bootstrap has not created a corpus."]
---
## Purpose
Find stale summaries, contradicted decisions, orphan IDs, missing indexed detail
paths, premature UI, duplicate opportunities, invalid releases, and unready handoffs.
## Preconditions
A bootstrapped discovery corpus. If none exists, route to `$product-bootstrap`.
## Workflow
Generate or read the landscape first; prioritize findings, update STATUS, and
generate/read `CONSISTENCY_REPORT.md`; prioritize findings, update STATUS, and
propose remediation without accepting product decisions.
## Output Contract
Produce a prioritized review report. End with exactly one `Recommended next focus:`;
name the highest-priority remediation without accepting a product decision.
