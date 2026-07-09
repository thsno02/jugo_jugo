---
id: ares-ais-answer-faithfulness-evaluation
title: ARES 在 AIS 归因基准上的幻觉检测
status: draft
card_type: experimental-finding
tags: [answer-faithfulness, hallucination-detection, ais, attribution, wow, cnn-dm]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-ares]
evidence_basis: experimental_paper
justification: ../justification/ares-ais-answer-faithfulness-evaluation.md
canonical_concept: ares-ais-answer-faithfulness-evaluation
aliases: [ARES on AIS, ARES answer faithfulness, ARES hallucination detection]
summary: >-
  ARES 在 AIS 归因基准的 WoW 和 CNN/DM 数据集上评估 answer faithfulness，预测正负分割比例与 ground truth 相差在 2.5 个百分点内（WoW: 0.478 vs 0.458; CNN/DM: 0.835 vs 0.859）。仅用 200 个标注的 human preference validation set。Judge 准确率 WoW 62.5%、CNN/DM 84.0%。证明 ARES 能在真实 RAG 系统中可靠区分忠实与幻觉答案。
related: []
---

ARES 在 AIS (Attributable to Identified Sources) 归因基准上测试 answer faithfulness 评估能力。选择 WoW 和 CNN/DM 数据集（排除涉及表格推理的 ToTTo 和段落摘要的 QRECC）。[^src-1]

结果：ARES 预测的正负分割比例与 ground truth 相差 2.5 个百分点内。WoW 预测 0.478 vs 真实 0.458；CNN/DM 预测 0.835 vs 真实 0.859。[^src-2]

Judge 准确率：WoW 62.5%、CNN/DM 84.0%。Human preference validation set 仅用 200 个标注。[^src-3]

结论：ARES 能在真实系统中可靠区分忠实答案与幻觉/无归因答案。[^src-4]

[^card-1]: [^ref→ares-three-dimensional-rag-evaluation] answer faithfulness 维度
[^card-2]: [^ref→prediction-powered-inference-for-rag-ranking] PPI 校正低精度 judge

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P855-858 -- "we tested ARES on the AIS attribution benchmark...we selected the Wizards of Wikipedia (WoW) and CNN/DM datasets"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P859 -- "ARES can effectively score the AIS datasets, getting within 2.5 accuracy points"
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" Table P841-852 -- "ARES Judge Accuracy 62.5%...84.0%...Human Preference Data Size 200"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P860-861 -- "the ability of ARES to reliably distinguish faithful and hallucinated answers in real-world RAG systems"
