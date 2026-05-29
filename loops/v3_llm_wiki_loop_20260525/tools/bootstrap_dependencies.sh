#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/../../.."

python3 -m pip install --user -r loops/v3_llm_wiki_loop_20260525/tools/requirements.txt

python3 - <<'PY'
import jieba
print("jieba ok", getattr(jieba, "__version__", "unknown"))
PY
