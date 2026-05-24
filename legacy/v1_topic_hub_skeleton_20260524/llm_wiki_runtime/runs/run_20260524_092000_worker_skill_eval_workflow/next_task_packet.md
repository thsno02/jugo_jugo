# Next Worker Task Packet

task_name:: cand_004_workflow_adoption_metadata_repair_and_revalidate
target_candidate:: cand_004_workflow
decision:: revise_skills_then_continue

## Objective

Repair the post-adoption metadata consistency gap for `20260524_084000_llm_wiki_ingest_compile_query_lint_workflow@1.0`, then revalidate the KB state. Do not redo generation, citation audit, adoption review, source mining, or view content creation beyond the minimum rebuilds needed to confirm consistency.

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_090000_worker_audit_workflow/audit_report.md`
- `.llmwiki/runs/run_20260524_091000_worker_adoption_view_workflow/adoption_trace.md`
- `.llmwiki/runs/run_20260524_091000_worker_adoption_view_workflow/validation_trace.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/node.yaml`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`
- Existing validators and build scripts under `scripts/`

## Allowed Writes

- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml`, only adoption metadata fields needed to match the adopted root and audit/adoption run.
- New run artifacts under a new `.llmwiki/runs/<repair_run_id>/` directory.
- Control status files needed to mark the repair complete and set the next worker action.
- Generated view/status files only if rerunning the existing view build scripts is necessary to verify consistency.

## Forbidden Writes

- Do not modify `card.md`, `provenance.md`, or `change.md`.
- Do not modify data source files, archive/protocol originals, unrelated nodes, or unrelated run artifacts.
- Do not perform network retrieval.
- Do not dispatch sub-agents.

## Required Validation

- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow`
- `/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all`
- `/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all`
- `/opt/homebrew/bin/python3 scripts/kb_status.py`

## Follow-On Recommendation

If validation passes, the next coverage worker should target `cand_005_comparison_space` by decomposing it into a bounded v1 comparison candidate rather than generating the broad hub directly. Preferred first slice: `cand_010_vs_rag_write_loop`, because the frontier already frames the durable write/maintenance loop as the comparison boundary that prevents "just RAG" overclaiming.
