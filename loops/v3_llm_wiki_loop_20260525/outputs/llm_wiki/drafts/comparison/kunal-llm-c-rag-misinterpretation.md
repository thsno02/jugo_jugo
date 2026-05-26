---
schema: comparison_provenance.v3
draft_card: ../cards/kunal-llm-c-rag-misinterpretation.md
draft_provenance: ../provenance/kunal-llm-c-rag-misinterpretation.md
similarity_result: ../similarity/kunal-llm-c-rag-misinterpretation.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1429
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1304
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0909
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选共享的 token 都仅在 `llm`、`wiki`、`的` 三个高频通用词上：draft 标题包含"LLM Wiki"，候选三张也都是 v2 `LLM Wiki` 系列。jaccard 只是机械捕到主题词重叠，不反映任何论点重叠。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-three-layer-architecture`：来源是 Karpathy gist L25–33，记录"raw sources / wiki / schema"三层架构。论点轴是**Karpathy 自己给出的架构定义**。
- 候选 #2 `llm-wiki-schema-configuration-document`：来源是同 gist 的 L33，仅说明 schema 层的定义。是一张围绕 schema 的纯事实卡。
- 候选 #3 `llm-wiki-health-checks`：来源是 Karpathy 推文 quote 的 Linting 段，描述 LLM 对 wiki 做 health checks。
- draft 的核心论点完全在另一个轴：标注 **Kunal Ganglani 2026-04 博文**把 "LLM Wiki" 误解为基于 `llm.c` 的本地 RAG 系统这一术语漂移现象，并主张 wiki 主题页应显式区分两种解读。draft 是 distinction 卡，处理外部社区对 Karpathy 模式的错读，v2 卡里没有任何卡触及 "误解 / 术语漂移 / 第三方解读" 这条线。

## 3. 下一步的核心依据

(1) (2) 共同表明，draft 与 top 3 在论点对象、来源类型与卡片类型上全部不同：候选都在记录 Karpathy 原始 gist 的内部事实，draft 在记录"另一篇文章如何误读 Karpathy 的 LLM Wiki"。

- 不是 `merge_candidate`：v2 没有任何 distinction 卡或术语漂移卡。
- 不是 `provenance_delta`：候选都没有"误读"维度可以反向加挂。
- 不是 `duplicate_skip`：内容没有任何重叠。
- 不是 `revise_before_gate`：draft 自带清楚的 Kunal 原文逐字 quotes（L48 / L60 / L70–76 / L173–195）与对照说明；门控阶段可以再讨论是否需要更克制地表述对 Kunal 的评价，但目前 statement 与边界自洽。
- 综上，判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；重点检查"SEO 与术语污染"那段是否越出来源直接支撑（属解读层，需要清晰标注）。

## 5. 备注

- 本卡属典型 jaccard 命中 v2 同一组 "LLM Wiki" 系列卡的低分误中，与 draft 论点无关。
- 这张卡也是未来 v3 wiki 主题页"LLM Wiki 真实定义 vs 常见误读"对照视图的一个基础卡。
