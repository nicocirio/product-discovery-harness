# Architecture

## System Map

The distribution is a Python package plus small POSIX shell entrypoints.

`src/product_discovery_harness/` owns all target-repository behaviour:

- `cli` exposes bootstrap, audit, validate, ID, session, and handoff commands.
- `detection`, `seeding`, and `paths` safely establish a target contract.
- `records` and `ids` enforce durable product record semantics.
- `validation` validates YAML/Markdown contracts and cross references.
- `handoff` writes canonical product-owned specs and, only by explicit opt-in,
  a public, versioned Engineering Harness export.

`templates/` and `schemas/` are package data. `skills/` contains agent-facing
workflows; each refers to the installed package via its own location and never
assumes that the target repository is this checkout. `bin/` is responsible only
for installation, update, status, and validation delegation.

`docs/product-discovery/` and `docs/product-specs/` are Product Discovery
Harness domains. Engineering directories are external domains; the only allowed
write there is a marked compatibility export. The package has no network dependency during product discovery. Installation
uses Git only to acquire or update the reusable harness checkout.
