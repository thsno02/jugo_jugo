# 2026-05-25 每日梳理：v2 胶囊、v3 启动与 Codex 到 Claude Code 接力

---
status: draft
day_id: 20260525
audit_status: pending
source_window: "2026-05-25 00:00:00 +0800 至 2026-05-25 23:59:59 +0800"
---

## 当日结论

1. `2026-05-25` 是 LLM Wiki 项目的实质开发日：精确 git 窗口内有 129 个提交，覆盖原子事实卡（atomic_fact_card）生产、worker 修复、control plane（控制面）审计、brain mailbox（脑邮箱）实验、v2 设计采纳和 loop capsule（循环胶囊）布局固化。证据：`git rev-list --count --since ... --until ...`，以及 `git log --date=iso --name-status`。
2. 当日凌晨的主线是 Codex 驱动的 bottom-up KB 生产循环（bottom-up KB production loop）：从本地 `data/` 来源挖事实候选，执行者（worker）写 draft/provenance，独立审计（independent audit）后再采纳（adoption），main-agent 只做决策和调度。证据：Codex session `rollout-2026-05-25T02-33-10...jsonl` 的启动 prompt、`fork_context:false` dispatch、`loops/v2_llm_wiki_loop_20260525/CONTEXT_ISOLATION.md`、`PRELAUNCH_REQUIREMENTS.md`。
3. v2 产出了可核验的知识卡闭环，但吞吐过低触发设计转向：文件系统中有 64 个 `iteration_20260525_*` 目录、15 张 accepted KB cards、24 个 fact candidates 的报告记录；用户指出“7 小时只产出 15 张 accepted card”后，决策切到 draft-first（草稿优先）与后置 publication/fusion gate（发布/融合门禁）。证据：`loops/v2.../outputs/llm_wiki/kb/indexes/cards.md`、`loops/v2.../decisions/20260525-1035-switch-to-atomic-draft-first.md`、`reports/loop_report.md`。
4. 下午 v2 进一步从 atomic_fact_card 转为 scoped_knowledge_card（有范围的知识卡），并采用 brain mailbox（脑邮箱）架构：production/similarity/audit/ops brain 通过 inbox/outbox 和 `brainctl` 协调；但这只是 smoke test（冒烟测试）通过，不等于完整 scheduler（调度器）已实现。证据：`LOOP_DESIGN_V2.md`、`CARD_CONTRACT_V2.md`、`DRAFT_FIRST_PIPELINE.md`、`brains/smoke_tests/20260525_brain_mailbox_smoke.md`、`decisions/20260525-1551-adopt-loop-design-v2.md`。
5. user-insights（用户洞察）在当天被 bootstrap（启动）为正式侧路记录，但其自身 metadata 标注 `coverage: partial`，只能作为用户输入和设计判断的二级索引（secondary index），不能作为项目事实的唯一来源。证据：`user-insights/sessions/session_20260525_llm_wiki_loop_bootstrap/metadata.json`、`session_log.md`、git commit `cdd1476`。
6. 晚间出现 Codex 到 Claude Code 的交接：v3 capsule 要求 Claude 从磁盘文件恢复、不得依赖聊天记忆或 Codex skills；Claude transcript 在 21:34 +0800 收到 `V3 Loop Start Prompt`，随后按 draft-first pipeline 创建 4 张英文 draft card 的 transcript 记录，并明确不进入 public KB adoption。证据：Claude transcript `4379b2d9-db20-4573-9450-751bb398208a.jsonl`、`CLAUDE_CODE_HANDOFF.md`、`CONTEXT_BOUNDARY.md`、v3 draft/provenance 的 `created_time: 2026-05-25T22:05:00+08:00`。缺口：这些 v3 draft 首次进入 git 是 `2026-05-26`，当日 git 窗口没有 v3 draft commit。

## 时间线

