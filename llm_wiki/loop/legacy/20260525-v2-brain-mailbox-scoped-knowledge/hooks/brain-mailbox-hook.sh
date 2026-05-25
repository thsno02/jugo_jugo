#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
cd "$ROOT"

EVENT="${CODEX_HOOK_EVENT:-manual}"
python3 llm_wiki/loop/tools/brainctl.py hook --event "$EVENT" >/dev/null
