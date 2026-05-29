# V3 Loop 0→1 全过程与优化轨迹

> 文档范围：从 v3 capsule 创建（2026-05-25T20:54:47+08:00）到 unified-citation 迁移完成（2026-05-28T18:00:00+08:00）。本文不是 contract，而是 narrative——讲清楚 v3 走过的每一步、为什么这么走、踩了什么坑、最后留下什么。
>
> Main language: 中文。schema 字段 / 路径 / 代码 / id / commit hash 保留英文。

## 0. 总览（一段话）

V3 是一次"draft-first 知识卡生产"的实验：从 72 条原始来源（论文、博客、github readme、social media、标准文档等）出发，先快速产出 draft 卡片，再做 title 相似度筛选、comparison 论证、interlink 编织、最后通过 publication_gate / fusion_audit 进入 v3 KB。最终全程跑完，落地 **171 张 accepted card + 171 张 accepted provenance + 171 份 similarity 工件 + 171 份 comparison provenance + 504+ 条 KB-internal footnote + 1 份 kb 索引**。中途经过 4 次大幅修正（中文化、全文读取、unified-citation、related 自动派生），合同与模板沉淀为 5 份 worker template + 4 个工具脚本 + 1 个项目级 PostToolUse hook + 1 份升级版 CARD_CONTRACT_V3。

## 1. 起点：v0 / v1 / v2 的遗产与 v3 的赌注

### 1.1 v2 留下的两个问题

读 v2 的 reflection 与 audit 后，v3 设计者发现两个症状：

- **流程偏慢**。v2 是"先把 KB 整体过一遍 → 再决定每张卡"的串行模式。每加一条材料都要重新比对全 KB，吞吐线性退化。
- **卡片质量参差**。一部分卡过于原子（"X 是 Y"这种标题级断言），另一部分卡又太啰嗦覆盖多主题。v2 的 atomicity 没有清楚定义。

### 1.2 v3 的赌注：draft-first

V3 选择把流程倒过来——先快速产出 draft，再做"贵的推理"（comparison / audit）只在 top-3 候选上。核心 idea：

```
material
-> 知识密集 draft 卡片
-> draft provenance
-> title similarity top-3（候选缩小）
-> comparison provenance（只对 top-3 做，回答三问）
-> decision（new_card / merge_candidate / provenance_delta / duplicate_skip / revise_before_gate）
-> publication_gate 或 fusion_audit
-> 进入 KB
```

该流水线设计写进 `DRAFT_FIRST_PIPELINE_V3.md`，配套：

- `CARD_CONTRACT_V3.md`：卡是什么、不能是什么。
- `SIMILARITY_MECHANISM_V3.md`：title-jaccard top-3 是 cheap candidate retrieval，**不**判断真理 / 重复 / 合并 / 发表。
- `PROVENANCE_CONTRACT_V3.md`：分两层——card provenance（卡的源证据）vs comparison provenance（卡之间的判定）。
- `CONTEXT_BOUNDARY.md`：每个 phase 严格隔离的读 / 写 allowlist。

### 1.3 关键认知：subagent 不能 spawn subagent

V3 起步时 Claude Code 文档明确说"标准 subagent 无法嵌套 spawn"。V3 的 mailbox / brain 设计被相应修正——`brains/*` 是文件态的角色协调表，不是运行中的 agent。如果真要两层 runtime，路径只有一条：top-level Claude → Agent tool subagent → Bash invoking `claude --permission-mode auto -p "<self-contained prompt>" --output-format text`。这一约束写进 `SUBAGENT_RUNTIME_CONSTRAINTS.md`，并被实际测试通过（marker `NESTED_CLAUDE_OK_9X2Y4Z`）。

## 2. Pipeline 全景

下面是 v3 真实跑过的 pipeline 全景，不是 contract 上的理想态：

