# Next Worker Task Packet

task_name:: cand_008_risks_governance_provenance_source_mining
target_candidate:: cand_008_risks_governance_provenance
related_seed:: cand_011_initial_risk_discourse
recommended_run_dir:: .llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/
worker_role:: source-mining + frontier-update worker
decision_required:: ready_to_plan | needs_more_mining | needs_retrieval | blocked

## Role Boundary

You are a worker executor, not the controller. The main agent/controller does not execute concrete source mining or frontier updates. Do not spawn sub-agents. Do not revert unrelated changes.

## Topic Boundary

Mine a bounded first-version candidate for LLM Wiki risks, governance, and provenance. Focus on provenance drift, stale/overgeneralized claims, citation faithfulness, maintenance drift, privacy/security exposure, source/prompt poisoning, governance and audit controls, and human review boundaries.

Use `cand_011_initial_risk_discourse` only as an early-discourse seed from HN. Do not build a standalone HN discourse node unless the frontier evidence requires it.

## Allowed Inputs

Required control and skill files:

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/control/skill_registry.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/skills/llmwiki-source-mining/SKILL.md`
- `.llmwiki/skills/llmwiki-frontier-management/SKILL.md`
- `.llmwiki/skills/llmwiki-dynamic-retrieval/SKILL.md`
- `.llmwiki/runs/run_20260524_103000_worker_skill_eval_vs_rag_write_loop/next_task_packet.md`

Primary local sources:

- `data/raw/arxiv/arxiv-memory-as-metabolism/text.txt`
- `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt`
- `data/raw/webpage/owasp-llm-top10-2025/text.txt`
- `data/raw/webpage/owasp-agentic-top10-2026/text.txt`
- `data/raw/webpage/nist-gai-profile/text.txt`
- `data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt`
- `data/raw/arxiv/arxiv-alce/text.txt`
- `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
- `data/raw/arxiv/arxiv-wicer/text.txt`
- `data/raw/arxiv/arxiv-etamp-memory-poisoning/text.txt`
- `data/raw/arxiv/arxiv-graph-poisoning/text.txt`
- `data/raw/arxiv/arxiv-poisonedrag/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`

Planning and manifest support:

- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`
- adopted KB anchors for origin, definition, architecture, workflow, and vs-RAG as boundary continuity only.

## Forbidden Inputs / Claims

- Do not use blocked Reddit pages as substantive evidence beyond block/gap metadata.
- Do not use intercepted AICritique enterprise pages as evidence.
- Do not claim enterprise readiness, compliance sufficiency, real-world incident rates, or measured risk reduction without direct evidence.
- Do not present generic AI safety/security risks as LLM Wiki-specific unless the link to source-preserving wiki maintenance is explicit.
- Do not use prior KB nodes as primary evidence for external governance, security, poisoning, or citation-accuracy facts.

## Retrieval Limits

Default to local corpus only. Dynamic retrieval is allowed only if a directly needed source is missing for a clearly named blocker. Limit retrieval to at most 3 targeted attempts. If company/network access blocks or returns low-quality pages, write `retrieval_requests.md` and mark the gap deferred; do not keep trying.

## Allowed Writes

- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`

Do not write `nodes/`, `kb/`, `generated/`, source data, or archive/protocol originals.

## Required Artifacts

Write these run artifacts:

- `task.md`
- `source_scope.md`
- `source_mining.md`
- `source_inventory.md`
- `source_notes.md`
- `evidence_matrix.yaml`
- `candidate_frontier_delta.yaml`
- `evidence_gaps.md`
- `retrieval_requests.md`
- `mining_trace.md`
- `frontier_trace.md`
- `next_task_packet.md`
- `loop_status.md`
- `loop_delivery.md`

## Decision Schema

Use this exact decision block in `loop_delivery.md`:

```text
status:: LOOP_DONE | LOOP_BLOCKED
decision:: ready_to_plan | needs_more_mining | needs_retrieval | blocked
target_candidate:: cand_008_risks_governance_provenance
evidence_state:: enough_for_first_version | partial | insufficient
retrieval_required_before_build:: true | false
next_action:: node_planning_for_cand_008_risks_governance_provenance | continue_mining | write_retrieval_request | controller_review_blocker
```

## Success Criteria

- Produces a narrow first-version candidate if evidence is enough.
- Separates LLM Wiki-specific risks from adjacent LLM/RAG/agent-memory risks.
- Preserves anti-strawman comparison rules from the updated card/audit skills.
- Queues any retrieval-deferred enterprise, Reddit, incident, compliance, or empirical-risk gaps without blocking bounded v1 coverage.

