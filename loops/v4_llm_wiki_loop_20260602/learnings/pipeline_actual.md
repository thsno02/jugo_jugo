---
schema: v4_learnings
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-12
topic: pipeline_actual
purpose: retrospective
---

# 管线实际状态（Pipeline As-Built）

本文记录 v4 管线在实际运行后的真实形态，对照 v3 `future_plans/pipeline_spec.md` 的设计意图，标出差异、失败点和经验。

---

## 1. 逐源类型路由（Per-Source-Type Routing）

v4 管线的核心数据采集层按源类型分流——每种源类型有不同的"阅读面"（reading surface）生成路径：

| 源类型 | 设计阅读面 | 实际运行路径 | 状态 |
|--------|-----------|-------------|------|
| arxiv (17) | agent_source_bundle.txt（TeX 全文拼接） | 15 正确使用 bundle；2 异常（ragas 46MB bloat, knowledge-compounding PDF-only） | 81% 正常，但 10% citations 误读了 text.txt（仅含摘要页 HTML） |
| webpage (27) | text.txt（理想为 markdown.md via trafilatura） | 21 有效 text.txt；3 空壳（反爬拦截）；3 高损耗（1261 结构元素丢失） | trafilatura 升级未实施；代码块/图片丢失严重 |
| github_repo (20) | material_bundle.txt（repo2doc 产物） | 仅 2/20 有 bundle（graphrag 143KB + nvk-llm-wiki 438KB） | repo2doc 工具未编写；90% repo 知识锁死 |
| reddit (6) | thread.json + text.txt | 全部被反爬拦截，6/6 blocked | 完全失败 |
| hacker_news (1) | text.txt | 完美（50KB, 95 comments） | 无需修复 |
| pypi (2) | pypi.json + text.txt | 完美 | 无需修复 |
| gist_raw (1) | text.txt | 完美（12KB Karpathy 原文） | 无需修复 |

**关键教训**：`source_text_path()` 原始实现是一个扁平优先级链（bundle > text.txt > browser_text.txt > README.remote > raw.txt），不区分源类型。arxiv 的 text.txt 实际只含摘要页 chrome (~5KB)，但被 fallback 误选。修复方案是逐类型 dispatch（见 `data_collection_fix_plan.md` S3.2）。

---

## 2. 提取协议（Extraction Protocol）

### 设计意图（v3 spec）

spec S2 定义了 coordinator + reader + questioner + reviewer 四角色模型。设计中 reviewer 是"独立审查者"——在 questioner 声明 SATISFIED 后才介入。

### 实际运行

实际编排模型：**coordinator 静态分派 reader+questioner 对话循环，reframe 在每轮间执行**（非最后一步）。

```
coordinator dispatches:
  1. reader 全文读取 → 产出 digest（in-memory，不落盘）
  2. questioner（拥有全文 + digest）系统性提问
  3. reader 从 KV-cache-warm 的全文回答
  4. [每轮间] Q&A pairs → reframing → draft cards
  5. [SATISFIED 后] reviewer quit-audit（覆盖率 + 源忠实抽查）
  6. inline fusion check（grep KB 查重叠）
```

**与 spec 的关键差异**：

- spec 暗示 reviewer 是与 reader/questioner 平行的独立角色。实际中 reviewer 只在 SATISFIED 后触发一次，是"退出门控"而非持续监督
- digest 设计为 reviewer 的覆盖率 checklist，但实际中 questioner 也参考它（questioner 拥有全文这一点是后加的设计决策）
- reframe 在每轮间执行（非 spec 描述的"最后一步"），使 canonical_concept 列表能反馈给 questioner 避免重复

---

## 3. Ingest 阶段

完全按 spec 实施：**script-only，禁止 LLM 复制 body**。

操作：
1. frontmatter `status: draft` → `status: accepted`
2. 物理移动 `drafts/cards/` → `kb/cards/`
3. 物理移动 `drafts/justification/` → `kb/justification/`
4. 重建 `kb/indexes/cards.md`（active-only view）

无偏差。280 张卡经主批次入库，后续 pipeline gaps 修复增量 48 张同路径入库，最终 328 张。

---

## 4. Governance 阶段

### 设计意图

spec S4 定义了 grep-based dedup + canonical normalization + distinction linking + merge-WHY。明确排斥 embedding/clustering。

### 实际运行

