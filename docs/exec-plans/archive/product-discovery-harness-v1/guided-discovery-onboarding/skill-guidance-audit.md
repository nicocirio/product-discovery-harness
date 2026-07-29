# Product Skill Guidance Audit

Date: 2026-07-29
Scope: all installed `product-*` skills. This is a protocol audit, not an
implementation change. “Guides” means that the skill either asks a meaningful
next question or explicitly recommends a next focus without assuming the owner
already knows the workflow.

## Summary

- Skills audited: 19
- Explicitly guide or route the next step: 7
- Safely conversational but missing an explicit next-step recommendation: 6
- Specialist operations that appropriately require a precondition: 6

The entry skills are mostly sound: bootstrap routes by mode, talk records a
recommended focus, and resume offers a question or landscape. The main gap is
not that specialist skills exist; it is that several complete their narrow task
without consistently returning the owner to a clear next decision. A later
behavior-change work item should add a shared “recommended next focus” output
to every conversational skill and offer intent-first routing when a supplied ID
does not resolve.

## Findings by Skill

| Skill | Guidance posture | Evidence in current protocol | Assumed owner knowledge | Recommendation |
| --- | --- | --- | --- | --- |
| `$product-bootstrap` | Guides | Chooses mode with owner when pending; recommends audit or talk. | Only target location/mode if evidence is inconclusive. | Keep as model for explicit routing. |
| `$product-resume` | Guides | Summarizes state, asks one high-leverage question or recommends landscape. | None beyond a bootstrapped target. | Keep as the returning-user entry point. |
| `$product-talk` | Guides | Asks one significant question and outputs a recommended next focus. | None; accepts open-ended intent. | Keep as the primary entry point; make the next-focus wording prominent in agent output. |
| `$product-focus` | Partial | Resolves a topic, asks one high-leverage question, and returns a next question. | User may know an ID or a resolvable topic. | When a topic cannot resolve, route to landscape instead of stopping. |
| `$product-synthesize` | Partial | Separates certainty and asks one confirmation question. | Owner knows enough context exists. | Add an explicit recommendation after confirmation or deferral. |
| `$product-landscape` | Guides | Produces a summary and one recommended next focus. | Bootstrapped target only. | Keep; make it the standard ID-recovery route. |
| `$product-reconcile` | Guides | Compares prior thinking and asks one owner resolution question. | A durable record exists, or a session idea can be identified. | Add a clearer path from raw session idea to the record being compared. |
| `$product-review` | Partial | Produces prioritized findings and remediation proposals. | A discovery corpus exists. | End with one recommended next focus, not only a report. |
| `$product-audit` | Guides | Requires brownfield and recommends review-current-state. | Brownfield mode and repository scope. | Keep explicit mode error and routing. |
| `$product-review-current-state` | Partial | Identifies the next strategic conversation. | Audit findings exist. | Name the recommended skill or question in the output contract. |
| `$product-opportunity-map` | Specialist | Creates portfolio records and reconciles before creation. | Owner has identified a problem/outcome worthy of durable tracking. | Add a plain-language preflight: if the thought is raw, route to talk. |
| `$product-opportunity-explore` | Guides | Asks one primary question and reports recommended experience next step. | A resolvable opportunity ID. | When ID is absent, tell the owner to use landscape or talk first. |
| `$product-experience-north` | Partial | Seeks confirmation for durable principles. | The owner knows global experience principles are the topic. | End with a suggested application or next question. |
| `$product-experience-explore` | Partial | Reports concepts and a next evaluation question. | A mature opportunity, outcome, and experience direction. | Add a preflight that routes insufficiently defined work to opportunity exploration. |
| `$product-experience-evaluate` | Specialist | Records explicit selection, tradeoffs, and next experiment. | Divergent concepts already exist. | State the recommended post-selection route, such as crystallization or experiment. |
| `$product-feature-crystallize` | Specialist | Allocates feature record after a selected opportunity direction. | A selected direction and source opportunity exist. | Add a preflight and next-focus output; do not imply it is the routine next command after talk. |
| `$product-slice` | Specialist | Organizes accepted features into releases. | Accepted features already exist. | Report the next release decision or handoff readiness check. |
| `$product-handoff` | Specialist | Checks readiness, writes spec, optionally prints harness-analyze after export. | Accepted feature and Definition of Ready are complete. | For non-ready features, give the highest-priority missing product step. |
| `$product-validate` | Specialist | Converts diagnostics into remediation actions. | Bootstrapped target. | Include a single recommended remediation focus after multiple diagnostics. |

## Cross-Cutting Recommendations

1. Keep `$product-talk` and `$product-resume` as the public default entry
   points. The README should never make users select among nineteen skills
   before they can express an idea.
2. Define a shared output contract for conversational skills: current
   understanding, one question or decision, files changed, and one recommended
   next focus. `talk`, `resume`, `landscape`, and `opportunity-explore` already
   provide much of this pattern.
3. Define friendly off-ramps for specialist preconditions. A missing or unknown
   ID should lead to `$product-landscape`; a raw thought should lead to
   `$product-talk`, not an unexplained refusal.
4. Preserve specialist boundaries. Opportunity understanding, divergent
   experience exploration, and feature crystallization are distinct decisions;
   they should be optional branches, not a mandatory ritual.
5. Create a separate implementation work item before changing any SKILL.md
   behavior, templates, or CLI output.
