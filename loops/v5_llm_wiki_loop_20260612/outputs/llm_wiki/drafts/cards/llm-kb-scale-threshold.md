---
id: llm-kb-scale-threshold
title: LLM KB 适用规模阈值
status: draft
card_type: boundary-condition
tags: [knowledge-management, scalability, llm-kb, rag, threshold]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
evidence_basis: practitioner_report
justification: ../justification/llm-kb-scale-threshold.md
canonical_concept: llm-kb-scale-threshold
aliases: [規模の閾値, small scale, ~100 articles, ~400K words]
summary: >-
  Karpathy 报告 LLM Knowledge Base 在 ~100 articles / ~400K words 规模下 LLM 自维护 index+summary 可行, 不必 fancy RAG。但材料指出数千件/数百万語时可能需要补充机制。当前验证仅限 small scale。llm-kb-scale-threshold 規模 閾値 スケール
related: []
---

Karpathy 明确将 LLM KB 的验证范围限定为"~small scale" [^src-1]:

- **已验证规模**: ~100 articles, ~400K words (约 40 万語)
- **该规模下表现**: LLM 自动维护 index files + brief summaries 效果良好, 无需 fancy RAG
- **潜在上限**: 作者指出 "ドキュメントが数千件、数百万語になると話は変わってくるかもしれません" [^src-2]

这暗示 LLM KB 模式存在规模天花板, 超出后可能需要向量检索等补充手段。作者自身加入 Mem0 + pgvector 的实装选择, 据材料推测部分源于对规模扩展的预防 [^card-1]。

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "RAG とどう違うのか" P31 -- "ただし、これは規模が ~100 記事、~400K words（約 40 万語）という比較的小さなスケールでの話です。"
[^src-2]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "RAG とどう違うのか" P31 -- "ドキュメントが数千件、数百万語になると話は変わってくるかもしれません。"
[^card-1]: 参见 [kb-compile-implementation] — 作者加入 Mem0 + pgvector 作为检索层补充
