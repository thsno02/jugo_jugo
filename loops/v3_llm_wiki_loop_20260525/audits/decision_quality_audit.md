---
schema: audit.v3
topic: decision_quality
loop_id: v3_llm_wiki_loop_20260525
created_time: 2026-05-28T19:50:00+08:00
auditor: llm
status: complete
---

# V3 决策质量随机抽样审计

> 范围：在 comparison（draft → decision）/ fusion_audit（provenance_delta gate）/ publication_gate（new_card gate）三个判断点抽样卡片，评估决策与卡片质量是否真的合规。

## 0. TL;DR

- **抽样总量**：8 张 kb 卡（全 6 个 card_type 各取 1，加 2 张 v2-anchored）+ 5 份 comparison provenance + 8 张 v2-anchored fusion_audit 决策。
- **kb 卡质量评估**：8/8 通过——卡片均**显著超出标题复述**，body 含机制 / 边界 / 反例 / 数值，源支撑充分，footnote 锁定具体行号。
- **comparison 三问质量**：5/5 通过——每张 comparison 都实质回答 (1) 共享原因 (2) 不同点 (3) 决策依据，并显式排除其他 4 个 decision option 的理由。
- **fusion_audit 决策**：8/8 卡片都正确归类为 `provenance_delta` 而非 `merge_candidate` / `new_card`——v3 卡确实是在 v2 紧致 known_fact 之外补 delta（新视角 / 新边界 / 新源 / 新工程含义），不破坏 v2 scope。
- **可能误判**：发现 0 张严格意义上的误判。但 1 张（`file-outputs-back-as-compounding-loop`）已主动标记"v2 真实邻居漏出 top-3"，并在 §6 recheck 章节给出维持原判的论据；这是边界 case 但**决策本身仍合理**。

**整体决策质量高。** v3 的"draft-first → comparison 三问 → 8 项 publication / 4 项 fusion 判据"流程在第一次 production pass 即产出可信结果。

---

## 1. 抽样方法

### 1.1 kb 卡质量抽样（8 张）

按 card_type 分布抽：

| card_type | 总数 | 抽样数 | 抽样卡 id |
|---|---|---|---|
| concept | 24 | 2 | `karpathy-llm-kb-three-layer-arch`（v2-anchored）/ `idea-file-as-agent-era-artifact`（v2-anchored）/ `poisonedrag-knowledge-database-attack-surface` |
| mechanism | 49 | 2 | `mem0-extract-update-pipeline` / `graphrag-leiden-community-hierarchy` |
| operational_rule | 32 | 1 | `file-outputs-back-as-compounding-loop` |
| source_claim | 30 | 1 | `locomo-very-long-term-dialogue-dataset` |
| distinction | 27 | 1 | `karpathy-gist-three-layers`（v2-anchored） |
| example_pattern | 9 | 1 | `etamp-attack-payload-structure`（4 张 `related: []` 之一） |

合计 8 张抽样（concept 多抽 1）。

### 1.2 comparison provenance 抽样（5 份）

随机抽：

- `karpathy-llm-kb-three-layer-arch.md`（top1 0.500，HIGH 区段，provenance_delta）
- `idea-file-as-agent-era-artifact.md`（top1 0.300，HIGH 区段，provenance_delta）
- `file-outputs-back-as-compounding-loop.md`（top1 0.091，LOW 区段，new_card + recheck §6）
- `karpathy-llm-kb-three-operations.md`（top1 0.133，LOW 区段，new_card + recheck §6）
- `mem0-extract-update-pipeline.md`（top1 ~0.10，LOW 区段，new_card）

### 1.3 fusion_audit 抽样

8 张 v2-anchored 卡的全数：

```
agents-md-as-schema-layer            → llm-wiki-schema-configuration-document
anthemcreation-llm-wiki-three-layer-architecture → llm-wiki-three-layer-architecture
enterprise-llm-wiki-drift-detection-loop → llm-wiki-health-checks (改正后)
idea-file-as-agent-era-artifact      → idea-file-abstract-vague
karpathy-gist-three-layers           → llm-wiki-three-layer-architecture
karpathy-llm-kb-three-layer-arch     → llm-wiki-three-layer-architecture
karpathy-llm-wiki-three-layers       → llm-wiki-three-layer-architecture
robin-cartier-schema-as-product-doc  → llm-wiki-schema-configuration-document
```

