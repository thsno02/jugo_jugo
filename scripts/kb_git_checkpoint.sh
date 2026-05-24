#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "usage: scripts/kb_git_checkpoint.sh <message> [trailers...]" >&2
  exit 2
fi

message="$1"
shift || true

git add .llmwiki generated kb nodes scripts/kb_*.py scripts/kb_git_checkpoint.sh
git commit -m "$message" "$@"
