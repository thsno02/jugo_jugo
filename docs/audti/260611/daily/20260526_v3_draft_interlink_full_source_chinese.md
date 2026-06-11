# 2026-05-26 每日梳理：v3 批量草稿、全文读取纠偏与互链固化

---
status: draft
day_id: 20260526
audit_status: pending
source_window: "2026-05-26 00:00:00 +0800 至 2026-05-27 00:00:00 +0800"
---

## 当日结论

1. `2026-05-26` 是 v3 的实质开发日（substantive development day）：精确日期窗口内有 529 个 git commits，集中在 10:49 到 12:16 +0800，覆盖 v3 draft card（草稿卡片）、draft provenance（草稿溯源）、similarity top3（相似度前三）、comparison provenance（比较溯源）、interlink（互链）和 bookkeeping（簿记）固化。
2. 5/25 晚间 first pass（第一轮生产）的 4 张英文 draft 在当天首先被 git 固化，并在用户纠偏后改为中文主语言（Chinese primary language）。原始 Claude transcript 在 10:43 +0800 记录用户要求“ALL output should keep the chinese as the main language”，随后 Claude 立刻重写 4 张卡片和 provenance；Claude memory 的 `feedback_output_language_chinese.md` 是该纠偏的提炼层，不是唯一事实源。
3. 当天从“单材料 first pass”扩展为对 manifest（清单）中全部 72 条来源做批量处理：loop 快照在 commit `bf1e810` 记录 `materials_total=72`、`materials_drafted=43`、`materials_blocked_empty_source=22`、`materials_blocked_upstream=7`，并形成 171 张 draft cards、171 份 draft provenance、171 份 similarity、171 份 comparison provenance。
4. 全文读取（full-source read）策略是当天的关键纠偏：首轮 8 个 batch worker 对若干 arxiv 材料仍使用 `limit:2000` 或更小切片，用户在 11:09 +0800 指出 1M context window（上下文窗口）足以一次读完整材料。Claude 随后写入 `feedback_full_source_reads.md`，修订 worker template，并派 4 个 revision worker 全文重读 14 篇被截断论文，补出 34 张新卡，未编辑既有卡。
5. 当天完成 comparison provenance 和 interlink，但没有完成 adoption（采纳）或 public KB（公共知识库）落地。commit `bf1e810` 的 `loop_state.json` 明确 `new_cards_adopted=0`、`fusion_audits_completed=0`；14:15 +0800 用户让 Claude “do it” 后，Claude 准备 adoption 任务，但 14:16 +0800 因 API quota 报错终止，且 12:16 之后到 24:00 无新的项目 git commit。
6. 5/27 adoption wave（采纳波次）和 5/28 unified citation migration（统一引用迁移）不得回填到 5/26。当前工作区的 `outputs/llm_wiki/kb/cards/` 与当前 `status.json` 已包含后续结果，本日报只采用 5/26 当时的 git 快照、Claude transcript 和当日 loop artifact。

## 时间线

