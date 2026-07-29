# Testing

## Test Types

Pytest unit and filesystem integration tests cover detection, safe seeding,
record IDs, validation, handoff creation, and temporary-home installation.

## Required Gates

`pytest`, `make validate`, and `git diff --check` must pass. CI runs the same
commands on supported Python versions.
