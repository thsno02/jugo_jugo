---
schema: accepted_card_provenance.v3
card: ../cards/docs-as-code-merge-block-incentive.md
material_id: writethedocs-docs-as-code
digest_id: digest_writethedocs-docs-as-code
source_paths:
  - data/raw/webpage/writethedocs-docs-as-code/text.txt
draft_card: ../../drafts/cards/docs-as-code-merge-block-incentive.md
draft_provenance: ../../drafts/provenance/docs-as-code-merge-block-incentive.md
similarity_result: ../../drafts/similarity/docs-as-code-merge-block-incentive.json
comparison_provenance: ../../drafts/comparison/docs-as-code-merge-block-incentive.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:42:00+08:00
  gate_notes: 6/6 通过；merge-block 原句 verbatim + fresh 设计意图 + 实现要点 + 边界 + 与 LLM Wiki linting 衔接齐全，引申段已 hedge。
created_time: 2026-05-26T11:16:00+08:00
edited_time: 2026-05-27T14:42:00+08:00
edited_entity: llm
---

## 源证据

- 直接来源是单句（行 31）：
  > "You can block merging of new features if they don't include documentation, which incentivizes developers to write about features while they are fresh"

## 卡片范围是否成立

卡片把这一条源材料显式列出的"机制"展开为"为什么 fresh 重要 / 实现要点 / 边界 / 与 LLM Wiki 衔接"四节。其中"实现要点"和"与 LLM Wiki 衔接"是合理引申而非源材料原文，因此卡片正文里都用"来自社区其他演讲的归纳"、"这条规则原本针对人写文档；但同样适用于…"等描述显式标注。"merge block 被视作官僚化"的边界来自常识，而非源材料。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:42:00+08:00
- 检查要点：
  - 不是标题复述：fresh 设计意图 + 四条实现要点 + 三条边界 + 与 LLM Wiki 衔接。
  - 知识密度足够：规则 + 机制 + 反例（行数凑数）+ 边界 + 跨主题映射。
  - 源支撑齐全：原句 verbatim + 行号定位；引申段已 hedge。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，operational_rule 类型与正文一致。
  - related 已链 docs-as-code-five-pillars、enterprise-drift、wicer。

## 备注

- 与 LLM Wiki 系列卡（特别是 `llm-knowledge-base-five-stage-workflow` 的 linting 阶段，与未来 `llm-wiki-by-nvk` 的 `/wiki:lint --fix`）形成跨主题 cross-link。
- comparison 显示 v2 候选无重叠，new_card 决策合理。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/docs-as-code-merge-block-incentive.md`
- draft provenance: `../../drafts/provenance/docs-as-code-merge-block-incentive.md`
- similarity: `../../drafts/similarity/docs-as-code-merge-block-incentive.json`
- comparison provenance: `../../drafts/comparison/docs-as-code-merge-block-incentive.md`