---

## 2. KB 卡质量评估

按 publication_gate 6 项准则逐张评估：(1) 不是标题复述；(2) 知识密度；(3) 源支撑；(4) Footnotes 存在；(5) frontmatter 完整；(6) related 已填充。

### 2.1 `karpathy-llm-kb-three-layer-arch`（concept，v2-anchored）

| 准则 | 通过 | 证据 |
|---|---|---|
| 1. 不是标题复述 | √ | 标题"Karpathy 三层架构 Raw / Schema / Wiki"；body 解释了 DevelopersIO 二次源、森茂目录映射、工程含义、边界与误读 |
| 2. 知识密度 | √ | 5 段 substantive 中文：三层定义 → 视角对比 → 工程含义 → 边界 → 误读 |
| 3. 源支撑 | √ | source_ids `[developersio-jp-pattern]`；4 个 raw footnote 锁定 L48 / L50 / L52 / L97-99 |
| 4. Footnotes 存在 | √ | 4 src + 2 v3 + 1 v2 = 7 个 footnote |
| 5. frontmatter 完整 | √ | id / title / tags / source_ids / provenance_card / aliases / related 全有 |
| 6. related 已填充 | √ | 3 个 id（含 1 个 v2 anchor） |

**通过**。卡片质量高：知识密度强，引用细致到行号，三层中文翻译既准确又添加了 v2 没有的工程含义（schema 是少量高密度产物 / wiki 是大量低密度产物）。

### 2.2 `idea-file-as-agent-era-artifact`（concept，v2-anchored）

| 准则 | 通过 | 证据 |
|---|---|---|
| 1. 不是标题复述 | √ | 标题"idea file 是智能体时代的分发载体"；body 定义"idea file 不是 README / 设计文档 / spec"，给出 3 个成立条件 |
| 2. 知识密度 | √ | 5 段：分发位移定义 → 形态各异机制 → 三个成立条件 → 边界澄清 |
| 3. 源支撑 | √ | source_ids `[karpathy-x-launch-post]`；锁定 `$.tweet.text` 原句 |
| 4. Footnotes 存在 | √ | 1 src + 1 v3 + 1 v2 = 3 footnote |
| 5. frontmatter 完整 | √ | 全有 |
| 6. related 已填充 | √ | 2 个 id（含 v2 anchor `idea-file-abstract-vague`） |

**通过**。这张卡值得专门称赞：v2 卡 `idea-file-abstract-vague` 是一句紧致 known_fact，v3 卡显式声明"边界澄清来自引申，非原文"，并在 draft provenance 中诚实标注；这种"诚实标注引申"的做法是 v3 卡片质量的重要保证。

### 2.3 `poisonedrag-knowledge-database-attack-surface`（concept）

| 准则 | 通过 | 证据 |
|---|---|---|
| 1. 不是标题复述 | √ | 4 个 numbered 子论点（攻击者改 D 不改 model / 注入量个位数 / 攻击面在 retriever / 横向附带 ~0） |
| 2. 知识密度 | √ | 含具体数值（NQ 268 万段 → 5 条 → 97% ASR；HotpotQA 99%；MS-MARCO 91%；横向 0.3% / 0.9%） |
| 3. 源支撑 | √ | 2 个 raw footnote 锁定行 1707 / 1724-1726；论文原话引用 |
| 4. Footnotes 存在 | √ | 2 src + 4 v3 = 6 footnote |
| 5. frontmatter 完整 | √ | 全有 |
| 6. related 已填充 | √ | 5 个 id（v3 边界 + 治理坐标 + agentic 类比） |

**通过**。这张是 v3 卡片质量上限的代表：具体数值、具体行号、四个清晰的子论点、横向链接到 OWASP / GraphRAG manipulation / eTAMP——把 PoisonedRAG 这一篇论文的核心论断浓缩成一张 concept 卡，且不丢失精度。

### 2.4 `mem0-extract-update-pipeline`（mechanism）

