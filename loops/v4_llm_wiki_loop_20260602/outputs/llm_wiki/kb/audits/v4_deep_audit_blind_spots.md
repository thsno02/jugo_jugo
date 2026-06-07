---
schema: deep_audit_report.v1
date: 2026-06-07
topics_audited: 8
focus: uncertainty_reduction
agents_used: 10
---

# v4 深层审计：认知盲点与不确定性消除

## 执行摘要

- **幽灵源问题严重**：74 个原始目录中 30 个（40.5%）未产出任何卡片，全部 20 个 github_repo 缺少 text.txt、全部 6 个 reddit 被反爬封锁——KB 的生态多样性覆盖存在系统性缺口
- **源权威扁平化是全局性的**：62% 的卡片（174/280）零认识论限定词，问题不在 HN 被当学术引用，而在 blog/pypi 描述用与实验论文同等断言口吻呈现——卡片生成管线系统性剥离了 hedging
- **直述与推断混淆率 50%**：首批 26 个 source footnote 中 13 个为 REASONABLE-INFERENCE（卡片添加了推导性机制细节后统一归因于单一脚注），第二批 23 个全部 DIRECT——说明问题集中在特定类型的卡片（学术综述型）而非全局
- **反向链接不对称 40.3%**：1021 条有向边中 411 条单向；40 张卡片入度为零（含全部 21 张 comparison 卡片作为纯 sink）；wikibase 9 卡完全断联主图
- **不确定性洗白几乎不存在**：引用链中最大 hedge-drop 仅为 3，且均为 APPROPRIATE-UPGRADE——KB 未通过引用链悄悄升级不确定声明
- **静默分歧裁决未检出**：21 张 comparison 卡中 19 张 NEUTRAL-ACKNOWLEDGED，2 张 NEUTRAL-BUT-FRAMED（证据不对称倾向一方但结论仍中立）
- **爬取有损性中度**：表格扁平化影响 4/5 抽查源（25 张 HTML 表格变为连续文本），wikibase 3 张 UML 图完全丢失，代码块缩进/结构在 3/5 源中消失

## 逐 Topic 发现

### 1. Source Authority Flattening（源权威扁平化）

- **判定**：全局性问题，但原因与预期不同——不是 HN 帖被当论文引用，而是管线统一剥离 hedging
- **关键证据**：
  - 280 张卡中 174 张（62%）零限定词，比率跨源类型高度一致（arxiv-experimental 63%、webpage-blog 60%、gist 59%）
  - HN 卡反而是最谨慎的非学术源（密度 4.472/100w，零限定比例仅 18%）
  - pypi 卡 100% 零限定词（7/7），webpage-blog 密度最低（1.490/100w）
  - 语义抽查 5 张卡中 4 张存在权威膨胀：cognitive-deskilling-risk 将 HN 轶事称为「实证支持」；complexity-collapse-threshold 将单条评论中的比喻呈现为普遍机制
- **对 KB 消费者的含义**：任何卡片中的断言性陈述不能直接等同于「源文献如此声称」；尤其 blog/pypi 来源的卡片，实际认识论置信度比卡面呈现低约一级

### 2. Uncertainty Laundering（不确定性洗白）

- **判定**：NOT DETECTED——KB 不存在系统性通过引用链悄悄升级不确定声明的问题
- **关键证据**：
  - 280 张卡中 87 张含 hedge 词，210 张含 [^card-*] 脚注
  - 最大 hedge-drop = 3（仅 10 对引用关系存在任何正向 drop）
  - Top 3 对（full-context-accuracy-ceiling、attention-dilution-at-scale 引用 context-extension-insufficiency；graphrag-small-context-window-advantage 引用 long-context-comprehension-illusion）均为 APPROPRIATE-UPGRADE：引用的是被引卡的实证核心结论，自然省略情境性 hedging
- **对 KB 消费者的含义**：引用链可信——若一张卡引用另一张卡的声明，置信度传递是准确的；不确定性问题集中在「源→卡」环节（见 Topic 1 & 3），而非「卡→卡」环节

### 3. Says-vs-Implies Conflation（直述与推断混淆）

- **判定**：中等风险，集中在学术综述型卡片；实现型/文档型卡片几乎不受影响
- **关键证据**：
  - 首批 5 卡 26 条 source footnote：13 条 REASONABLE-INFERENCE（50%），0 条 EXTRAPOLATION
  - 第二批 5 卡 23 条 source footnote：23 条 DIRECT（100%），0 条偏差
  - 最常见模式：卡片在引文段落添加机制细节或编辑性阐释后，将整段归因于单一 [^src-N]
  - 典型案例：wiki-rag src-2 将「grounding against curated knowledge」扩展为「reliable interpretive framework: key concepts, stable definitions, known relationships」；etamp src-1 将「without requiring direct memory access」改写为「only through environment observation」
  - 最严重卡片：wiki-rag-hybrid-pattern（3/4 footnotes 推断）、etamp-environment-memory-poisoning（5/6 footnotes 推断）
