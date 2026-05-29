#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/../../.."
python3 loops/v3_llm_wiki_loop_20260525/tools/build_kb_index.py
