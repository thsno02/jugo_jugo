---
id: graphrag-pipeline-formalism
title: GraphRAG 流水线的形式化：为什么 LLM 不直接看 chunk
status: accepted
card_type: concept
tags: [#graphrag, #rag, #pipeline, #knowledge-graph]
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-28T15:30:00+08:00
edited_entity: llm
source_ids: [arxiv-graph-poisoning]
provenance_card: ../provenance/graphrag-pipeline-formalism.md
aliases: ["GraphRAG pipeline", "community summary as context"]
related: [graphrag-global-sensemaking-pipeline, graphrag-leiden-community-hierarchy, graphrag-manipulation-only-attack-surface, ukpa-coreference-disruption, tkpa-graph-guided-targeted-poisoning]
---

GraphRAG（以 Microsoft GraphRAG 为代表）与普通 chunk-RAG 最本质的差别，是 LLM 回答时**根本不读原始 chunk**，而是读一层"社区摘要"。论文用一组函数把整条管线写成显式形式[^src1]，这套写法解释了为什么"改几个字也能把整套系统拖垮"。要把这套形式化与 Microsoft GraphRAG 的工程版本对齐，可参看 global sensemaking 两阶段流水线[^v3-1] 与 Leiden 社群层次[^v3-2]。

形式化分五步：

1. 切分：未结构化语料 $D=\{d_1,\dots,d_n\}$ 切成 chunks $\{c_1,\dots,c_m\}$。
2. 抽取：对每个 chunk 跑抽取函数 $G_i = f_{\text{extract}}(c_i)$，得到 entity–relation–entity 三元组组成的局部小图。
3. 合并：所有小图取并 $G_{\text{merged}}=\bigcup_{i=1}^{m} G_i$，得到全局知识图。
4. 社区与摘要：在 $G_{\text{merged}}$ 上跑社区检测 $C=f_{\text{community}}(G_{\text{merged}})$，再为每个社区 $C_j$ 生成摘要 $S_j$。**摘要才是 LLM 的"知识"**。
5. 查询时：对查询 $Q$，检索器 $g_{\text{retrieve}}$ 从社区摘要集合里挑相关子集 $S_{\text{rel}}=g_{\text{retrieve}}(Q, \{S_1,\dots,S_k\})$；最后 $\text{Answer}=\text{LLM}(Q, S_{\text{rel}})$。

这套写法暴露三个 chunk-RAG 没有的性质：

- **LLM 视野是摘要、不是 chunk**。投毒只要污染到摘要——而摘要由 $f_{\text{community}}$ 在被污染的图上生成——下游就被污染；攻击者**根本不需要让任何恶意句子被检索回来**。这正是 manipulation-only 攻击面[^v3-3] 立足的几何依据。
- **f_extract / f_community 都由 LLM 在构图阶段执行**。这一阶段没有人类在场、也没有检查，因而成了 GraphRAG 特有的"信任放大器"：源文本里的一个代词改动可以让 $f_{\text{extract}}$ 抽错实体，错误经 $f_{\text{community}}$ 进入摘要，永久驻留在 $S_j$ 中——UKPA[^v3-4] 正是利用这一点。
- **结构持久化**：图一旦构建好，所有后续 QA、对话都"消费"它。改 chunk 影响一次回答，改图影响所有依赖该社区的回答；这是 TKPA[^v3-5] / UKPA 能用 <0.06% 改动撬动全系统的几何原因。

论文进一步把这套管线和传统 RAG 的"three attack categories"做了对比[^src2]：document injection、prompt injection、retriever attack 都假设攻击者改的是直接被读到的内容；GraphRAG 的"manipulation-only"攻击则攻击 $f_{\text{extract}}$ 与 $f_{\text{community}}$ 之间的转换，这一面在 chunk-RAG 里根本不存在。

边界与误读：

- 不同 GraphRAG 实现的 $f_{\text{community}}$ 不同（Microsoft 用 Leiden 检测，LightRAG 等使用别的方案）；本卡的形式化跟随 Microsoft GraphRAG 的官方流水线。
- "LLM 不直接看 chunk"是默认设置的描述。某些 GraphRAG 实现在低层查询模式下会回退到 chunk-level 检索；这时的安全性接近传统 chunk-RAG。
- 不要把这套形式化当成"知识图 + RAG"的一般定义——它是 Microsoft GraphRAG 路线的具体管线；GraphRAG 是论文当下使用的术语，但学界对"图结构 + 检索增强生成"还有别的实现路径。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` — 行 261-282 — §Attack Methodology / Background / GraphRAG Pipeline：五步函数 $f_{\text{extract}}$、$f_{\text{community}}$、$g_{\text{retrieve}}$ 与 $\text{Answer}=\text{LLM}(Q, S_{\text{rel}})$ 的逐式定义；同段 L283-287 给出攻击者能改源语料而看不到图的威胁模型
[^src2]: `data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt` — 行 178-185 — Introduction：传统 RAG 的三类攻击与 GraphRAG 引入的 "qualitatively different vulnerability"
[^v3-1]: [graphrag-global-sensemaking-pipeline](graphrag-global-sensemaking-pipeline.md) — Microsoft GraphRAG 两阶段流水线的工程版本
[^v3-2]: [graphrag-leiden-community-hierarchy](graphrag-leiden-community-hierarchy.md) — Leiden 社群作为全局摘要索引
[^v3-3]: [graphrag-manipulation-only-attack-surface](graphrag-manipulation-only-attack-surface.md) — manipulation-only 攻击面立足的形式化依据
[^v3-4]: [ukpa-coreference-disruption](ukpa-coreference-disruption.md) — 利用 $f_{\text{extract}}$ 共指消解脆弱性的具体攻击
[^v3-5]: [tkpa-graph-guided-targeted-poisoning](tkpa-graph-guided-targeted-poisoning.md) — 利用结构持久化做 targeted 攻击的具体方法
