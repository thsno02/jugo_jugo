---
schema: justification_journal.v1
card: ../cards/rag-knowledge-corruption-attack.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt`
源证据：
- abstract.tex — "we propose PoisonedRAG, the first knowledge corruption attack to RAG"
- evaluation.tex — "PoisonedRAG could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) ASRs"
- evaluation.tex — "PoisonedRAG could achieve high ASRs on 3 datasets under 8 different LLMs"
- evaluation.tex — "on average, PoisonedRAG only needs to make around 2 queries to the GPT-4"
- introduction.tex — "an attacker could mislead the LLM to generate misinformation... commercial biased answers"
范围论证：此卡片作为对 PoisonedRAG 攻击方法的整体概述性概念卡片，记录其定义、效果、效率和威胁场景。与具体机制卡片（双条件、S+I 分解）互补但不重叠，聚焦于"是什么"和"效果如何"层面。
