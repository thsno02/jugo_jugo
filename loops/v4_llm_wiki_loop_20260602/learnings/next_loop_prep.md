---
schema: v4_learnings
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-12
topic: next_loop_prep
purpose: forward_prep
---

# 下一轮准备（v5 Inputs）

本文将 v4 全部经验提炼为 v5 的可执行输入。v4 最终产出 328 张活跃卡片（280 张来自主 governance pass + 48 张来自 pipeline gaps 修复增量）。v5 是独立的 0->1 过程——不引用 v4 KB、不继承 v4 卡片、不依赖 v4 的 related 图。但 v5 必须吸收 v4 的管线修复和技能迭代成果。

---

## 0. 运行环境

启动命令: claude --permission-mode bypassPermissions
Agent 调用: 所有 Agent() 必须传 model: "opus"（用户 endpoint 不支持 Haiku）
Sub-agent 递归: Agent tool 被 harness strip，若需嵌套用 claude -p via Bash
源材料读取: Read 全文（1M context），不要 limit:2000
Python 环境: trafilatura 2.1.0 已安装（webpage markdown 转换）

---

## 1. 待处理源（优先级排序）

### Tier-1: github_repo（需 repo2doc 生成 bundle，预计新增 60-80 张卡）

| 优先级 | Repo | 核心知识点 | 预估卡片 |
|--------|------|-----------|---------|
| 1 | microsoft-agent-governance-toolkit (1791py/729md) | policy DSL, runtime enforcement, audit schema | ~20 |
| 2 | kytmanov-obsidian-local (81py/16md) | local-first Ollama, review-rejection loop | ~8 |
| 3 | ar9av-obsidian-wiki (10py/58md) | 15+ agent skill framework | ~8 |
| 4 | ngmeyer-librarian-mcp (Rust) | MCP-native wiki, trigram search, D3 graph | ~5 |
| 5 | vectifyai-openkb (65py/5md) | vectorless PageIndex retrieval | ~5 |
| 6 | atomicstrata-llm-wiki-compiler (TS/Node) | multi-provider compilation strategy | ~4 |
| 7 | nashsu-llm-wiki (desktop) | 4-signal graph, Louvain, multimodal ingest | ~5 |
| 8 | agricidaniel-claude-obsidian (4py) | DragonScale Memory, 11-skill architecture | ~4 |

剩余 10 个 repo 为 Tier-2/3（paper-companion 与 Karpathy 变体），可视时间决定是否消化。

### Tier-2: 重抓/修复源

| 源 | 方法 | 预估卡片 |
|----|------|---------|
| reddit x6（全部 blocked） | old.reddit.com/<url>.json + 学术 User-Agent | 6-10 |
| arxiv-knowledge-compounding (PDF-only) | pymupdf/pdftotext -> agent_source_bundle.txt | 3-5 |
| obsidian-help-link-notes (SPA) | 直接 fetch Obsidian Publish API markdown | 2-3 |
| aicritique x2 (Alibaba 拦截) | web.archive.org 快照或标记 dead | 0-4 |
| langchain-long-term-memory-docs (SSR 压缩) | 从 raw.html script payload 提取 Next.js hydration data | 2-3 |

### Tier-3: 已有源质量提升（不产新卡，但可重提取）

- arxiv-graph-poisoning / arxiv-lightmem / arxiv-wicer：共 42 citations 仅摘要深度，需从 agent_source_bundle.txt 重新提取
- 15 个 webpage 代码重源：恢复 code block 结构（530 code + 51 pre 元素）
- OWASP x2：PDF 内容下载（当前仅摘要页）

---

## 2. 技能更新清单

### 2.1 Reframing: 保留 hedging markers

**问题**：v4 审计发现 62% 卡片（174/280）零认识论限定词。根因是 reframing 规则 1「对话体 -> 知识陈述体」系统性剥离了 reader 回答中的 hedge markers。

