---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-llm-wiki-three-layers.md
draft_provenance: ../provenance/karpathy-llm-wiki-three-layers.md
similarity_result: ../similarity/karpathy-llm-wiki-three-layers.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.3077
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.2667
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1333
decision: provenance_delta
audit_required: true
created_time: 2026-05-26T12:15:00+08:00
edited_time: 2026-05-26T12:15:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `llm-wiki-three-layer-architecture` (0.308)**：共享 `llm / wiki / 三层 / 的`。draft "三层架构"一节复述的内容与 v2 top1 statement 实质完全相同：raw（不可变源）/ wiki（LLM 编译层）/ schema（规则层）。这是**真共享**——两张卡都来自对 Karpathy 同一段 gist 内容的转述。
- **top 2 `llm-wiki-schema-configuration-document` (0.267)**：共享 `llm / schema / wiki / 的`。draft 把 schema 定义为 "AGENTS.md / CLAUDE.md，告诉 agent wiki 应该长什么样、怎么维护"，与 v2 top2 的 schema 定义（"配置文档…告诉 LLM wiki 的结构、约定、工作流"）是同一事实的不同表述。也是真共享，但 draft 把 schema 只放在三层之一的位置，未单独深谈。
- **top 3 `llm-wiki-health-checks` (0.133)**：共享 `llm / wiki`。draft 的 Lint 操作与 v2 top3 的 health checks 概念对得上（gist 第 4 操作 = Linting），属边缘相邻。

## 2. draft 与候选在哪里不同

- **来源不同（但谈同一原文）**：v2 top1 直接取自 Karpathy gist `raw.txt:25-33`；draft 取自 `marvin-hn-persistent-knowledge/text.txt:29-31`（HN 编辑对 Karpathy gist 的总结式介绍）。两条来源**指向同一个 Karpathy 原叙述**，但 marvin 的二次转述与原 gist 表述略有差异（marvin 用 "AGENTS.md or CLAUDE.md" 举例，原 gist 没有那么具体）。
- **draft 范围显著更宽**：v2 top1 只 statement "作者把 LLM Wiki 架构分为三层"；draft 同时覆盖三件事：
  1. **三层架构**（与 v2 top1 严格重合）；
  2. **三操作 Ingest / Query / Lint**（v2 KB 没有覆盖这个整体；v2 top3 health checks 只触及 Lint 子集）；
  3. **两个特殊文件 index.md / log.md**（v2 KB 完全没有）。
- draft 增加的论点：
  - "任何一层缺失都会失效"（基于职责正交的合理推断）；
  - "Ingest ≠ INSERT、Query ≠ SELECT、Lint ≠ housekeeping" 的 CRUD 拓扑差异；
  - "起步先写 schema.md"操作含义。
- 这些 v2 top1 都没有。

## 3. 下一步的核心依据

- (1)(2) 显示：draft 的"三层架构"段与 v2 top1 是同一事实的二次来源转述，但 draft 整张卡远大于这一段——它把"三层 + 三操作 + 两个特殊文件"作为一个完整 concept 卡呈现。
- 选 `provenance_delta`：
  - draft 为 v2 top1 的"三层"事实提供一份**独立的二次来源**（marvin-hn 编辑团队的转述），值得反向链接进 v2 top1 provenance 以加强可追溯性；
  - draft 同时携带 v2 KB 尚未覆盖的新内容（三操作的整合视角 + index/log 两文件），这些适合作为 draft 卡自身的主要价值留下；
  - draft 的"任何一层缺失都失效"的工程引申也是 v2 top1 没有声明的**新边界**，audit 时可以把它写进 v2 top1 的 provenance 备注。
- 不选 `merge_candidate`：draft 的范围（三层 + 三操作 + 两特殊文件）显著超出 v2 top1，合并会把 v2 top1 撑成另一张卡，破坏其 known_fact 紧致性。
- 不选 `new_card`：忽略"三层"段与 v2 top1 同事实的事实，会让二次来源失去回链。
- 不选 `duplicate_skip`：draft 携带大量 v2 没有的新内容（三操作、index/log、操作含义）。
- 不选 `revise_before_gate`：draft 的范围、边界、引用都已完备。

## 4. 决策

- decision: provenance_delta
- audit_required: true
- 后续动作建议：作为新 card 入库；audit 阶段把 marvin-hn 来源 + "三层职责正交，任何一层缺失都失效"的边界写进 v2 top1 `llm-wiki-three-layer-architecture.md` provenance；同时考虑在 v2 top3 `llm-wiki-health-checks` provenance 里加一条"该健康检查属于 marvin-hn 总结的 Karpathy 三操作之 Lint"的边界备注。

## 5. 备注

- draft 内的"两个特殊文件 index.md / log.md"是 v2 KB 完全缺失的事实，可考虑在后续 loop 单独拆出"index/log 的功能正交"事实卡。
- draft 的 schema 定义引用了 "AGENTS.md or CLAUDE.md"，比 v2 top2 的 schema 定义更具体；audit 时可在 v2 top2 provenance 加一条"marvin-hn 转述里给出的具体文件名举例"的注脚。
