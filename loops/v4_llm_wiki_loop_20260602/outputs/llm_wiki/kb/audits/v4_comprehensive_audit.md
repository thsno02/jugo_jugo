---
schema: audit_report.v1
loop_id: v4_llm_wiki_loop_20260602
date: 2026-06-07
cards_total: 280
agents_reporting: 21
cards_audited_mechanical: 280
cards_audited_faithfulness: 280
sources_audited: 27
---

# v4 综合审计报告

## 1. 执行摘要

- **YAML `related` 字段序列化缺陷是本轮最严重的系统性问题。** 70 张卡 (25%) 的 `related` 字段同时包含行内数组 `[]` 和缩进列表 `- item`，YAML 解析器只读行内值，缩进项被静默丢弃。其中 11 张行内为空 `[]`，导致全部 cross-link 完全丢失；其余 59 张部分丢失。另有 5 张卡 `related` 为真空（无任何链接且无缩进项），合计 75 张卡的 cross-link 数据不可靠。
- **源忠实性整体优秀。** 21 个审计 agent 共验证约 400+ 条 `[^src-*]` 脚注，零伪造引用，零凭空捏造数字。仅发现 2 处数值错配（temporal-reasoning-difficulty 和 locomo-five-reasoning-types 的 73% gap 混淆）、2 处上下文泄露（comparison-corrective-vs-servant-agency 的确认优先规则/参与程度谱系、comparison-multihop-runtime-vs-compiletime 的 GraphRAG 段落）。
- **Comparison/distinction 卡的源锚定模式存在结构性弱点。** 约 15 张 comparison 卡在 `source_ids` 中列出来源但正文零 `[^src-*]` 脚注，全部依赖 `[^card-*]` 间接引用。链条可追溯但审计成本高，且 `source_ids` 字段语义被稀释。
- **JJ 文件格式不一致。** 约 15 个 JJ 文件缺少标准 `## creation` 事件头或使用非标格式，集中在 comparison 类卡片，表明 comparison 卡的生成流水线与主流水线存在模板差异。
- **材料穷尽度总体良好，但存在可操作的缺口。** 最显著的缺失：arxiv-memory-as-metabolism 的冲突路由矩阵（Section 5.0，论文核心规范贡献）、arxiv-memgpt 的 Queue Manager 子系统、arxiv-locomo 的多模态对话生成任务、arxiv-poisonedrag 的 LLM agent 攻击结果。
- **原子性和别名质量整体通过。** 35 个标题含连词的疑似卡片经实质审查后仅 1 张（graphrag-community-hierarchy）为边界情况，其余均为合理的不可分概念对。约 10 个别名过于笼统（如 '系统模型'、'领域模板'、'positioning spectrum'）。
- **10 张 arxiv-knowledge-compounding 卡的源文本无法被验证。** 源 PDF 不可提取文本，审计仅能做摘要级一致性和内部算术校验。这是一个验证盲区。

## 2. 设计不变量判定

| 不变量 | 判定 | 证据 |
|---|---|---|
| Loop 独立性 | **PASS** | 280 张卡无任何对 v0-v3 loop 的引用；grep 确认零跨 loop slug 引用 |
| Zettelkasten 原子性 | **PASS** | 35 标题连词疑似中 34 通过实质审查；19 多源卡全部为 comparison 类型（预期行为）；6 长卡体中 2 张（knowledge-compounding 58 行、my-llm-wiki-implementation 58 行）偏 hub-page 但内容连贯 |
| 源忠实 + 可溯源 | **PARTIAL** | 400+ `[^src-*]` 脚注零伪造；但 15 张 comparison 卡零直接源脚注，2 处上下文泄露，2 处数值混淆，topic-isolation 有断裂 `[^card-1]` |
| 永不删除 | **PASS** | 280 张卡全部 `status: accepted`；无 deleted/rejected 状态 |
| grep-friendly metadata | **PARTIAL** | 所有 14 必填字段齐全；id==filename 全部通过；但 `related` 字段的 YAML 序列化缺陷使 70 张卡的元数据在解析后与文件内容不一致 |
| 材料穷尽 | **PARTIAL** | 27 个源中 20+ 个覆盖良好；4 个源存在核心贡献级缺口（冲突路由矩阵、Queue Manager、多模态任务、agent 攻击结果） |
| 中文输出 | **PASS** | 280 张卡正文均为中文；schema keys/slugs/paths 保持英文 |
| Governance 实际执行 | **PARTIAL** | 280 张 JJ 文件全部存在；259 非 comparison 卡全部有 src 脚注；184 脚注链接全部解析；但约 15 个 JJ 文件格式不符合 justification_journal.v1 schema，comparison 卡生成流水线未执行标准 creation event 写入 |

