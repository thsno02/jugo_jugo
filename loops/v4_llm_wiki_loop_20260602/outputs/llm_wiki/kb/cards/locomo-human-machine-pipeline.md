---
id: locomo-human-machine-pipeline
title: LoCoMo LLM 生成+人工编辑的对话数据管线
status: accepted
card_type: mechanism
tags: [data-pipeline, human-machine, dialogue-generation, quality-control, synthetic-data]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/locomo-human-machine-pipeline.md
canonical_concept: locomo-human-machine-pipeline
aliases: [LoCoMo 数据管线, human-machine dialogue generation pipeline]
summary: >-
  locomo-human-machine-pipeline（LoCoMo 数据管线, human-machine dialogue generation pipeline）用 GPT-3.5-turbo 双代理对话生成+人工标注者编辑 15% 轮次、替换 19% 图片以确保长程一致性，生成 50 段超长期多模态对话，是 LLM 合成+人工质控的混合数据构建范式
related: [locomo-benchmark, temporal-event-graph-grounding, locomo-reflect-respond-architecture]
---

LoCoMo 的数据构建采用"机器生成 + 人工编辑"的混合管线，平衡了大规模生成效率与数据质量[^src-1]。

**机器生成阶段**：两个虚拟代理 $\mathcal{L}_1$ 和 $\mathcal{L}_2$ 各以 GPT-3.5-turbo 为基础，被赋予独立的人设（从 MSC 数据集的 4-5 句初始人设扩展而来）和时序事件图[^src-2]。代理通过反思-回应机制和图像分享/反应功能进行多模态对话。图像通过以下流程生成：LLM 生成描述 -> 关键词提取 -> 网络搜索 -> 图像选择；图像反应则通过 BLIP-2 生成描述后由 LLM 生成回应[^src-3]。

**人工编辑阶段**：人工标注者负责三项任务：(1) 编辑对话以消除长程不一致性；(2) 移除或替换不相关图片；(3) 验证并编辑对话与事件图的对齐。最终统计显示，标注者编辑了近 15% 的对话轮次，移除或替换了约 19% 的图片[^src-4]。

论文承认此管线的局限：合成数据可能无法完全反映真实在线对话的细微差别，但认为这是避免收集年级跨度真实对话所涉及的后勤和法律复杂性的务实选择[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 1" -- "a human-machine pipeline to generate high-quality, very long-term dialogues by leveraging LLM-based agent architectures"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3" -- "We create two virtual agents, named L_1 and L_2, each initialized with a LLM M (i.e., gpt-3.5-turbo)"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.3" -- "image sharing function... (1) Generate a caption (2) Convert caption into keywords (3) Use keywords to find an image through web search (4) Share the chosen image"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.4" -- "annotators edited nearly 15% of the dialog turns and removed or substituted approx. 19% images"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 8 Limitations" -- "We pursued this method... to avoid the logistical and legal complexities of collecting very long-term real-world conversations at scale"
