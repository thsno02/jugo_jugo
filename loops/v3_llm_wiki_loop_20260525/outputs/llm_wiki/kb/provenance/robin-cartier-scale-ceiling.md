---
schema: accepted_card_provenance.v3
card: ../cards/robin-cartier-scale-ceiling.md
material_id: robin-cartier-llm-knowledge-bases
digest_id: digest_robin-cartier-llm-knowledge-bases
source_paths:
  - data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt
draft_card: ../../drafts/cards/robin-cartier-scale-ceiling.md
draft_provenance: ../../drafts/provenance/robin-cartier-scale-ceiling.md
similarity_result: ../../drafts/similarity/robin-cartier-scale-ceiling.json
comparison_provenance: ../../drafts/comparison/robin-cartier-scale-ceiling.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；200 页 / 100K tokens、四条 limits、三档选择矩阵、强项侧均回到 L35–58。
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- 行 35–37："Strengths: reliability (no retrieval misses — the LLM reads the index directly), zero infrastructure, excellent human readability, version-controlled via git."
- 行 39–47：四条 limits，分别为规模上限 200 页 / 100K tokens、去重脆弱、时间信号弱、单用户。
- 行 49–58：场景到模式的选择矩阵（个人/操作自动化/企业级三档）。
- 行 25："Token cost per ingest: ~$2–5 for a major session (10–15 pages); linting < $1; queries negligible."（间接证明经验值来自实际运行）
- 行 89："[src-002] Robin Cartier — 'Karpathy's LLM Knowledge Base: A Practitioner's Verdict' (2026-04-08)"——给出作者归属与原文出处。

## 卡片范围是否成立

本卡聚焦"四条规模/工程局限 + 选择矩阵"这一可独立的"实践 verdict"。所有数字与限制逐字来自源页面。"未来模型上下文涨上限也涨"是合理工程引申，明确标注为 boundary。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开四条局限 + 选择矩阵 + 强项侧 + 边界。
  - 知识密度：硬约束 + 量化 + 工具选择矩阵 + 误用警示。
  - 源支撑：source_ids 含 robin-cartier-llm-knowledge-bases；四条 limits 与矩阵均 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：6 张 Karpathy / robin-cartier / anthemcreation 相邻卡。

## 备注

- 与 karpathy-gist-bookkeeping-burden 互补：那里说"维护成本→0"，本卡说"这条主张有规模边界"。
- 选择矩阵的"何时用关系型 KB 何时用 RAG"是本卡里相对独立的子主题，未来可考虑切出。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/robin-cartier-scale-ceiling.md`
- draft provenance: `../../drafts/provenance/robin-cartier-scale-ceiling.md`
- similarity: `../../drafts/similarity/robin-cartier-scale-ceiling.json`
- comparison provenance: `../../drafts/comparison/robin-cartier-scale-ceiling.md`
