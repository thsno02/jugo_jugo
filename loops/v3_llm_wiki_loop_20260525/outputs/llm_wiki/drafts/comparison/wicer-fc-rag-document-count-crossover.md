---
schema: comparison_provenance.v3
draft_card: ../cards/wicer-fc-rag-document-count-crossover.md
draft_provenance: ../provenance/wicer-fc-rag-document-count-crossover.md
similarity_result: ../similarity/wicer-fc-rag-document-count-crossover.json
existing_cards:
  - card_id: rag-document-qa-does-not-accumulate-synthesized-knowledge
    card_path: llm_wiki/kb/cards/rag-document-qa-does-not-accumulate-synthesized-knowledge.md
    score: 0.1111
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0556
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- 候选 #1 `rag-document-qa-does-not-accumulate-synthesized-knowledge`：共享 token `rag`、`文档`。draft 与候选都谈 RAG 与文档，是本批 LOW 中相对"主题靠近"的撞分，但论点轴不同（见下）。
- 候选 #2 `llm-wiki-schema-configuration-document`：共享 `文档`。机械撞分。
- 候选 #3 `idea-file-abstract-vague`：共享 0 token（score 0）。无关。

## 2. draft 与候选在哪里不同

- 候选 #1 `rag-document-qa-does-not-accumulate-synthesized-knowledge`：仅记录 Karpathy gist 第 7–10 行对 RAG 式文档问答**不积累综合知识**这一**性质论断**。是 wiki 模式 vs RAG 的概念对比卡，无任何数字。
- draft 是 distinction 卡，论点轴是 WiCER 论文用 Policygenius（30 doc, 67K token）与 RepLiQA（80 doc, 55–95K token）做对照实验，给出"FC 4.38/RAG 4.08 → FC 3.47/RAG 3.64"的具体翻转、TTFT 7.3×→4.6×、557 个 lost-in-the-middle 案例、Q4 KV cache 在大语料下退化等实证细节。draft 的核心断言是"窗口占比不是唯一变量，编译质量决定 FC 可行性"，并把这一结论挂到 LLM Wiki thesis 上。
- 候选 #2、#3：完全无关。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：候选 #1 是概念性质卡，draft 是带具体数字的对照实验卡，抽象层级与论点结构不同。
- 不是 `provenance_delta`：尽管 draft 的"FC 在精编 wiki 上赢 / 在 raw collection 上输"结论与候选 #1 的"RAG 不积累综合知识"概念性结论有方向一致性，但加挂方式会丢失 draft 的核心数据（Policygenius/RepLiQA 表、557 案例、Q4 退化等）；正确路径是 draft 自成卡。
- 不是 `duplicate_skip`：无重叠。
- 不是 `revise_before_gate`：draft 已有完整数字（§568–614 / §656–671 / §672–683 / §687–690 / §634–638 / §641–644）、三条操作启示、与"WiCER 算法卡"互补的范围；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段可与 v2 `auto-index-replaces-rag-at-small-scale` 互相 cross-link 评估（draft 自身 provenance 已显式提到此 v2 卡）——该卡未进入本批 top 3，属审计阶段动作。

## 5. 备注

- top 3 第三名 score=0（共享 0 token），是 v2 仅 15 张候选 + 高频虚词分母时偶发的极端情况。
- 与同源 `wicer-cegar-compile-evaluate-refine`、`wicer-blind-compilation-catastrophic-loss` 三张 WiCER 卡互补。
