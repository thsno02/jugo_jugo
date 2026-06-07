---
id: credibility-scoring-pipeline
title: 可信度评分管道
status: accepted
card_type: mechanism
tags: [llm-wiki, credibility, source-quality, dedup, research-pipeline]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
justification: ../justification/credibility-scoring-pipeline.md
canonical_concept: credibility-scoring-pipeline
aliases: [可信度评分, credibility scoring, 来源可信度管道, Phase 2b credibility]
summary: >-
  credibility-scoring-pipeline（可信度评分 / credibility scoring / 来源可信度管道 / Phase 2b credibility）
  是 llm-wiki 研究流水线中防止「狐狸看守鸡舍」的独立评估阶段：在智能体返回结果后、摄入前，
  用五维信号（同行评审/时效/权威/偏见/佐证）打分并分为四级
related: [parallel-multi-agent-research, thesis-driven-research, citation-quality-tri-dimension]
---

可信度评分管道（Phase 2b: Credibility Review）位于研究流水线中**智能体返回结果之后、来源摄入之前**，是一个独立于智能体自评的质量关卡[^src-1]。其存在的理由是防止「狐狸看守鸡舍」问题——如果让智能体自己评价自己找到的来源质量，缺乏外部制衡[^src-2]。

**五维评分信号**[^src-3]：

| 信号 | 计分 |
|------|------|
| 同行评审（DOI、期刊名、会议名） | +2 如是，0 如否 |
| 时效性（近 3 年发表） | +1 近期，0 较旧，-1 超过 10 年 |
| 作者权威性（知名专家、被广泛引用） | +1 如确立，0 如未知 |
| 潜在偏见（行业赞助、活动家组织） | -1 如检出，0 如清洁 |
| 佐证（多个智能体发现类似主张） | +1 每多一个智能体，最高 +2 |

**四级分类**[^src-4]：
- **High（4-6 分）**：同行评审、近期、权威、无偏见 → 以 confidence: high 摄入
- **Medium（2-3 分）**：已发表但非同行评审，或较旧，或作者未知 → 以 confidence: medium 摄入
- **Low（0-1 分）**：博客、新闻稿、不可验证、有偏见 → 仅当无更好来源覆盖该角度时才摄入，标记 confidence: low
- **Reject（<0 分）**：明显垃圾、掠夺性期刊、伪造数据 → 完全跳过

**处理流程**[^src-5]：
1. 对所有智能体返回的全部来源评分
2. 去重（相同 URL 保留一份；内容重叠度 >80% 保留可信度更高者）
3. 按（可信度分 x 智能体质量分）排序
4. 选取前 N 个进入摄入（N = --sources 数量）
5. 跳过的来源连同理由在报告中列出

在 **retardmax 模式**中：降低拒绝阈值（接受 Medium 及以上而不过滤），但仍计分——分数作为 confidence 标签传递到下游文章[^src-6]。

该管道与引用质量三维评估模型共享「多维度独立评分后加权聚合」的设计模式[^card-1]，并直接决定了并行多智能体研究最终产出的文章置信度标签[^card-2]。

## Footnotes

[^card-1]: [引用质量三维评估](citation-quality-tri-dimension.md) -- 可信度管道的五维加权聚合与引用质量三维模型共享「多维度独立评分」的设计模式
[^card-2]: [并行多智能体研究机制](parallel-multi-agent-research.md) -- 可信度管道是并行研究 Phase 2b 阶段，直接决定摄入来源的 confidence 标签

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "Phase 2b: Credibility Review — after agents return, before ingestion"
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "This prevents the 'fox guarding the henhouse' problem where agents self-rate their own source quality."
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "Peer-reviewed? +2... Publication recency +1... Author authority +1... Potential bias -1... Corroboration +1 per additional agent, max +2"
[^src-4]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "High (4-6 points)... Medium (2-3 points)... Low (0-1 points)... Reject (<0 points)"
[^src-5]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "Score all sources from all agents... Deduplicate... Rank by (credibility score x agent quality score)... Select top N for ingestion"
[^src-6]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "In retardmax mode: lower the rejection threshold (accept Medium and above without filtering), but still score — the scores carry forward into confidence tags."
