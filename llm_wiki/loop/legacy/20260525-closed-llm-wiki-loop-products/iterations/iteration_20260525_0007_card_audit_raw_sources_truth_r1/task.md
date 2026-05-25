# 任务包模板：知识卡审计

- `task_id`: `task_20260525_0008_card_audit_candidate_8_r1`
- `iteration_id`: `iteration_20260525_0007_card_audit_raw_sources_truth_r1`
- `role`: `card_audit_worker`
- `main_language`: 中文

## 目标

审计一张草稿知识卡是否能进入采纳流程。审计结论必须基于任务包指定的知识卡、出处论证和来源证据。

## 允许输入

- 当前任务包。
- `draft_card_path`: `llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/draft_card.md`
- `provenance_path`: `llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/provenance.md`
- `source_evidence_path`: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- `source_evidence_lines`: `27-30`

## 禁止输入

- 父聊天上下文。
- 旧审计报告。
- 未列出的来源。
- 枢纽页、聚类页或主题覆盖文档。

## 允许写入

- `llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/loop_status.md`
- `llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/loop_delivery.md`
- `llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/read_log.md`
- `llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/artifacts/audit_report.md`

## 审计问题

- 这张卡是否只表达一个主要事实？
- `statement` 是否被来源支撑？
- `fact_type` 是 `known_fact` 还是 `accepted_fact`，是否合理？
- `scope` 是否清楚限制了适用范围？
- `support` 是否足够具体？
- 出处论证是否能 justify 这张卡暂时成立？
- 正文是否可读，是否像 zet 风格知识卡？
- `References` 是否在 `Footnotes` 前？
- `Footnotes` 是否是最后一个 section？
- 是否出现枢纽页、聚类、主题覆盖或复杂元数据漂移？

## 结论格式

```text
audit_result: pass | revise | reject
reason:
required_changes:
residual_risk:
```

## 成功门禁

- 审计结论明确。
- 每条问题都指向知识卡、出处论证或来源证据。
- 没有直接采纳知识卡。
- `loop_status.md`、`loop_delivery.md`、`read_log.md` 都存在。

## 阻塞条件

- 缺少知识卡。
- 缺少出处论证。
- 缺少来源证据。
- 来源证据与知识卡无法对应。
