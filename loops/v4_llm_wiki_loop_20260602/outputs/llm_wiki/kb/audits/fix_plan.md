---
schema: fix_plan.v1
date: 2026-06-07
audit_sources:
  - v4_comprehensive_audit.md
  - cluster_damage_assessment.md
  - leakage_trace_corrective_vs_servant.md
total_fixes: 22
categories:
  script: 3
  targeted: 8
  agent: 11
cards_total: 280
cards_affected_estimate: 145
---

# v4 KB Fix Plan

## 执行摘要

基于三份审计文档（综合审计报告、集群损伤评估、泄漏追踪报告）的全部发现，本计划整合 22 项修复任务，覆盖约 145 张受影响卡片。

**最严重的问题是 YAML `related` 字段的双格式序列化缺陷**（69 张卡，24.6%），由 governance rescue commit (b26dafc) 的 derive-related 步骤引入——该步骤对 block-style `related:` 字段执行单行替换但未删除后续缩进行。此问题为纯机械修复。

**其次是源忠实性问题**：2 处数值混淆、1 处上下文泄漏（确认优先规则）、1 处溯源缺口（GraphRAG map-reduce）、1 处超源数值（66%→60%）、1 处脚注引用注释区文本、1 处断裂脚注。这些均为已知修复方案的定向编辑。

**最大规模的 agent 工作是 comparison 卡的源脚注补全**（21 张卡零 `[^src-*]`）和跨领域桥梁链接建设（security↔memory 缺 ~20 条、wiki→governance 缺 ~15 条）。

执行顺序：**A（脚本）→ B（定向编辑）→ C（agent 判断）**，确保脚本修复不覆盖后续 agent 写入。

---

## Category A: 脚本修复（无需 LLM 判断）

### A1: YAML `related` 双格式修复

- **审计来源**: C1 + C2（综合审计）、预测 4（集群损伤评估）
- **影响**: 69 张卡（24.6%）
  - 11 张完全丢失：`related: []` 后跟缩进项，解析结果为空数组
  - 58 张部分丢失：`related: [a, b]` 后跟缩进项 `- c`，解析时 c 被丢弃
- **根因**: governance rescue commit (b26dafc) 的 derive-related 步骤将 `related:` 行替换为 `related: [item1, item2]`，但未删除 block-style 的后续 `- item` 行
- **方法**: Python 脚本，YAML parse + rewrite
- **具体逻辑**:

```python
import re, os

for card_file in glob('cards/*.md'):
    text = read(card_file)
    front, body = split_frontmatter(text)

    # 1. 提取 inline 数组值
    inline_match = re.search(r'related:\s*\[(.*?)\]', front)
    inline_items = parse_csv(inline_match.group(1)) if inline_match else []

    # 2. 提取后续缩进 `- item` 行
    block_items = extract_block_items_after_related(front)

    # 3. 合并去重
    merged = deduplicate(inline_items + block_items)

    # 4. 删除旧 related 行（含 inline 行 + 所有后续缩进行）
    # 5. 写入标准格式：related: [slug1, slug2, slug3]
    front = replace_related_field(front, merged)

    write(card_file, front + body)
```

- **预期结果**: 69 张卡的 `related` 字段恢复完整，所有双格式消除
- **验证**: 对修复后的 280 张卡执行 `yaml.safe_load()`，确认零解析异常；对比修复前后 related 项数（预期：仅增不减）

### A2: JJ 文件格式规范化

- **审计来源**: m2（综合审计）
- **影响**: 13 个 JJ 文件缺少标准 `## creation` 事件头
- **受影响文件**:
  - comparison-circularity-vs-entrenchment.md
  - comparison-compression-vs-transformation-granularity.md
  - comparison-corrective-vs-servant-agency.md
  - comparison-detection-blind-spot-under-entrenchment.md
  - comparison-full-context-task-divergence.md
  - comparison-grunt-work-outsourceability.md
  - comparison-infrastructure-vs-cognitive-limits.md
  - comparison-locomo-vs-longmemeval-taxonomy.md
  - comparison-multihop-runtime-vs-compiletime.md
  - comparison-posthoc-vs-builtin-provenance.md
  - comparison-rag-eval-reference-dependency.md
  - comparison-runtime-paging-vs-lifecycle-archiving.md
  - comparison-wiki-rag-positioning-spectrum.md
