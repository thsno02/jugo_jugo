---
id: comparison-infrastructure-vs-cognitive-limits
title: 技术基础设施限制 vs 认知复杂度限制
status: accepted
card_type: distinction
tags: [enterprise-wiki, scaling, infrastructure, complexity, comparison]
created_time: 2026-06-05T18:00:00+08:00
edited_time: 2026-06-05T18:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524, hacker-news-original-thread]
justification: ../justification/comparison-infrastructure-vs-cognitive-limits.md
canonical_concept: infrastructure-vs-cognitive-limits
aliases: [基础设施限制vs认知限制, infra vs cognitive limits, 企业扩展双重诊断]
summary: >-
  comparison-infrastructure-vs-cognitive-limits（基础设施限制vs认知限制 / infra vs cognitive limits）
  企业 wiki 扩展失败有两种不同诊断：技术基础设施限制（索引溢出/RBAC/并发）可通过更好架构解决，
  认知复杂度限制（人+agent 的联合管理能力上限）则是根本性的——前者导向「构建更好工具」，
  后者导向「主动管控复杂度」
related: [complexity-collapse-threshold, wiki-enterprise-failure-modes]
  - wiki-enterprise-failure-modes
  - complexity-collapse-threshold
---

企业 LLM Wiki 扩展失败可以从两个不同维度诊断，这两种诊断导向截然不同的应对策略。

**技术基础设施限制**——Atlan 的分析识别出三个具体瓶颈：索引溢出（50K-100K token 上限）、无原生 RBAC、并发写入冲突[^card-1]。这些限制是**设计假设的后果**（面向个人研究者），意味着可以通过不同的架构选择来解决：引入检索层处理索引溢出，引入策略级权限处理 RBAC，引入事务型数据库处理并发。这一诊断的逻辑终点是**构建更好的基础设施**（如数据目录、RAG 管道）。

**认知复杂度限制**——社区讨论识别出一个更根本的问题：系统复杂度会超过人与 agent 的**联合管理能力**[^card-2]。如果人类能处理 10 单位复杂度、LLM 能处理 20 单位，用户倾向于构建 30 单位复杂度的系统——且在失控前无法察觉。这一限制不因基础设施改善而消失：更好的工具只是推高了可构建的复杂度上限，而非消除崩溃的可能性。这一诊断的逻辑终点是**主动管控复杂度**（模块化、人类介入点、拒绝完全自治）。

两种诊断的核心分歧在于**企业扩展是工程问题还是治理问题**：前者相信正确的架构可以解决扩展，后者认为复杂度管理本身是永恒的挑战，任何架构都只是暂时推迟崩溃。在实践中，两者可能同时为真——技术限制需要工程解决，而工程解决方案本身的复杂度需要治理管控。

## Footnotes

[^card-1]: [Wiki 企业级三大失效模式](wiki-enterprise-failure-modes.md) -- 该卡从技术基础设施维度列出企业 wiki 的三个具体失效模式，代表「可通过更好架构解决」的诊断方向
[^card-2]: [复杂度崩溃阈值](complexity-collapse-threshold.md) -- 该卡从认知复杂度维度识别系统崩溃的临界点，代表「复杂度管理是根本问题」的诊断方向
