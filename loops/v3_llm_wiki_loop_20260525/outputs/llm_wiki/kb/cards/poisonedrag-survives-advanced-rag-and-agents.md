---
id: poisonedrag-survives-advanced-rag-and-agents
title: PoisonedRAG 在 Self-RAG / CRAG / 真实 Wikipedia / LLM 智能体上同样有效
status: accepted
card_type: source_claim
tags: [#rag, #poisonedrag, #self-rag, #crag, #llm-agent, #generalization]
created_time: 2026-05-26T11:48:00+08:00
edited_time: 2026-05-28T15:24:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
provenance_card: ../provenance/poisonedrag-survives-advanced-rag-and-agents.md
aliases: ["PoisonedRAG advanced RAG", "PoisonedRAG real-world"]
related: [etamp-environment-injected-memory-poisoning, owasp-agentic-top10-2026-positioning, ragchecker-generator-trilemma]
---

PoisonedRAG 论文的主实验在"基本 RAG"上做：Contriever + PaLM 2 / GPT-4 + 三个静态 QA 数据集。许多读者会下意识地把这套结果归到"研究环境"。Zou 等人特地补了四组"现实化"实验，专门把攻击 inject 到更接近生产的设置里——结果证明攻击效力几乎不被这些"硬化"路线削弱。

四组实验的成绩：

1. **Self-RAG**（Asai 2023，让 LLM 在回答时按需自我反思、调用检索并打 reflection tokens）：NQ 黑盒 ASR 0.77、HotpotQA 0.87、MS-MARCO 0.73；白盒类似。F1 ≈ 0.89–1.0 说明恶意文本仍然进得了 retrieval[^src1]。
2. **CRAG**（Yan 2024，引入轻量级 retrieval evaluator 给检索打分、丢弃低质上下文）：黑盒 ASR 0.74–0.78（NQ / HotpotQA / MS-MARCO），CRAG 的 evaluator 没把"看起来相关、实际是伪造证据"的恶意 chunk 筛掉[^src5]。
3. **Wikipedia-based ChatBot**（21,015,324 段，来自 2018-12-20 Wikipedia dump）：每个目标问题仍只注 5 条恶意文本，NQ / HotpotQA / MS-MARCO 黑盒 ASR 分别 0.95 / 1.0 / 0.94[^src2]。语料规模放大了 ~8×，攻击效力基本不掉——10⁻⁷ 量级的写入权仍足够。
4. **LLM Agent（ReAct）**：把 RAG 嵌进"思考–行动–观察"循环里，agent 自行决定何时检索。NQ / HotpotQA / MS-MARCO 黑盒 ASR 0.72 / 0.58 / 0.52[^src3]——比基本 RAG 略低，但仍是有效攻击。这与 eTAMP 在 web agent 上观察到的攻击成立性[^v3-1] 一道，把 RAG / agent 投毒纳入 agentic security 范围，正对应 OWASP Agentic Top 10 单列清单[^v3-2] 的范围限定。
5. （额外）**FEVER 事实验证**：把"目标答案"换成"目标判定" SUPPORTS/REFUTES，黑盒 ASR 0.97 / 白盒 0.88，F1 0.98 / 0.99[^src4]——说明攻击模式不依赖"开放域 QA"这一具体任务。

这串数字的含义比单一数字更重要：

- **常被推荐的"高级 RAG 方案"并不天然防投毒**。Self-RAG / CRAG 解决的是"模型用不好检索"的问题，不是"语料里有恶意"的问题。CRAG 的检索 evaluator 看的是相关性、不是真实性；恶意 chunk 故意构造得高度相关，正好绕过。这一观察也呼应 RAGChecker 给生成器画出的 trilemma[^v3-3]：faithfulness × context utilization × noise sensitivity 三角无法同时优化，恶意 chunk 正是在 utilization 这一极抓住生成器。
- **规模不是防御**。21M 段语料里的 5 条恶意文本（10⁻⁷ 写入比）仍能 ≥0.94 ASR，否认了"用更大的语料库稀释攻击"这一直觉。
- **agent 框架略削弱攻击**（ASR 从 ~0.97 掉到 ~0.6）：原因是 ReAct 有时多轮检索 / 推理，会"看到" clean context；但仍属于不可接受的攻击成功率。
- **泛 NLP 任务也受冲击**：FEVER 不是 QA，攻击同样有效，说明 "retrieval + generation conditions" 这套设计原则有跨任务普适性。

边界与误读：

- 4 个高级实验都用论文默认设置（$N=5$、$k=5$）；如果生产系统改用 $k=50$ 等"扩大检索"路线，ASR 会下降——但论文 Knowledge Expansion 实验已显示即使 $k=50$，HotpotQA 上 ASR 仍 41–43%（黑/白盒）。
- agent 框架的 0.52–0.72 ASR 是在 ReAct 框架上的——不同 agent 架构（如 Reflexion、AutoGPT、function-calling 直接调 search）可能差距更大；论文未做全面 agent 对比。
- 这些数字使用 substring matching 计算 ASR；论文同时给了人评对照，差距通常在 ±5%。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1587-1599 — Table tab:advanced-rag：Self-RAG / CRAG 在三数据集上的 ASR / F1
[^src2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1644-1656 — Table tab:real-world case study：21M Wikipedia 真实场景下 ASR 0.91–1.0
[^src3]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1663 — "ReAct LLM Agent" 在 NQ / HotpotQA / MS-MARCO 上黑盒 ASR 0.72 / 0.58 / 0.52
[^src4]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 2065-2066 — "PoisonedRAG can achieve a 0.98 and 0.99 F1-Score in black-box and white-box settings ... a 0.97 and 0.88 ASR ..." on FEVER
[^src5]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1623 — "the crafted malicious texts are relevant to the target questions, making the LLM generate incorrect answers based on malicious texts" —— CRAG / Self-RAG 失败的统一解释
[^v3-1]: [etamp-environment-injected-memory-poisoning](etamp-environment-injected-memory-poisoning.md) — eTAMP 在 web agent 上观察到的攻击成立性
[^v3-2]: [owasp-agentic-top10-2026-positioning](owasp-agentic-top10-2026-positioning.md) — agentic 风险单列清单的范围限定
[^v3-3]: [ragchecker-generator-trilemma](ragchecker-generator-trilemma.md) — faithfulness × utilization × noise 三角解释 CRAG / Self-RAG 为何挡不住伪相关 chunk