- **方法**: 脚本在 JJ 文件 frontmatter 后插入标准 creation event 头

```python
# 在 frontmatter 后、现有内容前插入：
CREATION_HEADER = """## creation
- event: card_created
  agent: governance-comparison-pipeline
  date: 2026-06-05
  note: comparison/distinction 卡由 governance workflow 生成
"""
```

- **预期结果**: 280 个 JJ 文件全部符合 justification_journal.v1 schema

### A3: 断裂 `related` 引用清理

- **审计来源**: M5 + M6（综合审计）
- **影响**: 3 条断裂引用，涉及 3 张卡
- **具体引用**:

| 来源卡 | 引用目标 | 目标状态 |
|--------|---------|---------|
| graphrag-knowledge-poisoning-attack | graphrag-extraction-attack-surface | 不存在 |
| memgpt-main-context-structure | memgpt-queue-manager | 不存在（待 C7 创建） |
| virtual-context-management | memgpt-queue-manager | 不存在（待 C7 创建） |

- **方法**:
  - graphrag-extraction-attack-surface：脚本从 related 中移除该 slug（无需创建，rag-knowledge-database-attack-surface 已覆盖该概念）
  - memgpt-queue-manager：**暂保留**，待 C7 创建 memgpt-queue-manager 卡后自动消除。若 C7 不执行，则脚本移除
- **预期结果**: 断裂引用降至 0

---

## Category B: 定向卡片编辑（特定卡，已知修复方案）

### B1: 数值混淆修复（73% gap 比较基准）

- **审计来源**: M3 + M4（综合审计）
- **卡片**: temporal-reasoning-difficulty, locomo-five-reasoning-types
- **问题**: 73% gap 与 42.1 best-RAG 并置，暗示 (92.6-42.1)/92.6=73%，但实际 73% 对应 long-context 25.0 而非 best-RAG 42.1
- **具体修改**:

temporal-reasoning-difficulty:
```
old: 在时间推理维度上，best-RAG 仅达到 42.1 分，与人类 92.6 分存在约 73% 的差距
new: 在时间推理维度上存在显著差距：best-RAG 得分 42.1（与人类差距 54.5%），而 long-context 模型仅得 25.0（与人类差距 73.0%）
```

locomo-five-reasoning-types:
```
old: (同样的 73% 混淆表述)
new: (同样的修正，区分两个比较基准)
```

- **预期结果**: 数值引用与 LoCoMo 论文 Table 2 一致

### B2: long-term-memory-accuracy-gap 多重修复

- **审计来源**: M8 + M9（综合审计）、5.3 跨 Topic 关联分析
- **卡片**: long-term-memory-accuracy-gap（单卡问题密度最高）
- **问题 1 (M8)**: 声称 "Llama 3.1 70B 下降高达 66%" 但源文本 3_benchmark.tex 写 "30% to 60%"
- **问题 2 (M9)**: `[^src-2]` 将图表数据包装为源文本引用格式

具体修改:
```
old: Llama 3.1 70B 下降高达 66%
new: Llama 3.1 70B 下降幅度在 30%-60% 之间
```

```
old: [^src-2]: 源文本: "..."（引用格式）
new: [^src-2]: 图表数据（Figure X / Table Y）：...（标注为图表数据而非源文本引用）
```

### B3: topic-isolation 断裂脚注修复

- **审计来源**: M7（综合审计）、预测 2 证据（集群损伤评估）
- **卡片**: topic-isolation
- **问题**: 正文引用 `[^card-1]` 但脚注节无定义。集群损伤评估显示该脚注原本指向 llm-wiki-pattern，证明交叉链接流程启动但未完成
- **具体修改**: 补充脚注定义

