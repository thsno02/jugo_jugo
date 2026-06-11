# 2026-05-22 每日梳理：循环清单（loop manifests）、扩展语料（expanded corpus）与 git 固化

```yaml
status: draft
day_id: 20260522
audit_status: pending
source_window: "2026-05-22 00:00:00 +0800 至 2026-05-22 23:59:59 +0800；主要实质窗口为 10:34-10:38 +0800"
```

## 当日结论

1. `2026-05-22` 确有项目实质开发证据，且核心动作是 git 固化（git solidification）与 push：当天 git history 有 4 个 commit，时间集中在 `10:34:48-10:37:39 +0800`，并由 Codex 会话记录（Codex transcript）逐条记录 `git commit`、`git push` 和最终干净状态。
2. 审计残余风险已被当天关键 commit `ec5ecd3` 正面覆盖：它把 `2026-05-21 21:03-21:39 +0800` 修正版覆盖驱动循环（corrected coverage-driven loop）的 runner、计划、状态、发现/分诊、日志、claims 和 coverage records 固化到 git，包含 `scripts/run_loop.py`、`candidate_sources.jsonl`、`triage_decisions.jsonl`、`claims.jsonl`、`coverage_records.jsonl`、`loop_events.jsonl` 等。
3. `ec5ecd3` 固化的是前一晚运行结果，而不是 `2026-05-22` 新跑的一轮研究循环：`loop_state.json`、`loop_events.jsonl`、`coverage_status.md` 的生成时间均落在 `2026-05-21 20:48-21:37 +0800`，而 `2026-05-22 10:34-10:38 +0800` 的 Codex 会话明确是 Git/File Steward（Git/文件管家）按类别 stage、commit、push。
4. 当天新增 expanded corpus（扩展语料）也被拆分提交：`e09ea2a` 新增 14 个 arXiv source directories（源码目录）和 458 个文件；`c14a93e` 新增 5 个 GitHub repo metadata groups（仓库元数据组）和 8 个 webpage source directories（网页来源目录）。
5. 当天报告层（reporting layer）在 `41e8693` 被固化，`coverage_status.md` 和 `judgment_status.md` 显示 8 个 coverage areas（覆盖区域）均 `supported/pass`，research paper gate（研究论文门禁）为 `passed`，但同一提交中的 `goal_satisfaction_audit.md` 保留了较早的“not satisfied”判断，需在后续审计中降级为历史 audit artifact（审计产物）而非最终状态。
6. 会话最终状态显示 `main` 已同步 `origin/main`、HEAD 在 `41e8693`、普通未跟踪文件为 `0`；这与当天 git log 的 4 个 commit 对齐，构成 git history、Codex transcript、仓库 artifacts 的三角校验（triangulation）。

## 时间线

| 时间（+0800） | 事件 | 证据 | 影响 |
| --- | --- | --- | --- |
| 2026-05-21 21:39（前置） | corrected loop 运行完成但未 commit；Git/File Steward 只读盘点显示 5 个 tracked modified files、515 个 untracked artifacts。 | Codex session `~/.codex/sessions/2026/05/21/rollout-2026-05-21T16-39-08-019e49b0-42f0-7b00-9dd9-0104ed3bf2d7.jsonl` lines 1483-1488；Git/File Steward session lines 244-245。 | 给 `2026-05-22` 的固化动作提供前置边界：前一晚产物存在，但尚未 stage/commit/push。 |
| 10:34:06 | 用户要求“当前 repo 里很多内容，把这些内容依次进行 git push”。 | Codex Git/File Steward session `~/.codex/sessions/2026/05/21/rollout-2026-05-21T19-53-57-019e4a62-9c4d-71f1-b5bd-021698b33b1f.jsonl` lines 252-253。 | 当天工作性质明确为 git/file-management（Git/文件管理），不是新研究执行。 |
| 10:34:41 | Steward 决定按 4 组处理：loop run records/manifests、arXiv raw data、GitHub+web raw data、reports。 | 同一 session lines 267-269；`git status` 和 staging commands。 | 建立当天 4 个 commit 的分组逻辑，降低大文件与混合提交风险。 |
| 10:34:48 | commit `ec5ecd3`：`Add loop run manifests and logs`。 | `git log --date=iso --name-status --since 2026-05-22 --until 2026-05-23`；session lines 272-273；`git show --stat ec5ecd3`。 | 固化 corrected loop 的核心控制面（control plane）：runner、loop plan/state、discovery、logs、manifests。 |
| 10:34-10:35 | 第一组 commit 后立即 push；随后开始处理 arXiv 原始资料。 | session lines 275-282。 | 说明 `ec5ecd3` 不只是本地 commit，而是进入远端同步流程。 |
| 10:35:16 | commit `e09ea2a`：`Add expanded arXiv source corpus`。 | `git log`；session lines 297-298；`git diff-tree` 统计 14 个 `data/raw/arxiv/*` source directories。 | 把 evaluation/comparison/risk 相关论文源码包、`agent_source_bundle.txt`、metadata 和 text 资料纳入 git。 |
| 10:37:14 | commit `c14a93e`：`Add web and repository source materials`。 | `git log`；session lines 355-356；`git diff-tree` 统计 5 个 GitHub repo groups 和 8 个 webpage groups。 | 补齐 GitHub repo metadata 与网页治理/记忆/RAG/PKM 类来源材料。 |
| 10:37:39 | commit `41e8693`：`Add loop run status reports`。 | `git log`；session lines 366-370；`git diff-tree --name-status 41e8693`。 | 固化 coverage、evidence matrix、goal satisfaction audit、judgment status 等报告层产物。 |
| 10:38:05-10:38:12 | 最终状态检查：HEAD 在 `41e8693`，`main` 同步 `origin/main`，未跟踪普通文件为 `0`。 | session lines 378-389；`git log --oneline` 输出 `41e8693`、`c14a93e`、`e09ea2a`、`ec5ecd3`。 | 当天 git 固化闭环完成；可作为下一阶段从 git history 回溯的稳定锚点。 |

