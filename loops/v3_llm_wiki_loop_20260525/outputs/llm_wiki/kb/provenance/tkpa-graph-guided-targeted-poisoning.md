---
schema: accepted_card_provenance.v3
card: ../cards/tkpa-graph-guided-targeted-poisoning.md
material_id: arxiv-graph-poisoning
digest_id: digest_arxiv-graph-poisoning
source_paths:
  - data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt
draft_card: ../../drafts/cards/tkpa-graph-guided-targeted-poisoning.md
draft_provenance: ../../drafts/provenance/tkpa-graph-guided-targeted-poisoning.md
similarity_result: ../../drafts/similarity/tkpa-graph-guided-targeted-poisoning.json
comparison_provenance: ../../drafts/comparison/tkpa-graph-guided-targeted-poisoning.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；TKPA 四步流水线、V_score 与 C_score 公式、默认权重 (0.5,0.3,0.2)、ASR/QASD 数字均回到 L321–471 / L613–638 / L794–798。
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- §"Targeted Knowledge Poisoning Attack" 开篇（L321–328）：*"the key insight behind Targeted Knowledge Poisoning Attack (TKPA) is to treat poisoning as a network intervention problem on the knowledge graph rather than a random text-editing task."*
- 脆弱度公式（L335–340）：*"$\mathcal{V}_\mathrm{score} = \frac{(1+D_e)(1+C_e)}{\log(1+\mathrm{TLen})}$"*，分子分母含义紧随其后。
- Ego-子图段（L345–351）：*"Specifically, an ego-subgraph $G_\mathrm{ego}(v_t)$ is extracted, consisting of the target node $v_t$, its one-hop neighbors, and the edges among them."*
- Chunk 评分（L374–388）：$\mathcal{C}_\mathrm{score}$ 三项含义、默认权重 $(0.5,0.3,0.2)$。
- LLM 改写（L390–393）：*"The top-ranked chunks are rewritten by a LLM to subtly alter facts or tone while preserving fluency and style."*
- TKPA 性能表（L613–638）：LP/FC08/JAPB 三数据集 ASR、QASD 与 PRAG/NS 对照。
- Ablation（L794–798）：单信号 ASR 65.3/58.2/51.7，top-k 曲线 55.8 → 81.3 → 91.2。

## 卡片范围是否成立

- TKPA 是论文 4 大成果之一，自然成片，且包含可复用的网络干预设计思路，独立成卡比合并到"GraphRAG 安全综述"更有信息密度。
- 卡片范围严格限定在 TKPA 流水线 + 关键数字 + 默认权重；不涉及防御侧（另卡处理）和 UKPA（另卡处理）。
- 引申极少：仅一处把 TKPA 与 UKPA 的目标差异列为"边界提醒"，但该差异本就由论文 Abstract 与 §Attack Model 明示。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开 TKPA 四步流水线 + 公式 + 数字 + 边界。
  - 知识密度：机制 + 公式 + ablation 数字 + 攻击者假设 + 与 UKPA 边界。
  - 源支撑：source_ids 含 arxiv-graph-poisoning；L335–340 / L345–351 / L374–388 / L390–393 / L620–633 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：7 张同 GraphRAG / poisoning 簇姊妹卡。

## 备注

- 与 v2 暂无重叠。
- 与同批 `graphrag-manipulation-only-attack-surface` 卡共享前缀概念，但本卡是 mechanism 类型，不重复 concept 卡的威胁建模。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/tkpa-graph-guided-targeted-poisoning.md`
- draft provenance: `../../drafts/provenance/tkpa-graph-guided-targeted-poisoning.md`
- similarity: `../../drafts/similarity/tkpa-graph-guided-targeted-poisoning.json`
- comparison provenance: `../../drafts/comparison/tkpa-graph-guided-targeted-poisoning.md`
