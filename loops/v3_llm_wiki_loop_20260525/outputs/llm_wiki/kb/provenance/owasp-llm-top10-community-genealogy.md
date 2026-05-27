---
schema: accepted_card_provenance.v3
card: ../cards/owasp-llm-top10-community-genealogy.md
material_id: owasp-llm-top10-2025
digest_id: digest_owasp-llm-top10-2025
source_paths:
  - data/raw/webpage/owasp-llm-top10-2025/text.txt
draft_card: ../../drafts/cards/owasp-llm-top10-community-genealogy.md
draft_provenance: ../../drafts/provenance/owasp-llm-top10-community-genealogy.md
similarity_result: ../../drafts/similarity/owasp-llm-top10-community-genealogy.json
comparison_provenance: ../../drafts/comparison/owasp-llm-top10-community-genealogy.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:24:00+08:00
  gate_notes: 6/6 项通过；起源 + 周边项目矩阵都来自源页结构。
created_time: 2026-05-26T11:35:00+08:00
edited_time: 2026-05-27T15:24:00+08:00
edited_entity: llm
---

## 源证据

- 发布信息（L90–92）：*"OWASP Top 10 for LLM Applications 2025 — November 17, 2024"*。
- 项目定位（L96）：*"The OWASP Top 10 for Large Language Model Applications started in 2023 as a community-driven effort to highlight and address security issues specific to AI applications."*
- 风险扩张句（L96）：*"As LLMs are embedded more deeply in everything from customer interactions to internal operations, developers and security professionals are discovering new vulnerabilities—and ways to counter them."*
- 周边项目（L42–58）：列出 AI Security Landscape、AIBOM Generator、Governance Checklist、Threat Intelligence、Agentic App Security、Secure AI Adoption、AI Red Teaming、Data Security。
- Landscape 系列（L100–118）：2026 年 3–4 月发布的三份资源。
- 许可（L156–158）：CC BY-SA 4.0。

## 卡片范围是否成立

- 源材料文本极薄（约 2KB，大部分是导航），唯一可抽取的有效知识是 Top 10 的"社区议题列表"定位 + 周边项目矩阵 + 版本治理含义。
- 直接来自源材料：2023 起源、2025 版发布日期、社区驱动属性、周边项目命名、Landscape 资源、CC BY-SA 4.0。
- 引申：Top 10 与"审计合规标准"的差别已在边界段标注。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:24:00+08:00
- 检查要点：
  - 起源 / 周边项目 / 局限三节，substantive。
  - 知识密度对应源页深度；非标题复述。
  - 源支撑：L90–96 / L42–58 / L100–118 verbatim。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 6 张邻接卡。

## 备注

- 单一来源、文本量少；如未来需要拆 Top 10 具体十项的卡，应从 PDF 全文取材。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/owasp-llm-top10-community-genealogy.md`
- draft provenance: `../../drafts/provenance/owasp-llm-top10-community-genealogy.md`
- similarity: `../../drafts/similarity/owasp-llm-top10-community-genealogy.json`
- comparison provenance: `../../drafts/comparison/owasp-llm-top10-community-genealogy.md`