| 时间（Asia/Shanghai） | 事件 | 证据 | 影响 |
| --- | --- | --- | --- |
| 10:37 | 用户追问为什么只产 4 张卡，指出 `data/raw/` 里还有大量 papers/blogs/repos 未使用 | Claude transcript `4379...jsonl` line 221 | 触发从单材料 first pass 转向批量处理剩余材料 |
| 10:42 | 用户要求处理剩余材料 | Claude transcript line 231；line 239 | Claude 开始枚举 manifest，准备 batch approach（批处理方案） |
| 10:43 | 用户要求所有输出以中文为主语言 | Claude transcript lines 241、248；assistant line 249 | 首 4 张英文 draft/provenance 被重写为中文；similarity 与 v2 中文索引开始同语言比较 |
| 10:44-10:46 | Claude 重写 4 张 first-pass card 与 4 份 provenance 为中文 | Claude transcript lines 270、272、277、279、282、287、289 | first pass 的英文输出被纠偏，但文件 id/path 保持稳定 |
| 10:47 | manifest 盘点：72 entries、65 complete、7 pending_or_blocked、64 remaining complete；识别 0KB README | Claude transcript line 304 | 批量生产范围被定为 64 条剩余 complete 材料，7 条上游 pending 阻塞 |
| 10:49 | 当天首个 v3 draft card commit：`2a44b0e` | `git log --reverse`；Claude transcript line 349 | first pass 的 5/25 运行首次进入 5/26 git 固化（git solidification） |
| 10:48-10:52 | 创建项目 PostToolUse hook（钩子）和 `commit_card.sh`，用文件锁防并发提交冲突 | Claude transcript lines 336、354、384-397；git snapshot `29f41f3` | 每写一张 draft card 时自动提交 card + provenance + similarity sibling |
| 10:52-10:53 | 创建 `batch_worker_prompt.md` 并派 8 个 opus batch worker | Claude transcript lines 397、404-412 | 64 条 complete 材料并行生产中文 draft/provenance |
| 11:05-11:09 | batch worker 回报若干 arxiv 材料存在截断读取或分段读取 | Claude transcript lines 417、420、421、422、426、428 | 暴露 defensive pagination（防御性分页）问题 |
| 11:09-11:10 | 用户以 queued command 指出 1M context，可一次读完整 paper/blog/material | Claude transcript lines 416、429 | 形成全文读取纠偏的一手事实 |
| 11:10 | Claude 写入 `feedback_full_source_reads.md` 并把 memory index 链接到该反馈 | Claude transcript lines 432-440；memory mtime 2026-05-26 11:10 +0800 | Claude memory 成为该纠偏的二级索引，originSessionId 指向原始 transcript |
| 11:10-11:13 | `batch_worker_prompt.md` 被修订，4 个 revision worker 被派发全文重读 14 篇 arxiv 论文 | Claude transcript lines 441-459 | 修复被截断来源的 coverage（覆盖度）缺口 |
| 11:22-11:24 | revision workers 汇报新增 7 + 7 + 8 等卡，既有卡未发现事实错误 | Claude transcript lines 460、464、465 | 确认问题主要是 coverage gap（覆盖缺口），不是既有卡事实错误 |
| 11:34 | commit `29f41f3`：first-pass + arxiv revision bookkeeping 完成 | `git show 29f41f3` | 固化 72 materials、171 cards、hook、similarity tool、batch template、state/report |
| 11:39 | hook 扩展测试产生临时 comparison commit 并清理 | Claude transcript line 626 | 验证 comparison 自动提交路径；属工具验证噪声 |
| 11:57 | commit `0271592`：171 份 comparison provenance 完成，决策为 163 new_card、8 provenance_delta、0 others | `git show 0271592`；`audit_queue.md` at `bf1e810` | publication_gate 与 fusion_audit 的输入队列形成，但未 adoption |
| 12:03-12:16 | 创建 interlink worker template，派 6 个 cluster worker，填充 related 字段 | Claude transcript lines 792、804-810、833-883 | 171 张 draft 形成 wiki 风格内部互链 |
| 12:16 | commit `bf1e810`：interlinks complete for all 171 drafts | `git show bf1e810`；`git show bf1e810:.../loop_state.json` | 固化 974 条 related edges、0 dangling ids、0 orphan cards、new_cards_adopted=0 |
| 14:15-14:16 | 用户让 Claude 继续 adoption；Claude 建 adoption 计划后遭遇 API quota 错误 | Claude transcript lines 895、898-910 | 当天 adoption 只有 transcript 级尝试，无 loop artifact/git 落地 |
| 12:16-24:00 | 无项目 git commit | `git log --since '2026-05-26 12:16:23 +0800' --until '2026-05-27 00:00:00 +0800'` | 防止把 5/27 adoption 提前计入 5/26 |

## 关键决策

