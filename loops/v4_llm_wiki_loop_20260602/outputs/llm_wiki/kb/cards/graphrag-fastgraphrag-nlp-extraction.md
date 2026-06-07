---
id: graphrag-fastgraphrag-nlp-extraction
title: FastGraphRAG 基于 NLP 的低成本图提取方法
status: accepted
card_type: mechanism
tags: [graphrag, fastgraphrag, nlp, nltk, spacy, cost-optimization, implementation]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
justification: ../justification/graphrag-fastgraphrag-nlp-extraction.md
canonical_concept: graphrag-fastgraphrag-nlp-extraction
aliases: [FastGraphRAG, NLP 图提取, 快速图索引, graphrag fast method]
summary: >-
  graphrag-fastgraphrag-nlp-extraction（FastGraphRAG）用 NLP 方法替代 LLM 进行图提取：实体为 NLTK/spaCy 提取的名词短语（无描述），关系为实体对在 text unit 中的共现（无描述），省去实体/关系摘要步骤，社区报告基于直接 text unit 文本生成——图提取成本约为标准方法的 25%
related: [graphrag-indexing-pipeline-six-phases, graphrag-self-reflection-gleaning, graphrag-cli-settings-yaml-config]
---

FastGraphRAG 是 GraphRAG 提供的一种混合索引方法（`graphrag index --method fast`），用传统 NLP 替代 LLM 执行图提取中最昂贵的部分 [^src-1]。

**标准方法 vs FastGraphRAG 对比**：

| 步骤 | Standard（LLM） | Fast（NLP） |
|------|-----------------|-------------|
| 实体提取 | LLM 提取命名实体 + 描述 | 名词短语提取，无描述 |
| 关系提取 | LLM 描述实体对关系 | text unit 共现定义关系，无描述 |
| 实体摘要 | LLM 合并多描述 | 不需要 |
| 关系摘要 | LLM 合并多描述 | 不需要 |
| Claim 提取 | 可选 LLM 提取 | 跳过 |
| 社区报告 | 基于实体/关系描述 | 基于直接 text unit 内容 |

**NLP 提取选项**（`extract_graph_nlp` 配置）[^src-2]：
- `regex_english`（默认）：NLTK + 正则表达式名词短语提取，极快但主要适用于英语
- `syntactic_parser`：使用 spaCy 句法分析（默认模型 `en_core_web_md`）
- `cfg`：使用 spaCy 上下文无关文法（支持自定义 `noun_phrase_grammars`）

FastGraphRAG 通常配合更小的 chunk size（50-100 tokens）使用，以产生更好的共现图 [^src-3]。

**成本分析**：标准方法中图提取约占索引总成本的 75%，FastGraphRAG 因省去这部分 LLM 调用而大幅降低成本 [^src-4]。

**权衡**：提取的图更嘈杂，实体缺乏语义描述，不适合直接图探索。但如果用例主要面向 Global Search 的摘要问题，FastGraphRAG 能以远低于标准方法的成本提供高质量的摘要结果 [^src-5]。

## Footnotes

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/methods.md -- "FastGraphRAG is a method that substitutes some of the language model reasoning for traditional natural language processing (NLP) methods"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/yaml.md -- "extract_graph_nlp: extractor_type regex_english|syntactic_parser|cfg, model_name, max_word_length, include_named_entities"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/methods.md -- "we also generally configure the text chunking to produce much smaller chunks (50-100 tokens). This results in a better co-occurrence graph"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/methods.md -- "We estimate graph extraction to constitute roughly 75% of indexing cost. FastGraphRAG is therefore much cheaper"
[^src-5]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/methods.md -- "the extracted graph is less directly relevant for use outside of GraphRAG, and the graph tends to be quite a bit noisier"
