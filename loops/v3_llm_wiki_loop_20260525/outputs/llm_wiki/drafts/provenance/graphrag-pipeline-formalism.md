---
schema: draft_card_provenance.v3
draft_card: ../cards/graphrag-pipeline-formalism.md
material_id: arxiv-graph-poisoning
digest_id: digest_arxiv-graph-poisoning
source_paths:
  - data/raw/arxiv/arxiv-graph-poisoning/agent_source_bundle.txt
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-26T11:40:00+08:00
edited_entity: llm
---

## 源证据

- L263–275：*"Given an unstructured document corpus $D = \{d_1, \dots, d_n\}$, GraphRAG first divides it into smaller text chunks ... $G_i = f_{\text{extract}}(c_i)$. These mini-graphs are then merged to form the overall corpus graph: $G_{\text{merged}} = \bigcup_{i=1}^m G_i$. Next, a community detection function $f_{\text{community}}$ partitions $G_{\text{merged}}$ into communities ... For each community $C_j$, a summary $S_j$ is generated ... When a user submits a query $Q$, GraphRAG applies a retrieval function $g_{\text{retrieve}}$ to extract the relevant community summaries $S_{\text{rel}} \subseteq \{S_1, \dots, S_k\}$ ... Finally, the LLM generates the answer conditioned on the query and retrieved context: $\text{Answer} = \text{LLM}(Q, S_{\text{rel}})$."*
- L178–185：*"Prior works have identified three main attack categories. First, malicious documents injected into the corpus ... Second, adversarial instructions ... Third, the retriever itself can be attacked ... GraphRAG inherits these risks but also exposes a qualitatively different vulnerability. Unlike traditional RAG, GraphRAG does not answer questions directly from retrieved context. It first converts the entire corpus into a structured knowledge graph, and all subsequent tasks depend on this graph."*
- L283–287：*"We consider a gray-box adversary that poisons GraphRAG by editing the source corpus ... The attacker can modify a small fraction of trusted sources (e.g., Wikipedia) but has no access to the constructed graph or model parameters."*

## 卡片范围是否成立

本卡聚焦于"流水线形式化 + 它如何在结构上放大单字改动的影响"。流水线步骤、$f_{\text{extract}}$ / $f_{\text{community}}$ / $g_{\text{retrieve}}$ 的函数名、"摘要才是 LLM 真正读到的内容"这一推论都来自论文的 §Background；攻击面只在 GraphRAG 出现（而不存在于 chunk-RAG）属于论文 Introduction 的明确论证。"信任放大器"是对论文论点的提炼措辞，不是原文术语，但与作者反复强调的"corruption persists and misleads a broad range of queries"语义一致。

## 发表门控结果

本轮未运行。

## 备注

- 与既有卡 `graphrag-manipulation-only-attack-surface` 互补：那张是从攻击面定性，本卡从管线机制定性；推荐 related 互链。
- 后续若有 v2 卡片专门描述"知识图 + 检索增强"通用范式，应在 comparison_provenance 阶段对比 scope 是否重叠。
