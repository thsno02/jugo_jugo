---
id: karpathy-llm-wiki-obsidian-plugin-overview
title: Karpathy LLM Wiki 的 Obsidian 插件实现：把 Karpathy 三层架构落地到日常写作流
status: draft
card_type: example_pattern
tags: [#obsidian, #karpathy-wiki, #llm-wiki, #plugin]
created_time: 2026-05-26T12:30:00+08:00
edited_time: 2026-05-26T12:30:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
provenance_card: ../provenance/karpathy-llm-wiki-obsidian-plugin-overview.md
aliases: [Karpathy LLM Wiki Obsidian Plugin, karpathywiki, Greener-Dalii plugin]
related: [karpathy-wiki-full-context-vs-rag, karpathy-wiki-aliases-and-dedup, karpathy-wiki-extraction-granularity, anthemcreation-llm-wiki-setup-cost-envelope, my-llm-wiki-three-layer-implementation, beyond-the-token-bottleneck-llm-wiki-case-study, llm-wiki-karpathy-runtime-vs-agent-split]
---

## 这是什么

由 Greener-Dalii 发布的 Obsidian 社区插件 `Karpathy LLM Wiki`（v1.10.2 at scan time，Obsidian 官方分数 94/100，~781 下载，8 语言原生支持）将 Karpathy 提出的"LLM 维护的个人 wiki"思想落到 Obsidian vault 中。

## Karpathy 三层架构在插件中的实现

```
sources/   # 📄 用户的源文档（只读）
   ↓ ingest
wiki/      # 🧠 LLM 生成的 wiki 页面
   ↓ query / maintain
schema/    # 📋 wiki 结构配置（命名、模板、分类）
```

- `sources/` 保留**只读**——插件承诺**永不修改源文件**；
- `wiki/` 是 LLM 写的 markdown 集合，由插件按 schema 与命令产出；
- `schema/` 是用户和 LLM **共演化**的配置层。

`wiki/` 内进一步分层：
- `wiki/sources/<file>.md` — 源摘要；
- `wiki/entities/<entity-name>.md` — 实体页（人、组织、产品、事件等）；
- `wiki/concepts/<concept-name>.md` — 概念页（理论、方法、术语等）；
- `wiki/index.md` — 自动生成的索引；
- `wiki/log.md` — 操作日志。

## 命令面

通过 Cmd+P 调出的命令（与 Obsidian 命令调色板一致）：

| 命令 | 行为 |
| --- | --- |
| 📥 Ingest single source | 选一个 note，抽取实体与概念，生成 wiki 页 |
| 📂 Ingest from folder | 选文件夹批量生成；自动跳过已处理文件（Smart Batch Skip） |
| 🔍 Query wiki | 流式 markdown 对话，回答中带 `[[wiki-links]]` |
| 🛠️ Lint wiki | 完整健康扫描：重复 / 死链 / 空页 / 孤儿 / 缺别名 / 矛盾 |
| 📋 Regenerate index | 手工重建 `wiki/index.md` |
| 💡 Suggest schema updates | LLM 分析 wiki 并提出 schema 改进 |

## 多提供商与本地模型支持

文档列出：Anthropic、Anthropic Compatible（含 Coding Plan endpoint）、Google Gemini、OpenAI、DeepSeek、Kimi、GLM、Ollama、OpenRouter、自定义。Ollama 本地不需 API key；其他需 API key。所有客户端在 HTTP 5xx / 429 上做指数退避自动重试（最多 2 次）。

## 模型选型建议（页面立场）

页面明确"This plugin follows Karpathy's philosophy: feed the LLM full Wiki context, not chunked RAG retrieval"——因此**强烈推荐长上下文模型**。给出的"价值优选"档：

- DeepSeek V4-Flash（1M context，$0.14/M）；
- Gemini-3.5-Flash（1M context，4× 输出速度优于 GPT-5.5）；
- Qwen3.6-Plus / Grok-4（2M context）；
- 平衡：Claude Sonnet 4.6；
- 旗舰：Claude Opus 4.7 / GPT-5.5。

本地 Ollama 受限于 8K–128K 上下文，页面建议"云模型 ingestion + 本地模型 query"的混合方案。

## 一致性与维护机制（页面突出的"非 RAG"特性）

- **Mandatory page aliases**：每个生成页至少含 1 个别名（翻译、缩写、别名），是跨语言去重的支撑；
- **Semantic-tier duplicate detection**（v1.7.10+）：Tier 1 始终 LLM 验证（跨语言、缩写、高相似度标题），Tier 2 填充剩余 token 预算；
- **Contradiction state machine**：detected → review_ok → resolved（AI 修复）或 detected → pending_fix（人工）；
- **Smart Knowledge Fusion**：多源更新合并新信息且保留矛盾的归属，`reviewed: true` 标记的页面**受写保护**；
- **Smart Fix All**：按因果顺序批修——污染页 → 别名 → 重复合并 → 死链 → 孤儿 → 空页扩展。

## 平台与许可

- Obsidian 1.6.6+，桌面 / 移动均可；
- MIT 许可；
- 4 周内已发布 27 个版本，迭代节奏快；
- 关键依赖：Anthropic SDK、OpenAI SDK、Obsidian Plugin API。

## References

- 来源页面：`data/raw/webpage/obsidian-community-plugin/text.txt`。
- 第 80–115 行：概念与"LLM-Wiki 是什么"。
- 第 196–212 行：命令面。
- 第 376–390 行：三层架构与代码组织。
- 第 343–370 行：模型选型表。
- 第 256–305 行：知识质量与维护特性。

## Footnotes

[^1]: 三层架构 verbatim（第 379 行）："sources/ # 📄 Your source documents (read-only) ↓ ingest wiki/ # 🧠 LLM-generated Wiki pages ↓ query / maintain schema/ # 📋 Wiki structure configuration (naming, templates, categories)"

[^2]: 安全升级承诺 verbatim（第 449 行）："The plugin never modifies your source files. Backup wiki/ → update plugin → Regenerate index → Lint Wiki → fix selectively."

[^3]: 矛盾状态机 verbatim（第 284 行）："Contradiction State Machine — detected → review_ok → resolved (AI fix) or detected → pending_fix (manual)"
