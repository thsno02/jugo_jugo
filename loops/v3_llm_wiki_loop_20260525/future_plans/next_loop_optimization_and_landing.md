---
status: future_plan
stage: discussion_only
created: 2026-05-29
loop_id: v3_llm_wiki_loop_20260525
topic: optimization_and_landing
note: 高级算法工程师视角的卡点推测 + 解决方案 + pros/cons（设计块），以及精确到 agent 编排的落地块。用户离开期间自主产出，开放问题集中在 §A.3 待回来讨论。
---

# 下一个 loop：优化分析与落地方案

> 两块：**【设计的】**（§A，卡点 / 方案 / pros&cons / 待讨论）与 **【落地的】**（§B，精确到哪个 agent spawn 哪个 agent、给什么上下文、解决什么、期望输出、容错、预期卡点）。
>
> 已敲定基线（对照用）：per-material 可复用流水线（collect→extract→ingest→evolve）；route B 先入库后治理；grep-only + agent-native 召回；Zettelkasten 原子卡、**无 taxonomy**；never-delete 的 storage/view；loop 独立；best-effort + 治理 zen。详见同目录 `next_loop_design.md` 与 `fusion_and_governance.md`。

---

# 【A. 设计的】

## A.1 优化点 × 方案 × pros/cons

每条：**卡点 → 方案候选 → pros/cons → 推荐**。按"会不会真的卡住下一轮"排序。

### A.1.1 grep/Bash 的可用性（澄清：不是限制，是 auto-mode 分类器的瞬时不可用）

- **澄清（更正此前判断）**：grep/bash **没有任何根本限制**，正常情况下照常执行。本会话反复遇到的 `...auto mode cannot determine the safety of Bash...` 是 **auto 模式的安全分类器（一个 LLM）临时不可用**所致：auto 模式跑 Bash 前要让分类器判定命令可否安全自动放行；分类器宕时 harness 宁可拦下也不盲跑。只读工具（Read）不经分类器，故照常工作。这是**瞬时基础设施抖动，不是设计约束**——本会话中途它也恢复过（git commit、git status 都成功）。
- **结论**：grep-only 召回**并不脆弱**；我此前把它拔高成"最高优先级结构性风险"是**判断失误**，在此更正。grep 在数千文件上也很快，operationally 无问题。
- **仍值得做、但定位下调为"可选优化"**：orchestrator 预计算 `concept→cards` 倒排表/簇图（B.3）。它的价值是**省 token + 编排更干净**（agent 不必各自重复 grep+推理），而**不是**"绕开 bash 限制"。可由写卡 hook 增量维护。
- **唯一容错**：遇分类器瞬时不可用 → **稍后重试**（transient）。v3 的 ~750K fallback 浪费源于"连续重试 4 次仍硬扛"，所以协议是"确属持续不可用时才转 fallback，且别反复重试"。
- **决策（2026-05-29，用户选 B）：loop 整轮跑 bypassPermissions**。agent 的 grep/git/python 全程**不经分类器**，本卡点在 loop 执行期**直接消失**。启动：`claude --permission-mode bypassPermissions`（或 `--dangerously-skip-permissions`）；process-level `claude -p` 嵌套时同样传 `--permission-mode bypassPermissions`。代价是命令无审查——靠"只在本 capsule 内写 + 跑自己已知 tools"把爆炸半径控住。非 loop 的零散操作仍可能遇瞬时 outage，用 `!` 或重试即可。

### A.1.2 canonical_concept 并行收敛

- **卡点**：Phase A 批量并行 extract，agent 互不可见，同一概念被铸成不同 canonical（grep 在 governance 时对不上）。
- **方案**：(a) 建卡 best-effort + governance 归一化（现计划）；(b) extract 后插一道**串行 alignment**（轻量 agent/脚本把近似 canonical 归并）；(c) 预置一个 seed canonical 表供并行 agent grep 复用。
- **pros/cons**：(a) 最简、并行友好，但 governance 负担重、且若 alias 发散则 grep 仍漏；(b) 收敛更好但加一趟成本；(c) 锚定收敛但 seed 表要 bootstrap、会 drift。
- **推荐**：**(a) + 强 `summary` 对冲**。summary 是稠密 grep 靶子（含概念+别名+论断），即使 canonical 发散，governance 在 summary 上 grep 仍能召回到同簇。把对冲放在 summary，而不是加一趟 alignment。

