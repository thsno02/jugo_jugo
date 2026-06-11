# read_log

## 允许输入之外读取

- path: `~/.codex/skills/agent-loop-runner/SKILL.md`
  reason: 开发者指令要求循环类任务使用对应技能。
  usage: 仅读取技能执行边界与交付要求，不作为知识卡事实来源。

## 允许输入读取

- path: `llm_wiki/loop/iterations/iteration_20260525_0017_card_adoption_schema_layer/task.md`
  usage: 确认任务包、允许读写范围、采纳对象和成功门禁。
- path: `llm_wiki/loop/iterations/iteration_20260525_0015_card_drafting_schema_layer/artifacts/draft_card.md`
  usage: 采纳指定草稿知识卡，并将 `status` 从 `draft` 改为 `accepted`。
- path: `llm_wiki/loop/iterations/iteration_20260525_0015_card_drafting_schema_layer/artifacts/provenance.md`
  usage: 采纳对应出处论证，并做卡片互链与采纳状态轻量整理。
- path: `llm_wiki/loop/iterations/iteration_20260525_0016_card_audit_schema_layer/artifacts/audit_report.md`
  usage: 核验 `audit_result: pass`。
- path: `llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md`
  usage: 存在性和覆盖冲突检查；结果为目标文件不存在。
- path: `llm_wiki/kb/provenance/llm-wiki-schema-configuration-document.md`
  usage: 存在性和覆盖冲突检查；结果为目标文件不存在。
- path: `llm_wiki/kb/indexes/cards.md`
  usage: 保留既有最小索引内容，并追加本卡索引行。

## 写入后验收读取

- path: `llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md`
  usage: 验收采纳后 `status: accepted`、互链和 `Footnotes` 位置。
- path: `llm_wiki/kb/provenance/llm-wiki-schema-configuration-document.md`
  usage: 验收出处论证已落盘并链接对应知识卡。
- path: `llm_wiki/kb/indexes/cards.md`
  usage: 验收最小索引新增行包含标题、路径、状态和来源。
- path: `llm_wiki/loop/iterations/iteration_20260525_0017_card_adoption_schema_layer/loop_status.md`
  usage: 验收状态文件存在且结果为 `LOOP_DONE`。
- path: `llm_wiki/loop/iterations/iteration_20260525_0017_card_adoption_schema_layer/loop_delivery.md`
  usage: 验收交付文件存在且包含 `LOOP_DONE`。
- path: `llm_wiki/loop/iterations/iteration_20260525_0017_card_adoption_schema_layer/read_log.md`
  usage: 验收读日志存在并记录本次读取范围。
