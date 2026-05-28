---
id: poisonedrag-knowledge-database-attack-surface
title: RAG 的知识库是一个新的、可低成本投毒的攻击面
status: accepted
card_type: concept
tags: [#rag, #attack-surface, #security, #poisonedrag]
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-28T15:20:00+08:00
edited_entity: llm
source_ids: [arxiv-poisonedrag]
provenance_card: ../provenance/poisonedrag-knowledge-database-attack-surface.md
aliases: [knowledge corruption attack, RAG 知识库投毒, RAG attack surface]
related: [poisonedrag-retrieval-generation-two-conditions, poisonedrag-baselines-isolate-two-conditions, poisonedrag-existing-defenses-insufficient, poisonedrag-survives-advanced-rag-and-agents, gragpoison-additive-vs-edit-attack, graphrag-manipulation-only-attack-surface, etamp-environment-injected-memory-poisoning, owasp-llm-top10-community-genealogy]
---

谈论 LLM 安全时常见的两类攻击是：(1) 训练阶段污染（data poisoning，需要改训练数据）和 (2) 推理阶段提示注入（prompt injection，需要改用户输入）。PoisonedRAG 的核心观察是：RAG 系统在**部署时**还多了一个具体的、攻击者真能写入的攻击面——**知识数据库本身**[^src1]。这个面有四个值得记住的特征。OWASP LLM Top 10[^v3-3] 已经把这一面列入官方风险清单的范围；GraphRAG 的 manipulation-only 攻击面[^v3-4] 与 eTAMP 的环境注入记忆投毒[^v3-5] 也共享同一个"被动消费数据 = 新攻击面"的论点。

**1. 攻击者改的是 D，不是 model 或 prompt。** 论文威胁模型里明确：攻击者不能看到知识库已有文本、不能看/查 LLM 的参数。攻击者只需要往 D 里塞 N 条恶意文本，并选好"目标问题"集合 {Q_i} 和"目标答案" {R_i}。区分黑盒/白盒只看是否能访问 **retriever** 的参数。这把可行性从"得拿到模型权重"降到了"找个能改 wiki / 提交网页 / 写公司内部知识库的渠道"——论文举例：Wikipedia 编辑（按 Carlini 等的估计可保守编辑 6.5% 的页面）、伪造新闻网页、企业内部 insider[^src1]。

**2. 注入量是个位数。** 在 NQ（268 万段 clean text）上，黑盒只要给每个目标问题注入 **5 条**恶意文本就能拿到 **97% ASR**；HotpotQA 99%、MS-MARCO 91%[^src2]。换句话说，相对于 D 整体规模，**攻击者只需要 10⁻⁵ 量级的写入权**就能掌控对特定问题的答案。

**3. 攻击面落在 retriever 上，不是 LLM 上。** 即使 LLM 是 GPT-4 / PaLM 2 / LLaMA-2 / Vicuna 等闭源或开源的不同模型，ASR 都稳定在 0.88–0.99（论文 Table `tab:ablation-llm-tmp-results`，温度=1.0 时依然）；换 retriever（Contriever / Contriever-ms / ANCE）也都在 0.88–0.99。也就是说**所谓"换更强的 LLM 就更安全"是一个误区**，只要 retriever 还是用通用语义相似度，这条攻击路径就成立。

**4. 横向附带几乎为零。** 攻击在 1000 道非目标问题上仅有 0.3% / 0.9%（黑/白盒）会被恶意文本影响检索，0% / 0.4% 会被影响最终答案。这意味着系统**不会出现广谱症状**，被攻击者在监控指标上看不到对照组的"被攻击"信号——只有"目标问题"会一次次给出攻击者答案。这种"目标特异性"与 eTAMP 的方向画像[^v3-6] 是同型观察。

操作启示：

- 任何接外部数据源（Wikipedia、网页爬虫、用户上传文档、企业内部 doc）的 RAG 系统都必须把"知识库写入权限"纳入威胁建模，而不是当成"内容质量"问题；
- 现成的 retrieval-side 防御（PPL 检测、改写问题、去重、扩大 k）都被论文逐一证明无效[^v3-1]，因此不能假设"接一个 retriever 就安全"；
- 把"目标问题"维度的端到端答案准确率作为监控信号优先于"整体 retrieval 质量"——后者几乎不会因为攻击而退化。

论文原话作锚：「the knowledge database in a RAG system introduces a new and practical attack surface ... an attacker could inject malicious texts by maliciously editing Wikipedia pages; an attacker could also post fake news or host malicious websites to inject malicious texts when the knowledge databases are collected from the Internet; an insider can inject malicious texts into an enterprise private knowledge database.」[^src1]

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1707 — "In this work, we find that knowledge databases of RAG systems introduce a new and practical attack surface. In particular, an attacker can inject malicious texts into the knowledge database of a RAG system to induce an LLM to generate attacker-desired answers to user questions. ... an attacker could inject malicious texts by maliciously editing Wikipedia pages; an attacker could also post fake news or host malicious websites ... an insider can inject malicious texts into an enterprise private knowledge database."
[^src2]: `data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt` — 行 1724-1726 — "PoisonedRAG could achieve high ASRs with a small number of malicious texts. For instance, on the NQ dataset, we find that PoisonedRAG could achieve a 97% ASR by injecting 5 malicious texts for each target question into a knowledge database (with 2,681,468 clean texts) in the black-box setting."
[^v3-1]: [poisonedrag-existing-defenses-insufficient](poisonedrag-existing-defenses-insufficient.md) — 四类 retrieval-side 防御全部被逐一证明不足
[^v3-3]: [owasp-llm-top10-community-genealogy](owasp-llm-top10-community-genealogy.md) — OWASP LLM Top 10 把"知识库 / 数据源被污染"列入官方治理坐标
[^v3-4]: [graphrag-manipulation-only-attack-surface](graphrag-manipulation-only-attack-surface.md) — GraphRAG 的"只改字、不加文"攻击面共享同一论点
[^v3-5]: [etamp-environment-injected-memory-poisoning](etamp-environment-injected-memory-poisoning.md) — agent memory 投毒是"被动消费的外部数据 = 攻击面"的 agentic 版本
[^v3-6]: [etamp-direction-asymmetry-and-stealth](etamp-direction-asymmetry-and-stealth.md) — 投毒/注入的"目标特异性"在两份论文里都出现
