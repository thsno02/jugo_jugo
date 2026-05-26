---
schema: draft_card_provenance.v3
draft_card: ../cards/llm-knowledge-base-five-stage-workflow.md
material_id: karpathy-x-launch-post
digest_id: digest_karpathy-x-launch-post
source_paths:
  - data/raw/webpage/karpathy-x-launch-post/text.txt
created_time: 2026-05-25T22:05:00+08:00
edited_time: 2026-05-26T09:30:00+08:00
edited_entity: llm
---

## 源证据

- 主要片段：`data/raw/webpage/karpathy-x-launch-post/text.txt`，JSON 指针 `$.tweet.quote.text`。被引用的推文本身使用了清晰的小标题：
  - "Data ingest:"——描述把源文档索引进 `raw/`、把 wiki 编译成 `.md`、摘要、反向链接、概念分类、Obsidian Web Clipper、批量下载图片的快捷键。
  - "IDE:"——描述 Obsidian 作为"读"前端；LLM 写，人几乎不动。
  - "Q&A:"——描述在 ~100 篇 / ~400K 词规模下基于自维护索引的问答；没有单独的 RAG 层。
  - "Output:"——描述把答案渲染成 markdown / Marp 幻灯 / matplotlib 图像，再在 Obsidian 中查看；并把输出归档回 wiki。
  - "Linting:"——描述 LLM health check：发现数据不一致、用 web search 补全缺失数据、提示新文章候选、清理整体完整性。
- 边界片段：同一被引用推文中的 TLDR 段落给出了"几乎不直接编辑 wiki"的不变式（"You rarely ever write or edit the wiki manually, it's the domain of the LLM"）。

## 卡片范围是否成立

这是一张"工作流卡片"，而源材料本身就把工作流呈现成五个带小标题的阶段。卡片正文每个子弹都映射到源材料中一个小标题，因此卡片的范围沿用了源材料自身的分解方式。卡片没有加入源材料未命名的任何阶段。

卡片显式标出了规模限定词（"this ~small scale"）和作者本人指向的下一步方向（合成数据 + 微调），从而保留了源材料的边界，而不是越界主张。

## 发表门控结果

本轮未运行。

## 备注

- 本卡片在主题上和 v2 中关于 LLM Wiki 架构与 ingest 流程的几张卡片有重叠，因此 similarity 阶段预期会把那些卡片列入 top 3。"是 `new_card`、`merge_candidate` 还是 `provenance_delta`"这个判定推后到 comparison provenance 阶段。
