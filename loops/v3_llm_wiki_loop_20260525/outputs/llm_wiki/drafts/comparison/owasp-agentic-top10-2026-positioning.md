---
schema: comparison_provenance.v3
draft_card: ../cards/owasp-agentic-top10-2026-positioning.md
draft_provenance: ../provenance/owasp-agentic-top10-2026-positioning.md
similarity_result: ../similarity/owasp-agentic-top10-2026-positioning.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0833
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0769
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0667
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 分数都低于 0.09，shared_tokens 仅为汉语助词「的」。draft 标题包含 OWASP / Agentic / Top / 10 / 2026 / 定位 / 受众等术语，与三张 v2 候选（全部是 Karpathy LLM-wiki 元描述）没有任何术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 source_claim 卡，来源 `owasp-agentic-top10-2026` 的官方项目页：内容包括 2025-12-09 发布、由 100+ 行业专家 peer review 的 framework 定位、面向 agentic（能 plan/act/decide）系统的范围、builders/defenders/decision-makers 三类受众、与 LLM Top 10 (2023/24/2025) 并列的关系。属于「AI 安全治理 / 风险清单」论点轴。

三张 v2 候选：top 1 是 idea file 抽象性元描述、top 2 是 LLM-wiki 三层架构、top 3 是 schema 配置文档。它们的论点轴是「LLM 维护个人知识库的模式」，与 OWASP 的「agentic 系统风险框架」毫无重叠：受众（个人知识管理者 vs 企业 builder/defender/decision-maker）、机制（wiki 写作 vs 风险清单）、来源类型（个人推文 / gist vs OWASP 项目页）全部不同。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义关联。v2 候选 scope 严格限于 Karpathy 来源，无法纳入 OWASP 元数据。draft 引文具体到 L92 / L96 / L100-118，scope 明确（只声明项目页内容，不展开 PDF 里的具体 10 条），证据完整。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- draft scope 严格自我设限「具体 10 条目内容需要通过 PDF 获取，不能仅凭这条 web 文案展开」，gate 时应保留这条边界。
