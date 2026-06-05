---
schema: justification_journal.v1
card: ../cards/claim-level-entailment-evaluation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt`
源证据：
- sections/framework.tex, Fine-grained Evaluation with Claim Entailment -- "we introduce two components: 1) a text-to-claim extractor that decomposes a given text T into a set of claims {c_i}, and 2) a claim-entailment checker to determine whether a given claim c is entailed in a reference text Ref or not"
- sections/introduction.tex, metric limitation -- "typical measures such as n-gram-based (e.g., BLEU, ROUGE), embedding-based (e.g., BERTScore), and LLM-based methods perform well with concise answers but fail to detect finer distinctions in longer responses"
范围论证：声明级蕴含检验是 RAGChecker 全部指标体系的方法论基础，也是区别于此前 RAG 评估框架的核心技术贡献。该概念独立于 RAGChecker 的具体指标，是一种通用的细粒度评估范式。
