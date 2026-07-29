# Backend

## Service Architecture

The package is a local CLI library with explicit filesystem boundaries; it does
not run a server or contact product systems.

## Backend Boundaries

Only documentation and harness metadata may change in a target during
discovery. Brownfield audit is read-only with respect to application code.
