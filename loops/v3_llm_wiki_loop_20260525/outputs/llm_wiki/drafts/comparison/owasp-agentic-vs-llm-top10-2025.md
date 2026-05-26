---
schema: comparison_provenance.v3
draft_card: ../cards/owasp-agentic-vs-llm-top10-2025.md
draft_provenance: ../provenance/owasp-agentic-vs-llm-top10-2025.md
similarity_result: ../similarity/owasp-agentic-vs-llm-top10-2025.json
existing_cards:
  - card_id: llm-wiki-human-llm-role-division
    card_path: llm_wiki/kb/cards/llm-wiki-human-llm-role-division.md
    score: 0.0769
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0714
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.0714
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「llm」。draft 标题的实质 token 是 OWASP / Agentic / Top / 10 / 分开列，与三张 v2 候选（Karpathy LLM-wiki 元描述）没有任何术语级重合。属于 jaccard 噪声——「llm」在两端语义指向完全不同（OWASP 安全清单针对 LLM 应用 vs Karpathy 描述 LLM 写 wiki）。

## 2. draft 与候选在哪里不同

draft 是 distinction 卡，来源 `owasp-agentic-top10-2026`，论述 OWASP Agentic Top 10 (2026) 与 LLM Top 10 (2025 / 2023-24) 在 resources 列表中并列陈列、范围限定为「plan + act + decide across workflows」三动作合一的 agentic 系统，意味着 agentic 系统风险不可被早期 LLM Top 10 完全覆盖。论点轴是「AI 安全治理框架范围划分」。

三张 v2 候选都是 Karpathy LLM-wiki 元描述。论点轴（安全治理框架 vs 个人知识库使用模式）、来源（OWASP 项目页 vs Karpathy 帖 / quote）、机制（清单陈列结构 + 范围限定语 vs 人 LLM 分工 / health check / use cases）全部不同。

## 3. 下一步的核心依据

shared_tokens 仅是「llm」一词（典型语义飘移），无实质语义重叠。v2 候选 scope 严格限于 Karpathy 来源，无法承载 OWASP 治理结构论证。draft 引文具体到 L23-26 / L51 / L90 / L96，scope 自洽（只声明并列结构与范围限定，不展开具体 10 条），证据完整。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与 sibling `owasp-agentic-top10-2026-positioning` 在 source 内互引。