```
new: [^card-1]: [LLM Wiki 模式](llm-wiki-pattern.md) -- 本卡讨论主题隔离的质量风险，该卡定义了 LLM Wiki 的整体模式框架
```

- 同时将 topic-isolation 添加到 related 字段（配合 C1 孤儿卡补链）

### B4: model-capability-security-disconnect 精度修复

- **审计来源**: m8（综合审计）
- **卡片**: model-capability-security-disconnect
- **问题**: 声称 "GPT-5.2 具有最高 TSR" 但 Qwen3.5-122B 并列

```
old: GPT-5.2 具有最高 TSR
new: GPT-5.2 与 Qwen3.5-122B 并列最高 TSR
```

### B5: open-source-vs-proprietary-context-discrimination 注释区修复

- **审计来源**: M13（综合审计）
- **卡片**: open-source-vs-proprietary-context-discrimination
- **问题**: `[^src-2]` 引用 LaTeX 注释区（COMMENTED-OUT）文本而非正式发表文本
- **具体修改**: 定位正文中被注释区引用支持的声明，替换为正式发表文本中的等价表述；若无等价表述，删除该声明并标注

### B6: comparison-corrective-vs-servant-agency 泄漏修复

- **审计来源**: M1（综合审计）、leakage_trace 全文
- **卡片**: comparison-corrective-vs-servant-agency
- **问题**: 第 27 行裸名引用「确认优先规则」，概念来自 cognitionus-llm-wiki-guide 经 confirm-first-skill-capture 渗入，无脚注锚定
- **附注**: 同句「参与程度谱系」经调查为 false positive（Karpathy gist 第 37 行有明确描述），无需修复
- **具体修改（两选一）**:

方案 A（首选：补脚注归因）:
```
old: 确认优先规则和参与程度谱系允许系统在不同场景下调节 LLM 的自主程度
new: 确认优先规则[^card-3]和参与程度谱系允许系统在不同场景下调节 LLM 的自主程度

(新增脚注)
[^card-3]: [确认优先的技能捕获规则](confirm-first-skill-capture.md) -- 本卡讨论纠偏权与执行权的分歧，该卡提供一种具体的门控机制（确认优先规则）来调和自主程度
```

方案 B（删除概念引用）:
```
old: 这一分歧在实践中通过门控机制得到部分调和：确认优先规则和参与程度谱系允许系统在不同场景下调节 LLM 的自主程度
new: 这一分歧在实践中通过门控机制得到部分调和：参与程度谱系允许系统在不同场景下调节 LLM 的自主程度
```

### B7: comparison-multihop-runtime-vs-compiletime 溯源修复

- **审计来源**: M2（综合审计）、8.2 修正判定（provenance gap）
- **卡片**: comparison-multihop-runtime-vs-compiletime
- **问题**: GraphRAG map-reduce 描述不属于任何声明的 source_id；事实可通过 KB 卡网络 3-hop 溯源（→ graphrag-map-reduce-query），但缺少 `[^card-*]` 脚注锚定；"第三条中间路径" 为 agent editorial
- **具体修改**:
  1. 为 GraphRAG 段落添加 `[^card-N]` 指向 graphrag-map-reduce-query
  2. 将 "第三条中间路径" 标注为编者合成分析
  3. 可选：将 arxiv-graphrag 添加到 source_ids（取决于是否通过卡链间接引用即可）

### B8: graphrag-knowledge-poisoning-attack 断裂引用修复

- **审计来源**: M5（综合审计）
- **卡片**: graphrag-knowledge-poisoning-attack
- **问题**: `related` 引用 graphrag-extraction-attack-surface，该卡不存在
- **具体修改**: 从 `related` 中移除 graphrag-extraction-attack-surface。检查是否应替换为 rag-knowledge-database-attack-surface（概念最近邻）

---

## Category C: Agent 判断修复

