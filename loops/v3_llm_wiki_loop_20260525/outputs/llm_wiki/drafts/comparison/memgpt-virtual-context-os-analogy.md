---
schema: comparison_provenance.v3
draft_card: ../cards/memgpt-virtual-context-os-analogy.md
draft_provenance: ../provenance/memgpt-virtual-context-os-analogy.md
similarity_result: ../similarity/memgpt-virtual-context-os-analogy.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0909
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.05
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

共享 token 仅 `llm`、`的`。draft 的核心 token `MemGPT`、`OS`、`RAM`、`磁盘`、`内存`、`窗口` 都不出现在候选标题。jaccard 0.1 完全由 `llm/的` 撞分。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-three-layer-architecture`：Karpathy gist 的三层架构。与 MemGPT OS 类比无关。
- 候选 #2 `llm-wiki-schema-configuration-document`：schema 配置文档定义。无关。
- 候选 #3 `idea-file-abstract-vague`：idea file 抽象性。无关。
- draft 来源是 `arxiv-memgpt` abstract / intro / method / conclusion，论点是 MemGPT 把 OS 虚拟内存范式搬到 LLM 上（上下文 = RAM、外部存储 = 磁盘、function call = 系统调用），让上下文受限的 LLM 表现得像无限上下文。v2 KB 完全没有 MemGPT 或 virtual context management 卡。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 无 MemGPT / virtual memory analogy 系列卡。
- 不是 `provenance_delta`：候选都是 Karpathy gist 元事实，无对接面。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有 abstract / intro / method / conclusion 引文锚（行 1197 / 1555–1575 / 1633–1637 / 709）、与"线性堆 token / 被动 RAG"的两条对照路线、边界（GPT-3.5 函数调用能力不足致嵌套 KV 任务下降 / OS 类比有限性）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 abstract 行 1197 的 verbatim 引用是否字字对齐。

## 5. 备注

- 与 draft 自身 related 列出的 `memgpt-main-vs-external-context`、`memgpt-queue-eviction-policy` 构成 MemGPT 三联视图。
- jaccard 0.1 完全由"llm/的"产生，是典型机械撞分。