| 决策 | 决策者 | 理由 | 后果 | 证据 |
| --- | --- | --- | --- | --- |
| 从单材料 first pass 扩大到处理剩余材料 | 用户触发，Claude 执行 | 5/25 prompt 只处理 `karpathy-x-launch-post`，但用户希望覆盖 `data/raw/` 其余材料 | 读取 manifest，派 8 个并行 batch worker，最终对 72 条来源做完整 accounting（盘点） | Claude transcript lines 221、231、239、304；commit `29f41f3` |
| 所有人类可读输出以中文为主语言 | 用户明确纠偏 | v2 accepted cards 是中文，英文标题会让 Jieba/Jaccard similarity（相似度）失真 | 4 张英文 first-pass 卡被中文化，后续 worker template 强制中文 | Claude transcript lines 241、248、249、257、270；memory `feedback_output_language_chinese.md` |
| 大材料默认一次读完整源文件 | 用户明确纠偏 | 1M context window 足以容纳几百 KB paper；防御性 `limit:2000` 漏掉评估、appendix、ablation、prompts 等后半段知识 | 写入 `feedback_full_source_reads.md`，修订 batch template，派 4 个 revision worker，补 34 张卡 | Claude transcript lines 416、429、433、442、456-459；memory `feedback_full_source_reads.md` |
| 用 PostToolUse hook 自动按卡提交 | Claude 实现 | 并行 worker 会竞争 `.git/index.lock`，需要每卡及时固化且串行化 git 操作 | `commit_card.sh` 加 `/tmp/v3-commit-card.lock`，提交 card + provenance + similarity；后续扩展 comparison | `git show 29f41f3:.../hooks/commit_card.sh`；`git show 0271592:.../hooks/commit_card.sh` |
| comparison provenance 全量完成后再进入 publication/fusion gate | v3 pipeline 设计，Claude 执行 | title similarity 只给候选，不直接决定 adoption；需要三问比较和 audit queue | 171 comparison provenance；163 `new_card`、8 `provenance_delta`；8 条进入 audit queue | commit `0271592`；`git show bf1e810:.../queues/audit_queue.md` |
| interlink 在 adoption 前完成 | Claude 执行 | draft 状态先建立 wiki adjacency（相邻关系），publication 后再迁移路径/KB | 6 个 cluster worker 填 related；974 edges；0 dangling/orphan | commit `bf1e810`；interlink template |
| 5/26 不做 public KB adoption 结论 | 证据约束 | 当天 loop_state 明确 adoption=0；14:16 API error；12:16 后无 commit | adoption 保留为下一步，不能提前写入 5/26 | `bf1e810:loop_state.json`；Claude transcript lines 895-910；git log 空窗 |

## 实现变化

### v3 draft production（草稿生产）

- `outputs/llm_wiki/drafts/cards/` 在 5/26 形成 171 张 draft card；`outputs/llm_wiki/drafts/provenance/` 形成 171 份配对 provenance；`outputs/llm_wiki/drafts/similarity/` 形成 171 份 JSON similarity artifact。
- `queues/material_queue.md` 和 `queues/draft_backlog.md` 在 11:34 的 bookkeeping commit 中记录全量 material accounting：43 条材料产出卡、22 条 0KB empty source 跳过、7 条 upstream pending 阻塞。
- `tools/similarity_top3.py` 在 5/26 成为 similarity top3 的实现，使用 Jieba + Jaccard 读取 v3 draft titles 与 v2 accepted-card title index。
- `task_templates/batch_worker_prompt.md` 建立批处理 worker 合同，要求中文主语言、受限读写路径、每材料 2-5 张知识密集卡，并在用户纠偏后加入全文读取默认规则。

### hook 与自动提交（hook and auto-commit）

- `hooks/commit_card.sh` 在 commit `29f41f3` 中固化：当写入 `drafts/cards/<id>.md` 时，自动 stage card、同名 provenance、同名 similarity，并用 `/tmp/v3-commit-card.lock` 序列化并发提交。
- `commit_card.sh` 在 commit `0271592` 中扩展：写入 `drafts/comparison/<id>.md` 时自动提交 comparison provenance。
- `.claude/settings.json` 在 transcript 和当前工作区中可见，用于注册 PostToolUse hook；但该文件未进入 git 跟踪，因此它只能作为 runtime config（运行时配置）事实，不能作为 git 固化事实。

### full-source revision（全文修订）

- 首轮 batch worker 的报告显示多个 arxiv 只读前 600、800、2000 行或关键中段，Claude memory 记录这些行为造成了真实 coverage loss（覆盖损失）。
- 修订后派 4 个 revision worker 全文重读 14 篇论文：mem0、memgpt、alce、graphrag、lightmem、longmemeval、locomo、graph-poisoning、poisonedrag、ragchecker、wicer、memory-as-metabolism、etamp 等进入复核范围；ragas 被确认 paper portion（论文主体）只有约 357 行，首轮读到 600 行已覆盖主体，44MB 主要来自 bib appendix（参考文献附录）。
- revision worker 汇报新增 34 张卡，并说明既有卡未发现需要 edit 的事实错误，问题定位为 under-coverage（覆盖不足）。

