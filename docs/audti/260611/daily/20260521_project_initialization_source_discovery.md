# 2026-05-21 每日梳理：项目初始化、来源发现与覆盖框架

```yaml
status: draft
day_id: 20260521
audit_status: pending
source_window: "2026-05-21 00:00:00 +0800 至 2026-05-21 23:59:59 +0800；主要实质窗口为 16:43-21:39 +0800"
```

## 当日结论

1. `2026-05-21` 确有项目实质开发证据，且不是单纯讨论：当天 git history 有 6 个 commit，从空壳项目推进到采集脚本、manifest、raw source corpus、报告和 coverage framework（覆盖框架）。
2. 当天建立了 raw knowledge database（原始知识库）阶段的仓库骨架：`README.md`、`docs/RESEARCH_PROTOCOL.md`、`scripts/fetch_sources.py`、`data/manifests/**`、`data/raw/**`、`reports/**` 均在当天 commit 中出现。
3. 第一轮 source acquisition（来源获取）已固化为 45 个 seed sources（种子来源）、38 个成功、6 个 Reddit blocked（受阻）、1 个 AICritique/intercept failure（拦截失败），并保留访问日志和 raw files（原始文件）。
4. arXiv acquisition（arXiv 获取）在当天被明确调整为 source-first（源码优先）：优先 `e-print` TeX/source bundle（源码包），PDF 只作为 fallback（兜底）；当天报告记录 3 个 arXiv entries，其中 2 个 TeX/source archives、1 个 PDF-only。
5. coverage framework（覆盖框架）当天已经形成，并把 LLM Wiki 研究拆成 definition（定义）、source preservation（来源保留）、knowledge compilation（知识编译）、persistent representation（持久表示）、provenance/auditability（溯源与可审计性）、maintenance（维护）等可证据化维度。
6. Codex transcript（会话记录）显示 21:03-21:39 又发生了一轮 coverage-driven loop（覆盖驱动循环）修复和扩展，包含 `run_loop.py`、72 条 sources、27 个候选源、41 条 claims、`SATISFACTION PASS`/`VERIFY PASS`。但这些动作未出现在当天 6 个 git commit 中，当前只能作为 transcript 强证据，不应等同于当天已 git 固化的事实。
7. 当天仍存在清晰缺口：Reddit 本地抓取受阻、AICritique 企业文章被拦截、实证评估（empirical evaluation）和治理风险（governance risk）材料不足；当天报告明确判断当前资料足够 landscape memo（格局备忘录），不足以支撑强 empirical paper（实证论文）。

## 时间线

