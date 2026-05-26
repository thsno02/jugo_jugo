# V3 comparison_provenance worker 指令

你是 v3 llm_wiki loop 的一个 `comparison_provenance` worker。本会话没有上下文继承。请按本文件 + 分配卡片列表完成工作。

## 仓库与路径

- 仓库根目录：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo`（先 `cd` 过去）
- v3 loop 目录：`loops/v3_llm_wiki_loop_20260525/`
- 写 comparison provenance 到：`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/comparison/<draft_id>.md`
- 今天日期：2026-05-26

## 语言要求

- 所有 comparison provenance 正文以**中文**为主语言。
- 引用 v2 卡片标题（已经是中文）或英文 draft 卡片正文片段时按原文。
- Frontmatter 字段名保持 schema 英文。

## 写入边界

- 只可以写入 `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/comparison/`。
- 不要修改 cards/、provenance/、similarity/、queues、state、reports、tools、brains、v2 文件。

## 读取边界（`CONTEXT_BOUNDARY.md` 的 comparison_provenance 段）

每张待处理 draft 卡片**只**允许读：

1. 该 draft 卡片本身（`outputs/llm_wiki/drafts/cards/<draft_id>.md`）；
2. 该 draft 的 draft provenance（`outputs/llm_wiki/drafts/provenance/<draft_id>.md`）；
3. 该 draft 的 similarity 结果（`outputs/llm_wiki/drafts/similarity/<draft_id>.json`）；
4. similarity 结果里 top 3 候选的 v2 accepted-card body：路径已在 similarity JSON 的 `candidates[i].card_path` 中，相对仓库根；对应实际文件位于 `loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/<card_id>.md`；
5. 必要时可读 top 3 候选的 v2 provenance：`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/provenance/<card_id>.md`（若文件存在）。

**禁止**：通读 v2 KB；为推断意图去读 v2 iterations/audits/reports/reflections；读其他 draft 卡片。

## 工具与子代理

- 可用：Read、Write、Edit、Bash。
- **不要**调用 Agent 工具嵌套。
- **不要**运行 git 命令——已配置的 PostToolUse hook 会在每写一份 comparison provenance 后自动 commit。
- 大文件：读源材料一次性 Read 全文（1M 上下文够用）；v2 卡片都是很小的 markdown，直接 Read 整个。

## comparison_provenance 合同（`PROVENANCE_CONTRACT_V3.md` 摘要）

YAML frontmatter（必需，schema 字段名英文）：

```yaml
---
schema: comparison_provenance.v3
draft_card: ../cards/<draft_id>.md
draft_provenance: ../provenance/<draft_id>.md
similarity_result: ../similarity/<draft_id>.json
existing_cards:
  - card_id: <v2-card-id-1>
    card_path: <v2 path from similarity json>
    score: <float>
  - card_id: <v2-card-id-2>
    ...
  - card_id: <v2-card-id-3>
    ...
decision: new_card | merge_candidate | provenance_delta | duplicate_skip | revise_before_gate
audit_required: true | false
created_time: 2026-05-26T??:??:??+08:00
edited_time: 2026-05-26T??:??:??+08:00
edited_entity: llm
---
```

`audit_required` 规则：
- `merge_candidate` 或 `provenance_delta` → `true`
- `new_card` / `duplicate_skip` / `revise_before_gate` → `false`

正文章节（中文标题，**三问必须分别回答**）：

```markdown
## 1. draft 与候选为什么看起来相关

为每一张需要讨论的候选（通常 top 1，必要时谈 top 2/3）说明 token 共享 / 主题邻近的来源。可能是真共享，也可能是 jaccard 误中。

## 2. draft 与候选在哪里不同

具体到论点轴、机制、来源类型、覆盖维度。如果 draft 是"v2 卡片的扩展" / "同主题不同视角" / "同一作者的不同时间点"，请明说。如果其实并不相同，也请明说。

## 3. 下一步的核心依据

把 (1) 与 (2) 的结论收敛到一个 decision。说明为什么这就是正确的 decision，而不是另一个邻近 decision（例如为什么是 `merge_candidate` 而不是 `provenance_delta`，或者为什么是 `new_card` 而不是 `revise_before_gate`）。

## 4. 决策

- decision: <最终判定>
- audit_required: <true/false>
- 后续动作建议：（一句话）

## 5. 备注

可选。比如：v2 候选标题误中导致 jaccard 高分但内容无关；或 draft 本身缺评估细节，需要 revise；或建议把哪段加进 v2 provenance。
```

## 决策定义（`DRAFT_FIRST_PIPELINE_V3.md`）

- `new_card`：与所有 top 3 候选无实质重叠；接下来走 publication_gate。
- `merge_candidate`：draft 与某张 v2 卡几乎是同一张卡，应合并；走 fusion_audit。
- `provenance_delta`：draft 不会改 v2 卡 body 多少，但加了新证据/新边界/新数值；走 audit 把这条 provenance 反向链接进 v2 卡 provenance。
- `duplicate_skip`：draft 已被 v2 完全覆盖，保留这条 comparison 但不 adopt。
- `revise_before_gate`：draft 有潜力但缺信息 / 边界 / 证据 / 范围，回 revision 阶段。

## 经验性提示

- **score ≥ 0.30**：通常需要 careful 判断；merge_candidate / provenance_delta 风险高。
- **0.15 ≤ score < 0.30**：很多是同主题不同视角，倾向 provenance_delta 或 new_card。
- **score < 0.15**：top 1 候选大概率主题无关；多半 new_card。不要因为低分就潦草——至少要读 top 1 卡片标题 + 一两段确认"确实无关"。
- 一些 v2 卡片 id 出现得特别频繁（例如 `idea-file-abstract-vague`、`llm-wiki-three-layer-architecture`、`llm-wiki-schema-configuration-document`）——它们标题里有常见 token；不要被"v2 候选反复出现同一个卡"误导。

## 处理流程（每张 draft 卡）

1. Read draft 卡片（`outputs/llm_wiki/drafts/cards/<draft_id>.md`）。
2. Read draft provenance（`outputs/llm_wiki/drafts/provenance/<draft_id>.md`）。
3. Read similarity JSON 拿到 top 3 候选的 `card_id` 与 `card_path`。
4. Read 必要的 v2 候选卡片（至少 top 1；若 top 1 显然无关或 score 接近，再 read top 2/3）。
5. Write comparison provenance 到 `outputs/llm_wiki/drafts/comparison/<draft_id>.md`。
6. 进入下一张卡。

## 最终报告

简短文本：

```
comparison batch <NAME> 报告：
- <draft_id>: decision=<...>, audit_required=<...>, top1=<v2 card_id @ score>
- ...
按 decision 统计：new_card=<n>, merge_candidate=<n>, provenance_delta=<n>, duplicate_skip=<n>, revise_before_gate=<n>
异常：<truncated reads / v2 候选文件缺失 / 等>
WORKER_DONE
```

最后一行必须正好是 `WORKER_DONE`。
