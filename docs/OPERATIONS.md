# Operations

## Observability

CLI commands report every write, preserve error paths, and use non-zero exit
codes for invalid contracts. No telemetry leaves a target repository.

## Performance

Discovery validation is local and linear in the scoped files. Large repositories
are constrained by `repository_scope` and ignored dependency/build directories.

## Rollout

Skills are globally symlinked into collision-safe namespaces. `stable` selects
the newest tag and `latest` selects the default branch; updates repair links.
Engineering compatibility export is manual and off by default; it refuses to
overwrite an unmarked `informal.md`.

## Releases

Releases are maintainer-owned and manual. Update `version.json`,
`pyproject.toml`, and `CHANGELOG.md`; run `make test`, `make validate`, and
`git diff --check`; then commit and push an annotated `vX.Y.Z` tag with
`git push origin main --follow-tags`. Never tag a revision with a failing gate.
