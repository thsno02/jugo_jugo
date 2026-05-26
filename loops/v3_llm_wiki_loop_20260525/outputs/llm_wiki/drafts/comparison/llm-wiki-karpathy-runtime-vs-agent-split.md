---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-karpathy-runtime-vs-agent-split.md
draft_provenance: ../provenance/llm-wiki-karpathy-runtime-vs-agent-split.md
similarity_result: ../similarity/llm-wiki-karpathy-runtime-vs-agent-split.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.3
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.25
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1818
decision: new_card
audit_required: false
created_time: 2026-05-26T12:25:00+08:00
edited_time: 2026-05-26T12:25:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `llm-wiki-three-layer-architecture` (0.3)**：共享 `llm / wiki / 的`。token 共享只是基础词。draft 谈的是 `@harrylabs/llm-wiki-karpathy` 这个具体 package 的 runtime / agent 责任划分；v2 top1 谈 Karpathy 原 gist 的 raw / wiki / schema 三层。两者**不在同一切分维度**——runtime/agent 划分横切 raw/wiki/schema 三层。
- **top 2 `llm-wiki-schema-configuration-document` (0.25)**：共享 `llm / wiki / 的`。同样是基础词命中；v2 top2 谈 schema 定义；draft 完全不谈 schema 是配置文档这件事。低分误中。
- **top 3 `llm-wiki-health-checks` (0.182)**：共享 `llm / wiki`。draft 有 `kb_lint` 提及一句，但论点不在 health checks 上。低分误中。

## 2. draft 与候选在哪里不同

- **来源完全独立**：v2 三张候选都来自 Karpathy 原始材料（gist + quote text）；draft 来自 `clawhub-llm-wiki-karpathy/text.txt:146-189`，是 `@harrylabs/llm-wiki-karpathy` v0.4.4 这个 package README 的 "Runtime Philosophy" / "Multimodal Ingest Model" / "Still Out of Scope" 三节。两份证据完全无交叉。
- **卡片类型与主张完全不同**：
  - v2 top1 = 三层架构事实；v2 top2 = schema 配置文档定义；v2 top3 = health checks 清理。
  - draft = distinction 类，给出该 package 显式的二段责任划分：
    - runtime 拥有 canonical paths / IDs / validation / deterministic writes / manifest-backed representation tracking / generated wiki navigation；
    - agent 拥有 summarization / OCR / vision / synthesis / 决定笔记归属 / 长期改进 wiki；
    - `kb_prepare_source_bundle` 是 runtime/agent 握手点；
    - out-of-scope：embeddings、向量搜索、DB 索引、rename 跟踪、内置 OCR / vision、自治后台 agent。
- **抽象层级不同**：v2 卡谈的是 Karpathy 原概念；draft 谈的是某具体工程 package 的内部架构选择。两者横切关系：draft 的 runtime/agent 二分本质上是对 raw/wiki/schema 三层职责的**正交切分**，而非同一切分。
- v2 KB 完全没有覆盖 runtime/agent 责任划分这一论点。

## 3. 下一步的核心依据

- (1)(2) 显示：draft 与 v2 三张候选的 token 重合都是基础词；论点、来源、抽象层级都不同；v2 KB 没有现成的卡可被 draft 加证据或重构。
- 选 `new_card`：
  - draft 是一个全新的工程 distinction 卡（runtime owns structure, agent owns synthesis）；
  - draft 不为任何 v2 卡补证据，也不修正任何 v2 卡 statement；
  - 引入新卡不与 v2 任何卡冲突。
- 不选 `provenance_delta`：draft 内容不属于 v2 任一卡 statement 的证据增量。
- 不选 `merge_candidate`：v2 没有任何可合并的对应卡。
- 不选 `duplicate_skip`：内容是 v2 KB 缺失的。
- 不选 `revise_before_gate`：draft 引用清楚（README 行号明确）、边界完整（out-of-scope 列出、Obsidian-style markdown vault 适用范围声明）。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；可在 draft `related` 保留 `llm-knowledge-base-five-stage-workflow` 互链以将"具体 package 的二段划分"接入"Karpathy 五阶段工作流"。

## 5. 备注

- token 高分（0.3）几乎完全由 `llm / wiki / 的` 解释——这是 worker prompt 已提示的"v2 schema-configuration / three-layer-architecture / health-checks 三张卡因高频 token 反复成为 top 3"的典型例子，需主动判定为低实质相关。
- 该 draft 与同 batch 的 `karpathy-llm-wiki-obsidian-plugin-overview`、`my-llm-wiki-three-layer-implementation` 同属"Karpathy LLM Wiki 在不同 package 中的实现"主题集，但**各自工程立场不同**（Greener-Dalii 是 monolithic Obsidian plugin、phuc-nt 是单命令 CLI、@harrylabs 把 runtime/agent 分离），不应合并。