- **grep-only recall** 按设计工作：agent 自主 grep canonical_concept/aliases/summary，多轮 zh/en/同义词改写
- **无 cluster count target**：早期尝试过设定聚类数量目标，导致过度合并（"cluster damage"）。最终学到：clustering 是启发式发现手段，不是分类目标
- **related 字段派生**：从 `[^card-N]` + `[^dist-N]` footnotes 扫描提取，脚本幂等——245/280 张卡被更新，861 条 related links
- **链接密度**：264/280 张卡有链接（94.3%），平均 3.3 条/卡
- **cross-link 缺口**：审计发现跨家族链接覆盖率仅 25%（citation eval 三家族间），后修复至 ~70%

**cluster damage 教训**：governance 的正确心态是"让问题更简单而非全解"（best-effort zen）。grep 命中 count>=2 时才启动人工判断，不预设"应该有 N 个簇"。

---

## 5. Spec vs Reality 对照表

| 维度 | v3 Spec 设计 | v4 实际运行 | 状态 |
|------|-------------|-------------|------|
| 源路由 | 逐类型优先级链 | 扁平 fallback，导致 arxiv text.txt 误读 | FAILED → 已识别修复方案 |
| repo 消化 | material_bundle.txt via repo2doc | repo2doc 未编写，18/20 repo 无 bundle | FAILED → 待实施 |
| Reddit 抓取 | thread.json 结构化评论树 | 全部被反爬拦截 | FAILED → 需 old.reddit.com/.json 重抓 |
| webpage 提取 | markdown.md via trafilatura | 原始 text.txt，1261 结构元素丢失 | PARTIAL → Phase 4 升级 |
| Extract 角色模型 | coordinator + reader + questioner + reviewer | 如设计，但 reviewer 仅做退出门控 | WORKED（细节微调） |
| Digest 用途 | reviewer 覆盖率 checklist | reviewer + questioner 双重参考 | EVOLVED（比 spec 更灵活） |
| Questioner 视野 | 全文 + digest | 如设计 | WORKED |
| Reframe 时机 | 每轮间执行 | 如设计 | WORKED |
| Ingest | script-only, status flip + move | 如设计 | WORKED |
| Governance | grep-based, 无 cluster 目标 | 如设计（经历了 cluster damage 后回到此路） | WORKED（有痛苦教训） |
| Mode B Synthesis | deferred | 确实 deferred | AS PLANNED |
| Typed footnote | 四种 prefix (src/card/dist/url) | 完整实施 | WORKED |
| Justification journal | append-only per-card | 完整实施 | WORKED |
| KB 规模 | 未预设目标 | 328 张 active 卡（280 governance pass + 48 pipeline gaps 修复增量）+ index | EXCEEDED EXPECTATIONS |

---

## 6. 数据采集层问题总结

审计（`pipeline_gaps_report.md` + `data_collection_fix_plan.md`）发现 4 类系统性缺口：

### 6.1 严重度分布

| 严重度 | 问题 | 量化影响 |
|--------|------|---------|
| CRITICAL | arxiv text.txt 误路由 | 62/626 footnotes (10%) 仅摘要深度，7 源受影响 |
| CRITICAL | cross-link 跨家族缺失 | 覆盖率 25%，14-16 条有向链接缺失 |
| HIGH | webpage 结构丢失 | 1261 结构元素（code=530, img=263, svg=370） |
| MEDIUM | repo 未消化 | 8 个 Tier-1 repo, 2520+ .py 未提取 |

### 6.2 根因分析

1. **路由逻辑过于简单**：单一扁平优先级链不适应异构源类型
2. **工具缺失**：repo2doc 在 spec 中提到但从未实现
3. **反爬未预案**：Reddit 6 源全军覆没，无降级策略
4. **提取器能力不足**：HTML→text 丢失全部 pre/code/table/img 结构

### 6.3 74 源总览

- 44/74 (59%) 具有可靠阅读面
- 12/74 (16%) 完全失败（Reddit 6 + 空壳 3 + PDF-only 1 + 403 错误 2）
- 18/74 (24%) 需要 repo2doc 生成 bundle

> 修复后实际有效源增至 50+（23 webpage 获得 markdown.md，arxiv-ragas bundle 重建）

---

## 参考文件

- 设计 spec：`../../v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`
- 管线缺口报告：`../outputs/llm_wiki/kb/audits/pipeline_gaps_report.md`
- 数据采集修复计划：`../outputs/llm_wiki/kb/audits/data_collection_fix_plan.md`
- 任务清单：`../task.md`
