---
schema: accepted_card_provenance.v3
card: ../cards/graphrag-manipulation-only-attack-surface.md
material_id: arxiv-graph-poisoning
digest_id: digest_arxiv-graph-poisoning
source_paths:
  - data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt
draft_card: ../../drafts/cards/graphrag-manipulation-only-attack-surface.md
draft_provenance: ../../drafts/provenance/graphrag-manipulation-only-attack-surface.md
similarity_result: ../../drafts/similarity/graphrag-manipulation-only-attack-surface.json
comparison_provenance: ../../drafts/comparison/graphrag-manipulation-only-attack-surface.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:05:00+08:00
  gate_notes: 6/6 项通过：gray-box 威胁模型 + 0.06% 词量数字 + 与 prompt injection / chunk-RAG 的边界对比锚定到 L157-230 / L284-296。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T10:05:00+08:00
edited_entity: llm
---

## 源证据

- 摘要原文（L157–166）：*"Targeting this attack surface, we propose two knowledge poisoning attacks (KPAs) and demonstrate that modifying only a few words in the source text can significantly change the constructed graph, poison the GraphRAG, and severely mislead downstream reasoning."*
- 引言原文（L197–199）：*"An unexplored question is whether GraphRAG is also vulnerable when the adversary cannot add new text, but is only able to make small, subtle modifications to the existing corpus."*
- 引言原文（L200）：*"This threat corresponds to subtle edits to trusted sources (e.g., minor changes in Wikipedia) rather than the injection of obviously malicious content."*
- 攻击模型（L284–287）：*"We consider a gray-box adversary that poisons GraphRAG by editing the source corpus rather than injecting entirely new documents or accessing model parameters."*
- 贡献列表（L226–230）：列出 TKPA / UKPA 的精度与广度边界、修改词数比例。

## 卡片范围是否成立

卡片把"manipulation-only attack surface"作为一个独立概念抽取出来，原因是：

- 论文用一整段（L196–207）把它与已有的"additive injection"系工作区分开，并以此组织后续 TKPA/UKPA 的设计动机；
- 它本身是一个可单独引用的安全立场，不依赖具体算法细节；
- 直接来自源材料的主张：modify-only 的语义、gray-box 模型、对 trusted source（Wikipedia）的威胁场景。
- 引申主张（明确标记）：与 prompt injection 的对比、与普通 chunk-RAG 的不同——这两点是结合 RAG 安全常识的推论，未直接出现在论文，但与论文立场一致。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:05:00+08:00
- 检查要点：
  - 非标题复述：以 gray-box 威胁模型三要素 + 威胁场景重定义 + 误读边界三段实质展开。
  - 知识密度：威胁模型 + 数值（0.05-0.06% / 93.1% ASR）+ 与 prompt injection / chunk-RAG 边界。
  - 源支撑：source_ids=[arxiv-graph-poisoning]；L157-166 / L197-200 / L226-230 / L284-287 多锚点。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 8 个 v3 draft id。

## 备注

- v2 卡片中暂无 GraphRAG 投毒条目；后续 comparison 阶段可与未来若出现的 "PoisonedRAG" 或 "GRAGPOISON" 卡片对照。
- TKPA / UKPA 的具体机制会拆出两张独立卡。
- Adoption 阶段观察：comparison 三个 v2 候选 jaccard 仅靠虚词「的」撞分，无 fusion 必要。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/graphrag-manipulation-only-attack-surface.md`
- draft provenance: `../../drafts/provenance/graphrag-manipulation-only-attack-surface.md`
- similarity: `../../drafts/similarity/graphrag-manipulation-only-attack-surface.json`
- comparison provenance: `../../drafts/comparison/graphrag-manipulation-only-attack-surface.md`
