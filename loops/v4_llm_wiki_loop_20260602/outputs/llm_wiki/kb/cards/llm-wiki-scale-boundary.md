---
id: llm-wiki-scale-boundary
title: LLM Wiki 的适用规模边界
status: accepted
card_type: distinction
tags: [llm-wiki, scale, vector-search, personal-knowledge]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-fr-guide]
justification: ../justification/llm-wiki-scale-boundary.md
canonical_concept: llm-wiki-scale-boundary
aliases: [规模边界, scale boundary, 个人知识规模]
summary: >-
  llm-wiki-scale-boundary（规模边界 / scale boundary / 个人知识规模）指 LLM Wiki 在个人规模
  （10 至数百篇文档）下表现最佳，超出后 interlink 管理的 token 成本上升，vector search 更为适合
related: [complexity-collapse-threshold, llm-wiki-rag-depth-distinction, wiki-enterprise-failure-modes]
---

LLM Wiki 的适用场景被明确定位为**个人规模的知识管理**，典型范围为 10 至数百篇文档[^src-1]。在此规模内，结构化 markdown 加上 LLM 的读写能力已经足够，不需要 vector database 或复杂的 RAG 管道。Karpathy 自己的研究 wiki 达到 100 篇以上文章、40 万词规模[^src-2]。

超出这一边界后，管理页面间互链（interlinks）在 token 消耗上变得昂贵，此时**语义搜索**（vector search）在数千个 chunk 上的检索能力更为适合[^src-3][^src-4]。

RAG 在大规模语料库和对非结构化数据的一次性查询场景中仍然具有优势[^src-5]。两种方法并非互斥——该来源预测未来演化方向之一是针对团队或企业部署的 RAG-vector 混合方案[^src-6]。Atlan 的分析将这一规模边界具体化为三个企业级失效模式：索引溢出、无访问控制、并发写入冲突[^card-1]。社区讨论识别出的复杂度崩溃阈值从认知维度解释了为何超出该边界后系统不仅在 token 成本上变得昂贵，而且在复杂度上对人和 agent 都变得不可管理[^card-2]。

## Footnotes

[^card-1]: [Wiki 企业级三大失效模式](wiki-enterprise-failure-modes.md) -- 本卡描述 wiki 在数百篇文档后的理论规模边界，Atlan 将这一边界具体化为三个企业级失效模式（50K-100K token 索引溢出、无 RBAC、并发冲突）
[^card-2]: [复杂度崩溃阈值](complexity-collapse-threshold.md) -- 本卡界定 wiki 的量化规模边界（10 至数百篇），该卡从认知维度解释超出该边界后的崩溃机制：系统复杂度超过人与 agent 的联合管理能力

[^src-1]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L154 -- "la connaissance personnelle a echelle individuelle, de 10 a quelques centaines de documents"
[^src-2]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L29 -- "des wikis de plus de 100 articles et 400 000 mots"
[^src-3]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L209-210 -- "Au-dela, la gestion des interliens peut devenir couteuse en tokens et une vector search devient plus adaptee."
[^src-4]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L158 -- "La vector database devient utile seulement au-dela d'une certaine echelle, la ou la recherche semantique sur des milliers de chunks devient necessaire."
[^src-5]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L154 -- "Le RAG reste pertinent pour des corpus massifs et des requetes ponctuelles sur des bases non structurees."
[^src-6]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L173 -- "L'hybridation RAG-vector pour les deploiements en equipe ou a l'echelle entreprise"
