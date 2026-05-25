# 循环任务队列

当前队列只放主控 agent 可以派发的窄任务，不放大目标。

### `task_20260525_0002_cli_worker_smoke`

- `role`: `independent_evaluator`
- `action`: 只读审计 Codex CLI / Claude CLI 的最小 worker runtime 可行性。允许输入应包含 `TECH_VALIDATION.md`、`cli_capability_probe.md` 和 `cli_worker_smoke.md`。
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0002_cli_worker_smoke/artifacts/cli_worker_audit.md`
- `note`: 不启动长任务，不写全局配置，不安装依赖。

## 进行中（in_progress）

### `task_20260525_0059_card_audit_candidate_6`

- `role`: `card_audit_worker`
- `action`: 独立审计第二轮候选 6 草稿卡和 provenance。
- `expected_output`: `llm_wiki/loop/iterations/iteration_20260525_0058_card_audit_idea_file_abstract_vague/artifacts/audit_report.md`
- `note`: 审计输入限定为草稿卡、provenance、候选 6 字段和 `raw.json` 的 `$.tweet.text`；不使用父聊天上下文。

## 待办（pending）

暂无。

## 已阻塞（blocked）

暂无。

## 已完成（done）

### `task_20260525_0058_card_drafting_candidate_6`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0057_card_drafting_idea_file_abstract_vague`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0909-card-drafting-candidate-6-ready-for-audit.md`

### `task_20260525_0057_card_adoption_candidate_3`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0056_card_adoption_idea_file_agent_builds`
- `card_id`: `idea-file-share-the-idea`
- `adopted_card`: `llm_wiki/kb/cards/idea-file-share-the-idea.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/idea-file-share-the-idea.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0858-card-adoption-accepted-candidate-3.md`

### `task_20260525_0056_card_audit_candidate_3_r1`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0055_card_audit_idea_file_agent_builds_r1`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0055_card_audit_idea_file_agent_builds_r1/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0849-card-audit-pass-candidate-3-r1.md`

### `task_20260525_0055_card_drafting_candidate_3_revision`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0054_card_drafting_idea_file_agent_builds_r1`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0841-card-drafting-candidate-3-revision-ready-for-audit.md`

### `task_20260525_0054_card_audit_candidate_3`

- `role`: `card_audit_worker`
- `result`: `audit_result: revise`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0834-card-audit-revise-candidate-3.md`

### `task_20260525_0053_card_drafting_candidate_3`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0052_card_drafting_idea_file_agent_builds`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0826-card-drafting-candidate-3-ready-for-audit.md`

### `task_20260525_0052_source_mining_karpathy_x_launch`

- `role`: `source_mining_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch`
- `source_id`: `karpathy-x-launch-post`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md`
- `fact_candidates_count`: 12
- `decision`: `llm_wiki/loop/decisions/20260525-0821-source-mining-accepted-candidate-3.md`

### `task_20260525_0051_card_adoption_candidate_6`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0050_card_adoption_llm_wiki_use_cases`
- `card_id`: `llm-wiki-listed-use-cases`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-listed-use-cases.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-listed-use-cases.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0812-card-adoption-accepted-candidate-6.md`

### `task_20260525_0050_card_audit_candidate_6`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0049_card_audit_llm_wiki_use_cases`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0049_card_audit_llm_wiki_use_cases/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0803-card-audit-pass-candidate-6.md`

### `task_20260525_0049_drafting_boundary_validation_evidence_audit`

- `role`: `independent_evaluator`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0048_drafting_boundary_validation_evidence_audit`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0048_drafting_boundary_validation_evidence_audit/artifacts/independent_audit.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0757-accept-drafting-boundary-repair.md`

### `task_20260525_0048_drafting_boundary_validation_evidence_repair`

- `role`: `prompt_repair_validation_evidence`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0047_drafting_boundary_validation_evidence_repair/artifacts/validation_evidence_report.md`
- `changed_files`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/artifacts/prompt_repair_report.md`
- `validation`: `validate_scope.py` pass; `inspect_delivery.py` pass

### `task_20260525_0047_drafting_candidate_boundary_repair_audit`

- `role`: `independent_evaluator`
- `result`: `audit_result: concern`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit/artifacts/independent_audit.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0747-drafting-boundary-repair-audit-concern.md`
- `required_change`: 补写目标修复任务的实际 validation result evidence。

### `task_20260525_0046_drafting_candidate_boundary_repair`

- `role`: `prompt_template_repair`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair`
- `changed_files`: `llm_wiki/loop/system_prompts/card_drafting_worker.md`, `llm_wiki/loop/task_templates/card_drafting_task.md`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/artifacts/prompt_repair_report.md`
- `validation`: `validate_scope.py` pass; `inspect_delivery.py` pass

### `task_20260525_0045_card_drafting_candidate_6`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0733-card-drafting-candidate-6-requires-boundary-repair.md`
- `reflection`: `llm_wiki/loop/reflections/20260525-read-boundary-noise-reflection.md`

