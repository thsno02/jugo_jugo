---
id: lightmem-attention-topic-segmentation
title: LightMem 注意力-相似度混合主题分割
status: accepted
card_type: mechanism
tags:
- topic-segmentation
- attention-matrix
- semantic-similarity
- chunking
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-lightmem
evidence_basis: experimental_paper
justification: ../justification/lightmem-attention-topic-segmentation.md
canonical_concept: lightmem-attention-topic-segmentation
aliases:
- Topic Segmentation Submodule
- 主题分割子模块
- hybrid topic segmentation
- attention-based boundary detection
summary: LightMem Light1 的主题分割子模块通过注意力矩阵和语义相似度的交集确定主题边界。使用 LLMLingua-2 高层（8-11层）注意力构建 turn-level 注意力矩阵 M，识别相邻句子注意力序列 {M_{k,k-1}} 中的局部峰值作为注意力边界集 B1；同时计算相邻 turn 的 embedding 语义相似度，低于阈值 tau 的位置构成相似度边界集 B2；最终边界为
  B = B1 交 B2。在 LongMemEval 上 50% 压缩率下分割准确率超 80%。消融实验表明移除该模块导致 GPT 准确率下降 6.3%、Qwen 下降 5.4%。
related:
- lightmem-pre-compression-sensory-memory
- lightmem-three-stage-architecture
---

LightMem 的主题分割子模块（Light1 第二部分）在感知记忆 buffer 填满时触发，将压缩后的对话按语义主题分组，为后续 STM summarization 提供更有意义的输入单元。

**注意力边界检测（B1）**：从 LLMLingua-2 的第 8-11 层提取 token 级注意力，聚合为 turn-level 矩阵 M。对子对角线序列 {M_{k,k-1}}（相邻句间注意力），若某位置 k 的值同时大于其前后位置，即为局部峰值——该句标记为新主题的起点。原理是：主题转换时，新主题首句对所有先前句子的整体注意力较低，反映出旧主题到新主题的明确过渡。

**相似度验证（B2）**：使用 embedding 模型（all-MiniLM-L6-v2）计算 B1 中候选边界附近相邻 turn 的语义相似度，仅保留相似度低于阈值的边界，缓解注意力汇聚和稀释问题。

**实现细节**：仅提取用户句子（更简洁且主题一致性高）；屏蔽首尾各 3 个 token 以减少 attention sink 影响；跨层平均获得更鲁棒的分数。[^src-1] [^src-2]

[^src-1]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Topic Segmentation Submodule" P809-828 -- "We define the final segmentation boundaries as the intersection of attention-based boundaries B1 and similarity-based boundaries B2"
[^src-2]: `data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt` -- "Appendix: Topic Segmentation" P462-499 -- "We extract only the user sentences... mask out the contributions of the first and last three tokens... Attention is derived from the higher layers of LLMLingua-2 (layers 8, 9, 10, and 11)"
