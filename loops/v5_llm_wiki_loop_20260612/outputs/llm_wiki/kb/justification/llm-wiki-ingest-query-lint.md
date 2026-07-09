# Justification: llm-wiki-ingest-query-lint

## 为什么成卡
三种操作（Ingest/Query/Lint）构成 LLM Wiki 的运行循环，材料对每种操作的步骤有明确描述。这是模式的动态行为层面，与静态结构（三层架构）互补。

## Evidence basis 选择
practitioner_report: 同上，源自 Karpathy gist 的社区报道。

## 原子性判断
本卡聚焦操作定义与步骤，不包含架构分层（→ llm-wiki-three-layer-architecture）或与 RAG 的对比（→ llm-wiki-vs-rag）。
