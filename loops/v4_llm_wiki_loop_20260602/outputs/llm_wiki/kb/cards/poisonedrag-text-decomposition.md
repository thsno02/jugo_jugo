---
id: poisonedrag-text-decomposition
title: PoisonedRAG 的 S+I 文本分解策略
status: accepted
card_type: mechanism
tags: [rag, poisoning, adversarial-text, text-decomposition, attack-method]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
justification: ../justification/poisonedrag-text-decomposition.md
canonical_concept: poisonedrag-text-decomposition
aliases: [S+I分解, S⊕I decomposition, PoisonedRAG文本拼接策略]
summary: >-
  poisonedrag-text-decomposition（S+I分解 / S⊕I decomposition）PoisonedRAG 将每条恶意文本分解为 P=S⊕I 两个子文本，I 由 LLM 生成以满足生成条件（约 2 次查询），S 在黑盒下直接用目标问题、在白盒下用对抗文本方法优化以满足检索条件，从而同时实现双条件。
related:
  - rag-retrieval-generation-dual-condition
  - rag-knowledge-corruption-attack
---

PoisonedRAG 的核心设计策略是将恶意文本 P 分解为两个不相交的子文本 S 和 I，即 P = S ⊕ I（⊕ 为文本拼接操作），分别负责满足检索条件和生成条件 [^src-1]。

**子文本 I（生成条件）**：通过提示 LLM（如 GPT-4）生成一段文本，使得该文本作为上下文时 LLM 会为目标问题 Q 输出目标答案 R。具体提示模板为："This is my question: [Q]. This is my answer: [R]. Please craft a corpus such that the answer is [R] when prompting with the question [Q]. Please limit the corpus to V words." 生成后验证答案是否正确，不正确则重试，最多 L 次。实验显示平均仅需约 2 次查询即可成功 [^src-2]。由于 LLM 的随机性（非零 temperature），相同提示可生成不同的 I，使得同一目标问题的多条恶意文本各不相同 [^src-3]。

**子文本 S（检索条件）**：
- 黑盒设定：直接令 S = Q（目标问题本身），因为 Q 与自身最相似，且不影响 I 的有效性。这一策略虽然简单但实验证明极其有效 [^src-4]。
- 白盒设定：通过对抗文本生成方法（HotFlip、TextFooler 等）优化 S，最大化 Sim(f_Q(Q), f_T(S ⊕ I))，使恶意文本与目标问题在嵌入空间中的相似度最大化 [^src-5]。白盒设定中 S 通常表现为无语义的乱序词汇（如 "chanting when? someone doing se se come out sounded"）。

在默认设定下（N=5, k=5, V=30 词），黑盒攻击在百万级文本库中可达 91-99% 的攻击成功率 [^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "our idea is to decompose the malicious text P into two disjoint sub-texts S and I, where P = S ⊕ I"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "on average, two or three queries are sufficient to generate I"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "due to the randomness of the LLM... the generated I could be different even if the prompt is the same, enabling PoisonedRAG to generate diverse malicious texts"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "our key insight is that the target question Q is most similar to itself. Moreover, Q would not influence the effectiveness of I"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "method.tex" -- "S = argmax_{S'} Sim(f_Q(Q), f_T(S' ⊕ I))"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` -- "evaluation.tex" -- "PoisonedRAG could achieve 97% (on NQ), 99% (on HotpotQA), and 91% (on MS-MARCO) ASRs for RAG with PaLM 2."