## 3. 隐式担忧判定

| 担忧 | 判定 | 证据 |
|---|---|---|
| Agent drift | **NOT CONFIRMED** | 280 张卡中无注入框架或公式化填充；2 张卡有 editorial 段落超出源文本（tree-sitter-code-extraction 的 "意义" 段、weight-internalization-aspiration 的 "规模瓶颈" 推断）但均为合理推论而非幻觉；comparison-access-vs-content-memory-tiering 引入四象限框架属于 agent 合成分析，已通过 card 类型（distinction）容许 |
| Context leakage | **CONFIRMED (1 true leakage + 1 provenance gap; 1 original finding was false positive from grep limitation)** | comparison-corrective-vs-servant-agency 引入 '确认优先规则'（true leakage：源自 cognitionus-llm-wiki-guide 经 confirm-first-skill-capture 渗入）和 '参与程度谱系'（false positive：Karpathy gist 第 37 行有明确描述）；comparison-multihop-runtime-vs-compiletime 引入 GraphRAG map-reduce 描述（provenance gap：可 3-hop 溯源但缺 footnote 锚定） |
| Over-engineering | **NOT CONFIRMED** | 卡片体系以 markdown + YAML frontmatter 为基础，无向量数据库、无嵌入层、无复杂检索管线；cross-link 通过 slug 引用而非 ID 系统 |
| Early-stop | **INCONCLUSIVE** | 4 个源存在核心贡献级缺口，但 280 张卡覆盖 27 个源的主要论点；248/280 张卡时间戳为同一批次 (2026-06-05T10:00:00+08:00)，提示可能存在批量生成后未回补的情况 |
| Token waste | **NOT CONFIRMED** | 6 张长卡体 (>45 行) 中仅 knowledge-compounding 和 my-llm-wiki-implementation 有 hub-page 倾向；其余卡片体量适中 |
| Cluster count targets | **NOT CONFIRMED** | 8 个 created_time 聚类为批次生成的自然产物，无证据表明为凑数；19 张 comparison 卡均有实质区分点 |

## 4. 全部发现（按 severity 排序）

### CRITICAL

| # | Topic | Finding | Cards | Fix Effort |
|---|---|---|---|---|
| C1 | YAML related 字段全损 | `related: []` 后跟缩进项，解析结果为空数组，全部 cross-link 丢失 | conditional-trigger-stealth-design, dynamic-agentic-roi, idea-file-paradigm, poisonedrag-text-decomposition, rag-knowledge-database-attack-surface, rag-parametric-bias-failure, rag-retrieval-generation-dual-condition, schema-template-verticals, topic-concentration-compounding, tree-sitter-code-extraction, weight-internalization-aspiration (11 张) | 低：脚本批量修复，将缩进项合并入行内数组 |
| C2 | YAML related 字段部分损 | `related: [a,b]` 后跟缩进项 `- c`，解析时 c 被丢弃 | 59 张卡（详见 mechanical_report.json 的 dual_related_format 列表） | 低：同 C1 脚本修复 |

### MAJOR

