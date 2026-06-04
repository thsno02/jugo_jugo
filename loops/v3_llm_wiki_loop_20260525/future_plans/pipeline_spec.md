---
status: future_plan
stage: spec_v2
created: 2026-06-01
updated: 2026-06-02
loop_id: v3_llm_wiki_loop_20260525
topic: pipeline_spec
note: 下一个 loop 的完整管线规格（v2 更新）。整合 questioning loop 定稿、typed footnote、justification journal、reviewer quit-audit 等设计决策。定义每个阶段的 scope/context/boundary/I-O schema/artifacts。先定契约，再讨论实现。
---

# Pipeline Spec：Knowledge Database Construction

> 可复用的 per-material 管线。**collect --> extract --> ingest --> evolve**。添加任意新材料时走相同路径。
>
> 执行模式 v4：**parallel (A)**，focus on skills building。evolve/Mode B deferred。

---

## 0. 全局约束（贯穿所有阶段）

| 约束 | 规则 |
|---|---|
| init is not special | init KB = N 个材料并行跑同一管线 + 一次全局 governance；后续 add = 1 个材料 + scoped governance。**同一套 per-material 契约，无特殊路径** |
| loop 独立 | 语料只用本 loop 自己的 cards；不比较/引用任何外部 loop |
| Zettelkasten | 原子卡、无 taxonomy（card_type/tags free-form）；结构靠 link+governance 涌现 |
| 永不删除 | superseded --> `kb/archive/` + status flag；不 rm |
| 中文主语言 | 卡片/justification/报告中文；schema key/path/code/id 英文 |
| grep-friendly metadata | `canonical_concept` / `aliases` / `summary`：描述卡内容的 per-card 字段，grep 的锚点 |
| typed footnote | 单一 `## Footnotes` hub，四种 typed prefix（`src`/`card`/`dist`/`url`）；`related:` 脚本从 `card`-type 派生 |
| best-effort zen | 治理让问题更简单而非全解；颗粒度 agent-judged；不追求完备 |
| bypassPermissions | loop 整轮以 `--permission-mode bypassPermissions` 执行 |
| grep-only recall | agent 自主 grep 召回，查询时主动改写为 zh/en/同义词多轮 grep。SOTA for this context，不引入 embedding/jieba/向量 |
| 无 tentative/stable 区分 | 卡出生即终态；KB 通过 governance + consumption 成熟，不设生命阶段 |

---

## 1. Stage: Collect

> **Scope**: 获取 raw material 到 `data/raw/`。本轮暂不动。

| 维度 | 定义 |
|---|---|
| **scope** | 按 source spec（URL / repo / paper id）获取原始材料落盘 |
| **context** | source spec（来自人工或 collect-request） |
| **boundary-read** | 外部网络 / 本地文件系统 |
| **boundary-write** | `data/raw/<source_type>/<source_id>/` |
| **input** | source spec（URL / repo / paper id / description） |
| **output** | raw material files + `data/manifests/source_digests_index.md` 条目 |
| **artifacts** | `data/raw/<source_type>/<source_id>/{text.txt, metadata.json}` |
| **status** | parked / TODO（v4 暂手动） |

---

## 2. Stage: Extract（Questioning Loop -- Mode A）

> **Scope**: 把一份 raw material 转化为 N 张源忠实的原子知识卡 + justification。通过 questioner<-->answerer 对话 exhaust 材料，reviewer 做 quit-audit 防止 early stop。
>
> **编排模型**：主 agent（orchestrator）是**静态协调者**——不读材料本身，只分派任务、中继消息、收集产出。知识抽取由三个角色完成：reader/answerer、questioner、reviewer。

### 2.0 总览

```
coordinator dispatches:
  reader reads full source --> produces digest (coverage map for reviewer)
  questioner (full material access) asks systematic questions
  reader/answerer answers from full text (KV cache warm)
  between rounds: Q&A pairs --> draft cards (reframing)
  reviewer: quit-audit (digest coverage + source grep verification)
  inline fusion check (grep KB for overlaps)
  output: draft cards + justification journals
```

### 2.0.1 角色定义

