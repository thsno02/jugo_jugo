---
schema: cluster_damage_assessment.v1
date: 2026-06-07
predictions_tested: 6
confirmed: 3
not_confirmed: 2
partially_confirmed: 1
---

# Cluster Damage Assessment

## 执行摘要

- **集群没有形成硬边界，但造成了三类实质性损伤**：6 项预测中 3 项确认、1 项部分确认；集群机制虽未制造信息孤岛（88.7% 的链接跨前缀），却引入了孤儿卡排斥（5 张卡完全失联）、YAML 序列化缺陷（69/280 张卡 = 24.6%）、以及脚注叙事泄漏（5/21 对比卡 = 24%）。
- **最严重的损伤来自 governance rescue commit (b26dafc)**：该提交的 derive-related 步骤以单行替换覆盖 block-style `related:` 字段，导致 63 张批量卡产生双格式 YAML 缺陷，同时遗漏了全部 5 张 llm-wiki-net 孤儿卡的交叉链接。
- **跨领域链接稀疏但非缺失**：纯跨领域链接占比 13.4%（101/753），security-memory 仅 2 条、wiki-governance 仅 4 条单向链接，高价值概念桥梁未被系统性建立。
- **集群的同前缀链接密度仍是跨前缀的 5.7-7.5 倍**：说明主题亲和性产生了温和的聚类偏好，虽未封锁信息流动，但抑制了最需要的跨领域洞察。
- **对比卡流水线的泄漏率达 24%**：集群内高脚注密度卡（5-6 条脚注）通过叙事描述为 governance agent 提供了"隐式上下文通道"，导致未声明来源的概念渗入对比卡正文。

## 预测验证结果

| # | 预测 | 判定 | 关键证据 |
|---|------|------|----------|
| 1 | 集群边界（以 canonical_concept 前缀代理）是否刚性 | NOT_CONFIRMED | 1332 条链接中 88.7% 跨前缀；同前缀仅 11.3%。但同前缀密度 3.25% vs 跨前缀 0.57%，比值 5.7-7.5x，存在温和聚类偏好 |
| 2 | 5 张孤儿卡被系统性排斥于交叉链接图 | CONFIRMED | 5 张卡均来自 llm-wiki-net，related: [] 且入站链接近零；至少 15 条高置信度链接缺失；topic-isolation 甚至有悬空 [^card-1] 脚注证明链接曾被尝试但未完成 |
| 3 | 对比卡因集群同质性而抑制跨领域对比 | NOT_CONFIRMED | 21 张对比卡中跨领域 10 张 = 47.6%，同领域 11 张 = 52.4%；跨领域对比并未被抑制 |
| 4 | 双格式 related: 缺陷的根因是 governance rescue 的单行替换 | CONFIRMED | 69/280 卡受影响（24.6%）；block-style 卡 63/63 = 100% 触发缺陷，inline-style 卡 0/196 = 0%；根因：单行替换未删除后续缩进行 |
| 5 | 脚注叙事泄漏是系统性模式，与集群内交叉链接密度相关 | CONFIRMED | 5/21 对比卡（24%）存在泄漏；3 例跨来源泄漏 + 2 例同来源溯源缺口；泄漏集群核心卡的脚注数 5-6 条，干净集群平均 3-4 条 |
| 6 | 跨领域洞察因集群主题同质性而缺失 | PARTIALLY_CONFIRMED | 纯跨领域链接 101/753 = 13.4%；security-memory 仅 2 条链接（17+71 张卡）；wiki->governance 方向 23 张卡讨论审计概念但零条链接至 governance 卡 |

## 根因链

### 因果链 1：governance derive-related 的序列化缺陷

```
集群分组（37 组）
  -> governance rescue commit (b26dafc) 批量执行 derive-related
    -> derive-related 脚本假设 related: 字段仅占一行
      -> 对 block-style related: 执行单行替换
        -> 原始缩进 `- item` 行未被删除
          -> 69 张卡产生双格式 YAML（inline + block 共存）
```

**影响路径**：Phase 4 extraction (d36f6f7) 生成 244 张批量卡，其中 63 张使用 block-style `related:`。Phase 4 governance (f4ec89b) 未改变格式。governance rescue (b26dafc) 的 derive-related 步骤将 `related:` 行替换为 `related: [item1, item2]`，但未删除后续的 `- item` 行，产生无效 YAML。另有 6 张对比卡在创建时即带有同样缺陷。

### 因果链 2：孤儿卡的系统性排斥

```
11 张 llm-wiki-net 来源卡进入 governance
  -> derive-related 步骤处理集群
    -> 5 张卡未被任何集群的交叉链接覆盖
      -> related: [] 保持为空
        -> 零出站链接 + 近零入站链接
          -> 15+ 条高置信度语义链接缺失
```

**证据细节**：同一来源的 11 张卡中，6 张正常获得 related 链接，5 张完全为空。topic-isolation 卡体内有 `[^card-1]` 引用 llm-wiki-pattern 但脚注从未定义，证明交叉链接流程启动但未完成。multi-platform-skill-portability 从 mcp-tool-skill-layering 收到 1 条入站链接但未产生对称出站链接，说明 derive-related 对该卡完全跳过。

