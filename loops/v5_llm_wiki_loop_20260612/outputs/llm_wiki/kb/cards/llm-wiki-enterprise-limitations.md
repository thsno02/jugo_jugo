---
id: llm-wiki-enterprise-limitations
title: LLM Wiki 企业场景三项核心限制
status: accepted
card_type: limitation_analysis
tags:
- llm-wiki
- enterprise
- scalability
- access-control
- concurrency
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- atlan-llm-wiki-vs-rag-dynamic-20260524
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-enterprise-limitations.md
canonical_concept: llm-wiki-enterprise-limitations
aliases:
- LLM wiki limitations
- wiki enterprise constraints
- wiki 企业限制
- markdown folder limitations
summary: LLM wiki enterprise limitations 包含三项核心约束：(1) 规模限制——index 必须放入 context，上限约 50k-100k tokens；(2) 访问控制缺失——markdown 文件夹无原生 RBAC，任何有文件访问权的 agent 可读全部内容；(3) 并发冲突——多用户/多 agent 同时更新产生 race conditions 和
  write conflicts，无事务型数据库支持。Karpathy 本人将方案显式限定于个人研究者，这些不是 bug 而是设计假设的后果。
related:
- context-window-threshold-50k-100k
- llm-wiki-three-folder-architecture
- scale-decides-architecture-governance-decides-outcome
---
LLM wiki 方案在企业规模下受三项核心限制约束——这些不是 bug，而是设计假设的后果(consequences of the design assumptions)。[^src-1]

**1. 规模限制**：index 必须放入 context window，将实际知识上限约束在 50,000-100,000 tokens。[^src-2] [^card-1]

**2. 访问控制缺失**：markdown 文件夹无原生角色权限(role-based permissions)，任何拥有文件访问权的 agent 可读取全部内容。[^src-3]

**3. 并发冲突**：多个同时使用的用户或 agent 创建 race conditions、write conflicts，以及潜在的数据损坏——无事务型数据库支持。[^src-4]

Karpathy 本人将方案显式限定于个人研究者。"bypasses RAG"的媒体框定误解了其声明意图。[^src-5]

具体场景示例：一位 fintech 数据工程师有约 80 篇内部研究笔记——wiki 方案可用。当同一公司需要一个合规助手服务 200 名分析师查询 5 个系统中 50,000 份文档并有角色访问控制时——wiki 方案立即崩溃。[^src-6]

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "FAQs" P93 -- "the limitations are not bugs, they are consequences of the design assumptions."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "FAQs" P91 -- "the index must fit in context, capping practical knowledge at 50,000-100,000 tokens"
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "FAQs" P91 -- "markdown folders have no native role-based permissions, meaning any agent with file access can read any content"
[^src-4]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Head-to-head comparison" P58 -- "multiple simultaneous agents updating a markdown wiki create race conditions, write conflicts, and potential for data corruption without transactional database support"
[^src-5]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Head-to-head comparison" P58 -- "Karpathy himself scoped the approach explicitly to individual researchers - the 'bypasses RAG' framing misrepresents his stated intent."
[^src-6]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/markdown.md` -- "Head-to-head comparison" P59 -- "the LLM wiki breaks down immediately: index overflow, no access control layer, and write conflicts across simultaneous users"
[^card-1]: 参见 [[context-window-threshold-50k-100k]] — 规模限制的详细分析
