# Change: genesis -> 1.0

node_id:: 20260524_132000_llm_wiki_evaluation_evidence
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: 2026-05-24T13:40:00+08:00
run_id:: run_20260524_134000_worker_generation_evaluation_evidence
adoption_status:: pending_audit

## Why this node was created

This node was created from `cand_007_evaluation_evidence` to capture how LLM Wiki evaluation and evidence should be expressed: evaluation dimensions, evidence grades, citation auditability, direct versus adjacent evidence, implementation self-description boundaries, source gaps, and deferred retrieval.

## Why this first version is acceptable

The first version is acceptable as a candidate because it stays inside the planned evidence scope, uses WiCER as bounded direct evidence, uses Knowledge Compounding only for cautious economic/token-cost framing, treats implementation README controls as self-description, labels adjacent evaluation frameworks as adjacent, and preserves evidence gaps.

Adoption remains pending. No root `node.yaml`, `kb/` view, or `generated/` index was written.

## Evidence basis

Direct LLM Wiki evaluation evidence:

- `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-wicer/text.txt`

Cautious economic/token-cost framing:

- `data/raw/arxiv/arxiv-knowledge-compounding/text.txt`

Implementation-described auditability:

- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`

Adjacent evaluation vocabulary:

- `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`

Process and gap boundaries:

- `reports/coverage_framework.md`
- `reports/source_gap_review.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/retrieval_requests.md`
- `.llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.yaml`

Prior KB anchors are used only for continuity and boundaries.

## Known limits

- WiCER is one recent direct evaluation source with model, hardware, RAG baseline, validation, judge, and scope limits.
- Knowledge Compounding was mined at abstract/PDF metadata level and is not used for detailed ROI claims.
- Atomicstrata and Kytmanov READMEs are implementation self-descriptions, not independent evidence that controls work.
- ALCE, Ragas, ARES, and RAGChecker are adjacent RAG/citation evaluation sources, not direct LLM Wiki benchmark evidence.
- No direct local citation audit of adopted KB pages is available.
- Independent replication, broad provider/model/corpus comparison, long-term drift/stale-claim rates, human expert evaluation, user studies, and negative cases remain deferred.

## Expected future changes

Future versions should change if audit finds unsupported claims, if WiCER or Knowledge Compounding reproducibility artifacts are mined, if local citation audits produce direct KB-level evidence, if long-term drift data becomes available, or if independent studies alter the evidence grade. Because this is a genesis candidate with no adopted downstream dependents, no propagation is required before audit.