### C1: 孤儿卡交叉链接

- **审计来源**: M12（综合审计）、预测 2（集群损伤评估）
- **卡片**: 5 张
  1. zero-runtime-dependency（0 出站 + 0 入站）
  2. topic-isolation（0 出站 + 0 入站，B3 已修复断裂脚注）
  3. thesis-driven-research（0 出站 + 0 入站）
  4. parallel-multi-agent-research（0 出站 + 0 入站）
  5. multi-platform-skill-portability（0 出站 + 1 入站，来自 mcp-tool-skill-layering）
- **全部来自 llm-wiki-net 来源**，证明 derive-related 步骤系统性跳过了该组卡
- **方法**: agent 读取每张卡的 canonical_concept + summary + tags，在全部 280 张卡中 grep 匹配候选，精选 3-5 条最有价值链接写入 `related` 字段
- **每张卡预期链接数**: 3-5 条
- **预期新增链接**: 15-25 条，消除信息孤岛

### C2: 跨领域桥梁链接建设

- **审计来源**: 预测 6（集群损伤评估）、因果链 4
- **问题**: 纯跨领域链接仅占 13.4%（101/753），同前缀密度是跨前缀的 5.7-7.5 倍
- **高优先级桥梁**:

| 领域对 | 现有链接 | 预估缺失 | 具体案例 |
|--------|---------|---------|---------|
| security↔memory | 2 条 | ~20 条 | 17 张 security 卡 + 71 张 memory 卡，几乎无交叉 |
| wiki→governance | 0 条 | ~15 条 | 23 张 wiki 卡提及审计/治理概念但零链接至 governance 卡 |
| eval↔RAG | 稀疏 | ~10 条 | LoCoMo 评估卡 ↔ RAG 攻击/防御卡 |

- **方法**:
  1. 对每对领域，提取各自卡片中提及对方领域概念但未链接的案例
  2. 候选对输入 agent，判断是否值得建立 related 链接
  3. 强制跨领域配额：确保补链后每对高优领域至少 5 条双向链接
- **预期结果**: 新增 35-45 条跨领域链接

### C3: Comparison 卡源脚注补全

- **审计来源**: m1（综合审计）、5.2 Comparison 卡管线质量差异
- **影响**: 21 张 comparison/distinction 卡零直接 `[^src-*]` 脚注
- **卡片列表**:
  - comparison-access-vs-content-memory-tiering
  - comparison-circularity-vs-entrenchment
  - comparison-cognitive-memory-metaphors
  - comparison-compression-vs-transformation-granularity
  - comparison-corrective-vs-servant-agency（B6 已处理泄漏问题）
  - comparison-detection-blind-spot-under-entrenchment
  - comparison-full-context-task-divergence
  - comparison-grunt-work-outsourceability
  - comparison-incremental-vs-batch-ingest
  - comparison-infrastructure-vs-cognitive-limits
  - comparison-introspective-vs-environmental-stress-testing
  - comparison-locomo-vs-longmemeval-taxonomy
  - comparison-lossy-compilation-vs-non-lossy-preservation
  - comparison-multihop-runtime-vs-compiletime（B7 已处理溯源）
  - comparison-posthoc-vs-builtin-provenance
  - comparison-rag-eval-reference-dependency
  - comparison-recency-invalidation-vs-pressure-promotion
  - comparison-replace-vs-optimize-rag
  - comparison-runtime-paging-vs-lifecycle-archiving
  - comparison-storage-vs-retrieval-compression
  - comparison-wiki-rag-positioning-spectrum
- **方法**: agent 读取每张 comparison 卡的 source_ids，定位源材料中支持该卡核心 tension 的段落，为每张卡补 1-2 条 `[^src-*]` 直接源脚注。若 source_ids 中列出的来源确实无直接引用，则从 source_ids 中移除
- **预期结果**: 21 张卡均至少有 1 条 `[^src-*]` 脚注，source_ids 语义恢复为"直接引用的来源"

### C4: 别名精细化