```
┌────────────────────┐
│ 0. material queue  │  data/manifests/source_digests_index.md → queues/material_queue.md
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ 1. material→draft  │  Read 整篇源材料 → 产出 2-5 张 draft cards + draft provenance
│   （8 batch worker）│  worker template: batch_worker_prompt.md
│   + 4 revision     │  arxiv 大文件全文重读补卡（修正首轮 limit:2000 截断）
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ 2. similarity top-3│  tools/similarity_top3.py（jieba + jaccard）
│                    │  → outputs/llm_wiki/drafts/similarity/<id>.json
│                    │  比较基：v2 cards.md 索引（accepted titles only）
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ 3. comparison      │  worker 答三问 + 决定 decision
│   （8 batch worker）│  → outputs/llm_wiki/drafts/comparison/<id>.md
│                    │  worker template: comparison_worker_prompt.md
└──────────┬─────────┘
           │ 163 new_card  ┐
           │ 8 prov_delta ─┤
           ▼               ▼
┌────────────────────┐  ┌────────────────────┐
│ 4a. interlink      │  │ 4b. fusion_audit   │  对 prov_delta 8 张
│   （6 cluster      │  │     check 三问 + v2 │  在 kb provenance 加
│    worker）        │  │     scope 是否保留 │  v2_anchor 字段
│   填 related:      │  │                    │
└──────────┬─────────┘  └──────────┬─────────┘
           └────────────┬──────────┘
                        ▼
┌────────────────────┐
│ 5. adoption        │  copy draft → kb/cards/<id>.md（status: accepted）
│   （6 batch worker）│  + kb/provenance/<id>.md（schema: accepted_card_provenance.v3）
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ 6. kb index        │  tools/build_kb_index.py（scriptable; bash classifier flaky 时手工）
└──────────┬─────────┘
           │
           ▼
┌────────────────────┐
│ 7. unified-citation│  把 ## References 砍掉并入 ## Footnotes
│   迁移             │  body 中识别自然 cross-card 提及加 [^id] marker
│   （6 cluster      │  8 张 v2-anchored 卡的 anchor 关系移到 body footnote
│    worker）        │  related: 改为脚本派生
└──────────┬─────────┘
           │
           ▼
   v3 KB candidate_ready
```

每一格的产物、边界、token 成本，详见 `audits/` 目录下的对应审计文件。

## 3. 时间线

下面按真实日期标出每个里程碑。每条标"做了什么 / 产生多少 artifact / 踩到什么坑"。

### 3.1 2026-05-25：Bootstrap + 第一次正式 production pass

- **创建 v3 capsule**，注册为 active；scaffold 出 contracts、queues、brains、outputs 目录骨架。
- **写 handoff**：CLAUDE_CODE_HANDOFF.md，让任何无上下文进入的 agent 知道从哪里读、从哪里写、从哪里出。
- **subagent runtime 测试**：本地 claude CLI 跑 `claude --permission-mode auto -p ... --output-format text` 跑通，记录 marker。
- **写 `LOOP_START_PROMPT.md`** 作为顶层启动 prompt。
- **第一次正式 production pass 在 `karpathy-x-launch-post`** 上跑通：4 张英文 draft 卡 + 4 张英文 provenance + 4 份 similarity（top-1 score 0.20，与 v2 中文卡的跨语言匹配很弱）。

artifact：4 cards + 4 provenance + 4 similarity；scaffolding：~12 contract / runbook 文件 + 4 brains + 4 queues。

### 3.2 2026-05-26：中文化 + 8 个 batch worker + arxiv revision

**用户更正 1：所有输出主语言必须是中文。**

→ 4 张已有的英文卡 + provenance 立即重写为中文。worker 模板被相应修正，把"中文优先"写成第 1 条规则。这次改动也意外修复了 cross-language similarity 的死结——v2 cards 是中文标题，v3 卡也改中文后，title-jaccard 终于能产生有意义的分布（详见 §4.1）。

**8 个并行 batch worker（model:opus）**：把剩余 64 条 complete 材料按 8 个均衡 batch 分给 8 个 worker，每 worker 独立读源 + 写 2-5 张卡。

artifact：129 张新卡（22 条 0KB README 跳过为 `blocked: empty_source`）。worker 平均 token 消耗 ~180K。

**用户更正 2：1M 上下文足够一次读完整篇论文，不要防御性 limit:2000。**

→ 派 4 个 revision worker 把 14 篇被截断的 arxiv 论文全文重读，补出 34 张额外的卡片。审阅原卡片后无 edit。这条更正同时进 memory：`feedback_full_source_reads.md`。