### `task_20260525_0044_card_adoption_candidate_5`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0043_card_adoption_human_llm_roles`
- `card_id`: `llm-wiki-human-llm-role-division`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-human-llm-role-division.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0725-card-adoption-accepted-candidate-5.md`

### `task_20260525_0043_card_audit_candidate_5`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0042_card_audit_human_llm_roles`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0042_card_audit_human_llm_roles/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0718-card-audit-pass-candidate-5.md`

### `task_20260525_0042_card_drafting_candidate_5`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0041_card_drafting_human_llm_roles`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0710-card-drafting-candidate-5-ready-for-audit.md`
- `reflection`: `llm_wiki/loop/reflections/20260525-read-boundary-noise-reflection.md`

### `task_20260525_0041_card_adoption_candidate_1`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0040_card_adoption_llm_wiki_pattern_file`
- `card_id`: `llm-wiki-pattern-file`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-pattern-file.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-pattern-file.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0702-card-adoption-accepted-candidate-1.md`

### `task_20260525_0040_validate_scope_path_check_repair_audit`

- `role`: `independent_evaluator`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0039_validate_scope_path_check_repair_audit`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0039_validate_scope_path_check_repair_audit/artifacts/independent_audit.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0654-accept-validate-scope-path-check-repair.md`

### `task_20260525_0039_validate_scope_path_check_repair`

- `role`: `tooling_repair`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0038_validate_scope_path_check_repair/artifacts/tooling_repair_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0654-accept-validate-scope-path-check-repair.md`

### `task_20260525_0038_card_audit_candidate_1`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0641-card-audit-pass-candidate-1-with-task-path-risk.md`
- `residual_risk`: 任务包中的 `fact_candidate_path` 不存在；已转入 validate_scope tooling repair。

### `task_20260525_0037_card_drafting_candidate_1`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0631-card-drafting-candidate-1-ready-for-audit.md`

### `task_20260525_0036_card_adoption_candidate_4`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0035_card_adoption_persistent_composite_wiki`
- `card_id`: `llm-wiki-persistent-compounding-artifact`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-persistent-compounding-artifact.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0624-card-adoption-accepted-candidate-4.md`

### `task_20260525_0035_card_audit_candidate_4`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0034_card_audit_persistent_composite_wiki`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0034_card_audit_persistent_composite_wiki/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0618-card-audit-pass-candidate-4.md`

### `task_20260525_0034_card_drafting_candidate_4`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0612-card-drafting-candidate-4-ready-for-audit.md`

### `task_20260525_0033_card_adoption_candidate_12`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0032_card_adoption_query_workflow`
- `card_id`: `llm-wiki-query-answer-writeback`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-query-answer-writeback.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0604-card-adoption-accepted-candidate-12.md`

### `task_20260525_0032_card_audit_candidate_12`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0031_card_audit_query_workflow`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0031_card_audit_query_workflow/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0557-card-audit-pass-candidate-12.md`

### `task_20260525_0031_card_drafting_candidate_12`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0030_card_drafting_query_workflow`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0551-card-drafting-candidate-12-ready-for-audit.md`

### `task_20260525_0030_card_adoption_candidate_11`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0029_card_adoption_ingest_workflow`
- `card_id`: `llm-wiki-ingest-example-flow`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-ingest-example-flow.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-ingest-example-flow.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0544-card-adoption-accepted-candidate-11.md`

### `task_20260525_0029_card_audit_candidate_11`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0028_card_audit_ingest_workflow`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0028_card_audit_ingest_workflow/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0537-card-audit-pass-candidate-11.md`

### `task_20260525_0028_card_drafting_candidate_11`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0530-card-drafting-candidate-11-ready-for-audit.md`

### `task_20260525_0027_card_adoption_candidate_2`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0026_card_adoption_rag_no_accumulation`
- `card_id`: `rag-document-qa-does-not-accumulate-synthesized-knowledge`
- `adopted_card`: `llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/rag-document-qa-does-not-accumulate-synthesized-knowledge.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0522-card-adoption-accepted-candidate-2.md`

### `task_20260525_0026_card_audit_candidate_2`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0025_card_audit_rag_no_accumulation`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0025_card_audit_rag_no_accumulation/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0513-card-audit-pass-candidate-2.md`

### `task_20260525_0025_card_drafting_candidate_2`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0024_card_drafting_rag_no_accumulation`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0506-card-drafting-candidate-2-ready-for-audit.md`

