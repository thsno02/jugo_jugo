---
id: graphrag-self-reflection-gleaning
title: GraphRAG 自我反思拾遗实体提取技术
status: accepted
card_type: mechanism
tags: [graphrag, entity-extraction, self-reflection, gleaning, prompt-engineering]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
justification: ../justification/graphrag-self-reflection-gleaning.md
canonical_concept: graphrag-self-reflection-gleaning
aliases: [gleaning, 拾遗提取, self-reflection entity extraction, 自反射实体提取]
summary: >-
  graphrag-self-reflection-gleaning（gleaning / 拾遗提取）通过将已提取实体回馈给 LLM 并用 logit bias 强制评估完整性，迭代"拾遗"遗漏实体，使大 chunk 下的实体提取量可接近小 chunk 水平（600 token chunk + 3 次迭代从约 9k 增至约 27k 实体引用）
related: [graphrag-global-sensemaking, chunk-size-tradeoff]
---

GraphRAG 在实体提取阶段采用自我反思（self-reflection）技术来弥补大 chunk 尺寸下 LLM 提取实体数量的下降。论文发现，使用 GPT-4 时，chunk 尺寸从 600 token 增加到 2400 token 时提取的实体引用数量几乎减半 [^src-1]。

拾遗（gleaning）过程如下：实体从某个 chunk 中提取后，已提取实体被回馈给 LLM，提示它"拾遗"可能遗漏的实体。这是一个多阶段过程：首先使用 logit bias 为 100 强制 LLM 做出 yes/no 判断——是否所有实体都已提取。如果 LLM 回答有遗漏，则用一个延续提示"MANY entities were missed in the last extraction"来鼓励 LLM 检测这些遗漏实体 [^src-2]。

在 HotPotQA 数据集上的实验表明，该方法显著有效：使用 600 token chunk 尺寸，0 次自我反思检测到约 9,348 个实体引用，1 次后增至约 15,976，2 次后约 19,491，3 次后达到约 27,240 [^src-3]。

该方法允许使用更大的 chunk 尺寸（减少 LLM 调用成本）而不损失提取质量，也不会引入强制噪声 [^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Appendix A.2 (appendix.tex) -- "GPT-4 extracted almost twice as many entity references when the chunk size was 600 tokens than when it was 2400"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Appendix A.2 (appendix.tex) -- "we first ask the LLM to assess whether all entities were extracted, using a logit bias of 100 to force a yes/no decision. If the LLM responds that entities were missed, then a continuation indicating that 'MANY entities were missed in the last extraction' encourages the LLM to detect these missing entities."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- self_reflection_figure.tex -- 600 chunk size coordinates: (0, 9348), (1, 15976), (2, 19491), (3, 27240)
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- Appendix A.2 (appendix.tex) -- "This approach allows us to use larger chunk sizes without a drop in quality or the forced introduction of noise."
