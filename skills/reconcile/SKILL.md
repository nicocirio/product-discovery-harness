---
name: product-reconcile
description: Compare one durable product record with related product intent and current evidence.
examples:
  - "$product-reconcile OPP-001"
  - "$product-reconcile FEATURE-003"
when_to_use:
  - "A brainstormed idea is ready to become an opportunity or feature."
  - "An existing opportunity or feature may overlap, conflict, or need revision."
when_not_to_use:
  - "The thought is still too raw to leave a session summary."
  - "A lifecycle decision has already been made without needing comparison."
---
## Purpose
Prevent durable product records from silently duplicating, contradicting, or
obscuring prior product thinking. Generate a focused reconciliation report and
facilitate one owner decision.

## Required Resources
Read `agents/product-facilitator.md`, `agents/product-editor.md`, STATUS,
product/experience sense, active opportunity and feature indexes, related
briefs, decision log, current-state inventory, and relevant sessions.

## Preconditions
A resolvable durable record or a session idea being considered for promotion. If
an ID cannot resolve, route to `$product-landscape`; if the thought is still
raw, route to `$product-talk`.

## Workflow
1. Treat a free brainstorm as a session idea, not a new ID.
2. Before promotion, compare its user, situation, outcome, constraints, and
   interaction hypothesis against existing OPP/FEATURE records, accepted
   decisions, and CURRENT evidence.
3. Cite concrete IDs and label every inferred overlap/conflict as `proposed`.
4. Ask one resolution question: merge, extend, split, supersede, keep distinct,
   defer, or reject.
5. Only after explicit owner confirmation, update `related_records`,
   `decision_refs`, `current_capability_refs`, `alignment_status`, the relevant
   brief, and the session summary.
6. Run `product-harness reconcile <target> --record <ID>` and regenerate the
   landscape after canonical records change.
If the precondition cannot be satisfied, use the stated route instead of
creating a record.

## Documentation Rules
Use only OPP and FEATURE for durable product work. Keep raw thoughts and
discarded early alternatives in sessions/rejected ideas; do not create IDEA IDs.
Relations use: `duplicates`, `overlaps`, `depends_on`, `conflicts_with`,
`extends`, `supersedes`, or `split_from`. A relation requires a rationale and
is `proposed` until confirmed by the owner.

## Validation
`$product-validate` rejects unknown, self-referential, duplicate, or malformed
relations and invalid CURRENT/DEC references. Reports never mutate records.

## Output Contract
Report cited records, proposed/confirmed relationships, alignment signals, one
recommended resolution question, and files changed only after confirmation. End
with exactly one `Recommended next focus:`.