| 时间（+0800） | 事件 | 证据 | 影响 |
| --- | --- | --- | --- |
| 16:43-16:46 | Codex 主线程检查 repo、工具和插件能力，判断仓库几乎为空壳，基础采集应依赖 `git`、`curl`/`wget`、Python、`requests` 等通用工具。 | Codex session `rollout-2026-05-21T16-39-08...jsonl` 的 agent messages；命令检查 `git status`、工具路径、skill/plugin 列表。 | 确定 acquisition（采集）不依赖新安装 crawler plugin（爬虫插件），而是自建轻量脚本。 |
| 17:48-18:03 | 建立 raw-source acquisition workspace（原始来源采集工作区），新增 README、research protocol、fetch script、seed manifest，并跑第一轮抓取。 | transcript 记录“repo 从空壳变成采集工程”；git commit `7ee730c`、`3e3ba65`、`11f7f41`；`git show --stat` 显示脚本、manifest、raw data 新增。 | 项目从空仓库进入可恢复的本地 raw database 阶段。 |
| 18:03 | 第一轮 acquisition 完成：45 seed、38 ok、15 repo clone、3 arXiv、raw 约 162 MB、2,765 files，并记录 blocked/failure。 | transcript final message；commit `8c9ab22:reports/acquisition_status.md`；`sources.jsonl` status counts 为 38 ok、6 blocked、1 http_error。 | 建立第一批证据库，同时把 blocked sources（受阻来源）作为证据缺口保存。 |
| 19:04-19:07 | 用户/主线程将 arXiv 采集方向改为 TeX/source-first，而不是 PDF-first；脚本改为优先 `https://arxiv.org/e-print/<id>`。 | transcript 中“对，这个取向要改”；commit `8c9ab22:scripts/fetch_sources.py` 中 `fetch_arxiv`、`eprint_source_kind`、`agent_source_bundle.txt` 逻辑；`docs/RESEARCH_PROTOCOL.md` 的 arXiv source rule。 | 提升 agent-readable（代理可读）证据质量，避免未来 synthesis（综合）优先读 PDF。 |
| 19:07-19:11 | 生成 first-principles coverage framework（第一性原理覆盖框架），并让 sub-agent 做 source gap review（来源缺口审计）。 | transcript final message；commit `b4eab5d` 和 `8c9ab22` 的 `reports/coverage_framework.md`、`reports/source_gap_review.md`、`reports/initial_gap_checklist.md`。 | 将后续研究从“收集材料”升级为 coverage-driven（覆盖驱动）的证据评估。 |
| 19:55:14 | 提交项目文档和 fetch tooling（获取工具）。 | git commit `7ee730cfb2df60cf53650d1989b57bb1d79a7bc5`，新增 `.gitignore`、`README.md`、`docs/RESEARCH_PROTOCOL.md`、`scripts/fetch_sources.py`。 | 当天第一个 git 固化点，确认项目初始化。 |
| 19:55:20 | 提交 source discovery manifests（来源发现清单）。 | git commit `3e3ba65b69ba3053542a91e98a039c8a719ee380`，新增 `data/discovery/**`、`data/logs/source_access_log.jsonl`、`data/manifests/**`。 | 固化 seed/source manifest 与访问日志。 |
| 19:55:48 | 提交 collected raw source materials（已采集原始材料）。 | git commit `11f7f41c358fc0bd4f9b3da13a2f039dc61835b2`，新增 166 个 raw files，包括 arXiv、gist、GitHub repos、HN、PyPI、Reddit block pages、webpages。 | 将 raw corpus（原始语料）纳入版本历史。 |
| 19:55:55 | 提交 acquisition status reports（采集状态报告）。 | git commit `b4eab5d2a6d141fb453e05015b9cf9764eba257a`，新增 `loop_manifest.json`、`loop_state.json`、`reports/acquisition_status.md`、`coverage_framework.md`、`initial_gap_checklist.md`、`source_gap_review.md`。 | 固化状态报告和初版 coverage framework。 |
| 19:56:04 | 将 local source repository snapshots（本地来源仓库快照）加入忽略。 | git commit `9d6a22e0b65427d907a96b3b71d2dda94d5ba031` 修改 `.gitignore`。 | 控制 Git 体量，避免把 clone 内部 `.git` 等快照继续纳入主仓库。 |
| 20:00:10 | 完善 coverage framework。 | git commit `8c9ab22543b309ae43b3bbf4bd85c133b8d26ab7`，`reports/coverage_framework.md` 1201 insertions、91 deletions。 | coverage framework 成为当天最完整的研究边界文档。 |
| 21:03-21:39 | 修复 corrected coverage-driven loop（修正版覆盖驱动循环），补齐 discover/triage/acquire、重跑并达到 `SATISFACTION PASS` 和 `VERIFY PASS`。 | Codex transcript `rollout-2026-05-21T16-39-08...jsonl`；命令输出显示 72 `sources.jsonl`、27 `candidate_sources.jsonl`、27 `triage_decisions.jsonl`、41 `claims.jsonl`、41 `coverage_records.jsonl`。 | 证明当天有后续实质开发，但当天 git history 未固化这批新增 loop artifacts，证据强度需与 commit 区分。 |

## 关键决策