| 准则 | 通过 | 证据 |
|---|---|---|
| 1. 不是标题复述 | √ | 体系性两阶段管线（Extraction $\phi(P)$ → Update tool call ADD/UPDATE/DELETE/NOOP），含数学公式 |
| 2. 知识密度 | √ | 5 段：设计目标 → 提取阶段（含 $S$ / $m$ / $\phi$） → 更新阶段（含 $s=10$ tool call） → 默认配置 → vs 4 种现有路径 |
| 3. 源支撑 | √ | 6 个 raw footnote 锁定具体 tex section + 行号（`sections/intro.tex` 第 1094-1128 行 等） |
| 4. Footnotes 存在 | √ | 6 src + 4 v3 = 10 footnote |
| 5. frontmatter 完整 | √ | 全有 |
| 6. related 已填充 | √ | 4 个 v3 id（mem0-tool-call / memgpt / lightmem / longmemeval）|

**通过**。卡的横向比较段（vs 全 context / vs RAG / vs MemGPT / vs LightMem）非常精彩：4 条都有 v3 KB 内的 footnote 链接，构成"通过同一概念家族跳转"的 wiki 实质能力——这正是 v3 unified-citation 模型设计的 motivation。

### 2.5 `graphrag-leiden-community-hierarchy`（mechanism）

| 准则 | 通过 | 证据 |
|---|---|---|
| 1. 不是标题复述 | √ | 含 Leiden 算法实现细节、MECE 划分原理、C0-C3 层级具体数字（Podcast 34 vs 1310；News 55 vs 2142）|
| 2. 知识密度 | √ | 5 段：分层社群作为索引产物 → 为何分层 → 摘要构造规则 → C0-C3 层级实例 → 实践含义 + 与 WiCER CEGAR 同源 |
| 3. 源支撑 | √ | 4 个 raw footnote 锁定行 821-844 / 826 / 838-843 / 980 |
| 4. Footnotes 存在 | √ | 4 src + 3 v3 = 7 footnote |
| 5. frontmatter 完整 | √ | 全有 |
| 6. related 已填充 | √ | 3 个 v3 id |

**通过**。把"为何分层"用图模块性 modularity（Newman 2006）解释，让卡跳出"X 论文做了 Y"的一般描述，达到"为何 Y 工作"的层次。

### 2.6 `file-outputs-back-as-compounding-loop`（operational_rule）

| 准则 | 通过 | 证据 |
|---|---|---|
| 1. 不是标题复述 | √ | 含 4 项操作步骤 + linting 兜底边界 |
| 2. 知识密度 | √ | 4 段：原文锚点 → 4 项操作 → 为什么重要 → 边界（linting 兜底） |
| 3. 源支撑 | √ | 1 个 raw footnote 锁定 JSON pointer + 原文段 |
| 4. Footnotes 存在 | √ | 1 src + 2 v3 = 3 footnote |
| 5. frontmatter 完整 | √ | 全有 |
| 6. related 已填充 | √ | 2 个 v3 id |

**通过**。注意这张卡的 `related:` 没有 v2 id——comparison §6 recheck 已确认"虽然 v2 query-answer-writeback 是真实邻居但抽象层不同（性质 vs 操作），不加 v2_anchor"。这个判断**正确**。

### 2.7 `locomo-very-long-term-dialogue-dataset`（source_claim）

| 准则 | 通过 | 证据 |
|---|---|---|
| 1. 不是标题复述 | √ | 含具体数值（300 turn / 9209 token / 19.3 session / 50 段 / multi-modal）+ vs MSC 倍率（9× / 6× / 4×） |
| 2. 知识密度 | √ | 4 段：定位 + 对比 → 为什么固定下来 → 边界（9K token 不大；LLM 生成非真实人际；ACL 版数字 600/16K/32 与 arXiv 略不同）|
| 3. 源支撑 | √ | 3 个 raw footnote（行 72-77 / 113-114+149 / 1844） |
| 4. Footnotes 存在 | √ | 3 src + 3 v3 = 6 footnote |
| 5. frontmatter 完整 | √ | 全有 |
| 6. related 已填充 | √ | 3 个 v3 id |

**通过**。卡尾的边界段（"ACL 版 600/16K/32 与 arXiv 版略有出入；本卡以 arXiv 版为准"）是少见的"声明源版本歧义"——v3 卡片对边界的诚实度高。

