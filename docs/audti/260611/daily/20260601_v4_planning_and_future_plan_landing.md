# 2026-06-01 每日梳理：v4 前置规划与 future plan 落盘

---
status: draft
day_id: 20260601
audit_status: pending
source_window: "2026-06-01 00:00:00 +0800 至 2026-06-02 00:00:00 +0800"
day_type: transition_day
subtype: planning_with_artifact_landing
---

## 当日结论

1. `2026-06-01` 不是空窗日（empty window）。本地日窗内，Claude 项目会话（Claude transcript）在本仓库 `cwd` 下持续讨论下一轮 LLM Wiki 管线，并发生两次明确的规划产物落盘（artifact landing）：`questioning_loop_design.md` 与 `pipeline_spec.md` 的创建/写入。
2. 本日性质应判为过渡/规划日（transition / planning day），不是 v4 loop 正式初始化日，也不是 KB 卡片生产日（knowledge-card production day）。当日活动主要围绕 v4 前置设计：reader/writer/context 边界、questioner 问答式抽取、Mode A / Mode B、inline fusion、并行/顺序执行取舍、pipeline contract。
3. 当日有项目文件落盘，但没有本仓库 git 固化（git solidification）：`git log` 在 `2026-06-01 00:00:00 +0800` 到 `2026-06-02 00:00:00 +0800` 无提交。相关 future plan 文件最终在 `2026-06-04 21:49:19 +0800` 的 commit `d1bfaa2` 中加入仓库历史。
4. `loops/v4_llm_wiki_loop_20260602/` 在本地 6/1 窗口无 mtime 命中；v4 loop capsule 初始化、`LOOP_START_PROMPT.md`、Phase 1-2 和 karpathy-gist 实验均由 6/4 git commit 证明，不能回填到 6/1。
5. Codex 会话（Codex sessions / archived sessions）在 6/1 有其它活动，但严格 `cwd == .` 命中为 0，项目路径文本命中为 0；不能作为本项目 6/1 开发事实。
6. `docs/**`、`user-insights/**`、Claude memory 和 6/4 才创建的 `design_interaction_log.md` 只作为二级对照（secondary material）或排除证据；本日报不把二级材料当作唯一事实源（single source of truth）。

## 时间线 / 复核

