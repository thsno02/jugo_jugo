---
status: active
skill: reframing
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-04
---

# Q&A → Card Reframing 契约

> 你负责将 questioner-reader 的 Q&A 对转化为自足的原子知识卡 + justification journal 创建事件。
> 这是一个独立的转化步骤，在每轮对话之间执行。

---

## 输入

1. **本轮 Q&A pairs**：问题 + 回答 + 来源位置
2. **当前轮次编号**（round N）
3. **材料 ID**（source_id，如 `karpathy-gist-llm-wiki`）
4. **材料路径**（如 `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`）
5. **现有 KB canonical_concept 列表**（grep 结果，用于复用/新铸判断）

---

## 转化规则

### 规则 1：对话体 → 知识陈述体

- 删除问答框架：「问：X 是什么？答：X 是...」→ 「X：一种...的机制」
- 正文应自足、密集、有据——读者不需要知道这是从对话中产出的
- 保留回答的信息密度，不稀释也不过度压缩
- 一张卡讲一个原子 idea：能在不引用兄弟卡的情况下被理解

### 规则 2：拆卡 vs 合卡判断

- **默认**：一个 Q&A = 一张卡
- **拆卡**：如果回答包含多个独立 idea（reader 用 (a)(b)(c) 分点的情况），每个独立 idea 拆为一张卡
- **拆卡信号**：回答引用了 2+ 个不同源节标题的 footnotes → 大概率应拆卡
- **合卡**：如果多个追问 Q&A 共同构成一个原子 idea（追问链深挖同一机制的不同层面），合为一张卡
- **判据**：能否在不引用兄弟卡的情况下被理解？能 → 独立成卡；不能 → 合并
- **标题测试**：如果标题需要「与」「和」等连词连接两个名词短语，几乎肯定应该拆成两张卡

### 规则 3：Metadata 填写

#### id
- stable ASCII slug, kebab-case
- 从 canonical_concept 或卡的核心概念派生
- 全 loop 唯一

#### title
- 中文短标题——概念名，不是完整句子
- 不是 claim 伪装成标题（「X 优于 Y」→ 不适合做标题）

#### canonical_concept
- kebab-case 英文
- **先 grep 现有 KB**：如果已有 canonical 匹配当前概念 → 复用
- 无匹配 → 新铸
- 一卡一个 canonical

#### aliases
- 该概念在材料中出现的真实表层变体
- 含中英文、缩写、符号形式
- 只列材料中实际出现的变体，不臆造

#### summary
- 一行稠密 grep 靶子
- **必须包含**：canonical_concept slug + **所有 aliases** + 核心论断，一句话
- 定位：为 grep 召回优化的信息密集行，不是给人看的优雅摘要
- 验证：如果 grep 任何一个 alias 无法命中此 summary，则不合格

#### card_type / tags
- 自由描述，agent 自选
- 不是受控分类——常见值参考：concept / mechanism / distinction / operational_rule / source_claim / example_pattern
- tags 自由 hashtag

#### source_ids
- 本卡使用的材料 ID 列表
- 通常只有一个（当前处理的材料）

### 规则 4：Typed Footnote 锚定

将 reader 回答中的来源位置转化为 `## Footnotes` section：

```
[^src-1]: `<材料路径>` -- <位置描述> -- "<关键原文引用>"
```

- 正文中用 `[^src-N]` 标记具体 claim 的源支撑
- 每个 `[^src-N]` marker 对应且仅对应一个 `[^src-N]: ...` 展开
- `## Footnotes` 放在 card body 末尾
- 按正文首次出现顺序排列

### 规则 5：Cross-Link（关联标记）

每张新卡产出后，检查**本轮已有卡 + 已有 KB 卡**的 canonical_concept 和 aliases：
- 如果新卡与某张已有卡共享主题或存在明确关联 → 在新卡 body 中添加 `[^card-N]` footnote，narrative 说明关系
- `related:` 字段由脚本从 `[^card-N]` + `[^dist-N]` 自动派生，reframing 时不手填 `related:`
- 但 reframing **必须主动添加 `[^card-N]` footnotes**——如果一张卡明显与其他卡相关却没有任何 card-type footnote，说明遗漏
- 最低标准：每张卡至少考虑是否与本轮其他卡存在关联

### 规则 6：Justification Journal 创建事件

为每张卡创建一个 jj 文件，包含 creation 事件：

```markdown
---
schema: justification_journal.v1
card: ../cards/<id>.md
created_time: <ISO8601+08:00>
---

## creation | <ISO8601+08:00>

生成方式：Mode A questioning loop, round <N>
问题：<触发本卡的问题>
来源：`<材料路径>`

源证据：
- <位置> — "<关键原文片段>"
- <位置> — "<关键原文片段>"

范围论证：<为什么这张卡的范围合理——上界/下界/与兄弟卡的边界>
```

---

## 输出

每张卡产出两个文件：

1. **Card**: `drafts/cards/<id>.md`
2. **Justification**: `drafts/justification/<id>.md`

### Card 文件完整格式

```markdown
---
id: <slug>
title: <中文短标题>
status: draft
card_type: <自由描述>
tags: [<自由 hashtag>]
created_time: <ISO8601+08:00>
edited_time: <ISO8601+08:00>
edited_entity: llm
source_ids: [<material_id>]
justification: ../justification/<id>.md
canonical_concept: <kebab-case-english>
aliases: [<变体词列表>]
summary: >-
  <一行稠密 grep 靶子>
related: []
---

<知识陈述体正文，含 [^src-N] 标记>

## Footnotes

[^src-1]: `<path>` -- <location> -- "<quote>"
```

---

## 每轮 Reframe 后的输出

除了卡片文件外，还需返回**本轮已产出 canonical_concept 列表**，格式：

```
本轮新增 canonical_concepts:
- <canonical-1>
- <canonical-2>
- ...

累计 canonical_concepts:
- <all-canonicals-so-far>
```

这个列表传给 questioner，供下一轮避免重复追问。