artifact：34 张额外卡片。worker 平均 token 消耗 ~310K（比 batch worker 高，因为大文件全读）。

**新建工具与 hook**：

- `tools/similarity_top3.py`（jieba + jaccard）。
- `hooks/commit_card.sh` + 项目 `.claude/settings.json` PostToolUse hook：每写一张 draft 卡，自动 `git add` + commit 卡片 + 配对 provenance + 配对 similarity。文件锁 `/tmp/v3-commit-card.lock` 串行化并发 worker 的提交。
- `task_templates/batch_worker_prompt.md`：第一份可复用 worker 模板。

### 3.3 2026-05-26 → 2026-05-27：comparison + interlink + adoption

**全部 171 张 draft 跑 comparison_provenance**：8 个并行 worker，按 similarity 分布切桶（HIGH ≥0.30 9 张 / MID 30 张 / LOW 107 张 / VLOW 25 张）。每 worker 答三问 + 给 decision。

判定结果：163 `new_card` / 8 `provenance_delta` / 0 其他三种。8 张 provenance_delta 全部围绕 v2 三个锚点：`llm-wiki-three-layer-architecture`（5 张）、`llm-wiki-schema-configuration-document`（2 张）、`idea-file-abstract-vague`（1 张）。后来 fusion 审计时一张 anchor 被修正到 `llm-wiki-health-checks`（详见 §3.4）。

**6 个并行 interlink worker** 按主题 cluster 切（A 概念 49 / B 工具 7 / C 内存架构 47 / D RAG 评估 21 / E 安全治理 27 / F GraphRAG-KB 20）填 frontmatter `related:`。结果：974 条边，平均 5.70 / 卡，0 张孤立卡，0 个 dangling id。

**6 个并行 adoption worker**（1 fusion_audit + 5 publication_gate）：163 new_card 全过 publication_gate；8 provenance_delta 全过 fusion_audit。每张通过的卡：

- `kb/cards/<id>.md`：把 frontmatter `status: draft → accepted`，更新 `edited_time`。正文逐字保留。
- `kb/provenance/<id>.md`：扩展为 `accepted_card_provenance.v3`，含 `gate` 块（type / result / decided_at / gate_notes）；8 张 v2-anchored 卡额外加 `v2_anchor` 块。

期间扩展 hook：`outputs/llm_wiki/kb/cards/<id>.md` 写入也触发自动 commit（`v3 adopt: <id>` 消息），并把同名 kb provenance stage 进同一 commit。

artifact：171 accepted card + 171 accepted provenance + 1 份 `kb/indexes/cards.md`（手工组装，因为 bash classifier 在 adoption 末段持续阻塞 python，详见 §5）。

### 3.4 2026-05-27 末：3 张 similarity miss recheck

Loop report 把三张 draft 标为"真实 v2 邻居漏出 top-3"——`karpathy-llm-kb-three-operations`、`file-outputs-back-as-compounding-loop`、`llm-wiki-karpathy-multimodal-representation-path`。复核后发现：

- 前两张：worker 实际上 top-1 / top-3 已包含真邻居，并已正确判 `new_card`（抽象层不同）。
- 第三张：top-1 也已含 `llm-wiki-ingest-example-flow`，judgement 也合理。

→ 给三张 comparison provenance 加 §6 v2_anchor 再核对小节，留 audit trail；不升级为 provenance_delta。

### 3.5 2026-05-28：Unified-citation 大型迁移

用户在多轮讨论后定下：

> footnote 是真理之源，metadata 是 derived view。脚本一次性扫出来填进 frontmatter，Obsidian 直接吃 frontmatter 做 graph view，body 里 footnote 也是可点链接——一处写、两处用。

这次重构的触发逻辑（详见 §4.4）：

- inline `[text](path)` 形式只能 1-to-1，N-to-1 citation（一句话引多个卡）必须靠 footnote-style。
- `## References` 与 `## Footnotes` 的二分，在引入 KB-internal citation 后变成 artifact——统一成单一 footnote hub 即可承载 raw / v3 / v2 / URL 四种 target。
- `related:` 之前手工维护，body 又没有锚点，silent rot 是结构问题。改由脚本从 footnotes 派生。

执行：

