---
report_type: pipeline_gaps
loop: v4_llm_wiki_loop_20260602
date: 2026-06-08
audits_count: 4
topics:
  - scrape_lossiness
  - github_repo_triage
  - citation_eval_cross_links
  - arxiv_text_quality
severity_summary:
  critical: 2    # arxiv text.txt 误用, cross-link 覆盖率仅 25%
  high: 1        # scrape 结构元素丢失 (1261 elements)
  medium: 1      # repo 优先级排序待执行
---

# Pipeline Gaps Report

## Executive Summary

v4 pipeline 存在 4 类系统性缺口：

| # | 缺口 | 严重度 | 量化影响 |
|---|------|--------|---------|
| 1 | Arxiv text.txt 误路由 | CRITICAL | 62/626 footnotes (10%) 仅含摘要深度，7 个源受影响 |
| 2 | Cross-link 缺失 | CRITICAL | 跨家族链接覆盖率 25%（5/~20），14-16 条缺失 |
| 3 | Scrape 结构丢失 | HIGH | 1261 结构元素丢失，92% 源含图片/SVG，57% 含代码块 |
| 4 | Repo 未消化 | MEDIUM | 8 个 Tier-1 repo（2520+ .py）尚未提取为 KB 卡 |

---

## 1. Scrape Lossiness — 网页结构元素丢失

### 发现

- 26 个 webpage 源含 raw.html；HTML→text 转换丢失全部结构
- 结构元素总计：1261（table=34, pre=51, code=530, img=263, figure=13, svg=370）
- 含代码块源：15/26 (57%)；含视觉元素源：24/26 (92%)
- 极端案例：langchain-long-term-memory-docs 压缩比 0.43%（2.6MB→11KB）
- 2 个空壳源（aicritique-enterprise-knowledge 及 dynamic 变体）：HTML 1.4KB，text 13 bytes

### Top-5 结构丢失源

| 源 | 元素数 | 主导类型 | HTML→text |
|----|--------|---------|-----------|
| llm-wiki-net | 256 | code (220) | 64KB→31KB |
| atlan-llm-wiki-vs-rag-dynamic | 163 | img (116) | 248KB→33KB |
| clawhub-llm-wiki-karpathy | 108 | code (86) | 94KB→8KB |
| obsidian-community-plugin | 96 | code (51) | 279KB→24KB |
| langchain-long-term-memory-docs | 79 | svg (52) | 2.6MB→11KB |

### 建议

1. 代码重源（llm-wiki-net, clawhub）：增强提取保留 code block 格式
2. 图片重源（atlan）：验证 alt-text 是否已提取
3. langchain：人工审查，内容大概率为 JS 渲染/SVG 图表
4. 2 个空壳源：重新抓取或标记为 failed scrape

---

## 2. GitHub Repo Triage — 优先级排序

### 发现

- 20 个 repo，合计 1904 .md + 2613 .py
- 分类：8 unique-implementation / 3 paper-companion / 9 fork-of-llm-wiki
- Tier 1（高唯一知识价值）：8 个 repo，含 2520+ .py 实现代码
- Tier 2（与已有 arxiv 论文高度重叠）：3 个 repo
- Tier 3（Karpathy 模式变体）：9 个 repo

### Tier-1 优先消化顺序

| 排名 | Repo | .py | 唯一知识点 |
|------|------|-----|-----------|
| 1 | microsoft-agent-governance-toolkit | 1791 | policy DSL, runtime enforcement, audit schema |
| 2 | microsoft-graphrag | 570 | indexing pipeline, community detection code |
| 3 | nvk-llm-wiki | 0 (722 .md) | thesis research, topic archive, librarian workflow |
| 4 | nashsu-llm-wiki | 0 (desktop app) | 4-signal graph, Louvain, multimodal ingest |
| 5 | vectifyai-openkb | 65 | vectorless PageIndex retrieval |
| 6 | agricidaniel-claude-obsidian | 4 | DragonScale Memory, 11-skill architecture |
| 7 | kytmanov-obsidian-local | 81 | local-first Ollama, review-rejection loop |
| 8 | ngmeyer-librarian-mcp | 0 (Rust) | MCP-native wiki, trigram search, D3 graph |

### 建议

- Tier 1：按排名顺序消化，重点提取实现架构（非 README 概述）
- Tier 2（ragchecker/ares/longmemeval repo）：跳过，arxiv 论文已覆盖
- Tier 3：仅 batch 消化 sdyckjq（中文竞品分析）+ ar9av（agent 兼容矩阵）

---

## 3. Citation Eval Cross-Links — 跨家族链接缺失