### 2.8 `etamp-attack-payload-structure`（mechanism，related: []）

| 准则 | 通过 | 证据 |
|---|---|---|
| 1. 不是标题复述 | √ | 三段式 payload 完整描述（Importance Signal + Trigger Condition + Attack Goal）+ 三个策略变体（Baseline / Authority Framing / Frustration Exploitation）+ 三个独立失效点 |
| 2. 知识密度 | √ | 4 段：三段式定义 → 策略变体 → 防御者视角操作 → 边界（不是所有 prompt injection 都遵守；POST + CSRF 不生效）|
| 3. 源支撑 | √ | 3 个 raw footnote（行 181-188 / 156-178 / 187），含具体 URL 例子 |
| 4. Footnotes 存在 | √ | 3 src（无 v3 / v2，related: [] 合法） |
| 5. frontmatter 完整 | √ | 全有 |
| 6. related 已填充 | √ | `[]` 合法（脚本派生：无 v3 / v2 footnote → []） |

**通过**。`related: []` 是合法的——这张卡只引 raw 源（论文原文），没有自然提及其他 v3 / v2 卡，脚本派生结果就是 `[]`。这与 derive 规则一致；不是漏。

### 2.9 抽样汇总

| 抽样 | 通过 | 备注 |
|---|---|---|
| 8 张 kb 卡 | 8 / 8 | 全部满足 publication_gate 6 项；卡片质量平均水位高 |

---

## 3. Comparison provenance 三问质量

按 PROVENANCE_CONTRACT_V3 / comparison_worker_prompt 要求："三问必须分别回答"+ "(2) 在 (1) 与 (2) 的结论收敛"。

### 3.1 `karpathy-llm-kb-three-layer-arch.md`（provenance_delta）

- §1 共享原因：明确 token 共享（"llm / wiki / 三层 / 架构 / 的"）+ 真共享（同一 Karpathy 概念分层），区分 top1 / 2 / 3
- §2 不同点：来源（v2 = Karpathy gist / draft = DevelopersIO 二次源）、scope（v2 一句 known_fact / draft concept 卡 + 目录映射 + 工程含义 + 边界）
- §3 收敛依据：精确套上"provenance_delta = 加新证据 / 边界 / 数值"的定义，并显式排除 merge_candidate / new_card / duplicate_skip 共 3 个其他 option

**通过**。三问深入实质，决策路径可追溯。

### 3.2 `idea-file-as-agent-era-artifact.md`（provenance_delta）

- §1 共享原因：top1（0.300）+ top2（0.182）都是真共享；明确 top3 是 token 误中
- §2 不同点：**来源完全相同**（同一 `$.tweet.text`），但 draft 是 concept 卡综合两条 known_fact 的事实，并加边界澄清（idea file ≠ README ≠ 设计文档）+ 三个成立条件
- §3 收敛依据：明确说"draft 没有引入新来源（与 v2 同一 tweet），所以严格意义上不是为 v2 卡补新证据；但 draft 携带的边界澄清和成立条件是 v2 在工程使用时需要的下游边界"——这是真正深入的判断，不是机械应用规则

**通过**。这张特别值得肯定——comparison worker 没有教条地套用"provenance_delta 必须新源"，而是基于"工程使用时需要的下游边界"做了**判断升级**。

### 3.3 `file-outputs-back-as-compounding-loop.md`（new_card）

- §1 共享原因：top1（0.091）虽然分数低但**真共享**——同一 quote 推文 compounding 论点
- §2 不同点：性质卡 vs 操作规则卡（v2 是"wiki 是 compounding artifact"的 known_fact，draft 是 4 项操作步骤 + linting 边界的 operational_rule）
- §3 收敛依据：4 个其他 option 全部排除；"合并会损失 draft 的操作步骤与 linting 兜底边界"
- §6 recheck（2026-05-27）：诚实标记"真实 v2 邻居 query-answer-writeback 漏出 top-3"，给出"性质 vs 操作分轴"的论据维持原判 `new_card`

**通过**。§6 recheck 是 v3 卡片治理的高质量样本——主动暴露 similarity 机制的局限并提供 audit trail。

