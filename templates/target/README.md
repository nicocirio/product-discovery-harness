<!-- product-discovery-harness:seeded -->
# Documentation map

## Product Discovery Harness owns

- `PRODUCT_SENSE.md` and `EXPERIENCE_SENSE.md`: stable product/experience guidance.
- `product-discovery/`: current evidence, strategy, opportunities, features,
  decisions, sessions, and generated product landscape.
- `product-specs/`: canonical accepted product feature specs.

## Engineering Harness owns

- `exec-plans/`: engineering analysis, architecture, plans, implementation, and evidence.
- `design-docs/`, `generated/`, and technical documentation.

## Compatibility boundary

Product Discovery Harness may generate an `informal.md` export under
`exec-plans/` only through explicit opt-in. It never modifies other engineering
artifacts. The canonical source remains `product-specs/`.

## Where to look

| Question | Read |
| --- | --- |
| How are product ideas progressing? | `product-discovery/PRODUCT_LANDSCAPE.md` |
| Where do ideas overlap or need alignment? | `product-discovery/CONSISTENCY_REPORT.md` |
| What needs definition? | `product-discovery/STATUS.md` |
| What product feature is accepted? | `product-specs/` |
| What is engineering doing? | `exec-plans/` when Engineering Harness is used |