| # | Topic | Finding | Cards | Fix Effort |
|---|---|---|---|---|
| M1 | 上下文泄露 | 引入源文本中不存在的概念 '确认优先规则' 和 '参与程度谱系' | comparison-corrective-vs-servant-agency | 中：需确认概念来源，添加脚注或删除段落 |
| M2 | 上下文泄露 | GraphRAG map-reduce 描述不属于任何 source_id | comparison-multihop-runtime-vs-compiletime | 中：添加 arxiv-graphrag 到 source_ids 并补脚注，或删除该段 |
| M3 | 数值混淆 | 73% gap 与 42.1 best-RAG 并置，暗示 (92.6-42.1)/92.6=73%，实际 73% 对应 long-context 25.0 | temporal-reasoning-difficulty | 低：修正文字，区分两个比较基准 |
| M4 | 数值混淆 | 同 M3，相同错误独立出现 | locomo-five-reasoning-types | 低：同 M3 |
| M5 | 断裂引用 | `related` 引用 graphrag-extraction-attack-surface，该卡不存在 | graphrag-knowledge-poisoning-attack | 低：移除或创建目标卡 |
| M6 | 断裂引用 | `related` 引用 memgpt-queue-manager，该卡不存在 | memgpt-main-context-structure, virtual-context-management | 中：创建 memgpt-queue-manager 卡（论文 Section 2.2 有材料） |
| M7 | 断裂脚注 | 正文引用 `[^card-1]` 但脚注节无定义 | topic-isolation | 低：补充脚注定义或移除引用 |
| M8 | 数值超源 | 声称 'Llama 3.1 70B 下降高达 66%' 但源文本 3_benchmark.tex 写 '30% to 60%' | long-term-memory-accuracy-gap | 低：修正为 60% 或注明数据来自图表 |
| M9 | 脚注伪引 | `[^src-2]` 将图表数据包装为源文本引用格式 | long-term-memory-accuracy-gap | 低：改写脚注标注为 "图表数据" |
| M10 | 源验证盲区 | 10 张 knowledge-compounding 卡引用 source.pdf，PDF 不可提取文本，无法做 section 级验证 | knowledge-compounding, cost-independence-assumption, dynamic-agentic-roi, compounding-cost-honesty, token-capital-goods, capitalized-latency, invest-harvest-cycle, supply-demand-token-dividend, search-write-back, topic-concentration-compounding | 高：需安装 pdftotext 或使用 PyMuPDF 重新验证 |
| M11 | 材料穷尽缺口 | 冲突路由矩阵 (Section 5.0) 是论文核心规范贡献，含 7 行路由规则和阿谀覆写，无卡捕获 | (SOURCE: arxiv-memory-as-metabolism) | 中：创建新卡 |
| M12 | Cross-link 孤岛 | 5 张卡 related 真空且无 YAML bug：zero-runtime-dependency, topic-isolation, thesis-driven-research, multi-platform-skill-portability, parallel-multi-agent-research | 5 张卡 | 低：补充 related 链接 |
| M13 | 源脚注引用注释区 | `[^src-2]` 引用 LaTeX 注释区（COMMENTED-OUT）文本而非正式发表文本 | open-source-vs-proprietary-context-discrimination | 低：替换为正式文本的等价表述 |

### MINOR