## 关键决策

| 决策 | 决策者 | 理由 | 后果 | 证据 |
| --- | --- | --- | --- | --- |
| 将大量仓库内容按类别拆成 4 个 commit 并逐次 push。 | Codex Git/File Steward，响应用户明确要求 | 文件很多，且包含 raw corpus（原始语料）、manifests（清单）、reports（报告）等不同性质产物；会话中还先检查单文件大小风险。 | 形成 `ec5ecd3`、`e09ea2a`、`c14a93e`、`41e8693` 四个清晰提交组。 | session lines 252-269、386-389；git log 当天 4 commits。 |
| 先固化 loop run manifests/logs，再固化 raw corpus。 | Codex Git/File Steward | loop artifacts 是前一晚 corrected loop 的控制面和审计残余风险核心，应单独成组。 | `ec5ecd3` 包含 `scripts/run_loop.py`、`loop_plan.md`、`loop_state.json`、`data/discovery/**`、`data/logs/**`、`data/manifests/**`。 | session lines 267-273；`git diff-tree --name-only ec5ecd3`。 |
| 将 arXiv raw corpus 独立成大提交。 | Codex Git/File Steward | arXiv 组文件最多；会话显示先 stage 后检查没有 `mode 160000` gitlink。 | `e09ea2a` 新增 458 files、14 个 arXiv source directories。 | session lines 281-300；`git diff-tree` arXiv source directory list。 |
| 将 GitHub repo metadata 与 webpage materials 放在同一提交组。 | Codex Git/File Steward | 两者都是 raw source materials（原始来源材料），但比 arXiv 组小。 | `c14a93e` 新增 5 个 GitHub repo groups 和 8 个 webpage groups。 | session lines 346-356；`git diff-tree` GitHub/webpage directory list。 |
| 证据不足以说明当天有新的研究口径决策。 | 本日报审计判断 | 当天 Codex 会话主要是 Git/File Steward 操作；loop run timestamps 和 reports 生成时间均指向前一晚。 | 当天结论只写“git 固化与 push”，不把前一晚 corrected loop 的执行误记为 5 月 22 日新研究运行。 | session lines 252-389；`loop_events.jsonl` 和 `loop_state.json` 的 `2026-05-21T13:*Z` 时间戳。 |

## 实现变化

