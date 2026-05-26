---
schema: comparison_provenance.v3
draft_card: ../cards/langgraph-tool-runtime-store-access.md
draft_provenance: ../provenance/langgraph-tool-runtime-store-access.md
similarity_result: ../similarity/langgraph-tool-runtime-store-access.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.0
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:08:30+08:00
edited_time: 2026-05-26T16:08:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "通过 ToolRuntime 让工具读写 LangGraph Store" **无 token 共享，score 全部 0.000**。三个候选都源于同一条 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序，没有实质邻近。

## 2. draft 与候选在哪里不同

- draft 主题：LangChain / LangGraph 官方文档展示的工具访问 long-term memory 接入方式——`ToolRuntime[Context]` 泛型 + `runtime.store.get/put/search`，附 Python 代码例。论据轴是 agent framework API 设计 + memory abstraction。
- 候选 1：Karpathy 推文 idea file 抽象性的事实卡。
- 候选 2：同推文 idea file 分享逻辑的事实卡。
- 候选 3：LLM 对 wiki 做 health checks 的事实卡。

draft 是具体的工程文档（含 `from langchain.tools import ToolRuntime, tool` 代码）；候选是 Karpathy 一条推文里关于 "idea file" 的理念性叙述——两者既无概念交叠，也无 API / 实现 / 工程 mapping。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 完全不包含 LangGraph / store / tool runtime / API 内容 → `new_card`。draft 已含读写代码示例、多模型选项卡说明、设计选择、局限，证据完整 → 不是 `revise_before_gate`。v2 无 LangChain / agent framework 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `langgraph-store-namespace-key-json-model` 等同系列 draft 内部 related。

## 5. 备注

LangGraph / LangChain 工程文档主题在 v2 KB 中完全缺席；本卡首批引入。