### A.1.3 governance 候选聚类如何不爆 O(N²)

- **卡点**：governance 要找重复簇，但 grep-only + agent-driven，怎么聚类而不退化成 N² 两两比？
- **方案**：(a) 逐卡 grep 自己的 canonical/alias，收集命中 → O(N) 次 grep；(b) 先建 concept→cards 倒排表（A.1.1b），**只对 count≥2 的概念**派 fusion 判断；(c) 按 canonical 排序分组。
- **pros/cons**：(a) 直接但 N 次 Bash grep（classifier 风险×N）；(b) 一次建表后零额外 grep，LLM 判断只落在真簇上，**最省也最稳**；(c) 需要 canonical 已较干净。
- **推荐**：**(b)**。倒排表把"聚类"变成纯数据操作；LLM 只在 `count≥2` 的簇上花钱。单卡概念（count=1）直接跳过 governance。

### A.1.4 extract 颗粒度一致性 + 目的性（无 taxonomy 网格、无 few-shot 内容）

- **卡点**：Zettelkasten 无网格 + **无 query**，"一个 idea 在哪结束 / 什么值得抽"全靠判断；并行 agent 颗粒度会漂。
- **方案**：(a) ~~few-shot 样卡~~ **否**——用户指出 few-shot **内容**会造成领域强偏好、降低 exploration、伤泛化；(b) **启发原则 + 目的性**：注入"面向未来检索"的宽口径目的，agent 先问"这 material 回答了哪些未来会被问的问题"，每个值得存的答案=一张卡（借鉴 deep research / STORM 的 question-driven 抽取，但用最宽 query=anticipated retrieval 以保泛化）；(c) 原子性自检清单（非显然/自足/密集/有据）；(d) governance merge 兜底。
- **pros/cons**：(b) 给方向又不收窄、**锐化 exhaust**（=所有有意义问题成卡）、无领域偏好；(c) 便宜但主观；(a) 已否（伤泛化）；若确需示例，用**跨领域 + 只给拆分形状/标题**，不给完整卡内容。
- **推荐**：**(b)+(c)**，(d) 兜底。**不用 few-shot 卡内容**。详见 `next_loop_design.md §1.1` 的"目的性"段。

### A.1.5 per-card re-read 成本是否复发（v3 的最大浪费）

- **卡点**：v3 adoption 逐字复制 body（~855K）、migration echo body（~342K）、分阶段横扫重复 read（~540K）。新设计要确保不复发。
- **方案/结论**：本设计**结构上消除**这三项——extract 出生即终态（无 migration）；ingest 是**脚本**（移动/置位，无 LLM body 复制）；governance 只读 `count≥2` 的簇（不是全量横扫）。**这是新设计相对 v3 最大的成本优化，无需额外动作，只需守住"ingest 不进 LLM"和"governance 只碰簇"。**
- **推荐**：把"ingest 必须是脚本、不得用 LLM 复制 body"写成硬约束。

### A.1.6 hub card 的生成与 split 难点

- **卡点**：merge→hub 要把 N 张卡的知识融成一张 hub，并吸收 N 份 provenance；反过来 split（拆过粗的卡）更难——要切 body、重分 footnote、重写 provenance。
- **方案**：hub 生成 = 一个 governance agent 读簇内全卡 → 写 1 张 hub（body 综合、footnote 合并指向各源 + 各原卡作为 `[^v3-x]`）→ 原卡 superseded 移 archive。split 暂**降级**：v1 只做 merge/distinction/keep，**不做自动 split**（过粗卡留着，标 `needs_split` 待人工或后续）。
- **pros/cons**：只做 merge → 简单可靠、覆盖 80% 价值（去重）；放弃 split → 过粗卡残留，但符合 best-effort zen（让问题更简单，不是全解）。
- **推荐**：**v1 hub-merge + distinction-link，不做 split**；split 标记待议。

### A.1.7 sub-agent 不能递归 → 编排约束

