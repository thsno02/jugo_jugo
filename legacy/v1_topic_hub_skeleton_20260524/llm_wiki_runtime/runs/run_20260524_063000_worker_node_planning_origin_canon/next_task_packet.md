# Next Task Packet

executor_role:: worker_executor
phase:: version_bundle_generation
handoff_from:: run_20260524_063000_worker_node_planning_origin_canon
source_task_packet:: .llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/task.md
target_candidate_id:: cand_001_origin_and_canon
candidate_frontier_source:: .llmwiki/control/knowledge_frontier.yaml
candidate_status_required:: ready_to_build
target_node_id:: 20260524_062000_llm_wiki_origin_and_canon
target_node_id_basis:: frontier current proposed_node_id
target_node_slug:: llm_wiki_origin_and_canon
version_target:: 1.0

## Objective

Generate the first version bundle for the bounded LLM Wiki origin/canon node.

## Candidate Authority

Use only `cand_001_origin_and_canon` from `.llmwiki/control/knowledge_frontier.yaml`.

This candidate was made ready by worker source mining run `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon` and accepted into the frontier by worker frontier update run `.llmwiki/runs/run_20260524_062500_worker_frontier_update_origin_canon`.

## Allowed Inputs

- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/planner_report.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/source_scope.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/source_mining.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/retrieval_requests.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/mining_trace.md`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`
- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.json`

## Evidence Use Rules

- Treat `karpathy-gist-llm-wiki` as the primary canonical source.
- Use `hacker-news-original-thread/text.txt` only for immediate early discourse and visible story metadata.
- Treat `karpathy-x-launch-post` only as source inventory/provenance because its allowed raw files are empty.
- State X limitation clearly if mentioning the X capture.

## Forbidden Inputs And Claims

- Do not retrieve network sources.
- Do not use topic plans, static backlog, or controller-authored drift artifacts as evidence authority.
- Do not use X raw files for exact wording, timestamps, quoted-post text, or social metrics.
- Do not claim pre-Karpathy historical lineage.
- Do not claim broad adoption, ecosystem completeness, enterprise readiness, or empirical effectiveness.
- Do not use Reddit/community reception for this node.
- Do not expand into full comparison, risk/governance, architecture ecosystem, or evaluation nodes.

## Required Outputs For Generator

- `nodes/20260524_062000_llm_wiki_origin_and_canon/node.yaml`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/provenance.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/change.md`

## Audit Gates For Generator

- Object topic gate: node stays about bounded origin/canon.
- Source scope gate: every claim traces to allowed inputs.
- Citation gate: primary canonical claims cite gist; early discourse claims cite HN text.
- Provenance gate: worker source mining and frontier update runs are named.
- Overclaim gate: X, adoption, historical lineage, enterprise, and empirical claims remain bounded.
- Retrieval gate: no new retrieval is performed.
- Language gate: main narrative language is zh-CN unless existing KB conventions require otherwise.

## Completion Marker

Generator should write `LOOP_DONE` only after all four bundle artifacts exist and satisfy the gates. Otherwise write `LOOP_BLOCKED` with the blocker.