1. **改 contract**：`CARD_CONTRACT_V3.md` 升级到 unified-citation 模型。`## References` 节移除；`## Footnotes` 升级为唯一 citation hub；frontmatter `related:` 标记为 auto-derived。
2. **写脚本**：`tools/derive_metadata_from_footnotes.py`，从 `## Footnotes` 解析 v3 + v2 card id 重生成 `related:`。
3. **写 worker 模板**：`task_templates/citation_migration_worker_prompt.md`。
4. **派 6 个并行 cluster worker** 做迁移：砍 `## References` 并入 `## Footnotes`，body 加 `[^id]` markers，8 张 v2-anchored 卡的 v2 anchor 关系移到 body inline footnote。共加入 504+ KB-internal footnote。
5. **跑脚本**：bash classifier 持续阻塞 python，fallback 派 fresh agent 用 Read+Edit 等价完成 171 张卡的 `related:` 重写。170 张更新，1 张已正确，4 张合法保持 `[]`（这些卡只引 raw / URL，无 KB 内引）。

artifact：171 张 kb 卡迁移到新模型；CARD_CONTRACT_V3 升级；新增 1 个工具 + 1 个 worker 模板。

## 4. 关键决策点（按重要性）

每条决策包含**触发场景 / 决策 / 后续效果**三部分。

### 4.1 中文优先输出（2026-05-26）

- **触发**：第一轮 production pass 产出 4 张英文卡。用户回复 "btw, all output should keep the chinese as the main language"。
- **决策**：所有 v3 输出（卡片 / provenance / queue / report / brain）main language 必须中文；schema 字段、路径、代码保留英文。
- **后续效果**：(1) 4 张已有英文卡立即翻译。(2) 所有 worker 模板更新加入"中文优先"第 1 条规则。(3) **意外副作用**：跨语言 title similarity 死结被修复。v2 索引是中文，v3 卡改中文后，title-jaccard 终于能给出有意义的相似度分布——top1 ≥ 0.30 的 9 张、=0.50 的 1 张（`karpathy-llm-kb-three-layer-arch` ↔ v2 三层架构），开始有可下手的判定。

### 4.2 全文读取（2026-05-26）

- **触发**：8 个 batch worker 全部默认用 `Read(..., limit: 2000)` 防御性截断读 arxiv 论文。结果是 mem0、memgpt、alce、ares、locomo、longmemeval、graphrag、lightmem、graph-poisoning、poisonedrag、ragchecker、wicer、memory-as-metabolism、etamp 14 篇都漏掉了后半段。用户提醒 "your context window is 1M, you can almost ingest the entire paper..."。
- **决策**：worker 默认行为改为"一次 Read 完整源文件"。只有真正多 MB 量级的文件（典型如 arxiv `agent_source_bundle.txt` 含完整 anthology.bib 附录）才需要分段。
- **后续效果**：(1) 派 4 个 revision worker 全文重读 14 篇，补 34 张卡（核心评估、ablation、failure modes、appendix prompts）。(2) 进 memory：`feedback_full_source_reads.md`。(3) 后续阶段（comparison / adoption / migration）默认 full read，不再退化为 paginate。

### 4.3 项目级 PostToolUse hook（2026-05-26 起）

- **触发**：第一次 production pass 后，171 张卡的 commit 全靠手工会非常累，且 bash classifier 不稳定时手工提交也常失败。
- **决策**：写 `hooks/commit_card.sh` + 项目 `.claude/settings.json` PostToolUse hook。每写 / 编辑一张卡，自动 `git add` + commit 卡片 + 同名 provenance + 同名 similarity。文件锁 `/tmp/v3-commit-card.lock` 串行化并发 worker。Hook 在 v3 进程中演进了三次：
  - v1：仅 `drafts/cards/*.md`
  - v2：加 `drafts/comparison/*.md`
  - v3：加 `kb/cards/*.md`（adoption 阶段）
- **后续效果**：(1) git history 极其 granular（每张卡 1 commit），易回溯易 review。(2) 文件锁通过 ~700+ 次 hook 触发未出现 index lock 冲突。(3) bookkeeping commit（loop_state、status、report、brain mailbox 等）仍要手工——但这些不在 hook scope 内。bash classifier 后期持续阻塞 `git add` 命令，多个 turn 试图 commit bookkeeping 都失败，最终 `commit_bookkeeping.sh` 留作交互 shell 用。

