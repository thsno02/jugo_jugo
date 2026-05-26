---
schema: comparison_provenance.v3
draft_card: ../cards/morishige-kb-compile-mem0-overlay.md
draft_provenance: ../provenance/morishige-kb-compile-mem0-overlay.md
similarity_result: ../similarity/morishige-kb-compile-mem0-overlay.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1765
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.125
decision: new_card
audit_required: false
created_time: 2026-05-26T12:06:00+08:00
edited_time: 2026-05-26T12:06:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选都来自 karpathy gist 卡片家族，共享 token `llm`、`wiki`、`的`。top1 (`three-layer-architecture`) jaccard 0.2 全部来自这三个高频功能词；draft 标题里有"森茂"、"Mem0"、"pgvector"、"/kb-compile"等 v2 不可能命中的实体词。表面相关性低。

## 2. draft 与候选在哪里不同

- **来源完全不同**：本 draft 取自 `developersio-jp-pattern`（Classmethod 工程师森茂的日文实践博客），v2 三张候选均出自 karpathy 自述 gist。
- **类型不同**：本 draft 是 `example_pattern`——一份 retrofit 实战记录：在已经运行的 Mem0+pgvector 上叠 LLM Wiki，而不是重建；v2 三张候选都是 `known_fact` 类的概念定义卡。
- top1 `three-layer-architecture` 谈"raw / wiki / schema 三层"——是抽象架构；本 draft 把这三层映射到具体目录（`workspace/knowledge/` = raw、`workspace/wiki/` = compiled、`CLAUDE.md` = schema）并新增 `/kb-compile` 命令实现 ingest 操作。两者是"概念" vs "落地映射"的关系。
- top2 `schema-configuration-document` 谈 schema 作为配置文档；本 draft 仅顺带说 `CLAUDE.md` 充当 schema 层，重心是 ingest 命令与 RAG / wiki 互补判断。
- top3 `health-checks` 谈 LLM 健康检查的抽象任务；本 draft 提到 `/kb-compile --lint` 是手动唤起的 Lint 实现，但重心是混合架构而非 lint 细节。

## 3. 下一步的核心依据

(1) 三张候选都是 v2 内部 karpathy 概念卡；本 draft 是一份独立来源的 retrofit 工程实践，v2 KB 里完全没有同源同主题的卡。(2) 它回答的工程问题（"已有 Mem0/RAG 投入要不要重建"）在 v2 没有对应。结论是 `new_card`。

不是 `provenance_delta`：本 draft 的核心是混合架构与 `/kb-compile` 命令、`_index.md` 入会议程、手动 vs 自动的工程判断——这些都不是 v2 三层架构卡可以"补一段证据"的范畴，而是另一个抽象层。不是 `merge_candidate`：v2 没有任何 example_pattern 或 hybrid retrofit 卡。不是 `revise_before_gate`：边界明确（个人工作流、非企业级、显式标 hacky、未做 A/B 测试），证据全引到行号。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引中加入 `developersio-jp-pattern`；与同批 karpathy 三层 / 三操作卡建立 related 互链作"概念 → 落地"链路。

## 5. 备注

- 这张卡是 v3 第一张 example_pattern 类的"已有基础设施 + 叠 LLM Wiki" 案例，是后续做 retrofit 决策的核心参考。
- 如果未来 v2/v3 KB 中出现"Mem0 vs 文档式 wiki"对比卡，可考虑双向 cross-link，但当前未触发 provenance_delta。
