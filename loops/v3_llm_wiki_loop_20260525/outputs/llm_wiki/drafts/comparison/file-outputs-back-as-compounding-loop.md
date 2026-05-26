---
schema: comparison_provenance.v3
draft_card: ../cards/file-outputs-back-as-compounding-loop.md
draft_provenance: ../provenance/file-outputs-back-as-compounding-loop.md
similarity_result: ../similarity/file-outputs-back-as-compounding-loop.json
existing_cards:
  - card_id: llm-wiki-persistent-compounding-artifact
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-compounding-artifact.md
    score: 0.0909
  - card_id: llm-wiki-persistent-wiki-alternative-mode
    card_path: llm_wiki/kb/cards/llm-wiki-persistent-wiki-alternative-mode.md
    score: 0.0833
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.0769
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- 候选 #1 `llm-wiki-persistent-compounding-artifact`：共享 token `wiki`。draft 的"复利循环"与候选 "持久复合 wiki" 在主题概念上**真有重叠**——两边都谈 wiki 的复合增长，且都来自同一份来源（Karpathy quote 推文）。这是本批 LOW 中**真共享而非误中**的关键案例。
- 候选 #2 `llm-wiki-persistent-wiki-alternative-mode`：共享 `wiki`。论点轴不同（替代模式 vs 回写复利）。
- 候选 #3 `llm-wiki-health-checks`：共享 `wiki`。是 draft 边界节明确依赖的兜底机制（"没有 linting，回写会放大错误答案"），主题相邻但不同卡。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-persistent-compounding-artifact`：是一张**性质论断**卡——"wiki 是持久复合产物，保留 cross-reference / 矛盾标记 / 综合内容，随新增源和提问继续变丰富"。来源行是 `karpathy-x-launch-post/text.txt` $.tweet.quote.text 的另一段。它描述 wiki 的"产物性质"。
- 候选 #2、#3：分别是 wiki 模式的元事实、health checks 的事实卡。
- draft 是一张 **operational_rule** 卡——把"复利"从性质转成可执行规则：把每次查询答案当候选新文章、渲染成 markdown/slides/png、归档到相关概念目录、允许后续查询将归档结果与原始导入文档同等对待、依赖 linting 做兜底。来源行是同一份 `karpathy-x-launch-post` quote 的 Output: 段 + Linting: 段。
- 两者抽象层级与卡片类型不同：候选 #1 是 known_fact / 性质论断，draft 是 operational_rule / 落地步骤。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：候选 #1 与 draft 是同一论点（compounding）的两个不同侧面——一个是"wiki 是 compounding artifact"的性质描述、一个是"如何让 compounding 发生"的操作规则。合并会损失 draft 的操作步骤与 linting 兜底边界。
- 不是 `provenance_delta`：draft 不只是给候选 #1 加证据/边界——它有完整的 4 项操作步骤与失败边界，自成机制卡。把 draft 收成候选 #1 的 provenance 补丁会丢失这些。
- 不是 `duplicate_skip`：候选 #1 不覆盖 draft 的操作步骤与 linting 边界。
- 不是 `revise_before_gate`：draft 已有 Karpathy 原文 verbatim、4 项操作步骤、结构性效果论断、linting 兜底边界；门控可继续。
- 综合判 `new_card`。这是 LOW 批中典型的"性质卡 vs 操作规则卡"分轴 case：两张卡共享来源段，但是论点轴不同。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议把本卡与 v2 `llm-wiki-persistent-compounding-artifact` 互相 cross-link（性质卡 ↔ 操作规则）。

## 5. 备注

- draft 自身 provenance 已显式指出："标题 token 与 v2 中的 'Query 操作回写好答案' 预期会高度重合；comparison provenance 阶段需要评估本卡片中新增的'结构性框架'是否足以独立成新卡，或者更应作为 provenance delta"——v2 `llm-wiki-query-answer-writeback` 卡未进入本批 top 3（jieba 把"回写好答案"切成 `回写` `好` `答案` 而 draft 的"回写进 wiki"切成 `回写` `进` `wiki`，主题词集合不同），但它确实与本 draft 论点高度重叠。建议 publication_gate 同时考察本 draft 与 v2 query-answer-writeback 的关系，可能产生 audit 阶段的合并/cross-link 提案。
- v2 池子里有三张 wiki 主题卡（候选 #1/#2/#3）共同形成本 draft 的 top 3，是单一主题词分母效应的典型表现。
