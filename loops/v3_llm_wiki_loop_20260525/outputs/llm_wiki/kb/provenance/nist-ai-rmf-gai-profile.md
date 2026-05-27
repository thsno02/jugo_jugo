---
schema: accepted_card_provenance.v3
card: ../cards/nist-ai-rmf-gai-profile.md
material_id: nist-gai-profile
digest_id: digest_nist-gai-profile
source_paths:
  - data/raw/webpage/nist-gai-profile/text.txt
draft_card: ../../drafts/cards/nist-ai-rmf-gai-profile.md
draft_provenance: ../../drafts/provenance/nist-ai-rmf-gai-profile.md
similarity_result: ../../drafts/similarity/nist-ai-rmf-gai-profile.json
comparison_provenance: ../../drafts/comparison/nist-ai-rmf-gai-profile.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T15:08:00+08:00
  gate_notes: 6/6 项通过；定位与元数据来自索引页 verbatim；边界明确说明 PDF 未读。
created_time: 2026-05-26T14:55:00+08:00
edited_time: 2026-05-27T15:08:00+08:00
edited_entity: llm
---

## 源证据

- 第 208 行：标题 `Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile`。
- 第 210-212 行：Published `July 26, 2024`。
- 第 216 行：作者列表（Autio, Schwartz, Dunietz, Jain, Stanley, Tabassi, Hall, Roberts）。
- 第 219 行：完整 abstract（cross-sectoral profile / EO 14110 / voluntary use 等定位）。
- 第 223-235 行：Citation `NIST Trustworthy and Responsible AI - 600-1` / Report Number `600-1` / DOI `https://doi.org/10.6028/NIST.AI.600-1`。
- 第 241 行：Keywords（AI / RMF / Generative AI / GAI Risk 等）。

## 卡片范围是否成立

- 文档定位（companion profile / EO 14110 / voluntary use / RMF 1.0 在 2023-01 发布）全部出自 abstract，无引申。
- "PDF 内容未读，控制项要去 600-1 全文找"是合理边界——本批次源文件仅含索引页文本，未含 PDF 全文。
- 与"欧盟 AI Act"对比是一个边界提示，未做实际对照（避免越界）。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T15:08:00+08:00
- 检查要点：
  - 这是 source_claim 卡，给出 NIST AI 600-1 的定位 + 注意事项，非标题复述。
  - 知识密度对应索引页内容深度（abstract 级别）；卡内已显式声明 PDF 未读以避免越界。
  - 源支撑：6 处 verbatim 行号引用。
  - References + Footnotes 双在；Footnotes 3 条 verbatim。
  - frontmatter 完整；related 含 5 张邻接卡。

## 备注

- 索引页内容有限，目前只够 1 张卡。若后续抓取 PDF 全文（NIST.AI.600-1），可以再拆"风险类目"、"控制项映射"等卡。
- adoption 阶段无修订。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/nist-ai-rmf-gai-profile.md`
- draft provenance: `../../drafts/provenance/nist-ai-rmf-gai-profile.md`
- similarity: `../../drafts/similarity/nist-ai-rmf-gai-profile.json`
- comparison provenance: `../../drafts/comparison/nist-ai-rmf-gai-profile.md`
