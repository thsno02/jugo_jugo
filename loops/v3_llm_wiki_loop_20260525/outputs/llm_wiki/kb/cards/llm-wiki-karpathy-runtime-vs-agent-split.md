---
id: llm-wiki-karpathy-runtime-vs-agent-split
title: llm-wiki-karpathy 的 runtime / agent 责任分割
status: accepted
card_type: distinction
tags: [#llm-wiki, #karpathy, #runtime, #agent, #obsidian, #plugin]
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-28T11:42:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
provenance_card: ../provenance/llm-wiki-karpathy-runtime-vs-agent-split.md
aliases: ["runtime owns structure, agent owns synthesis", "@harrylabs/llm-wiki-karpathy 责任划分"]
related: [llm-wiki-karpathy-multimodal-representation-path, llm-knowledge-base-five-stage-workflow, llm-wiki-karpathy-lint-grounding-trail, karpathy-llm-wiki-obsidian-plugin-overview, llm-wiki-mcp-design-boundary-mechanics-not-content, karpathy-llm-kb-three-operations]
---

`@harrylabs/llm-wiki-karpathy`（v0.4.4）这个 plugin 把 LLM Wiki 工作流明确切成两层职责，是它和"一个 LLM 全做"型方案的关键差别：

- **Runtime 拥有**[^src1]："canonical paths / canonical IDs / validation / deterministic writes / manifest-backed representation tracking / generated wiki navigation"。也就是：路径、ID、模式校验、写入是确定性的，且导航是生成的而非人手写的。这意味着两次运行同一份输入，runtime 必须给同样的 wiki 结构。
- **Agent 拥有**[^src2]："summarization / OCR, vision, or profiling work performed outside the runtime / synthesis / deciding whether a result belongs in output, concept, entity, or synthesis / improving the wiki over time instead of leaving value trapped in chat"。也就是：内容侧理解、合成、判断"这是 output 笔记还是 concept 笔记"这类语义决策都留给 agent。

之所以这样切：

- **可重复性**：路径与 ID 必须确定性，否则 wiki 内部的相互链接会随机失效。把所有"结构"动作放进 runtime，agent 永远不直接动文件名。
- **代价对齐**：合成和 OCR / vision 是高代价、外部 API 依赖的步骤，明确划给 agent，这样 runtime 可以保持轻量且本地可跑。
- **可审计**：runtime 提供的 `kb_lint`、manifest schema v2、representation 追踪都是为了"agent 做完后能被 lint 检查 grounding"。如果 agent 也能写结构，lint 就失去基准。

操作含义：

- `kb_prepare_source_bundle` 是 runtime/agent 的关键握手点[^src3]：对非文本资产（PDF、图片），runtime 一次性返回 raw metadata、reviewed asset refs、stored representations、compile_readiness 状态；agent 看到这些后才决定下一步生成什么 representation 或 source note[^v3-1]。
- agent 不应该直接写 wiki/、不应该自己定 source id，否则会和 runtime 的 manifest 冲突——`kb_repair_source_ids` 提供逃生口但属补救手段。
- `kb_map_gaps` / `kb_promote_gap` 让 agent 显式提出"我要补一张笔记"，runtime 决定如何落位。

边界：

- runtime 显式 out-of-scope[^src4]：embeddings、向量搜索、数据库索引、rename 跟踪、内置 OCR / vision、自治后台 agent。任何依赖这些的功能都必须由 agent 层或外部工具提供。
- 这套划分针对 Obsidian-style markdown vault，不直接适用于"内容存储在 DB / 第三方 wiki"的场景。

## Footnotes

[^src1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` L148-160 — runtime 拥有 "canonical paths / canonical IDs / validation / deterministic writes / manifest-backed representation tracking / generated wiki navigation"
[^src2]: 同文件 L162-172 — agent 拥有 "summarization / OCR, vision, or profiling work performed outside the runtime / synthesis / deciding whether a result belongs in output, concept, entity, or synthesis / improving the wiki over time instead of leaving value trapped in chat"
[^src3]: 同文件 L172-174 — "kb_prepare_source_bundle is the bridge between those layers for non-text assets"
[^src4]: 同文件 L181-187 — out-of-scope: "embeddings or vector search / database-backed indexing / rename tracking / built-in OCR, vision, or PDF parsing inside the runtime itself / autonomous background agents inside the package"
[^v3-1]: [llm-wiki-karpathy-multimodal-representation-path](llm-wiki-karpathy-multimodal-representation-path.md) — `kb_prepare_source_bundle` 握手与 representation-first ingest 的展开。
