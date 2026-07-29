<!-- product-discovery-harness:seeded -->
# Documentation map

## Product Discovery Harness owns

- `PRODUCT_SENSE.md` and `EXPERIENCE_SENSE.md`: stable product/experience guidance.
- `product-discovery/`: evidence, strategy, opportunities, features, decisions,
  sessions, and generated landscape.
- `product-specs/`: canonical accepted product feature specs.

## Engineering Harness owns

- `exec-plans/`: engineering analysis, design, planning, implementation, and evidence.
- `design-docs/`, `generated/`, and technical documentation.

## Compatibility boundary

Product Discovery Harness exports an `informal.md` under `exec-plans/` only by
explicit opt-in. It never modifies other engineering artifacts. Canonical
product truth remains in `product-specs/`.

## Where to look

| Question | Read |
| --- | --- |
| How are product ideas progressing? | `product-discovery/PRODUCT_LANDSCAPE.md` |
| Where do ideas overlap or need alignment? | `product-discovery/CONSISTENCY_REPORT.md` |
| What needs definition? | `product-discovery/STATUS.md` |
| What product feature is accepted? | `product-specs/` |
| What is engineering doing? | `exec-plans/`, if used |
