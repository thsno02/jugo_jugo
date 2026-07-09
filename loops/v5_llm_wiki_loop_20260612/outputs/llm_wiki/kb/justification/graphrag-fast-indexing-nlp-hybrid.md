# Justification: graphrag-fast-indexing-nlp-hybrid

## 提取依据
材料 docs/index/methods.md 完整描述了 FastGraphRAG 的设计理念、与 Standard 方法的对比、NLP 技术选择（NLTK/spaCy）、成本估计（图提取占 75%）、以及适用场景建议。

## 原子性判断
FastGraphRAG 是一个独立的索引方法变体，与标准 GraphRAG 索引有根本性实现差异（NLP vs LLM），值得独立成卡。

## Evidence basis
code_implementation -- 描述的是已实现的 `graphrag index --method fast` 命令背后的代码逻辑。