| 时间（Asia/Shanghai） | 事件 | 证据 | 影响 |
| --- | --- | --- | --- |
| 00:47-00:52 | 前一日 v0/v1 漂移后的原子事实技能、KB tooling、drift audit 固化进 git | commits `c5117f7`、`9f3aa77`、`33a8fb0` | 为 5/25 凌晨 v2 生产 loop 提供恢复入口和修复背景 |
| 02:33 | 用户启动 long-horizon autonomous loop，要求 bottom-up、中文主语言、atomic_fact_card、provenance、audit/adoption、main-agent 不亲自生产 | Codex session `rollout-2026-05-25T02-33-10...jsonl` | 锁定当天核心目标和控制面约束 |
| 02:38-02:39 | user-insights 与 long-horizon control plane 落库 | git commits `cdd1476`、`a47a6cd`、`32995e7` | 正式区分用户洞察索引与 KB 事实来源，建立 task templates/tools/system prompts |
| 02:48-03:16 | 第一条 source mining -> drafting -> audit -> adoption 链路推进，包含 delivery marker repair | commits `f33dc4f` 到 `56740c2`；v2 decisions 02:41-03:16 | 验证从 fact candidate 到 accepted card 的最小闭环 |
| 03:19-08:12 | 多张来自 Karpathy gist 的 accepted cards 连续产生，并出现 adoption template、validate_scope、draft boundary 等修复 | v2 decisions、audits、`tools/validate_scope.py` repair commits | v2 强化了 read/write scope（读写边界）和 task packet（任务包）纪律 |
| 10:33-10:42 | 用户质疑吞吐，决策切到 atomic draft-first | commit `992fdf1`；`decisions/20260525-1035-switch-to-atomic-draft-first.md` | expensive audit/adoption 后移，draft backlog（草稿积压队列）成为中间层 |
| 14:13-14:23 | control-plane subagent/task audit 开始并落审计产物 | commits `d8ab36c`、`728978b`；`audits/20260525-control-plane-subagent-task-audit/*` | 验证 task boundary、lifecycle、flow 是否能只凭磁盘复核 |
| 15:32-15:38 | brain mailbox smoke test 完成 | commit `38bd6d6`；`brains/smoke_tests/20260525_brain_mailbox_smoke.md`；`logs/subagent_lifecycle.jsonl` | 证明 mailbox + router + wake marker 可实践，但未证明自动 spawn/resume |
| 15:51-16:19 | v2 设计采纳：brain mailbox + scoped_knowledge_card + Jieba/Jaccard similarity top3 + comparison provenance | `decisions/20260525-1551-adopt-loop-design-v2.md`；commit `9c10bfa` | v2 从单卡串行采纳转为更高吞吐的 draft-first/scoped card 架构 |
| 19:31-20:41 | v2 snapshot/archive 与 loop capsule repository layout 固化 | commits `6f1d7ff`、`d95fa61`、`ac4968c`、`396eca1` | v2 成为可恢复胶囊，仓库开始按 `loops/v*` 管理版本 |
| 21:06-21:25 | Claude Code runtime 验证：原生 sub-agent 不能递归派生；process-level `claude -p` 可作为独立内层 worker；auto permission/model 设置调整 | Claude transcript `46cda2aa-e94e-4141-9544-ca4d7367d5e7.jsonl` | 形成 v3 handoff 中“无继承上下文、prompt 必须自包含”的运行约束 |
| 21:34-22:05 | v3 first formal production pass 在 Claude Code 中启动，目标是 `karpathy-x-launch-post` -> 2-5 draft cards/provenance/similarity，禁止 adoption | Claude transcript `4379b2d9...jsonl`；v3 `CLAUDE_CODE_HANDOFF.md`；draft card transcript writes | v3 从 Codex 设计/胶囊过渡到 Claude Code 执行；当天结论限于启动与首轮 draft 尝试 |

## 关键决策

