---
schema: draft_card_provenance.v3
draft_card: ../cards/owasp-agentic-vs-llm-top10-2025.md
material_id: owasp-agentic-top10-2026
digest_id: digest_owasp-agentic-top10-2026
source_paths:
  - data/raw/webpage/owasp-agentic-top10-2026/text.txt
created_time: 2026-05-26T11:32:00+08:00
edited_time: 2026-05-26T11:32:00+08:00
edited_entity: llm
---

## 源证据

- `data/raw/webpage/owasp-agentic-top10-2026/text.txt` L23-26：OWASP 项目页 "RESOURCES" → "LLM TOP 10" 子菜单下并列 "LLM TOP 10 FOR 2025" 与 "LLM TOP 10 FOR 2023/24"。
- L90：主资源页另起 "OWASP Top 10 for Agentic Applications for 2026" 作为独立条目。
- L51：导航 "PROJECT INITIATIVES" 下"AGENTIC APP SECURITY"作为独立 initiative。
- L96：About 段的范围限定语 `"autonomous and agentic AI systems"`、`"plan, act, and make decisions across complex workflows"`。

## 卡片范围是否成立

卡片只做"并列结构 + 范围限定"层面的区分，没有逐条对照具体风险条目（因为源页未给）。所有主张都能在源页找到结构证据：

- "并列而非替代"——基于 resources 与 LLM Top 10 子菜单的并列陈列。
- "plan + act + decide" 三动作限定 agentic 范围——来自 About 段。
- "操作含义"段属于合理引申：把"并列结构"翻译成"先判断系统类别、再选清单、混合则两份都走"。这一引申没引入源页没有的具体条目，只是结构性建议。

## 发表门控结果

本轮未运行。

## 备注

- 因为源页内容本身稀薄，本卡和 `owasp-agentic-top10-2026-positioning` 必须严格区分：positioning 卡讲"这份清单是什么 + 谁该看"，本卡讲"它与已有 LLM Top 10 的边界"。两卡有少量重叠在"About 段引用"，但聚焦角度不同。
