---
schema: v5_learnings
loop_id: v5_llm_wiki_loop_20260612
created: 2026-06-12
topic: next_loop_prep
purpose: forward_prep
---

# 下一轮准备（v6 Inputs）

v5 产出 477 张活跃卡片（63 有效源，4 wave parallel extraction → 487 draft → fusion 去重后 477）。v6 是独立 0->1 过程——不引用 v5 KB、不继承 v5 卡片。但 v6 必须吸收 v5 的管线改进和审计发现。

---

## 0. 运行环境（继承）

- 启动命令: `claude --permission-mode bypassPermissions`
- Agent 调用: 所有 Agent() 必须传 `model: "opus"`
- Sub-agent 递归: Agent tool 被 harness strip，嵌套用 `claude -p` via Bash
- 源材料读取: Read 全文（1M context），不要 limit:2000
- Python 环境: trafilatura 2.1.0 已安装

---

## 1. 权威扁平化指标改进方案

### 问题

v5 审计发现 79.8% 零限定词，远超 <35% 目标。但根因分析表明大部分源（arxiv 实验论文 59%、practitioner 报告 34%）本身以断言体写作，不含 hedge。当前一刀切指标无法区分"源无 hedge 的合理断言"与"源有 hedge 但卡片漏保留"。

### v6 方案: 分层 + 条件检测

**取消全局百分比指标**，改为:

1. **源有 hedge → 卡片必须保留**（精确检测）:
   - FILTER 阶段对每张卡的源文本 grep hedge 词表
   - 仅当源命中 hedge 词表时，检查卡片是否保留
   - 公式: `hedge_preservation_rate = 卡片保留限定词的条数 / 源含 hedge 的引用段落数`
   - 目标: `hedge_preservation_rate >= 90%`

2. **按 evidence_basis 分层审计**:
   - `community_discussion`: 严格检测（这类源天然含 hedge）
   - `experimental_paper`: 仅检测 discussion/limitation section 的引用
   - `practitioner_report` / `documentation` / `code_implementation`: 不设限定词目标

3. **实施方法**:
   - FILTER 阶段: 对 suspect 脚注的源段落做 hedge 词表 grep
   - 仅 hedge 存在但卡片丢失的情况计为违规
   - 新输出指标: `hedge_leakage_count`（源有 hedge 但卡片剥离的实例数）

---

## 2. repo2doc 实施建议

### 现状

v5 对 18 个 github_repo 源仅消化了 README（repo2doc 未实施），产出 76 张卡。信息密度低——平均 4.2 卡/repo，而 arxiv 论文平均 11 卡/源。

### v6 实施方案

**工具**: `tools/repo2doc.py`（新建，基于 v4 设计但简化）

**拼接优先级**（上限 500KB）:
1. README.md
2. docs/**/*.md（架构文档、ADR）
3. CLAUDE.md / CONTRIBUTING.md / ARCHITECTURE.md
4. 核心入口文件（main.py / index.ts / lib.rs 前 500 行）
5. 配置 schema（*.toml / *.yaml 注释型配置）

**特殊处理**:
- 超大 repo（>5000 文件）: 拆 sub-bundle（docs/ / src/ / examples/）
- 排除: checkpoint/ / data/ / node_modules/ / .git/ / __pycache__/

**预期提升**: 若 repo2doc 实施后每 repo 平均产出从 4.2 卡升至 8-12 卡，18 repo 可贡献 70-140 张增量卡。

---

## 3. Reddit 重抓方案

### 现状

v5 继承 v4 的 6 个 Reddit 源全部 blocked（反爬拦截），直接标记为死源排除。

### v6 方案

**方法 1（推荐）**: `old.reddit.com/<path>.json`
- Reddit 的 old. 子域名暴露 JSON API，无需认证
- User-Agent 设为学术 bot 格式: `llm-wiki-research/1.0 (research; contact@example.com)`
- 抓取后保存为 `data/raw/reddit/<slug>/thread.json`
- 解析: 递归展开 replies 树，拼接为 `text.txt`

**方法 2（备选）**: PRAW OAuth2
- 注册 Reddit app，获取 client_id/secret
- 优点: 稳定、合规
- 缺点: 需人工注册应用

**方法 3（最后手段）**: web.archive.org 快照
- 搜索 Wayback Machine 有无缓存
- 若有: 直接用 archive 版本的 HTML

**预估**: 6 源 → 6-10 张卡（community_discussion 类型，hedge 保留是重点）。

