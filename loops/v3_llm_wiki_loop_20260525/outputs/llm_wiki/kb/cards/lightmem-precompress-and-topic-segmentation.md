---
id: lightmem-precompress-and-topic-segmentation
title: LightMem 的感觉记忆——LLMLingua-2 预压缩 + 注意力∩相似度的话题分段
status: accepted
card_type: mechanism
tags: [#lightmem, #prompt-compression, #topic-segmentation, #llmlingua-2]
created_time: 2026-05-26T11:06:00+08:00
edited_time: 2026-05-27T10:31:00+08:00
edited_entity: llm
source_ids: [arxiv-lightmem]
provenance_card: ../provenance/lightmem-precompress-and-topic-segmentation.md
aliases: ["Light1 sensory memory", "LightMem pre-compression"]
related: [lightmem-three-stage-atkinson-shiffrin, lightmem-light2-topic-aware-stm, lightmem-complexity-formula, lightmem-sleep-time-offline-parallel-update, memory-as-metabolism-contextualize-depth-fitted]
---

LightMem 的第一层（Light1）不是"memory storage"，而是一个 *预过滤器*——把原始对话回合压缩成几条精炼且按主题分组的小段，再丢给上层的 STM。这一层由两个子模块串联完成，关键技术细节如下。

**预压缩子模块（pre-compressing）：**

- 模型：LLMLingua-2（默认）——一个 BERT 类双向编码器，token 级二分类（"retain" / "discard"）。需要 < 2GB GPU 显存，加入流水线后延迟可忽略。
- 评分：对每个 token 计算 retain 概率 $P(\text{retain}\ x_i\mid \mathbf{x};\theta) = \mathrm{softmax}(\ell_i)_1$；
- 阈值：动态地取整段 token 评分的第 r 分位数 τ，保留得分 > τ 的 token，最终留下比例 r；
- 兜底：若一句压缩后变空，回退到未压缩原句；若仍超 512 token（LLMLingua-2 输入上限），再以 r=0.5 递归压缩；
- 可替换：也可以换成生成式 LLM，用 cross-entropy 替代二分类，留下"高条件熵 / 高信息量"的 token。

**话题分段子模块（topic segmentation）：**

只在感觉 buffer 满（默认 512 token）时触发一次，输出一组分段边界 $\mathcal{B} = \mathcal{B}_1 \cap \mathcal{B}_2$：

- $\mathcal{B}_1$：在 turn 级注意力矩阵 $M$ 的 *次对角* 序列 $\{M_{k,k-1}\}$ 上找局部极大值。注意力来自 LLMLingua-2 高层（8–11 层）取均值；为防"attention sink"，每序列首尾各 3 个 token 被 mask 掉再 normalize。
- $\mathcal{B}_2$：用 embedding model（`all-MiniLM-L6-v2`）计算相邻 turn 余弦相似度，低于阈值 τ 的位置纳入。
- 二者取交集，定为真正的主题切点。论文 ablation 显示这种 hybrid 法比"只 attention"或"只 similarity"准确率高，整体 > 80%（LongMemEval 上把 session 自然边界当 ground truth）。

**为什么要在 sensory 层就切话题：**

- 后续 STM 的 `f_sum` 把整段 STM 一次性总结成多条记忆条目；如果输入混了多个 topic，summary 会把语义"搅在一起"，导致下游检索召回错误。
- 同时切得越准，STM 累计 token 增长越慢，调用 `f_sum` 的频率就越低——直接对接 LightMem 的复杂度优势（API 调用从 N 降到 Nr^x T/th）。

**误用与边界：**

- LLMLingua-2 输入 ≤ 512 token，所以 assistant 长回复被排除在 attention 矩阵之外，分段只用 user 句子；这是论文显式的"为了实用做的妥协"。
- 删除 topic segmentation 这一子模块在 ablation 里 *效率* 略升但 accuracy 掉 6.3%（GPT）/ 5.4%（Qwen），说明这一层不是装饰，是性能正贡献项。

## References

- §3.1 Light1（`data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt`，行 773–828），其中预压缩公式见行 781–807、话题分段公式见行 814–823。
- Appendix `\subsection{Topic Segmentation}`（行 462–500）给出注意力矩阵构造、首尾 3 token 屏蔽、8–11 层取平均、局部峰值切割等细节。
- Pre-compressor 选择与开销说明：行 618–622、195–197。
- Ablation（去掉 topic seg 后 GPT -6.3% / Qwen -5.4%）：行 638–641。

## Footnotes

- 公式 $P(\text{retain}\ x_i\mid \mathbf{x};\theta) = \mathrm{softmax}(\ell_i)_1$ 见行 786–790。
- "if a sentence becomes empty after compression, we retain its original uncompressed version" 见行 470。
- 首尾 3 token mask：行 470—"we mask out the contributions of the first and last three tokens in each sequence and subsequently normalize the remaining attention values."
- 边界交集 $\mathcal{B} = \mathcal{B}_1 \cap \mathcal{B}_2$ 见行 822。
- "absolute accuracy exceeding 80%" 见行 637。
- "removing the topic segmentation submodule slightly improves efficiency but significantly harms accuracy, causing a 6.3% drop for GPT and 5.4% for Qwen"——行 640。
