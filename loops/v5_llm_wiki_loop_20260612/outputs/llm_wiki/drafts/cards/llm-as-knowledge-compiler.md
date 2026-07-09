---
id: llm-as-knowledge-compiler
title: LLM 作为知识编译器
status: draft
card_type: conceptual-metaphor
tags: [knowledge-management, llm-compiler, paradigm-shift, karpathy]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
evidence_basis: practitioner_report
justification: ../justification/llm-as-knowledge-compiler.md
canonical_concept: llm-as-knowledge-compiler
aliases: [LLM compiler, LLM をコンパイラとして使う, 知識のコンパイル, kb-compile]
summary: >-
  Karpathy 提案的核心隐喻: 将 LLM 视为知识编译器, 输入 raw documents 输出结构化 wiki。不是让 LLM 仅写代码, 而是让其承担知识整理/结构化/保守(维护)。生のドキュメントを LLM に渡して構造化された wiki を「コンパイル」する。llm-as-knowledge-compiler コンパイラ 編译
related: []
---

Karpathy LLM Knowledge Base 提案的核心隐喻是"LLM 作为编译器" [^src-1]:

- **输入**: 生のドキュメント(raw documents)
- **输出**: 構造化された Markdown の wiki
- **编译过程**: 读取 → 理解 → 整理 → 结构化 → 永续化

这是一种发想转换(パラダイムシフト): 不仅让 LLM 写代码, 更让其承担知识的整理/結構化/保守。LLM 的角色从"回答者"扩展为"知识基础设施的维护者" [^src-2]。

作者在实装中直接以 `/kb-compile` 命名其编译命令, 体现了对此隐喻的采纳 [^card-1]。

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "LLM にナレッジの「保守」を任せる" P10 -- "端的に言えば、生のドキュメントを LLM に渡して、構造化された Markdown の wiki を「コンパイル」してもらうというアイデアです。"
[^src-2]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "まとめ" P61 -- "Karpathy 氏のポストの核心は、「LLM をコンパイラとして使う」という発想の転換だと思います。コードを書かせるだけでなく、知識の整理・構造化・保守を任せる。"
[^card-1]: 参见 [kb-compile-implementation] — 作者具体实装