| # | Topic | Finding | Cards | Fix Effort |
|---|---|---|---|---|
| m1 | Comparison 卡零源脚注 | source_ids 列出来源但正文仅有 `[^card-*]`，无直接 `[^src-*]` | comparison-rag-eval-reference-dependency, comparison-cognitive-memory-metaphors, comparison-multihop-runtime-vs-compiletime, comparison-wiki-rag-positioning-spectrum, comparison-full-context-task-divergence, comparison-circularity-vs-entrenchment, comparison-detection-blind-spot-under-entrenchment, comparison-grunt-work-outsourceability, comparison-infrastructure-vs-cognitive-limits, comparison-lossy-compilation-vs-non-lossy-preservation, comparison-incremental-vs-batch-ingest, comparison-compression-vs-transformation-granularity, comparison-locomo-vs-longmemeval-taxonomy (~15 张) | 中：为每张补 1-2 条直接源脚注，或从 source_ids 移除未直接引用的来源 |
| m2 | JJ 格式不一致 | JJ 文件缺少 `## creation` 事件头或使用非标模板 | comparison-corrective-vs-servant-agency, comparison-grunt-work-outsourceability, comparison-circularity-vs-entrenchment, comparison-detection-blind-spot-under-entrenchment, comparison-compression-vs-transformation-granularity, comparison-full-context-task-divergence, comparison-locomo-vs-longmemeval-taxonomy, comparison-posthoc-vs-builtin-provenance, comparison-runtime-paging-vs-lifecycle-archiving, comparison-rag-eval-reference-dependency, comparison-infrastructure-vs-cognitive-limits, comparison-wiki-rag-positioning-spectrum, comparison-multihop-runtime-vs-compiletime (~15 张) | 低：脚本统一补 creation event 头 |
| m3 | Editorial 超源 | 正文包含超出脚注覆盖范围的分析性推断，合理但未标注为编辑推论 | source-faithfulness-risk ('有损变换'), cross-session-continuity (零状态声明), comparison-incremental-vs-batch-ingest ('去重机制'), tree-sitter-code-extraction ('确定性'段), weight-internalization-aspiration ('规模瓶颈'), ai-rmf-voluntary-trustworthiness ('治理工具演化'), idea-file-paradigm ('fork 类比'), hn-architectural-pattern-reception (Licklider 归因) | 低：为每处添加 '编者注' 标记或补脚注 |
| m4 | 脚注覆盖不精确 | 正文声明由脚注支持，但脚注引用的文本范围窄于声明 | namespace-key-memory-model (tuple 格式/IndexConfig), context-scaling-diminishing-returns ('lost in the middle' 细节), llm-wiki-mainstream-prerequisites (Notion+Obsidian 愿景), observation-based-memory-representation ('5% improvement' vs 31% 实际) | 低：扩展脚注引用范围或拆分为多条脚注 |
| m5 | 别名过于笼统 | 别名词过于通用，搜索消歧价值低 | companion-object-model ('系统模型'), schema-template-verticals ('领域模板'/'domain-specific templates'), comparison-wiki-rag-positioning-spectrum ('positioning spectrum'), review-involvement-spectrum ('supervision level'), topic-concentration-compounding ('可用性鸿沟解释'), weight-internalization-aspiration ('合成数据微调'), intentional-abstraction ('modularity'), rag-wiki-synthesis-distinction ('RAG区分') | 低：替换为更具体的别名 |
| m6 | 材料穷尽缺口（中等） | 源论文的可操作内容未被捕获 | arxiv-memgpt Queue Manager (Section 2.2), arxiv-locomo 多模态对话生成任务, arxiv-poisonedrag LLM agent 攻击 + FEVER, arxiv-mem0 实体提取管线 + 26% 改进, arxiv-wicer 文档数量交叉阈值, openaitoolshub-six-months 复利波及量化数据 + 2 个 pitfall, robin-cartier ~200页/~100K 规模天花板, clawhub kb_lint 细节, anthemcreation 成本数据表 | 高：需为每个缺口创建新卡 |
| m7 | 原子性边界 | 标题连词连接可分离概念 | graphrag-community-hierarchy (检测 vs 摘要), source-faithfulness-risk (风险 vs 锚点), query-and-answer-filing (查询 vs 归档), rag-parametric-bias-failure (两种失效模式) | 低：重命名或拆卡 |
| m8 | 数值精度 | 声称 'GPT-5.2 具有最高 TSR' 但 Qwen3.5-122B 并列 | model-capability-security-disconnect | 低：改为 '并列最高' |
| m9 | Drift: agent 合成分析 | comparison 卡引入源文本未有的四象限框架 | comparison-access-vs-content-memory-tiering | 低：标注为编辑合成 |
| m10 | Drift: 未注脚跨卡概念 | 设计启示段引用其他卡概念但无 `[^card-*]` 脚注 | comparison-detection-blind-spot-under-entrenchment, comparison-corrective-vs-servant-agency | 低：补 card-ref 脚注 |

### INFO

| # | Topic | Finding | Cards |
|---|---|---|---|
| i1 | 时间戳聚类 | 248/280 张卡 created_time 为 2026-06-05T10:00:00+08:00，批量生成特征明显 | GLOBAL |
| i2 | 长卡体 | 6 张卡 >45 行，其中 knowledge-compounding 和 my-llm-wiki-implementation 偏 hub-page | 6 张卡 |
| i3 | 材料穷尽缺口（低优） | 背景性/实现细节级内容未捕获（wikibase Sitelinks/DataValue types、LLM inline-image workaround、DRAGON retriever、MemGPT LongMemEval 失败、future work 方向等） | 多个源 |
| i4 | 概念名称合成 | text-perturbation-amplification 的 '微扰放大效应' 是 agent 合成名称，源文本无此术语 | text-perturbation-amplification |

## 5. 跨 Topic 关联分析（系统性问题识别）

### 5.1 YAML related 字段序列化缺陷 (C1+C2+M12)

这是本轮最严重的系统性问题，由 mechanical-audit-agent 首次发现，后被 6 个独立 agent 在不同卡片子集上反复确认。

- **根因推断：** 卡片生成管线在写入 `related` 字段时，先输出行内数组语法 `related: [a, b]`，随后又以缩进列表形式追加额外项。这很可能是两个不同步骤（初始生成 vs. cross-link 补充）写入同一字段但未合并。
- **影响面：** 70 张卡 (25%)，其中 11 张完全丢失、59 张部分丢失、另有 5 张真空。合计 75 张卡的 cross-link 不可靠。
- **修复方案：** 单次 Python 脚本即可修复全部 70 张——解析行内数组和缩进项，去重合并后以标准 YAML 列表重写。