### 因果链 3：脚注叙事泄漏

```
集群内核心卡有 5-6 条 [^card-*]/[^dist-*] 脚注
  -> 每条脚注包含目标卡概念的叙事描述
    -> governance agent 读取集群全部卡片内容
      -> 脚注叙事中的外部概念被 agent 吸收
        -> 概念无归因地出现在对比卡正文
          -> 溯源链断裂（来源未声明）
```

**具体路径举例**：cognitionus-llm-wiki-guide -> confirm-first-skill-capture -> human-llm-role-division 的 [^card-4] 脚注叙事 -> governance agent 读取 -> comparison-corrective-vs-servant-agency 第 27 行出现"确认优先规则"但无归因。

### 因果链 4：跨领域链接稀疏

```
集群按主题分组（同前缀密度 5.7x）
  -> derive-related 在集群内寻找候选链接
    -> 同领域卡优先被选中（86.6% related 链接同领域）
      -> 纯跨领域链接仅 13.4%
        -> security-memory 等高价值桥梁未被建立
```

**但未形成硬边界**：88.7% 的链接跨前缀这一事实说明集群没有封锁信息流动。问题不是"集群阻止了跨领域链接"，而是"集群没有主动促进跨领域链接"——derive-related 的搜索范围受限于集群内邻域，自然倾向同主题。

## 影响面估算

| 损伤类型 | 受影响卡片数 | 占比 | 受影响链接数 | 严重程度 |
|----------|------------|------|------------|----------|
| 双格式 YAML 缺陷 | 69/280 | 24.6% | 69 张卡的 related 字段解析可能异常 | 高：数据完整性 |
| 孤儿卡排斥 | 5/280 | 1.8% | 缺失至少 15 条高置信度链接 | 中：信息可达性 |
| 脚注叙事泄漏 | 5/21 对比卡 | 23.8% | 涉及至少 8 个未归因概念 | 中：溯源可信度 |
| 跨领域链接稀疏 | 全局性 | -- | security-memory 缺 ~20 条潜在链接；wiki->governance 缺 ~15 条 | 低-中：知识发现 |
| 集群硬边界 | 0 | 0% | 无 | 无损伤（预测未确认） |
| 对比卡跨领域抑制 | 0 | 0% | 无 | 无损伤（预测未确认） |

**综合影响**：
- **数据层**：69 张卡存在结构缺陷，需要修复 YAML 序列化。
- **图层**：至少 50 条高价值链接缺失（15 条孤儿卡 + ~35 条跨领域桥梁）。
- **溯源层**：5 张对比卡的来源声明不完整，影响知识溯源可信度。
- **未损伤**：集群未造成信息孤岛（88.7% 跨前缀），对比卡流水线仍能产出 47.6% 跨领域对比。

## 设计修正建议

### 1. 废弃固定集群分组，改用全局 derive-related

**问题**：集群分组将 derive-related 的搜索范围限制在 3-15 张同主题卡内，导致跨领域候选被系统性遗漏。

**替代方案**：derive-related 步骤不再依赖集群分组，改为对每张卡在全部 280 张卡中搜索语义最近邻。搜索策略：
- 以 canonical_concept + aliases + tags 构建轻量检索索引（grep-friendly，无需 embeddings）
- 对每张卡提取关键词，在全局索引中匹配候选
- 候选数量上限 10，由 LLM 精选 3-5 条最有价值链接
- 强制跨领域配额：至少 1 条 related 链接必须来自不同 domain tag

### 2. 修复序列化：先规范化再覆写

**问题**：单行替换无法处理 block-style YAML。

**修正**：derive-related 脚本在写入前先用 YAML 解析器读取整个 frontmatter，修改 `related` 字段后重新序列化，确保输出格式一致（统一为 inline `related: [...]`）。永远不要用正则替换 YAML 字段。

### 3. 孤儿卡检测作为 governance gate

**问题**：5 张卡静默失联，无告警。

**修正**：governance 完成后增加一步孤儿检测：
```
对 related: [] 且 入站链接 = 0 的卡片：
  1. 标记为 orphan
  2. 触发一轮专项 derive-related（全局搜索）
  3. 若仍无候选链接，记录审计日志说明原因
```

### 4. 对比卡泄漏防护

**问题**：governance agent 读取集群全部内容时，脚注叙事中的外部概念被无归因地吸收。

**修正**：
- 对比卡生成 prompt 中增加约束：正文只能引用 source_ids 中声明的来源，或通过 [^card-*] 脚注显式归因的卡片概念
- 对比卡生成后增加自动校验：提取正文中所有 KB 概念提及，检查是否均有 source_ids 或脚注覆盖；未覆盖的概念标记为潜在泄漏

### 5. 跨领域桥梁的主动发现

**问题**：同领域链接占 86.6%，跨领域桥梁依赖偶然发现。

**修正**：governance 后增加一轮"桥梁扫描"：
- 对每对领域（security-memory, wiki-governance, eval-RAG 等），提取各自卡片中提及对方领域概念但未链接的情况
- 本次审计已发现：security 领域 9 张卡提及 memory 概念但零链接，wiki 领域 23 张卡提及 governance 概念但零链接
- 将这些候选对输入 derive-related 补链
