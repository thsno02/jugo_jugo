---
schema: draft_card_provenance.v3
draft_card: ../cards/owasp-agentic-top10-2026-positioning.md
material_id: owasp-agentic-top10-2026
digest_id: digest_owasp-agentic-top10-2026
source_paths:
  - data/raw/webpage/owasp-agentic-top10-2026/text.txt
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-26T11:30:00+08:00
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

- **没有**编造任何具体的 Top 10 条目名（源页未给出）。
- **没有**把 OWASP Top 10 for LLM 2025 的具体条目搬过来——那是不同来源。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 卡片可能存在的重叠：v2 若已有"agent 安全"通用卡，本卡的独特价值在于"明确给出 OWASP 2026 这份清单的定位与受众"。具体条目内容需后续 ingest PDF 后再开姊妹卡。
