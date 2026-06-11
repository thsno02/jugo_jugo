#!/usr/bin/env bash
# One-shot helper to commit v3 adoption-stage bookkeeping after a session.
set -uo pipefail
cd .

git add loops/v3_llm_wiki_loop_20260525/loop_state.json
git add loops/v3_llm_wiki_loop_20260525/status.json
git add loops/v3_llm_wiki_loop_20260525/reports/loop_report.md
git add loops/v3_llm_wiki_loop_20260525/brains/audit/brain_state.json
git add loops/v3_llm_wiki_loop_20260525/brains/audit/queue.jsonl
git add loops/v3_llm_wiki_loop_20260525/brains/audit/wake_required.json
git add loops/v3_llm_wiki_loop_20260525/brains/ops/brain_state.json
git add loops/v3_llm_wiki_loop_20260525/brains/ops/queue.jsonl
git add loops/v3_llm_wiki_loop_20260525/brains/ops/outbox.jsonl
git add loops/v3_llm_wiki_loop_20260525/brains/similarity/wake_required.json
git add loops/v3_llm_wiki_loop_20260525/hooks/commit_card.sh
git add loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md
git add loops/v3_llm_wiki_loop_20260525/tools/build_kb_index.py
git add loops/v3_llm_wiki_loop_20260525/tools/build_kb_index.sh
git add loops/v3_llm_wiki_loop_20260525/tools/build_adopt_batches.py
git add loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md

git commit -m "v3: adoption complete for all 171 cards

- 163 new_card via publication_gate, 8 provenance_delta via fusion_audit
- kb/cards/ and kb/provenance/ populated; kb/indexes/cards.md built
- 8 v2-anchored cards carry v2_anchor field in kb provenance
- hook extended to auto-commit kb/cards/<id>.md with sibling provenance
- new template: adoption_worker_prompt.md
- new tools: build_kb_index.py + build_kb_index.sh + build_adopt_batches.py
- loop_state/status/report and audit/ops/similarity brain mailboxes synced"
