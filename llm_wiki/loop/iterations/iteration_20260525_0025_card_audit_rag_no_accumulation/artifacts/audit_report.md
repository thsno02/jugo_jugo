# 知识卡审计报告

- task_id: `task_20260525_0026_card_audit_candidate_2`
- candidate_id: `候选 2`
- draft_card_path: `llm_wiki/loop/iterations/iteration_20260525_0024_card_drafting_rag_no_accumulation/artifacts/draft_card.md`
- provenance_path: `llm_wiki/loop/iterations/iteration_20260525_0024_card_drafting_rag_no_accumulation/artifacts/provenance.md`
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:7-10`

```text
audit_result: pass
reason:
该卡只表达一个主要事实：指定来源把常见 LLM 文档问答体验描述为查询时检索片段并生成答案的 RAG 形态，并指出这种方式不会在问题之间积累已综合出的知识。`statement`、`support` 和出处论证均可对应到 `raw.txt:7-10`，尤其是第 9 行对上传文件、查询时检索、生成答案、每个问题重新发现知识和没有积累的连续说明。`fact_type: known_fact` 合理，因为卡片记录的是来源中的明确描述，而不是已采纳知识库事实。`scope` 已限制为该来源的对比性描述，没有扩展为所有 RAG 系统的通用评价。`status: draft` 合理。正文可读，接近 zet 风格知识卡。
required_changes:
无。
residual_risk:
该卡只基于单一来源片段，且事实范围是“该来源如何描述 RAG 式文档问答”，后续采纳流程仍需另行处理去重和跨库一致性校验。
```

## 审计检查

- 单一事实：通过。卡片把“RAG 式文档问答体验”和“没有积累”作为同一来源段落中的同一对比性事实处理，没有展开成主题覆盖。
- 来源支撑：通过。`raw.txt:7-10` 支撑上传文件、查询时检索片段、生成答案、每个问题从头重新发现知识、没有积累，以及需要综合多文档问题时反复寻找并拼接片段。
- `fact_type`：通过。`known_fact` 适合记录来源明说内容；本次未进行采纳，所以不应为 `accepted_fact`。
- `support`：通过。`support` 明确指向 `raw.txt:7-10`，并具体说明来源中哪些描述支撑卡片。
- `scope`：通过。范围限定为该来源的对比性描述，明确排除了对所有 RAG 系统或所有文档问答产品的泛化。
- 出处论证：通过。`provenance.md` 清楚区分明说内容与中文整理，并解释草稿状态原因。
- 可读性：通过。标题、statement、support、scope、status 与引用结构清楚，没有扩写成主题分析。
- `References` / `Footnotes` 顺序：通过。`References` 在 `Footnotes` 前。
- `Footnotes` 位置：通过。`Footnotes` 是最后一个 section。
- 元数据漂移：通过。未出现枢纽页、聚类、主题覆盖或复杂元数据。
