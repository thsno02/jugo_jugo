---
schema: comparison_provenance.v3
draft_card: ../cards/llm-knowledge-base-five-stage-workflow.md
draft_provenance: ../provenance/llm-knowledge-base-five-stage-workflow.md
similarity_result: ../similarity/llm-knowledge-base-five-stage-workflow.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.2
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1818
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1538
decision: new_card
audit_required: false
created_time: 2026-05-26T12:02:00+08:00
edited_time: 2026-05-26T12:02:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top1 `llm-wiki-human-llm-role-division`（"人提问，LLM 维护"）和本 draft 都讲"LLM 维护知识库"，共享 token `llm`、`维护`，jaccard 0.2 主要来自这两个核心词。top2/3 都是 v2 内部架构卡，只共享 `llm`、`的` 这种功能词。三张候选都和 karpathy 来源家族高度相关（top1 来自同一作者 gist；top2/3 也是 gist 衍生卡），所以主题邻近。

## 2. draft 与候选在哪里不同

- **来源不同**：draft 取自 `karpathy-x-launch-post`（X/Twitter 发布推文），v2 top1 取自 `karpathy-gist-llm-wiki`（gist 全文）。同一作者、不同载体、不同表达层次。
- **抽象层不同**：v2 top1 是**角色划分卡**（who does what：人=策展/提问，LLM=写作/维护/簿记），属一句话定性事实。本 draft 是**工作流流程卡**：Ingest → IDE → Q&A → Output → Linting 五个阶段、每阶段独立产物与独立 LLM 任务、按规模触发条件（"~100 篇 / ~400K 词"才进入 Q&A 替代 RAG）。两者在论点轴上正交：一个回答"谁做"，一个回答"按什么顺序做、每步产物是什么"。
- top2 `three-layer-architecture` 讲 schema/sources/wiki 三层**静态结构**；本 draft 讲**动态流程**。静态分层 ≠ 动态阶段（虽然两者会在 ingest 阶段交汇）。
- top3 `schema-configuration-document` 讲 schema 充当配置文档，属架构内部机制；与五阶段流程无关。

## 3. 下一步的核心依据

(1) 三张候选都没有把"LLM 知识库工作流"分解成五个阶段；(2) 即使最近的 top1 也只是"人 vs LLM 谁负责"层面，没有 ingest/IDE/Q&A/output/linting 的流水线展开；(3) draft 的工作流来自不同源（X 发布推文）、不同表达层（流程而非角色），所以是一张全新的 mechanism 卡。结论是 `new_card`。

不是 `provenance_delta`：本 draft 不是给 top1 加一段"五阶段细节"的补充——它的五阶段架构是 X post 自身的结构性内容，自成 mechanism 卡，不是 top1 卡的边角证据。不是 `merge_candidate`：top1 卡的 statement（"人提问 LLM 维护"）与本 draft 的 statement（"工作流由五个阶段构成"）不可合并。不是 `revise_before_gate`：draft 已锁定规模边界、显式标出"this ~small scale" 适用条件、五阶段全部回引源材料原小标题。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；可与 v2 top1（角色划分）作 related 互链——两卡视角互补。

## 5. 备注

- v2 没有任何 source 来自 X post，本 draft 是该 source 的第一张采纳候选。如果接受，建议在 publication_gate 时同步建立 source_id `karpathy-x-launch-post` 在 sources 索引中的项。
- 五阶段中 "Linting"阶段恰好对应 v2 候选附近（v2 有 `llm-wiki-health-checks` 卡），可在卡 body cross-link，但不触发 provenance_delta。
