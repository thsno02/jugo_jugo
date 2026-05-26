---
schema: comparison_provenance.v3
draft_card: ../cards/microsoft-agent-governance-eight-packages.md
draft_provenance: ../provenance/microsoft-agent-governance-eight-packages.md
similarity_result: ../similarity/microsoft-agent-governance-eight-packages.json
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
created_time: 2026-05-26T16:14:00+08:00
edited_time: 2026-05-26T16:14:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "微软 Agent Governance Toolkit 用八个包切分智能体治理面" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：微软 agent-governance-toolkit 的八包架构——Agent OS / Mesh / Runtime / SRE / Compliance / Marketplace / Lightning / Hypervisor，每个包关心一个治理面（policy / privilege rings / Merkle audit chain 等）。论据轴是 agent system governance + 包切分设计。
- 候选 1 / 2 / 3：Karpathy 推文 idea file / health checks——与 agent governance toolkit 无任何主题交叠。

draft 与候选不在同一域。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不含 agent governance / policy engine / privilege rings 任何内容 → `new_card`。draft 自带八包速览表、设计要点、ADR 列表、原文 quote，证据完整 → 不是 `revise_before_gate`。v2 无 agent governance 邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `microsoft-agent-governance-standards-alignment` 同 family related。

## 5. 备注

agent governance toolkit 主题在 v2 KB 完全缺席。
