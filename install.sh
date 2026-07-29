#!/usr/bin/env bash
set -euo pipefail
CHANNEL="${1:-stable}"; REPO_PATH="${PRODUCT_HARNESS_REPO_PATH:-$HOME/.local/share/product-discovery-harness}"; REPO_URL="${PRODUCT_HARNESS_REPO_URL:-https://github.com/nicocirio/product-discovery-harness.git}"
mkdir -p "$(dirname "$REPO_PATH")"
if [[ "${PRODUCT_HARNESS_LOCAL_CHECKOUT:-}" != "1" ]]; then
  if [[ ! -d "$REPO_PATH/.git" ]]; then git clone "$REPO_URL" "$REPO_PATH"; fi
  git -C "$REPO_PATH" fetch --tags --force origin
  if [[ "$CHANNEL" == "stable" ]]; then
    REF="$(git -C "$REPO_PATH" tag --sort=-v:refname | head -1)"
    [[ -n "$REF" ]] || { echo "error: stable requires at least one version tag" >&2; exit 1; }
    git -C "$REPO_PATH" checkout --detach "$REF" >/dev/null
  else
    git -C "$REPO_PATH" checkout -B main origin/main >/dev/null
  fi
fi
exec env PRODUCT_HARNESS_REPO_PATH="$REPO_PATH" PRODUCT_HARNESS_REPO_URL="$REPO_URL" PRODUCT_HARNESS_LOCAL_CHECKOUT="${PRODUCT_HARNESS_LOCAL_CHECKOUT:-}" "$REPO_PATH/bin/product-harness-install" "$CHANNEL"
