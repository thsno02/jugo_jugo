---
schema: accepted_card_provenance.v3
card: ../cards/owasp-agentic-top10-2026-positioning.md
material_id: owasp-agentic-top10-2026
digest_id: digest_owasp-agentic-top10-2026
source_paths:
  - data/raw/webpage/owasp-agentic-top10-2026/text.txt
draft_card: ../../drafts/cards/owasp-agentic-top10-2026-positioning.md
draft_provenance: ../../drafts/provenance/owasp-agentic-top10-2026-positioning.md
similarity_result: ../../drafts/similarity/owasp-agentic-top10-2026-positioning.json
comparison_provenance: ../../drafts/comparison/owasp-agentic-top10-2026-positioning.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:18:00+08:00
  gate_notes: 6/6 项通过；定位描述严格限于源页可支撑事实，明确不编造 PDF 条目。
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-27T15:18:00+08:00
edited_entity: llm
---

## 源证据

- `data/raw/webpage/owasp-agentic-top10-2026/text.txt` L90-98 "About" 段，源页对项目的官方描述：
  - `"globally peer-reviewed framework that identifies the most critical security risks facing autonomous and agentic AI systems"`
  - `"Developed through extensive collaboration with more than 100 industry experts, researchers, and practitioners"`
  - `"distilling a broad ecosystem of OWASP GenAI Security guidance into an accessible, operational format"`
  - `"equips builders, defenders, and decision-makers with a clear starting point"`
- L92：发布日期 `December 9, 2025`。
- L24-26：项目页同时列出 LLM Top 10 for 2025 与 2023/24 两份并列资源。
- L98 + L99：源页只提供 "Download" 入口，正文未列出具体 10 条目内容。

## 卡片范围是否成立

源页本身内容稀疏（约 2KB，且大部分是导航文本），实质内容集中在 "About" 段一段话。卡片只覆盖该段能直接支撑的事实：

- 定位（peer-reviewed framework / agentic）。
- 过程（100+ 专家）。
- 作用层（distill 既有 OWASP 指南）。
- 受众三类。
- "源页未给具体条目、必须下载 PDF"——这是基于源页结构的事实，不是引申。

未做引申：

- **没有**编造任何具体的 Top 10 条目名。
- **没有**把 OWASP Top 10 for LLM 2025 的具体条目搬过来——那是不同来源。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:18:00+08:00
- 检查要点：
  - 范围 / 过程 / 作用层 / 受众 / 配套位置 + 操作含义，严守源页范围。
  - 知识密度对应源页深度（页面本身稀疏）；卡片显式告诉读者要去下载 PDF 才能看条目。
  - 源支撑：L90–98 verbatim。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 6 张邻接卡。

## 备注

- 具体条目内容需后续 ingest PDF 后再开姊妹卡。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/owasp-agentic-top10-2026-positioning.md`
- draft provenance: `../../drafts/provenance/owasp-agentic-top10-2026-positioning.md`
- similarity: `../../drafts/similarity/owasp-agentic-top10-2026-positioning.json`
- comparison provenance: `../../drafts/comparison/owasp-agentic-top10-2026-positioning.md`
