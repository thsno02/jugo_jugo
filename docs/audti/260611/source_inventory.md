# 证据目录（Source Inventory）

本文件汇总本轮只读盘点得到的证据源。可信度（confidence）表示该来源可作为历史开发事实的直接程度，不表示内容已经完成逐条审计。

## 总览（Overview）

| evidence source | source path | 类型（type） | 覆盖日期（coverage） | 可信度（confidence） | 用途（use） | 缺口（gap） |
| --- | --- | --- | --- | --- | --- | --- |
| Claude project transcripts | `~/.claude/projects/-Users-lw-Desktop-GitHub-llm-wiki-jugo-jugo/**/*.jsonl` | transcript/log | `2026-05-25` 到 `2026-06-07` | 高（high） | 还原 Claude 主线程与 subagent 执行、用户纠偏、工作边界、产出交付 | 需要后续 worker 逐日读取正文；当前仅做统计与代表路径盘点 |
| Claude memory | `~/.claude/projects/-Users-lw-Desktop-GitHub-llm-wiki-jugo-jugo/memory/*.md` | transcript/artifact | mtime 覆盖 `2026-05-25` 到 `2026-06-05` | 中高（medium-high） | 识别稳定用户偏好与工作约束，如中文主语言、全文读取、loop 独立性 | memory 是提炼层，不可单独证明具体开发事件 |
| Codex matching sessions | `~/.codex/sessions/**`、`~/.codex/archived_sessions/**` 中匹配项目路径或项目名的 JSONL | transcript/log | `2026-05-09` 到 `2026-06-11`；项目候选主段为 `2026-05-21` 到 `2026-06-08` | 中（medium） | 补齐 Claude 前后和 Codex 侧 loop/worker/验证记录 | 命中包含 cwd/base instruction/技能优化等噪声，`2026-06-09` 到 `2026-06-11` 需排除或专项确认 |
| user-insights | `user-insights/**` | artifact | `2026-05-25`、`2026-05-27` | 中（medium） | 作为用户输入与设计决策的二级索引（secondary index） | 不是完整 transcript；metadata 明示部分覆盖（partial/mixed） |
| loop capsules | `loops/v0*`、`loops/v1*`、`loops/v2*`、`loops/v3*`、`loops/v4*` | artifact/log | `2026-05-24` 到 `2026-06-08`，局部 mtime 到 `2026-06-11` | 高（high） | 还原 loop 版本、产物目录、状态、报告、审计和修复 artifact | v4 目录存在 `2026-06-11` Obsidian 配置 mtime 噪声；需与 git/transcript 区分 |
| git history | `git log --date=iso --name-status -- .` | git | `2026-05-21` 到 `2026-06-08` | 高（high） | 锚定实质文件变更、提交日期、主题和最后实质开发记录 | 未覆盖未提交工作；commit 粒度不能替代 transcript 意图 |
| docs secondary | `docs/**` | artifact | 已有 `docs/RESEARCH_PROTOCOL.md`、`docs/llm_wiki_practice_reframe/**`、未跟踪 `docs/present_doc/**` | 低到中（low-medium） | 作为表述、演示和后验总结对照 | 不可作为唯一事实源；`docs/present_doc/` 当前未跟踪，只记录不处理 |

## 日期覆盖矩阵（Date Coverage Matrix）

