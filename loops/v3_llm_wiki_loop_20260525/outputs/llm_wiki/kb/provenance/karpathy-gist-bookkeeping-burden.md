---
schema: accepted_card_provenance.v3
card: ../cards/karpathy-gist-bookkeeping-burden.md
material_id: karpathy-gist-llm-wiki
digest_id: digest_karpathy-gist-llm-wiki
source_paths:
  - data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
draft_card: ../../drafts/cards/karpathy-gist-bookkeeping-burden.md
draft_provenance: ../../drafts/provenance/karpathy-gist-bookkeeping-burden.md
similarity_result: ../../drafts/similarity/karpathy-gist-bookkeeping-burden.json
comparison_provenance: ../../drafts/comparison/karpathy-gist-bookkeeping-burden.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:13:00+08:00
  gate_notes: 6/6 项通过：核心主张原文 + 维护负担超线性论证 + 人侧分工 + 边界，证据锚 gist 行 37/41/64-70。
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-27T10:13:00+08:00
edited_entity: llm
---

## 源证据

- 行 66（"Why this works" 完整段）："The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. ... Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."
- 行 68："The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."
- 行 37："A single source might touch 10-15 wiki pages."
- 行 41：lint 段定义 LLM 周期性健康检查的具体维度——contradictions、stale claims、orphans、missing cross-references、data gaps。

## 卡片范围是否成立

本卡聚焦"维护成本是真瓶颈、LLM 把它降到零"这一论证。Karpathy 在 gist 中有完整逐字表述。"人侧分工"也来自原文。"维护负担超线性增长、新内容价值 sub-linear"是把原文"grows faster than the value"做简单数学化的解释，属于合理改写。"大规模下 LLM 也可能漏更新"是 Robin Cartier 等实践者已经在另一个材料里写过的边界（本卡用作 boundary note），未直接引用其他材料的具体来源。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:13:00+08:00
- 检查要点：
  - 非标题复述：以"核心主张 + LLM 改变了什么 + 可操作含义 + 边界"四段实质展开。
  - 知识密度：定量类的"10-15 页 / 维护超线性 / 价值 sub-linear" + 操作分工。
  - 源支撑：gist 行 37 / 41 / 64-70 / 68 多锚点。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 6 个 v3 draft id。

## 备注

- 与 v3 已有 idea-file-as-agent-era-artifact 主题相邻但视角不同：那张卡是"idea file as artifact"，本卡是"为什么这种模式能持续运转"。
- 在 Robin Cartier 来源中提到的"~200 页天花板"将另起一卡，本卡不展开。
- Adoption 阶段观察：comparison 与 v2 `wiki-layer-generated-markdown-directory` 同源不同段，不可 provenance_delta（合并会让 v2 角色边界卡范围失控）。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/karpathy-gist-bookkeeping-burden.md`
- draft provenance: `../../drafts/provenance/karpathy-gist-bookkeeping-burden.md`
- similarity: `../../drafts/similarity/karpathy-gist-bookkeeping-burden.json`
- comparison provenance: `../../drafts/comparison/karpathy-gist-bookkeeping-burden.md`
