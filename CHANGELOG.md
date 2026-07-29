# Changelog

## 0.1.1 — 2026-07-29

- Expose `product-harness` and maintenance commands in `~/.local/bin` during
  install/update, with safe collision protection and symlink-aware entrypoints.
- Ensure normal installations refresh and select the requested stable/latest
  channel; reserve the local-checkout bypass for explicit development use.
- Refresh tags forcibly so an installed checkout can recover from a corrected
  release tag.

## 0.1.0 — 2026-07-28

- Initial end-to-end Product Discovery Harness: target contract, skills,
  local validation, evidence-based audit, sessions, handoff, installer, tests,
  and CI.
- Added product landscape generation with real document links, review-age
  signals, safe stale-record prompts, and no Engineering Harness dependency.
- Made product specs canonical and Engineering Harness handoffs optional,
  explicit compatibility exports with ownership-conflict protection.
- Added relationship validation and product reconciliation reports so durable
  opportunities/features can record proposed or confirmed overlap, conflict,
  decision, and current-capability alignment.