| 时间（Asia/Shanghai） | 事件 | 事实类型 | 证据 | 当日归属 |
| --- | --- | --- | --- | --- |
| 00:00:00 | 6/1 本地日窗开始 | 日期边界（date boundary） | `source_window` | 本日开始 |
| 10:54 | 用户提出 writer 无全量上下文时如何保证信息充分，并追问为什么 reader 不直接写卡 | 会话事实（transcript fact） | Claude 主 JSONL line `2871` | v4 前置规划问题启动 |
| 10:57 | 助手提出 reader/writer split 对本项目不成立，reader 应同时写卡；后续被继续修正 | 会话事实 | line `2930` | 临时设计判断，非最终定稿 |
| 11:05-11:09 | 讨论 context 视角；阶段性形成“extract agent reads and writes, reviewer separate”的总结 | 会话事实 | lines `2937`, `2939`, `2942` | 设计演进，不作为最终实现 |
| 11:18-11:22 | 用户提出 main-agent reader 利用 KV cache fork sub-agent，但缺少反馈；助手分析反馈与并行取舍 | 会话事实 | lines `2944`, `2951` | 引出后续 questioner loop |
| 11:24-11:29 | 用户命名“LLM read once and understand all”隐藏假设；助手否定并提出 multi-pass reading with evolving questions | 关键决策候选 | lines `2958`, `2960`, `2967` | 本日稳定设计基础 |
| 11:58-12:00 | 用户转向 questioner 问答式 exhaust：不要求直接“抽尽”，而是让 agent 持续提问直到 satisfied | 关键决策候选 | lines `2969`, `2971` | questioning loop 成形 |
| 14:12-14:18 | 用户纠正 questioner 是 forked / scoped，而非全新 ignorant agent；形成 Mode A（建构）与 Mode B（进化）区分 | 关键决策候选 | lines `2979`, `2982`, `2988` | Mode A / Mode B 设计锚点 |
| 14:22-14:27 | 用户要求开 agent team 讨论 building/evolving stages 并写入文件；3 个 design sub-agent 返回 Mode A、Mode B、整合提案 | sub-agent 会话事实 | lines `2990`, `2992`-`3009`; subagent files `agent-ad1e...`, `agent-ace...`, `agent-a965...` | 一手设计输入 |
| 14:30 | 写入 `loops/v3_llm_wiki_loop_20260525/future_plans/questioning_loop_design.md` | 产物落地（artifact landing） | lines `3010`, `3016`, `3021`; file mtime `2026-06-01 14:30:30 +0800` | 本日落盘事实 |
| 14:54-15:23 | 用户把 Mode B 降为 further plan，聚焦 Mode A；讨论 inline fusion、parallel vs sequential、cluster 不是先验输入；最终去掉 pre-clustering 假设 | 设计复核（design review） | lines `3025`, `3028`, `3036`-`3060` | 收敛到更保守的 v4 执行策略 |
| 20:13-20:18 | 用户选择 v4 先用 A（parallel）focus on skills building，gist seed 先行，LLM Wiki 未来像 plugin；助手锁定 v4 execution decisions | 关键决策 | lines `3063`, `3070`, `3072` | v4 前置决策，不等于 v4 目录初始化 |
| 23:11-23:14 | 用户要求先写完整 pipeline：scope/context/boundary/input/output schema/artifacts；助手写入 `pipeline_spec.md` 初稿 | 产物落地 + 会话事实 | lines `3074`, `3081`, `3082`, `3088`, `3089` | 本日创建事实；现存文件后来被改写 |
| 23:24-23:27 | 用户讨论 repo/code material 的 reader 逻辑；2 个 sub-agent 提出材料类型 reader 和三角对话拓扑方案 | sub-agent 会话事实 | lines `3104`-`3114`; subagent files `agent-a8b...`, `agent-ae500...` | 当日晚间设计探索 |
| 23:35-23:46 | 用户纠正 main-agent 静态协调、文件/邮件式 agent team；中途中断一次红队调用后，再开两个 red-team sub-agent 挑战设计 | 会话事实 + 复核 | lines `3122`, `3124`, `3126`, `3139`, `3142`-`3151` | 设计压力测试 |
| 23:51-23:55 | 用户明确 grep 由 agent 做 zh/en/同义词改写，成本不是第一瓶颈；reviewer 需可 grep raw material 和 KB cards | 关键决策 | lines `3159`, `3161`, `3165`, `3171` | reviewer 设计收束 |
| 24:00:00 | 6/1 日窗结束 | 日期边界 | 后续 6/2、6/4 证据另属后续日期 | 不回填后续 v4 初始化 |

## 关键决策

| 决策 | 状态 | 内容 | 影响 | 证据 |
| --- | --- | --- | --- | --- |
| 从 reader/writer 分离转向 context 边界思考 | 演进中 | 早期认为 reader 应直接写卡，随后被用户推进为 main-agent / sub-agent / questioner 的上下文设计问题 | 触发 v4 extraction architecture 讨论 | `C20260601-02` |
| 否定“LLM 单次阅读即全面理解” | 稳定 | 以 multi-pass reading with evolving questions 替代一次性 exhaust | questioning loop 成为核心机制 | `C20260601-03` |
| 形成 Mode A / Mode B 两模式 | 稳定但分层 | Mode A 面向单材料建构（building/extract），Mode B 面向跨卡片进化（evolve/synthesis） | `questioning_loop_design.md` 的主结构；Mode B 后续被降为 future plan | `C20260601-04`, `C20260601-05` |
| v4 先采用 parallel (A)，focus on skills building | 稳定 | 用户认为 waves/seed 更自然，但 right-now action 是 build new loop skills/scripts；v4 先用 A | 后续 6/4 v4 task/skills 初始化的前置约束 | `C20260601-08` |
| 先写 pipeline contract，再谈 implementation | 稳定 | 明确每阶段 scope/context/boundary/input/output schema/artifacts | 产生 `pipeline_spec.md` 初稿 | `C20260601-06` |
| Reviewer 是 fresh eyes 但 not blind | 稳定 | reviewer 不预加载全文，但可用 grep 检索 raw material 和 KB cards，审查 quit / correctness / overlap | 后续 reviewer prompt 的设计依据 | `C20260601-09` |
| grep-only recall 以 agent 改写查询实现 | 稳定 | agent 自主用中文/英文/同义词多轮 grep；质量和架构学习优先，成本不是本轮瓶颈 | 后续 pipeline spec 中 grep-only recall 的基础 | `C20260601-09` |
| clustering 不是 right-now action | 稳定 | 预聚类材料需要先读懂材料，容易循环论证；v4 不把 semantic clusters 当输入 | 避免把 v3 ad-hoc clusters 回填为 v4 前提 | `C20260601-08` |

