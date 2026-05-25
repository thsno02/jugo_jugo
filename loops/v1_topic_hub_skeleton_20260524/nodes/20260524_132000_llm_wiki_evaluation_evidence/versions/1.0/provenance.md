# Provenance

node_id:: 20260524_132000_llm_wiki_evaluation_evidence
version:: 1.0

## Why this version exists

This first version exists because `cand_007_evaluation_evidence` reached `ready_to_build` with `retrieval_required_before_generation: false`. The bundle creates a candidate node about LLM Wiki evaluation/evidence: evaluation dimensions, evidence levels, citation auditability, unsupported-claim boundaries, source gaps, deferred retrieval, and KB trust expression.

This version is a candidate only. It does not adopt root metadata, write a `kb/` view, update generated indexes, or perform citation/adoption audit.

## Inputs used

### Existing data

Read and used as direct LLM Wiki evaluation evidence:

- `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-wicer/text.txt`

Read and used only as cautious economic/token-cost framing:

- `data/raw/arxiv/arxiv-knowledge-compounding/text.txt`

Read and used only as implementation-described auditability evidence:

- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`

Read and used only as adjacent evaluation vocabulary:

- `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`

Read and used as process/gap sources:

- `reports/coverage_framework.md`
- `reports/source_gap_review.md`

Read but not used as substantive authority:

- Existing adopted node examples and validator scripts, for local schema, citation formatting, and validation conventions only.

### Dynamic retrieval, if any

None. No network retrieval was used.

### Prior KB nodes

Read and used only as continuity and boundary anchors:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
- `kb/20260524_122000_llm_wiki_implementation_ecosystem.md`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md`

### Process artifacts

Read and used:

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-loop-orchestration/SKILL.md`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`
- `.llmwiki/skills/llmwiki-provenance-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-change-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/next_task_packet.md`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/node_plan.yaml`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.md`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.yaml`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/generation_entry_gate.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_inventory.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/source_notes.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/retrieval_requests.md`

## Production rationale

The card is framed as an evidence map and boundary ledger. It uses WiCER as the strongest direct evaluation evidence, Knowledge Compounding only as cautious economic/token-cost framing, Atomicstrata/Kytmanov only as implementation self-description, ALCE/Ragas/ARES/RAGChecker only as adjacent vocabulary, and process reports for evidence grades/gaps.

## Citation rationale

Every substantive claim is tied to raw source, process source, or prior KB anchor citations. Footnotes cite claim-level support. References cite dependency-level sources. Prior KB nodes are cited only as continuity anchors and never as primary evidence for new evaluation claims.

## Synthesis decisions

- Direct evidence: WiCER supports a bounded LLM Wiki evaluation frame around compilation gap, diagnostic probes, refinement iteration, baselines, scale limits, judge validation, and reproducibility constraints.
- Economic framing: Knowledge Compounding supports only the need for explicit query sequence, baseline, method, token logs, reproducibility, and projection boundaries before economic claims.
- Implementation-described auditability: Atomicstrata and Kytmanov support that some implementations describe source ranges, lint, hashes, review queues, compare previews, rejection feedback, and confidence warnings.
- Adjacent eval vocabulary: ALCE, Ragas, ARES, and RAGChecker provide terminology for citation support, faithfulness, relevance, claim-level diagnostics, evaluator calibration, confidence intervals, and noise sensitivity.
- Process gap: `coverage_framework.md`, `source_gap_review.md`, and source-mining artifacts support evidence grades, claim records, missing evidence, and deferred retrieval.
- Prior-KB separation: adopted nodes are continuity anchors only; they are not used to prove evaluation effectiveness.

## Audit trail

The version bundle was generated by `worker_executor` from `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/next_task_packet.md`. The generation entry decision was `pass`. The allowed output paths were limited to the candidate version bundle and generation run artifacts. Root node metadata, `kb/`, `generated/`, source evidence, skills, protocol files, archives, and other node bodies were intentionally not written.

## Adoption rationale

Adoption is pending audit. This version is acceptable as a candidate because it separates evidence tiers, avoids broad superiority or production claims, preserves deferred retrieval, labels adjacent evaluation sources as adjacent, and keeps the root metadata adoption gate closed. It should not be adopted until citation and adoption audit confirms source support, parseability, overclaim control, provenance completeness, tier separation, and footnote layout.

## Limits and uncertainty

This candidate does not claim that LLM Wiki generally beats RAG, GraphRAG, PKM, agent memory, or documentation systems. It does not claim production reliability, enterprise readiness, adoption scale, benchmark leadership, general ROI, solved hallucination, solved citation faithfulness, or long-term maintenance quality. It does not treat README controls as measured effectiveness, adjacent RAG/citation papers as direct LLM Wiki benchmarks, or prior KB anchors as new primary evidence.

Open gaps include independent replication, WiCER code/log mining, Knowledge Compounding full extraction and reproducibility artifacts, direct audits of adopted KB pages, long-term drift/stale-claim rates, broad provider/model/corpus comparisons, human/expert studies, and negative/failure cases.

## Revision triggers

- Audit finds citation parsing errors, unresolved paths, unsupported claims, or source-tier confusion.
- Audit finds WiCER generalized beyond its direct source limits.
- Audit finds Knowledge Compounding used as broad ROI or enterprise proof.
- Audit finds Atomicstrata/Kytmanov controls described as measured reliability.
- Audit finds ALCE/Ragas/ARES/RAGChecker treated as direct LLM Wiki evidence.
- Audit finds prior KB anchors used as new evaluation evidence.
- New source mining adds direct local citation audits, independent replications, provider/corpus comparisons, drift measurements, human studies, negative cases, or stronger reproducibility artifacts.