- **审计来源**: m5（综合审计）
- **影响**: ~10 个过于笼统的别名，涉及 ~8 张卡
- **具体修改**:

| 卡 | 当前别名 | 建议替换 |
|----|---------|---------|
| companion-object-model | 系统模型 | 伴侣对象系统模型 |
| schema-template-verticals | 领域模板 / domain-specific templates | LLM Wiki 领域垂直模板 |
| comparison-wiki-rag-positioning-spectrum | positioning spectrum | Wiki-RAG 定位谱系 |
| review-involvement-spectrum | supervision level | 人类审批参与程度 |
| topic-concentration-compounding | 可用性鸿沟解释 | 主题集中度复利与可用性鸿沟 |
| weight-internalization-aspiration | 合成数据微调 | 权重内化愿景（合成数据微调路径） |
| intentional-abstraction | modularity | 意向性抽象（LLM Wiki 模块化） |
| rag-wiki-synthesis-distinction | RAG区分 | RAG 与 Wiki 合成路径区分 |

- **方法**: agent 读取每张卡的上下文，判断最具消歧价值的别名表述
- **预期结果**: 每个别名在 KB 中搜索时具有唯一或高区分度的匹配

### C5: Editorial 超源标注

- **审计来源**: m3（综合审计）
- **影响**: ~8 张卡包含超出脚注覆盖范围的分析性推断
- **卡片列表**:

| 卡 | 超源内容 |
|----|---------|
| source-faithfulness-risk | "有损变换" 推论 |
| cross-session-continuity | "零状态" 声明 |
| comparison-incremental-vs-batch-ingest | "去重机制" 推断 |
| tree-sitter-code-extraction | "确定性" 段落 |
| weight-internalization-aspiration | "规模瓶颈" 推断 |
| ai-rmf-voluntary-trustworthiness | "治理工具演化" 推论 |
| idea-file-paradigm | "fork 类比" |
| hn-architectural-pattern-reception | Licklider 归因 |

- **方法**: 为每处添加 `[编者注]` 标记或补充 `[^src-*]` 脚注（若源材料中有支持内容）
- **预期结果**: 读者能区分"源忠实内容"与"编辑合理推论"

### C6: 脚注覆盖范围修正

- **审计来源**: m4（综合审计）
- **影响**: ~4 张卡脚注引用范围窄于声明范围

| 卡 | 问题 |
|----|------|
| namespace-key-memory-model | tuple 格式/IndexConfig 声明的脚注覆盖不足 |
| context-scaling-diminishing-returns | 'lost in the middle' 细节脚注窄 |
| llm-wiki-mainstream-prerequisites | Notion+Obsidian 愿景脚注窄 |
| observation-based-memory-representation | '5% improvement' vs 实际 31% |

- **方法**: agent 回查源材料，扩展脚注引用范围或拆分为多条脚注
- **预期结果**: 每条正文声明的脚注覆盖完整

### C7: 缺失卡片创建

- **审计来源**: M6 + M11 + m6（综合审计）、5.5 幽灵卡分析

#### C7a: 优先创建（消除断裂引用 + 核心缺口）

| 缺失卡 | 源 | 理由 | 预计工作量 |
|--------|---|------|-----------|
| memgpt-queue-manager | arxiv-memgpt Section 2.2 | 2 张卡的 related 断裂引用指向它 | 15 分钟 |
| conflict-routing-matrix | arxiv-memory-as-metabolism Section 5.0 | 论文核心规范贡献，含 7 行路由规则和阿谀覆写 | 20 分钟 |

#### C7b: 材料穷尽缺口补卡（按 impact 排序）