| 日期 | Claude JSONL | Codex JSONL | loops | git | user-insights | 初步判断 |
| --- | --- | --- | --- | --- | --- | --- |
| `2026-05-21` | 无 | 有 | v1 mtime/早期仓库材料 | 有，6 commits | 无 | 可审计起点；source discovery 和 acquisition framework |
| `2026-05-22` | 无 | 有 | 无显式 loop 版本 | 有，4 commits | 无 | 原始材料与 loop logs 扩展 |
| `2026-05-23` | 无 | 有，archived Codex | 无明确 git | 无 | 无 | 需要 transcript 复核的间隙日 |
| `2026-05-24` | 无 | 有，大量 Codex | v0/v1 | 无 | 无 | v0/v1 loop capsule 形成 |
| `2026-05-25` | 有 | 有 | v2/v3 | 有，129 commits | 有 | v2 archived、v3 active、bootstrap insights |
| `2026-05-26` | 有 | 有 | v3 | 有，529 commits | 间接 | v3 draft/interlink 大规模推进 |
| `2026-05-27` | 有 | 有 | v3 | 有，174 commits | 有 | v3 adoption 与用户纠偏记录 |
| `2026-05-28` | 有 | 有少量 | v3 | 有，672 commits | 无 | v3 adoption wave 与 provenance |
| `2026-05-29` | 有 | 无明确主证据 | v3 | 有，9 commits | Claude memory | v3 capsule 收束/上传/登记 |
| `2026-05-30` | 无 | 无明确主证据 | 无明确 mtime | 无 | 无 | 候选缺口日 |
| `2026-05-31` | 无 | 无明确主证据 | 无明确 mtime | 无 | 无 | 候选缺口日 |
| `2026-06-01` | 有少量 | 无明确主证据 | 无明确 mtime | 无 | 无 | Claude 侧少量记录，需复核主题 |
| `2026-06-02` | 有 | 有 | v4 loop id 指向 `20260602` | 无 | 无 | v4 设计/启动候选，需 transcript 锚定 |
| `2026-06-03` | 无 | 有 archived Codex | 无明确 git | 无 | 无 | v4 前置/过渡候选，需 transcript 复核 |
| `2026-06-04` | 有 | 有 | v4 | 有，6 commits | 无 | v4 初始化与 Phase 1-2 |
| `2026-06-05` | 有 | 有少量 | v3/v4 | 有，4 commits | Claude memory | v4 governance 和材料提取 |
| `2026-06-06` | 无 | 无明确主证据 | 无明确 git | 无 | 无 | 候选缺口日 |
| `2026-06-07` | 有 | 无明确主证据 | v4 | 有，2 commits | 无 | v4 全量审计与修复 |
| `2026-06-08` | 无 | 有 | v4 | 有，3 commits | 无 | 最后实质开发记录：v4 deep audit / pipeline repair |
| `2026-06-09` | 无 | 有 | 无实质 git | 无 | 无 | excluded：Codex 命中偏 skill optimization/validation，不入历史日梳理 |
| `2026-06-10` | 无 | 有 | 无实质 git | 无 | 无 | excluded：Codex 命中偏复验/skill optimization，不入历史日梳理 |
| `2026-06-11` | 无 | 有 | v4 Obsidian mtime 噪声；当前审计 | 无 | 无 | current-audit：本轮审计筹备，不入历史日梳理 |

## 关键统计（Inventory Stats）

- Claude JSONL：384 个文件，33135 行，timestamp 覆盖 `2026-05-25` 到 `2026-06-07`。
- Claude memory：12 个 Markdown 文件，mtime 覆盖 `2026-05-25` 到 `2026-06-05`。
- Codex 匹配 JSONL：184 个文件，60794 行，timestamp 覆盖 `2026-05-09` 到 `2026-06-11`；其中需要人工过滤 cwd/base instruction 噪声。
- loop capsule：v0 154 文件，v1 601 文件，v2 701 文件，v3 1145 文件，v4 659 文件。
- git history：实质提交日期覆盖 `2026-05-21` 到 `2026-06-08`；`2026-06-09` 之后当前未见项目实质 commit。

## 代表路径（Representative Paths）

- Claude 主路径：`~/.claude/projects/-Users-lw-Desktop-GitHub-llm-wiki-jugo-jugo/4379b2d9-db20-4573-9450-751bb398208a.jsonl`
- Claude v4 代表路径：`~/.claude/projects/-Users-lw-Desktop-GitHub-llm-wiki-jugo-jugo/2863f0e0-b891-41b4-923b-4b8c01ba8719.jsonl`
- Claude memory：`~/.claude/projects/-Users-lw-Desktop-GitHub-llm-wiki-jugo-jugo/memory/MEMORY.md`
- Codex 早期 archive：`~/.codex/archived_sessions/rollout-2026-05-18T17-41-41-019e3a76-7129-73f2-944f-4397ae96abac.jsonl`
- Codex 2026-06-09 命中：`~/.codex/sessions/2026/06/09/rollout-2026-06-09T01-18-14-019ea83d-f87a-7db0-aa4f-2ff3d4541abe.jsonl`
- user-insights index：`user-insights/index.md`
- v0：`loops/v0_meta_kb_initialization_demo_20260524/`
- v1：`loops/v1_topic_hub_skeleton_20260524/`
- v2：`loops/v2_llm_wiki_loop_20260525/`
- v3：`loops/v3_llm_wiki_loop_20260525/`
- v4：`loops/v4_llm_wiki_loop_20260602/`

