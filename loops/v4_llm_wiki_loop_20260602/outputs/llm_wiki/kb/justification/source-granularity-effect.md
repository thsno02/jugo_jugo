---
schema: justification_journal.v1
card: ../cards/source-granularity-effect.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/hacker_news/hacker-news-original-thread/text.txt`
源证据：
- vbarsoum 评论 — "The naive version (each book as 1 file) produced exactly the slop... But splitting into chapter-level files and recompiling changed the output categorically. Same model, same prompts — the only variable was source granularity."
- vbarsoum 评论 — "173K words of output from 155K input. It's not compression — it's synthesis."
范围论证：源粒度效应是一个可操作的实证发现，独立于双受众制品概念（后者描述谁使用 wiki，本卡描述如何构建高质量的 raw sources 层）。虽然证据来自单一实现者，但其对照实验设计（唯一变量是粒度）使其成为对 three-layer-architecture 实践层面的重要补充。
