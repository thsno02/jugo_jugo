---
id: data-catalog-as-enterprise-wiki
title: 数据目录作为企业级 Wiki 的结构等价物
status: accepted
card_type: concept
tags: [data-catalog, llm-wiki, enterprise, governance, structural-mapping]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
justification: ../justification/data-catalog-as-enterprise-wiki.md
canonical_concept: data-catalog-as-enterprise-wiki
aliases: [数据目录即企业wiki, data catalog as enterprise wiki, 企业wiki等价物]
summary: >-
  data-catalog-as-enterprise-wiki（数据目录即企业wiki / data catalog as enterprise wiki）
  受治理的数据目录在结构上等价于 Karpathy 个人 wiki 的企业版：策展摘要=wiki文章、
  血缘=反向链接、认证=质量分数、RBAC=访问控制、主动元数据传播=健康检查；
  连接（MCP/API）是缺失的环节而非构建
related: [complexity-collapse-threshold, continuous-drift-detection, cross-tool-entity-resolution, knowledge-as-work-byproduct, single-curator-bottleneck]
---

Atlan 文章提出一个结构映射：**受治理的数据目录在结构上就是 Karpathy 为个人构建的 wiki 的企业版本**[^src-1]。

具体的结构对应关系如下：

| 个人 Wiki 功能 | 企业数据目录等价物 |
|---|---|
| 策展的 wiki 摘要文章 | 策展的资产摘要（文档） |
| 反向链接（backlinks） | 交叉引用（数据血缘） |
| 概念定义 | 业务术语表 |
| 健康检查提示（手动触发） | 主动元数据传播（管线运行时自动推送） |
| 无访问控制 | 策略级 RBAC（如 FinanceAgent 无法访问 HR 数据） |

关键论断是：企业需要的 LLM 知识库在大多数情况下**已经存在**。**连接是缺失的环节，而非构建**——通过 MCP server 和 API 将受治理的、认证的、始终新鲜的元数据层连接到 LLM，而不是在未治理的源数据之上构建影子知识层[^src-2]。

这一映射的实际含义是：当企业高管读到 Karpathy 的帖子并要求数据团队"为公司构建 LLM wiki"时，数据团队面临的直接问题是——企业数据不是整洁的 markdown 文章集合，而是分布在数十个系统中、由数百人维护、默认未受治理的[^src-3]。

Falconer 的企业 wiki 指南独立提出了两个与数据目录映射高度一致的机制：持续偏移检测对应于目录的"主动元数据传播"[^card-1]，跨工具实体解析对应于目录的"血缘+业务术语表"[^card-2]。两个来源从不同视角趋同于同一架构。

数据目录的结构映射直接回应了单一策展人瓶颈：用系统级的自动化治理取代个人策展[^card-3]。Falconer 的「知识作为工作副产品」原则从工作流层面趋同于同一结论——知识应在工作中自动浮现，而非额外构建[^card-4]。然而，社区讨论提出的复杂度崩溃阈值对此持谨慎态度——即使连接了已有的元数据层，系统复杂度仍可能超过人与 agent 的管理能力[^dist-1]。

## Footnotes

[^src-1]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L394 -- "Atlan's data catalog is structurally the enterprise version of what Karpathy built for himself."
[^src-2]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L396 -- "The enterprise LLM knowledge base the organization needs already exists in most cases. The connection is the missing piece, not the construction."
[^src-3]: `data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L390-391 -- "enterprise data is not a tidy collection of markdown articles. It is distributed across dozens of systems, maintained by hundreds of people, ungoverned by default"
[^card-1]: [持续偏移检测](continuous-drift-detection.md) -- Falconer 的持续偏移检测对应于数据目录的"主动元数据传播"，两个来源从不同视角趋同于同一自动维护机制
[^card-2]: [跨工具实体解析](cross-tool-entity-resolution.md) -- Falconer 的跨工具语义实体解析对应于数据目录的"血缘+业务术语表"，两个来源独立地指向跨系统知识链接的必要性
[^card-3]: [单一策展人瓶颈](single-curator-bottleneck.md) -- 该卡诊断企业规模下个人策展的结构性失效，本卡的数据目录映射是对该瓶颈的架构层面解法：用自动化治理取代单一策展人
[^card-4]: [知识作为工作副产品](knowledge-as-work-byproduct.md) -- 本卡主张企业知识库已存在于数据目录中（连接而非构建），该卡从工作流层面主张知识应作为工作副产品自动浮现——两者趋同于「不额外构建」
[^dist-1]: [复杂度崩溃阈值](complexity-collapse-threshold.md) -- 本卡主张「连接是缺失的环节，而非构建」（乐观），该卡主张复杂度必然超出可管理范围（审慎），区分点在于：连接已有系统是否足以解决企业扩展问题，还是仍会触发复杂度崩溃