| 角色 | 看到什么 | 职责 | 边界 |
|---|---|---|---|
| **Coordinator** (主 agent) | 产出物 metadata（不读材料 body） | 静态分派 + 消息中继 + 产出收集 | 不做知识判断，不读原文 |
| **Reader / Answerer** | raw material 全文（KV cache warm） | 产出 digest；回答 questioner 的问题；标定位 | 被动应答，不主动引导 |
| **Questioner** | raw material 全文 + digest + 已有 Q&A + canonical 列表 | 系统性提问，exhaust 材料 | 只问源内知识；不注入外部知识 |
| **Reviewer** | digest + 产出的 draft cards + grep access to raw material + grep access to KB | quit-audit：覆盖率检查 + 源忠实抽查 | 不改 card body，只判 pass/reject/补问 |

### 2.1 Sub-stage: Digest Production

| 维度 | 定义 |
|---|---|
| **scope** | Reader 从全文产出一份轻量"地图"——**主要供 reviewer 做覆盖率检查**，也供 questioner 参考 |
| **context** | raw material 全文（一次性全读） |
| **boundary-read** | `data/raw/<source_type>/<source_id>/text.txt` |
| **boundary-write** | 无（digest 是 in-memory / in-session 中间产物，不落盘） |
| **input schema** | raw material 全文 |
| **output schema** | digest object: |

```yaml
digest:
  scope: string          # 1-2 句: 材料是什么、覆盖什么、不涉及什么
  toc:                   # 章节骨架
    - section: string    # 章节标题
      summary: string    # 一句话概述
  core_claims:           # 5-15 条核心主张（方向，不是答案）
    - string
  terms:                 # 关键术语/人名/模型名
    - string
```

| **artifacts** | 无落盘 artifact（session 内中间产物） |
| **用途** | reviewer 的覆盖率 checklist（core_claims 必须被 cards 覆盖）；questioner 的补充参考（非唯一输入） |

### 2.2 Sub-stage: Questioning Dialogue

| 维度 | 定义 |
|---|---|
| **scope** | Questioner 基于**全文 + digest**向 reader 提问，reader 从源回答，直到 questioner 判定 SATISFIED |
| **context** | questioner: **full material + digest** + 已有 Q&A + 已产出 canonical 列表；reader: full source (KV cache warm) |
| **boundary-read** | questioner: raw material 全文 + digest + accumulated Q&A + 现有 KB 的 canonical_concept 列表；reader: raw material 全文 |
| **boundary-write** | 无（Q&A 对是 session 内中间产物） |
| **input schema** | questioner receives: full material + digest + prior Q&A pairs + canonical list |
| **output schema** | Q&A pairs: |

```yaml
qa_pairs:
  - question: string           # questioner 的问题
    answer: string             # reader 的回答
    source_refs:               # reader 引用的源位置
      - location: string       # 行号 / JSON pointer / 节标题
        quote: string          # 原文片段（可选）
    round: int                 # 对话轮次
```

| **artifacts** | 无落盘（session 内） |
| **convergence** | SATISFIED = (a) questioner 判断材料已被系统性 exhaust + (b) 无开放追问链 + (c) 无新原子 idea |

**Questioner 提问策略**（五阶段）：

- **Phase 1 -- 广度扫描**：对材料的每个主要章节/主张提开放性问题。最少轮次触碰全域。
- **Phase 2 -- 深度追问**：识别"提到但未展开的机制/区分/条件"，逐一追问。每追问链 1-3 层。
- **Phase 3 -- 评判性提问**：对已有回答提评估性问题——局限、假设、与主流理解的差异。
- **Phase 4 -- 批判性/对比性提问**：追问材料**内部**张力——"第三节和第五节是否矛盾？"（不引入材料外知识。）
- **Phase 5 -- 覆盖率自检**：回顾已问范围，判断是否有遗漏区域。

**Questioner 拥有全文的意义**：questioner 不是从摘要出发"盲问"，而是能看到全文细节，从而提出更精准、更深入的问题。digest 不再是 questioner 的唯一视野——它是 reviewer 的覆盖率工具。

**关键机制**：reframe 在每轮对话之间（非最后一步），这样 questioner 在下一轮看到"已产出的 canonical_concept 列表"，避免重复追问已覆盖概念。

