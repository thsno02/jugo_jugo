---
id: poisonedrag-baselines-isolate-two-conditions
title: PoisonedRAG 的五个基线分别"丢"哪一个条件
status: accepted
card_type: distinction
tags: [#rag, #attack, #poisonedrag, #baseline-comparison]
created_time: 2026-05-26T11:46:00+08:00
edited_time: 2026-05-28T15:16:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
provenance_card: ../provenance/poisonedrag-baselines-isolate-two-conditions.md
aliases: ["Naive Attack vs GCG vs Disinformation vs Prompt Injection vs Corpus Poisoning", "PoisonedRAG baselines"]
related: [etamp-pseudo-trajectory-methodology, poisonedrag-retrieval-generation-two-conditions, gragpoison-additive-vs-edit-attack]
---

PoisonedRAG 论文在 Table 7 给了五个基线 + 自己（黑/白盒）在 NQ / HotpotQA / MS-MARCO 上的 ASR / F1 对比[^src1]。最有用的读法不是"PoisonedRAG 赢了"，而是**每个基线恰好"丢掉"两条件之一**——这把"为什么 retrieval condition + generation condition 必须同时满足"用消融的方式证明了。这种"按条件拆基线"的方法学与 eTAMP 用 pseudo / non-pseudo 拆 PR 与 ASR$_B$[^v3-1] 是同一族——只有把混合在一起的失败模式拆开，跨方法 / 跨模型的比较才有意义。

NQ 上的对照（ASR / F1，黑盒 PoisonedRAG = 0.97 / 0.96 作锚）：

| 基线 | ASR | F1 | 丢掉的条件 | 为什么 |
| --- | --- | --- | --- | --- |
| Naive Attack（把 $Q$ 直接当恶意文本） | 0.03 | 1.0 | generation | F1=1.0 说明 $Q$ 必然被自己 retrieve；但 $Q$ 是"问题"，不是"答案"，作为 context 不会让 LLM 改答 |
| Corpus Poisoning（Zhong 2023） | 0.01 | 0.99 | generation | 用对抗字符串塞进语料，能挤进 top-k（F1≈1），但内容是"随机字符 + 关键词"，LLM 拒绝采信[^src2] |
| GCG Attack（Zou 2023 拿来改） | 0.02 | 0.0 | retrieval | 在 Vicuna-7B 上把"!!!"优化成 `! Dr ! ett . Moore payment--> ...`，确实能强迫 LLM 答出目标答案，但优化目标里没有"被检索"——F1=0 说明根本进不了 top-k[^src3] |
| Disinformation Attack（只用 $I$ 段） | 0.69 | 0.48 | retrieval（部分） | $I$ 是 GPT-4 写的"如果这段被读到，LLM 会答 R"的小段，单独投到语料里有时被检中（F1=0.48），所以 ASR 也能拿到 0.69[^src4] |
| Prompt Injection（指令型） | 0.62 | 0.73 | "知识表述"而非"指令表述" | 注入"当问 Q 时输出 R"的指令；既被检索（F1=0.73），LLM 也部分听话（ASR 0.62），但指令在文本检测里很扎眼，且对齐良好的 LLM 会偶尔抗指令 |

PoisonedRAG 的 $S \oplus I$ 同时拿满两个条件：$S=Q$（黑盒）解决检索、$I$（GPT-4 现场生成的"伪证据"）解决生成，**所以 ASR 跳到 0.97**[^v3-2]。HotpotQA / MS-MARCO 上的相对排序一致：Naive 与 Corpus Poisoning 拿满 F1 但 ASR 接近 0；GCG 拿满"生成被骗"但 F1=0；Disinformation 与 Prompt Injection 各拿到中等分但都被 PoisonedRAG 大幅超越。

这条对照的几个工程含义：

- **新提"检索增强系统"的攻击，必须独立报告 retrieval-side（是否被检中）与 generation-side（被检中后能否驱动答案）两个分数**，否则会和论文里这些基线一样"看起来都做了些什么但什么都没做透"[^src5]。
- **既有的 corpus poisoning 文献（Zhong 等）不能直接拿来评估 RAG**，因为它的目标是"被检中"而不"驱动回答"。同理，prompt injection 检测器（侧重指令模式）也对 PoisonedRAG 的"恶意知识"基本无效——它伪装成事实而非指令。
- **disinformation 攻击是 PoisonedRAG 的弱化版**。如果攻击者只能不加 $S$ 段（例如不知道目标问题文本，只知道目标话题），仍能拿到 ASR 0.69 / 1.0 / 0.57，比 prompt injection 还高——说明"伪事实"本身已是强攻击载体。这一观察也对应 GraphRAG additive vs in-place 攻击的家族区分[^v3-3]：纯"事实改写"已是独立强类。

边界与误读：

- 比较是在论文默认设置（$N=5$、$k=5$、PaLM 2 / GPT-4 等）下做的；不同设置下绝对数字会变，但"每个基线恰好缺一个条件"的结构性结论稳定。
- GCG ASR 0.02 不等于 GCG 在 RAG 场景上一无是处——只是它没被设计来攻击"被检索"环节。若把 GCG 的优化目标改成"既被检索又驱动答案"，原则上能恢复——论文将此列为开放方向。
- Naive Attack 的 ASR=0.03 不是噪声底线：它代表"未受攻击时 LLM 自己也偶尔会给出和 target answer 一致的答案"的下界，约等于 random hit。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1332-1338 — Table tab:comparision-baseline：NQ 上五基线 + PoisonedRAG（黑/白盒）的 ASR / F1 全表
[^src2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1226-1232 — "Corpus Poisoning Attack ... this attack is similar to PoisonedRAG (white-box) when PoisonedRAG uses S alone as the malicious text P (i.e., P=S)"
[^src3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1236 — "GCG achieves a very low ASR (close to Naive Attack). The reason is that it cannot achieve the retrieval condition."
[^src4]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1239 — "The crafted I ... can be viewed as disinformation. ... This baseline can be viewed as a variant of PoisonedRAG."
[^src5]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1403-1404 — "those baselines are not designed to simultaneously achieve retrieval and generation conditions"
[^v3-1]: [etamp-pseudo-trajectory-methodology](etamp-pseudo-trajectory-methodology.md) — 同样按条件拆基线（PR vs ASR）才能跨方法比较
[^v3-2]: [poisonedrag-retrieval-generation-two-conditions](poisonedrag-retrieval-generation-two-conditions.md) — $S \oplus I$ 双条件机制本身
[^v3-3]: [gragpoison-additive-vs-edit-attack](gragpoison-additive-vs-edit-attack.md) — "伪事实"作为独立攻击家族，与 GraphRAG additive 路线呼应
