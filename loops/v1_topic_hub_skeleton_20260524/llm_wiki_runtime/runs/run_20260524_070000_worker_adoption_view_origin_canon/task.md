# Task

executor_role:: adoption_view_worker
status:: in_progress
task_packet:: user_directed_adoption_view_origin_canon
target_node_id:: 20260524_062000_llm_wiki_origin_and_canon
target_version:: 1.0

## Allowed inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`
- `.llmwiki/runs/run_20260524_065500_worker_reaudit_origin_canon/loop_delivery.md`
- `.llmwiki/runs/run_20260524_065500_worker_reaudit_origin_canon/audit_report.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/node.yaml`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/provenance.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/change.md`
- Repository validation/build scripts.

## Allowed outputs

- Root adopted node metadata for `20260524_062000_llm_wiki_origin_and_canon`.
- Adopted KB view and generated graph/status artifacts produced by official scripts.
- This run's adoption, view-build, validation, status, and delivery records.

## Constraints

- Adopt only `20260524_062000_llm_wiki_origin_and_canon` version `1.0`.
- Do not generate new KB content.
- Do not alter card content unless required for path consistency.
- If validation/build fails, record `LOOP_BLOCKED` with exact failure.