### `task_20260525_0024_card_adoption_candidate_3`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0023_card_adoption_persistent_wiki_mode`
- `card_id`: `llm-wiki-persistent-wiki-alternative-mode`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-persistent-wiki-alternative-mode.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0459-card-adoption-accepted-candidate-3.md`

### `task_20260525_0023_card_audit_candidate_3`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0022_card_audit_persistent_wiki_mode`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0022_card_audit_persistent_wiki_mode/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0452-card-audit-pass-candidate-3.md`

### `task_20260525_0022_card_drafting_candidate_3`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0021_card_drafting_persistent_wiki_mode`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0446-card-drafting-candidate-3-ready-for-audit.md`

### `task_20260525_0021_card_adoption_candidate_9`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0020_card_adoption_wiki_layer`
- `card_id`: `llm-wiki-wiki-layer-generated-markdown-directory`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-wiki-layer-generated-markdown-directory.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0438-card-adoption-accepted-candidate-9.md`

### `task_20260525_0020_card_audit_candidate_9`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0019_card_audit_wiki_layer`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0019_card_audit_wiki_layer/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0431-card-audit-pass-candidate-9.md`

### `task_20260525_0019_card_drafting_candidate_9`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0018_card_drafting_wiki_layer`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0424-card-drafting-candidate-9-ready-for-audit.md`

### `task_20260525_0018_card_adoption_candidate_10`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0017_card_adoption_schema_layer`
- `card_id`: `llm-wiki-schema-configuration-document`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-schema-configuration-document.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0417-card-adoption-accepted-candidate-10.md`

### `task_20260525_0017_card_audit_candidate_10`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0016_card_audit_schema_layer`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0016_card_audit_schema_layer/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0409-card-audit-pass-candidate-10.md`

### `task_20260525_0016_card_drafting_candidate_10`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0015_card_drafting_schema_layer`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0403-card-drafting-candidate-10-ready-for-audit.md`

### `task_20260525_0013_adoption_template_repair`

- `role`: `main_agent_control_plane_repair`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0012_adoption_template_repair/artifacts/template_repair_report.md`

### `task_20260525_0014_adoption_template_repair_audit`

- `role`: `independent_evaluator`
- `result`: `audit_result: concern`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0013_adoption_template_repair_audit`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0013_adoption_template_repair_audit/artifacts/independent_audit.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0348-adoption-template-audit-concern-resolution.md`

### `task_20260525_0015_adoption_template_repair_audit_r1`

- `role`: `independent_evaluator`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/artifacts/independent_audit.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0354-accept-adoption-template-repair.md`

### `task_20260525_0003_source_mining_bootstrap`

- `role`: `source_mining_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
- `candidate_count`: 12
- `decision`: `llm_wiki/loop/decisions/20260525-0241-source-mining-accepted-candidate-8.md`

### `task_20260525_0004_card_drafting_candidate_8`

- `role`: `card_drafting_worker`
- `result`: `delivery_inspection_fail`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth`
- `note`: 草稿卡和 provenance 已生成，但 `loop_delivery.md` 缺少 `LOOP_DONE` / `LOOP_BLOCKED` marker，不能进入审计；已触发最小 prompt 修复。

### `task_20260525_0005_delivery_marker_prompt_repair`

- `role`: `main_agent_control_plane_repair`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0004_delivery_marker_prompt_repair/artifacts/prompt_repair_report.md`

### `task_20260525_0006_prompt_repair_independent_audit`

- `role`: `independent_evaluator`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0005_prompt_repair_audit`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0005_prompt_repair_audit/artifacts/independent_audit.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0254-accept-delivery-marker-prompt-repair.md`

### `task_20260525_0007_card_drafting_candidate_8_r1`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0301-card-drafting-revision-ready-for-audit.md`

### `task_20260525_0008_card_audit_candidate_8_r1`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0308-card-audit-pass-candidate-8.md`

### `task_20260525_0009_card_adoption_candidate_8`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth`
- `card_id`: `raw-sources-readonly-source-of-truth`
- `adopted_card`: `llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/raw-sources-readonly-source-of-truth.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0316-card-adoption-accepted-candidate-8.md`

### `task_20260525_0010_card_drafting_candidate_7`

- `role`: `card_drafting_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0009_card_drafting_architecture_layers`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0324-card-drafting-candidate-7-ready-for-audit.md`

### `task_20260525_0011_card_audit_candidate_7`

- `role`: `card_audit_worker`
- `result`: `audit_result: pass`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0010_card_audit_architecture_layers`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0010_card_audit_architecture_layers/artifacts/audit_report.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0330-card-audit-pass-candidate-7.md`

### `task_20260525_0012_card_adoption_candidate_7`

- `role`: `card_adoption_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0011_card_adoption_architecture_layers`
- `card_id`: `llm-wiki-three-layer-architecture`
- `adopted_card`: `llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md`
- `adopted_provenance`: `llm_wiki/kb/provenance/llm-wiki-three-layer-architecture.md`
- `index`: `llm_wiki/kb/indexes/cards.md`
- `decision`: `llm_wiki/loop/decisions/20260525-0337-card-adoption-accepted-candidate-7.md`

### `task_20260525_0001_prelaunch_validation`

- `role`: `independent_evaluator`
- `result`: `concern`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/artifacts/independent_audit.md`
- `resolution`: `llm_wiki/loop/decisions/20260525-0208-prelaunch-concern-resolution.md`
