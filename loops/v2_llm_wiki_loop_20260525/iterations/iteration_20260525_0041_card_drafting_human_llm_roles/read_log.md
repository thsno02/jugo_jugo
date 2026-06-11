# read_log

## 额外流程说明读取

- path: `~/.codex/skills/agent-loop-runner/SKILL.md`
- reason: 开发者指令要求在 loop/agent loop 任务中使用对应 skill。
- usage: 只用于执行流程约束，不用于知识卡事实内容或来源支撑。

## 允许输入读取

- path: `llm_wiki/loop/iterations/iteration_20260525_0041_card_drafting_human_llm_roles/task.md`
- usage: 确认当前任务包、允许输入、允许写入、成功门禁与阻塞条件。

- path: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
- usage: 仅核对 `候选 5` 的 `statement`、`fact_type`、`support`、`scope`、`source_evidence` 与 `draft_status`。
- note: 首次 `rg` 命令带上下文输出时意外显示了下一候选的标题起始行；未使用该内容，随后改用 `sed -n '45,52p'` 只读取 `候选 5`。

- path: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- lines: `15-16,68-69`
- usage: 核对候选 5 的直接来源证据，并作为草稿卡与出处论证的唯一事实支撑。
