---
id: poisonedrag-retrieval-generation-two-conditions
title: PoisonedRAG 把"投毒文本"拆成检索条件+生成条件两段
status: accepted
card_type: mechanism
tags: [#rag, #attack, #knowledge-corruption, #poisonedrag]
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-28T15:22:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
provenance_card: ../provenance/poisonedrag-retrieval-generation-two-conditions.md
aliases: [PoisonedRAG 双条件, retrieval condition + generation condition, S + I 拆解]
related: [poisonedrag-knowledge-database-attack-surface, poisonedrag-baselines-isolate-two-conditions, poisonedrag-existing-defenses-insufficient, poisonedrag-survives-advanced-rag-and-agents, etamp-attack-payload-structure, tkpa-graph-guided-targeted-poisoning, ragas-faithfulness-metric]
---

PoisonedRAG（Zou 等，PSU + IIT）想做的事：往 RAG 的 knowledge database 里塞少量恶意文本，让 LLM 对**特定目标问题** Q 输出**攻击者指定**的目标答案 R。难点在于：一段单一文本同时要满足"被检索回来"和"误导生成"这两件事，而这两件事在直觉上互相矛盾——文本越像 Q，越容易被检索回来，但也越不像"答案的证据"，未必能改变模型答案。

论文把"恶意文本 P"形式化为两个**必要条件**[^src1]：

- **Retrieval condition**：retriever 在 D ∪ Γ 上检索 Q 的 top-k 时必须包含 P（即 embedding(Q) 与 embedding(P) 足够相似）；
- **Generation condition**：当 P 单独作为 context 给 LLM 回答 Q 时，模型就该吐出 R——这样把 P 和其他干扰文本拼在一起时，R 仍然有较高生成概率。

这种"把攻击载荷拆成多段、分头担责"的结构，与 eTAMP 把 payload 拆成 Importance Signal + Trigger Condition + Attack Goal 三段[^v3-1]、以及 TKPA 把改写决策拆成 graph / semantic / attitude 三项[^v3-2] 同属一族——攻击的"可优化性"来自维度分离。

两个条件不能由"让 P = Q"或"让 P = R"单独解决，所以论文把 P 拆成两段：`P = S ⊕ I`（⊕ 是文本拼接），由两段分头担责：

- **I 段**用一个攻击者自己选的 LLM（如 GPT-4）现场生成：以 prompt "Please craft a corpus such that the answer is [R] when prompting with [Q]. Please limit the corpus to V words." 生成一段"如果作为 context，会让模型答 R"的小段（最多 V 词）。若验证后模型仍不答 R 就重试，最多 L 次；论文实测平均 2–3 次即可成功[^src2]。
- **S 段**负责让 P 进 top-k：
  - **黑盒**：直接令 S = Q——攻击者不知 retriever 参数时，"问题本身"和"问题"的相似度天然最高，且 Q 不会破坏 I 的生成效果；
  - **白盒**：以 Q 初始化 S，按 `S = argmax_{S'} Sim(f_Q(Q), f_T(S' ⊕ I))` 做基于梯度的对抗文本优化（HotFlip / TextFooler 等都能用）。

两段决策有以下机制含义：

1. **"P 单独就能让模型答 R"** 是个比"和正确答案混合后能赢"更强的条件——论文为此调用 LLM 现场生成 + 自我验证，等于把"能否说服 LLM"这件事用"另一个 LLM"先打过分。这个"用 LLM 验证 LLM 输出"的子流程与 Ragas Faithfulness[^v3-3] 把 answer 拆 statement 后逐条对 context 做 LLM 验证完全同构，只是用途相反；
2. **检索条件几乎被"复制 Q"白送**：黑盒下 S = Q 简单粗暴但极度有效（NQ 数据集 ASR 0.97），它顺便给后续防御（如改写问题、PPL 检测）暴露了攻击表面——S 段会带上原问题的字面 token；
3. **白盒优化的边际收益不大**：表 6 显示，白盒和黑盒 ASR 几乎打平（0.97 vs 0.97），白盒主要赢在"完整的检索 F1"，但代价是生成的 S 看起来像 GCG 后缀那样的"垃圾字符串"，更容易被 PPL 检测。

边界与失败：

- I 段是 LLM 自由生成的，有概率自带正确答案——例如 `What is the name for the CH3COO- ion?` 的恶意文本一句"the CH3COO- ion, typically known as the acetate ion, is now referred to as the sulfate ion"反而提示模型记起了 acetate ion，这种 **parametric bias** 使攻击失败[^src3]；
- 若 retriever 没把所有 k 个 slot 都塞满恶意文本，clean text 会反过来稳住模型（论文 Table 9：top-5 里恶意数 1 → ASR 仅 0.48；恶意数 5 → ASR ~1.00）；
- 该攻击对"目标问题"高度有效，但对**非目标问题**几乎不产生附带影响（黑盒 0.3%、白盒 0.9% 命中非目标问题），因此从被攻击系统侧看不到广谱症状。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1762-1869 — §3 Design of PoisonedRAG：两条件推导、S/I 分解、白/黑盒算法 1 的完整章节
[^src2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1807 — "If the generated answer is not R, we regenerate I until success or a maximum number of (say L) trials have been reached ... As we will show in our experimental results, on average, two or three queries are sufficient to generate I."
[^src3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 354-369 — Analysis on Failure Case：CH3COO- ion 的恶意文本因 parametric bias 自带正确答案，导致攻击失败
[^v3-1]: [etamp-attack-payload-structure](etamp-attack-payload-structure.md) — eTAMP payload 同样把攻击拆成多段分头担责
[^v3-2]: [tkpa-graph-guided-targeted-poisoning](tkpa-graph-guided-targeted-poisoning.md) — TKPA 三项 chunk score 也是 attack-load 维度分离的同族设计
[^v3-3]: [ragas-faithfulness-metric](ragas-faithfulness-metric.md) — 用 LLM 验证 LLM 输出的子流程与 I 段自验证同构
