---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-gist-bookkeeping-burden.md
draft_provenance: ../provenance/karpathy-gist-bookkeeping-burden.md
similarity_result: ../similarity/karpathy-gist-bookkeeping-burden.json
existing_cards:
  - card_id: llm-wiki-wiki-layer-generated-markdown-directory
    card_path: llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md
    score: 0.1818
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1429
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1304
decision: new_card
audit_required: false
created_time: 2026-05-26T12:16:00+08:00
edited_time: 2026-05-26T12:16:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选**全部**来自同一源 `karpathy-gist-llm-wiki` —— draft 也是这个源，所以是同源关系（不是 token 误中）。top1 `wiki-layer-generated-markdown-directory` 共享 `llm`、`wiki`、`和`、`维护`——这是真共享：draft 论"维护成本接近零"、v2 卡谈"LLM 负责维护"。top2/top3 共享通用功能词。同源 + 维护话题，需要谨慎判断是否落到 `provenance_delta` 而非 `new_card`。

## 2. draft 与候选在哪里不同

- **gist 段落不同**：v2 top1 取 `raw.txt:31-32`（"The wiki" 架构定义段）；本 draft 取 `text.txt:64-70`（"Why this works" 段）+ `text.txt:37`（"A single source might touch 10-15 wiki pages"）+ `text.txt:41`（lint 段）。同一份 gist，不同小节，给出的论点完全不同。
- **fact_type 与论点轴不同**：
  - v2 top1 是 `known_fact`：陈述 wiki 层"由 LLM 生成和维护"的角色边界。
  - 本 draft 是 `concept`：论证**为什么**这个分工能持续运转——核心主张是"bookkeeping 才是真瓶颈，不是 reading 或 thinking；LLM 把这块降到零"，并附"维护超线性增长 vs 内容 sub-linear 价值"的数学性解释、"人侧不可替代的思考层"的分工原文。
- v2 top1 完全不触及成本/有效性论证；本 draft 也不重复"LLM 负责生成 wiki"那条事实，而是 _建立在_ 那条事实之上去解释 _为什么_。
- top2 `three-layer-architecture` 是结构分层，与"为什么这种结构可行"的论证无关。
- top3 `schema-configuration-document` 与 bookkeeping 论证无关。

## 3. 下一步的核心依据

(1) 三张候选都不覆盖"为什么 LLM Wiki 工作"这一概念论证；(2) 本 draft 自带独立 statement、独立证据（行 64–70 完整段）、独立边界（大规模 LLM 仍会漏更新、错误模式从遗漏转为幻觉）、独立操作含义（评估 PKM 工具看是否把 bookkeeping → 零作为设计目标）——是一张能独立存活的 concept 卡。结论是 `new_card`。

不是 `provenance_delta`：尽管同源同主题家族，本 draft 不是给 v2 top1 卡补一段边角证据——它是 gist 中一整节的核心论证（"Why this works"），值得 / 必须自成一卡，否则会被压在角色定义卡的脚注里失去可被引用的位置（idea-file-abstract-vague 风险）。如果做成 provenance_delta，下游想引用"bookkeeping 概念"时无法 cite 一张独立卡。

不是 `merge_candidate`：两张卡的 statement 不可合并——一个是角色边界 known_fact，一个是有效性 concept 论证。合并会让 v2 角色边界卡的范围失控。

不是 `revise_before_gate`：draft 含完整证据链与多条引文行号，边界（大规模局限、人偶尔手写、错误模式转移）明确，可直接进入 publication_gate。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 v2 `wiki-layer-generated-markdown-directory` 做 related 互链作"角色边界（v2）↔ 为什么这个角色边界能持续运转（v3 本卡）"；与同批 `karpathy-gist-memex-connection` 互链作"为什么有效（机制）+ 历史定位（概念史）"。

## 5. 备注

- 本卡是把 gist 的 "Why this works" 段从其它 v2 卡的脚注里抢救出来——v2 这条信息其实存在于源材料但未被采纳成卡。
- "大规模下 LLM 也可能漏更新"是借用 Robin Cartier 等实践者材料的 boundary 声明，本卡未直接引该来源（避免越界），仅作 boundary note。如未来 v3 加 `robin-cartier-scale-ceiling`（同批）卡，可双向 cross-link。