### 2.3 Sub-stage: Q&A --> Card Reframing

| 维度 | 定义 |
|---|---|
| **scope** | 把 Q&A 对转化为自足的原子知识卡 + metadata + typed footnotes |
| **context** | Q&A pairs + 现有 KB canonical_concepts（供 grep 复用） |
| **boundary-read** | 现有 KB `canonical_concept` 列表（grep） |
| **boundary-write** | `outputs/llm_wiki/drafts/cards/` + `outputs/llm_wiki/drafts/justification/` |
| **input schema** | Q&A pairs (from S2.2) |
| **output schema** | draft card + draft justification journal (schemas below in S6) |
| **artifacts** | `drafts/cards/<slug>.md` + `drafts/justification/<slug>.md` |

**转化规则**：
- (a) 对话体 --> 知识陈述体（"问：X 是什么？答：X 是..." --> "X：一种...的机制"）。
- (b) 补 metadata：canonical_concept（grep 现有 KB 复用/新铸）、aliases（从回答变体词提取）、summary（稠密 grep 靶子）。
- (c) typed footnote 锚定：把回答中引用的源位置转化为 `## Footnotes`（`[^src-N]: ...`）。
- (d) justification journal 创建：写 creation 事件（生成方式 + 源证据 + 范围论证）。

**一对一 vs 多对一**：默认一个 Q&A = 一张卡。广度问题的回答若含多个独立 idea --> 拆多张；追问链若共同构成一个原子 idea --> 合一张。判断标准：能否在不引用兄弟卡的情况下被理解。

### 2.4 Sub-stage: Review / Quit-Audit

| 维度 | 定义 |
|---|---|
| **scope** | 独立 reviewer 检查产出卡的覆盖率和源忠实性，防止 early stop |
| **context** | digest (coverage checklist) + 产出的 draft cards |
| **boundary-read** | digest + draft cards + raw material（**grep access only**，按需验证特定 claim）+ KB cards（grep access，查重叠） |
| **boundary-write** | 无（reviewer 不改 card body，只输出审查结果） |
| **input** | digest + draft cards from S2.3 |
| **output** | audit verdict: |

```yaml
quit_audit:
  coverage:                    # 逐条检查 digest.core_claims
    - claim: string            # digest 中的核心主张
      covered_by: [slug]       # 哪些 card 覆盖了此主张
      verdict: covered | gap   # 是否有卡覆盖
  source_spot_check:           # 抽样源忠实性验证
    - card: slug
      claim_checked: string    # 卡中被检查的陈述
      source_location: string  # grep 找到的源位置
      verdict: supported | unsupported | ambiguous
  overall: pass | needs_more_questions
  gap_questions: [string]      # 若 needs_more_questions，补问清单
```

| **artifacts** | 无落盘（session 内中间产物） |
| **机制** | (1) 覆盖率检查：逐条比对 digest.core_claims vs 产出卡的 summary/body，标记 gap；(2) 源忠实抽查：抽 3-5 张卡，grep raw material 验证关键 claim 是否有源支撑 |
| **触发** | questioner SATISFIED 后触发；若 verdict = needs_more_questions --> 补问清单回传 questioner 继续 |

### 2.5 Sub-stage: Inline Fusion Check

| 维度 | 定义 |
|---|---|
| **scope** | 新 draft 卡与已有 KB 的重叠检测（card-body 级，非 source 级） |
| **context** | 新 draft cards + 现有 KB cards（body/summary） |
| **boundary-read** | `kb/cards/*.md`（现有 active 卡的 body/summary）+ `kb/archive/*.md`（archive 在 grep scope 内） |
| **boundary-write** | draft cards 的 frontmatter（标记 skip/link/keep） |
| **input** | draft cards from S2.3 (passed review) |
| **output** | 每张 draft 的 fusion verdict: `keep` / `skip` (duplicate) / `link` (related-but-distinct) |
| **artifacts** | draft cards updated with verdict; link 信息写入 typed footnotes (`[^card-N]`) |
| **mechanism** | grep canonical_concept + aliases（zh/en/同义词多轮改写） against KB --> 命中则 Read matching card body --> LLM judge same-claim / related / different |
| **grep scope** | active cards (`kb/cards/`) + archive (`kb/archive/`) 均在 grep scope 内 |