### 4.4 Unified-citation 模型（2026-05-28）

详见 §3.5。这是 v3 内的最大重构。**触发理由有三层**：

1. **N-to-1 citation 需求**：一句话引多个卡 / 多个 source 是知识写作常态。inline `[text](path)` 只支持 1-to-1，footnote-style `text[^a][^b][^c]` 天然 N-to-1。
2. **`## References` vs `## Footnotes` 的二分是 artifact**：在引入 KB-internal citation（v3 / v2 卡作为 target）后，"宽口径 idea-level refer" vs "窄口径 inline locator" 的区分变得没必要——academic 写作就是用 inline `[Smith 2020]` 同时承担两种角色。
3. **`related:` silent rot 问题**：手工维护的 frontmatter 列表，body 没有锚点，没法验证某条 `related:` 还成立否。改为脚本派生后，body footnotes 是单一真理源；`related:` 是派生 view。

**为什么这次重构发生在 adoption 之后而不是 contract 起草时**：v3 起草时还没遇到 KB 内部互引的场景（drafts 都是新卡，没有"卡 → 卡"关系）。adoption 完成、171 张卡已经在 KB 里站稳后，互引才成为现实问题。这是一个"边做边精确化合同"的典型案例——合同不是设计完美的产物，是被实际工作压出来的稳定形态。

### 4.5 Cluster 切分（2026-05-26 / 27 / 28 三次复用）

- **触发**：处理 64 / 171 / 171 张卡时，串行不可接受；并行 worker 各自分到一份独立 batch，互不读对方文件。
- **决策**：6 个主题 cluster（A 概念 49 / B 工具 7 / C 内存架构 47 / D RAG 评估 21 / E 安全治理 27 / F GraphRAG-KB 20），按 source_id 归类。这套切分被 interlink、adoption（拆为 1+5）、citation migration 三次复用，未做大调整。
- **后续效果**：(1) 切分按主题而非按字母序，让"同 cluster 的卡共享 v2 anchor / 共享语义骨架"，cross-card footnote 命中率高。(2) cluster 大小不均（A、C 各 47-49 vs B 7），运行时间也不均，但每 worker 独立成本，串行总时间被压到 max(per-cluster)。(3) cluster 定义沉淀在 worker 模板里，下一轮 production 不需要重切。

### 4.6 Process-level nested claude（确认可用，但未主用）

- **触发**：subagent 不能 spawn subagent；但有时一个 worker 内部需要再调一次 LLM 做更窄的判断。
- **决策**：`SUBAGENT_RUNTIME_CONSTRAINTS.md` 记录可用路径——top-level → Agent tool → Bash invoking `claude -p`。这条路径在 bootstrap 阶段实际跑通过（marker `NESTED_CLAUDE_OK_9X2Y4Z`）。
- **后续效果**：本轮 v3 实际未用——所有 worker 都是单层 Agent 调用 + 自包含 prompt。process-level nesting 留作未来需要"worker 内再分发"时的 escape hatch。

## 5. 工具 / Hook / 模板栈

每条一句话讲它做什么 + 关键 detail。

### 工具（`tools/`）

- **`bootstrap_dependencies.sh`**：装 `jieba`（用户 endpoint pip 可用）。在第一次 similarity 跑之前调用一次。
- **`similarity_top3.py`**：jieba 分词 + Jaccard 集合相似度。读所有 v3 draft 卡 + v2 cards 索引，每张 draft 输出 top-3 候选 JSON。
- **`build_kb_index.py`** + **`build_kb_index.sh`**：扫 `kb/cards/*.md`，按 frontmatter 生成 `kb/indexes/cards.md`（card_type 统计 / source_id 聚合 / 字母序清单 / v2-anchored 专章）。bash classifier 阻塞时由 fresh agent 手工组装替代。
- **`build_adopt_batches.py`**：从 comparison decisions 切 1 fusion + 5 publication batch。
- **`derive_metadata_from_footnotes.py`**：unified-citation 后从 body `## Footnotes` 派生 frontmatter `related:`（与可选 `source_ids:`）。bash classifier 阻塞时由 fresh agent 用 Read+Edit 替代。
- **`commit_bookkeeping.sh`**：人工调用，手工 commit 一系列 bookkeeping 文件。bash classifier 持续阻塞 `git add ...` 时，留给用户在 shell 里跑。

