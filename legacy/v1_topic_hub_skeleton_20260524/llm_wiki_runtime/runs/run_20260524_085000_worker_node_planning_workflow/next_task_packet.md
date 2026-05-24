# Next Task Packet

executor_role:: worker_executor
next_worker_kind:: generator
candidate_id:: cand_004_workflow
candidate_name:: llm_wiki_ingest_compile_query_lint_workflow
target_node_id:: 20260524_084000_llm_wiki_ingest_compile_query_lint_workflow
version_target:: 1.0
source_mining_readiness_run:: .llmwiki/runs/run_20260524_084000_worker_source_mining_workflow

## Objective

Generate the first version bundle for `cand_004_workflow`, a bounded LLM Wiki workflow node covering ingest/source intake, compile/wiki update, query/synthesis, lint/health-check, update/file-back, and index/log maintenance.

## Allowed Inputs

- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/source_mining.md`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/loop_delivery.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/evidence_scope.yaml`
- `kb/_index.yaml`
- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/{card.md,provenance.md,change.md}`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/{card.md,provenance.md,change.md}`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/{card.md,provenance.md,change.md}`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- Secondary reports only as scoped in `evidence_scope.yaml`: `reports/source_gap_review.md`, `reports/coverage_framework.md`.

## Forbidden Inputs

- Network retrieval or newly fetched web sources.
- Unscoped implementation ecosystem sources.
- Unscoped enterprise, benchmark, adoption, social metric, governance, or broad comparison sources.
- Controller drift sample artifacts unless independently worker-reviewed and explicitly scoped.

## Required Outputs

Write only these version-bundle paths:

- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/provenance.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/change.md`

Do not write, copy, symlink, or adopt root `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/node.yaml`. Root metadata is created only after citation/adoption audit passes.

## Content Boundaries

The card should center on:

- ingest/source intake from curated raw sources
- compile/wiki update into durable markdown/wiki artifacts
- query/synthesis over the compiled wiki
- lint/health-check for contradictions, stale claims, orphan pages, missing concepts, missing cross-references, citation/provenance issues, and gaps
- update/file-back of valuable answers and approved outputs
- index/log maintenance as navigation and operation-history infrastructure
- implementation details from atomicstrata and ClawHub only when directly mined and clearly labeled as implementation variants

The card must not claim enterprise readiness, ecosystem maturity, adoption, empirical effectiveness, scale/reliability, benchmark results, or broad superiority/comparison against adjacent systems.

## Audit Gates For Generated Bundle

- Object-topic gate: generated node is about `cand_004_workflow`, not a hub ecosystem or comparison node.
- Source-scope gate: all claims stay within `evidence_scope.yaml`.
- Citation gate: citations point to scoped sources and do not cite secondary reports as primary workflow authority.
- Provenance gate: provenance distinguishes primary gist evidence, adopted KB anchors, implementation examples, and secondary reports.
- Overclaim gate: no enterprise, adoption, empirical, scale, or broad comparison claims.
- Retrieval gate: no new retrieval needed or performed.
- Language gate: write the node in zh-CN, consistent with existing KB style.

## Completion Marker

Generator should report `LOOP_DONE` only after all four version-bundle files are written and self-checked. Otherwise report `LOOP_BLOCKED` with the missing gate or artifact.

