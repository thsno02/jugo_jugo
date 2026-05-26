---
schema: comparison_provenance.v3
draft_card: ../cards/docs-as-code-five-pillars.md
draft_provenance: ../provenance/docs-as-code-five-pillars.md
similarity_result: ../similarity/docs-as-code-five-pillars.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0833
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0769
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 分数都低于 0.09，shared_tokens 仅为「的」这一汉语助词。draft 标题主体是英文 token（docs/as/code/五条/工具/工程/栈/定义），与三张 v2 候选标题（均为 LLM Wiki 主题）没有任何实质语义 token 重叠。这是 jaccard 噪声，不是主题邻近。

## 2. draft 与候选在哪里不同

draft 来源 `writethedocs-docs-as-code`，讲 Write the Docs 社区把 Docs as Code 拆成的五条工具栈支柱：issue tracker / VCS / 纯文本标记 / code review / 自动测试，并讨论收益、误用与边界（不是所有文档都该进 git，Markdown 不等于 Docs as Code 等）。属于「软件文档工程方法」论点轴。

三张 v2 候选全部来自 Karpathy LLM-wiki gist：top 1 是 `idea file` 抽象性的元描述；top 2 是 LLM-wiki 的「原始来源 / wiki / schema」三层架构；top 3 是 schema 作为配置文档。它们的论点轴是「LLM 维护个人知识库的模式」，不是「软件团队文档工程实践」。两者论点轴、来源类型（社区方法论文章 vs 个人推文 / gist）、读者角色（工程团队 vs 个人知识管理者）都不重叠。

## 3. 下一步的核心依据

共享 token 仅是「的」，语义关联为零。draft 的来源、scope、论点都不会改写或扩充任何 v2 候选 body，也不属于同主题不同视角。draft 本身证据充分（行号引用到位），不需要 revise。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- Docs as Code 与 LLM Wiki 在「持久文档协作流程」上有抽象的间接相通处，但本批次 v2 KB 还没有相应的桥接卡片；future 可考虑在 KB 成熟后建立交叉引用。