- **卡点**：spawned agent 无 Agent 工具（已确认 [[subagent_no_recursion]]）。所以 extract/governance agent 都不能自己再 fan-out。
- **方案**：**所有扇出由 top-level orchestrator（主会话）做**：orchestrator 建表、分簇、分区、派 N 个无状态 agent。需要两层时走 `claude -p` 进程级嵌套（已验证），但有 classifier + 成本风险，非必要不用。
- **推荐**：单层 agent + orchestrator 扇出；`claude -p` 仅作 escape hatch。

### A.1.8 never-delete 并发一致性

- **卡点**：并行 governance agent 若触碰重叠簇或共享 index，会冲突；archive 移动 + index 重建 + canonical 归一化都是写。
- **方案**：(1) **分区不相交**（一个概念簇整体只给一个 agent）；(2) index/related 重建是**所有 agent 完成后的单次串行脚本**；(3) 沿用 v3 的文件锁 hook。
- **推荐**：分区按"整簇"切，绝不让两个 agent 碰同一张卡；index/derive 最后串行跑。

## A.2 优化收益概览（相对 v3）

| 维度 | v3 | 下一轮（本设计） | 机制 |
|---|---|---|---|
| 比较语料 | v2（错） | self-only | loop 独立 |
| 去重/fusion | 从未发生 | 显式 governance（簇级） | route B + 倒排表聚类 |
| citation | 事后迁移(+1.42M) | 出生即终态 | extract 出 unified-footnote |
| ingest | LLM 逐字复制(+855K) | 脚本，无 LLM | 硬约束 |
| 召回成本 | 全量横扫(+540K 重复) | 仅 count≥2 簇 | 倒排表 |
| classifier 门控 | ~750K fallback 浪费 | loop 整轮 bypassPermissions（消除） | 非 loop 命令偶遇，! / 重试 |

## A.3 需要和用户讨论的（开放问题）

按"阻塞程度"排序。每条给我的倾向。

1. **grep/Bash 的 classifier 依赖（最关键）**：是否确认环境没有非 Bash grep 通道？若没有，是否接受"倒排表物化 + 1-reject-即-fallback"作为容错主轴？（我倾向：是。）
2. **canonical 收敛**：只靠 best-effort + summary 对冲，还是要加一趟 alignment？（我倾向：不加，靠 summary。）
3. **"KB 成型" / Phase B 触发阈值**：init 后跑一次 governance 是默认；后续按卡数阈值还是每次 add 都跑 scoped governance？（我倾向：每次 add 跑 scoped；另设周期性全量 governance。）
4. **hub provenance 吸收模型**：hub 卡如何记录"融合自哪 N 张原卡 + 各自的源"？需要定 schema（如 `merged_from: [ids]` + footnote 指向各原卡）。
5. **ingest 语义**：drafts → active 是物理 copy 到 `kb/cards/`，还是 in-place 置 `status:active` + index 过滤？（我倾向：物理分目录 `kb/cards/`(active) vs `kb/archive/`(superseded)，与 never-delete 的"放到别处"一致。）
6. **split 取舍**：v1 是否真的不做自动 split、只标 `needs_split`？（我倾向：是。）
7. **extract few-shot 选样**：用哪几张 v3 卡当颗粒度锚（建议各取一个代表：一个 mechanism、一个 distinction、一个 source_claim）。
8. **data collection 取数环节**（parked TODO）：按 source spec 抓取新源的机制，本轮是否要一并设计。
9. **embedding escape hatch**：确认"永不用"，还是保留"grep 严重不足时才上"的远期口子？（我倾向：保留口子但 v1 不建。）

---

# 【B. 落地的】

> 精确到：谁 spawn 谁、给什么 context、解决什么、期望输出、容错、预期卡点。**所有扇出由 orchestrator（主会话）做；spawned agent 一律单层、无状态、不递归。每个 Agent 调用必须 `model: opus`**（[[agent_call_always_opus]]）。
>
> **运行模式：整轮以 bypassPermissions 启动**（`claude --permission-mode bypassPermissions`；process-level `claude -p` 同传该 flag）——agent 的 Bash（grep/git/python）全程不经分类器，分类器卡点在 loop 内不存在。