### 2.6 Reader 角色契约

Reader 是**被动应答者**，不主动引导、不建议问什么、不评价问题质量。好回答四标准：
- **源忠实**：只基于手中材料，不注入外部知识。
- **定位精确**：引用具体位置（"第三节第二段"/"JSON pointer $.section.3"），使 typed footnote 锚定可操作。
- **卡片就绪**：信息量足以支撑一张原子卡——不过简也不过长。
- **显式标注不确定性**：材料未讨论 --> 说"材料未直接讨论此点"，不编造。

---

## 3. Stage: Ingest

> **Scope**: 把通过 fusion check 的 draft cards 移入 KB active view。**脚本，不用 LLM。**

| 维度 | 定义 |
|---|---|
| **scope** | drafts --> active KB（移动/置位，无 LLM body 复制） |
| **context** | draft cards + KB 目录结构 |
| **boundary-read** | `outputs/llm_wiki/drafts/cards/` + `drafts/justification/` |
| **boundary-write** | `outputs/llm_wiki/kb/cards/` + `kb/justification/` + `kb/indexes/` |
| **input** | draft cards with verdict=`keep` or verdict=`link` |
| **output** | active KB cards (status: accepted) + index |
| **artifacts** | `kb/cards/<slug>.md`（status: accepted）+ `kb/justification/<slug>.md` + `kb/indexes/cards.md`（regenerated） |
| **硬约束** | **禁止 LLM 复制 body**——只做 frontmatter status flip + 物理移动 + index 重建 |

---

## 4. Stage: Evolve / Governance

> **Scope**: 在 KB 上做 dedup + canonical normalization + distinction linking。best-effort。Mode B (synthesis) deferred。

| 维度 | 定义 |
|---|---|
| **scope** | 找到近重复卡 --> 标 superseded --> 移入 archive --> 归一化 canonical；建立 distinction link（typed footnote） |
| **context** | 完整 active KB + archive（grep scope） |
| **boundary-read** | `kb/cards/*.md` + `kb/archive/*.md` + `kb/indexes/` + 倒排表 |
| **boundary-write** | `kb/cards/`（update frontmatter / add cards）+ `kb/archive/`（move superseded）+ `kb/justification/`（append entries）+ `kb/indexes/`（rebuild） |
| **input** | active KB snapshot (all accepted cards) |
| **output** | cleaner KB: fewer dups, normalized canonicals, distinction links |
| **artifacts** | moved cards in `kb/archive/<slug>.md`（status: superseded, superseded_by: <id>）; updated `kb/indexes/cards.md`; updated `related:` via derive script |
| **mechanism** | grep canonical_concept/aliases/summary（zh/en/同义词多轮改写）--> 找 count>=2 簇 --> agent 判 merge/distinction/keep --> superseded 移 archive |
| **grep scope** | active cards + archive 均在 grep scope 内；archive 排除出 view（index） |

### 4.1 Link-as-Distinction 机制

当 governance 判定两张卡 **related-but-distinct**（同主题、不同角度/立场/范围），执行：

1. **双向 typed footnote**：两张卡各自加一条 `[^dist-N]` footnote，指向对方，narrative 说明区分点。
   - 例：卡 A 加 `[^dist-1]: [card-B](card-B.md) -- 本卡聚焦 X 的机制，B 聚焦 X 的局限性`
   - 例：卡 B 加 `[^dist-1]: [card-A](card-A.md) -- 本卡聚焦 X 的局限性，A 聚焦 X 的机制`
2. **`related:` 自动派生**：derive 脚本从 `[^card-N]` 和 `[^dist-N]` 中提取，重建 `related:` 列表。
3. **jj 记录**：两张卡的 justification journal 各 append 一条 governance 事件（谁和谁做了 distinction，为什么）。

**比较知识 = distinction footnote**：不产生单独的"比较卡"。比较知识以 `[^dist-N]` 的形式 inline 在相关卡中——governance 的产出是 footnote，不是新卡。

