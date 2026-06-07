---
id: graphrag-provider-factory-extensibility
title: GraphRAG 工厂模式可扩展子系统架构
status: accepted
card_type: pattern
tags: [graphrag, factory-pattern, extensibility, plugin, architecture, implementation]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
justification: ../justification/graphrag-provider-factory-extensibility.md
canonical_concept: graphrag-provider-factory-extensibility
aliases: [GraphRAG 工厂模式, provider factory pattern, GraphRAG 可扩展架构, 自定义 provider 注册]
summary: >-
  graphrag-provider-factory-extensibility（GraphRAG 工厂模式可扩展架构）在 7 个子系统（language model/input reader/cache/logger/storage/vector store/pipeline+workflows）使用工厂注册模式，允许用户以任意字符串名注册自定义实现甚至覆盖内置默认，支持 LiteLLM 以外的模型协议注入
related: [graphrag-cli-settings-yaml-config, graphrag-indexing-pipeline-six-phases, graphrag-litellm-model-integration]
---

GraphRAG 的架构在多个子系统中使用工厂模式（factory pattern）实现深度可定制性——用户可以注册自己的 provider 实现以替换或扩展内置功能 [^src-1]。

**七大可扩展子系统**：

1. **Language Model**（`graphrag_llm/completion/completion_factory.py`）：实现自定义 `chat` 和 `embed` 方法以使用内置 LiteLLM 之外的模型提供商
2. **Input Reader**（`graphrag_input/input_reader.py`）：支持 text/CSV/JSON 以外的文件格式
3. **Cache**（`graphrag_cache/cache_factory.py`）：在 file/blob/CosmosDB 之外创建自定义缓存位置
4. **Logger**（`graphrag/logger/factory.py`）：在 file/blob 之外创建自定义日志写入目标
5. **Storage**（`graphrag_storage/tables/table_provider_factory.py`）：在 file/blob/CosmosDB 之外的自定义存储后端
6. **Vector Store**（`graphrag_vectors/vector_store_factory.py`）：在 LanceDB/Azure AI Search/CosmosDB 之外实现自定义向量存储
7. **Pipeline + Workflows**（`graphrag/index/workflows/factory.py`）：实现自定义 `run_workflow` 函数或注册整个 pipeline（命名 workflow 列表）

**自定义模型注册示例** [^src-2]：
```python
from graphrag_llm.completion import LLMCompletion, register_completion

class MyCustomCompletionModel(LLMCompletion):
    ...  # 实现 Protocol

register_completion("my-custom-completion-model", MyCustomCompletionModel)
```

配置中通过类型名引用：
```yaml
completion_models:
  default_completion_model:
    type: my-custom-completion-model
```

所有工厂都允许使用任意字符串名注册实现，甚至直接覆盖内置实现的名称 [^src-3]。

**限制**：自定义模型会收到与 GraphRAG 内部使用相同的初始化参数和方法调用参数，目前不支持自定义参数定义——需要通过闭包作用域或工厂模式获取自定义配置值 [^src-4]。

此架构设计体现了 GraphRAG 作为可组合研究平台的定位——不仅是一个固定管线，而是一组可替换组件的框架。

## Footnotes

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/architecture.md -- "Several subsystems within GraphRAG use a factory pattern to register and retrieve provider implementations. This allows deep customization to support your own implementations"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/models.md -- register_completion example with MyCustomCompletionModel class
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/index/architecture.md -- "All of these factories allow you to register an impl using any string name you would like, even overriding built-in ones directly"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/models.md -- "There is not currently any ability to define custom parameters, so you may need to use closure scope or a factory pattern within your implementation to get custom config values"
