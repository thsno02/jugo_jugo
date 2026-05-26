---
schema: comparison_provenance.v3
draft_card: ../cards/owasp-genai-landscape-2026q2.md
draft_provenance: ../provenance/owasp-genai-landscape-2026q2.md
similarity_result: ../similarity/owasp-genai-landscape-2026q2.json
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
created_time: 2026-05-26T16:15:00+08:00
edited_time: 2026-05-26T16:15:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个 top 候选与 draft "OWASP 2026 Q2 三件套：把"Top 10"扩成"防御方案地图"" **token 共享为空，score 全部 0.000**。三个候选都来自 Karpathy "llm wiki" launch 推文，是 v2 仅 15 张卡时算法的兜底排序。

## 2. draft 与候选在哪里不同

- draft 主题：OWASP 在 2026-03-17 / 04-09 集中发布三份 AI Security Solutions Landscape Q2 2026（For LLM/GenAI Apps、Agentic AI、Red Teaming），把 Top 10 扩展为防御方案地图——属于项目演化模式 / 治理 / 社区运营层面。
- 候选 1 / 2 / 3：Karpathy 推文 idea file / health checks——与 OWASP / AI 安全 landscape / 治理无任何交叠。

draft 与候选完全不在同一域。

## 3. 下一步的核心依据

(1) 无 token 共享 + (2) v2 候选 bodies 不含 OWASP / AI security landscape 任何内容 → `new_card`。draft 自带三份资源发布日期、模式分析、行号引用与 quote，证据完整 → 不是 `revise_before_gate`。v2 无 OWASP / 安全社区运营邻近卡 → 不是 `provenance_delta`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；与 `owasp-llm-top10-community-genealogy` 内部 related。

## 5. 备注

OWASP / AI 安全治理主题在 v2 KB 完全缺席。
