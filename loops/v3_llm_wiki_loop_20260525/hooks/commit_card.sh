#!/usr/bin/env bash
# PostToolUse hook helper: when a draft artifact under v3 is written or edited,
# stage that artifact (plus its siblings, for cards) and commit.
#
# Reads Claude Code's PostToolUse stdin JSON, extracts the file path, and acts
# on either:
#   - .../drafts/cards/<id>.md       -> commit card + matching provenance + matching similarity
#   - .../drafts/comparison/<id>.md  -> commit just the comparison file
#
# Idempotent: silently no-ops if no diff to commit. Does NOT use --no-verify,
# --amend, or git config changes. Serializes via /tmp/v3-commit-card.lock so
# parallel workers cannot race on .git/index.lock.
set -uo pipefail

REPO_ROOT="/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo"
CARDS_FRAG="loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards"
COMPARISON_FRAG="loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/comparison"

raw_path="$(jq -r '.tool_response.filePath // .tool_input.file_path // empty' 2>/dev/null)"
if [ -z "$raw_path" ]; then
  exit 0
fi

kind=""
case "$raw_path" in
  */"$CARDS_FRAG"/*.md|"$CARDS_FRAG"/*.md) kind="card" ;;
  */"$COMPARISON_FRAG"/*.md|"$COMPARISON_FRAG"/*.md) kind="comparison" ;;
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

case "$kind" in
  card)
    case "$rel" in "$CARDS_FRAG"/*.md) : ;; *) exit 0 ;; esac
    ;;
  comparison)
    case "$rel" in "$COMPARISON_FRAG"/*.md) : ;; *) exit 0 ;; esac
    ;;
esac

id="$(basename "$rel" .md)"

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

if [ "$kind" = "card" ]; then
  prov="loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/provenance/${id}.md"
  sim="loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/similarity/${id}.json"
  git add -- "$rel" 2>/dev/null || exit 0
  [ -f "$prov" ] && git add -- "$prov" 2>/dev/null
  [ -f "$sim" ] && git add -- "$sim" 2>/dev/null
  msg="v3 draft card: ${id}"
else
  git add -- "$rel" 2>/dev/null || exit 0
  msg="v3 comparison provenance: ${id}"
fi

if git diff --cached --quiet; then
  exit 0
fi

git commit -m "$msg" >/dev/null 2>&1 || true
exit 0
