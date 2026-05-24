# 任务包模板：知识卡采纳

- `task_id`: `task_20260525_0036_card_adoption_candidate_4`
- `iteration_id`: `iteration_20260525_0035_card_adoption_persistent_composite_wiki`
- `role`: `card_adoption_worker`
- `main_language`: 中文

## 目标

把审计通过的草稿知识卡采纳到 `llm_wiki/kb/`。采纳只做文件移动、轻量整理和最小索引更新，不做重写和扩写。

## 采纳对象

- `candidate_id`: `候选 4`
- `card_id`: `llm-wiki-persistent-compounding-artifact`
- `card_title`: `持久复合 wiki`
- `audit_result_required`: `pass`
- `target_card_path`: `llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md`
- `target_provenance_path`: `llm_wiki/kb/provenance/llm-wiki-persistent-compounding-artifact.md`
- `target_index_path`: `llm_wiki/kb/indexes/cards.md`

## 允许输入

- 当前任务包。
- `draft_card_path`: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/artifacts/draft_card.md`
- `provenance_path`: `llm_wiki/loop/iterations/iteration_20260525_0033_card_drafting_persistent_composite_wiki/artifacts/provenance.md`
- `audit_report_path`: `llm_wiki/loop/iterations/iteration_20260525_0034_card_audit_persistent_composite_wiki/artifacts/audit_report.md`
- `target_card_path`: `llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md`，仅用于存在性和覆盖冲突检查。
- `target_provenance_path`: `llm_wiki/kb/provenance/llm-wiki-persistent-compounding-artifact.md`，仅用于存在性和覆盖冲突检查。
- `target_index_path`: `llm_wiki/kb/indexes/cards.md`，仅用于保留既有最小索引内容并做增量更新。

## 禁止输入

- 父聊天上下文。
- 没有通过审计的知识卡。
- 未列出的来源。
- 旧版 `legacy/` 知识库。

## 允许写入

- `llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md`
- `llm_wiki/kb/provenance/llm-wiki-persistent-compounding-artifact.md`
- `llm_wiki/kb/indexes/cards.md`
- `llm_wiki/loop/iterations/iteration_20260525_0035_card_adoption_persistent_composite_wiki/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0035_card_adoption_persistent_composite_wiki/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0035_card_adoption_persistent_composite_wiki/read_log.md`

## 采纳规则

- 只有 `audit_result: pass` 的知识卡可以采纳。
- 采纳后知识卡的 `status` 改为 `accepted`。
- 不新增复杂元数据。
- 不把采纳动作写成枢纽页。
- 出处论证和知识卡分文件保存，但彼此链接。
- 如果知识卡含 `Footnotes`，它必须仍然是最后一个 section。
- 读取目标 KB 路径只允许用于存在性检查、覆盖冲突检查和最小索引增量更新，不得用目标 KB 里的其它内容补充事实。

## 成功门禁

- 知识卡落在 `llm_wiki/kb/cards/`。
- 出处论证落在 `llm_wiki/kb/provenance/`。
- 最小索引包含卡片标题、路径、状态和来源。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 审计结论不是 `pass`。
- 草稿卡或出处论证缺失。
- 采纳会覆盖已有不同内容。
