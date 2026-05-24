# 循环任务队列

当前队列只放主控 agent 可以派发的窄任务，不放大目标。

### `task_20260525_0002_cli_worker_smoke`

- `role`: `independent_evaluator`
- `action`: 只读审计 Codex CLI / Claude CLI 的最小 worker runtime 可行性。允许输入应包含 `TECH_VALIDATION.md`、`cli_capability_probe.md` 和 `cli_worker_smoke.md`。
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0002_cli_worker_smoke/artifacts/cli_worker_audit.md`
- `note`: 不启动长任务，不写全局配置，不安装依赖。

## 进行中（in_progress）

### `task_20260525_0026_card_audit_candidate_2`

- `role`: `card_audit_worker`
- `action`: 审计候选 2 草稿卡、provenance 与 `raw.txt:7-10` 的对应关系，判断是否可进入采纳流程。
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0025_card_audit_rag_no_accumulation`
- `draft_card_path`: `llm_wiki/loop/iterations/iteration_20260525_0024_card_drafting_rag_no_accumulation/artifacts/draft_card.md`
- `provenance_path`: `llm_wiki/loop/iterations/iteration_20260525_0024_card_drafting_rag_no_accumulation/artifacts/provenance.md`
- `source_evidence_path`: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:7-10`
- `note`: 任务包已创建并通过 `validate_scope.py`；dispatch 使用 `fork_context:false`，worker 完成后关闭。

## 已阻塞（blocked）

暂无。

## 已完成（done）

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
