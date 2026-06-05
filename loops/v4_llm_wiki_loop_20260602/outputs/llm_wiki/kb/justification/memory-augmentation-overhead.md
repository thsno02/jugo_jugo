---
schema: justification_journal.v1
card: ../cards/memory-augmentation-overhead.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-lightmem/text.txt`
源证据：
- Abstract -- "Large Language Models (LLMs) struggle to effectively leverage historical interaction information in dynamic and complex environments"
- Abstract -- "Memory systems enable LLMs to move beyond stateless interactions by introducing persistent information storage, retrieval, and utilization mechanisms"
- Abstract -- "existing memory systems often introduce substantial time and computational overhead"
- Abstract -- "reducing total token usage by up to 38x / 20.9x and API calls by up to 30x / 55.5x"
范围论证：记忆系统开销问题是 LightMem 论文的出发点动机，也是记忆增强生成领域的核心挑战。该问题独立于任何具体解决方案（如三阶段架构），构成一个可复用的问题定义卡片。论文通过基线对比数据从侧面量化了该问题的严重程度。
