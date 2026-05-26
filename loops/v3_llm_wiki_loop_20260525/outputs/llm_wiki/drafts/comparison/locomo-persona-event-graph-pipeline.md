---
schema: comparison_provenance.v3
draft_card: ../cards/locomo-persona-event-graph-pipeline.md
draft_provenance: ../provenance/locomo-persona-event-graph-pipeline.md
similarity_result: ../similarity/locomo-persona-event-graph-pipeline.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0667
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0625
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0556
---

## 1. draft 与候选为什么看起来相关

Top 1 / Top 2 / Top 3 的 jaccard 分数都在 0.06 附近，远低于 0.15 经验阈值。三张 v2 候选都属于 Karpathy gist 一类的同语料分支（idea file 抽象性、三层架构、schema 配置），共享 token 几乎只是中文虚词。没有任何 token 与 draft 关注的 LoCoMo / persona / event graph / reflect-respond 三件套相关。

## 2. draft 与候选在哪里不同

draft 描述的是 Maharana 等人 LoCoMo 数据集的**对话生成管线**：使用 `gpt-3.5-turbo` 扩写 persona、用 `text-davinci-003` 迭代生成 ≤25 个带因果连接的时间事件、复用 Park et al. (2023) 的 generative-agent reflect-respond 架构，最后人工编辑约 15% turn。论点轴是"长程一致性靠外部因果时间线 anchor 而不是模型记忆"。

v2 三张候选与之毫无重叠：`idea-file-abstract-vague` 讨论的是 Karpathy 帖文中 idea file 被有意保持抽象的设计取向；`llm-wiki-three-layer-architecture` 是 Karpathy LLM Wiki 三层划分（raw / wiki / schema）；`llm-wiki-schema-configuration-document` 描述 schema 层的配置文档角色。论文来源、研究对象、机制对象都不同。

## 3. 下一步的核心依据

(1) 与 (2) 共同表明这是一篇外部对话数据集论文，与 Karpathy LLM Wiki 的概念层根本不相交。draft 写得完整（三模块 + reflect/respond 公式 + 人工编辑比例 + 边界），无 revise 必要。结论唯一合理选项是 `new_card`。

不选 `provenance_delta`：v2 三张候选都没有"对话数据集生成"的论点要被补充。
不选 `merge_candidate`：没有任何一张 v2 卡是关于 LoCoMo / persona pipeline。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：直接进 publication_gate；本卡是后续 mem0 / LongMemEval 系列卡的基础数据集卡。

## 5. 备注

三张 top 候选都是高频"v2 token 干扰卡"，本批次中大量出现，应当被理解为 jaccard 噪声而非内容相关。
