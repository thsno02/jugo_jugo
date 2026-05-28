---
id: karpathy-wiki-full-context-vs-rag
title: "Feed full wiki context, not chunked RAG retrieval"——Karpathy 立场在插件中的执行
status: accepted
card_type: distinction
tags: [#karpathy-wiki, #rag, #long-context, #design-philosophy]
created_time: 2026-05-26T12:40:00+08:00
edited_time: 2026-05-28T11:26:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
provenance_card: ../provenance/karpathy-wiki-full-context-vs-rag.md
aliases: [full-context query, anti-RAG stance, long-context model recommendation]
related: [karpathy-llm-wiki-obsidian-plugin-overview, karpathy-wiki-extraction-granularity, karpathy-llm-wiki-vs-rag, anthemcreation-llm-wiki-vs-rag-multi-hop, hn-llm-wiki-is-just-rag-debate, auto-index-replaces-rag-at-small-scale, robin-cartier-scale-ceiling]
---

## 立场陈述

Karpathy LLM Wiki Obsidian 插件页面明确声明：

> "This plugin follows Karpathy's philosophy: feed the LLM full Wiki context, not chunked RAG retrieval. Long-context models are strongly recommended — the larger your Wiki grows, the more context the LLM needs."

并给出 Karpathy 对 RAG 的原始批评："RAG fragments knowledge and breaks the LLM's ability to reason across the full knowledge graph."

## 与 RAG 范式的具体差异

| 维度 | 传统 RAG | Karpathy LLM Wiki 模式 |
| --- | --- | --- |
| 知识表征 | 切块后嵌入 + 向量索引 | 互联的 markdown 页 + `[[wiki-links]]` |
| 查询时机制 | top-k 检索相关 chunks 拼入 prompt | 把（相关子集或全部的）**结构化 wiki** 送入长上下文 |
| 推理范围 | 受限于检索召回 | 跨整个知识图谱推理 |
| LLM 选型 | 短上下文也可工作 | **强烈推荐**长上下文模型 |
| 推理质量退化模式 | 检索遗漏导致空洞回答 | 上下文过长导致注意力稀释 |

## 工程后果：模型选型表

页面给出的"Value Pick"档全是长上下文模型：

| 档位 | 模型 | 上下文窗口 | 主要卖点 |
| --- | --- | --- | --- |
| Value Pick | DeepSeek V4-Flash | 1M tokens | $0.14/M，284B MoE，批量 ingestion 经济 |
| Value Pick | Gemini-3.5-Flash | 1M tokens | 4× 输出速度优于 GPT-5.5 |
| Value Pick | Qwen3.6-Plus | 1M tokens | 强 coding/agentic |
| Value Pick | Grok-4 | 2M tokens | 极大 wiki 友好 |
| Balanced | Claude Sonnet 4.6 | 1M tokens | $3/$15 per million |
| Lightweight | Claude Haiku 4.5 | 200K tokens | 小 wiki 可用 |
| Flagship | Claude Opus 4.7 / GPT-5.5 | 1M tokens | 选择性使用 |

本地 Ollama 上下文典型 8K–128K，所以页面建议**云端 ingestion + 本地 query** 的混合方案——本地模型在小 wiki 子集上可用，但不能承担全 wiki 查询。

## 边界与代价

- **长上下文模型成本上升**：每次查询都送大量 token，token 经济性比 RAG 差，依赖模型供应商的长上下文定价；
- **注意力稀释**：即便 1M 上下文可装入，超长文本上的事实回忆和推理精度未必维持高位；
- **wiki 增大就触顶**：当 wiki 超过最大上下文时，必须降级到选择性载入（实际上接近 RAG），插件未在页面公开此时的退化策略；
- **混合策略需要用户协调**：云端 ingestion + 本地 query 把成本与隐私两个维度都摊在用户头上。

## 与本 batch 其它立场的对照

- 与 **mem0**（dense memory retrieval）相对：mem0 仍是"检索 + 注入"路线，但检索单位是**已抽取的事实**而非 raw chunks；
- 与 **memory-as-metabolism** 的 CONTEXTUALIZE 相比：后者要把外部源压缩到用户当前 working depth，本插件则是"先抽实体/概念到结构化页，再以全 wiki 上下文供 LLM 推理"——两者都拒绝"原文切块嵌入"，但在压缩 vs 不压缩、有 vs 无 governance 上分歧明显。

## References

- 来源页面：`data/raw/webpage/obsidian-community-plugin/text.txt`。
- 第 343–346 行：full-context 立场与 Karpathy 对 RAG 的批评。
- 第 348–370 行：模型选型表。
- 第 371–375 行：Ollama / Anthropic Compatible 配置说明。

## Footnotes

[^1]: full-context 立场 verbatim（第 344 行）："This plugin follows Karpathy's philosophy: feed the LLM full Wiki context, not chunked RAG retrieval. Long-context models are strongly recommended — the larger your Wiki grows, the more context the LLM needs."

[^2]: 为什么不用 RAG verbatim（第 346 行）："Karpathy's original critique argues that RAG fragments knowledge and breaks the LLM's ability to reason across the full knowledge graph."

[^3]: 模型选型表来自第 348–366 行；本地 Ollama 上下文限制与混合方案建议来自第 371 行。
