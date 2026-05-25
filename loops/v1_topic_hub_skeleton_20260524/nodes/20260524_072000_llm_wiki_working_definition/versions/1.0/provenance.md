# Provenance

node_id:: 20260524_072000_llm_wiki_working_definition
version:: 1.0

## Why this version exists

This version exists because `cand_002_working_definition` was marked `ready_to_build` with `evidence_state: enough_for_first_version`. The goal is to create a first candidate bundle that defines LLM Wiki operationally while preserving the boundaries set by the adopted origin/canon node and the generation entry gate.

## Inputs used

Read inputs and used inputs are the same except where noted below. No network retrieval was performed.

### Existing data

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`: used as the primary definitional source.
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`: allowed and checked as equivalent raw source material, but the card cites the readable `text.txt` path for parseability.
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`: used only for bounded early discourse context.
- `data/raw/hacker_news/hacker-news-original-thread/item.json`: allowed as structured HN metadata, but not needed in the card because the definition does not rely on story metadata.
- `data/raw/webpage/karpathy-x-launch-post/text.txt`: used only for bounded launch context and source inventory.
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`: allowed and checked as a raw form of the launch capture, but the card cites `text.txt`.
- `data/raw/webpage/karpathy-x-launch-post/raw.json`: allowed as raw launch capture data, but not needed for substantive claims.
- `reports/source_gap_review.md`: used as secondary gap framing, not as original topic evidence.
- `reports/coverage_framework.md`: used as secondary boundary framing, not as Karpathy's exact original definition.

### Dynamic retrieval, if any

None. The task packet and evidence scope explicitly forbid network retrieval and state that no retrieval is required before building this first version.

### Prior KB nodes

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`: used as the adopted prior KB anchor.
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`: used as the pinned version path for the adopted anchor citation.
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/provenance.md`: read as allowed prior provenance context but not cited in the card because the adopted card was enough for the boundary dependency.

### Process artifacts

- `.llmwiki/control/orchestration_gates.yaml`: used for gate requirements and executor attribution.
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`: used for card shape and content rules.
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`: used for citation field formatting.
- `.llmwiki/skills/llmwiki-provenance-generation/SKILL.md`: used for this provenance shape.
- `.llmwiki/skills/llmwiki-change-generation/SKILL.md`: used for `change.md`.
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`: used for candidate version metadata.
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/next_task_packet.md`: used as the controlling task packet.
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/generation_entry_gate.md`: used to verify gate 004 pass.
- `.llmwiki/runs/run_20260524_073000_worker_node_planning_working_definition/evidence_scope.yaml`: used as the detailed evidence boundary.
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/source_mining.md`: used for source-backed observations and candidate synthesis.
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/candidate_frontier_delta.yaml`: used for candidate status, statement, constraints, and missing evidence.
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/evidence_gaps.md`: used for non-blocking gaps to preserve.
- `.llmwiki/runs/run_20260524_072000_worker_source_mining_working_definition/retrieval_requests.md`: used to confirm no retrieval is needed before building.

No out-of-scope inputs were used for substantive claims.

## Production rationale

The card is written as a Chinese working-definition node rather than a product, ecosystem, risk, or comparison node. Its central claims are tied to the gist: three layers, persistent wiki artifact, schema/instruction governance, ingest/query/lint operations, writeback, index/log support, optional tooling, and human/LLM division of labor.

The node metadata keeps the version at `candidate_pending_audit` and `adopted: false`. It includes a future `kb_view` path for renderer compatibility, but no KB view was written.

## Citation rationale

The primary definitional citation points to `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` because the gist is the source of truth for the working definition. The prior KB dependency cites the adopted `kb/20260524_062000_llm_wiki_origin_and_canon.md` path and pins to `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`, matching the task requirement for origin/canon citations.

HN and X are cited only as bounded discourse and launch context. The coverage framework and source-gap report are cited only as secondary framing and gap preservation, not as original source truth.

## Synthesis decisions

- Source-backed observation: the gist describes raw sources, wiki, schema, ingest, query, lint, index, log, optional tooling, and human/LLM roles.
- Working definition: those observations are synthesized into a concise operational definition.
- Interpretation: the difference from one-shot retrieval is framed as persistence and maintenance of a reusable artifact, not as a rigorous RAG comparison.
- Evidence gap: empirical effectiveness, enterprise readiness, adoption, implementation ecosystem maturity, broad comparison, historical lineage, and governance/security remain outside this node.

## Audit trail

- Gate 003 and gate 004 had already passed in the planning run.
- This worker created only the allowed version bundle and generation run delivery files.
- The candidate was not adopted.
- Root `nodes/20260524_072000_llm_wiki_working_definition/node.yaml` was not written.
- No `kb/` or `generated/` paths were written.

## Adoption rationale

Adoption is pending audit. The version is acceptable as a candidate because the primary definitional claims are directly supported by the gist, the prior KB anchor is adopted, no retrieval is required before this first version, and the card explicitly preserves the required evidence boundaries. Adoption should occur only after the later citation and adoption audit gates pass.

## Limits and uncertainty

This version does not establish enterprise readiness, empirical proof, measured superiority, broad adoption, full implementation ecosystem completeness, complete historical lineage, or rigorous comparison with RAG, graph RAG, PKM, knowledge graphs, documentation systems, or agent memory.

HN comments are not treated as authoritative technical proof. X social metrics are not used. Coverage reports are secondary framing only. The definition is a first-version working definition and may need revision when comparison, evaluation, risk/governance, or ecosystem nodes are separately mined.

## Revision triggers

- New primary source evidence changes the canonical definition or clarifies required components.
- A later audit finds citation parsing failures, path mistakes, overclaiming, or unsupported synthesis.
- Separate comparison mining establishes more precise boundaries against RAG, graph RAG, PKM, knowledge graphs, documentation systems, or agent memory.
- Empirical or ecosystem evidence warrants a separate node and requires this definition to narrow or revise its claims.
- The adopted origin/canon node receives a major version update that affects this node's dependency.
