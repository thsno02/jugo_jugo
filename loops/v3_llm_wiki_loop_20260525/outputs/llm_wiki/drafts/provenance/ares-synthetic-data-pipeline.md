---
schema: draft_card_provenance.v3
draft_card: ../cards/ares-synthetic-data-pipeline.md
material_id: arxiv-ares
digest_id: digest_arxiv-ares
source_paths:
  - data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-26T11:05:00+08:00
edited_entity: llm
---

## 源证据

- `methods.tex` L700-708：合成 query/answer 用 FLAN-T5-XXL 在 in-domain passage 上少样本 prompt，并用 retriever 过滤"拿不回原 passage"的 query。
- `methods.tex` L713-719：双路负例生成策略（weak / strong）的逐字定义。
- `methods.tex` L693-694：所需输入 = in-domain passage set + 150 标注 + 5 个 few-shot 样本。
- `appendix.tex` L298-303：判官 fine-tune 超参（DeBERTa-v3-Large + 单 linear head + dropout 0.1 + lr 5e-6 + batch 32 + linear warmup/decay）。
- `methods.tex` L738：早停策略 "stopping when we have three epochs with no improvement in loss"。
- `limitations.tex` L668-674：150–300 验证集需求 + 32GB GPU 门槛。
- `experiments.tex` L554-555：KILT/SuperGLUE 不评 A.F. 因为没有真实 hallucination 标签。
- 表 `tab:ppi_count`（L189-199）：100-150 是 PPI 校准集的有效下界。

## 卡片范围是否成立

卡片只覆盖"合成数据生成 + 判官 fine-tune"这一段，把 PPI 部分留给姊妹卡 `ares-ppi-confidence-bound`。卡内的关键主张都能在源材料里找到原文：

- 双负例生成的具体定义来自论文 enumerate 列表。
- "weak 和 strong 各占一半"对应 `methods.tex` L721 `"the number of negatives generated equals the number of positives generated"`（结合上下文等比分配的解读）。
- 硬件门槛和 PPI 校准集下界都来自 Limitations / 附录表。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 卡片潜在重叠：如果 v2 已有"用 LLM 当 judge"通用卡，可在 comparison_provenance 阶段标注本卡范围更狭窄（合成数据 + DeBERTa 路径）。
