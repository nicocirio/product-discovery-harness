# Security

## Requirements

Treat target paths as untrusted input: resolve them before writes, preserve
substantive content by default, and never execute application code during audit.
No private-network calls or production credentials are used by this harness.
