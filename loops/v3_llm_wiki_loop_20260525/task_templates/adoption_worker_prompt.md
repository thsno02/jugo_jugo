# V3 adoption worker 指令（publication_gate / fusion_audit）

你是 v3 llm_wiki loop 的 adoption worker。本会话无上下文继承。你的任务是对分配给你的一组 draft 卡片做 **publication_gate**（针对 `new_card`）或 **fusion_audit**（针对 `provenance_delta`），通过的卡片 adopt 到 v3 KB。

## 仓库与路径

- 仓库根目录：`.`（先 `cd` 过去）
- v3 loop 目录：`loops/v3_llm_wiki_loop_20260525/`
- Draft 路径：`outputs/llm_wiki/drafts/cards/<id>.md` + `drafts/provenance/<id>.md` + `drafts/similarity/<id>.json` + `drafts/comparison/<id>.md`
- Adopted 路径：
  - 卡片 → `outputs/llm_wiki/kb/cards/<id>.md`
  - provenance → `outputs/llm_wiki/kb/provenance/<id>.md`
- 今天日期：2026-05-27

## 语言要求

- 所有 adopted 卡片正文、provenance 正文以**中文**为主语言（draft 已经满足；adoption 不改正文）。
- frontmatter schema 字段名保持英文。

## 写入边界

- 你**只**写入两个目录：`outputs/llm_wiki/kb/cards/` 和 `outputs/llm_wiki/kb/provenance/`。
- 不要修改 drafts/、queues/、state、reports、tools、brains、v2 等任何其他文件。
- Hook 已配置：写一个 kb 卡片 → 自动 `git add` + commit（包含同名 kb provenance），message 形如 `v3 adopt: <id>`。**不要**自己运行 git。

## 读取边界

每张待处理 draft 允许读：
- 该 draft 卡片（`drafts/cards/<id>.md`）；
- 该 draft 的 provenance（`drafts/provenance/<id>.md`）；
- 该 draft 的 similarity（`drafts/similarity/<id>.json`，可选）；
- 该 draft 的 comparison（`drafts/comparison/<id>.md`）；
- 对于 `provenance_delta` 卡片：comparison 文件里指明的 v2 anchor card body（`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/<v2-id>.md`）和 provenance（如有）。

不要读：其他 draft 卡片；v2 KB 中未被 comparison 指明的其他卡片；任何 v0/v1/v2 历史。

## publication_gate 判定准则（针对 `new_card`）

逐条检查，全部通过才能 adopt：

1. **不是标题复述**：正文必须真在解释知识。如果正文只是把标题写成完整句子（"X 是 Y 的 Y"），fail。
2. **知识密度**：正文至少给出概念解释 / 机制 / 边界 / 反例 / 操作规则 中的若干条，不只是"主题简介"。三段以上 substantive 中文段落是合理下限。
3. **源支撑**：`source_ids` 不为空；正文中至少有一个具体的源材料引用片段（原文 + 路径/JSON 指针）。
4. **References / Footnotes 存在**：正文末尾有 `## References` 与（可选的）`## Footnotes` 章节，定位到具体的源文件路径 / 行号 / JSON 指针。
5. **frontmatter 完整且合法**：id、title、card_type、tags、source_ids、provenance_card、created_time、edited_time、edited_entity 全部存在且不为空。
6. **related 字段已填充**：related 非空，且其中的 id 都是 v3 draft 卡 id（interlink 阶段已确保）。

如果有 1–2 条小瑕疵（例如 frontmatter 字段顺序不规范、tags 写法略不一致）但卡片整体合格，**允许 adopt**——adoption 阶段的小规整不算 fail。

如果 4 条以上 fail，标记 `gate_failed`，不 adopt，写明原因。

## fusion_audit 判定准则（针对 `provenance_delta`）

读完 draft + provenance + comparison + v2 anchor 后逐条检查：

1. **三问真的被回答**：comparison 文件的"draft 与候选为什么看起来相关 / 在哪里不同 / 下一步核心依据"三节不是空话，而是 substantive。
2. **v2 anchor body 真的被读过**：comparison 的描述要能从 v2 卡片内容中找到对应（不是从标题或 v2 索引描述外推）。
3. **v3 draft 不破坏 v2 scope**：draft 卡的知识不是改写 v2 卡的核心主张，而是在 v2 scope 之外加东西（细节 / 反例 / 限定 / 第三方实现 / 后续版本）。
4. **provenance 链接是增量且可追溯**：adopt 后，新 kb provenance 文件里要有显式的 `v2_anchor_card` 字段指向 v2 卡 id 与路径，并把 comparison 文件路径写进去。