| 决策 | 决策者 | 理由 | 后果 | 证据 |
| --- | --- | --- | --- | --- |
| 当前阶段只做 raw acquisition（原始获取）与 preservation（保留），不做 final wiki synthesis（最终 wiki 综合）。 | 主线程/Codex；由项目协议固化 | 先保存 source URL、raw files、metadata、hash、fetch time，避免早期过度总结。 | 形成 `data/raw/**`、`data/manifests/sources.jsonl`、`source_access_log.jsonl` 的原始证据库。 | `8c9ab22:docs/RESEARCH_PROTOCOL.md` 的 Current Stage 和 Source Rules；`7ee730c` commit。 |
| 不安装新包，第一版采集用已有工具和轻量脚本。 | 主线程/Codex；工具审计 sub-agent 支持 | 本机已有 `git`、`gh`、`curl`/`wget`、Python、`requests` 足以完成 raw acquisition；额外 HTML/PDF 抽取包可后置。 | `scripts/fetch_sources.py` 成为 dependency-light fetcher（轻依赖获取器），optional extraction packages 需用户批准。 | transcript 16:43-17:49；`8c9ab22:docs/RESEARCH_PROTOCOL.md` Tooling Policy。 |
| arXiv 改为 source-first（源码优先），PDF 仅 fallback（兜底）。 | 用户方向 + 主线程执行 | Agent 后续阅读 TeX/source bundle 比 PDF 更稳定；部分 arXiv e-print 现实上只返回 PDF，需要标注。 | `fetch_sources.py` 写入 `source.tar.gz`、`source/`、`agent_source_bundle.txt`；PDF-only 记录 metadata note。 | transcript 19:04-19:07；`8c9ab22:scripts/fetch_sources.py`；`reports/acquisition_status.md`。 |
| coverage framework 先按 first principles（第一性原理）定义，再用 sub-agent 做独立 gap review。 | 主线程/Codex，按用户要求执行 | 仅有来源列表不足以判断研究是否充分；需要覆盖维度和缺口审计。 | 生成 `reports/coverage_framework.md`、`source_gap_review.md`、`initial_gap_checklist.md`。 | transcript 19:07-19:11；commit `b4eab5d`、`8c9ab22`。 |
| corrected loop 的 stop condition（停止条件）应是 coverage satisfaction（覆盖满足），不是 structural verify（结构校验）。 | 用户明确纠偏，主线程执行 | 用户指出 plan 核心逻辑是持续寻找信息直到 data 满足 coverage；`verify` 只能说明结构健康。 | 21:03-21:39 的 transcript 显示新增 discover/triage/acquire 闭环，并最终 `SATISFACTION PASS`。 | transcript 用户消息 21:03；`run_loop.py satisfaction/verify` 输出；但缺少当天 git commit 固化。 |

## 实现变化

- 项目初始化（project initialization）：新增 `.gitignore`、`README.md`、`docs/RESEARCH_PROTOCOL.md`、`scripts/fetch_sources.py`，把仓库定位为 LLM Wiki raw-source acquisition workspace。
- source discovery（来源发现）：新增 `data/discovery/github_search_*.json`、`data/manifests/seed_sources.json`、`data/manifests/sources.jsonl`、`data/manifests/acquired_sources_index.md`、`data/logs/source_access_log.jsonl`。
- raw source acquisition（原始来源获取）：新增 `data/raw/**`，类型包含 gist、webpage、hacker_news、reddit block pages、PyPI、arXiv、GitHub repo metadata/README/clone。
- acquisition reporting（采集报告）：新增 `reports/acquisition_status.md`，记录 45 seed、38 ok、6 blocked、1 http_error、162 MB raw data、2,765 raw files、15 repo clone、3 arXiv entries。
- coverage framework（覆盖框架）：新增并扩展 `reports/coverage_framework.md`，定义 LLM Wiki 的 primitive objects（基本对象）、core claims（核心主张）、coverage dimensions（覆盖维度）和 evidence requirements（证据要求）。
- gap analysis（缺口分析）：新增 `reports/source_gap_review.md` 和 `reports/initial_gap_checklist.md`，明确 landscape memo 可行、strong empirical paper 不足。
- 当天 transcript 还显示后续 loop runner（循环运行器）扩展：`scripts/run_loop.py`、candidate/triage/claims/coverage records 等。但这些未出现在当天 git commit，应作为当天未固化或后续待追踪 artifacts。

