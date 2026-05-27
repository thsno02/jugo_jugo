---
schema: accepted_card_provenance.v3
card: ../cards/lightmem-precompress-and-topic-segmentation.md
material_id: arxiv-lightmem
digest_id: digest_arxiv-lightmem
source_paths:
  - data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt
draft_card: ../../drafts/cards/lightmem-precompress-and-topic-segmentation.md
draft_provenance: ../../drafts/provenance/lightmem-precompress-and-topic-segmentation.md
similarity_result: ../../drafts/similarity/lightmem-precompress-and-topic-segmentation.json
comparison_provenance: ../../drafts/comparison/lightmem-precompress-and-topic-segmentation.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:31:00+08:00
  gate_notes: 6/6 项通过：LLMLingua-2 公式 + 注意力∩相似度切点 + 分段 80% 准确率 + ablation -6.3%/-5.4%。
created_time: 2026-05-26T11:06:00+08:00
edited_time: 2026-05-27T10:31:00+08:00
edited_entity: llm
---

## 源证据

- §3.1（行 780–807）给出预压缩公式与兜底机制：
  > "Following Xia et al., we use LLMLingua-2 as our compression model θ. ... The threshold τ is set to the r-th percentile of retention scores"
  > "$P(\text{retain } x_i \mid \mathbf{x}; \theta) = \mathrm{softmax}(\ell_i)_1$"
- 话题分段公式（行 814–823）：
  > "$\mathcal{B}_1 = \{ k \mid M_{k,k-1} > M_{k-1,k-2}, M_{k,k-1} > M_{k+1,k}, 1 < k < n \}$"
  > "$\mathcal{B}_2 = \{ k \mid \mathrm{sim}(s_{k-1}, s_k) < \tau, 1 \le k < n\}$, $\mathcal{B} = \mathcal{B}_1 \cap \mathcal{B}_2$"
- Appendix Topic Segmentation 细节（行 462–500）：
  > "we mask out the contributions of the first and last three tokens in each sequence and subsequently normalize the remaining attention values. Attention is derived from the higher layers of LLMLingua-2 (layers 8, 9, 10, and 11)."
  > "if a sentence becomes empty after compression, we retain its original uncompressed version; if the token length of a sentence still exceeds the maximum limit, we continue to compress it using the LLMLingua-2 model at a 0.5 compression rate until the token length falls below the threshold."
- Embedding 模型：`all-MiniLM-L6-v2`（行 275）。
- LLMLingua-2 < 2GB 与运行时占用可忽略：行 195–197、622。
- Ablation：行 640。
- 分段准确率 > 80%：行 637。

## 卡片范围是否成立

卡片只综合了论文 §3.1 主体 + Appendix 对话题分段的具体定义；所有数字（80%、6.3%、5.4%、512 token）都按原文引用。"这一层不是装饰，是性能正贡献项"是 ablation 结论的直接转述，未越界。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:31:00+08:00
- 检查要点：
  - 非标题复述：以预压缩子模块 + 话题分段子模块 + 为何在 sensory 层切 + 边界四段实质展开。
  - 知识密度：LLMLingua-2 公式 + 8-11 层 + 首尾 3 token mask + B1∩B2 + ablation 数字。
  - 源支撑：lightmem §3.1 行 780-807 / 814-823 / Appendix 462-500 / 195-197 / 622 / 275 / 637 / 640。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 5 个 v3 draft id。

## 备注

- 与 prompt compression / 与 LLMLingua-2 相关的 v2 卡片可能重叠（v2 当前未发现）。
- 主卡 `lightmem-three-stage-atkinson-shiffrin` 已涵盖了三模块的高层职责，这张卡是 Light1 的细节展开。
- Adoption 阶段观察：v2 候选 token 共享在中文虚词上，无主题重叠。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/lightmem-precompress-and-topic-segmentation.md`
- draft provenance: `../../drafts/provenance/lightmem-precompress-and-topic-segmentation.md`
- similarity: `../../drafts/similarity/lightmem-precompress-and-topic-segmentation.json`
- comparison provenance: `../../drafts/comparison/lightmem-precompress-and-topic-segmentation.md`
