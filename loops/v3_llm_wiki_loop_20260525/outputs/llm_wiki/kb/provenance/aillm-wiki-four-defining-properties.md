---
schema: accepted_card_provenance.v3
card: ../cards/aillm-wiki-four-defining-properties.md
material_id: aillm-wiki-directory
digest_id: digest_aillm-wiki-directory
source_paths:
  - data/raw/webpage/aillm-wiki-directory/text.txt
draft_card: ../../drafts/cards/aillm-wiki-four-defining-properties.md
draft_provenance: ../../drafts/provenance/aillm-wiki-four-defining-properties.md
similarity_result: ../../drafts/similarity/aillm-wiki-four-defining-properties.json
comparison_provenance: ../../drafts/comparison/aillm-wiki-four-defining-properties.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:00:00+08:00
  gate_notes: 6/6 项通过，四属性原文引用 + 行号齐全，边界段标注社区话术非 Karpathy 原意。
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-27T14:00:00+08:00
edited_entity: llm
---

## 源证据

- 四属性章节标题与解释（L25–39）。
- 与 RAG 对比的关键句（L26–27、L37–39）见 References 与 Footnotes。
- aillm.wiki 的非官方属性见 L130：*"Not affiliated with Anthropic or Andrej Karpathy."*

## 卡片范围是否成立

- 四属性是 aillm.wiki 首页最完整、最有结构的内容；它们既是产品话术，也是社区对 LLM Wiki 的最简定义集。把它独立成 distinction 卡有助于建立"四 lens"的引用接口。
- 直接来自源材料：四条属性的描述与原文小段。
- 引申：把每条作为"破坏即不是 LLM Wiki"的 if-then 边界——这是论文/原帖未明文给出的强主张，但属于合理外推，已在边界段标注。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:00:00+08:00
- 检查要点：
  - 正文不是标题复述，而是逐条展开四属性含义并加破坏-边界推理。
  - 知识密度足够：四属性解释 + 三条 why-it-matters + 三条边界。
  - 源支撑齐全：每条属性均有原文引用 + 行号定位。
  - References 与 Footnotes 章节均存在。
  - frontmatter 完整合法，所有必填字段非空。
  - related 已填充 v3 draft 卡 id（含 aillm-wiki-schema-as-bottleneck、enterprise-llm-wiki-four-properties 等）。

## 备注

- 与 v2 `llm-knowledge-base-five-stage-workflow` 重叠维度低：那张是 Karpathy 推文的五阶段工作流，本卡是社区目录站对 LLM Wiki 的"四属性"。后续 comparison 阶段值得交叉链接（在 related 中已链）。
- Adoption 阶段未发现新瑕疵；边界段已标注"平台自陈未经第三方验证"，无需补正。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/aillm-wiki-four-defining-properties.md`
- draft provenance: `../../drafts/provenance/aillm-wiki-four-defining-properties.md`
- similarity: `../../drafts/similarity/aillm-wiki-four-defining-properties.json`
- comparison provenance: `../../drafts/comparison/aillm-wiki-four-defining-properties.md`
