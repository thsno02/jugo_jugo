---
id: llm-wiki-multi-provider-support
title: 多 LLM 提供商支持
status: draft
card_type: feature
tags: [llm-wiki, provider, api, ollama, i18n]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
evidence_basis: documentation
justification: ../justification/llm-wiki-multi-provider-support.md
canonical_concept: llm-wiki-multi-provider-support
aliases: [multi-provider, 多提供商, LLM provider support]
summary: >-
  支持 10 种 LLM 提供商：Anthropic、Anthropic Compatible（Coding Plan）、Google Gemini、
  OpenAI、DeepSeek、Kimi、GLM、Ollama、OpenRouter、自定义端点。Ollama 本地免 API key。
  动态模型列表从提供商 API 实时获取。5xx/429 自动指数退避重试（最多 2 次）。
  UI 和 Wiki 输出语言独立配置，8 种语言，269+ UI 字段翻译。
related: [llm-wiki-model-recommendations, parallel-page-generation]
---

该插件支持 10 种 LLM 提供商：Anthropic、Anthropic Compatible（Coding Plan）、Google Gemini、OpenAI、DeepSeek、Kimi、GLM、Ollama、OpenRouter、自定义端点。Ollama 支持本地运行无需 API key。[^src-1]

工程特征：
- 动态模型列表：从提供商 API 实时获取可用模型
- 5xx/429 错误自动指数退避重试（最多 2 次）
- Wiki 输出语言与 UI 语言独立配置，支持 8 种语言（EN/ZH/JA/KO/DE/FR/ES/PT）
- 269+ UI 字段完整翻译，使用自然本地化表达 [^src-2]

[^src-1]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Configure" P1 -- "Pick a provider from the dropdown (Anthropic, Anthropic Compatible, Google Gemini, OpenAI, DeepSeek, Kimi, GLM, Ollama, OpenRouter, or custom)"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/markdown.md` -- "Features" P1 -- "Full UI Internationalization — Plugin UI supports 8 languages (EN/ZH/JA/KO/DE/FR/ES/PT), 269+ UI fields fully translated with natural local expressions"
