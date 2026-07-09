---
id: llm-wiki-two-step-cot-ingest
title: LLM Wiki 两步 Chain-of-Thought 摄入
status: accepted
card_type: technique
tags:
- ingest
- chain-of-thought
- llm-wiki
- two-step
- analysis-generation
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-nashsu-llm-wiki
evidence_basis: code_implementation
justification: ../justification/llm-wiki-two-step-cot-ingest.md
canonical_concept: llm-wiki-two-step-cot-ingest
aliases:
- Two-Step Chain-of-Thought Ingest
- 两步摄入
- two-step ingest
- CoT ingest
- 分析-生成两步法
summary: LLM Wiki 两步 Chain-of-Thought 摄入（Two-Step CoT Ingest）将原来的单步读写拆为两次顺序 LLM 调用：
  Step 1 Analysis（分析：提取实体/概念/论点、联系、矛盾、结构建议）→ Step 2 Generation（生成：wiki 页面 + index/log/overview
  更新 + review items）。 附加 SHA256 增量缓存、持久队列、文件夹导入、auto-watch 等增强。
related:
- llm-kb-ingest-operation
- llm-wiki-ingestion-workflow
- ingest-operation
---

LLM Wiki 将 Karpathy 原始设计中的单步摄入（LLM 同时读取和写入）拆分为两次顺序 LLM 调用，以显著提升生成质量：

**Step 1 — Analysis（分析）**：LLM 读取源文件，输出结构化分析：
- 关键实体、概念、论点
- 与现有 wiki 内容的联系
- 与现有知识的矛盾和张力
- wiki 结构建议

**Step 2 — Generation（生成）**：LLM 接收分析结果，生成 wiki 文件：
- 带 frontmatter 的源摘要页（type, title, sources[]）
- 实体页、概念页（含交叉引用）
- 更新 index.md、log.md、overview.md
- 供人类审核的 review items
- Deep Research 的搜索查询 [^src-1]

附加的摄入增强包括：SHA256 增量缓存（跳过未变文件）、持久摄入队列（崩溃恢复 + 自动重试最多 3 次）、文件夹递归导入（路径作为分类提示）、源文件夹 auto-watch。[^src-2] [^card-1]

[^src-1]: `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` -- "3. Two-Step Chain-of-Thought Ingest" P98-115 -- "We split it into two sequential LLM calls for significantly better quality"
[^src-2]: `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` -- "Additional ingest enhancements" P117-128 -- "SHA256 incremental cache — source file content is hashed before ingest; unchanged files are skipped automatically"
[^card-1]: 参见 [[llm-wiki-three-layer-architecture]] 了解摄入结果写入的 wiki 层结构
