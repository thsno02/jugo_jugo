---
id: raw-wiki-code-architecture
title: Raw/Wiki/Code 三层架构
status: draft
card_type: architecture
tags: [llm-wiki, architecture, raw, wiki, code, three-layer]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-ss1024ss-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/raw-wiki-code-architecture.md
canonical_concept: raw-wiki-code-architecture
aliases: [raw/wiki/code, 三层架构, three-layer architecture, raw wiki code layers]
summary: >-
  Raw/Wiki/Code 三层架构 (raw-wiki-code-architecture): LLM Wiki 的文件系统结构。
  raw 层存放不可变源材料(PDF/Excel/客户文档)；wiki 层是 LLM 编译产出的 markdown 当前共识，
  持续更新；code 层是从 wiki 生成的执行制品(compiled artifact)而非真相。
  ~100 docs / ~80k tokens 以内 wiki 可单次直读无需 RAG。支持 stale detection 和 delta-compile。
related: [llm-compilation-paradigm, llm-wiki-five-rules]
---

LLM Wiki 定义了一个三层文件系统架构，数据在层间单向流动：[^src-1]

```
raw/  → 不可变源材料（PDF、Excel、客户文档）
wiki/ → LLM 编译产出的 markdown，当前共识，持续更新
code/ → 从 wiki 生成的执行层，是 compiled artifact 而非 truth
```

各层关键约束：
- **raw 层**：immutable，不应放入 Git（binary junk pile）[^src-2]
- **wiki 层**：current consensus，所有决策必须回写此处；~100 docs / ~80k tokens 以内可被 LLM 单次读取（由 `wiki_size_report.py` 监测，GREEN 表示在阈值内）[^src-3]
- **code 层**：generated artifact，地位低于 wiki；不更新 wiki 的代码变更被视为"incomplete work"

配套工具链支持架构运转：`ingest_raw.py`（注册新 raw 文件）、`stale_report.py`（识别需重新编译的内容）、`delta_compile.py --write-drafts`（生成草稿而非覆盖）。[^card-1]

[^src-1]: `data/raw/github_repo/repo-ss1024ss-llm-wiki/repo/README.md` -- "The Idea" P2 -- "raw/ (PDFs, Excel, client docs — immutable source material) ↓ LLM compiles wiki/ (markdown — current consensus, continuously updated) ↓ LLM generates code/ (the execution layer — a compiled artifact, not the truth)"
[^src-2]: `data/raw/github_repo/repo-ss1024ss-llm-wiki/repo/README.md` -- "Don't Do These Things" P1 -- "Don't put raw PDFs/XLSX into Git. That's a binary junk pile, not version control."
[^src-3]: `data/raw/github_repo/repo-ss1024ss-llm-wiki/repo/README.md` -- "The Idea" P3 -- "Wiki before RAG — Under ~100 docs (or ~80k tokens, measured by scripts/wiki_size_report.py), LLM reads directly. No vector DB needed."
[^card-1]: llm-compilation-paradigm — 三层架构是编译范式的物理实现
