---
id: nvk-llm-wiki-audit-and-librarian
title: nvk/llm-wiki 的 audit + librarian——把"信任评估"做成可重复 workflow
status: accepted
card_type: operational_rule
tags: [#llm-wiki, #nvk, #audit, #librarian, #provenance, #staleness]
created_time: 2026-05-26T11:27:00+08:00
edited_time: 2026-05-28T11:52:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
provenance_card: ../provenance/nvk-llm-wiki-audit-and-librarian.md
aliases: ["wiki:audit workflow", "wiki:librarian workflow"]
related: [enterprise-llm-wiki-drift-detection-loop]
---

nvk/llm-wiki 把"LLM 写出来的东西能不能信"拆成两个互补的命令：`/wiki:librarian` 做内容打分，`/wiki:audit` 做证据链与可信度的反向追溯。这两件事单独都不新鲜，把它们做成**可重复的 workflow**、并把审计触发的"补研究"也包进去，是这套工具值得借鉴的地方。

**`/wiki:librarian`——文章级 staleness + quality 打分**[^src1]：

- 两层扫描：第一层只读 frontmatter / metadata 做快速判断，flagged 的文章再做"deep content read"；
- 输出"machine-readable JSON + human-readable report"，便于自动化也便于人审；
- 有 checkpoint recovery——对大 wiki 跑长 librarian 不怕中断；
- `--article <path>` 可针对单篇做。

**`/wiki:audit`——回答"这条输出能信吗"**[^src2]：

- 复用 librarian 的 pass，但把范围从"文章质量"扩成"输出可信度"；
- 跨三层追溯：`raw/` / `wiki/` / `output/`——一份 report 是从哪些文章合成的，那些文章又依赖哪些 raw 源；
- detect drift：raw 改了 / 文章后写 / 输出尚未更新 → 暴露错位；
- inspect provenance：每个声明能回链到 raw 行吗？
- 若本地证据不足 → **触发 fresh research**（不是 hold-the-line，而是带着 audit gap 自动跑一轮研究补回来）；
- 通过 `--artifact <path>` 可锁定某一份 output 做 audit，`--project <name>` 可锁定某个 project 的所有 output。

**为什么把"补研究"做进 audit 是关键设计：**

- 传统 audit / lint 工具只标"红 / 黄 / 绿"，把修复留给人；
- LLM Wiki 的特殊之处是 LLM 既是写者也是审者，所以"audit 暴露 gap → 启动 `/wiki:research` 子流程 → 补到 raw → 文章重新合成"可以是一个无人值守闭环；
- 把这个闭环包在一条命令里，让"trust check"变成日常操作，而不是项目末期才做的批审。

**与"git 仓库的 CI"类比：**

- `librarian` ≈ unit tests（针对单页文章的健康）；
- `audit` ≈ end-to-end / integration tests（从 raw 到 output 的完整链路）；
- `lint --fix` ≈ format check（断链、缺索引、archive registry 漂移；`--fix` 自动修可修的，`--deep` 额外做事实联网核验）[^src3]；
- `retract` ≈ 撤销 commit + 清理下游引用[^src4]。

**操作规则（可复用到自建 LLM Wiki）：**

- 在每次 ingest 或 compile 之后跑一次 `librarian`，把分数写进文章 frontmatter（便于下次"快速 metadata 扫描"复用）；
- 在每次生成 *output*（report / slides / plan）之前跑一次 `audit --artifact` 校验它依赖的所有 wiki 文章仍然 fresh；
- 把"audit 触发 fresh research"的预算上限设定好（否则它能跑到外网耗 token 没尽头）；
- `lint --fix` 适合在 CI 里自动跑；`audit` 涉及外网 fetch 适合手动触发[^v3-1]。

## Footnotes

[^src1]: `data/raw/webpage/llm-wiki-net/text.txt` 行 52-54 — "Score every article for staleness and quality. Two-tier scan: fast metadata check, then deep content read for flagged articles. Checkpoint recovery. Machine-readable JSON + human-readable report."
[^src2]: 同文件 行 56-58 — "Answer the broader trust question. Reuse the librarian pass, trace outputs across raw/ , wiki/ , and output/ , detect drift, inspect provenance, and do fresh research when local evidence is not enough."
[^src3]: 同文件 行 228 — "/wiki:lint Health checks. --fix auto-repairs. --deep web-verifies facts."
[^src4]: 同文件 行 230 — "/wiki:retract Remove a source and clean up downstream references."
[^v3-1]: [enterprise-llm-wiki-drift-detection-loop](enterprise-llm-wiki-drift-detection-loop.md) — 企业版的连续后台 drift detection，与 nvk audit 的手动触发是同主题不同执行模式。
