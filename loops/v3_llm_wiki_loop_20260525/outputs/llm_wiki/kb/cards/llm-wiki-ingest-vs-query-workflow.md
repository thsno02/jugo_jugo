---
id: llm-wiki-ingest-vs-query-workflow
title: LLM wiki 工作流分 ingest（写入侧）与 query（读取侧）两步
status: accepted
card_type: mechanism
tags: [#llm-wiki, #workflow, #obsidian]
created_time: 2026-05-26T15:05:00+08:00
edited_time: 2026-05-28T11:36:00+08:00
edited_entity: llm
source_ids: [anthemcreation-en-guide]
provenance_card: ../provenance/llm-wiki-ingest-vs-query-workflow.md
aliases: [LLM wiki workflow, ingest phase, query phase]
related: [karpathy-llm-wiki-source-executable-analogy, karpathy-llm-kb-three-operations, llm-knowledge-base-five-stage-workflow, file-outputs-back-as-compounding-loop, llm-wiki-karpathy-lint-grounding-trail]
---

## 两个阶段的角色分工

LLM wiki 的运行被显式拆成两个阶段，对应两个不同的"用户↔LLM"接口：

1. **Ingest（写入侧）**
   - 用户把新文档丢进 `/sources/` 子目录。
   - LLM 读源、抽 key idea、然后**只写 wiki**：可能"为新概念建一个 entity 页（如 'Phi-2'，记其 2.7B 参数 / 1.4T token 训练量）"、可能"在已存在页面追加新信息"、可能"识别两源矛盾并合成对比段"、并自动建 backlink[^src1]。
   - **原始资料不可变；用户只读 wiki，LLM 只写 wiki**——角色分离严格[^src2]。
2. **Query（读取侧）**
   - 用户直接查询 canonical wiki，而不是原始文档。
   - 因为 wiki 已经是合成、互联、矛盾消解过的产物，所以可以做 RAG 不能做的多跳推理（"链接三个分散概念回答复杂问题"）[^v3-1]。

中间还有一个**setup 步骤**（约 5 分钟）：把 Karpathy Gist 复制到 LLM agent；建空目录在 Obsidian 中作 vault；建 `/sources/` 子目录与 wiki 隔离；让 LLM ingest 第一份源，自动生成 index 页与 entity 页。

## 为什么这种分阶段有意义

- **写时贵、读时便宜**：ingest 时 LLM 干 "synthesize / link / detect contradiction" 的重活；query 时 LLM 只需在 wiki 上做轻量阅读。这把成本前置，节省每次查询的 token。
- **agents.md 是写阶段的契约**[^v3-2]——它定义"何时新建 entity 页 vs 更新已有"、"如何 format 矛盾"。质量好坏直接决定 ingest 行为是否稳定。
- **Obsidian 不是强需求**——VS Code + Markdown Preview Enhanced、Logseq 均可。只要文件是 flat markdown，工具可换。

## 边界

- Ingest 时 LLM 决定"建新 entity 还是更新旧"——若 agents.md 不严，相似概念会被 fork 成多个页面。
- 当 wiki 增长到几百页，"自动 backlink + 自动矛盾检测"的 token 成本变高，社区有人用 vector search 做 hybrid。
- 文章把 setup 描述成 "5 分钟"[^v3-3]——但这只是最初 1 个 source 的成本；wiki 真正的价值在 10+ 文档累积后才显现[^src3]。

## Footnotes

[^src1]: `data/raw/webpage/anthemcreation-en-guide/text.txt` 第 100-106 行（Ingest 四种典型行为）— "Create a new entity page for a concept that didn't exist yet (e.g., a 'Phi-2' page detailing its 2.7 billion parameters trained on 1.4 trillion tokens) / Update an existing page with new information / Identify and synthesize contradictions between sources / Create automatic backlinks between related pages"
[^src2]: 同文件 第 108 行（角色分离）— "The raw sources remain immutable. The LLM writes to the wiki, the user reads the wiki. The separation of roles is strict."
[^src3]: 同文件 第 176 行（价值在累积中显现）— "Start small. Choose a topic you are actively studying, add your first 5 sources, and let the LLM build the initial pages. The system's value reveals itself in accumulation, not in the initial setup."
[^v3-1]: [anthemcreation-llm-wiki-vs-rag-multi-hop](anthemcreation-llm-wiki-vs-rag-multi-hop.md) — multi-hop 推理优势的本卡。
[^v3-2]: [agents-md-as-schema-layer](agents-md-as-schema-layer.md) — `agents.md` 作为写阶段契约的本卡。
[^v3-3]: [anthemcreation-llm-wiki-setup-cost-envelope](anthemcreation-llm-wiki-setup-cost-envelope.md) — 5 分钟 setup 路径的本卡。
