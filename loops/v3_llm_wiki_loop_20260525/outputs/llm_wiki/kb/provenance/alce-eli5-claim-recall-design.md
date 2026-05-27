---
schema: accepted_card_provenance.v3
card: ../cards/alce-eli5-claim-recall-design.md
material_id: arxiv-alce
digest_id: digest_arxiv-alce
source_paths:
  - data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
draft_card: ../../drafts/cards/alce-eli5-claim-recall-design.md
draft_provenance: ../../drafts/provenance/alce-eli5-claim-recall-design.md
similarity_result: ../../drafts/similarity/alce-eli5-claim-recall-design.json
comparison_provenance: ../../drafts/comparison/alce-eli5-claim-recall-design.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:06:00+08:00
  gate_notes: 6/6 通过；反 ROUGE 对比表 + 120 sub-claim 校验 + 80% NLI accuracy 全有原文引用；操作含义与已知失败模式齐全。
created_time: 2026-05-26T15:40:00+08:00
edited_time: 2026-05-27T14:06:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-alce/agent_source_bundle.txt` 第 249–264 行（反 ROUGE 论证 + 抽取流程）：

> "We elect not to use ROUGE-L as our main correctness metrics since it does not account for the different ways of expressing the same answer and it can be easily gamed. ... A system can easily achieve high ROUGE-L score by retrieving and returning the top passage from a BM25 index. However, the claims evaluation metric does not reward this approach since the output often lacks different aspects of the answers. ... we leverage the original answers to generate sub-claims ... we use text-davinci-003 to generate the sub-claims. We first manually annotate three question and answer pairs from the original ELI5 training set with 3 sub-claims each. Then, we prompt text-davinci-003 with these pairs as demonstrations."

2. 第 266–270 行（抽取质量人工检验）：

> "We found that 112 out of the 120 (93.33%) sub-claims received a score of 1, meaning that our generated sub-claims are of high quality and faithful to the ground truth. Furthermore, the average number of words in the generated sub-claims is 14 words, and they are typically just one sentence long."

3. 第 273–277 行（NLI accuracy）：

> "Using the human annotations as the ground truth label, we found that the NLI model achieved an accuracy of 80.0%."

4. `tables/eli5_rouge.tex` 第 1962–1967 行（ROUGE vs Claim recall 对比表）；

5. 第 106–110 行（limitations，承认 sub-claim 不全 + NLI 的 partial-support 局限）；

6. `tables/eli5_claims_prompt.tex` 第 1823–1866 行（抽取 prompt verbatim，含 Sunni/Shia / 双相情感 / 声音定位三个 in-context demo）。

## 卡片范围是否成立

本卡补充已有三张 ALCE 卡（三维度/citation NLI/prompting）都未展开的"ELI5 correctness 度量怎么来"：

- 数据全部由附录 §"Generating Claims for ELI5" 与 ELI5 rouge 对比表直接支撑；
- "80% 是 ELI5 correctness 自动评估的上限"是引申，但有 80.0% NLI accuracy 这一硬数字作为依据；
- "±2-3 个点之内可能是 NLI 噪声"是基于 80% accuracy 的经验估计，已在卡片中标注为"可能"。

与已有 ALCE 三卡均不重叠：三维度卡只一笔带过 "ELI5 用 InstructGPT 派生 3 条 sub-claim"，citation NLI 卡只讲 citation NLI，prompting 卡只讲策略选择。本卡是 ELI5 correctness 度量的专卡。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:06:00+08:00
- 检查要点：
  - 不是标题复述：含两步机制 + 反 ROUGE 对比表 + 双人工校验数 + 操作含义 + 失败模式。
  - 知识密度足够：表格 + 公式化定义 + 数字（93.33%/80%/19.1 vs 3.0）+ 边界。
  - 源支撑齐全：每条数字均锁到 `agent_source_bundle.txt` 的具体节与行号。
  - References 与 Footnotes 双章节存在（含四条原文 verbatim）。
  - frontmatter 完整合法，mechanism 类型与正文一致。
  - related 已链 ALCE 系列、ragas、ragchecker、ARES。

## 备注

- 此方法可推广到任何 long-form QA 评估，建议在 v3 evaluation-design 系列里复用。
- comparison 显示与 v2 的 0.05 分数全部来自 `的` 助词同形误中，new_card 决策合理。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/alce-eli5-claim-recall-design.md`
- draft provenance: `../../drafts/provenance/alce-eli5-claim-recall-design.md`
- similarity: `../../drafts/similarity/alce-eli5-claim-recall-design.json`
- comparison provenance: `../../drafts/comparison/alce-eli5-claim-recall-design.md`