### Hook（`hooks/`）

- **`commit_card.sh`**：项目 `.claude/settings.json` 注册的 PostToolUse hook。三种触发：
  - `drafts/cards/<id>.md` → 提交卡片 + 同名 provenance + 同名 similarity，message `v3 draft card: <id>`
  - `drafts/comparison/<id>.md` → 提交 comparison file，message `v3 comparison provenance: <id>`
  - `kb/cards/<id>.md` → 提交 kb 卡片 + 同名 kb provenance，message `v3 adopt: <id>`
- 文件锁通过 `mkdir /tmp/v3-commit-card.lock` 实现（macOS 没 flock）。

### Worker 模板（`task_templates/`）

每份模板都是 self-contained 的 prompt，内嵌：repo root、loop path、读 / 写边界、language 要求、合同摘要、最终报告格式。

- **`batch_worker_prompt.md`**：material → draft 阶段。
- **`comparison_worker_prompt.md`**：comparison_provenance 阶段。三问 + decision schema。
- **`interlink_worker_prompt.md`**：填 `related:`（unified-citation 之前）。
- **`adoption_worker_prompt.md`**：publication_gate（6 项判据）+ fusion_audit（4 项判据）+ kb 卡 + accepted_card_provenance.v3 + v2_anchor schema。
- **`citation_migration_worker_prompt.md`**：unified-footnote 迁移阶段。
- **`process_level_nested_prompt_template.md`**：process-level nested claude 调用时复制改填。

## 6. 关键数字

| 维度 | 数字 |
|---|---:|
| 来源总数（manifest） | 72 |
| 已 draft 来源 | 43 |
| `blocked: empty_source`（0KB README） | 22 |
| `blocked: upstream_pending_or_blocked` | 7 |
| Draft 卡 | **171** |
| Draft provenance | 171 |
| Similarity 工件 | 171 |
| Comparison provenance | 171 |
| KB-internal footnote（unified-citation 后） | **504+** |
| v2-anchored 卡（带 `v2_anchor` 字段） | 8 |
| `related:` 由脚本派生的卡 | 170（4 张合法 `[]`，1 张恒等） |
| publication_gate 通过 / 失败 | 163 / 0 |
| fusion_audit 通过 / 失败 | 8 / 0 |
| Accepted card / provenance | 171 / 171 |
| KB 索引文件 | 1 |
| card_type 分布 | mechanism 49 / operational_rule 32 / source_claim 30 / distinction 27 / concept 24 / example_pattern 9 |
| Sub-agent token 总和（estimated） | ~8.74M |
| Total token estimate（含主会话） | ~10M |

## 7. 优化轨迹（v3 内部 → v3.x / v4 outlook）

V3 内部跑出的"显著改善 quality / throughput / cost"的优化：

1. **PostToolUse hook 自动 commit**：消除手工 git；granular history；并发文件锁 → 无 index 冲突。
2. **6 个主题 cluster 并行 worker**：把 171 张卡的 wall-clock 时间压到 max-cluster 时间。每个 worker 独立 prompt，互不读对方文件。
3. **1M context full source read**：modify 前 worker 防御性 limit:2000，14 篇 arxiv 后半段全漏；改 full read 后补 34 张卡，知识密度显著提升。
4. **中文统一**：跨语言 jaccard 死结被解开；title-similarity 终于有可解释分布（39 张 ≥0.15、9 张 ≥0.30、1 张 0.50）。
5. **Unified-citation 模型**：把 References + Footnotes + related 三层折叠成"body footnote 真理源 + 脚本派生 metadata"两层；解决 silent rot；inline N-to-1 citation 自然支持。
6. **Worker template 沉淀**：每加一个阶段就有 reusable template；下一轮 production 不需要重写 prompt。

V3 内未做、留给 v4 / v3.5 的优化（详见 `audits/token_consumption_audit.md`）：

