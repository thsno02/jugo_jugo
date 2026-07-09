---
id: digital-landscape-knowledge-graph
title: 数字山水知识图谱
status: accepted
card_type: product-feature
tags:
- knowledge-graph
- visualization
- offline
- chinese-aesthetics
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-sdyckjq-llm-wiki-skill
evidence_basis: code_implementation
justification: ../justification/digital-landscape-knowledge-graph.md
canonical_concept: digital-landscape-knowledge-graph
aliases:
- 数字山水知识图谱
- 数字山水图谱
- digital landscape knowledge graph
- 东方编辑部
- 国风知识图谱
summary: llm-wiki 的交互式知识图谱产物：自包含 HTML 文件，双击即可在浏览器中离线浏览，不依赖服务器。三栏国风布局、山水底图、可拖拽缩放画布、小地图定位。节点按地名/索引签条/朱砂批注视觉分层。左侧社区聚类、搜索、学习队列联动；右侧摘要与正文。首屏推荐预览，点击后进入阅读态。是知识编译产物的可视化呈现形式。
related:
- knowledge-compilation-paradigm
- confidence-level-annotation
---

llm-wiki 的数字山水知识图谱是知识编译产物的交互式可视化呈现，采用东方美学设计语言。[^src-1]

技术形态为自包含 HTML 文件，双击即可在浏览器中探索，全部离线运行，不依赖服务器。[^src-1] 布局为三栏国风结构，含山水底图、可拖拽缩放画布和小地图定位。[^src-2]

视觉设计上，节点按地名、索引签条、朱砂批注进行分层。首次打开只显示推荐预览，点击后才进入阅读态。[^src-3]

阅读交互方面，左侧提供社区聚类、聚焦、搜索、学习队列、推荐起点保持联动；搜索跟随当前可见范围，收藏和学习笔记按 wiki 本地隔离。[^src-4] [^card-1]

[^src-1]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "效果预览" -- "东方编辑部 × 数字山水风交互式知识图谱 — 双击 HTML 文件即可在浏览器中探索...全部离线运行，不依赖服务器"
[^src-2]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "核心亮点" -- "自包含 HTML，双击即可浏览；三栏国风布局、山水底图、可拖拽缩放画布、小地图定位"
[^src-3]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "核心亮点" -- "节点按地名、索引签条、朱砂批注分层；首次打开只显示推荐预览，点击后才进入阅读态"
[^src-4]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "核心亮点" -- "左侧社区、聚焦、搜索、学习队列、推荐起点保持联动；搜索跟随当前可见范围"
[^card-1]: knowledge-compilation-paradigm -- 图谱是编译产物的可视化呈现
