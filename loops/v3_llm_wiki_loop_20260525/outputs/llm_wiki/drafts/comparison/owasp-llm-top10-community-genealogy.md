---
schema: comparison_provenance.v3
draft_card: ../cards/owasp-llm-top10-community-genealogy.md
draft_provenance: ../provenance/owasp-llm-top10-community-genealogy.md
similarity_result: ../similarity/owasp-llm-top10-community-genealogy.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0588
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0556
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.0556
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选都是 Karpathy LLM Wiki gist 卡，共享 token 大致是 `llm` / `应用` / `社区` 这类通用词。OWASP / Top 10 / GenAI / AIBOM / Agentic AI / Threat Intelligence 等核心 token 在 v2 不出现。

## 2. draft 与候选在哪里不同

draft 描述 OWASP Top 10 for LLM Applications 的家系：2023 首版、2024-11-17 发布 2025 版、社区驱动而非机构标准；2026 年向外辐射 AI Security Landscape、AIBOM Generator、Governance Checklist、Threat Intelligence、Agentic App Security 等周边治理项目。论点轴是"在缺乏成熟法规期 OWASP 提供共享优先级坐标"以及"不能把不在当年 Top 10 视为风险已解决"。

v2 候选：top 1 是 Karpathy gist 的人/LLM 分工；top 2 是 LLM 跑 health checks 清理 wiki；top 3 是 LLM Wiki 应用场景清单。三者无任何 LLM 安全标准、社区项目家系、治理框架概念。

## 3. 下一步的核心依据

(1) (2) 共同表明无重叠。draft 完整（家系、周边、局限齐备）。结论 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；本卡建立 LLM 安全治理类入口；可与同 batch 中各类 RAG/agent 安全卡（PoisonedRAG、TKPA/UKPA、eTAMP）形成"风险清单 vs 具体攻击"的层级关系。

## 5. 备注

无。
