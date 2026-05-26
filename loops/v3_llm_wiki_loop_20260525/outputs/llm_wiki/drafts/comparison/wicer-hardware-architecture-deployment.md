---
schema: comparison_provenance.v3
draft_card: ../cards/wicer-hardware-architecture-deployment.md
draft_provenance: ../provenance/wicer-hardware-architecture-deployment.md
similarity_result: ../similarity/wicer-hardware-architecture-deployment.json
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
created_time: 2026-05-26T16:16:30+08:00
edited_time: 2026-05-26T16:16:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "WiCER 跨硬件部署画像：M4 Pro / RTX 4090 / Inferentia2" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：WiCER Appendix B 的跨硬件部署对照——M4 Pro / RTX 4090 / Inferentia2 在 cached KB QA 上的 prefill / decode / KV 量化能力 + Inferentia2 结构性不适配。论据轴是 LLM inference hardware projection + KV cache deployment。
- 候选 1 / 2 / 3：Karpathy 推文 idea file / health checks——与硬件 inference / 部署毫无关联。

draft 与候选完全不在同一域。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 完全不含 LLM inference hardware / KV cache / deployment 任何内容 → `new_card`。draft 自带三硬件画像表、bandwidth-bound vs compute-bound 解释、Inferentia2 结构性约束、原文 quote、projection vs 实测的边界标注，证据完整 → 不是 `revise_before_gate`。v2 无 LLM inference / hardware 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `wicer-fc-rag-document-count-crossover` 等同 family related。

## 5. 备注

WiCER / LLM inference hardware 主题在 v2 KB 完全缺席。