- **对 KB 消费者的含义**：source footnote 标注的存在不等于「此段文字是源文献的直接翻译」；对于学术综述型卡片，footnote 实际含义为「此段基于该源的信息推导而成」

### 4. Silent Disagreement Resolution（静默分歧裁决）

- **判定**：NOT DETECTED——comparison 卡片表现良好
- **关键证据**：
  - 21 张 comparison 卡中 19 张 NEUTRAL-ACKNOWLEDGED：明确标注分歧为未解决或情境依赖
  - 2 张 NEUTRAL-BUT-FRAMED：comparison-detection-blind-spot-under-entrenchment（比较轴本身偏向 metabolism 论文的视角）、comparison-replace-vs-optimize-rag（证据 3:1 倾向「replace RAG」阵营但结论仍中立）
  - 零张卡片直接裁定一方正确
- **对 KB 消费者的含义**：comparison 卡片的显式结论可信；但需注意 2 张 NEUTRAL-BUT-FRAMED 卡的证据选择隐含倾向——若要做决策，应回溯源文献验证

### 5. Scrape Lossiness（爬取有损性）

- **判定**：中度有损，结构化内容系统性退化
- **关键证据**：
  - 表格扁平化：4/5 抽查源受影响，25 张 HTML 表格变为连续文本行（列名与单元格值不可区分）
  - 图表丢失：wikibase-data-model 的 3 张 UML 类图完全缺失（text.txt 中仅有占位引用），这些图是理解数据模型的核心
  - 代码格式丢失：3/5 源中 63 个 code/pre 元素丢失缩进和块分界（langchain-long-term-memory-docs 最严重——多行 Python 示例压为单行）
  - 导航噪声：atlan 页导航菜单重复（85 行 x2）；langchain 侧边栏占 100 行噪声
- **对 KB 消费者的含义**：KB 中基于表格比较的卡片（如 comparison-*）的细节精度不可完全信赖，应回查源页面验证；wikibase 相关卡片缺少图表中的类型继承关系信息

### 6. Phantom Sources（幽灵源）

- **判定**：严重——40.5% 原始目录为废数据，15 个独立 github_repo 是最大未开发内容机会
- **关键证据**：
  - 30/74 目录未产出卡片（20 github_repo + 6 reddit + 4 webpage）
  - github_repo 全军覆没：管线没有从代码仓库提取可读文本的步骤（缺 text.txt），涵盖高星项目如 nashsu/llm-wiki（8658 星）、agricidaniel/claude-obsidian（5296 星）
  - reddit 全军覆没：全部 6 个目录 text.txt 仅含 222-224 字节的「You have been blocked by network security」
  - 8 个幽灵源与其他活跃源重复（5 repo 有 arxiv 伴侣、2 aicritique 为同一文章二次抓取、1 HN 镜像）
  - 15 个非重复 github_repo（独立 LLM wiki 实现/分叉/桌面应用）是最大未利用信息源
- **对 KB 消费者的含义**：KB 当前对 LLM wiki 生态系统的开源实现多样性、社区采用模式、Reddit 用户反馈几乎无覆盖——这些主题的认知空白未被承认

### 7. Source Balkanization（源巴尔干化）

- **判定**：局部问题，非系统性——3 个源形成回音室，但全局跨源链接率 54.3%
- **关键证据**：
  - 全局统计：1021 条有效 related 链接中 467 条（45.7%）指向同源 vs 554 条（54.3%）跨源
  - 完全回音室：wikibase-data-model（9 卡，19 链接，100% 同源）——零条对外边
  - 近回音室：arxiv-knowledge-compounding（10 卡，81.6% 同源）、arxiv-alce（10 卡，79.2% 同源）
  - 卡片级视角：73.9%（207/280）卡片至少有一条跨源链接；26.1%（73 张）全部链接指向同源
  - 仅 19/280（6.8%）卡片属于多源——这些 comparison 卡是跨源连接组织的主要载体
- **对 KB 消费者的含义**：wikibase、knowledge-compounding、ALCE 相关卡片的 related 链接几乎全部指向同源内容，不能依赖这些链接发现跨领域关联

### 8. Backlink Asymmetry（反向链接不对称）

- **判定**：显著——40.3% 单向边，hub 浓度极高，comparison 卡片结构性断联
- **关键证据**：
  - 411/1021 条边为单向（40.3%），305 对为双向互链
  - 40 张零入度卡片：21 张 comparison（100% 均为 sink）+ 19 张非 comparison（如 topic-isolation、locomo-human-machine-pipeline、idea-file-paradigm）
  - Hub 集中度：前 5 hub（llm-wiki-pattern=27、three-layer-architecture=21、lint-operation=17、human-llm-role-division=16、ingest-operation=15）吸收 28% 入边
  - wikibase 9 卡形成完全断联子图（零条与主图 271 卡的连接）
  - 移除 21 张 comparison 卡仅损失 6.8% 边——结构影响极小，说明 comparison 卡是装饰性叶节点