## B.0 角色总览

```
Orchestrator（主 Claude 会话，唯一扇出者）
├─ spawn → Extract Agent ×N      （material → 原子卡）
├─ run   → ingest 脚本           （drafts → kb active，无 LLM）
├─ run   → 倒排表脚本/grep        （建 concept→cards 表）
├─ spawn → Governance Agent ×M   （簇 → hub/archive）
└─ run   → index/derive 脚本      （active-only 索引 + related 派生）
```

## B.1 Extract Agent

- **谁 spawn**：orchestrator。**数量**：init = N（按材料均衡分批）；后续 add = 1。
- **context（给它什么）**：
  - 分配到的 material 绝对路径（只读这些，**不读其他材料、不读任何外部 loop**）。
  - CARD_CONTRACT 摘要：Zettelkasten 原子颗粒度（§next_loop_design 1.1）+ grep-friendly metadata（`canonical_concept`/`aliases`/`summary`，**无 taxonomy**，`card_type`/`tags` 自由可选）+ 单一 `## Footnotes` 出生格式（target 仅 raw 源 / 兄弟 v3 卡 / URL）。
  - 2-3 张 v3 **few-shot 样卡**（颗粒度锚）+ 原子性自检清单（独立/自足/密集/有据）。
  - 语言=中文；写边界=仅 `drafts/cards/` + `drafts/provenance/`；全文一次读（>2MB 才分段）。
  - 现有 KB 的 `canonical_concept` 清单（若存在，供 best-effort 复用；init 首批可为空）。
- **解决什么**：把一个 material 变成若干**源忠实、原子、出生即终态**的卡 + provenance。
- **期望输出**：`drafts/cards/<slug>.md` + `drafts/provenance/<slug>.md`（每卡含 grep-friendly metadata + footnotes）；结构化报告（material→slugs / skip / 异常 / 末行 `WORKER_DONE`）。
- **容错**：空源→skip+报告；grep 复用 canonical 被 classifier 拦→跳过复用、铸新（best-effort），报告；颗粒度拿不准→偏原子但不过碎（merge 比 split 容易兜底）。
- **预期卡点**：canonical 并行发散（A.1.2，靠 summary 对冲）；颗粒度漂移（A.1.4，靠 few-shot）；超大文件分段读。

## B.2 Ingest（脚本，**不是 agent**）

- **谁运行**：orchestrator（Bash）。
- **做什么**：把 `drafts/cards/*` 纳入 active view —— 物理放入 `kb/cards/`（待 §A.3.5 定）；**纯移动/置位，禁止任何 LLM 复制 body**（硬约束，杜绝 v3 的 855K 浪费）。route B：无 gate。
- **期望输出**：active KB 卡 + provenance 就位。
- **容错**：classifier 拦 python/git → **第 1 次拒即 fallback**（orchestrator 用 Write/Edit 等价完成，或派一个最小 fallback agent；**不重试 4 次**，吸取 v3 教训）。
- **预期卡点**：classifier 阻塞（A.1.1）；move 语义未定（A.3.5）。

## B.3 倒排表 / grep-cluster（orchestrator）

- **谁运行**：orchestrator。
- **做什么**：在 classifier 可用窗口，一次性 grep 全 KB 的 `canonical_concept`/`aliases`/`summary`，物化成 `concept → [card ids]` 倒排表（纯文本，落盘）。最好由写卡 hook 增量维护。
- **期望输出**：倒排表文件 + 簇清单（`count≥2` 的概念）。
- **容错**：grep 被拦→重试 1 次→降级为"只用已有倒排表 / 只处理明显簇"。
- **预期卡点**：grep=Bash classifier 风险（A.1.1，核心）；alias 发散导致簇漏卡（靠 summary grep 补）。

## B.4 Governance Agent