| 缺失内容 | 源 | 优先级 |
|---------|---|--------|
| Queue Manager 子系统细节 | arxiv-memgpt Section 2.2 | 高（与 C7a 合并） |
| 多模态对话生成任务 | arxiv-locomo | 中 |
| LLM agent 攻击 + FEVER 数据集 | arxiv-poisonedrag | 中 |
| 实体提取管线 + 26% 改进 | arxiv-mem0 | 中 |
| 文档数量交叉阈值 | arxiv-wicer | 中 |
| 复利波及量化数据 + 2 pitfall | openaitoolshub-six-months | 低-中 |
| ~200页/~100K 规模天花板 | robin-cartier | 低-中 |
| kb_lint 细节 | clawhub | 低 |
| 成本数据表 | anthemcreation | 低 |

- **方法**: agent 读取源材料对应章节，按标准 KB 卡 schema 创建，生成 JJ 文件，补充 related 链接
- **预期新增**: 2 张优先卡 + 最多 9 张材料缺口卡

### C8: Comparison 卡跨卡引用脚注补全

- **审计来源**: m10（综合审计）
- **卡片**:
  - comparison-detection-blind-spot-under-entrenchment：设计启示段引用其他卡概念但无 `[^card-*]` 脚注
  - comparison-corrective-vs-servant-agency：同上（与 B6 协同修复）
- **方法**: agent 检查正文中提及的 KB 概念，为每个添加 `[^card-*]` 脚注
- **预期结果**: 正文中所有 KB 概念提及均有脚注锚定

### C9: 原子性边界审查

- **审计来源**: m7（综合审计）
- **卡片**: 4 张

| 卡 | 问题 | 建议处理 |
|----|------|---------|
| graphrag-community-hierarchy | 检测 vs 摘要两个可分概念 | 评估是否拆卡；若概念不可分则保留并加注 |
| source-faithfulness-risk | 风险 vs 锚点 | 评估是否拆卡 |
| query-and-answer-filing | 查询 vs 归档 | 评估是否拆卡 |
| rag-parametric-bias-failure | 两种失效模式 | 评估是否拆卡 |

- **方法**: agent 读取每张卡，判断标题连词连接的概念是否为不可分整体。若可分且每部分有足够独立论点，则拆为两张卡并保持 related 链接
- **预期结果**: 4 张卡审查完毕，拆卡 0-2 张（大多数预期为保留）

### C10: Agent 合成分析标注

- **审计来源**: m9（综合审计）
- **卡片**: comparison-access-vs-content-memory-tiering
- **问题**: 引入源文本未有的四象限框架，属于 agent 合成分析
- **方法**: 在四象限框架前添加 `[编者注：以下为 KB 编辑合成的分析框架，非原始源文本内容]` 标注
- **预期结果**: 读者清楚区分源忠实内容与 agent 合成分析

### C11: Knowledge-compounding 源验证

- **审计来源**: M10（综合审计）、5.4 验证盲区分析
- **影响**: 10 张卡的源 PDF 不可提取文本
- **卡片**:
  - knowledge-compounding
  - cost-independence-assumption
  - dynamic-agentic-roi
  - compounding-cost-honesty
  - token-capital-goods
  - capitalized-latency
  - invest-harvest-cycle
  - supply-demand-token-dividend
  - search-write-back
  - topic-concentration-compounding
- **方法**: 安装 PyMuPDF 或 pdftotext，提取源 PDF 文本，对 10 张卡执行 section 级脚注验证
- **预期结果**: 消除验证盲区，10 张卡升级为 "fully verified" 或发现新问题纳入修复

---

## 执行顺序

```
Phase 1: Category A（脚本修复）
  A1 → A2 → A3
  预计耗时: 30 分钟（脚本开发 + 执行 + 验证）
  前置条件: 无

Phase 2: Category B（定向编辑）
  B1-B8 可并行执行
  预计耗时: 60-90 分钟
  前置条件: A1 完成（避免 YAML 修复覆盖手动编辑）

Phase 3: Category C（Agent 判断）
  批次 1: C1 + C4 + C5 + C8 + C10（轻量编辑，可并行）
  批次 2: C2 + C3（大规模链接补全，最耗时）
  批次 3: C6 + C7（需读取源材料）
  批次 4: C9 + C11（评估性工作）
  前置条件: B 全部完成（避免冲突编辑）
```