- **对 KB 消费者的含义**：从任意卡片出发的「related」导航无法到达 comparison 卡（因为没人链接它们）；wikibase 知识孤岛完全不可通过图遍历到达；hub 卡可能造成导航「引力井」效应

## 跨 Topic 模式识别

1. **管线系统性问题 > 内容判断问题**：三个最大发现（幽灵源 40.5%、权威扁平化 62% 零限定、爬取有损表格/图）都源于管线工程缺陷而非知识提取的判断错误。修复管线比逐卡修复更有效。

2. **wikibase 三重困境**：同时出现在 Balkanization（100% 同源链接）、Backlink Asymmetry（完全断联子图）、Scrape Lossiness（3 张 UML 图丢失）——这组 9 张卡片的认知可靠性最低。

3. **Comparison 卡的矛盾地位**：静默分歧裁决表现优秀（19/21 NEUTRAL），但结构上完全是 sink 节点（零入度）、内容上是唯一跨源桥梁（6.8% 多源卡）——它们是「写得好但找不到」的知识。

4. **认识论问题集中在「源→卡」边界**：不确定性洗白（卡→卡）几乎为零，但权威扁平化（源→卡注册）和推断混淆（源→卡归因）均为中-高风险——信息失真发生在进入 KB 的那一刻。

5. **缺失内容 vs 错误内容的不对称**：KB 几乎无事实错误（零 EXTRAPOLATION、零 SILENT-ADJUDICATION），但有大量认知空白（30 个幽灵源、零 Reddit 覆盖、零代码仓库覆盖、wikibase 图表缺失）——KB 的问题是「不知道自己不知道什么」。

## KB 认知健康总评

**认识论不确定性最高的区域：**

| 区域 | 不确定性类型 | 严重度 |
|------|-------------|--------|
| 开源实现生态 | 完全认知空白（15 独立 repo 未提取） | 极高 |
| Reddit 社区反馈 | 完全认知空白（6 源全被封锁） | 高 |
| wikibase 数据模型 | 结构信息缺失（UML 图）+ 图孤立 | 高 |
| Blog/pypi 来源卡片 | 置信度标注缺失（100% 零限定词） | 中高 |
| 学术综述型卡片的脚注 | 归因精度不足（50% 为推导非直述） | 中 |
| 表格比较内容 | 精度退化（列值不可区分） | 中 |

**KB 消费者应意识到的关键事实：**
- KB 声称覆盖 74 个源，实际有效源仅 44 个
- 卡面呈现的断言性语气不反映源文献的认识论置信度
- `[^src-N]` 脚注的语义是「基于此源」而非「此源原文如此」
- Related 链接不保证双向可达，且 comparison 卡完全不可通过 related 导航发现
- LLM wiki 的社区采用、用户体验反馈、开源实现差异是 KB 当前最大的认知盲区

## 建议（按不确定性消除价值排序）

1. **添加 github_repo text 提取步骤**（消除价值：极高）——为 15 个独立 repo 生成 text.txt（拼接 README + 关键源文件），预计可新增 30-50 张覆盖生态多样性的卡片，填补最大认知空白

2. **为 blog/pypi/gist 卡片添加 confidence_level 字段**（消除价值：高）——在卡元数据中标注 `epistemic_confidence: assertion | observation | speculation`，使消费者无需逐一审查即可识别低确定性内容

3. **wikibase 桥接 + 图表补充**（消除价值：高）——至少添加 2-3 条从 wikibase 卡到主图的跨源链接（如 wikibase-entity-value-hierarchy → schema-as-configuration）；手动补充 3 张 UML 图的文本描述到 text.txt

4. **source footnote 区分 DIRECT vs INFERRED 标记**（消除价值：中高）——在脚注中添加 `[^src-N direct]` / `[^src-N inferred]` 标记，使推导性归因透明化

5. **Comparison 卡双向链接 governance pass**（消除价值：中）——为每张 comparison 卡的被比较对象添加 `see_also: comparison-X` 反向链接，使 comparison 内容可通过图遍历发现

6. **Reddit 替代抓取方案**（消除价值：中）——使用 old.reddit.com + 适当 UA 或 Pushshift API 替代直接爬取，恢复社区反馈覆盖

7. **非 comparison 零入度卡片 backlink pass**（消除价值：低-中）——19 张非 comparison sink 卡片需要从主题相关卡片添加入边（优先处理 topic-isolation、locomo-human-machine-pipeline 等出度>=3 的卡片）