## 问题、坑、解决方案

| 问题/坑 | 证据 | 解决方案 | 剩余风险 |
| --- | --- | --- | --- |
| Reddit sources 在 terminal/browser capture paths 均 blocked。 | `sources.jsonl` 6 条 `blocked`；`reports/acquisition_status.md` Known Gaps；`source_gap_review.md` Community Discourse。 | 保留 block/raw 记录，建议后续用 approved Reddit-capable API、alternate network 或 manual export。 | Reddit 社区反馈、插件使用体验、long-PDF/multimodal 讨论仍缺。 |
| AICritique 企业文章被 network safety page/intercept 接管。 | `sources.jsonl` 中 `aicritique-enterprise-knowledge` 为 `http_error`；`source_gap_review.md` 说明 text 仅含拦截信息。 | 保留 intercepted response，并在 gap review 中列为 enterprise evidence 缺口。 | 企业适用性证据仍偏 blog/vendor narrative。 |
| GitHub API metadata 曾撞 rate limit 或不完整。 | transcript 19:08 提到无认证 `requests` 抓 API metadata rate limit；source_gap_review 指出 metadata 后续已改善但仍不足。 | 使用已配置 `gh api` 补齐 15 个 repo metadata。 | contributors、release history、issue/PR analysis、traffic/downloads 仍缺。 |
| arXiv PDF 对 agent 不友好。 | 用户纠偏和 transcript 19:04；协议明确 source-first。 | 改 `fetch_sources.py` 优先 e-print source bundle，生成 `agent_source_bundle.txt`。 | `arxiv-knowledge-compounding` 仍是 PDF-only，需 metadata 标注和后续人工处理。 |
| coverage loop 曾把 structural verify（结构校验）误当完成。 | transcript 21:03 用户指出 corrected plan；21:15 agent 发现 failed acquisition 未阻塞 satisfaction。 | 修复 runner：failed acquisition 继续阻塞，重试/替换来源，最终 `SATISFACTION PASS`。 | 当天 git commit 未固化该 runner 结果，需要后续日期追踪其提交状态。 |

## 证据地图（Evidence Map）