- loop runner/control plane（循环运行器/控制面）：`ec5ecd3` 新增 `scripts/run_loop.py`、`loop_plan.md`，并更新 `loop_manifest.json`、`loop_state.json`。`loop_state.json` 在提交态显示 `current_phase: satisfied`、`satisfaction.status: pass`、open queues 全为 0。
- discovery and triage（发现与分诊）：`ec5ecd3` 新增 `data/discovery/candidate_sources.jsonl` 27 行、`triage_decisions.jsonl` 27 行、`search_tasks.jsonl` 3 行。
- manifests and audit logs（清单与审计日志）：`ec5ecd3` 新增或更新 `claims.jsonl` 41 行、`coverage_records.jsonl` 41 行、`source_digests.jsonl` 72 行、`claim_source_links.jsonl` 824 行、`loop_events.jsonl` 47 行、`audit_events.jsonl` 8 行、`inaccessible_sources.xml`。
- source manifest（来源清单）：`ec5ecd3:data/manifests/sources.jsonl` 提交态为 72 行，状态计数为 65 `ok`、6 `blocked`、1 `http_error`；source type（来源类型）计数为 17 `arxiv`、20 `github_repo`、25 `webpage`、6 `reddit`、2 `pypi`、1 `gist_raw`、1 `hacker_news`。
- expanded arXiv corpus（扩展 arXiv 语料）：`e09ea2a` 新增 14 个 source directories：`arxiv-alce`、`arxiv-ares`、`arxiv-etamp-memory-poisoning`、`arxiv-graph-poisoning`、`arxiv-graphrag`、`arxiv-lightmem`、`arxiv-locomo`、`arxiv-longmemeval`、`arxiv-mem0`、`arxiv-memgpt`、`arxiv-poisonedrag`、`arxiv-ragas`、`arxiv-ragchecker`、`arxiv-zep`。
- web/repository corpus（网页/仓库语料）：`c14a93e` 新增 5 个 GitHub repo groups（`repo-amazon-ragchecker`、`repo-longmemeval`、`repo-microsoft-agent-governance-toolkit`、`repo-microsoft-graphrag`、`repo-stanford-ares`）和 8 个 webpage groups（LangChain long-term memory、Microsoft agent governance toolkit docs、NIST GAI profile、Obsidian link notes、OWASP Agentic Top 10 2026、OWASP LLM Top 10 2025、Wikibase data model、Write the Docs docs-as-code）。
- reporting layer（报告层）：`41e8693` 新增 `reports/coverage_status.md`、`reports/evidence_matrix.md`、`reports/goal_satisfaction_audit.md`、`reports/judgment_status.md`，并修改 `reports/acquisition_status.md`。

## 问题、坑、解决方案

| 问题/坑 | 证据 | 解决方案/当日处理 | 剩余风险 |
| --- | --- | --- | --- |
| 产物生成日与 git 固化日不同，容易把 `2026-05-21` 晚间 loop 误写成 `2026-05-22` 新执行。 | `loop_events.jsonl` 时间戳为 `2026-05-21T12:48-13:37Z`；`loop_state.json` `last_completed_loop` 为 `2026-05-21T13:36:22Z`；但 commit 在 `2026-05-22 10:34-10:37 +0800`。 | 本日报把 5 月 22 日定义为 git 固化（git solidification）与 push，不把前一晚运行误记为当日新 research loop（研究循环）。 | 后续总线路需要继续区分“运行发生时间”和“版本历史固化时间”。 |
| 初次 acquisition（获取）出现代理/网络失败，但最终 manifest 已显示多数来源 `ok`。 | `acquisition_failures.jsonl` 记录 13:15Z 大量 proxy/git errors；后续 `loop_events.jsonl` 显示 acquire 重试从 27 failed 到 0 failed；`sources.jsonl` 提交态为 65 ok、6 blocked、1 http_error。 | runner 重试并更新 manifest；无法访问的 Reddit/AICritique 继续进入 `inaccessible_sources.xml`。 | acquisition_failures 是历史失败日志，不能单独用来否定最终 state；blocked/http_error 仍是真缺口。 |
| 报告层存在状态不一致：`goal_satisfaction_audit.md` 说 current evidence not satisfied，但 `judgment_status.md` 与 `loop_state.json` 说 satisfaction/pass。 | `41e8693:reports/goal_satisfaction_audit.md` 的 Current Evidence 段落；`41e8693:reports/judgment_status.md` 的 `research_paper passed` 和 `Current satisfaction status: PASS`；`ec5ecd3:loop_state.json`。 | 将 `goal_satisfaction_audit.md` 视为较早 audit artifact（审计产物），以 `loop_state.json`、`audit_events.jsonl`、`judgment_status.md` 和 session final answer 交叉判断最终状态。 | 后续 audit worker 应确认是否需要标注 stale report（过期报告）或修订报告生成流程。 |
| raw corpus 文件量大，存在 push/文件大小风险。 | Steward 会话先检查“没有发现超过 95MB 的单文件”，并把内容拆成 arXiv、GitHub+web、reports 等组。 | 分批 commit/push，避免一次性混杂提交；最终 `main` 同步 `origin/main`。 | 没有在本日报中逐文件审计所有 raw source 内容质量。 |

## 证据地图（Evidence Map）

