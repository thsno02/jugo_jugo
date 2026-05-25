# Provenance

node_id:: 20260524_062000_llm_wiki_origin_and_canon
version:: 1.0

## Why this version exists

This candidate version exists to create the first bounded origin/canon node for `cand_001_origin_and_canon`, which the worker-attributed frontier marks as `ready_to_build`.

Source-backed observation: the allowed gist directly describes the LLM Wiki idea-file pattern, architecture, operations, index/log navigation, and optional tooling boundary.

Discourse note: the allowed HN text directly records immediate public discussion around the idea, including visible story metadata and debate about whether the pattern is RAG, persistent memory, or a maintained wiki/write loop.

Process rationale: the repaired generation packet requires first-version outputs under `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/` and forbids root adoption metadata.

## Inputs used

### Existing data

Read and used:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.json`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`

Used as primary evidence:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`

Used as secondary early-discourse evidence:

- `data/raw/hacker_news/hacker-news-original-thread/text.txt`

Used only as gap/inventory checks:

- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.json`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`

Repair note: the generation run incorrectly recorded the X files and HN item JSON as empty. Current repair verification found `text.txt`, `raw.txt`, and `raw.json` under `karpathy-x-launch-post` are present and non-empty, and `hacker-news-original-thread/item.json` is present and non-empty.

### Dynamic retrieval, if any

None. No network retrieval was performed.

### Prior KB nodes

None. No prior KB nodes were read or used as evidence.

### Process artifacts

Read and used as process constraints:

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`
- `.llmwiki/skills/llmwiki-provenance-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-change-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/next_task_packet.md`
- `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/evidence_scope.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/planner_report.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/source_scope.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/source_mining.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/retrieval_requests.md`
- `.llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/mining_trace.md`

Out-of-scope reads: none.

## Production rationale

The card is written in Chinese because the control gates set `main_language: zh-CN`. It is scoped as an object-level topic node rather than a protocol or run-log node.

The synthesis keeps four categories separate:

- Source-backed observations from the gist.
- Working definition inferred from the gist.
- Early discourse notes from HN.
- Evidence gaps and forbidden claims from planning/mining process artifacts.

## Citation rationale

Primary canonical claims cite `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` because it is the only allowed source that directly describes the LLM Wiki pattern.

Early discussion claims cite `data/raw/hacker_news/hacker-news-original-thread/text.txt` because it is the only allowed source for immediate public discourse.

Evidence-boundary and gap claims cite the worker planning/mining process artifacts, not as topic evidence, but as process authority for what this candidate may and may not claim.

## Synthesis decisions

Working definition: the phrase "保留 raw sources、由 LLM 编译并持续维护、受 schema/instructions 约束的持久知识层" is a synthesis from the gist's raw/wiki/schema architecture and persistent wiki maintenance claims.

Interpretation: the node says the distinctive emphasis is the durable writeback/maintenance loop. This is supported by the gist and echoed by HN debate, but it is not used to settle a full RAG comparison.

Discourse handling: HN comments are treated as early discourse, not as technical ground truth.

Gap handling: X is treated as bounded launch-context/source-inventory evidence rather than as adoption, ecosystem, enterprise, or empirical-effectiveness evidence.

## Audit trail

- `gate_004_generation_entry_to_bundle_generation` passed in `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/generation_entry_gate.md`.
- This generation run wrote all four required version bundle files under `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/`.
- This generation run did not write `nodes/20260524_062000_llm_wiki_origin_and_canon/node.yaml`.
- This generation run did not write `kb/` or `generated/`.

## Adoption rationale

Adoption is pending audit. This version is acceptable as a candidate because its substantive claims are bounded to the allowed gist and HN text, and its evidence gaps are explicit.

This version is not adopted because citation/adoption audit has not yet passed. Root metadata and adopted KB views must be created only by a later adoption step if the audit decision is `adopt`.

## Limits and uncertainty

Evidence boundary: X raw files are present in the current checkout and can support bounded launch-context/source-inventory checks, but this version still does not use X to claim adoption, implementation ecosystem, enterprise suitability, or empirical effectiveness.

Evidence boundary: HN `item.json` is present in the current checkout and can support structured story metadata; HN comments remain discourse evidence rather than technical proof.

Evidence gap: pre-Karpathy historical lineage is not established by this batch.

Evidence gap: adoption, implementation ecosystem, enterprise suitability, empirical effectiveness, and governance claims require separate mining.

Interpretation limit: the working definition should be reviewed when the dedicated working-definition node is generated.

## Revision triggers

- X launch post capture materially changes or conflicts with the current local snapshot.
- HN structured JSON materially changes or conflicts with the current local snapshot.
- A dedicated historical-lineage batch changes the bounded origin framing.
- Separate implementation, adoption, risk, governance, or evaluation source mining introduces material constraints.
- Citation/adoption audit finds parser failures, unsupported claims, or adoption-boundary violations.