## 实现变化

本日没有确认 KB 卡片生产（card production）、v4 loop capsule 初始化或 git commit；但有 v3 future plan 目录中的规划产物落盘。

- `loops/v3_llm_wiki_loop_20260525/future_plans/questioning_loop_design.md`
  - Claude 主会话在 `2026-06-01 14:30:30 +0800` 调用 `Write` 并得到 “File created successfully”。
  - 文件 mtime 也是 `2026-06-01 14:30:30 +0800`。
  - 内容为 future plan（`stage: discussion_only`），主题是 reader/questioner 对话的 Mode A / Mode B 设计；不是执行日志，也不是 v4 运行产物。
  - 注意：文件 frontmatter 写 `created: 2026-05-30`，但一手 transcript 与 mtime 都指向 6/1 创建/落盘。该 frontmatter 日期不作为本日报的主要事实锚。
- `loops/v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`
  - Claude 主会话在 `2026-06-01 23:13:48 +0800` 调用 `Write` 创建初稿，并在 `23:14:05` 总结其阶段：collect → extract → ingest → evolve，包含 scope/context/boundary/I-O schema/artifacts。
  - 当前文件 mtime 为 `2026-06-04 21:31:58 +0800`，frontmatter 有 `updated: 2026-06-02`，说明现存内容已包含后续修订；本日报只把“6/1 创建初稿”记为当天事实，不把现存全文全部归到 6/1。
- Git 固化（git solidification）
  - 6/1 本地日窗无 commit。
  - 上述两个文件在 git 中均由 `d1bfaa2` 于 `2026-06-04 21:49:19 +0800` 添加，commit message 为 `v3 future plans: pipeline spec v2 + questioning loop + metadata template + jj template + optimization docs`。
- v4 loop artifacts
  - `loops/v4_llm_wiki_loop_20260602/` 在 6/1 本地日窗无 mtime 命中。
  - v4 capsule 初始化、`LOOP_START_PROMPT.md` 和 Phase 1-2 文件由 6/4 commits `bc81caf`, `39d57d1`, `2df61dd` 证明，属于后续日期。

## 问题、坑、解决方案