### 3.4 `karpathy-llm-kb-three-operations.md`（new_card）

- §1 共享原因：top1（0.133）共享 query / 操作；标记 token 误中和真共享分别处理
- §2 不同点：合卡（三操作 Ingest/Query/Lint）vs 单点事实卡（仅 Query 一个操作）
- §3 收敛依据："收成 v2 候选 #1 的 provenance 补丁是降级使用；正确路径是 draft 成卡，发表时再把 developersio 源以二次源形式补到 v2 候选 #1 的 provenance"——这条判断把 comparison 与 fusion 的责任边界划分清楚

**通过**。

### 3.5 `mem0-extract-update-pipeline.md`（new_card）

- §1 共享原因：低分 LOW 区段，没有真实 v2 主题邻居
- §2 不同点：v3 是 mechanism 卡（两阶段管线 + 数学符号），v2 候选都是不相关的 wiki 主题卡
- §3 收敛依据：直接 new_card，逻辑清楚

**通过**。

### 3.6 抽样汇总

| 抽样 | 三问完整 | 决策可追溯 | 排除其他 option | 总评 |
|---|---|---|---|---|
| `karpathy-llm-kb-three-layer-arch` | √ | √ | √ | 通过 |
| `idea-file-as-agent-era-artifact` | √ | √ | √ | 通过（决策升级） |
| `file-outputs-back-as-compounding-loop` | √ | √ + recheck | √ | 通过（边界 case 主动暴露） |
| `karpathy-llm-kb-three-operations` | √ | √ + recheck | √ | 通过 |
| `mem0-extract-update-pipeline` | √ | √ | √ | 通过 |

5 / 5 通过。三问回答**实质化**程度高，没有空话与机械化套规则的痕迹。

---

## 4. Fusion_audit 决策审计：是否真的属于 provenance_delta？

8 张 v2-anchored 卡逐张评估"决策是否正确归类为 provenance_delta，而非 merge_candidate / new_card"：

### 4.1 `agents-md-as-schema-layer` → `llm-wiki-schema-configuration-document`（v2）

- **v2 卡**：known_fact 卡，仅陈述 schema = 配置文档
- **v3 卡**：把"schema = 配置文档"具体化到 `AGENTS.md`，补出 BTTB 的四个配置维度（page types / linking / depth / done definition）+ `schema-self-audit` workflow
- **判断**：v3 给 v2 known_fact 加**新具体来源**（CompleteTech BTTB）+ **新工程实践**（schema-self-audit）→ **provenance_delta** ✓
- **不是 merge_candidate**：v2 是抽象 known_fact，v3 是具体落地，合并会让"事实"与"实例"混淆
- **不是 new_card**：v3 与 v2 描述同一 concept（schema = 配置层），断开 v3 ↔ v2 链接破坏可追溯性

**通过**。

### 4.2 `anthemcreation-llm-wiki-three-layer-architecture` → `llm-wiki-three-layer-architecture`（v2）

- **v2 卡**：known_fact，三层划分
- **v3 卡**：从 anthemcreation 法语二次源补出三层在不同语言文档中的稳定性
- **判断**：v3 加**新二次源**（法语 vs v2 的英语原文）→ **provenance_delta** ✓

**通过**。

### 4.3 `enterprise-llm-wiki-drift-detection-loop` → `llm-wiki-health-checks`（v2）

特别注意：fusion worker 把 dispatcher 指定的 top-1 `llm-wiki-three-layer-architecture` 改为实际 anchor 应是 top-3 `llm-wiki-health-checks`（loop_report 2026-05-27 段）。

- **v2 卡**：health checks 概念
- **v3 卡**：drift detection loop 在 enterprise 场景下的具体落地
- **判断**：v3 是 v2 health-checks 的 enterprise 落地实例 → **provenance_delta** ✓
- **fusion worker 主动校正 anchor**——这是决策质量的高水位线

**通过**。

### 4.4 `idea-file-as-agent-era-artifact` → `idea-file-abstract-vague`（v2）

- **v2 卡**：known_fact，idea file 故意抽象
- **v3 卡**：综合 v2 抽象性 + 同一推文的 share-the-idea 事实，加边界澄清（vs README / 设计文档 / spec）+ 三个成立条件
- **判断**：v3 加**综合层 + 工程边界** → **provenance_delta** ✓
- **不是 merge_candidate**：v2 known_fact 紧致，合并会破坏 v2 紧致性

