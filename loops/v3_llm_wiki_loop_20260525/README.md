# V3 LLM Wiki Loop

状态：`active`

v3 的目标是验证一个更快、更可审计的知识卡生产流程：先把 material 变成有信息量的 draft card，再用轻量 similarity 机制找到可能相似的 top 3 卡，随后根据 comparison provenance 决定新建、融合、增量 provenance、跳过或返修。

## V3 要解决什么

v2 暴露的问题不是“没有卡”，而是流程成本过高，且部分卡太像标题复述。v3 要把这两件事拆开处理：

- 生产端先批量生成 scoped draft cards，不在每张卡上做全库融合判断。
- 每张 draft 必须像知识本身，而不是 title 的 paraphrase。
- similarity 只做候选召回，用 Jieba 标题分词和 Jaccard set similarity 取 top 3。
- 只有可能融合或增量改写已有卡时，才进入 fusion audit。
- 决策证据必须落在 comparison provenance 里，不能留在聊天上下文。
- provenance 是增量链接，不重写历史证据。

## 核心顺序

```text
source material / exhausted article
-> knowledge-dense draft card
-> title similarity top 3
-> comparison provenance questions
-> decision: new_card | merge_candidate | provenance_delta | duplicate_skip | revise_before_gate
-> publication gate or fusion audit
-> candidate KB adoption
```

## 当前入口

- `LOOP_START_PROMPT.md`：可直接用于 `claude --permission-mode auto -p` 的 v3 正式启动 prompt。
- `RUNBOOK.md`：主控 agent 如何推进 v3。
- `CARD_CONTRACT_V3.md`：v3 知识卡写法和 metadata。
- `DRAFT_FIRST_PIPELINE_V3.md`：生产管线。
- `SIMILARITY_MECHANISM_V3.md`：轻量 similarity 机制。
- `PROVENANCE_CONTRACT_V3.md`：comparison provenance 和融合审计要求。
- `BRAIN_MAILBOX_PROTOCOL.md`：brain mailbox / queue 最小协议。
- `loop_state.json`：当前机器可读状态。
- `reports/loop_report.md`：人类可读进度报告。

`outputs/llm_wiki/` 是 v3 候选产物，不是仓库根目录 stable product。
