# Next Worker Task Packet

task_name:: cand_008_risks_governance_provenance_node_planning
target_candidate:: cand_008_risks_governance_provenance
recommended_run_dir:: .llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/
worker_role:: node-planning worker
decision_required:: generation_entry_pass | needs_more_mining | needs_retrieval | blocked

## Target Node

suggested_node_id:: 20260524_104000_llm_wiki_risks_governance_and_provenance
suggested_slug:: llm_wiki_risks_governance_and_provenance
suggested_version:: 1.0

## Required Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/skills/llmwiki-node-planning/SKILL.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_scope.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/source_mining.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/candidate_frontier_delta.yaml`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/evidence_gaps.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/retrieval_requests.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/frontier_trace.md`

## Evidence Scope

Primary LLM Wiki-specific evidence:

- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`
- `data/raw/arxiv/arxiv-wicer/text.txt`
- `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt`

Governance/drift source:

- `data/raw/arxiv/arxiv-memory-as-metabolism/text.txt`
- `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt`

Adjacent evidence:

- `data/raw/arxiv/arxiv-alce/text.txt`
- `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt`
- `data/raw/arxiv/arxiv-poisonedrag/text.txt`
- `data/raw/arxiv/arxiv-graph-poisoning/text.txt`

Process/framework/discourse sources:

- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/webpage/owasp-llm-top10-2025/text.txt`
- `data/raw/webpage/owasp-agentic-top10-2026/text.txt`
- `data/raw/webpage/nist-gai-profile/text.txt`
- `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`

## Planning Goals

Plan a first-version node that answers:

- What are the LLM Wiki-specific provenance and maintenance risks?
- Which controls are directly evidenced by implementations?
- Which risks come only from adjacent RAG/GraphRAG/agent-memory security papers?
- What governance boundaries are necessary before trusting agent-written wiki state?
- What claims are explicitly out of scope until later retrieval/mining?

## Non-Goals

- Do not write the card or node bundle.
- Do not claim enterprise readiness, compliance sufficiency, legal advice, incident rates, or measured risk reduction.
- Do not transfer PoisonedRAG/eTAMP/GraphRAG poisoning attack rates to LLM Wiki.
- Do not use prior KB nodes as primary evidence for security or governance facts.
- Do not use blocked Reddit or intercepted AICritique pages.

## Citation Constraints

- Use implementation READMEs and WiCER for direct LLM Wiki claims.
- Use ALCE only for adjacent citation-quality/evaluation claims.
- Use eTAMP, PoisonedRAG, and GraphRAG poisoning only as adjacent threat models.
- Use OWASP/NIST/Microsoft as broad framework/control vocabulary unless detailed preserved text exists.
- Use HN only as early discourse.
- Every substantive risk/control claim in the planned generation packet must identify source type and source id.

## Generation Risks To Warn About

- Overclaiming governance controls as solved rather than proposed/implemented in specific repos.
- Treating citation presence as citation faithfulness.
- Treating source preservation as privacy/security safety.
- Collapsing adjacent RAG/agent-memory attacks into direct LLM Wiki incidents.
- Writing generic AI governance rather than LLM Wiki-specific source/compile/wiki maintenance boundaries.

## Expected Outputs

- `planner_report.md`
- `evidence_scope.yaml`
- `next_task_packet.md`
- `generation_entry_gate.md`
- `loop_delivery.md`

