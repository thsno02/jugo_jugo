---
schema: draft_card_provenance.v3
draft_card: ../cards/poisonedrag-baselines-isolate-two-conditions.md
material_id: arxiv-poisonedrag
digest_id: digest_arxiv-poisonedrag
source_paths:
  - data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt
created_time: 2026-05-26T11:46:00+08:00
edited_time: 2026-05-26T11:46:00+08:00
edited_entity: llm
---

## 源证据

- L1221–1244：*"Naive Attack ... If we view $Q$ as the malicious text, it will likely be retrieved. We compare with this attack to demonstrate that the generation condition is necessary ..."*；*"Corpus Poisoning Attack ... this attack is similar to PoisonedRAG (white-box) when PoisonedRAG uses $S$ alone as the malicious text"*；*"GCG Attack ... we view the optimized adversarial text as a malicious text and inject it into the knowledge database. Our results show that GCG achieves a very low ASR ... The reason is that it cannot achieve the retrieval condition."*；*"Disinformation Attack ... we view the crafted $I$ as a malicious text, i.e., $P=I$. This baseline can be viewed as a variant of PoisonedRAG."*
- L1332–1354：基线表 ASR / F1（NQ / HotpotQA / MS-MARCO）。
- L1403–1404：*"those baselines are not designed to simultaneously achieve retrieval and generation conditions, resulting in sub-optimal performance."*
- L110–151：附录中把 GCG 适配到 RAG 的具体例子——明确把 context 初始化为 40 个 "!"，优化目标是让 LLM 输出 target answer，**没有 retrieval 项**。

## 卡片范围是否成立

本卡是"distinction"型，专门聚焦 5 个基线如何分别证伪两条件之一，所有 ASR / F1 数字、每个基线为什么失败的解释都来自论文 §"Compared baselines" 与 §"Main Results" 的对应段落。表格中"丢掉的条件"一列是对论文论述的提炼（论文原文用"cannot achieve retrieval/generation condition"的句式说明同样意思）。"prompt injection 在 LLM 抗指令时偶失"是依据论文 §Background §3.2 中提到的指令检测可被识别的论述合理延伸；不是新主张。

## 发表门控结果

本轮未运行。

## 备注

- 与既有卡 `poisonedrag-retrieval-generation-two-conditions` 紧密配对：那张是两条件的**正向**机制，本卡是**反证**——通过 5 个基线分别去掉一个条件来证明缺一不可。
- v2 阶段若有"RAG 攻击对比 / 基线选择"元卡，应链接本卡而非重写。
