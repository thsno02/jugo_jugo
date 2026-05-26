---
schema: draft_card_provenance.v3
draft_card: ../cards/docs-as-code-merge-block-incentive.md
material_id: writethedocs-docs-as-code
digest_id: digest_writethedocs-docs-as-code
source_paths:
  - data/raw/webpage/writethedocs-docs-as-code/text.txt
created_time: 2026-05-26T11:16:00+08:00
edited_time: 2026-05-26T11:16:00+08:00
edited_entity: llm
---

## 源证据

- 直接来源是单句（行 31）：
  > "You can block merging of new features if they don't include documentation, which incentivizes developers to write about features while they are fresh"

## 卡片范围是否成立

卡片把这一条源材料显式列出的"机制"展开为"为什么 fresh 重要 / 实现要点 / 边界 / 与 LLM Wiki 衔接"四节。其中"实现要点"和"与 LLM Wiki 衔接"是合理引申而非源材料原文，因此卡片正文里都用"来自社区其他演讲的归纳"、"这条规则原本针对人写文档；但同样适用于…"等描述显式标注。"merge block 被视作官僚化"的边界来自常识，而非源材料。

## 发表门控结果

本轮未运行。

## 备注

- 与 LLM Wiki 系列卡（特别是 `llm-knowledge-base-five-stage-workflow` 的 linting 阶段，与未来 `llm-wiki-by-nvk` 的 `/wiki:lint --fix`）形成跨主题 cross-link。
