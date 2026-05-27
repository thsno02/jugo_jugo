---
schema: accepted_card_provenance.v3
card: ../cards/ragchecker-claim-entailment-decomposition.md
material_id: arxiv-ragchecker
digest_id: digest_arxiv-ragchecker
source_paths:
  - data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
draft_card: ../../drafts/cards/ragchecker-claim-entailment-decomposition.md
draft_provenance: ../../drafts/provenance/ragchecker-claim-entailment-decomposition.md
similarity_result: ../../drafts/similarity/ragchecker-claim-entailment-decomposition.json
comparison_provenance: ../../drafts/comparison/ragchecker-claim-entailment-decomposition.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；claim/entailment 原语、Precision/Recall 公式、RefChecker+Llama3-70B 实现栈、meta evaluation 与 Neutral/Contradiction 限制全部回到论文章节。
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- 摘要原文（L171–176）：*"In this paper, we propose a fine-grained evaluation framework, RagChecker, that incorporates a suite of diagnostic metrics for both the retrieval and generation modules. Meta evaluation verifies that RagChecker has significantly better correlations with human judgments than other evaluation metrics."*
- 定义节（L424）：claim 分解与 entailment 关系的形式化；relevant chunk 定义（同行）。
- Overall 公式（L429–431）：Precision / Recall 的 entailment 形式。
- 实现栈（L669–670）：Llama3-70B 同时担当 extractor & checker。
- RefChecker 验证表（L213–243）：Llama3 + Llama3 在 Zero / Noisy / Accurate context 三种设定下均超过纯开源最佳基线。
- meta evaluation 结论（L758–760）：*"RagChecker has the strongest correlation with human preference in terms of three aspects."*
- 限制段（L455–462）：作者承认目前 Neutral 与 Contradiction 未分开处理。

## 卡片范围是否成立

- 这是 RAGChecker 全套指标的共同基底，单独成卡能服务多张派生指标卡，避免每张卡都重复解释"什么是 claim、什么是 entailment"。
- 直接来自源材料：claim 定义、relevant chunk 定义、Precision/Recall 公式、Llama3 extractor、meta evaluation 结论。
- 唯一引申：把 RAGChecker 与 BLEU/ROUGE/BERTScore 的"表面相似 vs 命题对账"差别放在边界段——这是论文 §Meta Evaluation 提到要用 BLEU/ROUGE/BERTScore 做对照的直接含义，不算原创。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开原语、公式、实现栈、为何值得记住、边界。
  - 知识密度：机制 + 数字 + 边界 + 与 BLEU/ROUGE 对照。
  - 源支撑：source_ids 含 arxiv-ragchecker；L424–425 / L429–431 / L669–670 / L758–760 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：7 张同 RAGChecker / Ragas / ALCE 簇姊妹卡。

## 备注

- 后续 3 张 RAGChecker 派生卡（generator 三元张力、retriever-noise 折衷、chunk-level faithfulness）共享本卡，related 字段中应当回链本卡。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ragchecker-claim-entailment-decomposition.md`
- draft provenance: `../../drafts/provenance/ragchecker-claim-entailment-decomposition.md`
- similarity: `../../drafts/similarity/ragchecker-claim-entailment-decomposition.json`
- comparison provenance: `../../drafts/comparison/ragchecker-claim-entailment-decomposition.md`
