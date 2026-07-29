# Tech Debt Tracker

## Post-publication release check

- Add a remote smoke test that installs the public `install.sh` endpoint with
  `curl`, bootstraps a temporary target, and validates it. This is intentionally
  deferred until `nicocirio/product-discovery-harness` is public and has a
  release tag; local installer coverage remains the pre-publication gate.