- **谁 spawn**：orchestrator。**数量**：M（按**整簇**分区，分区不相交）。
- **context**：分配到的簇（card ids + 路径 + 可只给 summaries 省 token）；fusion 决策空间（merge→hub / distinction-link / subsume / **keep-separate**，v1 **不做 split**，过粗只标 `needs_split`）；never-delete 规则（superseded 卡**移到** `kb/archive/` + 置 `status:superseded` + `superseded_by:<hub>`，**绝不 rm**）；canonical/alias 归一化指令；hub provenance 吸收 schema（A.3.4 待定，给临时约定 `merged_from:`）；loop 独立。
- **解决什么**：把簇内冗余收敛——产 hub 卡、标 superseded、归一化 canonical、链 distinction。
- **期望输出**：`kb/cards/<hub>.md`（综合 body + 合并 footnote 指向各源与各原卡）；被取代卡移入 `kb/archive/` 并置位；决策报告。
- **容错**：不确定→**keep-separate**（保守、best-effort）；只读预算的簇、不重新全库 grep（省 classifier）；分区保证零碰撞；绝不删除只移动。
- **预期卡点**：跨分区概念（A.1.8，靠"整簇分区"规避）；hub provenance 复杂度；agent 不能递归（独立处理本簇）。

## B.5 Index / Derive（脚本，orchestrator，最后串行）

- **谁运行**：orchestrator，在所有 governance agent 完成后。
- **做什么**：`build_kb_index.py`（**只索引 active**）+ `derive_metadata_from_footnotes.py`（重派生 `related:`，只含 v3 active 卡）。
- **容错**：classifier 拦→1-reject-即-fallback（agent 用 Read+Edit 等价；拆小分批，别派 1 个大 agent，吸取 v3 derive 623K 教训）。
- **预期卡点**：classifier；archive 卡须排除出 index/related。

## B.6 两种运行模式

- **init KB（批）**：B.1×N 并行 → B.2 → B.3 → B.4×M 并行 → B.5。一次性。
- **单材料 add（增量）**：B.1×1 → B.2 → B.3（只对新卡 grep 既有倒排表）→ B.4×（受影响簇数）→ B.5。**同一套 per-material 契约**，只是规模小、governance scoped。

## B.7 容错总纲（贯穿）

1. **loop 整轮跑 bypassPermissions**（2026-05-29 决定）：agent 的 Bash（grep/git/python）全程跳过分类器，分类器卡点在 loop 内不存在。代价是命令无审查——靠"只在本 capsule 内写 + 跑自己已知 tools"控住爆炸半径。loop 外零散命令若遇瞬时 outage，用 `!` 或重试。倒排表（B.3）作为省 token 的编排优化保留。
2. **never-delete**：任何"删除"都改成"移到 `kb/archive/` + 置位"。禁止 `rm`、禁止 `git reset --hard`。
3. **分区不相交 + 末尾串行**：并行 agent 绝不碰同一文件；index/derive 收尾串行。
4. **best-effort 默认值**：不确定时取保守分支（extract 偏原子、governance keep-separate、ingest 不动 body）。
5. **commit**：沿用 PostToolUse hook 自动 commit；**commit message 不带任何 Co-Authored-By trailer**（[[feedback_no_coauthor_trailer]]）。

## B.8 预期卡点汇总

| # | 卡点 | 出现环节 | 缓解 | 残留风险 |
|---|---|---|---|---|
| 1 | 分类器门控 | loop 内（bypass 直接消除） | 整轮 bypassPermissions | bypass 无审查，靠 capsule 写边界控风险 |
| 2 | canonical 并行发散 | B.1 | summary 对冲 + governance 归一化 | 极端发散簇漏召 |
| 3 | 颗粒度漂移 | B.1 | few-shot + 自检 | 过粗卡残留（不 split） |
| 4 | 跨分区概念 | B.4 | 整簇分区 | 簇定义依赖倒排表质量 |
| 5 | hub provenance | B.4 | `merged_from:` 临时约定 | schema 未最终定（A.3.4） |
| 6 | ingest 误用 LLM | B.2 | 硬约束"脚本-only" | 若违反则 855K 浪费复发 |
| 7 | 索引含 archive | B.5 | active-only 过滤 | 过滤遗漏则 view 脏 |

---

> 待用户回来：先过 §A.3 的 9 个开放问题（尤其 #1 grep/classifier、#4 hub provenance schema、#5 ingest 语义），定了之后 §B 即可直接执行。
