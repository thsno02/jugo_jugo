---
schema: comparison_provenance.v3
draft_card: ../cards/mem0-baseline-failure-modes.md
draft_provenance: ../provenance/mem0-baseline-failure-modes.md
similarity_result: ../similarity/mem0-baseline-failure-modes.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0625
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0625
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.0588
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选分数 0.058–0.062，token 共享停留在中文虚词。`llm-wiki-persistent-wiki-alternative-mode` 因为标题中含 "持久" 可能与 draft 中"长期 / 持久化" 这类词碰巧重叠，但论点轴完全不同。LangMem / Zep / A-Mem / OpenAI ChatGPT memory / Full-context 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 分别列出 Mem0 论文里 5 个 baseline 的失败模式：LangMem（搜索延迟 p95 59.82s，论文判定 impractical）；Zep（token 600k 通胀、异步图构建延迟数小时）；OpenAI（时间戳丢失，temporal J 21.71）；A-Mem（重跑 J 49.91，LLM-judge 削减 F1 优势）；Full-context（J 72.90 但 p95 17.117s）。论点轴是"五种失败模式各异，必须分别防御"。

v2 三张候选：top 1 idea file 抽象性；top 2 持久 wiki 替代模式（Karpathy gist 关于 wiki 不是 ephemeral 而是持续累积知识的设计）；top 3 LLM Wiki 作为模式文件。三者都属于 Karpathy gist 概念层，无 baseline 评估、latency 数字、token 通胀等论点。

特别地，top 2 `llm-wiki-persistent-wiki-alternative-mode` 表面看似与 memory system 主题相关，但实质是 Karpathy 对 RAG-style 文档问答的对照设计描述，不涉及任何 memory baseline 的实测数字。

## 3. 下一步的核心依据

(1) (2) 共同表明 v2 无 mem0 baseline 评估卡。draft 完整。结论 `new_card`。

不选 `provenance_delta`：Karpathy 持久 wiki 卡的论点是设计倡议，本 draft 是对实际 baseline 的失败模式总结，不是为前者补充证据。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 `mem0-locomo-benchmark-evaluation`、`mem0-rag-chunk-size-ablation`、`mem0-answer-generation-prompt-design` 形成 mem0 系列簇。

## 5. 备注

top 2 `llm-wiki-persistent-wiki-alternative-mode` 是少数有"持久 memory"语义共鸣的 v2 卡，但只是 Karpathy 的设计倡议，未涉及 baseline 评估；不应被误判为同主题。
