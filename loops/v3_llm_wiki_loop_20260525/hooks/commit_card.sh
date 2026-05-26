#!/usr/bin/env bash
# PostToolUse hook helper: when a draft card under v3 is written or edited,
# stage that card + its matching provenance/similarity sibling and commit.
#
# Reads Claude Code's PostToolUse stdin JSON, extracts the file path, and only
# acts on paths under loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards/*.md
# (excluding README.md). Idempotent: silently no-ops if no diff to commit.
#
# Does NOT use --no-verify, --amend, or git config changes.
set -uo pipefail

REPO_ROOT="/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo"
CARDS_DIR_FRAGMENT="loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards"

raw_path="$(jq -r '.tool_response.filePath // .tool_input.file_path // empty' 2>/dev/null)"
if [ -z "$raw_path" ]; then
  exit 0
fi

case "$raw_path" in
  */"$CARDS_DIR_FRAGMENT"/*.md) : ;;
  "$CARDS_DIR_FRAGMENT"/*.md) : ;;
  *) exit 0 ;;
esac

case "$raw_path" in
  *"/README.md") exit 0 ;;
esac

cd "$REPO_ROOT" || exit 0

# Normalize to repo-relative path.
case "$raw_path" in
  "$REPO_ROOT"/*) rel="${raw_path#"$REPO_ROOT"/}" ;;
  /*) exit 0 ;;
  *) rel="$raw_path" ;;
esac

case "$rel" in
  "$CARDS_DIR_FRAGMENT"/*.md) : ;;
  *) exit 0 ;;
esac

id="$(basename "$rel" .md)"
prov="loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/provenance/${id}.md"
sim="loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/similarity/${id}.json"

# Serialize git operations across parallel hook invocations.
LOCK_DIR="${TMPDIR:-/tmp}/v3-commit-card.lock"
deadline=$(( $(date +%s) + 60 ))
while ! mkdir "$LOCK_DIR" 2>/dev/null; do
  if [ "$(date +%s)" -ge "$deadline" ]; then
    exit 0
  fi
  sleep 0.2
done
trap 'rmdir "$LOCK_DIR" 2>/dev/null' EXIT

git add -- "$rel" 2>/dev/null || exit 0
[ -f "$prov" ] && git add -- "$prov" 2>/dev/null
[ -f "$sim" ] && git add -- "$sim" 2>/dev/null

if git diff --cached --quiet; then
  exit 0
fi

git commit -m "v3 draft card: ${id}" >/dev/null 2>&1 || true
exit 0
