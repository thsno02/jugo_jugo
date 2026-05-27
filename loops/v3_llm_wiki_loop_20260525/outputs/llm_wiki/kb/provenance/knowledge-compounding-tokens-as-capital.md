---
schema: accepted_card_provenance.v3
card: ../cards/knowledge-compounding-tokens-as-capital.md
material_id: arxiv-knowledge-compounding
digest_id: digest_arxiv-knowledge-compounding
source_paths:
  - data/raw/arxiv/arxiv-knowledge-compounding/text.txt
draft_card: ../../drafts/cards/knowledge-compounding-tokens-as-capital.md
draft_provenance: ../../drafts/provenance/knowledge-compounding-tokens-as-capital.md
similarity_result: ../../drafts/similarity/knowledge-compounding-tokens-as-capital.json
comparison_provenance: ../../drafts/comparison/knowledge-compounding-tokens-as-capital.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:24:00+08:00
  gate_notes: 6/6 项通过：消耗品 vs 资本品归类论 + 经济决策含义 + 边界 + JEL 分类佐证。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:24:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "The theoretical contribution of this paper is a recategorization of LLM tokens from consumables to capital goods, shifting the economic discussion from static marginal cost analysis to dynamic capital accumulation."
2. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:39` —— "JEL: C63, D24, O33, L86"。
3. `data/raw/arxiv/arxiv-knowledge-compounding/text.txt:37` —— "Calibrated 30-day projections indicate cumulative savings of 53.7% under medium topic concentration and 81.3% under high concentration, with the gap widening monotonically over time."

## 卡片范围是否成立

- 卡片范围只覆盖"会计归类的概念重构"这一单一主张，是论文标题级别的"理论贡献"陈述，与源完全对齐。
- "NPV / 回本期 / 折旧曲线"是基于"资本品"框架的自然延伸；论文未直接列出这些工具，但把 token 归为 capital good 本身就蕴含这套分析语言，已在卡片中标注为引申。
- 折旧 / 长期外推作为"边界"提出，是因为论文只校准了 30 天窗口；这是合理的方法论边界声明，未越界。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:24:00+08:00
- 检查要点：
  - 非标题复述：以消耗品 vs 资本品视角对比 + 为什么区分重要 + 边界三段实质展开。
  - 知识密度：会计归类切换 + NPV/回本期/折旧引申 + 30 天校准边界。
  - 源支撑：text:37 / text:39 multiple lines + JEL D24/O33 分类佐证。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 4 个 v3 draft id。

## 备注

- 与 v2 卡片 `idea-file-as-agent-era-artifact` 在"沉淀的产物"主题上有相邻性，但论点轴不同（经济会计 vs 个人知识库）。
- 与 sibling `knowledge-compounding-dynamic-roi` / `knowledge-compounding-three-mechanisms` 是同 source 内的概念互引。
- Adoption 阶段观察：三个 v2 候选 jaccard ≤ 0.08，shared token 仅「llm」，无 fusion 必要。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/knowledge-compounding-tokens-as-capital.md`
- draft provenance: `../../drafts/provenance/knowledge-compounding-tokens-as-capital.md`
- similarity: `../../drafts/similarity/knowledge-compounding-tokens-as-capital.json`
- comparison provenance: `../../drafts/comparison/knowledge-compounding-tokens-as-capital.md`