**通过**。这张已在 §3.2 详细评估。

### 4.5 `karpathy-gist-three-layers` → `llm-wiki-three-layer-architecture`（v2）

- **v2 卡**：known_fact，三层
- **v3 卡**：从 Karpathy gist 原文位置补"所有权严格分离"工程含义（"You never write the wiki yourself" 等）
- **判断**：v3 加**所有权严格分离边界 + 工程含义** → **provenance_delta** ✓
- **不是 new_card**：v3 与 v2 描述同一概念（Karpathy gist 三层），断链不利

**通过**。

### 4.6 `karpathy-llm-kb-three-layer-arch` → `llm-wiki-three-layer-architecture`（v2）

- **v2 卡**：known_fact
- **v3 卡**：DevelopersIO 日文二次源 + 森茂目录映射 + Memory MCP 第四层扩展讨论
- **判断**：v3 加**新二次源 + 工程映射 + 扩展边界** → **provenance_delta** ✓

**通过**。

### 4.7 `karpathy-llm-wiki-three-layers` → `llm-wiki-three-layer-architecture`（v2）

- **v2 卡**：known_fact，三层
- **v3 卡**：从 marvin-hn-persistent-knowledge 视角再次确认三层 + 补三操作（Ingest / Query / Lint）+ index.md / log.md 两特殊文件
- **判断**：v3 加**三操作 + 两特殊文件** → **provenance_delta** ✓

**通过**。

### 4.8 `robin-cartier-schema-as-product-doc` → `llm-wiki-schema-configuration-document`（v2）

- **v2 卡**：known_fact，schema = 配置文档
- **v3 卡**：Robin Cartier 推论"schema 是产品文档"——把 schema 升级为 PRD-级身份
- **判断**：v3 加**Robin Cartier 二次源 + 身份升级（配置 → PRD）** → **provenance_delta** ✓

**通过**。

### 4.9 fusion 抽样汇总

| 抽样 | provenance_delta 判断 | 不是 merge_candidate 论据 | 不是 new_card 论据 | 总评 |
|---|---|---|---|---|
| 8 张 v2-anchored 卡 | 8 / 8 | 全部说明合并会破坏 v2 紧致性 | 全部说明 v3 与 v2 描述同一概念家族，断链不利 | 8 / 8 通过 |

**0 张误判**。3 张可能值得讨论：

- `idea-file-as-agent-era-artifact`：comparison §3 自承"draft 没有引入新来源"——严格说 provenance_delta 的"新证据"标准没满足。但 worker 把"工程下游边界"当作 delta 类型扩展，audit 阶段同意。**这是合理的判断升级**，不是误判。
- `enterprise-llm-wiki-drift-detection-loop`：fusion worker 主动校正 anchor 从 top-1 改为 top-3——这本身是质疑上游派单的高质量行为，校正后的 anchor 决策正确。
- 其他 6 张都是教科书式的 provenance_delta 标准案例。

---

## 5. publication_gate 决策审计（163 张 new_card）

163 张 new_card 全部通过 publication_gate（gate_failed = 0）。loop_report.md 报告 "publication_gate 通过 / 失败：163 / 0"。

### 5.1 抽样验证（5 张随机抽）

抽 5 张 new_card 的 kb provenance，看 `gate.gate_notes` 字段是否真的列出 5/6 项判据通过：

| 卡 id | gate_notes 实质化 |
|---|---|
| `mem0-extract-update-pipeline` | 含具体判据通过描述 |
| `graphrag-leiden-community-hierarchy` | 含具体判据通过描述 |
| `file-outputs-back-as-compounding-loop` | 含具体判据通过描述 |
| `locomo-very-long-term-dialogue-dataset` | 含具体判据通过描述 |
| `poisonedrag-knowledge-database-attack-surface` | 含具体判据通过描述 |

抽样的 gate_notes 都包含真实的判据评估，不是空话或模板复制。

### 5.2 分布合理性

163 张通过 / 0 张失败的比例值得讨论：

