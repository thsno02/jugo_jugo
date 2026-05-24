# Task

run_id:: run_20260524_111000_worker_audit_risks_governance_provenance
executor_role:: worker_executor
worker_role:: cand_008_risks_governance_provenance citation/adoption audit worker
task_packet:: user_dispatch_2026-05-24_cand_008_audit
status:: LOOP_DONE

## Scope

Audit the candidate version bundle for:

- `cand_008_risks_governance_provenance`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/`

The audit checks card validation, citation target and pinned-path resolution, citation faithfulness, source-category boundaries, provenance completeness, change/adoption state, and root metadata gate status.

## Required Inputs Read

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-citation-audit/SKILL.md`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/runs/run_20260524_104000_worker_source_mining_risks_governance_provenance/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/node_plan.yaml`
- `.llmwiki/runs/run_20260524_105000_worker_node_planning_risks_governance_provenance/evidence_scope.md`
- `.llmwiki/runs/run_20260524_110000_worker_generation_risks_governance_provenance/loop_delivery.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/node.yaml`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/provenance.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/change.md`

Additional raw/source files were read only to verify citation faithfulness against the evidence matrix and planner scope.

## Write Boundary

Allowed output directory:

- `.llmwiki/runs/run_20260524_111000_worker_audit_risks_governance_provenance/`

Files written:

- `task.md`
- `citation_audit.md`
- `audit_report.md`
- `validation_trace.md`
- `loop_status.md`
- `loop_delivery.md`

No candidate bundle, root node, `kb/`, `frontier`, or skill files were intentionally modified.
