---
schema: justification_journal.v1
card: ../cards/lossy-compression-citation-tradeoff.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-alce/agent_source_bundle.txt`
源证据：
- sections/model.tex -- "we propose to provide summaries or snippets of passages instead of the full text...they reduce passage length by 6x on average"
- sections/results.tex -- "such an improvement comes at a cost of citation quality due to the lossy compression"
- sections/results.tex -- "Combining Interact with Summ/Snippet does not bring improvement"
范围论证：有损压缩策略及其引用权衡是 ALCE 论文在提示策略方面的核心发现，涉及上下文窗口限制下的设计取舍。这一机制独立于其他发现，适合单独成卡。