**修改**：
- 新增规则：「保留 reader 回答中的认识论标记。源材料说'suggests'/'implies'/'appears to' 时，卡片正文必须保留对应中文限定词（'据材料推测'/'证据有限'/'源暗示但未证实'）。删除 hedging 等于篡改源置信度。」
- frontmatter 新增 `evidence_basis` 字段，取值枚举：`experimental_paper | theoretical_paper | practitioner_report | community_discussion | documentation | code_implementation`
- 源类型→evidence_basis 默认映射：arxiv->experimental/theoretical, blog/gist->practitioner_report, HN/reddit->community_discussion, pypi->documentation, github_repo->code_implementation

### 2.2 Comparison: 强制归因标记

**问题**：v4 审计发现 5/21 comparison 卡（24%）存在未归因概念泄漏。脚注叙事构成了隐式上下文通道。

**修改**：
- 新增 Footnote Discipline 规则：「comparison 卡正文提及非核心 tension 概念时必须有 [^card-N] 脚注追溯来源卡。裸名引用（无脚注的概念名）是 BUG。」
- comparison 生成 prompt 显式区分"卡正文 src 锚定内容"与"脚注跨引内容"
- 或者标记为 editorial：若概念为合理推论则添加「[编者注：此处为基于 X 卡的延伸推断]」

### 2.3 Reader: 位置格式标准化

**问题**：v4 种子测试发现 reader 混用中文序数和英文格式，导致 footnote 位置描述混乱。

**状态**：已修复——统一为 `"Section Title" PN` 格式。v5 需验证此规范是否在全量运行中被一致执行。

**验证方法**：Phase 2 种子测试后抽查 10 张卡的 `[^src-N]` 位置段，确认无中文序数混用。

### 2.4 Questioner: Phase 5 覆盖率 + 原子性

**已完成的修改**（从 v4 种子测试）：
- Phase 5 包含"看似次要的节"（Tips/Note 等）
- 标题连词信号 -> 拆卡
- canonical 反馈机制防重复追问

**遗留**：长材料（>200 page bundle）的 Phase 2 深度追问无明确终止条件。建议增加"3 层追问后若信息递减率 > 70%（新增 idea < 2）则停止"硬约束。

---

## 3. 管线工具待建

（详见 ./pipeline_actual.md #6 — 数据采集层问题总结）

### 3.1 source_router.py（逐类型 boundary-read dispatch）

**功能**：替代当前 `source_text_path()` 的扁平 fallback 逻辑。按源类型分流：

```
arxiv:       agent_source_bundle.txt（排除 .bib/.sty noise）
webpage:     markdown.md > text.txt（trafilatura 升级后优先 markdown）
github_repo: material_bundle.txt > repo/README.md
reddit:      text.txt（重抓后）
hacker_news: text.txt
pypi:        text.txt
gist_raw:    text.txt
```

**质量门控**：text.txt < 500 字节或含 blocked/captcha/403 关键词 -> 标记 `scrape_status: failed`，不传入 extraction。

### 3.2 repo2doc.py（仓库 -> material_bundle.txt）

**输入**：`data/raw/github_repo/<slug>/repo/`
**输出**：`data/raw/github_repo/<slug>/material_bundle.txt`（上限 500KB）

**拼接优先级**：
1. README.md（项目定位 + 用法）
2. docs/**/*.md（架构文档、ADR）
3. CLAUDE.md / CONTRIBUTING.md / ARCHITECTURE.md
4. 核心入口文件（main.py / index.ts / lib.rs 前 500 行）
5. 配置 schema（*.toml / *.yaml 中注释型配置）
6. 测试 fixtures 目录列表（文件名暗示边界条件）

**特殊处理**：
- microsoft-agent-governance-toolkit（3871 文件）：拆 3 sub-bundle（docs/, python-sdk/, examples/）
- 超大 repo：排除 checkpoint/ / data/ / node_modules/ / .git/

### 3.3 Governance 无集群模型

