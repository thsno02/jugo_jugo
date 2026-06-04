---
status: future_plan
stage: reference_template
created: 2026-06-02
loop_id: v3_llm_wiki_loop_20260525
topic: jj_template
note: Justification Journal 完整格式参考模板。展示 6 种事件类型 + rollup 机制。替代原 provenance schema。
---

# Justification Journal (jj) Template

> 每张卡一个 jj 文件，append-only 日志。记录卡从出生到 deprecation 的完整生命周期。
> 路径：`kb/justification/<card-id>.md`（与卡的 `justification:` 字段对应）。
> 替代原来的一次性 provenance schema——provenance 只记录出生，jj 记录一生。

---

## 文件格式

```markdown
---
schema: justification_journal.v1
card: ../cards/<id>.md
created_time: <ISO8601+08:00>
---

## <event_type> | <ISO8601+08:00>

<事件内容，<=20 行>

## <event_type> | <ISO8601+08:00>

<事件内容，<=20 行>

...
```

---

## 约束

| 约束 | 规则 |
|---|---|
| append-only | 只在末尾追加新事件，不修改已有事件（rollup 除外） |
| 每条 <=20 行 | 事件内容不超过 20 行（含空行） |
| <=6 条事件 | 文件中最多 6 条事件；超过时触发 rollup |
| 6 种事件类型 | creation / review / fusion / governance / evolution / deprecation |
| 完整历史 | rollup 压缩旧事件；完整逐条历史可通过 git history 回溯 |

---

## 完整示例（含全部 6 种事件类型）

```markdown
---
schema: justification_journal.v1
card: ../cards/beam-search-pruning-mechanism.md
created_time: 2026-06-02T14:30:00+08:00
---

## creation | 2026-06-02T14:30:00+08:00

生成方式：Mode A questioning loop, round 3
问题：beam search 中的剪枝机制具体如何工作？
来源：`data/raw/paper/cho-2024-decoding/text.txt`

源证据：
- 行 142-158："When the beam width exceeds k, the algorithm prunes
  candidates by comparing their cumulative log-probabilities..."
- 行 203-210："Pruning threshold is dynamically adjusted based on
  the ratio between best and worst candidates in the current beam."

范围论证：本卡聚焦 beam search 的剪枝判据和动态阈值机制，
不涉及 beam width 选择策略（那是独立的原子 idea）。

## review | 2026-06-02T15:00:00+08:00

quit-audit 结果：pass
覆盖率：digest core_claim #7（剪枝机制）由本卡覆盖
源忠实抽查：行 142-158 原文确认支撑"累积对数概率比较"的陈述
reviewer 备注：无补问需求

## fusion | 2026-06-02T15:10:00+08:00

inline fusion check：与 `beam-search-width-selection` 比较
verdict：link（related-but-distinct）
理由：两卡共享 beam search 主题，但本卡聚焦剪枝判据，
该卡聚焦 width 选择策略——原子 idea 不同，建立 [^card-1] 链接。

## governance | 2026-06-03T10:00:00+08:00

操作：link-as-distinction
与 `beam-search-early-stopping` 建立 distinction link
本卡 -> [^dist-1]：本卡聚焦运行时剪枝（每步淘汰候选），
该卡聚焦终止条件（何时停止整个搜索过程）。
canonical_concept 确认：`beam-search-pruning`（已有，复用）。

## evolution | 2026-06-05T09:00:00+08:00

编辑内容：补充了动态阈值的数学表达式
原因：新材料 `data/raw/paper/wu-2025-beam-analysis/text.txt`
提供了更精确的阈值公式（行 87-92），增补为 [^src-3]。
edited_time 已更新。

## deprecation | 2026-06-10T14:00:00+08:00

合并入 `beam-search-candidate-management`。
完整 merge 论证见该卡 jj 的 governance 事件。
status -> superseded; superseded_by -> beam-search-candidate-management。
```

---

## 各事件类型详细说明

### 1. creation（创建）

触发：extract reframing 产出卡片时。**必须是 jj 的第一条事件。**