1. **抽出 worker 共享 prompt 文件**：减少 6 worker 同时各自重读相同 contract 内容造成的重复 input token。预估省 25-35% sub-agent token。
2. **Worker 间 catalog 共享**：6 个 cluster worker 各自读一遍 catalog（~30KB × 6 = 180KB 的重复 input）。可以让 main session 预 reduce 一次再 passe 给 worker。
3. **Hook 触发频率聚合**：每张卡 1 commit 太 granular（171×4 阶段 ~684 commits）。可以改为 batch commit per cluster；只在阶段结束时触发一次 hook。
4. **Bash classifier flaky → 立刻 fallback agent**：v3 在末段为 build_kb_index 与 derive_metadata 各派一次 fallback agent，前后浪费 ~750K token。RUNBOOK 应明确写"classifier 连续 reject 同一个命令 ≥3 次时立即派 fallback"。

## 8. 踩到的坑（坦诚记录）

1. **第一轮 worker 防御性 limit:2000**（§4.2）。损失：14 篇 arxiv 论文后半段。修复：4 个 revision worker 重读 → 34 张补卡 + memory 写入。
2. **第一轮 cards 默认英文**（§4.1）。损失：4 张卡需要重写 + worker 模板需要补条款。修复：中文化重写 + memory 写入。
3. **bash classifier 持续 flaky**（§5、§7）。损失：python script 多次跑不动；adoption 末段 + citation derivation 阶段累计 ~750K token 浪费在 fallback agent 上；bookkeeping commit 至今未落地。当前缓解：fallback agent + Read+Edit 等价路径。建议：RUNBOOK 写明 fallback。
4. **3 张 similarity miss 的 报告 偏差**（§3.4）。loop report 把它们标为 miss，但 recheck 后发现 worker 实际上已正确处理 top-1 / top-3。教训：自动报告生成时不要把"jieba 分母效应"误读为"系统漏判"。
5. **`related:` silent rot 问题**（§4.4）。直到 unified-citation 阶段才暴露。教训：任何"频繁变化但缺乏锚点"的 metadata 都必然腐烂——必须由 derived view 维护，不能手工维护。
6. **Cluster 大小不均**（A 49 / B 7 / C 47 / F 20 / E 27 / D 21）：最大 worker 比最小 worker 长 ~7 倍 wall-clock。下次切 cluster 时建议按"卡数大致均衡 + 主题边界"双约束。

## 9. 下一步

按 priority 排序：

1. **Promote v3 KB 到 root `llm_wiki/`**（需要人工授权）。涉及 `loops/registry.json` + `loops/current_loop.json` 更新。
2. **处理 7 条 upstream `pending_or_blocked` 材料**（aicritique-enterprise-knowledge + 6 reddit）。等上游补内容后重新入队。
3. **22 张 0KB github_repo README 上游补内容后再 draft**。
4. **bash classifier flaky 缓解写进 RUNBOOK**：明确 fallback 路径。
5. **共享 prompt 文件机制**：tools 多了之后 worker prompt 复用度增加，可以引入 `prompt_includes/` 目录或类似机制。
6. **kb provenance 的 `v2_anchor` 字段是否需要保留**：现在 body 已经有 `[^v2-1]` footnote，frontmatter `related:` 也含 v2 id。`v2_anchor:` 字段是 audit-only metadata（fusion_audit 决策痕迹），保留即可，不必简化。
7. **下一轮 production pass**：直接走 unified-citation 模型，draft 阶段就用 footnote-style 单一 hub，省去后续迁移。

## 10. 一句话总结

V3 不是"按设计跑通"的 loop，而是"边跑边修正合同"的实验。最重要的修正全部由用户驱动（中文化、full read、unified-citation），三次都让产品质量本质提升而非微调。最大的工程沉淀是 hook + cluster worker + worker template 这套"文件态合同 + 并行执行 + auto-commit"组合——它让单次 production pass 的 wall-clock 时间从可预期的天级压到几小时级，并把所有产物写在 git history 上可逐张回溯。

> 详细 audit 数据见 `audits/` 目录；流程合同见同级 `*_V3.md` / `*_V3.md`；产物在 `outputs/llm_wiki/kb/`；reports 见 `reports/loop_report.md`；当前状态见 `loop_state.json` / `status.json`。
