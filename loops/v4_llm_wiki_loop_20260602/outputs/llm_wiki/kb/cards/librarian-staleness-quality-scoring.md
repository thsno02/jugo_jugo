---
id: librarian-staleness-quality-scoring
title: Librarian 陈旧度与质量评分机制
status: accepted
card_type: mechanism
tags: [llm-wiki, librarian, staleness, quality, maintenance, tiered-scan]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
justification: ../justification/librarian-staleness-quality-scoring.md
canonical_concept: librarian-staleness-quality-scoring
aliases: [Librarian 评分, librarian scoring, 陈旧度评分, wiki quality scoring]
summary: >-
  librarian-staleness-quality-scoring（Librarian 评分 / librarian scoring / 陈旧度评分 / wiki quality scoring）
  是 llm-wiki 的文章维护评分系统：陈旧度和质量各 0-100 分（四维度各 25 分），
  采用两级扫描（Tier 1 仅读元数据、Tier 2 升级读全文），带检查点崩溃恢复
related: [parallel-multi-agent-research, archive-lifecycle, continuous-drift-detection]
---

`/wiki:librarian` 是 llm-wiki 的聚焦维护工具，仅作用于 `wiki/` 层的编译文章。它通过两个评分维度识别需要关注的文章[^src-1]：

**陈旧度评分（staleness score，0-100）**由四个等权维度组成，每项 25 分[^src-2]：
- 来源新鲜度（source freshness）
- 验证近期度（verification recency）
- 编译近期度（compilation recency）
- 来源链完整性（source chain integrity）

衰减曲线按文章的 `volatility` 分级（hot/warm/cold）缩放——热门文章衰减更快[^src-3]。低于 `freshness_threshold`（默认 70）的文章被标记为需要关注[^src-4]。

**质量评分（quality score，0-100）**同样四维度各 25 分[^src-5]：
- 来源多样性（source diversity）
- 内容深度（content depth）
- 交叉引用密度（cross-reference density）
- 摘要质量（summary quality）

**两级扫描（tiered scan）**是性能优化的关键设计[^src-6]：
- **Tier 1**（所有文章）：仅读取 YAML frontmatter，计算来源数量、检查 See Also 存在性、估算文件大小，产出粗粒度评分
- **Tier 2**（升级条件触发）：读取全文正文，精细评估连贯性和实用性——仅在以下条件之一满足时升级：陈旧度低于阈值、volatility 为 hot、Tier 1 深度代理值极低（疑似 stub）

这避免了在大型 wiki 上读取每篇文章全文的开销[^src-7]。

**检查点崩溃恢复**：每篇文章扫描完成后写入 `checkpoint.json`（先写 `.checkpoint.tmp` 再 rename 保证原子性）[^src-8]。中断后重启时自动检测检查点，跳过已完成文章继续扫描[^src-9]。

扫描完成后产出两个制品：`.librarian/scan-results.json`（结构化数据）和 `.librarian/REPORT.md`（人类可读报告），然后删除检查点文件[^src-10]。

Librarian 与 audit 的分工边界明确：librarian 只关注 wiki 文章层的健康状况，更广泛的信任审计（包括 output 依赖链、出处追踪、新鲜研究验证）属于 `/wiki:audit`[^src-11]。这与通用知识系统中的漂移检测机制共享「持续监控 + 按严重度升级」的模式[^card-1]。

## Footnotes

[^card-1]: [持续漂移检测](continuous-drift-detection.md) -- Librarian 的周期性陈旧度扫描是持续漂移检测在 wiki 维护中的具体实现

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/librarian.md -- "Keep the active wiki article layer in check: staleness, quality, accuracy, and coherence."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: AGENTS.md -- "Staleness scoring (0-100): four dimensions at 25 points each — source freshness, verification recency, compilation recency, source chain integrity."
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: AGENTS.md -- "Decay curves scaled by article volatility tier (hot/warm/cold)."
[^src-4]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/librarian.md -- "Read config.md for freshness_threshold (default: 70)."
[^src-5]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: AGENTS.md -- "Quality scoring (0-100): four dimensions at 25 points each — source diversity, content depth, cross-reference density, summary quality."
[^src-6]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/librarian.md -- "Tier 1 (all articles, metadata-only)... Tier 2 escalation — read the full article body if ANY of these are true"
[^src-7]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/librarian.md -- "Non-escalated articles: coherence and utility default to 3 (adequate). This avoids reading every article body on large wikis."
[^src-8]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/librarian.md -- "Write result to checkpoint.json (atomic: write .checkpoint.tmp, rename)."
[^src-9]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/librarian.md -- "If exists and --resume or no explicit flag: read it, report how many articles are already done, continue from where it left off."
[^src-10]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/librarian.md -- "Compile all results from checkpoint into scan-results.json... Generate REPORT.md from the JSON... Delete checkpoint.json (scan complete)"
[^src-11]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/librarian.md -- "/wiki:librarian is the focused wiki-maintenance tool. It reviews the wiki/ layer only. If the user wants a broader trust inspection across outputs, provenance, and fresh research, direct them to /wiki:audit."
