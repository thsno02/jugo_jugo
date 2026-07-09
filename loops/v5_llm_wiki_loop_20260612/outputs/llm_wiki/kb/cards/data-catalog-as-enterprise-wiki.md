---
id: data-catalog-as-enterprise-wiki
title: 数据目录作为 LLM Wiki 的企业等价物
status: accepted
card_type: architectural_analogy
tags:
- data-catalog
- enterprise-knowledge
- llm-wiki
- governance
- metadata
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- atlan-llm-wiki-vs-rag-dynamic-20260524
evidence_basis: practitioner_report
justification: ../justification/data-catalog-as-enterprise-wiki.md
canonical_concept: data-catalog-as-enterprise-wiki
aliases:
- data catalog as enterprise wiki
- enterprise LLM wiki
- 数据目录企业等价
- governed data catalog
summary: data catalog as enterprise wiki：材料将经治理的数据目录(data catalog)定位为 LLM wiki 在企业规模下的结构等价物。对应关系：策展资产摘要=wiki articles、血缘交叉引用=backlinks、业务术语定义=concept definitions、认证状态=quality scores、active metadata propagation=自动新鲜度机制（非
  manual health checks）、策略级 RBAC=访问控制（非 file system permissions）。通过 MCP server/API 连接到 LLM stack。
related:
- llm-wiki-three-folder-architecture
- two-tier-knowledge-architecture
- scale-decides-architecture-governance-decides-outcome
- enterprise-llm-wiki-architecture
---

材料将经治理的数据目录(governed data catalog)定位为 Karpathy 个人 wiki 在企业规模下最接近的结构等价物。[^src-1]

**功能映射**：

| Wiki 组件 | 数据目录等价 |
|---|---|
| wiki/ 文章 | 策展资产摘要(curated asset summaries) |
| backlinks | 血缘交叉引用(lineage cross-references) |
| 概念定义 | 业务术语表(business glossary) |
| — | 认证状态(certification/quality scores) |
| health check prompts | active metadata propagation（管道运行时自动推送，非手动触发） |
| file system permissions | 策略级 RBAC（FinanceAgent 不可达 HR 数据） |
| index.md | 结构化查询层（处理百万资产无 context overflow） | [^src-2]

**关键增量**：数据目录在 wiki 三文件夹的每个功能之上增加了治理层——访问控制从无到策略级，新鲜度从手动到自动，规模从百篇到百万。[^src-3]

**连接方式**：企业团队通过 MCP server 和 API 将已治理、已认证、始终新鲜的元数据层连接到 LLM stack——"connection is the missing piece, not the construction"。[^src-4] [^card-1]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "How Atlan approaches the enterprise knowledge base" P75 -- "Atlan's data catalog is structurally the enterprise version of what Karpathy built for himself."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "How Atlan approaches the enterprise knowledge base" P75 -- "curated asset summaries (documentation), cross-references (lineage), concept definitions (business glossary), certification status (quality scores), and a freshness mechanism via active metadata propagation"
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "How Atlan approaches the enterprise knowledge base" P75 -- "Where the markdown folder has no access control, the catalog enforces policy-level RBAC"
[^src-4]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "How Atlan approaches the enterprise knowledge base" P76 -- "rather than building a shadow knowledge layer on top of ungoverned source data. The enterprise LLM knowledge base the organization needs already exists in most cases. The connection is the missing piece, not the construction."
[^card-1]: 参见 [[llm-wiki-three-folder-architecture]] — 个人版 wiki 架构，此卡为其企业映射
