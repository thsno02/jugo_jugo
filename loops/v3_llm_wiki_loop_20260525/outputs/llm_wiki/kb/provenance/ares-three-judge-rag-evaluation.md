---
schema: accepted_card_provenance.v3
card: ../cards/ares-three-judge-rag-evaluation.md
material_id: arxiv-ares
digest_id: digest_arxiv-ares
source_paths:
  - data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
draft_card: ../../drafts/cards/ares-three-judge-rag-evaluation.md
draft_provenance: ../../drafts/provenance/ares-three-judge-rag-evaluation.md
similarity_result: ../../drafts/similarity/ares-three-judge-rag-evaluation.json
comparison_provenance: ../../drafts/comparison/ares-three-judge-rag-evaluation.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:28:00+08:00
  gate_notes: 6/6 通过；三判官定义 + 不共享参数机制 + KILT/SuperGLUE 跳过 A.F. 边界全部锁到原文行号。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:28:00+08:00
edited_entity: llm
---

## 源证据

- `methods.tex`（L730-734）三判官的定义：
  - `"Context Relevance: Is the passage returned relevant for answering the given query?"`
  - `"Answer Faithfulness: Is the answer generated faithful to the retrieved passage, or does it contain hallucinated or extrapolated statements beyond the passage?"`
  - `"Answer Relevance: Is the answer generated relevant given the query and retrieved passage?"`
- `methods.tex` L736-738：每个 metric 各 fine-tune 一个独立 DeBERTa 判官并加二分类头。
- `introduction.tex` L621-626：ARES 是"first automated RAG evaluation system to generate tailored LLM judges for each component of a RAG pipeline"。
- `methods.tex` L725：使用 DeBERTa-v3-Large 作为 LLM 判官的基础模型。
- `experiments.tex` L554-555：A.F. 评估在 KILT/SuperGLUE 上被跳过，因为没有 human-annotated hallucinated answers。
- `results.tex` 跨域段落（约 L895-904）：跨语言 / 跨模态时 Kendall's τ 降到 0.28–0.38。

## 卡片范围是否成立

卡片范围聚焦在"ARES 把评估拆成三个独立判官"这一机制层面。所有主张直接来自源材料：

1. 三维定义 → 直接引用论文 `methods.tex`。
2. "三段失败模式"是合理引申——源材料明确指出"ARES can evaluate each component of a RAG system separately to help improve system understanding and create targeted solutions"（`future_work_and_conclusion.tex` L588-589）。
3. 跨领域边界 → 直接来自 `results.tex` 跨域实验段。

未把 PPI、合成数据、AIS 等并入本卡，留给同前缀的姊妹卡片。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:28:00+08:00
- 检查要点：
  - 不是标题复述：三判官定义 + 故障定位机制 + 操作含义 + 跨域边界。
  - 知识密度足够：定义 + 机制（参数独立、A.F. 训练前提）+ 数字（C.R.=85.6%, A.R.=93.3%；跨域 τ=0.28–0.38）。
  - 源支撑齐全：三判官原文直接引用。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，mechanism 类型与正文一致。
  - related 已链 ARES 系列、alce、ragas、ragchecker。

## 备注

- 与 v2 卡片可能有 token 重叠的位置在"RAG 评估指标"主题。区分点：本卡聚焦"三判官独立性 + 故障定位"机制，而非具体得分。
- comparison 显示 v2 top1 仅"RAG"字面命中，决策合理。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ares-three-judge-rag-evaluation.md`
- draft provenance: `../../drafts/provenance/ares-three-judge-rag-evaluation.md`
- similarity: `../../drafts/similarity/ares-three-judge-rag-evaluation.json`
- comparison provenance: `../../drafts/comparison/ares-three-judge-rag-evaluation.md`
