---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-llm-kb-three-operations.md
draft_provenance: ../provenance/karpathy-llm-kb-three-operations.md
similarity_result: ../similarity/karpathy-llm-kb-three-operations.json
existing_cards:
  - card_id: llm-wiki-query-answer-writeback
    card_path: llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md
    score: 0.1333
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1333
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1176
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- 候选 #1 `llm-wiki-query-answer-writeback`：共享 token `query`、`操作`。draft 的"Query/filing back"这一子论点和该 v2 卡有**真共享**——v2 卡描述 Karpathy gist 中 Query 操作可把好答案归档回 wiki，draft 也把"filing back"列为 Query 操作的关键特征。这不是 jaccard 误中，是真实主题重叠。
- 候选 #2 `llm-wiki-three-layer-architecture`：共享 `llm`、`的`。draft 与候选都引自 Karpathy gist 体系，但 draft 谈"操作语义"层，候选谈"静态架构"层。
- 候选 #3 `llm-wiki-schema-configuration-document`：共享 `llm`、`的`，单纯主题词撞分。

## 2. draft 与候选在哪里不同

- draft 是一张 **mechanism 合卡**，把 Karpathy gist 的三类操作（Ingest / Query / Lint）作为整体描述，并由日文二次源 `developersio-jp-pattern` 转述并加上 RAG 对照与 filing back 反直觉论。它包含：
  - **Ingest = integration** 论点（强调"统合"非"索引化"）；
  - **Query + filing back** 论点（与候选 #1 论点重合）；
  - **Lint = health check** 论点（与未在 top 3 的 v2 `llm-wiki-health-checks` 论点重合）。
- 候选 #1 是单点事实卡，仅记录 Karpathy gist 第 39–40 行对 Query 操作回写好答案的事实，不覆盖 Ingest 与 Lint 维度，也不做"事前编译 vs 事后检索"的对照分析。
- 候选 #2、#3 与 draft 论点轴不同（架构 / schema 层 vs 操作层）。
- 来源类型不同：draft 来源是日文二次解读（`developersio-jp-pattern/text.txt` L54–66），引入了"森茂洋如何理解 Karpathy 三操作"的二次视角；候选 #1 来源是 Karpathy gist 原文。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：draft 是三操作合卡，v2 候选 #1 只覆盖三操作中的一个；合并会把 draft 的 Ingest/Lint 内容丢失。
- 不是 `provenance_delta`：虽然 draft 的 Query 子段可作为 v2 候选 #1 的二次源补强，但 draft 本身是合卡级别的新机制论述，把整张 draft 收成"v2 候选 #1 的 provenance 补丁"是降级使用；正确路径是 draft 成卡，发表时再把 developersio 源以"二次源"形式补到 v2 候选 #1 的 provenance（这一动作在 fusion/audit 而非 comparison 决定）。
- 不是 `duplicate_skip`：仅一个子段重叠，整体不重叠。
- 不是 `revise_before_gate`：draft 已有清晰三操作、引文锚（L58 / L60 / L62 / L66）、边界与误读。门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段可顺手把 developersio 这一日文二次源作为 `llm-wiki-query-answer-writeback` 与 `llm-wiki-health-checks` 两张 v2 原子卡的额外引证候选（属 audit 工作面，本卡不直接做）。

## 5. 备注

- 这张 draft 是本批 LOW score 卡中**少见的"真共享但仍 new_card"**案例：jaccard 0.1333 实际上低估了 Query/filing back 的主题重叠；判 `new_card` 的依据是 draft 与 v2 候选不在同一抽象层（合卡 vs 原子卡）。
- 同批 `kunal-llm-c-rag-misinterpretation` 与 `llm-wiki-ingest-vs-query-workflow` 都涉及对 Karpathy gist 的二次解读，三张卡共同构成"原始 + 多语种二次源"的对照视图。