### 5.2 Comparison 卡生成管线质量差异 (m1+m2+M1+M2)

约 15 张 comparison/distinction 卡集中出现三类问题：
1. 零直接源脚注（仅靠 `[^card-*]` 间接引用）
2. JJ 文件格式不符合 justification_journal.v1 schema
3. 2 例上下文泄露恰好都在 comparison 卡中

**推断：** Comparison 卡由独立的合成步骤生成，该步骤的模板缺少 `[^src-*]` 脚注要求和标准 JJ creation event 写入。

### 5.3 long-term-memory-accuracy-gap 多重问题叠加

该卡同时命中 M3（数值混淆 73%）、M8（66% 超源）、M9（脚注伪引），是单卡问题密度最高的案例，需优先整改。

### 5.4 knowledge-compounding 源验证盲区 (M10)

10 张卡引用的 source.pdf 无法文本提取。虽然摘要级一致性和内部算术校验全部通过，但 section 级引用（如 "Section 3.4 P10" 的具体引文）未经验证。这 10 张卡的忠实性判定为 "passed with caveat"，不可与经 grep 验证的卡片等同对待。

### 5.5 memgpt-queue-manager 幽灵卡

2 张卡在 `related` 字段引用 memgpt-queue-manager，该卡在 cards/ 目录不存在。同时 arxiv-memgpt 的 Section 2.2 Queue Manager 被标记为材料穷尽缺口。推断：该卡被规划但未创建。

## 6. 需立即修复的卡列表

按修复优先级排列：

### P0: 脚本批量修复（影响 70 张卡）

运行 YAML related 字段修复脚本，合并行内数组与缩进项，消除 C1+C2。

### P1: 手动修复（影响 7 张卡，每张 <5 分钟）

| 卡 | 修复内容 |
|---|---|
| temporal-reasoning-difficulty | 修正 73% gap 的比较基准说明 |
| locomo-five-reasoning-types | 同上 |
| long-term-memory-accuracy-gap | 修正 66%→60%、改写 [^src-2] 为图表数据标注 |
| topic-isolation | 补充 [^card-1] 脚注定义 |
| model-capability-security-disconnect | '最高' 改为 '并列最高' |
| open-source-vs-proprietary-context-discrimination | 替换注释区引用为正式文本 |
| graphrag-knowledge-poisoning-attack | 移除不存在的 related 目标或更正 slug |

### P2: 内容修复（影响 2 张卡，每张 10-15 分钟）

| 卡 | 修复内容 |
|---|---|
| comparison-corrective-vs-servant-agency | 删除或注明 '确认优先规则'/'参与程度谱系' 段落的来源 |
| comparison-multihop-runtime-vs-compiletime | 为 GraphRAG 段落添加 arxiv-graphrag 到 source_ids 并补脚注，或删除该段 |

### P3: 补建卡片（影响知识库完整度，每张 15-30 分钟）

| 缺失卡 | 源 | 理由 |
|---|---|---|
| memgpt-queue-manager | arxiv-memgpt Section 2.2 | 2 张卡的 related 断裂引用指向它 |
| conflict-routing-matrix（暂定） | arxiv-memory-as-metabolism Section 5.0 | 论文核心规范贡献，含阿谀覆写规则 |

### P4: Cross-link 孤岛补链（影响 5 张卡）

为 zero-runtime-dependency, topic-isolation, thesis-driven-research, multi-platform-skill-portability, parallel-multi-agent-research 补充 related 链接。

## 7. 建议（按 impact/effort 排序）

