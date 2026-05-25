# Task Packet

run_id:: run_20260524_084000_worker_source_mining_workflow
executor_role:: worker_executor
task_packet:: cand_004_workflow / llm_wiki_ingest_compile_query_lint_workflow source_mining_and_frontier_update
status:: LOOP_DONE

## Objective

Mine the bounded local evidence for `cand_004_workflow` and update the knowledge frontier so the controller can decide whether to dispatch node planning.

## Candidate

- candidate_id: `cand_004_workflow`
- proposed_node_slug: `llm_wiki_ingest_compile_query_lint_workflow`
- target decision: `ready_to_build` if evidence supports a bounded first version.

## Boundaries

- Include: ingest, compile, query, lint/health-check, update/writeback, file-back, index/log maintenance, review gates, and agent/runtime interfaces when directly supported.
- Exclude: node/card generation, adoption, broad implementation ecosystem survey, enterprise suitability, empirical effectiveness, scale claims, and broad RAG/PKM comparison.
- No network retrieval.

## Allowed Inputs Used

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-source-mining/SKILL.md`
- `.llmwiki/skills/llmwiki-frontier-management/SKILL.md`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_083000_worker_skill_eval_architecture/next_decision.md`
- `generated/status.yaml`
- `kb/_index.yaml`
- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`