**风险预案**: 若方法 1 也被 block，不阻塞 loop——标记为 `exclude_from_pipeline: true`。

---

## 4. Fusion Scan 优化

### 问题

v5 FILTER 阶段 431 条脚注 grep 验证中 18 条 suspect，其中 10 条因 LaTeX 格式差异、4 条因 Markdown 格式差异。这些全部经 JUDGE 语义验证为 pass，但增加了审计工作量。

### v6 方案: 格式剥离预处理

**实施**:
1. 对源文件创建 `.stripped` 副本（不修改原文件）:
   - LaTeX: 移除 `\textbf{}`, `\emph{}`, `$...$`, `\\`, `&`, `\%` 等标记
   - Markdown: 移除 `**`, `` ` ``, `|`, 多余空格
2. grep 时同时搜索原文件和 `.stripped` 副本
3. 任一命中即为 verified

**预期效果**: 消除 14/18 (78%) 的 false-suspect，JUDGE 工作量从 18 降至 ~4。

**实施位置**: 集成到 `tools/fusion_candidates.py` 的 grep 逻辑中。

---

## 5. 管线工具继续可用

以下 v5 工具经验证可直接复用（路径: `loops/v5_llm_wiki_loop_20260612/tools/`）:

| 工具 | 功能 | v5 验证状态 |
|------|------|------------|
| `source_router.py` | 逐类型 boundary-read dispatch | 63 源全部正确路由 |
| `yaml_lint.py` | frontmatter YAML 格式验证 | 477 卡零格式错误 |
| `ingest.py` | status flip + move + index rebuild | 正常工作 |
| `batch_link.py` | 批量 related 双向链接写入 | 151 对链接正确写入 |
| `backward_backlink.py` | 反向 backlink 补全 | 不对称率从初始 ~15% 降至 0.5% |
| `fusion_candidates.py` | pairwise 重叠检测 | 163 候选对正确识别 |

**复用建议**: 直接复制 tools/ 目录到 v6 loop，仅需修改 fusion_candidates.py 增加格式剥离。

---

## 6. 规模预估

### 基准

v5: 63 有效源 → 477 卡（7.6 卡/源）

### v6 预计

| 增量来源 | 源数 | 预计卡片 | 依据 |
|----------|------|---------|------|
| 现有源（baseline） | 63 | 477 | 与 v5 相同源池 |
| repo2doc 增量 | 18 | +70-100 | 4.2→8 卡/repo 提升 |
| Reddit 重抓 | 6 | +6-10 | community_discussion 密度低 |
| 新增外部源（可选） | 5-10 | +30-60 | 视 queue 补充情况 |
| **总计** | **80-97** | **550-650** | |

**注意**: 规模增长主要来自 repo2doc 的信息密度提升，而非简单堆源。

---

## 7. 编排模式建议

### 继续使用

- **4 wave parallel extraction**: v5 证明有效（按 token 量均衡分配），v6 可沿用
- **Post-extraction sequential fusion scan**: 必须在全量 draft 落地后执行
- **batch_link 脚本化**: 比逐卡手动 governance 更准确（v5 零写入错误）
- **FSJS 审计**: Filter-Shard-Judge-Synthesize 四阶段稳定

### 改进

- **Orphan governance 前置**: v5 在 batch_link 后发现 81 孤儿需补链。v6 建议 fusion scan 阶段即标记"疑似孤儿"（related candidates < 2），governance 阶段优先处理
- **Wave 内 sub-split**: 若某 wave 内单源 token 量 >200K，拆为独立 sub-agent（v5 有 1-2 个源偏大）

---

## 8. 从 v5 继承的验证清单

以下 v5 确认的设计决策在 v6 中继续生效:

- [x] Loop 独立性（0->1，不引用前序 KB）
- [x] Zettelkasten 无 taxonomy（card_type/tags 自由描述）
- [x] Comparison 卡为 sink（零入度 by design）
- [x] grep-friendly metadata over embedding
- [x] Best-effort governance zen
- [x] Ingest = script-only（禁止 LLM 复制 body）
- [x] Typed footnote 四前缀（src/card/dist/url）
- [x] evidence_basis 字段必填（v5 新增，已验证有效）
- [x] Anti-merge bias in fusion scan（宁可 distinct_link 也不轻易 merge）
- [x] backward_backlink 作为独立 pass（非嵌入 batch_link）
