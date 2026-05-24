# Read Log

| path | reason | use |
| --- | --- | --- |
| `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md` | 开发侧技能触发要求读取；不作为事实审计来源 | 仅确认循环执行文件落盘与 worker 隔离原则 |
| `llm_wiki/loop/iterations/iteration_20260525_0019_card_audit_wiki_layer/task.md` | 当前任务包 | 确认审计对象、允许输入、允许写入、审计问题和结论格式 |
| `llm_wiki/loop/iterations/iteration_20260525_0018_card_drafting_wiki_layer/artifacts/draft_card.md` | 任务包允许的草稿知识卡 | 审计 statement、fact_type、support、scope、status、正文结构与引用顺序 |
| `llm_wiki/loop/iterations/iteration_20260525_0018_card_drafting_wiki_layer/artifacts/provenance.md` | 任务包允许的出处论证 | 检查出处论证是否足以 justify 草稿卡暂时成立 |
| `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:31-32` | 任务包指定的来源证据行 | 核对草稿卡与来源证据是否对应 |
