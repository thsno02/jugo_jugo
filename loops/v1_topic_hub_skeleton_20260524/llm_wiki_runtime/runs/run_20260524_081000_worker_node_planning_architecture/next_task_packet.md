# Next Task Packet: Version Bundle Generation

task_id:: cand_003_architecture_generate_version_1_0
executor_role:: worker_executor
from_run:: run_20260524_081000_worker_node_planning_architecture
candidate_id:: cand_003_architecture
target_node_id:: 20260524_080000_llm_wiki_three_layer_architecture
version_target:: 1.0
source_mining_run:: .llmwiki/runs/run_20260524_080000_worker_source_mining_architecture

## Objective

Generate first-version KB bundle files for the LLM Wiki three-layer architecture node.

## Required Outputs

Write only these version-bundle paths:

- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/node.yaml`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/provenance.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/change.md`

Do not write or adopt root `nodes/20260524_080000_llm_wiki_three_layer_architecture/node.yaml`. Root metadata is created only after adoption audit passes.

## Allowed Inputs

Primary architecture source:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`

Prior KB anchors:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/provenance.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/change.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/provenance.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/change.md`
- `kb/_index.yaml`

Implementation-flavored sources:

- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`

Secondary process/report sources:

- `.llmwiki/runs/run_20260524_080000_worker_source_mining_architecture/source_mining.md`
- `.llmwiki/runs/run_20260524_080000_worker_source_mining_architecture/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_080000_worker_source_mining_architecture/loop_delivery.md`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`
- `.llmwiki/runs/run_20260524_081000_worker_node_planning_architecture/evidence_scope.yaml`

## Required Content Boundary

Build a bounded architecture node centered on:

- raw source layer;
- compiled markdown/wiki layer;
- schema/instruction layer;
- index/log/tooling/provenance/review/lint/search/CLI/MCP/viewer/storage only as supporting infrastructure or implementation variants.

## Forbidden Claims

Do not write:

- detailed ingest/compile/query/lint workflow as the main node;
- implementation ecosystem survey;
- enterprise, adoption, maturity, social-metric, or empirical claims;
- broad comparisons with RAG, GraphRAG, PKM, knowledge graphs, documentation systems, or agent memory;
- scale, governance, privacy, security, compliance, or risk conclusions;
- claims that implementation-specific tools are required by the abstract architecture.

## Audit Gates To Satisfy

- object topic: the node is about LLM Wiki three-layer architecture only;
- source scope: every claim stays inside `evidence_scope.yaml`;
- citation: layer claims cite primary gist evidence; implementation details cite implementation sources; boundaries cite prior KB anchors or secondary reports as appropriate;
- provenance: `provenance.md` records source roles, limitations, and synthesis status;
- overclaim: no enterprise, adoption, ecosystem, empirical, or broad comparison claims;
- retrieval: no network retrieval or unapproved new sources;
- language: main prose uses zh-CN with clear source-backed/worker-synthesis distinctions.

## Completion Marker

End generator delivery with `LOOP_DONE` if all required version-bundle files are written and self-checked. Use `LOOP_BLOCKED` if the generator cannot satisfy the evidence scope or output contract.
