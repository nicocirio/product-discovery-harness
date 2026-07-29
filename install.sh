#!/usr/bin/env bash
set -euo pipefail
CHANNEL="${1:-stable}"; REPO_PATH="${PRODUCT_HARNESS_REPO_PATH:-$HOME/.local/share/product-discovery-harness}"; REPO_URL="${PRODUCT_HARNESS_REPO_URL:-https://github.com/nicocirio/product-discovery-harness.git}"
mkdir -p "$(dirname "$REPO_PATH")"
if [[ ! -d "$REPO_PATH/.git" ]]; then git clone "$REPO_URL" "$REPO_PATH"; fi
exec env PRODUCT_HARNESS_REPO_PATH="$REPO_PATH" PRODUCT_HARNESS_REPO_URL="$REPO_URL" "$REPO_PATH/bin/product-harness-install" "$CHANNEL"
