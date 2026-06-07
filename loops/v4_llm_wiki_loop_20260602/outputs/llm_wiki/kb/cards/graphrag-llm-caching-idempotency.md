---
id: graphrag-llm-caching-idempotency
title: GraphRAG LLM 缓存层实现幂等与容错索引
status: accepted
card_type: mechanism
tags: [graphrag, caching, idempotency, fault-tolerance, llm-api, implementation]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
justification: ../justification/graphrag-llm-caching-idempotency.md
canonical_concept: graphrag-llm-caching-idempotency
aliases: [GraphRAG LLM 缓存, LLM completion cache, 索引幂等性, graphrag cache layer]
summary: >-
  graphrag-llm-caching-idempotency（GraphRAG LLM 缓存层）在所有 LLM 交互外层包裹缓存——相同输入（prompt + tuning parameters）返回已缓存的 completion 结果，使索引器在网络故障后重启时自动跳过已完成的请求，实现幂等索引与断点续跑
related: [graphrag-indexing-pipeline-six-phases, graphrag-cli-settings-yaml-config, graphrag-provider-factory-extensibility]
---

GraphRAG 在设计时充分考虑了 LLM API 交互的脆弱性——网络延迟、限流、服务中断等都是索引大型语料时的常见障碍。为此，系统在 LLM 交互层引入了缓存机制 [^src-1]。

**缓存原理**：当使用相同输入集（prompt 文本 + 调优参数如 temperature、max_tokens 等）发起 completion 请求时，如果存在已缓存的结果则直接返回。这使得索引器具备三个关键属性 [^src-2]：
- **网络容错**：中断后重启时，已完成的 LLM 调用无需重新执行
- **幂等性**：相同输入多次运行产生相同结果
- **效率**：避免对相同内容的重复付费调用

**配置选项**（`cache` section）[^src-3]：
- `type: json`（默认）——将缓存序列化为 JSON 文件
- `type: memory`——内存缓存（进程结束即丢失）
- `type: none`——禁用缓存

缓存的存储后端通过内嵌的 `storage` 配置指定，支持 file/blob/CosmosDB，使分布式团队可以共享同一缓存存储 [^src-4]。

**实际影响**：GraphRAG 索引"可能是昂贵的操作"（README 警告），尤其是对大型语料使用 GPT-4 级别模型时。缓存层使得：
- 因限流失败的索引任务可安全重启，已完成的 text unit 提取不会重新计费
- 调试管线配置时，修改下游参数不会重新触发上游 LLM 调用
- 团队成员可复用已有缓存结果

缓存机制也是工厂模式可扩展子系统之一——用户可注册自定义缓存实现[^card-1]。

## Footnotes

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/architecture.md -- "The GraphRAG library was designed with LLM interactions in mind, and a common setback when working with LLM APIs is various errors due to network latency, throttling, etc."
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/architecture.md -- "When completion requests are made using the same input set (prompt and tuning parameters), we return a cached result if one exists. This allows our indexer to be more resilient to network issues, to act idempotently, and to provide a more efficient end-user experience."
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/yaml.md -- "cache: type json|memory|none"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/yaml.md -- cache storage 配置支持 file/memory/blob/cosmosdb
[^card-1]: [GraphRAG 工厂模式可扩展子系统架构](graphrag-provider-factory-extensibility.md) -- 缓存是七大可扩展子系统之一，用户可注册自定义 cache provider