| 优先级 | 建议 | Impact | Effort | 说明 |
|---|---|---|---|---|
| 1 | **修复 YAML related 字段** | 极高（25% 卡片数据恢复） | 低（单次脚本） | 编写 Python 脚本：读取每张卡的 frontmatter，检测行内数组+缩进项混合格式，合并去重后以标准 `related: [slug1, slug2, ...]` 或 block-list 重写。run_audit.py 已就绪，可扩展。 |
| 2 | **修复 P1 手动修复列表** | 高（消除全部 major 忠实性问题） | 低（7 张卡 x <5 分钟） | 逐张按上表修正 |
| 3 | **统一 comparison 卡生成模板** | 中（防止未来同类问题） | 中 | 在 comparison 卡生成流水线中增加：(a) 至少 1 条 `[^src-*]` 脚注检查；(b) JJ 使用标准 justification_journal.v1 模板；(c) source_ids 仅列直接引用的来源 |
| 4 | **补建 2 张缺失卡** | 中（消除断裂引用 + 核心缺口） | 中（2 x 15-30 分钟） | memgpt-queue-manager, conflict-routing-matrix |
| 5 | **安装 pdftotext 后重验 10 张 KC 卡** | 中（消除验证盲区） | 中 | 一次性安装 poppler-utils，对 knowledge-compounding 源 PDF 执行 section 级脚注验证 |
| 6 | **清理笼统别名** | 低（改善检索精度） | 低 | 替换约 10 个过于通用的 alias（'系统模型' → '伴侣系统模型', '领域模板' → 'LLM Wiki 领域模板' 等） |
| 7 | **为 comparison 卡补直接源脚注** | 低-中（改善审计链） | 高（~15 张卡 x 10 分钟） | 每张 comparison 卡至少补 1 条直接引用其 source_ids 列出来源的 `[^src-*]` 脚注 |
| 8 | **补建 m6 材料穷尽缺口卡片** | 低（增量覆盖） | 高（~10 张新卡） | 按 m6 列表逐个评估是否值得独立建卡；优先处理有量化数据的条目（openaitoolshub 复利波及、robin-cartier 规模天花板、anthemcreation 成本表） |

## 8. 审计方法论修正与遗留 TODO

### 8.1 grep-based 审计的局限性（lessons learned）

本轮审计的源忠实性检查以 grep exact-quote matching 为主要手段。深入调查后发现此方法存在两类偏差：

- **False Positive（假阳性）**：agent 对源材料的合理意译被 grep 判定为 "leakage"。Case 1 中「参与程度谱系」实际是 Karpathy gist 第 37 行描述的参与程度从深度介入到低监督批量的合理概括，但因措辞不同导致 grep 未命中。
- **False Negative 风险（假阴性）**：如果 agent editorial 恰好使用了源文本中出现的词汇，grep 会误判为 "supported"，导致真实的 editorial 注入无法被捕获。

**修正后的审计协议（TODO：在下一次审计中落实）**：
- grep 未命中时，不直接判定为 leakage，而是标记为 "suspect — needs full-text review"
- 对 suspect 项，派 agent 读取完整源材料原文进行语义级验证
- 审计报告的 findings 必须区分 "grep-verified"（quote 逐字匹配）和 "semantic-verified"（agent 读原文确认为合理意译）两个置信度级别

### 8.2 Context Leakage 判定修正

原报告判定 2 例 CONFIRMED leakage，经深入调查修正如下：

| 原判定 | 卡片 | 概念 | 修正后判定 | 理由 |
|--------|------|------|-----------|------|
| leakage | comparison-corrective-vs-servant-agency | 参与程度谱系 | **False Positive** | Karpathy gist 第 37 行有明确描述，卡片是合理意译 |
| leakage | comparison-corrective-vs-servant-agency | 确认优先规则 | **True Leakage** | 两个声明源均无此概念；实际来源是 cognitionus-llm-wiki-guide（经 sibling card confirm-first-skill-capture 渗入） |
| leakage | comparison-multihop-runtime-vs-compiletime | GraphRAG map-reduce | **Provenance Gap** | 事实可通过 KB 卡网络 3-hop 溯源（→ graphrag-map-reduce-query），但本卡缺少 [^card-*] footnote 锚定 + "第三条中间路径" 为 agent editorial |

修正后隐式担忧判定：Context leakage → **CONFIRMED (1 true case + 1 provenance gap)**，非原报告的 "2 cases"。

### 8.3 遗留 TODO

- [ ] 对 15 张 comparison 卡执行 semantic-level 源忠实验证（本轮仅覆盖 2 张）
- [ ] 为审计脚本增加 "suspect — needs review" 中间状态，替代 grep 的二元 supported/unsupported 判定
- [ ] 建立 comparison 卡生成模板的 footnote 硬约束：每个 body claim 必须有 [^card-*] 或 [^src-*] 锚定
- [ ] 调查 true leakage 的执行链路：governance workflow 的 comparison 卡生成 agent 是否被允许读取超出 cluster 范围的卡（详见 leakage trace report）