**弃用**：固定集群分组 + derive-related 集群内搜索。

**新模型**：sequential per-card governance
```
对每张新 draft 卡 C：
  1. grep 全量 KB（canonical_concept + aliases + key_terms）命中候选集 S
  2. 对 S 中每张候选卡 Read 全文
  3. judge：duplicate / overlap_merge / distinct_link / unrelated
  4. 执行：merge -> fusion card / link -> 双向 related + footnote / unrelated -> skip
```

**关键约束**：
- 无 cluster count target（启发式驱动，不是数量驱动）
- grep 未命中 != 无关（supplement 同义词改写搜索 2 轮）
- 全局搜索而非集群内搜索（消除跨领域桥梁遗漏）

### 3.4 YAML lint gate

**触发**：每次 derive-related / frontmatter 修改后自动运行。

**检查项**：
- related 字段无双格式（行内 [] 与缩进 - 互斥）
- 所有 frontmatter key 可被标准 YAML 解析器正确读取
- slug 引用在 cards.md index 中存在（无悬空引用）

---

## 4. 治理设计修正

### 4.1 核心原则

- **无 cluster count target**：clustering 是启发式发现手段，不是分类目标。v4 经历"cluster damage"后确认此原则。
- **Best-effort zen**：governance 目标是降熵，不是完备性。O(N^2) 完备配对在 300+ 卡规模不经济。
- **grep-friendly metadata over embedding**：召回质量来自 canonical_concept/aliases/summary 的一致性纪律，不来自向量基础设施。

### 4.2 Sequential per-card governance（取代集群分组）

**流程**：
```
ingest 完成（全部 draft 入库后）
  -> 全量 pairwise fusion scan（对每张新卡 grep 全量 KB）
  -> judge：duplicate / overlap / distinct_link / unrelated
  -> 写入 related + footnote
  -> 孤儿检测 gate：related:[] 且入站=0 的卡触发补链
```

### 4.3 双向 backlink 强制

**规则**：derive-related 写入 A->B 时，同步检查 B->A 是否存在。若不存在且关系类型为 symmetric（shared_concept / contrast / parallel_design），则自动补写 B->A。

**例外**：天然单向关系不强制反向——comparison 卡作为 sink 是正确设计。但需在被比较的 subject cards 中添加 `see_also: comparison-X` 轻量指针。

### 4.4 Comparison 卡 provenance

**规则**：comparison 卡的每个 tension point 必须追溯至具体 [^card-N] 或 [^src-N]。无脚注的 tension point 标记为 `[编者注]`。

### 4.5 Post-governance 检查脚本

自动化检测：
1. 裸名概念检测（正文含概念名但无对应 footnote）
2. 孤儿卡检测（related:[] 且入站=0）
3. 反向链接不对称率（目标 < 20%，v4 为 40.3%）
4. 跨域桥梁覆盖率（每个 domain 至少 2 条对外链接）

---

## 5. 第一天该做什么

### Step 1: 管线工具准备（Day 0，在 extraction 前完成）

1. **编写 repo2doc.py** 并对 Tier-1 前 3 个 repo 生成 material_bundle.txt，人工抽检质量
2. **修复 source_text_path()** 为逐类型 dispatch（copy fix_plan S3.2 代码）
3. **重建 arxiv-ragas bundle**（排除 anthology.bib，从 46MB 降至 ~34KB）
4. **标记 3 个死源**（aicritique x2 + obsidian-help）为 `exclude_from_pipeline: true`
5. **运行 YAML lint gate** 验证工具链就绪

### Step 2: 数据采集补全（Day 1）

1. 对 Tier-1 全部 8 个 repo 运行 repo2doc.py
2. 尝试 Reddit 重抓（old.reddit.com/.json）——若失败立即标记为 deferred 不阻塞
3. 对 arxiv-knowledge-compounding 运行 pymupdf PDF->text

### Step 3: Extraction（Day 2-3）

