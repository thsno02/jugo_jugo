---
schema: comparison_provenance.v3
draft_card: ../cards/mem0-answer-generation-prompt-design.md
draft_provenance: ../provenance/mem0-answer-generation-prompt-design.md
similarity_result: ../similarity/mem0-answer-generation-prompt-design.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0588
  - card_id: llm-wiki-query-answer-writeback
    card_path: llm_wiki/kb/cards/llm-wiki-query-answer-writeback.md
    score: 0.0556
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

Top 2 `llm-wiki-query-answer-writeback` 标题中含 `answer`——和 draft 标题 "答案生成 prompt" 在"答案"语义上相邻。其他两张是 v2 高频干扰卡。Mem0 / GPT-4o-mini / prompt template / timestamp / contradictory information 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 描述 Mem0 论文附录 *Prompt Template for Results Generation* 的六条硬约束：(1) 逐 memory 扫描；(2) 时间戳优先；(3) 直接证据原则；(4) 冲突仲裁——prioritize 最新 memory；(5) 相对时间换算（"last year" → 算出绝对时间）；(6) 角色 / 用户分离。还包括答案 ≤ 5–6 词约束、Mem0g 仅多一条 graph 关系分析步骤。论点轴是"temporal J 55.51 不靠模型能力，而靠 prompt 中的时间换算 + 冲突仲裁强制指令"。

Top 2 `llm-wiki-query-answer-writeback` 描述 Karpathy gist 中 query 操作的回写流程（"LLM 搜索 wiki → 阅读 → 生成带引用答案 → 好答案归档回 wiki"），主语是 Karpathy gist 设计意图。draft 主语是 Mem0 的具体 prompt template 与 LOCOMO temporal 评测结果，与 query 回写完全不在同一论点轴。

## 3. 下一步的核心依据

虽然两边都涉及"answer"，但 v2 卡讨论的是 Karpathy gist 把 query 答案归档回 wiki 的设计倡议，draft 讨论的是 Mem0 答案生成 prompt 的六条硬约束。一个是 wiki 写回，一个是 generation prompt engineering。论点轴完全不同。结论 `new_card`。

不选 `provenance_delta`：v2 query-answer-writeback 卡的论点是设计倡议，本 draft 不会为它补充新证据。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 mem0 系列其他卡互相 cite。

## 5. 备注

`answer` 一词在两处含义不同：v2 指 query 阶段产生的回答被回写 wiki；draft 指 Mem0 在生成阶段对 LLM 的 prompt 约束。不要被字面相同误判。
