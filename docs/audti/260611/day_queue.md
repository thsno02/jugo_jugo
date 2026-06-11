# 日期队列（Day Queue）

队列范围：从可证据化起点 `2026-05-21` 到最后实质开发记录 `2026-06-08`。`2026-06-09` 到 `2026-06-11` 当前不进入历史每日梳理；原因见“排除日期”。

状态（status）在 inventory 阶段只使用 `pending` 或 `excluded`；进入执行阶段后，主控验收通过的日期可更新为 `accepted`，需要返修的日期可更新为 `repair_required`，阻断日期可更新为 `blocked`。

## 待处理日期（Pending Days）

| 日期 | day_id | 状态 | 候选主题 | 主要证据源 | 下一步 worker 指令摘要 |
| --- | --- | --- | --- | --- | --- |
| `2026-05-21` | `day_20260521` | accepted | 项目初始化、source discovery、raw source acquisition、coverage framework | `git log`、Codex sessions、`data/**`、`reports/**` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；下一天追踪 corrected loop artifacts 的 git 固化 |
| `2026-05-22` | `day_20260522` | accepted | loop run manifests、expanded corpus、logs/manifests | `git log`、`data/logs/**`、`data/manifests/**` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；后续继续将 stale/inconsistent report 作为残余风险处理 |
| `2026-05-23` | `day_20260523` | accepted | 缺口日/过渡空窗日：未确认实质项目开发 | Codex archived sessions、git/loop 空窗复核 | 已通过 daily synthesis、independent audit 和 main-agent acceptance；这是“空窗日通过”，不纳入实质开发阶段叙事 |
| `2026-05-24` | `day_20260524` | accepted | v0/v1 loop capsule、topic hub skeleton、context isolation audit | Codex sessions、`loops/v0*`、`loops/v1*` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；5/25 凌晨 commit 仅作为后验固化处理 |
| `2026-05-25` | `day_20260525` | accepted | v2 loop capsule、v3 launch、brain mailbox、user-insights bootstrap | Claude JSONL、Codex JSONL、`loops/v2*`、`loops/v3*`、`user-insights/**`、`git log` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；v3 first pass 记录为 5/25 运行、5/26 git 固化 |
| `2026-05-26` | `day_20260526` | accepted | v3 draft/interlink 大规模生产、全文读取与中文约束 | Claude JSONL、`loops/v3*`、`git log`、Claude memory | 已通过 daily synthesis、independent audit 和 main-agent acceptance；5/27 adoption 与 5/28 unified citation 不回填到本日 |
| `2026-05-27` | `day_20260527` | accepted | v3 adoption、comparison provenance、user-insights 提炼 | Claude JSONL、Codex JSONL、`user-insights/**`、`loops/v3*`、`git log` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；5/28 unified-citation migration 与 5/29 合同/脚本固化不回填到本日 |
| `2026-05-28` | `day_20260528` | accepted | v3 adoption wave、provenance 和 KB cards 批量提交 | Claude JSONL、`loops/v3*`、`git log` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；672 个 commits 解释为 171 张既有 KB card 的多轮 migration edits，而非新增卡 |
| `2026-05-29` | `day_20260529` | accepted | v3 capsule 收束、uploads、active 候选登记、memory 反馈 | Claude JSONL、Claude memory、`loops/v3*`、`git log` | 已通过 daily synthesis、round1 repair、independent reaudit 和 main-agent acceptance；保留 no Co-Authored-By rule 的分段提交事实 |
| `2026-05-30` | `day_20260530` | accepted | 缺口日：暂无明确主证据 | 后续复查 Codex/Claude/git 空窗 | 已通过 daily synthesis、independent audit 和 main-agent acceptance；验收类型为 transition_window_pass，只支持跨午夜尾声/近空窗 |
| `2026-05-31` | `day_20260531` | accepted | 缺口日：暂无明确主证据 | 后续复查 Codex/Claude/git 空窗 | 已通过 daily synthesis、independent audit 和 main-agent acceptance；验收类型为 empty_window_pass |
| `2026-06-01` | `day_20260601` | accepted | Claude 少量记录，v4 前置候选 | Claude JSONL | 已通过 daily synthesis、independent audit 和 main-agent acceptance；验收类型为 transition_planning_pass，不是 v4 实质生产日 |
| `2026-06-02` | `day_20260602` | accepted | v4 loop id / 设计启动候选 | Claude JSONL、Codex JSONL、`loops/v4*` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；验收类型为 transition_runtime_pass，主线是未提交演示材料运行产出，不是 v4 初始化 |
| `2026-06-03` | `day_20260603` | accepted | 本项目空窗、Codex 外部工作区活动过渡 | Codex archived sessions、Claude/git/mtime 排除证据 | 已通过 daily synthesis、independent audit 和 main-agent acceptance；验收类型为 empty_window_pass，不是 v4 前置开发日 |
| `2026-06-04` | `day_20260604` | accepted | v4 初始化、loop start prompt、Phase 1-2、karpathy-gist 实验 | Claude JSONL、Codex JSONL、`loops/v4*`、`git log` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；后续 6/5 不得回写 Phase 4/治理修复到本日 |
| `2026-06-05` | `day_20260605` | accepted | v4 Phase 4、governance 门禁完成、dedup/cross-link/质量抽检 | Claude JSONL、Claude memory、`loops/v4*`、`git log` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；治理补救不是最终质量闭环，6/7/6/8 继续承接审计修复 |
| `2026-06-06` | `day_20260606` | accepted | 缺口日：暂无明确主证据 | 后续复查 Codex/Claude/git 空窗 | 已通过 daily synthesis、independent audit 和 main-agent acceptance；验收类型为 empty_window_pass，6/5 与 6/7 之间保持空窗 |
| `2026-06-07` | `day_20260607` | accepted | v4 FSJS 审计、fix plan、全量修复与验证 | Claude JSONL、`loops/v4*`、`git log` | 已通过 daily synthesis、independent audit 和 main-agent acceptance；`fix_verification.json` 停在 `fb7b406`，末态断裂引用归零由 `5d7586f` git 快照证明 |
| `2026-06-08` | `day_20260608` | accepted | v4 deep audit、blind spots、pipeline gaps、arxiv/repo/scrape flags 修复 | Codex JSONL、`loops/v4*`、`git log` | 已通过 daily synthesis、round1 repair、independent reaudit 和 main-agent acceptance；`data_collection_fix_plan.md` 为 6/8 execution artifact、6/11 git solidification，6/11 后续提交保留为队列外风险 |

## 排除日期（Excluded / Current Audit）

| 日期 | day_id | 状态 | 说明 | 证据源 | 后续处理 |
| --- | --- | --- | --- | --- | --- |
| `2026-06-09` | `day_20260609` | excluded | Codex 命中存在，但当前观察主要指向 skill optimization / validation 类工作，不足以纳入 LLM Wiki 历史开发主线 | Codex JSONL、无项目 git commit | 如后续 worker 发现实质项目开发证据，可提出队列修订 |
| `2026-06-10` | `day_20260610` | excluded | Codex 命中偏复验（revalidation）/skill optimization；无项目实质 git commit | Codex JSONL、无项目 git commit | 保持排除，除非原始 transcript 证明与本项目开发主线直接相关 |
| `2026-06-11` | `day_20260611` | excluded | current-audit：本轮审计筹备；不得混入历史开发线路。另有 v4 Obsidian 配置 mtime 噪声 | 当前 Codex session、`loops/v4.../.obsidian/*` mtime、无项目 git commit | 只在 inventory/read log 记录，不进入日梳理正文 |
