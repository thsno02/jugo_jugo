# 知识卡审计报告

```text
audit_result: pass
reason:
- 单一事实成立。草稿卡的 `statement` 只主张该来源把 LLM Wiki 架构分成三个层次；正文对三层职责的说明仍围绕同一架构分层事实，没有扩写成主题覆盖、枢纽页或聚类页。
- 来源支撑充分。来源证据 `raw.txt:25-33` 在 `Architecture` 小节直接说明有三层，并分别列出 `Raw sources`、`The wiki` 和 `The schema`；草稿卡的 `support` 与出处论证都准确指向这一结构。
- `fact_type: known_fact` 合理。该事实是单一来源中的明示内容，不是被多来源共同确认的通用事实，因此不应标为 `accepted_fact`。
- `scope` 清楚。草稿卡限定为“仅限该来源提出的架构分层”，没有声称所有 LLM Wiki 都必须采用此架构。
- `status: draft` 合理。出处论证说明当前只用指定来源段落支撑，尚未进入更高层采纳流程。
- 正文可读，接近 zet 风格知识卡。正文用一段话说明三层名称和职责，未引入复杂元数据漂移。
- section 顺序合格。`References` 位于 `Footnotes` 前，`Footnotes` 是最后一个 section。
required_changes:
- 无。
residual_risk:
- 该卡只依据 `raw.txt:25-33` 这一段来源证据，适合作为草稿进入采纳流程；若后续要提升事实强度，仍需要由采纳流程决定是否补充额外来源或更高层验证。
```