### comparison 与 interlink（比较与互链）

- `task_templates/comparison_worker_prompt.md` 和 171 个 `drafts/comparison/*.md` 在 5/26 固化，comparison 判定为 163 张 `new_card`、8 张 `provenance_delta`、0 张 `merge_candidate`、0 张 `duplicate_skip`、0 张 `revise_before_gate`。
- `queues/audit_queue.md` 在 5/26 列出 8 张 provenance_delta，需要后续 fusion_audit（融合审计）。
- `task_templates/interlink_worker_prompt.md` 在 commit `bf1e810` 固化，6 个语义 cluster 为 171 张 draft 填 `related:`。loop_state 记录 974 条 related edges、平均每卡 5.70 条、0 dangling ids、0 orphan cards。

## 问题、坑、解决方案

| 问题/坑 | 触发 | 解决方案 | 残余风险 |
| --- | --- | --- | --- |
| first pass 只产 4 张卡 | 5/25 prompt 明确只读一个材料、产 2-5 张卡；用户 5/26 追问剩余材料 | 转为批量处理 manifest 剩余 complete 材料 | 批量处理放宽了原 first-pass context boundary（上下文边界），需要后续审计确认无越界影响 |
| 英文输出与中文主语言不一致 | 首 4 张 draft/provenance 是英文 | 用户 10:43 纠偏，Claude 重写为中文，并写入 memory | `feedback_output_language_chinese.md` 是提炼层，必须回到 transcript 验证 |
| 大论文防御性截断 | batch worker prompt 和具体 Agent prompt 仍出现 `limit:2000 first` | 用户 11:09 指出 1M context，Claude 写 memory、改 template、派 revision worker | commit `29f41f3` 的 prompt 前半已改全文读取，但“处理流程”仍残留“>200KB 用 limit:2000”；这是合同残余不一致 |
| 0KB github README 占比高 | 22 条 complete 材料实际为 0KB source | 标为 `blocked: empty_source`，不产卡 | 上游补齐后需要重新入队，5/26 不解决抓取缺口 |
| title similarity 误判 | 中文后 Jaccard 分布变得有意义，但仍有高频 token 干扰和漏邻居 | comparison provenance 全量复核，8 张 provenance_delta 入 audit queue | 3 张 similarity miss 在 5/26 报告中仍列为后续补查项 |
| 并行 worker 竞争 git index | 多 worker 同时写卡并触发 hook | `commit_card.sh` 加 lock dir 串行化 git 操作 | hook 依赖 `.claude/settings.json` 运行时配置，该配置未 git 固化 |
| JSON 写入中出现转义错误 | loop_state notes 中中文引号导致 JSON 校验失败 | Claude 读错误片段并修复，随后 commit `29f41f3` 成功 | 说明手写 JSON 易错，后续应优先脚本生成或 `json.tool` 校验 |
| adoption 启动但未落地 | 14:15 用户说 “do it”，Claude 准备 adoption workers | 14:16 API quota error 停止；无 git commit | 不得把 5/27 adoption 结果回填到 5/26 |
| 当前文件被后续日期污染 | 当前 `status.json`/`loop_state.json` 包含 5/28 unified citation；当前 `kb/cards/` 含后续 adoption | 使用 `git show bf1e810:path` 读取 5/26 快照 | 若只读工作区 current files，会把后续事件误写进 5/26 |

## 证据地图（Evidence Map）