内容要求：
- 生成方式：Mode A questioning loop, round N, 触发问题
- 源证据：关键原文片段 + 精确位置（行号/JSON pointer/节标题）
- 范围论证：为什么这张卡的范围合理（上界/下界/与兄弟卡的边界）

### 2. review（审查）

触发：reviewer quit-audit 完成时。

内容要求：
- quit-audit verdict（pass / needs_more_questions）
- 覆盖率判定：本卡覆盖了 digest 的哪条 core_claim
- 源忠实抽查结果（如果本卡被抽中检查）
- reviewer 备注（如有）

### 3. fusion（融合检查）

触发：inline fusion check 完成时。

内容要求：
- 与哪张/哪些卡比较
- verdict（keep / skip / link）
- 理由（same-claim / related-but-distinct / different）
- 如果 link：建立了什么 footnote

### 4. governance（治理）

触发：governance 阶段的任何操作。

内容要求（按操作类型）：
- **merge**（作为 hub 卡的 jj）：完整 merge-WHY。哪些卡被合并、为什么合并、合并后知识如何组织、每张原卡的贡献。**merge 的完整推理只在 hub 卡的 jj 中。**
- **link-as-distinction**：与谁建立 distinction、区分点是什么、双向 `[^dist-N]` 内容
- **canonical 归一化**：旧 canonical -> 新 canonical，归并理由

### 5. evolution（演化）

触发：卡的 body 或 metadata 发生实质性编辑时。

内容要求：
- 什么改了（body 增补 / metadata 更新 / footnote 新增）
- 为什么改（新材料提供更精确信息 / governance 建议 / 纠错）
- 相关的新 source reference（如有）

### 6. deprecation（弃用）

触发：governance 判定 merge，本卡被 supersede 时。

内容要求：
- 一行 pointer："合并入 `<hub-card-id>`，完整论证见该卡 jj"
- status 变更记录
- **注意：不在此处重复 merge-WHY**——完整论证只在 hub 卡的 jj 中

---

## Rollup 机制

### 何时触发

当 jj 文件中的事件条目达到 **6 条**时，在 append 第 7 条之前执行 rollup。

### 操作步骤

1. 取前 4 条事件
2. 压缩为 1 条 `## rollup | <timestamp>` 条目（<=20 行摘要）
3. 保留最近 2 条事件不变
4. rollup 后文件结构：1 rollup + 2 recent = 3 条
5. append 新事件 -> 4 条（继续有空间）

### Rollup 条目内容要求

rollup 摘要必须保留：
- 关键决策的结论（不需要完整推理过程）
- 源追溯链（creation 的核心源证据位置）
- 重要 governance 操作的结果（merge/distinction 的最终 verdict）
- 时间线概要（哪些阶段何时发生）

### Rollup 示例

```markdown
## rollup | 2026-06-05T09:00:00+08:00

本条 rollup 压缩了 4 条事件（2026-06-02 ~ 2026-06-05）。

创建：Mode A round 3，源 `cho-2024-decoding/text.txt` 行 142-158/203-210。
聚焦 beam search 剪枝判据和动态阈值。
审查：quit-audit pass，覆盖 core_claim #7。
融合：与 `beam-search-width-selection` link（related-but-distinct）。
治理：与 `beam-search-early-stopping` 建立 distinction link
（本卡=运行时剪枝，该卡=终止条件）。

完整事件详情见 git history。
```

### Rollup 后的文件结构

```markdown
---
schema: justification_journal.v1
card: ../cards/beam-search-pruning-mechanism.md
created_time: 2026-06-02T14:30:00+08:00
---

## rollup | 2026-06-05T09:00:00+08:00

（如上所示的压缩摘要）

## evolution | 2026-06-05T09:00:00+08:00

（保留的最近第 2 条事件）

## deprecation | 2026-06-10T14:00:00+08:00

（保留的最近第 1 条事件）
```

新事件继续 append 在末尾，直到再次达到 6 条时执行下一轮 rollup。
