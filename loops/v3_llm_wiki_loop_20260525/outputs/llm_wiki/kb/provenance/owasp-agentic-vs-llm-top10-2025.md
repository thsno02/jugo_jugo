---
schema: accepted_card_provenance.v3
card: ../cards/owasp-agentic-vs-llm-top10-2025.md
material_id: owasp-agentic-top10-2026
digest_id: digest_owasp-agentic-top10-2026
source_paths:
  - data/raw/webpage/owasp-agentic-top10-2026/text.txt
draft_card: ../../drafts/cards/owasp-agentic-vs-llm-top10-2025.md
draft_provenance: ../../drafts/provenance/owasp-agentic-vs-llm-top10-2025.md
similarity_result: ../../drafts/similarity/owasp-agentic-vs-llm-top10-2025.json
comparison_provenance: ../../drafts/comparison/owasp-agentic-vs-llm-top10-2025.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:20:00+08:00
  gate_notes: 6/6 项通过；并列结构与范围限定语严格基于源页结构。
created_time: 2026-05-26T11:32:00+08:00
edited_time: 2026-05-27T15:20:00+08:00
edited_entity: llm
---

## 源证据

- `data/raw/webpage/owasp-agentic-top10-2026/text.txt` L23-26：OWASP 项目页 "RESOURCES" → "LLM TOP 10" 子菜单下并列 "LLM TOP 10 FOR 2025" 与 "LLM TOP 10 FOR 2023/24"。
- L90：主资源页另起 "OWASP Top 10 for Agentic Applications for 2026" 作为独立条目。
- L51：导航 "PROJECT INITIATIVES" 下"AGENTIC APP SECURITY"作为独立 initiative。
- L96：About 段的范围限定语 `"autonomous and agentic AI systems"`、`"plan, act, and make decisions across complex workflows"`。

## 卡片范围是否成立

卡片只做"并列结构 + 范围限定"层面的区分，没有逐条对照具体风险条目（因为源页未给）。所有主张都能在源页找到结构证据。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:20:00+08:00
- 检查要点：
  - distinction 卡，区分两份清单的并列关系。
  - 知识密度对应源页深度；操作含义合理引申。
  - 源支撑：L23–26 / L90 / L51 / L96 verbatim。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 5 张邻接卡。

## 备注

- 与 `owasp-agentic-top10-2026-positioning` 角度不同：positioning 讲"这份清单是什么 + 谁该看"，本卡讲"它与 LLM Top 10 的边界"。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/owasp-agentic-vs-llm-top10-2025.md`
- draft provenance: `../../drafts/provenance/owasp-agentic-vs-llm-top10-2025.md`
- similarity: `../../drafts/similarity/owasp-agentic-vs-llm-top10-2025.json`
- comparison provenance: `../../drafts/comparison/owasp-agentic-vs-llm-top10-2025.md`