| claim_id | 主张 | 支撑证据 | 证据强度 | 缺口 |
| --- | --- | --- | --- | --- |
| C20260526-01 | 5/26 是实质开发日，有 529 个 commits | `git log --since 2026-05-26 --until 2026-05-27`；hourly summary 10/11/12 点分别 64/293/172 commits | 强 | commit 数不含 ignored runtime config，如 `.claude/settings.json` |
| C20260526-02 | first pass 的 git 固化发生在 5/26 | earliest commit `2a44b0e` at 10:49 +0800；5/25 日报已记录运行在 5/25 | 强 | first pass 运行与固化分属两日，需要持续区分 |
| C20260526-03 | 中文主语言纠偏来自原始 transcript | Claude transcript lines 241、248、249、270；memory `feedback_output_language_chinese.md` mtime 10:43 | 强 | memory 是提炼层，不能单独证明 |
| C20260526-04 | 全文读取纠偏来自原始 transcript，并进入 Claude memory | queued command lines 416/429；assistant write memory line 433；memory `feedback_full_source_reads.md` mtime 11:10 | 强 | 用户原话作为 queued command attachment，不是普通 user message，但仍在 JSONL |
| C20260526-05 | 批量生产最终形成 171 drafts/provenance/similarity | commit `29f41f3` message；`bf1e810:loop_state.json` counters | 强 | 当前 working tree 已有后续 KB cards，不能用 current counts |
| C20260526-06 | revision pass 补了 34 张卡，未改既有卡 | loop report at `bf1e810`；revision worker reports lines 460/464/465；commit `29f41f3` message | 中强 | 未逐张全文审计 34 张卡内容，只核对 worker reports 与 counts |
| C20260526-07 | comparison provenance 全量完成且产生 163/8/0 决策 | commit `0271592` message；`bf1e810:loop_state.json` counters；`audit_queue.md` | 强 | comparison 文件逐张内容未全部人工读完 |
| C20260526-08 | interlink 全量完成，974 edges、0 dangling/orphan | commit `bf1e810` message；`bf1e810:loop_state.json` | 强 | 未复算每条 edge 的语义质量，只采纳验证指标 |
| C20260526-09 | 5/26 未完成 adoption | `bf1e810:loop_state.json` `new_cards_adopted=0`；`git ls-tree bf1e810 .../kb/cards | wc -l` 输出 0；14:16 API error | 强 | 14:15 后的 intent 存在，但无落地事实 |
| C20260526-10 | 5/27 adoption 与 5/28 unified citation 不属于当天 | 当天 12:16 后 git 空窗；当前 status 明示后续 `updated_at=2026-05-28` | 强 | 后续日报需另行处理 |

## 未解决问题

- 22 条 `empty_source` 和 7 条 `upstream_pending_or_blocked` 未在当天解决；它们不应被虚构成已覆盖材料。
- `batch_worker_prompt.md` 在 commit `29f41f3` 中仍存在局部残余指令“>200KB 用 `limit:2000`”，与全文读取新规则冲突。
- `source_access_log.jsonl` 仍只有 bootstrap 记录；批量读取大量 `data/raw/...` 虽按任务分配允许，但没有细粒度 access log（访问日志）可审计。
- similarity top3 仍有高频 token 误判和真实邻居漏出 top3 的风险；5/26 报告要求后续补查 3 张 similarity miss。
- `.claude/settings.json` 作为 hook 注册配置未进入 git，长期可恢复性依赖本地 ignored 文件。
- 14:15 adoption intent 因 API quota 未执行；后续若 5/27 继续，应在 5/27 日报中按新日期归属。

## 当日边界

- 本日报只覆盖 `2026-05-26 00:00:00 +0800` 到 `2026-05-27 00:00:00 +0800`。
- 不把 5/25 的 first pass 运行写成 5/26 运行事实；5/26 只记录其 git 固化和中文修订。
- 不把 5/27 的 adoption wave、KB index build、fusion/publication gate 通过写入 5/26。
- 不把 5/28 的 unified citation migration、typed footnotes、`related:` 自动派生写入 5/26。
- 不把当前工作区 `outputs/llm_wiki/kb/cards/` 作为 5/26 事实；`git ls-tree bf1e810 .../kb/cards` 显示当时为 0。
- Claude memory 只能作为二级索引（secondary index）；已回到原始 Claude transcript 校验对应用户原话和 tool write。
- `docs/**` 只作任务协议和索引，不作为当天事实唯一来源。

## 自检

- 已读取任务协议、source inventory、day queue，并按 day_id `20260526` 建立本地日期窗口。
- 已用 transcript（Claude JSONL）、loop artifact（v3 快照）、git history（529 commits 和关键 commit 快照）、Claude memory 做三角校验（triangulation）。
- 已区分运行发生时间（execution time）、git 固化时间（git solidification time）和后续当前文件状态（current state）。
- 已显式标注 residual risk（残余风险）：prompt 残余冲突、access log 缺口、similarity 误判、ignored runtime config、empty source。
- 已避免把 5/27 adoption 或 5/28 unified citation 提前写进 5/26。
- 本文件只写入允许路径 `docs/audti/260611/daily/20260526_v3_draft_interlink_full_source_chinese.md`。
