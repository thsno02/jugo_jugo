---
id: obsidian-tooling
title: Obsidian 工具生态
status: accepted
card_type: operational_rule
tags: [llm-wiki, obsidian, tooling, tips]
created_time: 2026-06-05T00:00:00+08:00
edited_time: 2026-06-05T00:00:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/obsidian-tooling.md
canonical_concept: obsidian-tooling
aliases: [Obsidian 工具, Obsidian ecosystem, Web Clipper, graph view, Marp, Dataview]
summary: >-
  obsidian-tooling（Obsidian 工具 / Obsidian ecosystem / Web Clipper / graph view / Marp / Dataview）
  是 LLM Wiki 实践中的 Obsidian 工具生态：Web Clipper 采集资料、graph view 可视化连接、
  Marp 生成幻灯片、Dataview 查询 frontmatter，Obsidian 作为「IDE」供用户浏览 wiki
related: []
---

在 LLM Wiki 的实践中，作者使用 **Obsidian** 作为 wiki 的浏览器和「IDE」[^card-1]。材料推荐的 Obsidian 工具链包括：

- **Obsidian Web Clipper**——浏览器扩展，将网页文章转为 markdown，便于快速将资料加入 raw 集合[^src-1]
- **Graph view**——可视化 wiki 的连接结构，显示哪些页面是 hub、哪些是孤立页面，是「看到 wiki 形态的最佳方式」[^src-2]
- **Marp**——基于 markdown 的幻灯片格式，Obsidian 有插件支持，可直接从 wiki 内容生成演示文稿[^src-3]
- **Dataview**——对 wiki 页面 frontmatter 执行查询的插件，如果 LLM 为页面添加 YAML frontmatter（标签、日期、资料计数），Dataview 可生成动态表格和列表[^src-4]
- **本地图片下载**——可设置快捷键将文章中的图片下载到本地目录，避免 URL 失效[^src-5]

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Tips and tricks" P1 -- "Obsidian Web Clipper is a browser extension that converts web articles to markdown"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Tips and tricks" P3 -- "Obsidian's graph view is the best way to see the shape of your wiki"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Tips and tricks" P4 -- "Marp is a markdown-based slide deck format. Obsidian has a plugin for it."
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Tips and tricks" P5 -- "Dataview is an Obsidian plugin that runs queries over page frontmatter"
[^src-5]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Tips and tricks" P2 -- "Download images locally... it lets the LLM view and reference images directly instead of relying on URLs that may break"
[^card-1]: [人机角色分工](human-llm-role-division.md) -- 「Obsidian 是 IDE，LLM 是程序员」的类比来自该卡