**关键约束**: A → B → C 严格串行，同一 Phase 内可并行。理由：A 的 YAML 修复会改变卡文件结构，B 的定向编辑可能与 C 的 agent 写入冲突。

---

## Workflow 实现建议

### Phase 1 实现（A1-A3）

单个 Python 脚本 `fix_yaml_and_jj.py`，顺序执行三项脚本修复。不需要 LLM agent。

```
输入: cards/*.md, justification/*.md
输出: 原地修改 + fix_report_phase1.json（记录每张卡的修改详情）
```

### Phase 2 实现（B1-B8）

**1 个 agent**，接收 8 项修复任务清单，逐张执行已知修改。每张卡的修改内容已在本计划中明确，agent 只需读卡 → 定位 → 编辑 → 写入。

预估 token 开销: ~50K（8 张卡全文 + 编辑指令）

### Phase 3 实现（C1-C11）

需要 **3-4 个并行 agent**，按工作量均匀分配：

| Agent | 任务 | 预估 token | 理由 |
|-------|------|-----------|------|
| Agent 1 | C1（5 张孤儿卡）+ C4（8 张别名）+ C10（1 张标注） | ~80K | 轻量编辑，每张卡 grep KB + 写入 |
| Agent 2 | C3 前半（11 张 comparison 卡脚注补全） | ~120K | 需读源材料定位引用段落 |
| Agent 3 | C3 后半（10 张 comparison 卡脚注补全）+ C8（2 张跨卡脚注） | ~120K | 同上 |
| Agent 4 | C2（跨领域桥梁）+ C5（8 张 editorial 标注）+ C6（4 张脚注扩展） | ~100K | C2 需全局扫描 |

**单独执行**（不适合并行）：
- C7（创建新卡）: 在 Phase 3 批次 1-2 完成后执行，因为新卡的 related 字段需要引用已修复的卡
- C9（原子性审查）: 需要独立判断，1 个 agent 单独执行
- C11（PDF 重验）: 需要安装工具 + 源 PDF 访问，可能需要人工介入

### 验证步骤

Phase 3 全部完成后，运行验证脚本：

```python
# 1. YAML 格式验证: 280 张卡全部可 yaml.safe_load()
# 2. 断裂引用验证: related 字段中所有 slug 在 cards/ 目录中存在
# 3. 孤儿卡验证: 无 (0 出站 + 0 入站) 的卡片
# 4. 脚注完整性验证: 正文中所有 [^xxx-N] 引用在脚注节有定义
# 5. Comparison 卡验证: 所有 comparison 卡至少 1 条 [^src-*]
# 6. JJ 格式验证: 所有 JJ 文件包含 ## creation 头
```

---

## 未纳入本轮修复的项目（INFO 级 / 低优先）

以下发现已记录但不在本次修复范围内：

| 编号 | 发现 | 理由 |
|------|------|------|
| i1 | 248/280 张卡时间戳聚类 | 信息性发现，批量生成的自然产物，无需修复 |
| i2 | 6 张长卡体（>45 行） | knowledge-compounding 和 my-llm-wiki-implementation 偏 hub-page 但内容连贯 |
| i3 | 背景性/实现细节级材料缺口 | wikibase Sitelinks、DRAGON retriever 等，不影响 KB 核心覆盖 |
| i4 | text-perturbation-amplification 概念名称合成 | "微扰放大效应" 为 agent 合成名称，但概念本身准确 |
| 集群设计修正 | 废弃固定集群、全局 derive-related | 属于流水线设计改进，非本轮 KB 修复范围 |
| 审计协议修正 | grep → semantic-verified 双级别 | 属于审计工具改进，非 KB 修复范围 |
| Comparison 模板改进 | 脚注硬约束、阅读区分指令 | 属于下一轮预防措施，非当前修复 |
| 集群日志持久化 | scanResult.clusters 写入 JSON | 属于流水线改进 |
