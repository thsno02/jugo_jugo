---
schema: accepted_card_provenance.v3
card: ../cards/graphrag-adaptive-benchmark-via-personas.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
draft_card: ../../drafts/cards/graphrag-adaptive-benchmark-via-personas.md
draft_provenance: ../../drafts/provenance/graphrag-adaptive-benchmark-via-personas.md
similarity_result: ../../drafts/similarity/graphrag-adaptive-benchmark-via-personas.json
comparison_provenance: ../../drafts/comparison/graphrag-adaptive-benchmark-via-personas.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:01:00+08:00
  gate_notes: 6/6 项通过：三块协议 + 四指标 + 一致率数字均有具体引用与行号锚定。
created_time: 2026-05-26T11:03:00+08:00
edited_time: 2026-05-27T10:01:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:01:00+08:00
- 检查要点：
  - 非标题复述：以三块协议（adaptive gen / LLM-judge / claim-based 交叉验证）展开。
  - 知识密度：K/N/M 配置、四维指标、反向控制原理、一致率 78%/69-70% 全部给出。
  - 源支撑：source_ids=[arxiv-graphrag]；正文 References 节明列行号。
  - References / Footnotes 存在：含 §3.2/§3.3/§3.4 行号与多段原文引用。
  - frontmatter 完整。
  - related 字段已填充 6 个 sibling。

## 备注

- 与 GraphRAG 方法卡片正交，可单独被引用为"LLM-as-judge 协议"模板。
- 与 v2 中关于 LLM-as-judge / RAG 评测的卡片可能重叠。
- Adoption 阶段观察：comparison 三个 v2 候选 jaccard ≤ 0.0556，仅靠「生成」一词同形，无语义重合，无 fusion 必要。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/graphrag-adaptive-benchmark-via-personas.md`
- draft provenance: `../../drafts/provenance/graphrag-adaptive-benchmark-via-personas.md`
- similarity: `../../drafts/similarity/graphrag-adaptive-benchmark-via-personas.json`
- comparison provenance: `../../drafts/comparison/graphrag-adaptive-benchmark-via-personas.md`
