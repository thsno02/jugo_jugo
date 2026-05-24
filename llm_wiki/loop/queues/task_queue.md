# 循环任务队列

当前队列只放主控 agent 可以派发的窄任务，不放大目标。

## 待派发（queued）

### `task_20260525_0002_cli_worker_smoke`

- `role`: `independent_evaluator`
- `action`: 只读审计 Codex CLI / Claude CLI 的最小 worker runtime 可行性。允许输入应包含 `TECH_VALIDATION.md`、`cli_capability_probe.md` 和 `cli_worker_smoke.md`。
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0002_cli_worker_smoke/artifacts/cli_worker_audit.md`
- `note`: 不启动长任务，不写全局配置，不安装依赖。

## 进行中（in_progress）

### `task_20260525_0003_source_mining_bootstrap`

- `role`: `source_mining_worker`
- `action`: 从本地 `data/` 中选择一个已获取来源，生成第一批事实候选。
- `preferred_source_index`: `data/manifests/acquired_sources_index.md`
- `fallback_source_index`: `data/manifests/sources.jsonl`
- `iteration`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist`
- `source_path`: `data/raw/gist_raw/karpathy-gist-llm-wiki`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
- `note`: 只有前置门禁通过后，主控 agent 才能把具体 `source_id` 和 `source_path` 写入任务包并派发执行者。

## 已阻塞（blocked）

暂无。

## 已完成（done）

### `task_20260525_0001_prelaunch_validation`

- `role`: `independent_evaluator`
- `result`: `concern`
- `output`: `llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/artifacts/independent_audit.md`
- `resolution`: `llm_wiki/loop/decisions/20260525-0208-prelaunch-concern-resolution.md`
