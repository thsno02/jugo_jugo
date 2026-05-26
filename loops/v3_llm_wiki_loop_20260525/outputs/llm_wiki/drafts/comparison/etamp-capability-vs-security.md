---
schema: comparison_provenance.v3
draft_card: ../cards/etamp-capability-vs-security.md
draft_provenance: ../provenance/etamp-capability-vs-security.md
similarity_result: ../similarity/etamp-capability-vs-security.json
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
created_time: 2026-05-26T16:05:30+08:00
edited_time: 2026-05-26T16:05:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft 标题"模型能力越强 ≠ 越安全：GPT-5.2 在 authority framing 下显著脆弱" **没有任何 token 共享**（`shared_tokens: []`，score 0.000）。三个候选全部源于同一条 Karpathy "llm wiki" launch 推文（`idea file` 概念与 `health checks` 段落），是 v2 全 15 张卡里"凑数"排前 3 的产物，并不构成实质邻近。

## 2. draft 与候选在哪里不同

- draft 主题：ETAMP 论文用 (Visual)WebArena 跨 6 个模型给出"capability ≠ security"的反直觉结论；论据轴是 web agent memory poisoning、ASR、authority framing、TSR scaling 关系。
- 候选 1 (`idea-file-abstract-vague`)：Karpathy 推文里关于 idea file 表述"刻意保持抽象"，纯叙述帖文。
- 候选 2 (`idea-file-share-the-idea`)：同推文对 idea file 作为分享形式的论述。
- 候选 3 (`llm-wiki-health-checks`)：LLM 对 wiki 跑健康检查清理。

draft 属于"agent security / model scaling vulnerability"域；候选属于"Karpathy llm-wiki 设计帖文"域。两者既无证据共享也无观点交叠——既不是 v2 卡的扩展，也不是同主题不同视角。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选内容确实只讲 Karpathy 推文里 idea file / health checks 概念，与 ETAMP 实验完全无关 → `new_card`。不是 `revise_before_gate`：draft 已给出三组对照证据（GPT-5.2 vs mini、vs Qwen3.5-122B、Qwen 系列内部）+ 论文原文 quote + 边界声明，证据完备。不是 `provenance_delta`：v2 没有任何 agent security / memory poisoning 卡可被反向链接。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate，作为 ETAMP 系列首批独立 adopt。

## 5. 备注

v2 KB 当前完全无 agent security / web agent vulnerability 主题；本卡所属的 ETAMP 系列预计还会再带 2–3 张相关 draft（chaos monkey、pseudo trajectory），它们之间的内部连接交由 v3 内部 related 字段处理。
