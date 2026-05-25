# 知识卡审计报告

audit_result: pass
reason:
- 知识卡只表达一个主要事实：该来源中的人机角色分工。虽然 statement 同时列出人的职责和 LLM 的职责，但二者共同构成同一条分工事实，没有扩展为主题覆盖或聚类。
- `statement` 被指定来源行支撑。`raw.txt:15-16` 支撑“用户很少亲自写 wiki，LLM 写作并维护，以及人负责 sourcing、exploration、asking the right questions，LLM 负责 summarizing、cross-referencing、filing、bookkeeping”；`raw.txt:68-69` 支撑“人负责 curate sources、direct the analysis、ask good questions、think about meaning，LLM 负责 everything else”。
- `fact_type: known_fact` 合理。这张卡记录的是“该来源如何描述角色分工”，不是已经被知识库采纳或由多源交叉确认的事实，因此不应标为 `accepted_fact`。
- `scope` 清楚限制为“该来源对人机分工的描述”，并明确不外推到所有 LLM 知识库、Obsidian 工作流或人机协作模式。
- `support` 具体到指定来源行，并说明每组行号支撑了哪些职责。出处论证也明确区分了来源明说与中文轻度整理。
- 正文可读，说明段落短而集中，符合一张 zet 风格知识卡的原子事实表达。
- `References` 位于 `Footnotes` 之前，`Footnotes` 是最后一个 section。
- 未发现枢纽页、聚类、主题覆盖或复杂元数据漂移。
required_changes:
- 无必须修改项。
residual_risk:
- 该卡只基于任务指定的一份来源和指定行号成立；进入采纳流程后，仍应保持其范围限制，不应把这条分工描述扩展为通用方法论事实。
