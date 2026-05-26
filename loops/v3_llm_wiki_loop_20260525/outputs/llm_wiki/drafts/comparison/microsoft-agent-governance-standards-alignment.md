---
schema: comparison_provenance.v3
draft_card: ../cards/microsoft-agent-governance-standards-alignment.md
draft_provenance: ../provenance/microsoft-agent-governance-standards-alignment.md
similarity_result: ../similarity/microsoft-agent-governance-standards-alignment.json
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
created_time: 2026-05-26T16:14:30+08:00
edited_time: 2026-05-26T16:14:30+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "Agent Governance Toolkit 把四份外部合规标准做成可自动核验项" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：微软 agent-governance-toolkit 对齐 OWASP Agentic AI Top 10 / NIST AI RMF 1.0 / EU AI Act / SOC 2 四份外部标准并自动导出证据。论据轴是 agent compliance + audit trail + deterministic policy。
- 候选 1 / 2 / 3：Karpathy 推文 idea file / health checks，与外部合规标准无任何关系。

draft 与候选完全不在同一域。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不含合规标准 / 审计 / policy enforcement 任何内容 → `new_card`。draft 自带四份标准对齐方式表 + ADR-0017/18/19 引用 + 原文 quote，证据完整 → 不是 `revise_before_gate`。v2 无相关合规 / 审计邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `microsoft-agent-governance-eight-packages` 内部 related。

## 5. 备注

agent compliance / governance standards 主题在 v2 KB 完全缺席。
