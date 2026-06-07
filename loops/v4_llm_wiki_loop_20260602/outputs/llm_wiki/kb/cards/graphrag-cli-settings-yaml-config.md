---
id: graphrag-cli-settings-yaml-config
title: GraphRAG CLI 与 settings.yaml 配置体系
status: accepted
card_type: mechanism
tags: [graphrag, cli, configuration, yaml, settings, implementation]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
justification: ../justification/graphrag-cli-settings-yaml-config.md
canonical_concept: graphrag-cli-settings-yaml-config
aliases: [GraphRAG 配置系统, graphrag settings.yaml, GraphRAG CLI 命令]
summary: >-
  graphrag-cli-settings-yaml-config（GraphRAG 配置系统）通过 graphrag init 生成 settings.yaml + .env + prompts/ 三件套，支持 ${ENV_VAR} token 替换；CLI 提供 init/index/query/prompt-tune 四个主命令，配置分为模型定义/输入/分块/输出/缓存/向量存储/各 workflow 参数等层级
related: [graphrag-indexing-pipeline-six-phases, graphrag-prompt-tuning-auto-adaptation, graphrag-leiden-clustering-config]
---

GraphRAG 的配置体系围绕 `settings.yaml` + `.env` 环境变量文件展开，通过 `${ENV_VAR}` 语法实现 token 替换，避免在配置文件中硬编码密钥 [^src-1]。

**初始化**：`graphrag init --root [path]` 生成三个产物 [^src-2]：
- `settings.yaml`：全部管线配置
- `.env`：环境变量（如 `GRAPHRAG_API_KEY`）
- `prompts/`：默认 LLM 提示词模板（可被 auto-tuning 覆盖）

**CLI 主命令** [^src-3]：
- `graphrag init` -- 初始化工作空间
- `graphrag index [--method standard|fast]` -- 执行索引管线
- `graphrag query "..." [--method local|global|drift|basic]` -- 查询
- `graphrag prompt-tune` -- 自动提示词适配

**配置层级结构**（关键 section）[^src-4]：

| Section | 职责 |
|---------|------|
| `completion_models` / `embedding_models` | 模型定义（支持多模型非对称配置） |
| `input` | 输入格式(text/csv/json)、存储位置 |
| `chunks` | 分块策略(size/overlap/prepend_metadata) |
| `output` / `update_output_storage` | 输出存储（file/blob/cosmosdb） |
| `cache` | LLM 缓存(json/memory/none) |
| `vector_store` | 向量存储(lancedb/azure_ai_search/cosmosdb) |
| `extract_graph` | 图提取参数(entity_types/max_gleanings) |
| `cluster_graph` | Leiden 聚类参数 |
| `community_reports` | 社区报告生成参数 |
| `local_search` / `global_search` / `drift_search` | 查询参数 |

**模型非对称配置**：可在 `completion_models` 中定义多个模型（如 gpt-4o 用于索引、o1 用于查询），各 workflow 通过 `completion_model_id` 引用不同模型键名 [^src-5]。版本迭代间需执行 `graphrag init --force` 以获取最新配置格式。

## Footnotes

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/yaml.md -- "If a .env file is present along with this config file, then it will be loaded, and the environment variables defined therein will be available for token replacements in your configuration document using ${ENV_VAR} syntax"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/init.md -- "The init command will create the following files: settings.yaml, .env, prompts/"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/get_started.md -- graphrag init / graphrag index / graphrag query 命令示例
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/yaml.md -- 完整配置 section 定义（completion_models, input, chunks, output, cache, vector_store, extract_graph, cluster_graph 等）
[^src-5]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/models.md -- "you can define as many models as you like in the models block of your settings.yaml and reference them by key for every workflow that requires a language model. You could use gpt-4o for indexing and o1 for query"
