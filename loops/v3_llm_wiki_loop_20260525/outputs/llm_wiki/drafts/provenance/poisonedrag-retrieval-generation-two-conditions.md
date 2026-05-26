---
schema: draft_card_provenance.v3
draft_card: ../cards/poisonedrag-retrieval-generation-two-conditions.md
material_id: arxiv-poisonedrag
digest_id: digest_arxiv-poisonedrag
source_paths:
  - data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-26T11:25:00+08:00
edited_entity: llm
---

## 源证据

- 两条件推导（`method.tex` 第 1768–1777 行）：
  > "To craft a malicious text P that could lead to an effective attack for a target question Q, we need to achieve two conditions, namely retrieval condition and generation condition ... To ensure P is retrieved for Q, the embedding vectors produced by a retriever for the malicious text P and the target question Q should be similar ... the LLM should generate the target answer R when P alone is used as the context for the target question Q."。
- S/I 拆分动机与黑盒/白盒解法（第 1785–1856 行）：
  > "the key challenge in crafting P to simultaneously achieve the two conditions is that they could be conflicted in certain cases ... our idea is to decompose the malicious text P into two disjoint sub-texts S and I, where P = S ⊕ I ... we first craft I such that it could achieve the generation condition ... In Black-box setting ... we propose to set S = Q, i.e., P = Q ⊕ I ... For White-box setting ... S = argmax_{S'} Sim(f_Q(Q), f_T(S' ⊕ I))"。
- I 段生成 prompt 与重试上限（第 1802–1807 行）：
  > "This is my question: [question]. This is my answer: [answer]. Please craft a corpus such that the answer is [answer] when prompting with the question [question]. Please limit the corpus to V words. ... If the generated answer is not R, we regenerate I until success or a maximum number of (say L) trials have been reached ... on average, two or three queries are sufficient to generate I."。
- 变体 ablation Table 6（第 185–201 行）：
  > "S⊕I ASR 0.97 / S alone ASR 0.03 / I alone ASR 0.69 ... NQ Black-Box"，证明两段都不能单独胜任。
- top-k 内恶意数量 Table 9（第 241–254 行）：
  > "NQ Black-Box 1→0.48, 2→0.76, 3→0.84, 4→0.90, 5→1.00"。
- 非目标问题影响（`relatedwork.tex` 第 2076–2077 行）：
  > "the fractions of non-target questions influenced by malicious texts are 0.3% and 0.9% in black-box and white-box settings, respectively. Additionally, the fractions of non-target answers ... are affected ... is 0% and 0.4%."。

## 卡片范围是否成立

这张卡承担的是 PoisonedRAG 算法的"核心机制"——两条件 + S/I 拆解。所有论断（retrieval condition / generation condition / S=Q / 白盒优化 / 重试 L 次 / 变体单独无效 / parametric bias / 非目标低附带）都直接来自 §3 与附录的对应表格，没有引申到论文外。卡内三条机制含义是对实验结果的直接读取（白盒 vs 黑盒 ASR 几乎打平、白盒 PPL 易检测、I 段自带正确答案触发 parametric bias），不属于额外推断。

## 发表门控结果

本轮未运行。

## 备注

可与 `wicer-fc-rag-document-count-crossover` 形成对照：那张卡讲 RAG 在大规模上的"性能优势"，本卡讲 RAG 同一处架构上的"安全劣势"。预计 `new_card`。v2 现有卡无相关安全攻击主题。
