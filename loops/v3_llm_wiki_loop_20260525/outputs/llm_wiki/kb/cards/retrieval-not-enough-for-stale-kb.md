---
id: retrieval-not-enough-for-stale-kb
title: 检索工具无法解决"知识库陈旧"问题，只会更快地给出错答案
status: accepted
card_type: distinction
tags: [#enterprise, #retrieval, #rag, #maintenance, #stale-context, #llm-wiki]
created_time: 2026-05-26T11:53:00+08:00
edited_time: 2026-05-28T12:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
provenance_card: ../provenance/retrieval-not-enough-for-stale-kb.md
aliases: ["better retrieval over bad context", "retrieval ≠ maintenance"]
related: [enterprise-llm-wiki-drift-detection-loop, enterprise-llm-wiki-four-properties, karpathy-gist-bookkeeping-burden, anthemcreation-llm-wiki-vs-rag-multi-hop, karpathy-llm-wiki-vs-rag, llm-wiki-contradictions-are-assets]
---

Falconer 指南把"语义搜索 / RAG"和"LLM Wiki 维护循环"明确切开。前者是查询层、后者是底层图谱的真新鲜程度。两者解决的不是同一类问题：

- **检索层（Glean / Notion AI / Confluence AI search 等）**：让用户更容易找到已经被捕获的信息。query → 找到 doc → 回答。
- **维护循环（Karpathy LLM Wiki 模式 / Falconer 企业版）**：保持底层知识图谱本身的准确性——LLM 持续做 linting、起草、矛盾消解。

Falconer 的核心论断："Better retrieval over bad context delivers wrong answers more quickly than slow retrieval over bad context."[^src1] 把它拆成几条规则：

- **检索改善只放大底层准确性**。底层 KB 是正确的，更好的检索让答案更快得到；底层 KB 是陈旧的，更好的检索让错误答案更快地被自信地交付。
- **语义搜索本身不修复 doc**。它不会发现"这条 runbook 在 Q2 后就不再为真"，也不会发现"这两个 doc 互相矛盾"。
- **检索层提高 fluency 但不提高 truth**。retrieval 引擎把 doc 摘要交给 LLM，LLM 据此生成自然答案——但答案的真伪完全继承自被检索 doc 的真伪。
- **PKM 圈子很早就识别了这一点**。Obsidian power user 重视的是"笔记本身能保持真"，而不是"更好的查询入口"。同样的逻辑放到企业规模，只是问题更严重，因为没有一个 Karpathy 当 curator。

操作含义：

- **评估企业 KB 产品时**，要分别问两个问题：(1) 它如何让我查到信息？(2) 它如何确保被查到的信息是 current 的？只回答第一个问题的工具不在"LLM Wiki"范畴。
- **决定要不要在公司接 RAG 之前**，先回答"底层 doc 的 freshness 是否被维护"。如果底层是陈旧 Confluence，先解决维护问题再上 RAG，否则只是把"翻不到答案"换成"快速翻到错答案"。
- **AI agent 消费这套系统时风险被放大**。文章引用 Anthropic 工程团队："context is the scarcest resource for AI agents"——一个没维护的 KB 是 agent 最差的输入，因为 agent 把这些 context 翻译成代码 / 决策的速度远高于人。

边界 / 反例：

- 这条规则**不**说 "retrieval 没用"。retrieval 是查询层的必要组件，特别是在 KB 已经经过维护循环之后。问题是把 retrieval 当成解决维护问题的替代品。
- 在"底层数据频繁变更但没有维护循环"的场景下，retrieval 反而比静态文档危险，因为它把伪权威感拉到最高。
- "维护循环"本身需要 LLM 持续运行，是有成本的——不是"装个搜索就能省下维护成本"，而是"维护成本必须存在，只是从人转到 LLM"。

## References

- "Why retrieval tools don't solve this" 整段：`data/raw/webpage/falconer-enterprise-guide/text.txt` L124–130。
- FAQ 中重申该立场："Why doesn't adding AI search to Confluence or Notion fix this?"：同文件 L148。
- Anthropic 关于 context 是 agent 最稀缺资源：同文件 L74 + L150。

## Footnotes

- `data/raw/webpage/falconer-enterprise-guide/text.txt` L128：`"Retrieval doesn't fix the maintenance problem. A semantic search engine pointed at a stale knowledge base returns confidently-worded answers from documents that haven't been true since Q2. Better retrieval over bad context delivers wrong answers more quickly than slow retrieval over bad context."`
- 同文件 L130：`"What makes Karpathy's LLM Wiki interesting is the maintenance loop, not the search layer. The graph stays accurate because the LLM is doing the linting, drafting, and reconciliation work continuously."`
- 同文件 L148：FAQ：`"Without that loop, smarter search over bad context just produces wrong answers faster."`
- 同文件 L150：`"the Anthropic engineering team describes context as the scarcest resource for AI agents."`