### 4.2 Merge-WHY 约定

当 governance 判定 merge（N 张卡 --> 1 张 hub 卡），执行：

1. **新 hub 卡创建**：综合 body + 合并 footnote（`[^src-N]` 指向各源 + `[^card-N]` 指向各原卡）。
2. **完整 merge 论证写入新卡的 jj**：justification journal 的 governance 事件中记录完整的 WHY——为什么 merge、哪些卡被合并、合并后知识如何组织。**merge 的完整推理只存在于新卡的 jj 中**。
3. **旧卡只加 pointer**：被 superseded 的旧卡在 frontmatter 加 `superseded_by: <hub-id>`，jj 中 append 一条 deprecation 事件（一行 pointer："合并入 <hub-id>，完整论证见该卡 jj"）。
4. **旧卡移入 archive**：`kb/archive/<slug>.md`，status 置为 superseded。

---

## 5. Stage: Synthesize (Mode B) -- DEFERRED

> **Scope**: 跨源综合——连接/抽象/找 gap。**v4 不实施，deferred to future。**

| 维度 | 定义 |
|---|---|
| **scope** | questioner 基于 card-cluster summaries 提问，reader 回答，产出 bridge/abstract 卡 + collect-requests |
| **input** | card-cluster summaries + cross-cluster bridge-edge list |
| **output** | synthesis cards + collect-requests |
| **artifacts** | `kb/cards/<slug>.md` + `kb/collect_requests/<slug>.yaml` |
| **status** | deferred -- spec 见 `questioning_loop_design.md` S2 |

---

## 6. Schemas（数据模型）

### 6.1 Card Schema (frontmatter)

```yaml
---
id: <stable-ascii-slug>
title: <中文短标题>
status: draft | accepted | superseded
card_type: <自由描述，可选>
tags: []                           # 自由描述，可选，不是 taxonomy
created_time: <ISO8601+08:00>
edited_time: <ISO8601+08:00>
edited_entity: llm
source_ids: [<material_id>]
justification: ../justification/<id>.md
canonical_concept: <kebab-case-english>    # grep 锚点；建卡时 grep 复用
aliases: [<中文变体>, <英文变体>, ...]      # 真实表层串
summary: <一行稠密 grep 靶子>               # 含 canonical + key terms + 核心论断
related: []                        # AUTO-DERIVED from [^card-N] + [^dist-N] footnotes（脚本派生，不手维护）
# ── governance fields (only when applicable, not in default template) ──
# superseded_by: <id>             # governance 添加：仅在 status=superseded 时
---
```

**与 v1 的差异**：
- `provenance_card` --> `justification`：指向 justification journal（append-only 日志），替代一次性 provenance
- 移除 `card_class`（Mode B deferred，source_grounded 是唯一活跃类型，无需字段）
- 移除 `derived_from`（Mode B deferred，无 synthesis 卡）
- `superseded_by` 不在默认模板中：仅由 governance 添加

### 6.2 Card Body 结构

```markdown
<知识陈述体正文 -- 自足、密集、有据>

正文中使用 typed footnote markers: text[^src-1]、text[^card-1]、text[^dist-1]

## Footnotes

[^src-1]: `data/raw/paper/example/text.txt` -- 行 42-50 -- "原文引用片段"
[^src-2]: `data/raw/webpage/example/text.txt` -- S3.2 -- "另一段引用"
[^card-1]: [sibling-card-id](sibling-card-id.md) -- 本卡与该卡共享 X 概念的基础定义
[^dist-1]: [related-card-id](related-card-id.md) -- 本卡聚焦 X 的机制，该卡聚焦 X 的局限性
[^url-1]: <https://example.com/resource> -- 外部参考资源描述
```

### 6.3 Justification Journal (jj) Schema

> 替代原 provenance schema。每张卡一个 jj 文件，append-only 日志。记录卡的完整生命周期事件。

```yaml
---
schema: justification_journal.v1
card: ../cards/<id>.md
created_time: <ISO8601+08:00>
---
```

Body = 按时间顺序 append 的事件条目。每条事件格式：

```markdown
## <event_type> | <ISO8601+08:00>

<事件内容，<=20 行>
```

