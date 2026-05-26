---
schema: comparison_provenance.v3
draft_card: ../cards/wicer-targeted-vs-random-pinning-ablation.md
draft_provenance: ../provenance/wicer-targeted-vs-random-pinning-ablation.md
similarity_result: ../similarity/wicer-targeted-vs-random-pinning-ablation.json
existing_cards:
  - card_id: raw-sources-readonly-source-of-truth
    card_path: llm_wiki/kb/cards/raw-sources-readonly-source-of-truth.md
    score: 0.0667
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0625
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

Top 3 score = 0 即无 token 共享，被列入仅是 top 3 占位。Top 1 与 Top 2 都在 0.06+，共享 token 大概是中文虚词或"wiki"，与 WiCER / pinning / diagnosis / CEGAR / RepLiQA 等关键概念无对应。

## 2. draft 与候选在哪里不同

draft 是 WiCER 论文 §6.4 的 ablation 总结：诊断 pinning 对照 random pinning，前者 +0.95 后者 +0.16，5.9× 差距；17 个 RepLiQA 主题中赢 16 个；唯一反例 `local_education_systems` 同时也是主表中 0% recovery 主题。论点轴是"基于失败的强化循环必须配 random control 才能分离功劳"。

v2 候选与之毫无重叠：top 1 是 raw sources 只读事实来源（Karpathy gist 三层中的第一层），top 2 是 schema 配置文档，top 3 是 idea file 抽象性。没有 ablation、pinning、knowledge compilation 等任何概念。

## 3. 下一步的核心依据

(1) (2) 共同表明 v2 无相关卡。draft 数字、来源、对照设定完整。结论 `new_card`。

不选 `provenance_delta`：v2 无 body 可补。
不选 `revise_before_gate`：draft 已具备足够证据与边界。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进 publication_gate；与 WiCER 主簇（compile-evaluate-refine 等）后续互相 cite。

## 5. 备注

Top 3 score = 0 再次出现，体现 v2 卡片基数小（15 张）时 jaccard 召回的局限。
