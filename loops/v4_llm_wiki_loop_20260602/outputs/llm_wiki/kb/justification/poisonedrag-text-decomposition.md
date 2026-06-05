---
schema: justification_journal.v1
card: ../cards/poisonedrag-text-decomposition.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt`
源证据：
- method.tex — "our idea is to decompose the malicious text P into two disjoint sub-texts S and I, where P = S ⊕ I"
- method.tex — "we propose to set S=Q, i.e., P=Q ⊕ I"
- method.tex — "S = argmax_{S'} Sim(f_Q(Q), f_T(S' ⊕ I))"
- evaluation.tex — "on average, PoisonedRAG only needs to make around 2 queries to the GPT-4 to craft each malicious text"
范围论证：S⊕I 分解是 PoisonedRAG 的具体实现机制，将双条件框架落地为可操作的攻击算法。它独立于双条件的理论推导（后者是 why，此卡片是 how），构成独立的原子机制知识。
