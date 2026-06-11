---
schema: justification_journal.v1
card: ../cards/latent-reasoning-continuous-thought.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：Mode A extraction from structured source
来源：`data/raw/webpage/complete-tech-live-frontier/markdown.md`
源证据：
- 第9-10行 — "Feed hidden states back as input embeddings instead of decoding to tokens. The model reasons silently in continuous vector space, holding multiple reasoning paths in superposition."
- 第10行 — "Headline number from Hao et al.'s Coconut (ICLR 2025): 97.0% on planning tasks via emergent BFS, vs. 77.5% for chain-of-thought on the same tasks."
- 第10行 — "Pause Tokens, iCoT, SoftCoT, Thinking States, and the Superposition Theory paper round out this thread."
范围论证：现有卡片中 production-scale-wiki-reference 和 literature-velocity-argument 提及「潜空间推理」仅作为 BTTB wiki 跟踪的研究领域名称，未描述该领域的核心技术机制（隐状态反馈）和量化结果（97.0% vs 77.5%）。Coconut 的 emergent BFS 结果是该源中最具体的量化指标之一，值得作为独立概念卡记录。