1. 全部源经 source_router.py 路由后进入 extraction
2. 并行 extraction（提速），但记录每批次 draft 产出时间戳
3. **关键**：extraction 完成后、ingest 前，执行 intra-loop pairwise fusion scan——解决 v4 的"batch 并行无法去重"问题

### Step 4: Ingest + Governance（Day 4）

1. Script-only ingest（status flip + move + index rebuild）
2. Sequential per-card governance（全局 grep，非集群分组）
3. 双向 backlink 强制 + 孤儿检测 gate
4. YAML lint gate 验证格式一致性

### Step 5: 审计验收（Day 5）

1. FSJS 审计配方：FILTER（机械扫描）-> SHARD（源亲和分片）-> JUDGE（语义判断）-> SYNTHESIZE（汇聚）
2. 验收标准：
   - 源忠实性：零伪造引用（与 v4 同标准）
   - 权威扁平化：零限定词比例 < 40%（v4 为 62%，目标改善 1/3）
   - 反向链接不对称率 < 25%（v4 为 40.3%）
   - 孤儿卡（非 comparison）< 5%（v4 为 6.8%）
   - 跨域桥梁：每个 domain 至少 2 条对外链接（v4 的 wikibase 0 条）

---

## 6. 风险预案

| 风险 | 概率 | 影响 | 缓解策略 |
|------|------|------|---------|
| Reddit API 也 block 学术 UA | 高 | 6 源失败 | 备选 PRAW OAuth2 或 Pushshift 存档；不阻塞 loop |
| repo2doc 对大 repo 生成低质量 bundle | 中 | 噪声卡片 | 500KB 上限 + 前 3 个人工抽检后再批量运行 |
| reframing hedge 保留规则导致卡片冗长 | 中 | 可读性下降 | 限定词用括号旁注形式而非完整从句 |
| sequential governance 在 400+ 卡规模下耗时过长 | 中 | 瓶颈 | 分 batch（50 卡/轮），每轮 governance 后更新 grep 基 |
| PDF 提取（knowledge-compounding）文本质量差 | 低 | 10 张卡仍为 caveat-pass | 标记 `text_extractable: partial`，epistemic_confidence 降级 |

---

## 7. 从 v4 继承的验证清单

以下 v4 确认的设计决策在 v5 中**继续生效**，无需重新验证：

- [x] Loop 独立性（0->1，不引用前序 KB）
- [x] Zettelkasten 无 taxonomy（card_type/tags 自由描述）
- [x] Comparison 卡为 sink（零入度 by design，补 see_also 提高可发现性）
- [x] grep-friendly metadata over embedding
- [x] Best-effort governance zen（降熵而非完备性）
- [x] Ingest = script-only（禁止 LLM 复制 body）
- [x] Typed footnote 四前缀（src/card/dist/url）
- [x] Justification journal append-only

---

## 8. 文件依赖

v5 启动前需确认以下文件就位：

| 文件 | 状态 | 用途 |
|------|------|------|
| `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/scripts/source_router.py` [待建] | 待编写 | 逐类型 boundary-read dispatch |
| `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/scripts/repo2doc.py` [待建] | 待编写 | repo -> material_bundle.txt |
| `scripts/yaml_lint.py` | 待编写 | frontmatter 格式验证 |
| `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/scripts/run_loop.py` (source_text_path 修复) | 待修改 | 逐类型 dispatch 替代扁平 fallback |
| `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/scripts/fetch_sources.py` (bundle 过滤) | 待修改 | .bib 排除 + 大小上限 |
| `skills/reframing/PROMPT.md` (hedge 保留规则) | 待修改 | evidence_basis + hedge 保留 |
| `skills/reframing/PROMPT.md` (comparison footnote discipline) | 待修改 | 裸名概念 = BUG |
| `data/raw/github_repo/*/material_bundle.txt` x18 | 待生成 | repo2doc 产物 |
