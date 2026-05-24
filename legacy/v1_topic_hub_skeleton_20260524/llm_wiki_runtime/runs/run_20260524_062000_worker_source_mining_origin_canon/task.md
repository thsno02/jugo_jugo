# Worker Task Packet

run_id:: run_20260524_062000_worker_source_mining_origin_canon
executor_role:: worker_executor
phase:: source_mining
skill:: llmwiki-source-mining
orchestration_skill:: llmwiki-loop-orchestration
created_at:: 2026-05-24T06:20:00+08:00
status:: LOOP_DONE

## Task

Execute an independent origin/canon source-mining review/rerun for `cand_001_origin_and_canon`, repairing the prior controller drift in `run_20260524_061000_source_mining_origin_canon`.

## Task Packet

- Re-read the orchestration gate and source-mining contracts.
- Use only the allowed local evidence listed below.
- Produce worker-attributed source-mining artifacts in this run directory.
- Do not update `.llmwiki/control/knowledge_frontier.yaml`.
- Do not generate node/card/provenance/change artifacts.
- Do not modify `nodes/`, `kb/generated/`, or other run/control artifacts.
- Do not use network retrieval.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-source-mining/SKILL.md`
- `.llmwiki/skills/llmwiki-loop-orchestration/SKILL.md`
- `.llmwiki/runs/run_20260524_061000_source_mining_origin_canon/loop_status.md`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.json`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`
- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`
- `.llmwiki/runs/run_20260524_061000_source_mining_origin_canon/*` as non-authoritative reference only

## Forbidden Actions

- No frontier merge.
- No KB node generation.
- No card/provenance/change generation.
- No direct adoption of prior controller-authored artifacts.
- No web retrieval.

## Outputs Written

- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/task.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/source_scope.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/source_mining.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/retrieval_requests.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/mining_trace.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/loop_status.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/loop_delivery.md`

