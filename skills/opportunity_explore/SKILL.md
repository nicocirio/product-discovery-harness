---
name: product-opportunity-explore
description: Explore one opportunity through focused conversation.
examples: ["$product-opportunity-explore OPP-001"]
when_to_use: ["An opportunity needs evidence and outcome depth."]
when_not_to_use: ["The ID does not resolve."]
---
## Purpose
Clarify user, frequency, severity, trigger, workaround, desired outcome, inaction cost, alignment, constraints, uncertainty, and edge cases.
## Preconditions
A resolvable opportunity. If its ID is unknown, route to `$product-landscape`;
if the thought is not durable enough to have an opportunity yet, route to
`$product-talk`.
## Workflow
Ask one primary question at a time and update brief, assumptions, questions, and session history.
## Output Contract
Report evidence gaps and exactly one `Recommended next focus:`; name experience
exploration only when the outcome is sufficiently clear.
