---
schema: accepted_card_provenance.v3
card: ../cards/docs-as-code-five-pillars.md
material_id: writethedocs-docs-as-code
digest_id: digest_writethedocs-docs-as-code
source_paths:
  - data/raw/webpage/writethedocs-docs-as-code/text.txt
draft_card: ../../drafts/cards/docs-as-code-five-pillars.md
draft_provenance: ../../drafts/provenance/docs-as-code-five-pillars.md
similarity_result: ../../drafts/similarity/docs-as-code-five-pillars.json
comparison_provenance: ../../drafts/comparison/docs-as-code-five-pillars.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:40:00+08:00
  gate_notes: 6/6 通过；五条支柱 verbatim + 文化引文 + 三条收益 + 三条误用边界全部锁到 writethedocs 行号。
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-27T14:40:00+08:00
edited_entity: llm
---

## 源证据

- 定义句（行 11）：
  > "Documentation as Code (Docs as Code) refers to a philosophy that you should be writing documentation with the same tools as code:"
- 五条支柱（行 13–21）：
  > "Issue Trackers / Version Control (Git) / Plain Text Markup (Markdown, reStructuredText, Asciidoc) / Code Reviews / Automated Tests"
- 文化与团队整合段（行 23）：
  > "This means following the same workflows as development teams, and being integrated in the product team. It enables a culture where writers and developers both feel ownership of documentation, and work together to make it as good as possible."
- 三条收益（行 25–31）：
  > "Writers integrate better with development teams / Developers will often write a first draft of documentation / You can block merging of new features if they don't include documentation, which incentivizes developers to write about features while they are fresh"

## 卡片范围是否成立

卡片把页面的"定义 + 五条支柱 + 收益"三部分原文直接组合成一张定义卡，没有引入页面外的资料；只在"边界与误用"段做了从五大支柱的字面延伸得到的限制（"五条都需要、不只是 Markdown"），属于忠于源材料的解读。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:40:00+08:00
- 检查要点：
  - 不是标题复述：五条支柱逐条 + 文化引文 + 三条收益 + 三条误用边界。
  - 知识密度足够：定义 + 工具栈 + 流程文化 + 反例（Markdown ≠ Docs as Code）+ 边界。
  - 源支撑齐全：每条主张锁到 writethedocs 行号。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，concept 类型与正文一致。
  - related 已链 docs-as-code-merge-block、enterprise 系列、wicer、nvk-audit。

## 备注

- 与"docs-driven development"、"AGENTS.md"、"spec-driven dev"、LLM Wiki 等卡片在主题上正交但相关，可以做后续 cross-link 候选。
- comparison 显示 v2 候选无重叠，new_card 决策合理。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/docs-as-code-five-pillars.md`
- draft provenance: `../../drafts/provenance/docs-as-code-five-pillars.md`
- similarity: `../../drafts/similarity/docs-as-code-five-pillars.json`
- comparison provenance: `../../drafts/comparison/docs-as-code-five-pillars.md`
