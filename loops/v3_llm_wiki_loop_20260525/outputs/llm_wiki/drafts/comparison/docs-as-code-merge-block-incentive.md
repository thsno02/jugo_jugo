---
schema: comparison_provenance.v3
draft_card: ../cards/docs-as-code-merge-block-incentive.md
draft_provenance: ../provenance/docs-as-code-merge-block-incentive.md
similarity_result: ../similarity/docs-as-code-merge-block-incentive.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1579
  - card_id: rag-document-qa-does-not-accumulate-synthesized-knowledge
    card_path: llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md
    score: 0.0952
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T12:24:00+08:00
edited_time: 2026-05-26T12:24:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top1 `schema-configuration-document` jaccard 0.1579 共享 `文档`/`是`/`的`——`文档` 在 draft 是"docs"对应词，在 v2 是"配置文档"，语义无关。top2 `rag-document-qa-...` 共享 `不`/`文档`——同样是表面 token。top3 `idea-file-abstract-vague` 0.0556 只共享 `的`。属于典型低分批 + 误中。draft 标题中的核心 token `docs`、`code`、`ci`、`合并`、`激励机制` 在 v2 候选标题中都没出现。

## 2. draft 与候选在哪里不同

- **领域不同**：本 draft 取自 `writethedocs-docs-as-code`（技术写作社区 Write the Docs 关于 Docs as Code 实践的资料），与 LLM Wiki / RAG / 个人知识库领域不同。
- **类型不同**：本 draft 是 operational_rule（CI 规则）：检测到 PR 改了功能代码但没改文档时阻止 merge；展开了 "为什么 fresh 关键"（文档腐烂高峰 1–4 周）、实现要点（规则分级、修复指引、与 review/issue tracker 支柱配合）、边界（终端用户文档不适用、行数检测会让人凑数）、与 LLM 写作器衔接（CI 检测 raw vs wiki 对应、与 karpathy linting / `wiki:lint --fix` 同源）。
- top1 `schema-configuration-document` 谈 karpathy schema 角色，与 PR CI 阻止机制无关。
- top2 `rag-document-qa-...` 谈 RAG 不积累综合知识，与 CI 激励无关。
- top3 `idea-file-abstract-vague` 谈 idea file 抽象性，无关。
- 关键论点（"在 PR 时刻 fresh 强制写"作为防止文档腐烂的硬约束）在 v2 完全没有；这也是 docs-as-code 五支柱实践（issue tracker / version control / plain text / review / CI）中的 CI 支柱。

## 3. 下一步的核心依据

(1) 三张候选完全不覆盖 docs-as-code 领域；(2) draft 来自一个 v2 KB 完全未涉的新领域（技术写作社区）；(3) operational_rule 类卡天然以"规则 + 触发条件 + 修复 + 边界"组织，与 v2 已有的 known_fact 概念卡不可合并。结论是 `new_card`。

不是 `provenance_delta`：本 draft 不是给 v2 任一卡补证据——领域、类型、论点轴全无对应。不是 `merge_candidate`：v2 没有 CI / docs-as-code / merge-block 任何相关卡可合并。不是 `revise_before_gate`：draft 已显式标注哪些段是"来自社区其他演讲的归纳"（非源材料原文）、哪些是 boundary 声明（终端用户文档不适用、Docs as Code 不完整团队下易官僚化），可直接进入 publication_gate。
不是 `duplicate_skip`：v2 完全没有同主题卡。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引加入 `writethedocs-docs-as-code`；与 `llm-knowledge-base-five-stage-workflow` 的 linting 阶段、`nvk-llm-wiki-audit-and-librarian` 的 `/wiki:lint --fix` 做 related cross-link 形成"Docs as Code → LLM Wiki 健康检查"主题链。

## 5. 备注

- 本卡是 v3 第一张 docs-as-code 主题卡，建议同时建立"Docs as Code"标签或主题页。
- "把 docs as code 与 LLM 写作器衔接"那一段是合理引申，编辑/审稿可视情况保留或拆出独立卡——本卡决策仍是 new_card。