| 决策 | 决策者 | 理由 | 后果 | 证据 |
| --- | --- | --- | --- | --- |
| KB 生产采用 bottom-up，不先做 topic hub | 用户主导，main-agent 执行 | 用户多次纠偏 top-down 漂移，要求由 atomic 到 hub | v2 任务包以 fact candidate/card/provenance 为主对象 | Codex session 启动 prompt；user-insights E005/E009 |
| main-agent 是 control plane，不亲自写卡、审计或采纳 | 用户主导 | 保护上下文隔离（context isolation），避免父聊天成为事实来源 | worker 必须通过 task packet、read_log、delivery、audit 交付 | `PRELAUNCH_REQUIREMENTS.md`、`CONTEXT_ISOLATION.md`、`SUBAGENT_LIFECYCLE.md` |
| 大多数执行者采用 disposable lifecycle（阅后即焚生命周期） | main-agent 固化，用户原则驱动 | 长驻 worker 容易带入旧判断和未授权上下文 | source_mining/card_drafting/card_audit/card_adoption 默认任务结束即关闭 | `SUBAGENT_LIFECYCLE.md`、`logs/subagent_lifecycle.jsonl` |
| References（参考文献）在 Footnotes（脚注）之前，Footnotes 最后 | 用户明确纠偏 | Markdown 渲染中间 footnotes 会位置异常 | 写入 card worker prompt 与 v2 card contract | user-insights E008；`CARD_CONTRACT_V2.md`；Codex task packet |
| 先 batch draft，再 similarity/publication/fusion gate | 用户触发，main-agent 接受 | 串行 drafting/audit/adoption/commit 导致 7 小时仅 15 张 accepted cards | `draft_backlog.md` 和后置门禁成为 v2/v3 核心结构 | `20260525-1035-switch-to-atomic-draft-first.md` |
| v2 primary object 从 atomic_fact_card 变为 scoped_knowledge_card | 用户和 main-agent 协同 | 过度 atomic 导致信息量低，卡片必须是 knowledge 本身 | v2 contract 强调范围、证据、误用边界，不强制正文模板 | `20260525-1551-adopt-loop-design-v2.md`、`CARD_CONTRACT_V2.md` |
| v3 Claude Code handoff 不依赖隐藏技能、记忆或先前对话 | main-agent/Codex 为 Claude 准备 | Claude Code 接手时没有 Codex skill 上下文，必须从文件恢复 | `CLAUDE_CODE_HANDOFF.md` 与 `CONTEXT_BOUNDARY.md` 成为 source of truth | Codex final handoff；Claude transcript line 2/10 |
| v3 first pass 不做 direct adoption | main-agent/Codex 设计，Claude 执行 | draft-first 要先产出可恢复草稿和相似候选，publication gate 单独授权 | 当天只允许 draft/provenance/similarity/backlog/state/report，不写 public KB | `LOOP_START_PROMPT` transcript；v3 provenance “发表门控结果” |

## 实现变化

### v2 loop files（v2 循环文件）

- `loops/v2_llm_wiki_loop_20260525/` 成为 v2 capsule，包含 `README.md`、`RUNBOOK.md`、`CONTEXT_ISOLATION.md`、`PRELAUNCH_REQUIREMENTS.md`、`SUBAGENT_LIFECYCLE.md`、`LOOP_DESIGN_V2.md`、`CARD_CONTRACT_V2.md`、`DRAFT_FIRST_PIPELINE.md`。
- `iterations/` 下有 64 个 `iteration_20260525_*` 目录，覆盖 source mining、card drafting、audit、adoption、repair、batch drafting 等。
- `outputs/llm_wiki/kb/cards/` 有 15 张 accepted cards；`outputs/llm_wiki/kb/indexes/cards.md` 列出标题、路径、状态与来源。
- `decisions/` 记录从 control plane 建立、source mining 验收、候选选择、audit pass、adoption accepted，到 draft-first/v2 design adoption 的完整决策链。
- `audits/20260525-control-plane-subagent-task-audit/` 与 `audits/20260525-subagent-lifecycle-session-audit/` 为 task boundary（任务边界）、task flow（任务流）和 lifecycle（生命周期）提供独立复核。

### v2 brains、hooks、queues（脑、钩子、队列）

- `brains/` 引入 production/similarity/audit/ops lane（工作道）概念，使用 inbox/outbox、wake marker 和 `brainctl.py`。
- `brains/smoke_tests/20260525_brain_mailbox_smoke.md` 显示 audit -> production -> audit 的 message route（消息路由）成功，最终所有 brain idle。
- `hooks/brain-mailbox-hook.sh` 作为 repo-local hook-friendly command 被测试，但未完成全局 Codex hook 安装或自动 worker 唤醒。
- `queues/draft_backlog.md` 把 draft-first 的中间状态显式化，避免未审计草稿直接进入 public KB。

### v3 capsule（v3 胶囊）

- v3 的核心合同包含 `CLAUDE_CODE_HANDOFF.md`、`CONTEXT_BOUNDARY.md`、`SKILLS_AND_DEPENDENCIES.md`、`SUBAGENT_RUNTIME_CONSTRAINTS.md`、`RUNBOOK.md`、`CARD_CONTRACT_V3.md`、`DRAFT_FIRST_PIPELINE_V3.md`、`SIMILARITY_MECHANISM_V3.md`、`PROVENANCE_CONTRACT_V3.md`、`BRAIN_MAILBOX_PROTOCOL.md`。
- v3 明确以 draft-first pipeline 为正式生产路径：material -> knowledge-dense draft card -> draft provenance -> title similarity top3 -> comparison provenance -> decision -> publication/fusion gate -> adoption。
- v3 first pass 的 transcript 创建了 4 张英文 draft card：`idea-file-as-agent-era-artifact`、`llm-knowledge-base-five-stage-workflow`、`auto-index-replaces-rag-at-small-scale`、`file-outputs-back-as-compounding-loop`。当前磁盘版本已被 5/26 中文化/后续流程改写，不能把当前文件全貌当作 5/25 结果。
- v3 的第一轮 similarity 依赖 `jieba` + Jaccard（杰卡德相似度）和 v2 accepted-card title index；当日 transcript 和后续 artifact 均显示 cross-language title overlap（跨语言标题重叠）是一个风险点。

