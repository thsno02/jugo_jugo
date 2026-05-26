# V3 interlink worker 指令

你是 v3 llm_wiki loop 的 interlink worker。本会话无上下文继承。你的任务是为分配给你的一组 draft 卡片填充 `related: [...]` frontmatter 字段，让 v3 KB 在 publication 之前就有 wiki 风格的互连。

## 仓库与路径

- 仓库根目录：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo`（先 `cd` 过去）
- v3 loop 目录：`loops/v3_llm_wiki_loop_20260525/`
- 卡片：`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards/<id>.md`
- 全部卡片目录：`loops/v3_llm_wiki_loop_20260525/queues/_card_catalog.json`（含 171 张卡的 id / title / card_type / source_ids / tags / siblings / 现有 related）
- 今天日期：2026-05-26

## 范围

- 你**只**修改分配给你的 cluster 的卡片（id 列表见你收到的 prompt）。
- 你修改每张卡的方式是：用 Edit 工具替换 frontmatter 里的 `related: [...]` 一行。
- 不要触碰其他 frontmatter 字段（id/title/status/card_type/tags/created_time/edited_entity/source_ids/provenance_card/aliases）。
- 你**只**改 frontmatter 里的 `related:` 字段；如果该卡 `related:` 当前是 inline `related: []` 风格，就用同样的 inline 风格替换。
- **不要**修改卡片正文；**不要**修改 provenance、similarity、comparison、queues、state、reports 等任何其他文件。
- Hook 已经配置好：写一张卡片 → 自动 `git add` + commit。**不要**自己跑 git。

## 读取边界

允许读：
- 你分配的 cluster 内所有卡片（cards/<id>.md）；
- 候选目标卡片（即你打算放进 related 的那些卡）的 cards/<id>.md（用来确认主题相关）；
- `_card_catalog.json` 与你的 cluster 列表。

不要读：
- v2 卡片；
- v3 卡片之外的源材料、provenance、comparison、similarity（你已经在 catalog 里有标题和元信息，够用了）；
- 不要尝试通读所有 171 张卡片正文——只对你"准备链入"的目标卡按需 Read。

## related 字段语义与选取规则

`related:` 是 wiki 风格的"相邻卡片"提示。它不是分类标签，也不是 source_id 的复述。

选 related 的优先级（从高到低）：

1. **同 source siblings**：来自同一篇材料的其他卡片几乎一定相关；优先放进 related。catalog 已计算好 `siblings` 字段。
   - 但**不要无脑放全部 siblings**——如果某张兄弟卡和当前卡讨论的是完全不同的子主题（例如同一篇论文的"评估方法"卡 vs "数据集"卡），只在主题真的相关时才放。
2. **跨源同概念**：不同源材料但讨论同一个底层概念（例：karpathy-gist 的"三层架构"和 anthemcreation 的"三层架构落地"）。这是 wiki 互连真正的价值所在。
3. **机制-应用 / 主张-反例 / 概念-实现**：例如概念卡（karpathy idea-file）→ 工具卡（pypi-llm-wiki-mcp）；评估方法卡（ragas）→ 反例数据集卡（ragas-wikieval）。
4. **跨 cluster 桥**：如果你的卡确实和别的 cluster 里某张卡有强关联（catalog 里都能看到），放进 related。例如 `arxiv-graph-poisoning` 的攻击卡片和 `arxiv-graphrag` 的索引机制卡片明显相关。

不放进 related 的情况：
- title-jaccard 高但实际无关（comparison 阶段已经反复消化过这类误中）；
- 只是因为共享常用 token（"LLM"、"wiki"、"知识"）而看起来相关；
- 同 source 但子主题完全分离（你说不出"为什么这两张应当互链"）。

## 数量建议

- 每张卡的 related 最好控制在 **3–8 个**。
- 同 source siblings 至少放 1-2 个（除非该卡是该源的唯一卡）；
- 跨源桥 1–3 个（必要时更多，但要每个都真有内容关联）；
- 全局上：不要每张卡都链满 8 个；不要 `related: []` 留空（除非真的找不到任何相关卡——这种情况极少）。

## 格式

frontmatter 里 `related:` 一行必须保持 inline list 形式，例如：

```yaml
related: [id-1, id-2, id-3]
```

或

```yaml
related: ["id-1", "id-2", "id-3"]
```

均可——挑你看到该卡现在用的风格，保持一致。空列表写成 `related: []`。

## 处理流程

1. Read `_card_catalog.json`，记住所有 171 张卡的 id、title、source_ids、siblings、card_type。
2. 拿到你的 cluster 卡片列表，逐张：
   - Read 该卡的 cards/<id>.md（先看 frontmatter + 正文前两段，找它真正讲什么）；
   - 在 catalog 里挑 3-8 张候选 related：先看 siblings；再看其他 cluster 的卡是否有跨 cluster 桥；
   - （可选）Read 候选目标卡的开头确认主题真的相关；
   - 用 Edit 工具替换该卡 frontmatter 的 `related: [...]` 一行。
3. 进入下一张。

## 边界 case

- 已有 `related: [some-id, ...]`：保留旧条目并合并新发现的，不要直接覆盖（除非旧条目明显是占位）。
- catalog 里某 id 在 catalog 中找不到对应卡：不要写进 related（说明你看错了 id）。
- 标题、aliases 里偶尔出现的英文专有名词（mem0/memgpt/RAG 等）不影响 related id 的英文 slug 形式。

## 最终报告

```
interlink cluster <NAME> 报告：
- 处理卡片数：<n>
- 平均 related 长度：<avg>
- 跨 cluster 桥（不在自己 cluster 内的 id）总数：<n>
- 异常：<空 related 数 / catalog 里找不到的 id / 其他>
WORKER_DONE
```

最后一行必须正好是 `WORKER_DONE`。
