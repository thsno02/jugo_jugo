---
schema: justification_journal.v1
card: ../cards/locomo-benchmark-design.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`
源证据：
- sections/experiment_setup.tex — "The LOCOMO dataset is designed to evaluate long-term conversational memory in dialogue systems. It comprises 10 extended conversations, each containing approximately 600 dialogues and 26000 tokens on average"
- sections/experiment_setup.tex — "These questions are categorized into multiple types: single-hop, multi-hop, temporal, and open-domain."
范围论证：LOCOMO 的四类问题分类（单跳/多跳/时序/开放域）构成了评估长期记忆系统的标准框架，是理解 Mem0 论文所有实验结果的前提条件。该卡片记录基准设计本身，而非在其上的实验结果。
