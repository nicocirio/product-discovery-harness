# Bug Fix Execution Record

## Expected vs Actual
- Expected: `product-harness-status` works after install.
- Actual: only skill links were installed, so the shell command was absent.

## TDD Evidence
- [x] AC-001 regression test failed before the command links existed.
- [x] Added safe links in `~/.local/bin` and symlink resolution in helper scripts.
- [x] AC-002 covers a second installer pass for existing checkouts.

## Verification
- [x] Targeted installation tests pass.
- [x] Full repository gates pass.

## Review
- [x] Checked collision behavior: unmanaged commands are not overwritten.
