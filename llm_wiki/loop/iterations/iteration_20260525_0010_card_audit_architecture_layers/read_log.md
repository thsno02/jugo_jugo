# read_log

| path | reason | use |
|---|---|---|
| `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md` | 系统技能指令要求读取 loop 执行规范 | 只用于执行流程约束，不作为知识卡事实审计依据 |
| `llm_wiki/loop/iterations/iteration_20260525_0010_card_audit_architecture_layers/task.md` | 当前任务包 | 确认允许输入、允许写入、审计问题和交付格式 |
| `llm_wiki/loop/iterations/iteration_20260525_0009_card_drafting_architecture_layers/artifacts/draft_card.md` | 任务包指定草稿知识卡 | 审计 statement、fact_type、support、scope、status、正文和 section 顺序 |
| `llm_wiki/loop/iterations/iteration_20260525_0009_card_drafting_architecture_layers/artifacts/provenance.md` | 任务包指定出处论证 | 核对卡片论证是否能 justify 草稿暂时成立 |
| `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:25-33` | 任务包指定来源证据行 | 核对卡片 statement、support 和正文展开是否被来源支撑 |