| claim_id | 主张 | 支撑证据 | 证据强度 | 缺口 |
| --- | --- | --- | --- | --- |
| C20260521-01 | 当天确有实质项目开发。 | git log 当天 6 commits；Codex session 从 16:43 到 21:39；`data/**`、`reports/**` artifacts。 | 强 | 21:03 后部分动作缺少当天 commit 固化。 |
| C20260521-02 | 项目从空壳初始化为 raw-source acquisition workspace。 | transcript 16:43 “repo 几乎空壳”；commit `7ee730c` 新增 README、protocol、fetch script。 | 强 | 空壳状态主要来自 transcript 和 git 状态，不是单独 artifact。 |
| C20260521-03 | 当天第一轮采集固化为 45 seed、38 ok、6 blocked、1 http_error。 | `8c9ab22:data/manifests/seed_sources.json` length 45；`sources.jsonl` status counts；`reports/acquisition_status.md`。 | 强 | 工作区后续 sources 已变化，必须用 commit 版本复核。 |
| C20260521-04 | raw corpus 覆盖 gist、HN、PyPI、arXiv、webpages、GitHub repos 和 blocked Reddit pages。 | `acquired_sources_index.md`；commit `11f7f41` raw files；`sources.jsonl` source list。 | 强 | 内容质量未逐文件深审。 |
| C20260521-05 | arXiv source-first 策略当天确立。 | transcript 19:04-19:07；`docs/RESEARCH_PROTOCOL.md`；`fetch_sources.py` `e-print`/`agent_source_bundle.txt` 逻辑；`acquisition_status.md`。 | 强 | 只有 3 个首批 arXiv entries；更大 arXiv corpus 属后续/未当天 git 固化。 |
| C20260521-06 | coverage framework 当天形成并被完善。 | commit `b4eab5d` 新增，commit `8c9ab22` 大幅扩展；`coverage_framework.md` 内容。 | 强 | 框架是研究规范，不等于已满足全部证据。 |
| C20260521-07 | 当天的 gap review 判断资料足够 landscape memo，不足强 empirical paper。 | `source_gap_review.md`、`initial_gap_checklist.md`、`acquisition_status.md` Known Gaps。 | 强 | 该判断基于首批 corpus，不覆盖 21:03 后扩展 corpus。 |
| C20260521-08 | corrected coverage-driven loop 在 21:03-21:39 实质运行并通过 satisfaction/verify。 | transcript 中 create_goal、run_loop commands、`SATISFACTION PASS`、`VERIFY PASS`、72 sources/41 claims 输出。 | 中高 | 未见当天 git commit；需要后续日期追踪是否提交及是否被修改。 |
| C20260521-09 | Reddit 和 AICritique 是当天明确证据缺口。 | `sources.jsonl` blocked/http_error；`reports/acquisition_status.md` Known Gaps；`source_gap_review.md` Missing Evidence。 | 强 | 可后续通过替代访问路径补证。 |

## 未解决问题

- 21:03-21:39 的 corrected loop artifacts（`run_loop.py`、`candidate_sources.jsonl`、`claims.jsonl`、`coverage_records.jsonl` 等）当天未在 git commit 中固化；其最终提交日期、是否被后续修改，需要在 `2026-05-22` 或后续日梳理中继续追踪。
- 首批 raw corpus 的内容质量没有逐源审计；当前仅确认 acquisition/provenance（采集与溯源）和报告结论。
- Reddit、AICritique、enterprise governance（企业治理）、empirical evaluation（实证评估）、citation/provenance accuracy（引用/溯源准确性）仍是证据缺口。
- GitHub adoption（采用情况）当天只到 stars/forks/issues 等粗粒度 metadata，缺 contributors、release history、issue/PR 语义分析和真实使用数据。
- `coverage_framework.md` 是当天研究边界和评价框架，不能直接当作事实结论或最终总线路。

## 当日边界

- 不覆盖 `2026-05-22` 的 expanded corpus commits、loop status reports 或后续归档动作，只在必要处说明 21:03 后当天 transcript 存在未固化动作。
- 不把 `2026-06-11` 当前审计工作混入当天开发线。
- 不以 `docs/**` 作为唯一事实源；涉及 docs/reports 的结论均用 git commit、transcript、`data/**` manifest/raw artifacts 交叉校验。
- 不推断 blocked Reddit 或 intercepted AICritique 的正文内容。
- 不把 landscape memo readiness（格局备忘录可写）扩大为 empirical paper readiness（实证论文可写）。
- 不写入 final timeline（最终总线路）结论；本文件仅为 `draft` 和 `audit_status: pending`。

## 自检

- [x] 只读确认 `2026-05-21` 有项目实质开发证据，并使用 git history、Codex transcript、仓库 artifacts 三角校验（triangulation）。
- [x] 日报主语言为中文，关键术语使用中文（English）锚定。
- [x] 未使用 `docs/**` 作为唯一事实源。
- [x] 未把后续日期事件写成当天结论；21:03-21:39 当天 transcript 但未当天 commit 的动作已明确降级。
- [x] 未把推测写成事实；对无明确证据处标注缺口。
- [x] 未混入 `2026-06-11` 当前审计工作。
- [x] 本日报仅写入允许路径：`docs/audti/260611/daily/20260521_project_initialization_source_discovery.md`。