| 问题/坑 | 触发 | 处理 | 残余风险（Residual Risk） |
| --- | --- | --- | --- |
| 容易把 6/1 规划落盘误写成 v4 正式启动 | `pipeline_spec.md` 明确提到 v4，且后续 v4 目录名含 `20260602` | 用 git、mtime 和 v4 目录扫描分开：6/1 是 future plan / spec；6/4 才有 v4 capsule commits | 6/2 可能有设计启动事实，需由 `day_20260602` 单独确认 |
| 当前 `pipeline_spec.md` 不是纯 6/1 内容 | 文件现存 mtime 为 6/4，frontmatter 有 `updated: 2026-06-02` | 只引用 Claude line `3082`/`3089` 中的初稿创建和概要，不把后续内容回填 | 初稿完整正文只能从 transcript 的 Write payload 中恢复，现存文件不能直接代表 6/1 全文 |
| `questioning_loop_design.md` frontmatter 日期与落盘证据不一致 | frontmatter `created: 2026-05-30`，但 transcript/mtime 是 6/1 | 以一手 transcript 和 file mtime 作为落盘事实；frontmatter 视为设计元数据而非文件创建证据 | 若 5/30 有未保存讨论，当前未见一手落盘证据 |
| agent team 讨论多次纠偏，早期回答被用户推翻 | reader/writer、main-agent 是否静态、questioner 是否 full material 等多轮变化 | 把关键决策表区分“演进中”和“稳定”；以当日后段用户纠偏后的结果为最终设计状态 | 后续 6/2 / 6/4 可能再次改写，不能提前写入本日 |
| 成本与质量取舍未量化 | red-team 指出约 9x 成本，用户表示质量/架构学习优先 | 记录为当日取舍，不把成本问题视为解决完成 | 后续 v4 实验需用真实 token/cost artifact 验证 |
| Codex 6/1 有活动但不属于本仓库 | 全量 Codex timestamp 扫描有 day events，但 strict project cwd / project text hits 为 0 | 作为排除证据，不纳入本项目主线 | 不排除外部会话口头提到类似概念，但无本仓库证据 |

## 证据地图（Evidence Map）

| claim_id | 主张 | 支撑证据 | 证据强度 | 缺口 |
| --- | --- | --- | --- | --- |
| C20260601-01 | 6/1 不是空窗日（empty window） | Claude 项目 JSONL 本地 6/1 窗口命中 246 events：主文件 147 lines，10 个 subagent 文件有命中；主会话 `cwd` 为本仓库 | 强 | 不代表全部事件都是实质开发，需逐条分类 |
| C20260601-02 | 当日核心是 v4 前置规划/复盘，而非卡片生产 | 主会话 lines `2871`-`2988` 围绕 reader/writer/context、KV cache、read-once 假设、questioner loop 和 Mode A/B 讨论 | 强 | transcript 是讨论事实，不自动等于实现事实 |
| C20260601-03 | “read once understand all” 被明确否定，multi-pass questioning 成为设计基础 | lines `2958`, `2960`, `2967` | 强 | 仅为设计决策，6/1 未见可运行 skill 实现 |
| C20260601-04 | `questioning_loop_design.md` 在 6/1 落盘 | lines `2990`-`3016`：用户要求 agent team + put into file，3 个 sub-agent 返回提案，`Write` 创建文件；文件 mtime `2026-06-01 14:30:30 +0800` | 强 | 文件 frontmatter `created: 2026-05-30` 与落盘证据不一致 |
| C20260601-05 | Mode B 被定位为 further plan，v4 先聚焦 Mode A/skills | line `3025` 用户说 Mode B 可算 further plan；lines `3063`, `3070`, `3072` 锁定 v4 parallel / skills building / gist seed | 强 | 后续 6/2 或 6/4 可能细化实现，不回填 |
| C20260601-06 | `pipeline_spec.md` 初稿在 6/1 创建 | lines `3074`, `3081`, `3082`, `3088`, `3089` 显示用户要求 pipeline contract，助手 `Write` 创建文件并总结内容 | 强（创建事实）/ 中（现存内容归属） | 当前文件已在 6/2/6/4 后续更新，不能把现存全文都视为 6/1 初稿 |
| C20260601-07 | 6/1 无 git 固化 | `git log --all --since='2026-06-01 00:00:00 +0800' --until='2026-06-02 00:00:00 +0800' -- .` 无输出；相关 files 的 git add commit 在 `d1bfaa2` 6/4 | 强 | git 不覆盖未提交瞬态操作；本日确有未固化落盘 |
| C20260601-08 | v4 loop capsule 未在 6/1 落盘 | `find loops/v4_llm_wiki_loop_20260602 ... 6/1 window` 无输出；git log 显示 v4 初始化 commits 在 6/4 | 强 | v4 目录名含 `20260602`，6/2 需另审 |
| C20260601-09 | 晚间形成 reviewer grep access、agent-driven grep、质量优先等设计约束 | lines `3129`, `3135`, `3159`, `3161`, `3165`, `3171`; red-team subagents lines `3142`-`3149` | 强 | 仍是设计层约束，未见 6/1 prompt/skill 实现 |
| C20260601-10 | Codex 6/1 不能作为本项目主线证据 | 全量 Codex JSONL 扫描 `strict_project_cwd_hits: 0`, `project_text_hits: 0`; 当日 mtime 的 Codex 文件均无本项目路径命中 | 强 | Codex JSON schema 部分文件无 cwd 字段；以项目路径文本命中补充仍为 0 |
| C20260601-11 | `docs/**`、`user-insights/**`、Claude memory 未提供 6/1 本项目事实 | `find docs user-insights ... 6/1 window` 无输出；Claude memory 6/1 mtime 无输出；`design_interaction_log.md` 是 6/4 commit 的二级对照 | 强 | 二级材料未全文作为事实源使用，符合协议但可能遗漏后验索引中的线索 |

