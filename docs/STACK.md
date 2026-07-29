# Stack

## Languages

Python 3.10+ for the CLI, validation, and tests; POSIX-compatible Bash for
installer entrypoints; Markdown, YAML, and JSON Schema for durable contracts.

## Frameworks

The runtime is deliberately framework-free. PyYAML and jsonschema are the only
runtime dependencies; pytest is used for automated tests.

## Storage

Target repositories store discovery state as versioned files. No database,
service, secret, or remote API is required.
