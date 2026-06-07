---
id: graphrag-litellm-model-integration
title: GraphRAG 通过 LiteLLM 支持 100+ 模型的集成策略
status: accepted
card_type: mechanism
tags: [graphrag, litellm, model-provider, structured-output, implementation]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-graphrag]
justification: ../justification/graphrag-litellm-model-integration.md
canonical_concept: graphrag-litellm-model-integration
aliases: [GraphRAG LiteLLM 集成, 多模型支持, GraphRAG model provider]
summary: >-
  graphrag-litellm-model-integration（GraphRAG LiteLLM 集成）使用 LiteLLM 作为模型调用层支持 100+ 模型提供商，要求模型必须支持 JSON schema 结构化输出；配置中 model_provider 对应 LiteLLM 的 "/" 前缀，model 对应后缀；同时提供 retry/rate_limit/metrics 精细控制
related: [graphrag-cli-settings-yaml-config, graphrag-provider-factory-extensibility, graphrag-llm-caching-idempotency]
---

GraphRAG 使用 LiteLLM 作为底层模型调用管理器，实现对 100+ 模型提供商的统一访问 [^src-1]。虽然 GraphRAG 主要在 OpenAI gpt-4 系列上测试和优化，但通过 LiteLLM 可以接入 Gemini、Anthropic、本地模型等。

**关键约束**：所选模型必须支持返回符合 JSON schema 的结构化输出（structured outputs）——这是 GraphRAG 图提取等步骤正确运作的前提 [^src-2]。

**配置映射规则**：LiteLLM 使用 `provider/model` 格式调用模型，在 GraphRAG 配置中拆分为两个字段 [^src-3]：
- `model_provider`：`/` 前的部分（如 openai、gemini、anthropic）
- `model`：`/` 后的部分（如 gpt-4.1、gemini-2.5-flash-lite）

**请求控制机制** [^src-4]：
- `retry`：指数退避重试（max_retries=7, base_delay=2.0, jitter=true）或立即重试
- `rate_limit`：滑动窗口限流（按 requests_per_period 或 tokens_per_period）
- `metrics`：请求指标收集（memory 存储 + log/file 输出）
- `call_args`：每次请求的默认参数（如 temperature、max_completion_tokens）

**o-series 推理模型适配**（v2.2.0+）[^src-5]：
- 响应长度控制从 `max_tokens` 硬约束改为 prompted approach（提示词引导）
- gleaning 的 yes/no 判断从 `logit_bias` 强制改为 prompted approach
- 推理模型的原生 CoT 可能与 GraphRAG 提示词中的手写 CoT 冲突，建议调优提示词

**Proxy 方案**：ollama 或 LiteLLM Proxy Server 可将 HTTP 调用代理到不支持的模型，但常见 JSON 格式问题——模型必须可靠返回 GraphRAG 期望的特定响应格式 [^src-6]。

## Footnotes

[^src-1]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/models.md -- "GraphRAG uses LiteLLM for calling language models. LiteLLM provides support for 100+ models"
[^src-2]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/models.md -- "when choosing a model it must support returning structured outputs adhering to a JSON schema"
[^src-3]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/models.md -- "The model_provider is the portion prior to / while the model is the portion following the /"
[^src-4]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/yaml.md -- retry (exponential_backoff/immediate, max_retries=7), rate_limit (sliding_window, requests_per_period, tokens_per_period), metrics 配置
[^src-5]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/models.md -- "GraphRAG 2.2.0 now supports these models... switched from using max_tokens to use a prompted approach... gleanings switched to prompted approach"
[^src-6]: `data/raw/github_repo/repo-microsoft-graphrag/material_bundle.txt` -- docs/config/models.md -- "we frequently see issues with malformed responses (especially JSON), so if you do this please understand that your model needs to reliably return the specific response formats"