## 未解决问题

- `pipeline_spec.md` 的 6/1 初稿与当前 6/4 版本之间的具体 diff 尚未单独恢复；本日报只确认 6/1 创建和概要，不确认现存全部条款的当日归属。
- `questioning_loop_design.md` frontmatter 的 `created: 2026-05-30` 与 6/1 transcript / mtime 不一致。当前证据支持 6/1 文件落盘，但不排除 5/30 有未落盘或外部讨论。
- 6/2 的 v4 loop id / 设计启动关系需要由 `day_20260602` 独立审计；本日报只确认 6/1 尚无 v4 目录 mtime 和 git commit。
- 6/4 的 v4 初始化、pipeline spec v2、skills placeholder 和 karpathy-gist 实验不能回填到 6/1；后续日报需以 git commit 和 transcript 单独建立链路。
- 成本、quality uplift、reviewer quit-audit 是否实际有效，在 6/1 仅有设计讨论，没有实验验证（experiment validation）。
- 本日类型是 transition/planning day with artifact landing；是否在最终总线中归入“实质开发”还是“v4 前置规划”，应由 independent audit 和 main-agent acceptance 决定。

## 当日边界

- 本日报只覆盖 `2026-06-01 00:00:00 +0800` 到 `2026-06-02 00:00:00 +0800`。
- 5/31 已验收为空窗日（empty_window_pass）；其结论不延展到 6/1。
- 6/1 的事实不包括 `loops/v4_llm_wiki_loop_20260602/` 初始化，不包括 `LOOP_START_PROMPT.md` 创建，不包括 v4 Phase 1-2 skills / cards / karpathy-gist 实验。
- 6/2 的 loop id 与 v4 设计启动候选不在本日报展开；只能作为下一日报的待审主题。
- 6/4 git commits 是后续固化事实（git solidification），在本日报中只用于排除跨日污染和说明 commit 时间。
- `design_interaction_log.md`、`docs/**`、`user-insights/**`、Claude memory/summary 和本轮 6/11 审计产物不是 6/1 的一手历史事实源。

## 自检

- 已读取 `docs/audti/260611/tasks/daily_synthesis_task.md`、`docs/audti/260611/protocols/execution_protocol.md`、`docs/audti/260611/source_inventory.md`、`docs/audti/260611/day_queue.md`。
- 已参考 20260531 日报、独立审计和主控验收，避免把 5/31 空窗或 5/30 尾声污染到 6/1。
- 已按 Asia/Shanghai 建立本地日期窗口，并用 UTC `2026-05-31T16:00:00Z` 到 `2026-06-01T16:00:00Z` 扫描 Claude/Codex JSONL。
- 已核查 Claude JSONL、subagent JSONL、git log、v3/v4 loop artifacts、Codex sessions/archived sessions、`docs/**`、`user-insights/**`、Claude memory。
- 已明确区分会话事实（transcript fact）、产物落地（artifact landing）、git 固化（git solidification）和二级材料（secondary material）。
- 已给出 claim_id、证据强度、残余风险（residual risk）和跨日边界。
- 本文件只写入允许路径 `docs/audti/260611/daily/20260601_v4_planning_and_future_plan_landing.md`。