**6 种事件类型**：

| event_type | 触发时机 | 内容 |
|---|---|---|
| `creation` | 卡首次创建（extract reframing） | 生成方式（Mode A round N, question）+ 源证据（关键原文 + 位置）+ 范围论证 |
| `review` | reviewer quit-audit 通过 | 覆盖率判定 + 源忠实抽查结果（如有） |
| `fusion` | inline fusion check 判定 link | 与哪张卡比较、verdict（keep/link）、理由 |
| `governance` | governance 阶段操作 | merge-WHY（完整论证）/ distinction-link 理由 / canonical 归一化记录 |
| `evolution` | 后续编辑/增补 | 什么改了、为什么改 |
| `deprecation` | 卡被 supersede | pointer："合并入 <hub-id>，完整论证见该卡 jj" |

**约束**：
- 每条事件 **<=20 行**
- 每个 jj 文件 **<=6 条事件**；超过时执行 **rollup**（见 S6.3.1）

### 6.3.1 Rollup 机制

当 jj 条目达到 6 条，执行 rollup：

1. 前 4 条事件压缩为 1 条 `## rollup | <timestamp>` 条目（<=20 行摘要）
2. 最近 2 条事件保持原样
3. rollup 后文件 = 1 rollup + 2 recent = 3 条，腾出空间继续 append
4. rollup 摘要保留：关键决策、源追溯链、重要 governance 操作的结论
5. 完整历史可通过 git history 回溯

### 6.4 Collect-Request Schema (future, for Mode B)

```yaml
id: cr-<timestamp>-<slug>
type: collect-request
question: <string>
context_cards: [<card-ids>]
expected_contribution: <string>
priority: high | medium | low
source_hints: [<string>]
```

Artifact: `kb/collect_requests/<id>.yaml`

### 6.5 Typed Footnote Contract

> 所有 citation 统一为 typed footnote，在 `## Footnotes` section 中展开。footnote ID 使用类型前缀，使 target domain 在 marker 处即可识别。

#### 四种 footnote 类型

| type prefix | 用途 | 谁产出 | 格式 |
|---|---|---|---|
| `[^src-N]` | 原始材料引用 | extract reframing | `[^src-N]: [target](material_path) -- line/pointer -- "quote"` |
| `[^card-N]` | 同 loop KB 卡引用 | extract (inline fusion) / governance | `[^card-N]: [card-title](card-id.md) -- narrative` |
| `[^dist-N]` | 区分标注（governance 产出） | governance (link-as-distinction) | `[^dist-N]: [card-title](card-id.md) -- "本卡聚焦 X，该卡聚焦 Z"` |
| `[^url-N]` | 外部 URL | extract / governance | `[^url-N]: <https://...> -- narrative` |

#### 格式规范

```
[^type-N]: [target](path) -- narrative
```

- `type`：`src` / `card` / `dist` / `url` 四选一
- `N`：同类型内递增编号（从 1 开始）
- `target`：链接文本（材料文件名 / 卡标题 / URL）
- `path`：相对路径或 URL
- `narrative`：`--` 后的说明文字（src 类型含位置 + 引用片段；card/dist 类型含关系说明）

#### Body 使用规则

- 在正文中用 `text[^src-1]` 标记具体 claim 的源支撑
- 多 target 同一 anchor：链式标记 `text[^src-1][^card-2]`
- 每个 `[^id]` marker 必须有且仅有一个 `[^id]: ...` 展开
- `## Footnotes` section 放在 card body 末尾，按首次出现顺序排列

#### 自动派生规则

- `related:` frontmatter 由脚本从 `[^card-N]` 和 `[^dist-N]` footnotes 中提取 card id，生成 union
- `source_ids:` 可从 `[^src-N]` footnotes 中提取 material id（可选）
- `[^url-N]` 不进入 `related:` 或 `source_ids:`
- 脚本幂等——body 编辑后重跑即可刷新

---

## 7. Artifacts 目录结构

