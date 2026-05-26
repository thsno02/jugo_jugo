---
schema: draft_card_provenance.v3
draft_card: ../cards/graphrag-adaptive-benchmark-via-personas.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
created_time: 2026-05-26T11:03:00+08:00
edited_time: 2026-05-26T11:03:00+08:00
edited_entity: llm
---

## 源证据

- §3.2 Algorithm 1（行 873–890）按 K (personas) × N (tasks per persona) × M (questions per pair) 三层组合生成问题；K=M=N=5、125 题（行 894）。
- §3.2 的"避免直接从语料生成问题"动机（行 741–743）：
  > "in order to produce a fair evaluation, our method avoids generating the questions directly from the corpus itself."
- §3.3 给出四指标的定义（行 906–910）以及 directness 作为反向控制项（行 912–915）：
  > "Since directness is effectively in opposition to comprehensiveness and diversity, we would not expect any method to win across all four criteria."
- §3.4 + Experiment 2 引入 Claimify（行 964–966）：
  > "To extract factual claims, we used Claimify ... After removing duplicate claims from each answer, we extracted 47,075 unique claims, with an average of 31 claims per answer."
- 两套度量交叉验证（行 1013）：
  > "the aggregated LLM label matched the claim-based label in 78% of pairwise comparisons for comprehensiveness and 69-70% for diversity (across all distance thresholds), indicating moderately strong alignment."
- LLM-judge 多副本平均：
  > "we run each comparison with multiple replicates and average the results across replicates and questions."（行 919）

## 卡片范围是否成立

卡片把论文 §3.2、§3.3、§3.4、Experiment 2 的设定整合成一套"可复用评测协议"。所有数字均来自论文原文。把它讲成"操作含义"是合理的——论文本身在 §3 把这套协议作为方法贡献之一明示（"a novel application of the LLM-as-a-judge technique"，行 701）。

## 发表门控结果

本轮未运行。

## 备注

- 与 GraphRAG 方法卡片正交，可单独被引用为"LLM-as-judge 协议"模板。
- 与 v2 中关于 LLM-as-judge / RAG 评测的卡片可能重叠。