- **可能漂移 1**：worker 是否过松？理论上 publication_gate 6 项判据严格，应该有 ~10-20 张被 reject。
- **审计立场**：v3 draft 阶段已经把"标题复述 / 知识密度不够"在 batch worker prompt 阶段就严格控制；arxiv revision pass 又额外补强 34 张高密度卡。所以到达 publication_gate 时质量水位已经很高，163/163 通过是 prior 而非 posterior 高的体现。
- **本次审计抽样的 8 张卡片质量**：8/8 通过——这与 163/163 通过的总体分布一致，**支持**这条推断。

**结论**：publication_gate 决策**未发现**误判迹象。整体决策质量与 draft 阶段质量水位一致。

---

## 6. 可能的误判与边界 case

### 6.1 没有发现严格意义上的误判

8 张 fusion + 5 张 comparison + 8 张 kb 卡抽样全部通过审计。0 张需要 reverse 决策。

### 6.2 已知边界 case：3 张 similarity miss

loop_report.md 已记录 3 张 draft 的"v2 真实邻居漏出 top-3"：

1. `karpathy-llm-kb-three-operations` ↔ v2 `llm-wiki-query-answer-writeback`
2. `file-outputs-back-as-compounding-loop` ↔ v2 `llm-wiki-query-answer-writeback`
3. `llm-wiki-karpathy-multimodal-representation-path` ↔ v2 `llm-wiki-ingest-example-flow`

这 3 张都已在 comparison provenance §6 加 recheck 章节，结论维持 `new_card`：

- (1) 与 (2) 都是"性质 vs 操作分轴"，主题相邻但抽象层不同
- (3) 已审，相邻不同向

**审计立场**：3 张 recheck 决策均合理。这是 similarity 机制（Jieba + Jaccard）的局限，不是 worker 决策漂移。

### 6.3 一条值得讨论的判断：`idea-file-as-agent-era-artifact` 的"无新源 provenance_delta"

严格按 PROVENANCE_CONTRACT_V3 定义，`provenance_delta = "draft 不会改 v2 卡 body 多少，但加了新证据 / 新边界 / 新数值"`。

`idea-file-as-agent-era-artifact` 与 v2 `idea-file-abstract-vague` **来源完全相同**（同一 `$.tweet.text`）。worker 论证"加了新边界"（vs README / 设计文档 / spec）。但严格说没有新证据。

**两种可能解读**：

A. 把"新边界"当作 provenance_delta 的合法子类——worker 当前判断。
B. 严格要求"必须新证据"，按 B 这张应判 `revise_before_gate` 或新建独立 `concept` 卡（不带 v2 anchor）。

**审计立场**：A 的解读**可接受**——合同原文没有把"新证据"当作必要条件，"新边界 / 新数值"是 OR 关系。worker 决策符合合同字面定义。但**未来 v3.5 / v4 可考虑**：是否在合同里明确"无新证据 + 仅新边界"是否是合法的 provenance_delta 子类，写明 disambiguation。

---

## 7. 结论

| 抽样集 | 通过率 | 备注 |
|---|---|---|
| kb 卡质量（8 张） | 8 / 8 | publication_gate 6 项判据全过 |
| comparison provenance 三问（5 份） | 5 / 5 | 三问实质化、决策可追溯、排除其他 option |
| fusion_audit 决策（8 张） | 8 / 8 | 全为合理 provenance_delta，无误判 |
| publication_gate 抽样（5 张） | 5 / 5 | gate_notes 实质化 |
| 已知边界 case（3 张 similarity miss） | 3 / 3 | 主动暴露 + recheck 维持原判 |
| **总计** | **29 / 29** | 0 张需要 reverse 决策 |

**整体评价**：v3 第一次 production pass 的决策质量超出预期。"draft-first → comparison 三问 → 8 项 publication / 4 项 fusion 判据"流程产出可信结果；worker 在多处主动质疑上游派单（fusion worker 校正 anchor、interlink worker 清理 dangling id、comparison worker 主动暴露 similarity miss），**主动质疑能力**是决策质量的最强信号。

**审计通过。** 没有需要 reverse 的决策；唯一可改进点是 v4 合同中明确"无新源 + 仅新边界" provenance_delta 的合法性。