注意：v3 不能写 v2 文件，所以 fusion_audit 不会真的去改 v2 accepted card 的 provenance。我们在 v3 KB 里 adopt 这张卡，**同时**在 kb provenance 文件里记录"这是某 v2 卡的 delta"，让未来的双向链接成为可能。

如果 fusion_audit 通过 → adopt 这张卡到 v3 KB（同时在 kb provenance 里加 v2_anchor 字段）。
如果 fusion_audit 失败 → 不 adopt，标记 `audit_failed`，写明原因。

## 通过后的 Adoption 操作

对每张通过的卡：

### 1. 卡片 → `outputs/llm_wiki/kb/cards/<id>.md`

复制 draft 卡片内容，只改 frontmatter：

- `status: draft` → `status: accepted`
- `edited_time: <旧值>` → `edited_time: 2026-05-27T<现在>+08:00`
- 其他 frontmatter 字段保持不变（id、title、card_type、tags、source_ids、provenance_card、aliases、related、edited_entity 等）。
- `provenance_card: ../provenance/<id>.md` 保留——kb 目录结构和 drafts 一致，相对路径仍然解析正确。

正文（YAML 之后的全部内容）**逐字保留**，不要改动。

### 2. provenance → `outputs/llm_wiki/kb/provenance/<id>.md`

构造 kb provenance 文件。它是 draft provenance 的扩展版：

```yaml
---
schema: accepted_card_provenance.v3
card: ../cards/<id>.md
material_id: <来自 draft provenance>
digest_id: <来自 draft provenance>
source_paths:
  - <来自 draft provenance>
draft_card: ../../drafts/cards/<id>.md
draft_provenance: ../../drafts/provenance/<id>.md
similarity_result: ../../drafts/similarity/<id>.json
comparison_provenance: ../../drafts/comparison/<id>.md
gate:
  type: <publication_gate | fusion_audit>
  result: passed
  decided_at: 2026-05-27T<现在>+08:00
  gate_notes: <一句话总结：例如『5/6 项通过，frontmatter 字段顺序略不规范但不影响 adoption』>
# 仅 provenance_delta 卡片需要这一节：
v2_anchor:
  card_id: <v2 卡 id>
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/<v2-id>.md
  comparison_decision: provenance_delta
created_time: <draft provenance 的 created_time>
edited_time: 2026-05-27T<现在>+08:00
edited_entity: llm
---

## 源证据

（从 draft provenance 复制对应章节）

## 卡片范围是否成立

（从 draft provenance 复制对应章节）

## 发表门控结果

- 类型：<publication_gate | fusion_audit>
- 结果：passed
- 决定时间：2026-05-27T<now>+08:00
- 检查要点：<列出本次 gate 通过的关键判据，每条一句话>

## 备注

（从 draft provenance 复制；可追加 adoption 阶段发现的小观察）

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/<id>.md`
- draft provenance: `../../drafts/provenance/<id>.md`
- similarity: `../../drafts/similarity/<id>.json`
- comparison provenance: `../../drafts/comparison/<id>.md`
```

`v2_anchor` 仅在 fusion_audit 通过 provenance_delta 时加；publication_gate 通过的 new_card 不写这一节。

## 不通过的处理

不通过的卡不写入 kb/。在最终报告里列出 `<id>: failed (publication_gate|fusion_audit), reason=...`。

## 处理流程（每张卡）

1. Read draft card、draft provenance、comparison provenance（如有）、（provenance_delta 才读）v2 anchor。
2. 应用判定准则。
3. 如果通过：Write kb 卡片（`outputs/llm_wiki/kb/cards/<id>.md`）。Hook 会自动 commit 卡片 + 同名 provenance（如果 provenance 已经存在）。
4. 紧接着 Write kb provenance（`outputs/llm_wiki/kb/provenance/<id>.md`）。**先写 provenance 再写卡片**，可以让 hook 在 commit 卡片时也能 stage 上 provenance（hook 同时 `git add` 卡片 + 同名 provenance）。
5. 进入下一张。

**重要**：因为 hook 在 kb 卡片写完时把同名 provenance 也 stage，所以请**先 Write kb provenance，再 Write kb card**——这样 hook 触发时 provenance 已经在 disk 上，可以被 stage 进同一个 commit。

## 最终报告

```
adoption batch <NAME> 报告：
- 处理总数：<n>
- 通过：<n>
- 失败：<n>
- 通过详情（id 列表）：[...]
- 失败详情：- <id>: <reason>
WORKER_DONE
```

最后一行必须正好是 `WORKER_DONE`。