### 发现

- 3 个评估家族共 23 张卡：ALCE (10) / RAGChecker (10) / ARES (4)
- 现有跨家族有向链接：5 条（3 对唯一连接）
- 应有跨家族有向链接：~20 条
- **覆盖率：25%，缺失 14-16 条有向链接（10 个概念桥）**

### 最严重缺口

| 优先级 | 缺失链接 | 共享概念 |
|--------|---------|---------|
| T1 | closed-book-citation-paradox <-> rag-generator-self-knowledge | 同一现象：无检索时正确但不可引用 |
| T1 | citation-partial-support-limitation -> claim-level-entailment-evaluation | 问题→解决方案对 |
| T1 | retrieval-as-citation-bottleneck <-> context-utilization-as-performance-key | 均度量 context utilization gap |
| T2 | alce-citation-benchmark <-> ares-rag-evaluation-framework | 旗舰框架卡零链接 |
| T2 | citation-quality-tri-dimension <-> ragchecker-three-tier-metrics | 平行多维设计 |
| T2 | retrieval-as-citation-bottleneck <-> retrieval-improvement-faithfulness-noise-tradeoff | 同一实证现象 |

### 轴向分布

| 轴 | 现有 | 应有 | 缺口 |
|----|------|------|------|
| ALCE <-> RAGChecker | 2 | ~10 | 8 |
| RAGChecker <-> ARES | 2 | ~4 | 2 |
| ALCE <-> ARES | 1 (单向) | ~6 | 5 |

### 建议

- 修复 Tier 1 (3对) + Tier 2 (3对) 即可将覆盖率从 25% 提升至 ~70%
- ALCE→ARES 轴当前零链接，为最急迫修复方向

---

## 4. Arxiv text.txt 误路由 — 摘要深度卡片

### 发现

- 17 个 arxiv 源的 text.txt 均为 arXiv 摘要页爬取（~5KB，207 行）
- agent_source_bundle.txt 为真实论文全文（66KB-46MB，12x-9155x 大）
- 正确路径使用率：507/626 = 81%（agent_source_bundle.txt）
- **误用 text.txt：62 citations / 7 个源，全部仅含 Abstract 深度**

### 受影响源

| 源 | text.txt citations | 有 bundle? | 严重度 |
|----|-------------------|-----------|--------|
| arxiv-graph-poisoning | 15 | Yes | 全部卡片仅摘要深度 |
| arxiv-wicer | 16 | Yes | 几乎全部 |
| arxiv-lightmem | 11 | Yes | 全部卡片仅摘要深度 |
| arxiv-ares | 9 | Yes | 部分 |
| arxiv-ragas | 8 | Yes | 部分 |
| arxiv-longmemeval | 2 | Yes | 轻微 |
| arxiv-memgpt | 1 | Yes | 轻微 |

### 根因

Reader-worker 路由逻辑未强制 agent_source_bundle.txt 优先；部分 worker 读取了同目录下更小的 text.txt。

### 建议

1. 路由修复：强制优先级 agent_source_bundle.txt > source.pdf > text.txt（仅元数据）
2. 重提取：graph-poisoning (15) + lightmem (11) + wicer (16) 三源全部卡片从 bundle 重新提取
3. 防混淆：将 text.txt 重命名为 abs_page.txt 或 metadata.txt

---

## Prioritized Action Items

| # | 动作 | 影响 | 工作量 | 阻塞 |
|---|------|------|--------|------|
| 1 | 修复 reader-worker 路由：arxiv 源强制读 agent_source_bundle.txt | 消除 10% 浅卡问题 | 低 | 无 |
| 2 | 重提取 graph-poisoning / lightmem / wicer 卡片 | 42 citations 从摘要→全文深度 | 中 | #1 |
| 3 | 添加 cross-link Tier 1 (3对6条有向链接) | 覆盖率 25%→45% | 低 | 无 |
| 4 | 添加 cross-link Tier 2 (3对6条有向链接) | 覆盖率 45%→70% | 低 | #3 |
| 5 | 消化 Tier-1 repo top-3（governance-toolkit, graphrag, nvk-llm-wiki） | +2361 .py 知识增量 | 高 | 无 |
| 6 | 代码重 webpage 源增强提取（保留 code block 格式） | 581 code/pre 元素恢复语义 | 中 | 无 |
| 7 | 重抓取 2 个空壳源 + 审查 langchain 极端压缩源 | 3 个源数据完整性 | 低 | 无 |
| 8 | 消化 Tier-1 repo #4-8 + Tier-3 精选 2 个 | 长尾知识覆盖 | 高 | #5 |
