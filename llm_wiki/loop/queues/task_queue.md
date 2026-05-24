# 循环任务队列

当前队列只放主控 agent 可以派发的窄任务，不放大目标。

## 待派发（queued）

### `task_20260525_0002_cli_worker_smoke`

- `role`: `independent_evaluator`
- `action`: 只读审计 Codex CLI / Claude CLI 的最小 worker runtime 可行性。允许输入应包含 `TECH_VALIDATION.md`、`cli_capability_probe.md` 和 `cli_worker_smoke.md`。
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0002_cli_worker_smoke/artifacts/cli_worker_audit.md`
- `note`: 不启动长任务，不写全局配置，不安装依赖。

## 进行中（in_progress）

### `task_20260525_0004_card_drafting_candidate_8`

- `role`: `card_drafting_worker`
- `action`: 将第一轮 source mining 的 `候选 8` 写成一张草稿原子事实知识卡，并写一份可读 provenance。
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth`
- `fact_candidate_path`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
- `source_evidence_path`: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:27-30`
- `outputs`: `artifacts/draft_card.md`, `artifacts/provenance.md`
- `note`: 只处理一个候选；不得写多张卡，不得采纳。

## 已阻塞（blocked）

暂无。

## 已完成（done）

### `task_20260525_0003_source_mining_bootstrap`

- `role`: `source_mining_worker`
- `result`: `LOOP_DONE`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
- `candidate_count`: 12
- `decision`: `llm_wiki/loop/decisions/20260525-0241-source-mining-accepted-candidate-8.md`

### `task_20260525_0001_prelaunch_validation`

- `role`: `independent_evaluator`
- `result`: `concern`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/artifacts/independent_audit.md`
- `resolution`: `llm_wiki/loop/decisions/20260525-0208-prelaunch-concern-resolution.md`