## 9. Pipeline 根因追踪与设计修正

### 9.1 Data Collection 层：raw.html 从未被使用

- **现状**：27 个 webpage 源全部有 `raw.html`（平均比 text.txt 大 7-35 倍），但 pipeline_spec.md 硬编码 `boundary-read: text.txt`
- **`TextExtractor(HTMLParser)`** 在 `fetch_sources.py` 第 41-69 行，将 table 压成空格分隔文本、code/pre 丢失缩进、img/svg 完全丢弃
- **arxiv 源**：`text.txt` 仅 5KB（arXiv 页面导航文字），`agent_source_bundle.txt` 为 TeX 解析结果 223KB——实际提取使用后者，text.txt 对 arxiv 无意义
- **根因**：pipeline 设计假设 `text.txt` 是充分表示，但 collection 脚本的 text extraction 从未针对结构化内容优化
- **修正方向**：boundary-read 改为优先级级联：agent_source_bundle.txt > raw.html（经 markdown converter 转换）> text.txt

### 9.2 GitHub Repo 完全缺失：20 源零卡

- **现状**：20 个 repo 已克隆到 `data/raw/github_repo/*/repo/`，全部有 README.md（5-36KB），部分有 docs/ 目录（如 microsoft-agent-governance-toolkit 有 729 个 .md 文件）
- **根因**：`fetch_sources.py` 第 474-528 行执行 git clone + API 获取 README，但**从不生成 text.txt**。pipeline 的 boundary-read 找不到文件直接跳过
- **影响**：KB 只有理论模型卡（arxiv 论文）+ 概念描述卡（blog/HN），缺少实践落地卡（实现细节、配置方式、CLI 用法）
- **修正方向**：为 github_repo 类型生成 material_bundle.txt = README.md + docs/**/*.md 拼接（类似 arxiv 的 agent_source_bundle.txt 做法）
- **优先级最高的 5 个 repo**：
  - repo-nvk-llm-wiki（722 .md 文件，完整 wiki-manager 实现文档）
  - repo-microsoft-agent-governance-toolkit（729 .md，治理框架文档 + 8 个 Python 包）
  - repo-kytmanov-obsidian-local（81 .py，完整本地 pipeline 实现）
  - repo-microsoft-graphrag（570 .py + docs/，补充 arxiv-graphrag 的实现细节）
  - repo-vectifyai-openkb（65 .py，开源 KB 构建工具）

### 9.3 Extraction 层：权威扁平化的 prompt 根因

- **reader skill** 有不确定性标注指令（"材料未直接讨论此点"），但 **reframing skill** 的规则 1「对话体→知识陈述体」倾向于产出断言式语言，系统性地去除了 reader 回答中的 hedge markers
- **schema 无 evidence_basis 字段**：card_type 区分"这张卡是什么"（mechanism/concept），但不区分"我们对它有多确信"
- **修正方向**：
  1. reframing skill 增加规则：保留 reader 的 hedge level，源是 blog/HN 的卡必须在正文中标注来源类型
  2. 可选：frontmatter 增加 `evidence_basis: experimental | theoretical | practitioner_report | community_discussion`

### 9.4 Backlink 不对称的正当性判断

- **21 comparison 卡是设计性 sink**（正确）——comparison 引用 subject，subject 不需要反引所有关于自己的 comparison
- **~200 条常规不对称边**：多数是批量处理导致——A 和 B 由不同 agent 独立处理，governance 发现 A→B 关系后只更新了 A 而未更新 B
- **修正方向**：governance 的 derive-related 步骤改为双向：写入 A→B 时同步写入 B→A（除非关系类型是 support/evidence，这类天然单向）

### 9.5 源巴尔干化的三种情况

| 源 | 自引率 | 判定 | 原因 |
|---|--------|------|------|
| wikibase-data-model | 100% | **Genuinely unique** | KB 无其他知识图谱/数据建模源，隔离是 scope gap 不是 link failure |
| arxiv-knowledge-compounding | 81.6% | **False alarm** | 实际有 11 条来自其他源的入站链接，内部密度高是多卡提取的自然结果 |
| arxiv-alce | 79.2% | **Bridge-link failure** | citation evaluation 概念与 ragchecker/ares 重叠但未建桥，governance 遗漏 |

### 9.6 遗留 TODO（需后续 workflow 执行）

- [ ] 对 27 个 webpage 源的 raw.html 执行结构化内容量化（tables/code/images 计数）
- [ ] 为 5 个优先 repo 生成 material_bundle.txt 并运行 extract pipeline
- [ ] reframing skill 增加 hedge preservation 规则
- [ ] ALCE ↔ RAGChecker ↔ ARES 补建 bridge links
- [ ] governance derive-related 改为双向写入
