# Provenance

node_id:: 20260524_084000_llm_wiki_ingest_compile_query_lint_workflow
version:: 1.0

## Why this version exists

This first version exists because `cand_004_workflow` reached `ready_to_build` with `evidence_state: enough_for_first_version` in the worker source-mining and node-planning artifacts. The bundle creates a candidate version for the bounded LLM Wiki maintenance workflow: ingest/source intake, compile/wiki update, query/synthesis, lint/health-check, update/file-back, and index/log maintenance.

This version is a candidate only. It does not adopt root metadata, write a `kb/` view, or update generated indexes.

## Inputs used

### Existing data

Read and used:

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`

### Dynamic retrieval, if any

None. No network retrieval was used.

### Prior KB nodes

Read and used as adopted anchors:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/provenance.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/change.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/provenance.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/change.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/provenance.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/change.md`
- `kb/_index.yaml`

### Process artifacts

Read and used:

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`
- `.llmwiki/skills/llmwiki-provenance-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-change-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/next_task_packet.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/source_mining.md`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_084000_worker_source_mining_workflow/loop_delivery.md`

Out-of-scope reads: none. `find`, `git status`, and local file inspection commands were used only to check whether target paths already existed and to avoid overwriting unrelated worker changes.

## Production rationale

The card centers on the workflow object named in the packet, not on origin, definition, architecture, ecosystem, enterprise readiness, or comparison. The Karpathy gist is treated as primary workflow evidence because it directly defines operations, index/log support, human guidance, and modular tooling boundaries. Prior adopted KB nodes are used only as anchors for canon, working definition, and raw/wiki/schema architecture. Atomicstrata and ClawHub are used as implementation/process examples where their local texts directly describe compile, review, query save, lint, CLI/MCP, representation readiness, source validation, deterministic writes, and gap promotion.

## Citation rationale

Primary workflow claims cite `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`. Existing KB dependencies cite adopted `kb/` paths and pin the corresponding version card under `nodes/.../versions/1.0/card.md`. Implementation details cite raw/source paths for the atomicstrata README and ClawHub listing. Reports cite report paths only for secondary gap and boundary framing, not as primary workflow authority.

## Synthesis decisions

- Source-backed observation: the gist explicitly names ingest, query, lint, index, and log.
- Source-backed observation: ingest updates summary pages, index, entity/concept pages, and log.
- Source-backed observation: query works against wiki pages and valuable answers can be filed back.
- Source-backed observation: lint checks contradictions, stale claims, orphan pages, missing concepts, missing cross-references, and gaps.
- Current project fact: adopted origin/canon, working definition, and architecture nodes already bound the gist as canon and define raw/wiki/schema boundaries.
- Interpretation: compile/wiki update is the workflow action that operationalizes the transition from raw sources to compiled wiki artifacts.
- Synthesis: index/log maintenance is part of the loop because index and log are updated through ingest, query, and lint activity.
- Implementation variant: hash checks, review queues, source markers, line-range citations, representation readiness, deterministic writes, CLI, MCP, viewer, and gap promotion are implementation supports, not abstract requirements.
- Evidence gap: no claim is made about empirical effectiveness, scale, enterprise suitability, adoption, governance completeness, or broad comparison.

## Audit trail

The version bundle was generated by `worker_executor` from `.llmwiki/runs/run_20260524_085000_worker_node_planning_workflow/next_task_packet.md`. The generation entry gate result was `pass`. The allowed output paths were limited to the version bundle and generation run delivery files. Root node metadata, `kb/`, and `generated/` were intentionally not written.

## Adoption rationale

Adoption is pending audit. This version is acceptable as a candidate because the primary gist directly supports the abstract workflow phases, the implementation sources are clearly labeled as variants, and the card preserves the packet's overclaim boundaries. It should not be adopted until citation and adoption audit confirms source scope, citation parseability, provenance completeness, overclaim control, and root metadata gating.

## Limits and uncertainty

This candidate does not prove that LLM Wiki works better than RAG, scales reliably, is enterprise-ready, has broad adoption, or has a mature implementation ecosystem. It does not evaluate ingestion quality, compile reliability, citation accuracy, long-term drift, privacy/security, governance, or benchmark performance. Multimodal details are limited to directly present representation-readiness and runtime-surface observations from ClawHub.

## Revision triggers

- Audit finds citation parsing errors, path drift, missing required citation fields, or unsupported claims.
- Audit finds overclaim into implementation ecosystem survey, enterprise, empirical, adoption, scale/reliability, governance, or broad comparison territory.
- New authorized source mining provides neutral workflow taxonomy, independent implementation evidence, empirical evaluation, citation audits, or governance evidence.
- Any prior adopted anchor receives a major update that changes canon, working definition, or architecture boundaries.
- Future implementation nodes require clearer separation between abstract workflow phases and implementation-specific tools.
