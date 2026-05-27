---
schema: accepted_card_provenance.v3
card: ../cards/ragchecker-retriever-claim-vs-chunk-precision.md
material_id: arxiv-ragchecker
digest_id: digest_arxiv-ragchecker
source_paths:
  - data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
draft_card: ../../drafts/cards/ragchecker-retriever-claim-vs-chunk-precision.md
draft_provenance: ../../drafts/provenance/ragchecker-retriever-claim-vs-chunk-precision.md
similarity_result: ../../drafts/similarity/ragchecker-retriever-claim-vs-chunk-precision.json
comparison_provenance: ../../drafts/comparison/ragchecker-retriever-claim-vs-chunk-precision.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；非对称设计原因 (L884–886) verbatim，CR/CP 公式 (L432–435)，扫描 k 的 CR 61.5→77.6 与 §Limitations 反思齐全。
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- L879–886：*"Ideally, a perfect retriever returns precisely all claims needed to generate the ground-truth answer. Completeness-wise, we can measure how many claims made in the ground-truth answer are covered by retrieved chunks. With retrieved chunks as the reference text, we compute claim recall as the proportion of $\{c^{(gt)}_i | c^{(gt)}_i \in \{\text{chunk}_j\}\}$. ... a chunk-level precision provides better interpretability than a claim-level one, because in practice RAG systems usually work with documents processed to be text chunks in a fixed size. That being said, it is likely that a chunk may contain relevant claims and irrelevant or misleading information at the same time. As a result, the best possible retriever can only achieve a claim-level precision score lower than 100%, and such an upper-bound varies depending on the actual text distribution in $D$ and chunking strategy."*
- L432–435：附录 §Retriever Metrics 的两个公式 $\text{Claim Recall} = \dots$ 与 $\text{Context Precision} = \dots$。
- L456–458：*"the diagnostic metrics for the retriever component are less insightful compared to those for the generator. The retrieval metrics primarily focus on the recall of ground truth claims and precision of retrieved context, but they may not fully capture the nuances and complexities of the retrieval process."*
- L820：扫描 $k$ 5→20 时 *"claim recall 61.5→77.6 with $k$ 5→20"*；CP 的同步下降可在 `tables/ablation_k.tex` 中读出（如 BM25 + GPT-4 on RobustQA-Finance：CP 60.8→52.1）。

## 卡片范围是否成立

本卡聚焦于"RAGChecker 检索端为何 recall 用 claim-level、precision 用 chunk-level"这一**设计性**的非对称选择，以及它对工程使用的下游含义。所有定义、设计动机引文、限制 explicitly 来自论文相应段落。卡中 "CR 升 / CP 降"的双向曲线观察基于 ablation 表数字（CR 已在正文显式列出，CP 见附录表）。"为什么不能直接做调和平均"是对论文 §Overall Metrics 与 §Retriever Metrics 设计的合理推论（论文 overall F1 只用回答端 P/R，不混入 retriever P/R）。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开非对称设计、公式、设计动机、三层后果、操作含义、边界。
  - 知识密度：原语对照 + 公式 + ablation 数字 + Limitations 反思 + 与 RAGAS/TruLens 对比。
  - 源支撑：source_ids 含 arxiv-ragchecker；L884–886 / L432–435 / L456–458 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：6 张同 RAGChecker / Ragas / ALCE 簇姊妹卡。

## 备注

- 与同 material 的 `rag-chunk-level-faithfulness` 卡互锁——本卡解释为什么"chunk-level"是 evaluation schema 选择，那张解释生成器为何在 chunk 粒度上信不信。一对"原因 + 现象"。
- v2 阶段若已有 RAGAS / TruLens / ARES 的 metric 对比卡，应链接本卡补一行"RAGChecker 在 retriever 端是非对称粒度"。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ragchecker-retriever-claim-vs-chunk-precision.md`
- draft provenance: `../../drafts/provenance/ragchecker-retriever-claim-vs-chunk-precision.md`
- similarity: `../../drafts/similarity/ragchecker-retriever-claim-vs-chunk-precision.json`
- comparison provenance: `../../drafts/comparison/ragchecker-retriever-claim-vs-chunk-precision.md`
