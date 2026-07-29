# Tooling

## Commands

- `make test` — run pytest.
- `make validate` — verify target-contract validation with seeded temporary
  targets and invalid configuration fixtures.
- `python -m product_discovery_harness.cli validate <target>` — validate any
  target product repository.
- `python -m product_discovery_harness.cli bootstrap <target>` — safely seed a
  target repository.

## Required Gates

Run formatting-free unit tests, target validation, and the applicable
Engineering Harness work-item validator before a release.
