---
id: graphrag-provider-factory-extensibility
title: GraphRAG Provider/Factory 可扩展架构
status: draft
card_type: design-pattern
tags: [factory-pattern, extensibility, custom-provider, litellm, model-injection, plugin-architecture]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
evidence_basis: code_implementation
justification: ../justification/graphrag-provider-factory-extensibility.md
canonical_concept: graphrag-provider-factory-extensibility
aliases: [GraphRAG factory pattern, provider extensibility, custom model injection, 自定义Provider注入, LiteLLM integration]
summary: >-
  GraphRAG 多个子系统（language model、input reader、cache、logger、storage、vector store、pipeline/workflows）采用 factory 模式支持自定义实现注册。LLM 层通过 LiteLLM 支持 100+ 模型且要求 structured output JSON schema 能力；不支持的模型可通过 Model Protocol 自定义实现注入或 Proxy API（ollama/LiteLLM Proxy）转发。factory pattern provider extensibility LiteLLM custom model protocol register。
related: [graphrag-six-phase-indexing-pipeline, graphrag-knowledge-graph-augmented-rag]
---

GraphRAG 的架构在多个子系统中采用 factory 模式实现深度可定制化。以下子系统均支持通过注册自定义实现来替换或扩展内置功能：[^src-1]

1. **Language Model** -- 实现自定义 `chat` 和 `embed` 方法
2. **Input Reader** -- 支持 text/CSV/JSON 以外的文件类型
3. **Cache** -- 除内置的 file/blob/CosmosDB 外的缓存位置
4. **Logger** -- 自定义日志写入目标
5. **Storage** -- 自定义表存储后端（数据库等）
6. **Vector Store** -- 除 LanceDB/Azure AI Search/CosmosDB 外的向量存储
7. **Pipeline & Workflows** -- 自定义 workflow 步骤或注册完整 pipeline

LLM 调用通过 LiteLLM 统一管理，支持 100+ 模型提供者，但要求模型能返回符合 JSON schema 的 structured output。[^src-2] 对于 LiteLLM 不支持的模型，有两种接入路径：

- **Proxy API**：通过 ollama 或 LiteLLM Proxy Server 将 HTTP 调用转发到其他模型提供者。需注意模型必须可靠返回 GraphRAG 期望的特定响应格式。[^src-3]
- **Model Protocol**：实现标准的 completion/embedding Protocol 类并通过 `register_completion` 注册到 factory，随后在配置中通过 type 名引用。此方式仅支持库模式使用（不支持 CLI）。[^src-4]

所有 factory 允许使用任意字符串名称注册实现，甚至可以直接覆盖内置实现。

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/index/architecture.md" P362-376 -- "Several subsystems within GraphRAG use a factory pattern to register and retrieve provider implementations"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/config/models.md" P1339 -- "LiteLLM provides support for 100+ models though... must support returning structured outputs adhering to a JSON schema"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/config/models.md" P1406-1408 -- "Many users have used platforms such as ollama and LiteLLM Proxy Server to proxy the underlying model HTTP calls"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- "docs/config/models.md" P1412-1428 -- "We support model injection through the use of a standard completion and embedding Protocol"
[^card-1]: [graphrag-six-phase-indexing-pipeline](graphrag-six-phase-indexing-pipeline.md) -- factory 模式贯穿流水线各阶段的实现