### handoff、hooks、brains、queues（交接、钩子、脑、队列）

- Codex 侧负责把 v3 运行入口压缩成自包含 prompt，Claude Code 侧从 `LOOP_START_PROMPT` 开始，不继承 Codex chat context。
- Claude Code runtime 测试证明标准 sub-agent 没有 Agent tool，不能递归开 sub-agent；需要通过顶层 Claude 编排或 process-level `claude --permission-mode auto -p "<self-contained prompt>"` 启动独立进程。
- `--permission-mode auto` 被选为长任务运行模式，原因是 headless inner Claude 不能卡在权限提示上，同时避免直接使用更粗暴的 bypass 路径。
- user-insights 侧路被确认是 recall/decision index，不是 KB fact source；当前 coverage partial，不阻塞 KB 生产。

## 问题、坑、解决方案

| 问题/坑 | 触发 | 解决方案 | 证据 |
| --- | --- | --- | --- |
| 目标从“生成 LLM Wiki KB”漂移成“讨论如何生成 KB” | 用户指出核心目的被误解 | 改为 bottom-up source mining，topic plan 只做建议 | user-insights E003/E005；Codex 启动 prompt |
| 只初始化 skill，不用 skill build KB | 用户要求 skill + KB 双交付 | loop 同时生产 KB cards 并演化 prompts/tools/skills | user-insights E006；v2 reports |
| main-agent 容易亲自执行 | 用户要求保持 context clean | 规定 main-agent 只能建任务、验收、修复控制面，生产交给 worker | `PRELAUNCH_REQUIREMENTS.md` |
| worker 忘记最终 delivery marker | 早期 drafting 交付失败 | 修复 base worker prompt，要求 `LOOP_DONE`/`LOOP_BLOCKED` | decisions 02:54；commit `54db249`、`cce4cab` |
| adoption/read boundary 噪声 | adoption template 允许读取边界不稳 | repair + independent audit 后再继续 | decisions 03:48/03:54 |
| `validate_scope.py` 未检查输入路径存在 | scope validation 漏洞 | 修复工具并记录 audit result | decisions 06:54；commit `6f08ec0` |
| drafting candidate boundary 不稳 | candidate block 可能混入未授权候选 | 修 prompt/template，再审计通过 | decisions 07:33/07:57；commit `bb96515` |
| 7 小时只 15 张 accepted cards | 用户质疑吞吐 | 改为 draft-first、batch audit/adoption、similarity/publication gate 后置 | decision 10:35 |
| 过度 atomic 让卡片像标题复述 | 用户反馈 card 必须是 knowledge | v2 改为 scoped_knowledge_card，正文不强模板但必须有信息量 | decision 15:51；`CARD_CONTRACT_V2.md` |
| Claude sub-agent 不能再开 sub-agent | 21:06 用户询问并要求实测 | 记录不能递归；可用 process-level `claude -p` 独立进程 | Claude transcript `46cda2aa...`；`SUBAGENT_RUNTIME_CONSTRAINTS.md` |
| Claude 无 Codex 上下文和技能 | v3 handoff 前提 | v3 capsule 文件成为唯一 source of truth，inner prompt 必须自包含 | `CLAUDE_CODE_HANDOFF.md`、`CONTEXT_BOUNDARY.md` |
| v3 首轮英文 draft 与中文主语言冲突 | 5/25 first pass 产出英文卡，5/26 才中文化 | 当天只记录为首轮 pass 缺口，不把 5/26 中文化提前写入 | Claude transcript；git 首次 v3 draft commit 在 5/26 |

## 证据地图（Evidence Map）

