# 循环任务队列

当前队列只放主控 agent 可以派发的窄任务，不放大目标。

### `task_20260525_0002_cli_worker_smoke`

- `role`: `independent_evaluator`
- `action`: 只读审计 Codex CLI / Claude CLI 的最小 worker runtime 可行性。允许输入应包含 `TECH_VALIDATION.md`、`cli_capability_probe.md` 和 `cli_worker_smoke.md`。
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0002_cli_worker_smoke/artifacts/cli_worker_audit.md`
- `note`: 不启动长任务，不写全局配置，不安装依赖。

## 进行中（in_progress）

暂无。

## 已阻塞（blocked）

暂无。

## 已完成（done）

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
