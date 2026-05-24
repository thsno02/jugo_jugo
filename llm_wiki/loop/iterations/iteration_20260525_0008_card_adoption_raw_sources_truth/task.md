# 任务包模板：知识卡采纳

- `task_id`: `task_20260525_0009_card_adoption_candidate_8`
- `iteration_id`: `iteration_20260525_0008_card_adoption_raw_sources_truth`
- `role`: `card_adoption_worker`
- `main_language`: 中文

## 目标

把审计通过的草稿知识卡采纳到 `llm_wiki/kb/`。采纳只做文件移动、轻量整理和最小索引更新，不做重写和扩写。

## 采纳对象

- `card_id`: `raw-sources-readonly-source-of-truth`
- `card_title`: `Raw sources 是只读事实来源`
- `audit_result_required`: `pass`
- `target_card_path`: `llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md`
- `target_provenance_path`: `llm_wiki/kb/provenance/raw-sources-readonly-source-of-truth.md`

## 允许输入

- 当前任务包。
- `draft_card_path`: `llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/draft_card.md`
- `provenance_path`: `llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/provenance.md`
- `audit_report_path`: `llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/artifacts/audit_report.md`

## 禁止输入

- 父聊天上下文。
- 没有通过审计的知识卡。
- 未列出的来源。
- 旧版 `legacy/` 知识库。

## 允许写入

- `llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md`
- `llm_wiki/kb/provenance/raw-sources-readonly-source-of-truth.md`
- `llm_wiki/kb/indexes/cards.md`
- `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/read_log.md`

## 采纳规则

- 只有 `audit_result: pass` 的知识卡可以采纳。
- 采纳后知识卡的 `status` 改为 `accepted`。
- 不新增复杂元数据。
- 不把采纳动作写成枢纽页。
- 出处论证和知识卡分文件保存，但彼此链接。
- 如果知识卡含 `Footnotes`，它必须仍然是最后一个 section。

## 成功门禁

- 知识卡落在 `llm_wiki/kb/cards/`。
- 出处论证落在 `llm_wiki/kb/provenance/`。
- 最小索引包含卡片标题、路径、状态和来源。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 审计结论不是 `pass`。
- 草稿卡或出处论证缺失。
- 采纳会覆盖已有不同内容。
