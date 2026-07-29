---
name: product-landscape
description: Generate a compact, trustworthy overview of active product ideas and what needs attention.
examples:
  - "$product-landscape"
  - "$product-landscape --stale-after-days=45"
when_to_use:
  - "The product owner asks how product ideas are progressing."
  - "Discovery needs a concise orientation view before choosing the next conversation."
when_not_to_use:
  - "A target has not been bootstrapped."
  - "The goal is to change a record's lifecycle without human review."
---
## Purpose
Generate `docs/product-discovery/PRODUCT_LANDSCAPE.md`: a derived view of
indexed opportunities and features with real document links, lifecycle/next
action, and time since meaningful review.

## Required Resources
Read `product-harness.yml`, opportunity and feature indexes, `STATUS.md`, and
`agents/product-editor.md`.

## Preconditions
The target has been bootstrapped. Index entries that should be shown need stable
IDs and should provide title, target-relative `path`, and review dates.
If the target is not bootstrapped, route to `$product-bootstrap` rather than
trying to infer records.

## Workflow
1. Run `product-harness landscape <target> --stale-after-days 30`.
2. Read the generated summary and “Needs attention” section.
3. Treat missing paths as documentation work, not as proof that an idea is invalid.
4. For each stale item, ask one decision question: revisit, keep deferred with a
   review trigger, supersede, or reject with rationale.
5. Update the canonical index/detail record only after the owner responds; then
   regenerate the landscape.

## Documentation Rules
`PRODUCT_LANDSCAPE.md` is generated and is never canonical. The index records
and their linked files remain canonical. Generation never updates
`last_reviewed_at`, changes a lifecycle state, or depends on Engineering Harness.
An old item is a review signal, never an automatic discard rule.

## Validation
Run `$product-validate` after changing canonical records. The command marks
missing documents rather than inventing Markdown links.

## Output Contract
Report output path, record count, records requiring review, missing documents,
and exactly one `Recommended next focus:`.