| claim_id | 主张 | 支撑证据 | 证据强度 | 缺口 |
| --- | --- | --- | --- | --- |
| C20260522-01 | 当天存在实质开发证据，核心为 git 固化与 push。 | `git log --date=iso --name-status --since 2026-05-22 --until 2026-05-23` 命中 4 commits；Codex session lines 252-389 记录 commit/push；最终 status clean。 | 强 | 无当天新研究运行证据；只能认定 git/file-management 实质动作。 |
| C20260522-02 | `ec5ecd3` 固化了 5 月 21 日晚 corrected coverage-driven loop 的核心 artifacts。 | `git show --name-status ec5ecd3`；`git show ec5ecd3:<path>` 行数：27 candidates、27 triage、41 claims、41 coverage records、47 loop events、824 claim links；session lines 272-273。 | 强 | artifacts 内容质量未逐条审计。 |
| C20260522-03 | 当天固化的是前一晚运行结果，而不是当天新跑 loop。 | `loop_events.jsonl` 和 `loop_state.json` 时间戳为 `2026-05-21T12:48-13:37Z`；`coverage_status.md` Generated 为 `2026-05-21T13:37Z`；Codex 10:34 用户指令是 push。 | 强 | 无法排除当天 10:34 前非 Codex 的人工检查，但无证据显示新的 loop run。 |
| C20260522-04 | expanded corpus 在当天被拆为 arXiv 与 web/repo 两个 raw corpus commits。 | `e09ea2a` commit output 458 files/14 arXiv groups；`c14a93e` 39 files/5 GitHub repo groups/8 webpage groups；`git diff-tree` directory lists。 | 强 | 未逐篇核对论文/网页正文是否完整。 |
| C20260522-05 | 最终 loop status 报告宣称 coverage/gates pass，但同组有 stale audit artifact 风险。 | `41e8693:coverage_status.md` 8 areas supported；`41e8693:judgment_status.md` research_paper passed；`41e8693:goal_satisfaction_audit.md` Current Evidence still says not satisfied。 | 中高 | 需要后续审计判定是否为过期报告未刷新。 |
| C20260522-06 | 当天最终已 push 到 `origin/main` 且工作区在当时干净。 | Codex session lines 378-389：`git status --short --branch`、`git log --oneline`、untracked count 0、final answer 含 push directive。 | 强 | 本日报当前工作区有 2026-06-11 审计未跟踪文件；不代表 2026-05-22 结束态。 |

## 未解决问题

- `goal_satisfaction_audit.md` 与 `judgment_status.md`/`loop_state.json` 的状态不一致需要后续 audit worker 专门判断：它更像早期 audit artifact，但当前日报不直接修正文档或历史。
- raw corpus（原始语料）只确认采集、提交、目录和文件规模；未逐篇深读 arXiv、网页或 repo metadata 的内容完整性与摘要准确性。
- Reddit blocked（受阻）与 AICritique network_intercepted/http_error（网络拦截/HTTP 错误）缺口仍存在；`inaccessible_sources.xml` 记录了原因和下一步重试路径。
- `acquisition_failures.jsonl` 保留了早期失败尝试；使用时必须结合后续 acquire events、`sources.jsonl` 状态和 raw data commits，不能孤立解读。
- 当天可证实的是 Git/File Steward 的提交策略和固化动作；没有证据显示 5 月 22 日新增了研究问题定义、coverage framework 设计或内容性综合结论。

## 当日边界

- 不覆盖 `2026-05-23` 或后续 loop/KB 工作；后续日期只能在各自日报中追踪。
- 不把 `2026-06-11` 当前审计文件、未跟踪目录或本日报写入动作混入 `2026-05-22` 历史事实。
- 不使用 `docs/**` 作为唯一事实源；上一日日报、审计报告、source inventory 和 day queue 只作为路标，核心结论回到 git history、Codex transcript、`data/**` 和 `reports/**` 提交态 artifacts。
- 不把报告中的 `supported/pass` 直接扩大为“内容已充分可信”；这里只确认 loop stop condition（循环停止条件）与报告状态被提交。
- 不把 blocked Reddit 或 intercepted AICritique 的正文内容写成事实。
- 不写入 audits、decisions、final、repairs 或 day_queue；本文件仅为 daily draft（每日草稿）。

## 自检

- [x] 只读确认 `2026-05-22` 有项目实质开发证据，并使用 git history、Codex transcript、仓库 artifacts 三角校验（triangulation）。
- [x] 特别核查 `ec5ecd3` 是否固化 `2026-05-21 21:03-21:39 +0800` corrected loop artifacts，结论为已固化核心 runner/manifests/logs/reports 数据。
- [x] 明确区分 “2026-05-21 晚间运行” 与 “2026-05-22 上午 git 固化/push”。
- [x] 未使用 `docs/**` 作为唯一事实源。
- [x] 未把 `2026-05-23` 或后续事件写入当天结论。
- [x] 未把推测写成事实；对 stale report、raw corpus 内容质量、blocked sources 均标注缺口。
- [x] 未混入 `2026-06-11` 当前审计工作。
- [x] 本日报仅写入允许路径：`docs/audti/260611/daily/20260522_loop_manifests_expanded_corpus.md`。
