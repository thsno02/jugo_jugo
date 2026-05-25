# 出处论证：持久 wiki 替代模式

## 对应知识卡

- `llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md`

## 事实来源

本卡事实来自 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:11-13`。`fact_candidates.md` 仅用于核对候选 3 的 statement、fact_type、scope 与 source_evidence 字段，没有用于引入其它事实。

## 支撑关系

证据段落直接说明这个想法不同于只在查询时从原始文档检索；它提出由 LLM 递增式构建并维护一个持久 wiki。该段还说明这个 wiki 是位于用户与原始来源之间的结构化、互链 markdown 文件集合。

来源还明确描述新增来源进入后的处理方式：LLM 不只是为稍后检索而索引来源，而是读取来源、抽取关键信息，并把这些信息整合进既有 wiki。这足以支撑卡片中“在新增来源时把关键信息整合进既有 wiki”的表述。

## 明说与整理

来源明说的部分包括：区别于查询时检索原始文档、LLM 递增构建并维护持久 wiki、wiki 位于用户与原始来源之间、新增来源会被读取并整合进既有 wiki。

整理后的部分是“替代模式”这一中文概括。它来自来源中 “The idea here is different” 与 “Instead of...” 的对比结构，用来概括该段提出的工作方式，而不是额外添加新的机制。

## 成立范围

该事实只在该来源提出的 LLM Wiki 模式范围内成立。它不声称所有 LLM 知识管理系统都采用这种模式，也不声称这种模式已经被外部验证或普遍实现。

## 采纳说明

该卡已根据审计结论 `audit_result: pass` 采纳。成立范围仍限于指定来源段落，不外推为更广泛的事实结论。

