# Adopt Loop Design V2

- `decision_time`: `2026-05-25T15:51:23+08:00`
- `decision`: `accept`
- `scope`: loop control plane, card contract, similarity flow, brain-mailbox routing

## 背景

用户指出旧流程的 card 生产效率过低，而且 card 过度 atomic、信息量不足。随后确认：

- card 本身必须是 knowledge，不只是 title restatement；
- metadata 需要固定，包括 `tags`、`created_time`、`edited_time` 和 `edited_entity`；
- body 不需要强模板；
- `References` 和 `Footnotes` 是不同 schema；
- similarity 是新版流程内容，先用 Jieba title token + Jaccard 做 top3，再写 comparison provenance 三问；
- brain 之间需要通过 mailbox 传递 audit / production / similarity 信息。

## 决策

将 V1 draft-first 控制面冻结到：

`legacy/v2_llm_wiki_loop_20260525/snapshots/draft_first_control_plane/`

当前活跃设计切换到：

- `llm_wiki/loop/LOOP_DESIGN_V2.md`
- `llm_wiki/loop/CARD_CONTRACT_V2.md`
- `llm_wiki/loop/DRAFT_FIRST_PIPELINE.md`
- `llm_wiki/loop/brains/README.md`

V2 primary object 是 `scoped_knowledge_card`。

## 新流程要点

```text
material / exhausted source
-> scoped draft card + draft provenance
-> Jieba/Jaccard title similarity top3
-> comparison provenance 三问
-> publication audit 或 fusion audit
-> public adoption 或 provenance delta adoption
```

comparison provenance 必须回答：

- 为什么认为 draft card 和 A 卡有共同点？
- draft card 和 A 卡的不同在哪里？
- 进行下一步操作的核心依据是什么？

`merge_candidate` 和 `provenance_delta` 必须经过 fusion audit，才能把 comparison provenance 链接回 A 卡 provenance。

## 残余风险

- 文件层 mailbox 已 smoke 验证，但自动 spawn/resume Codex sub-agent 尚未验证。
- 已有 V1 draft / accepted cards 需要未来按 V2 metadata 和知识含量要求逐步迁移或标注。
- Jieba/Jaccard title similarity 是轻量候选选择机制，不保证语义召回；需要允许有记录的人工/agent override。
