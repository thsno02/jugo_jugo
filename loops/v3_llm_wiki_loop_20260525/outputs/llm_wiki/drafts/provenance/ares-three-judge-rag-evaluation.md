---
schema: draft_card_provenance.v3
draft_card: ../cards/ares-three-judge-rag-evaluation.md
material_id: arxiv-ares
digest_id: digest_arxiv-ares
source_paths:
  - data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
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

本轮未运行。

## 备注

- 与 v2 卡片可能有 token 重叠的位置在"RAG 评估指标"主题。区分点：本卡聚焦"三判官独立性 + 故障定位"机制，而非具体得分。
