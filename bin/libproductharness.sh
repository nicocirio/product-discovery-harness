#!/usr/bin/env bash

set -euo pipefail

PRODUCT_HARNESS_DEFAULT_REPO_PATH="${HOME}/.local/share/product-discovery-harness"
PRODUCT_HARNESS_DEFAULT_REPO_URL="https://github.com/nicocirio/product-discovery-harness.git"
PRODUCT_HARNESS_CONFIG_PATH="${PRODUCT_HARNESS_CONFIG_PATH:-${PRODUCT_HARNESS_DEFAULT_REPO_PATH}/.install-config}"

product_harness_die() { echo "error: $*" >&2; exit 1; }
product_harness_require_git() { command -v git >/dev/null || product_harness_die "git is required"; }
product_harness_require_python() { command -v python3 >/dev/null || product_harness_die "python3 is required"; }
product_harness_prepare_runtime() {
  local repo_path="$1"
  [[ -x "$repo_path/.venv/bin/python" ]] && return
  python3 -m venv "$repo_path/.venv"
  "$repo_path/.venv/bin/pip" install "PyYAML>=6.0" "jsonschema>=4.18"
}
product_harness_channel() { [[ "${1:-stable}" == stable || "${1:-stable}" == latest ]] || product_harness_die "channel must be stable or latest"; echo "${1:-stable}"; }
product_harness_version() { sed -n 's/.*"version"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$1/version.json"; }
product_harness_clone_or_fetch() {
  local repo_path="$1" repo_url="$2"
  if [[ -d "$repo_path/.git" ]]; then git -C "$repo_path" fetch --tags origin
  elif [[ -e "$repo_path" ]]; then product_harness_die "repo path exists but is not a git checkout: $repo_path"
  else mkdir -p "$(dirname "$repo_path")"; git clone "$repo_url" "$repo_path"; fi
}
product_harness_checkout_channel() {
  local repo_path="$1" channel="$2" ref
  if [[ "$channel" == stable ]]; then
    ref="$(git -C "$repo_path" tag --sort=-v:refname | head -1)"
    [[ -n "$ref" ]] || product_harness_die "stable requires at least one version tag; use latest for the default branch"
    git -C "$repo_path" checkout --detach "$ref" >/dev/null
  else
    ref="$(git -C "$repo_path" symbolic-ref --quiet --short refs/remotes/origin/HEAD 2>/dev/null || true)"
    ref="${ref#origin/}"; [[ -n "$ref" ]] || ref="main"
    git -C "$repo_path" checkout -B "$ref" "origin/$ref" >/dev/null
  fi
  git -C "$repo_path" rev-parse --short HEAD
}
product_harness_targets() {
  local roots=()
  [[ -d "$HOME/.agents/skills" ]] && roots+=("$HOME/.agents/skills")
  [[ -d "$HOME/.claude/skills" ]] && roots+=("$HOME/.claude/skills")
  if [[ ${#roots[@]} -eq 0 ]]; then mkdir -p "$HOME/.agents/skills"; roots=("$HOME/.agents/skills"); fi
  printf '%s\n' "${roots[@]}"
}
product_harness_namespace() {
  local root="$1" repo_path="$2" name="product-discovery-harness" count=0 candidate
  while :; do
    candidate="$root/$name"; [[ $count -gt 0 ]] && candidate="$root/${name}_$count"
    if [[ ! -e "$candidate" || -f "$candidate/.product-harness-install-root" ]]; then echo "$candidate"; return; fi
    count=$((count + 1))
  done
}
product_harness_link_target() {
  local repo_path="$1" namespace="$2" channel="$3" skill skill_name
  mkdir -p "$namespace"
  printf 'REPO_PATH=%s\nCHANNEL=%s\n' "$repo_path" "$channel" > "$namespace/.product-harness-install-root"
  for skill in "$repo_path"/skills/*; do
    [[ -f "$skill/SKILL.md" ]] || continue
    skill_name="$(sed -n 's/^name:[[:space:]]*//p' "$skill/SKILL.md" | head -1)"
    [[ -n "$skill_name" ]] && ln -sfn "$skill" "$namespace/$skill_name"
  done
  ln -sfn "$repo_path/bin/product-harness" "$namespace/product-harness"
  ln -sfn "$repo_path" "$namespace/product-discovery-harness-root"
}
product_harness_save_config() {
  local repo_path="$1" repo_url="$2" channel="$3" commit="$4" version="$5"
  mkdir -p "$(dirname "$PRODUCT_HARNESS_CONFIG_PATH")"
  local tmp_path="${PRODUCT_HARNESS_CONFIG_PATH}.tmp"
  printf 'REPO_PATH=%s\nREPO_URL=%s\nCHANNEL=%s\nCOMMIT=%s\nINSTALLED_VERSION=%s\n' "$repo_path" "$repo_url" "$channel" "$commit" "$version" > "$tmp_path"
  mv "$tmp_path" "$PRODUCT_HARNESS_CONFIG_PATH"
}
product_harness_load_config() {
  [[ -f "$PRODUCT_HARNESS_CONFIG_PATH" ]] || product_harness_die "no install metadata: $PRODUCT_HARNESS_CONFIG_PATH"
  REPO_PATH=""; REPO_URL=""; CHANNEL=""; COMMIT=""; INSTALLED_VERSION=""
  while IFS='=' read -r key value; do case "$key" in REPO_PATH|REPO_URL|CHANNEL|COMMIT|INSTALLED_VERSION) printf -v "$key" '%s' "$value";; esac; done < "$PRODUCT_HARNESS_CONFIG_PATH"
  [[ -n "$REPO_PATH" && -n "$CHANNEL" ]] || product_harness_die "invalid install metadata"
}
