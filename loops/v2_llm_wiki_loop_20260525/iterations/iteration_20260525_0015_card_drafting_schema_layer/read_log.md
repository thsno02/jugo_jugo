# read_log

| path | reason | usage |
| --- | --- | --- |
| `~/.codex/skills/agent-loop-runner/SKILL.md` | 开发者环境要求匹配循环任务时使用该 skill。 | 只核对循环任务交付和状态文件的执行约束，不作为事实来源。 |
| `llm_wiki/loop/iterations/iteration_20260525_0015_card_drafting_schema_layer/task.md` | 当前任务包。 | 确认任务边界、允许输入、允许写入和成功门禁。 |
| `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md` | 允许输入，核对候选 10 字段。 | 只读取候选 10 对应片段，不引入其它候选内容。 |
| `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt` | 允许输入，核对来源证据第 33 行。 | 只使用第 33 行支撑知识卡和出处论证。 |
