# Justification: index-as-navigation

## Extraction rationale
Index-based navigation 是 LLM Wiki 区别于传统 RAG 的关键实现策略。"surprisingly well" 的规模声明是重要的实证数据点。

## Evidence quality
- 有具体规模数据（~100 sources, ~hundreds of pages）
- "surprisingly well" 保留了原文的 hedge 语气
- 与 CLI tools 部分的 qmd 建议形成规模梯度

## Atomicity check
仅覆盖 index.md 作为导航/检索机制及其适用规模。log.md 的功能不在此卡范围。
