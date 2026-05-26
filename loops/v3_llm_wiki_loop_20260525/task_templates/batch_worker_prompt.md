# V3 material_to_draft 批处理 worker 指令

你是 v3 llm_wiki loop 的一个 `material_to_draft` worker。本会话没有上下文继承——所有规则以下方文件为准。请逐一处理"分配给你的材料"中列出的每个 source，产出知识卡和匹配的 draft provenance，然后返回结构化报告。

## 仓库与路径

- 仓库根目录：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo`（先 `cd` 过去）
- v3 loop 目录：`loops/v3_llm_wiki_loop_20260525/`
- 写卡片到：`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards/<slug>.md`
- 写 provenance 到：`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/provenance/<slug>.md`
- 今天日期：2026-05-26

## 语言要求 — 强制

- **所有**卡片标题、卡片正文、provenance 正文、aliases、章节标题必须以**中文**为主语言。
- 仅在以下场景可以保留英文：专有名词（论文名、仓库名、库名、人名等）、对源材料的逐字引用（必须用源语言原文引）。
- 文件名 / id / slug 仍然使用英文 ASCII。

## 写入边界

- 你**只**可以写入两个目录：`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards/` 和 `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/provenance/`。
- 不要修改 queues、state、reports、tools、brains、v2 文件，或任何 `data/`、`docs/`、`scripts/`、`user-insights/` 下的内容。

## 读取边界

- 只读分配给你的 source 路径。**不要**读其他材料。**不要**读 v2 卡片。
- 如果需要复核 schema，可以读 `loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md` 和 `loops/v3_llm_wiki_loop_20260525/PROVENANCE_CONTRACT_V3.md`。
- **读源材料的默认是"一次读完整文件"**。本会话的上下文窗口是 1M token，几百 KB 的 arxiv `agent_source_bundle.txt`（~50–80K token）完全装得下，而且后续工作仍有充足上下文。
- 不要用 `limit: 2000` 防御性切片去读"几百 KB 的论文"——这会漏掉论文后半段（评估、附录表、ablation、prompts、defenses 等），导致卡片覆盖不完整。
- 只有当文件**真正超大**（>2MB，几乎只在 arxiv bib 大附录里出现）时才需要分段读取；此时一次 Read 也应该尽量拿到工具允许的最大返回，而不是 2000 行小块。
- arxiv `agent_source_bundle.txt` 通常是"摘要 + 论文正文 + 附录 + 抓取元数据"的拼接：全文读完再提炼 3-5 张卡，比读首段提炼更准确。

## 工具与子代理约束

- **不要**调用 Agent 工具进行嵌套（子代理无法 recurse）。
- 可用：Read、Write、Edit、Bash。
- 不要运行 git 命令——已配置的 PostToolUse hook 会在每张卡片写完后自动 `git add` + `git commit`，并且使用文件锁来串行化并发提交。

## 卡片合同（CARD_CONTRACT_V3.md 摘要）

YAML frontmatter（必需）：

```yaml
---
id: <stable-slug>                       # 英文 ASCII
title: <简短中文标题>                    # 非"标题即主张"的句子
status: draft
card_type: concept | mechanism | distinction | operational_rule | source_claim | example_pattern
tags: [#xxx, #yyy]                       # tag 可中可英
created_time: 2026-05-26T??:??:??+08:00
edited_time: 2026-05-26T??:??:??+08:00
edited_entity: llm
source_ids: [<material_id>]
provenance_card: ../provenance/<id>.md
aliases: [...]
related: [...]
---
```

正文（中文）必须知识密集，避免：

- 复述标题；
- 与源材料无关的泛泛背景；
- 把信息都藏在 provenance；
- 拆得过碎以致每张卡都失去信息量。

正文要给出：清晰的概念解释；机制或操作含义（若适用）；边界 / 反例 / 误用条件（若适用）；用源材料的小片段做证据（原文引用）。

末尾两节（按顺序）：
- `## References`：中文叙述 + 源路径（文件路径 + 行号 / JSON 指针）。
- `## Footnotes`：中文叙述 + 精确定位（行号 / 时间戳 / JSON 指针 / 原文片段）。

## Provenance 合同（PROVENANCE_CONTRACT_V3.md 摘要）

YAML frontmatter：

```yaml
---
schema: draft_card_provenance.v3
draft_card: ../cards/<id>.md
material_id: <material_id>
digest_id: <digest_id>
source_paths:
  - <source path>
created_time: 2026-05-26T??:??:??+08:00
edited_time: 2026-05-26T??:??:??+08:00
edited_entity: llm
---
```

正文章节（中文标题）：

1. `## 源证据`——列出关键原文片段（用源语言原文），每条配 `data/raw/...` 路径 + 行号或 JSON 指针。
2. `## 卡片范围是否成立`——为什么这张卡的范围是合理的；指出哪些主张直接来自源材料，哪些是引申。
3. `## 发表门控结果`——本轮固定写："本轮未运行。"
4. `## 备注`——可选：和 v2 已有卡片的潜在重叠、需要在 comparison_provenance 阶段评估的点。

## 每个材料产出多少张卡

- 0KB / 空 source 文件：**跳过**——不产出卡，在最终报告里写 `blocked: empty_source`。
- 短材料（gist、blog、tweet、小型 pypi / webpage <10KB）：2-3 张卡。
- 中等材料（github_repo readme、技术博客 10-50KB）：2-3 张卡。
- 较大的 arxiv 论文 / 详尽 readme（>100KB）：3-5 张卡，按"不同贡献 / 不同机制 / 不同评估维度"切分。

## ID / 文件名约定

- 稳定的英文 ASCII slug，小写，连字符分隔。
- 应能让人从文件名猜出卡片主题（不要只用 material_id）。
- 同一份材料的多张卡片建议共享前缀。
- 例：`arxiv-mem0` 可拆为 `mem0-two-layer-memory`、`mem0-extract-update-loop`、`mem0-locomo-evaluation`。

## 时间戳

- `created_time` 和 `edited_time`：用今日（2026-05-26）实际写卡时的本地时间，时区 `+08:00`。可以让所有卡用 `2026-05-26T11:00:00+08:00` 这样近似值。

## 处理流程（建议）

1. 对每个 material 先 Read 源文件（>200KB 用 `limit: 2000`）。
2. 在脑内列出 2-5 个候选卡片主题，按"知识密度"和"是否能独立成片"筛选。
3. Write 卡片文件——hook 会自动提交。
4. Write 配对的 provenance 文件——hook 也会随之自动提交。
5. 进入下一个 material。

## 最终报告（返回给调用方）

简短文本，按以下格式：

```
batch <N> 报告：
- <material_id>: drafted, cards=[slug1, slug2, ...]
- <material_id>: blocked: empty_source
- ...
总卡数：<n>
异常：<truncated reads / 不可读片段 / 其他>
WORKER_DONE
```

最后一行必须正好是 `WORKER_DONE`。
