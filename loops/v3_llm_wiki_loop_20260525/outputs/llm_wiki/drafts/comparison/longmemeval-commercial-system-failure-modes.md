---
schema: comparison_provenance.v3
draft_card: ../cards/longmemeval-commercial-system-failure-modes.md
draft_provenance: ../provenance/longmemeval-commercial-system-failure-modes.md
similarity_result: ../similarity/longmemeval-commercial-system-failure-modes.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0588
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0588
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选分数 0.056–0.059。Top 2 `llm-wiki-persistent-wiki-alternative-mode` 看似与 "long-term memory" 有概念邻近——都涉及"在用户与原始来源之间积累知识"。但其论点是 Karpathy 对 RAG 模式的批判，不是 commercial memory system 的实测失败模式。LongMemEval / ChatGPT / Coze / IE / MR / KU / TR 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 描述 LongMemEval §3.4 pilot study：97 道题对比 ChatGPT 与 Coze——两者比 offline reading 掉 30–64%。ChatGPT 失败模式是 KU（覆盖式压缩，把"用户车型"覆盖成"喜欢电动车"）；Coze 失败模式是 IE（拒绝间接表达，"帮我查车保险" → 漏抽"我有车"）。同节还测长上下文 LLM 直读 115K token 也掉 30–60%。论点轴是"存了 user fact ≠ 长期记忆能力"。

v2 三张候选：top 1 idea file 抽象性；top 2 持久 wiki 替代模式（Karpathy 的设计倡议）；top 3 LLM Wiki 作为模式文件。三者都是 Karpathy LLM Wiki 概念层的设计意图描述，不涉及任何商业系统实测。

## 3. 下一步的核心依据

虽然 top 2 与 draft 在"持久知识维护"层面有抽象主题相邻，但 v2 卡讨论的是 Karpathy 的设计倡议，draft 讨论的是商业 memory system 在新 benchmark 上的实测失败——前者是 vision，后者是 empirical evaluation。论点轴、来源类型、能否定/肯定都不重叠。结论 `new_card`。

不选 `provenance_delta`：本 draft 无法直接作为 Karpathy 持久 wiki 卡的反向证据（draft 不直接评测 Karpathy 系统）。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；将本卡纳入 LongMemEval 系列簇与 mem0 baseline 系列簇互相 cite。

## 5. 备注

top 2 `llm-wiki-persistent-wiki-alternative-mode` 是少数与"长期记忆"概念有共鸣的 v2 卡——其与本 draft 的关系是抽象上"问题—证据"的反向呼应，但不是"同一张卡"。
