---
id: nvk-llm-wiki-parallel-multi-agent-research
title: nvk/llm-wiki 的并行多 agent 研究流程——5/8/10 个 agent + 多轮 gap-driven
status: accepted
card_type: mechanism
tags: [#llm-wiki, #nvk, #multi-agent, #research, #thesis-mode]
created_time: 2026-05-26T11:26:00+08:00
edited_time: 2026-05-28T11:56:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
provenance_card: ../provenance/nvk-llm-wiki-parallel-multi-agent-research.md
aliases: ["wiki:research workflow", "thesis-driven research"]
related: [nvk-llm-wiki-hub-and-topic-wikis, nvk-llm-wiki-audit-and-librarian, file-outputs-back-as-compounding-loop, llm-knowledge-base-five-stage-workflow, llm-wiki-karpathy-runtime-vs-agent-split]
---

`/wiki:research` 是 nvk/llm-wiki 工具的核心命令——它把"Karpathy LLM Wiki 的 ingest 阶段"展开成一个可调参的、并行多 agent 的、由 gap 驱动多轮的研究流程。它的设计点是同时压住"搜不够"和"过度浏览"两个失败模式。

**单轮基本流程（四阶段）**[^src1]：

1. **Ask / Pick topic**：自动判断输入是"问题"还是"topic 名"；
2. **Parallel search**：默认 5 个 agent，`--deep` 提到 8，`--retardmax` 提到 10；每个 agent 跑 2–3 个 web 搜索，全文抓取，质量打分 1–5；
3. **Ingest + Compile**：top 源进 `raw/`（immutable），编译为 `wiki/concepts/`、`wiki/topics/`、`wiki/references/` 下的文章，加 cross-reference、confidence score、bidirectional link；
4. **Gap report**：每轮结束输出"已覆盖 / 仍缺失 / 建议补"[^src3]，2+ gap 时提示并行追研。

**几种关键模式：**

- `--min-time <duration>`（如 `1h` / `2h`）：在时间窗口内多轮研究，每轮针对上一轮的 gap 深挖；
- `--plan`：先把宏 topic 分解成多个独立 *path*（如 "mechanisms / clinical evidence / devices / criticisms"），每个 path 跑自己的 5-agent swarm；ingest 并行，最后**统一一次 compile** 看到所有源以做跨 path 合成；
- `--new-topic`：研究和创建 topic-wiki 一气呵成；
- `--mode thesis "<claim>"`：thesis-driven 研究——agent 被分到 *supporting / opposing / mechanistic / meta-review / adjacent*，输出 *verdict* （supported / partially / contradicted / insufficient / mixed），并在 round 2 *focuses harder on the weaker side*，对抗确认偏差[^src2]；
- `--retardmax`：10-agent、跳过 plan、最广撒网、aggressive ingest、稍后再 lint——"act first, think later"[^src4]。

**为什么把它结构成"agent 群 + gap 报告"：**

- 一个 agent 串行做完搜索 + 写作 + 自评，会陷入"已知偏差"循环：第一轮搜到的文献会强约束后面的搜索词；
- 多 agent **从不同角度并行启动**（学术 / 技术 / 应用 / 新闻 / 反方），把 confirmation bias 摊平到 swarm 级；
- gap report 不是产物的修饰，而是**下一轮研究的目标函数**——这是 LLM Wiki 从"一次性 ingest" 升级成"长期增长"[^v3-1]的循环不变量；
- 多轮 vs 单轮：单轮适合快速摸底，`--min-time 2h` 适合主题研究/学习，`--plan` 适合大题分解，`thesis` 适合判断真伪。

**与 fuzzy router 的衔接：**

直接 `/wiki research <topic>` 也行——fuzzy router 会分流到 `wiki:research`、`wiki:query`、`wiki:ingest` 等子命令；同样可以用 `/wiki add https://...`、`/wiki what do we know about CRISPR?`。这把多 agent 研究包在最浅一层 UX 后面。

**边界与误用：**

- "5 agent / 8 agent" 的并行依赖底层平台（Claude Code、Codex、OpenCode、AGENTS.md）能支撑并行 agent 调用——本地小模型 + AGENTS.md 不能享受全部加速；
- `--retardmax` 显式是 "act first, think later"，不应被用作严肃文献调研的默认模式；
- thesis mode 的 "skip sources that don't relate to the claim's variables" 会**裁掉跨域类比和反例**，研究目的若是 exploratory，应该用 plan + min-time 而不是 thesis。

## References

- `nvk/llm-wiki` 主站，Commands 与 How it works 部分：`data/raw/webpage/llm-wiki-net/text.txt`，研究流程行 122–137；`/wiki:research` 命令选项行 213–217；Research workflow 节行 276–296；`--plan` 行 350–366；thesis 行 471–478；retardmax 行 466–470。

## Footnotes

- 命令行原文（行 214）：
  > "/wiki:research <topic> 5 parallel agents. --plan (multi-path), --deep (8), --retardmax (10), --new-topic , --min-time 1h ."
- thesis 模式（行 473–478）：
  > "Agents are split across supporting , opposing , mechanistic , meta/review , and adjacent — balanced by design."
  > "Sources that don't relate to the claim's variables are skipped, which keeps the wiki tight. Output is a verdict : supported, partially supported, contradicted, insufficient evidence, or mixed."
  > "With --min-time , round two focuses harder on the weaker side of the evidence — counter-weight against confirmation bias."
- gap report 范例（行 295）：
  > "### Close gaps? 1. Dose-response curves for wavelength specificity 2. Long-term safety data for daily exposure 3. Device comparison ..."
- retardmax 哲学（行 468–470）：
  > "A research mode inspired by Elisha Long's retardmaxxing philosophy — act first, think later. Ten parallel agents, skip planning, cast the widest net, ingest aggressively, compile fast, lint later."