```
loops/<loop_id>/
+-- outputs/llm_wiki/
|   +-- drafts/
|   |   +-- cards/<slug>.md              # Stage 2 output (draft)
|   |   +-- justification/<slug>.md      # Stage 2 output (draft jj)
|   +-- kb/
|       +-- cards/<slug>.md              # Stage 3 output (active)
|       +-- archive/<slug>.md            # Stage 4 output (superseded, grep-visible, index-excluded)
|       +-- justification/<slug>.md      # Stage 3 output (append-only per-card journal)
|       +-- indexes/cards.md             # Stage 3+4 rebuild (active-only view)
|       +-- collect_requests/            # Stage 5 output (future, Mode B)
+-- run/
|   +-- <source_id>.json                 # per-material run-record (stage/status/attempts)
+-- queue.jsonl                          # work queue for BSP scheduler
+-- skills/
    +-- questioning/SKILL.md             # questioner 的 SOP
    +-- reader/PROMPT.md                 # reader 的应答契约
    +-- reviewer/PROMPT.md               # reviewer 的 quit-audit 契约
```

**目录说明**：

| 目录 | 内容 | grep scope | index (view) |
|---|---|---|---|
| `kb/cards/` | active 卡 | YES | YES |
| `kb/archive/` | superseded 卡 | YES（grep 可见，用于溯源和去重检查） | NO（排除出可消费 index） |
| `kb/justification/` | per-card append-only journal | YES | NO（不直接索引，通过卡的 `justification:` 字段链接） |

---

## 8. 阶段间数据流（总览）

```
                    +----------------------------+
 source spec --->   | 0. COLLECT                 | ---> data/raw/<source>/text.txt
                    +----------------------------+
                                |
                                v
                    +----------------------------+
 raw material --->  | 1. EXTRACT                 |
                    | coordinator dispatches:    |
                    |  digest (coverage map)     |
                    |  questioner <-> answerer   |
                    |  reframe -> draft cards    |
                    |  reviewer quit-audit       |
                    |  inline fusion check       |
                    +----------------------------+ ---> drafts/cards/*.md + justification
                                |
                                v
                    +----------------------------+
 draft cards --->   | 2. INGEST (script)         | ---> kb/cards/*.md (active)
                    +----------------------------+      + kb/justification/*.md
                                |                       + kb/indexes/cards.md
                                v
                    +----------------------------+
 active KB --->     | 3. EVOLVE / GOVERNANCE     | ---> kb/archive/*.md (superseded)
                    | distinction link (footnote)|      + canonical normalized
                    | merge -> hub + archive     |      + [^dist-N] added
                    | jj append                  |
                    +----------------------------+
                                |
                                v (future)
                    +----------------------------+
 card clusters ---> | 4. SYNTHESIZE (Mode B)     | ---> synthesis cards + collect-requests
                    +----------------------------+
```

---

## 9. 待讨论（详细实现阶段）

定了管线规格后，下一步逐个讨论实现：

1. **Questioning Skill (SKILL.md)** -- questioner 的具体 SOP（5 阶段提问策略、SATISFIED 判据、boundary）。
2. **Reader Prompt** -- reader 的应答契约（源忠实、定位精确、卡片就绪、不确定性标注）。
3. **Reviewer Prompt** -- reviewer 的 quit-audit 契约（覆盖率检查流程、源忠实抽查抽样策略、verdict 输出格式）。
4. **Digest Template** -- digest 生成的精确 prompt + 格式。
5. **Reframing Logic** -- Q&A --> card 的转化规则（一对一 vs 拆/合判据、metadata 填写、typed footnote 锚定、jj creation 事件）。
6. **Inline Fusion Logic** -- grep 策略（zh/en/synonym 改写）+ 判决标准。
7. **Ingest Script** -- 文件移动 + frontmatter flip + index rebuild。
8. **Governance Agent Spec** -- dedup 判据 + distinction-link 机制 + merge-WHY jj 约定 + archive 流程 + canonical normalization 规则。
9. **Orchestrator Logic** -- per-material dispatch + run-record + queue drain + reporting。
10. **Skills/Agents 的文件系统布局** -- 怎么组织成 plugin 结构。
11. **Justification Journal 管理** -- rollup 触发 + 脚本实现。
12. **Typed Footnote Derive Script** -- 从 typed footnotes 派生 `related:` + `source_ids:` 的脚本规格。