| claim_id | 主张 | 支撑证据 | 证据强度 | 缺口 |
| --- | --- | --- | --- | --- |
| C20260525-01 | 5/25 是实质开发日，有 129 个 git commits | `git rev-list --count` 精确窗口；`git log --date=iso --name-status` | 强 | commit 不能覆盖未提交 v3 工作 |
| C20260525-02 | v2 凌晨按 bottom-up atomic_fact_card 生产 loop 推进 | Codex session 启动 prompt；v2 `CONTEXT_ISOLATION.md`、`PRELAUNCH_REQUIREMENTS.md`、task dispatch | 强 | Codex transcript 体量大，本日报只抽关键片段 |
| C20260525-03 | v2 accepted KB card 数为 15 | `find .../kb/cards -name '*.md' | wc -l`；`kb/indexes/cards.md` | 强 | 后续迁移可能改变 root KB，但 v2 capsule 内稳定 |
| C20260525-04 | 吞吐问题触发 draft-first | 用户质疑记录；`20260525-1035-switch-to-atomic-draft-first.md` | 强 | 无需后验推断 |
| C20260525-05 | v2 采纳 brain mailbox/scoped card/Jieba similarity 设计 | `20260525-1551-adopt-loop-design-v2.md`；`LOOP_DESIGN_V2.md`；smoke test | 强 | 自动 scheduler 未验证 |
| C20260525-06 | user-insights bootstrap 只可作二级索引 | `metadata.json` 明示 `coverage: partial`；`session_log.md` | 强 | 缺完整 transcript coverage |
| C20260525-07 | Claude Code handoff 要求无上下文从文件恢复 | `CLAUDE_CODE_HANDOFF.md`；Claude transcript 21:34 读取 handoff | 强 | v3 当前文件后续被 5/26-5/28 改写，需用 transcript 定日界 |
| C20260525-08 | Claude sub-agent 不能递归派生，process-level nesting 是替代路径 | Claude transcript `46cda2aa...`；`SUBAGENT_RUNTIME_CONSTRAINTS.md` | 强 | 官方文档引用未在本日报二次联网核验 |
| C20260525-09 | v3 first formal production pass 在 5/25 启动并创建 4 张初稿 | Claude transcript line 2 prompt、line 103-108 card writes；draft cards `created_time` | 中强 | 当日 git 无 v3 draft commit；current iteration status/delivery 未同步 |
| C20260525-10 | v3 first pass 不允许直接 adoption | LOOP_START_PROMPT transcript；v3 provenance “发表门控结果” | 强 | 后续 5/26-5/27 adoption 不属于当天 |

## 未解决问题

- v2 brain mailbox 只完成文件层 smoke test，未证明全局 hook 自动安装、自动 spawn/resume 或真正长期调度。
- v2 已有 V1 accepted cards 是否需要按 V2 metadata 和知识密度标准迁移，当天只记录为残余风险。
- v3 first formal production pass 的 5/25 transcript 证据强，但 5/25 git 落库证据弱；first draft card commits 出现在 2026-05-26，current v3 files 还包含 5/26-5/28 改写。
- v3 current `loop_state.json` 和 `loop_report.md` 已被后续统一 citation migration 等内容覆盖，不能直接作为 5/25 state 使用。
- v3 first pass 的英文输出与用户“中文主语言”要求冲突；中文化发生在 5/26，不写入当天成果。
- title Jaccard similarity（标题杰卡德相似度）容易受语言和高频 token 干扰，5/25 已露出 cross-language 风险，后续需要停用词、alias 或 comparison provenance 消化。
- user-insights 记录 coverage partial，若未来可恢复 full transcript，应重跑或修补 coverage。

## 当日边界

- 不把 2026-05-26 的中文化、全文读取、批量 draft/interlink/comparison/adoption 写成 5/25 成果。
- 不把 2026-05-27/05-28 的 v3 adoption wave、unified citation migration、171 卡指标写入 5/25 结论。
- 不把 2026-06-11 当前审计工作混入当天开发时间线。
- `docs/**` 和 `user-insights/**` 只作为索引或二级材料；关键事实必须回到 git、Codex/Claude transcript、loop artifacts。
- v3 当天描述采用“启动与首轮生产 pass 尝试/初稿创建”，不声称当日 git 已完整固化 v3 production artifacts。

## 自检

- 已使用 git history、Codex transcript、Claude transcript、loop artifacts、user-insights 做三角校验（triangulation）。
- 已区分 v2 的 atomic_fact_card、audit/adoption gate、sub-agent lifecycle、main-agent control plane、v2 decisions/iterations。
- 已区分 v3 capsule、draft-first pipeline、Claude Code handoff、first formal production pass、publication gate 不直接 adoption。
- 已记录中文主语言、bottom-up vs top-down、skill+KB 双交付、main-agent 不亲自生产、References/Footnotes 顺序、subagent context isolation、Claude 无上下文恢复等设计变化。
- 已显式排除 5/26 及后续大规模生产事件。
- 本文件只写入允许路径 `docs/audti/260611/daily/20260525_v2_v3_handoff_user_insights.md`。
