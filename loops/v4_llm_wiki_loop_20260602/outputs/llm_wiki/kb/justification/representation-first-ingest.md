---
schema: justification_journal.v1
card: ../cards/representation-first-ingest.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
源证据：
- "What 0.4.4 Implements" — "This release makes the runtime representation-first and explicitly multimodal"
- "Multimodal Ingest Model" — "PDFs and images use a representation-first path: inspect the asset with kb_get_raw_asset ... compile the final source note only after the representation trail is present"
- "Multimodal Ingest Model" — "The runtime intentionally does not perform OCR or vision itself. Instead, it gives agents a canonical place to store those intermediate artifacts and then validates that the final wiki pages stay grounded in them."
- "What 0.4.4 Implements" — "compile-readiness tracking with ready, partial, and needs_representation"
范围论证：本卡聚焦于双路径摄入机制及其背后的「表示先行」设计原则，与已有的 ingest-operation 卡（描述 Karpathy 原始工作流中的摄入概念）不同，本卡描述的是运行时实现中针对多模态资产的具体技术机制。编译就绪状态追踪作为该机制的组成部分一并收录，避免为三个状态值单独建卡。
