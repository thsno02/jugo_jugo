# 知识卡审计报告

task_id: task_20260525_0029_card_audit_candidate_11
candidate_id: 候选 11
audit_result: pass

## 结论

audit_result: pass
reason:
- 草稿卡 `statement` 位于 `draft_card.md:3`，主要表达一个事实：该来源把 ingest 描述为一个示例操作流程，包含新来源进入 raw collection、交给 LLM 处理、读取来源、讨论要点、写摘要页、更新 index、更新实体和概念页、追加日志。
- 指定来源证据 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:35-38` 中，`raw.txt:37` 直接写明新来源进入 raw collection、让 LLM process it，并以 "An example flow" 列出同一组动作，因此 `statement` 和 `support` 有直接支撑。
- `fact_type: known_fact` 位于 `draft_card.md:5`，合理；该卡是在记录指定来源明说的内容，而不是把该内容提升为已采纳体系事实。
- `scope` 位于 `draft_card.md:9`，清楚限制为该来源示例化的 ingest 操作流程，并排除通用规范、监督强度和批量摄取偏好。
- `support` 位于 `draft_card.md:7`，具体指向 `raw.txt:35-38`，且概括内容与 `raw.txt:37` 的操作顺序一致。
- 出处论证在 `provenance.md:5`、`provenance.md:9`、`provenance.md:19` 和 `provenance.md:23` 说明来源位置、支撑关系、整理方式和成立范围，能够 justify 该卡暂时成立。
- 正文短小、可读，像 zet 风格知识卡；没有枢纽页、聚类、主题覆盖或复杂元数据漂移。
- `References` 位于 `draft_card.md:13`，早于 `Footnotes` 的 `draft_card.md:17`；`Footnotes` 是最后一个 section。
required_changes:
- 无。
residual_risk:
- 证据来自单一来源，且该来源把流程称为 example flow；后续采纳时仍应保留示例范围，避免被改写成通用 ingest 标准。

## 审计问题核对

- 单一事实：通过。`draft_card.md:3` 表达的是一个 ingest 示例流程事实，虽包含多个步骤，但这些步骤属于同一来源句子中的同一示例流程。
- 来源支撑：通过。`raw.txt:37` 直接支撑 `draft_card.md:3` 和 `draft_card.md:7`。
- `fact_type`：通过。`draft_card.md:5` 使用 `known_fact`，符合单一来源明示事实的性质。
- `scope`：通过。`draft_card.md:9` 将适用范围限制在该来源示例。
- `support`：通过。`draft_card.md:7` 明确引用来源行，并说明来源中被使用的动作序列。
- 出处论证：通过。`provenance.md:9` 和 `provenance.md:19` 说明压缩整理没有添加步骤；`provenance.md:23` 说明边界。
- 可读性：通过。卡片结构清楚，正文没有主题综述化。
- `References` / `Footnotes` 顺序：通过。`draft_card.md:13` 在 `draft_card.md:17` 前，且 `Footnotes` 后无新 section。
- 元数据漂移：通过。未出现枢纽页、聚类、主题覆盖或复杂元数据。
