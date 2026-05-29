# v3 KB 卡片索引

截至 2026-05-27，v3 KB 共有 **171** 张 `accepted` 卡片（其中 **8** 张携带 `v2_anchor` 反链 v2 accepted card）。全部卡片均通过 publication_gate（163 张 `new_card`）或 fusion_audit（8 张 `provenance_delta`）。

## 按 card_type 统计

| card_type | 数量 |
| --- | ---: |
| `mechanism` | 49 |
| `operational_rule` | 32 |
| `source_claim` | 30 |
| `distinction` | 27 |
| `concept` | 24 |
| `example_pattern` | 9 |
| **总计** | **171** |

## 按 source_id 聚合

| source_id | 卡片数 |
| --- | ---: |
| `arxiv-memory-as-metabolism` | 8 |
| `arxiv-etamp-memory-poisoning` | 8 |
| `arxiv-graph-poisoning` | 7 |
| `arxiv-longmemeval` | 7 |
| `arxiv-mem0` | 7 |
| `arxiv-memgpt` | 7 |
| `arxiv-wicer` | 7 |
| `arxiv-ares` | 6 |
| `arxiv-graphrag` | 6 |
| `arxiv-locomo` | 6 |
| `arxiv-alce` | 5 |
| `arxiv-lightmem` | 5 |
| `arxiv-poisonedrag` | 5 |
| `arxiv-ragchecker` | 5 |
| `arxiv-ragas` | 5 |
| `wikibase-data-model` | 5 |
| `karpathy-x-launch-post` | 4 |
| `falconer-enterprise-guide` | 4 |
| `obsidian-community-plugin` | 4 |
| `openaitoolshub-six-months` | 4 |
| `arxiv-zep` | 4 |
| `anthemcreation-fr-guide` | 3 |
| `hacker-news-original-thread` | 3 |
| `karpathy-gist-llm-wiki` | 3 |
| `developersio-jp-pattern` | 3 |
| `marvin-hn-persistent-knowledge` | 3 |
| `arxiv-knowledge-compounding` | 3 |
| `clawhub-llm-wiki-karpathy` | 3 |
| `pypi-llm-wiki-mcp` | 3 |
| `llm-wiki-net` | 3 |
| `complete-tech-live-frontier` | 2 |
| `aillm-wiki-directory` | 2 |
| `cognitionus-llm-wiki-guide` | 2 |
| `writethedocs-docs-as-code` | 2 |
| `anthemcreation-en-guide` | 2 |
| `kunal-local-knowledge-base` | 2 |
| `langchain-long-term-memory-docs` | 2 |
| `microsoft-agent-governance-toolkit-docs` | 2 |
| `pypi-my-llm-wiki` | 2 |
| `owasp-agentic-top10-2026` | 2 |
| `owasp-llm-top10-2025` | 2 |
| `robin-cartier-llm-knowledge-bases` | 2 |
| `nist-gai-profile` | 1 |

## 卡片清单（按 id 字母序）

| id | title | card_type | source_id | v2_anchor |
| --- | --- | --- | --- | --- |
| `agents-md-as-schema-layer` | AGENTS.md 充当 LLM Wiki 的 schema 层——让多轮 ingest 不发散 | `concept` | `complete-tech-live-frontier` | `llm-wiki-schema-configuration-document` |
| `aillm-wiki-four-defining-properties` | aillm.wiki 给 LLM Wiki 模式总结的四个定义性属性 | `distinction` | `aillm-wiki-directory` |  |
| `aillm-wiki-schema-as-bottleneck` | 在 LLM Wiki 三步工作流里，"挑 schema"才是真正的瓶颈 | `operational_rule` | `aillm-wiki-directory` |  |
| `alce-citation-recall-precision-nli` | ALCE 用 NLI 模型把 citation recall / precision 算成可重复的二元判定 | `operational_rule` | `arxiv-alce` |  |
| `alce-eli5-claim-recall-design` | ALCE 的 ELI5 claim-recall：用 InstructGPT 拆 3 条子主张，再让 NLI 判蕴含 | `mechanism` | `arxiv-alce` |  |
| `alce-prompting-strategies` | ALCE 实验里五种 prompting 策略的取舍 | `distinction` | `arxiv-alce` |  |
| `alce-retriever-and-context-utilization-gap` | ALCE 的 retrieval 分析揭示 "passage 越多不等于答案越好" 的 LLM 利用瓶颈 | `source_claim` | `arxiv-alce` |  |
| `alce-three-dimension-citation-metric` | ALCE 用 fluency / correctness / citation quality 三维度堵住作弊路径 | `mechanism` | `arxiv-alce` |  |
| `anthemcreation-llm-wiki-setup-cost-envelope` | LLM wiki 个人版的 5 分钟搭建路径与成本上限 | `operational_rule` | `anthemcreation-fr-guide` |  |
| `anthemcreation-llm-wiki-three-layer-architecture` | Karpathy 的 LLM wiki 是三层结构：原始源 / LLM 编译产物 / agents.md | `concept` | `anthemcreation-fr-guide` | `llm-wiki-three-layer-architecture` |
| `anthemcreation-llm-wiki-vs-rag-multi-hop` | LLM wiki 与 RAG 的差距不在速度而在推理深度 | `distinction` | `anthemcreation-fr-guide` |  |
| `ares-cross-domain-generalization-limits` | ARES 跨域可迁移：query/document 类型可变，但语言/代码/抽取跨域会塌 | `distinction` | `arxiv-ares` |  |
| `ares-gpt4-vs-human-annotation-tradeoff` | GPT-4 标注替代 human preference set：ARES 的 τ 退化 0.05–0.30 的成本 | `source_claim` | `arxiv-ares` |  |
| `ares-mock-rag-system-evaluation-design` | 用 mock RAG（已知准确率梯度）作为 ARES 自身的 ranking 基准 | `operational_rule` | `arxiv-ares` |  |
| `ares-ppi-confidence-bound` | ARES 用 PPI 把小标注集放大成带置信区间的 RAG 排名 | `mechanism` | `arxiv-ares` |  |
| `ares-synthetic-data-pipeline` | ARES 用合成 query–answer 训练小判官以替代人工标注 | `mechanism` | `arxiv-ares` |  |
| `ares-three-judge-rag-evaluation` | ARES 把 RAG 评估拆成三个独立判官 | `mechanism` | `arxiv-ares` |  |
| `audit-by-suspension-against-entrenchment` | AUDIT-by-Suspension：用反事实悬挂剥离"结构显著但功能空洞"的高引力条目 | `mechanism` | `arxiv-memory-as-metabolism` |  |
| `auto-index-replaces-rag-at-small-scale` | 小规模 wiki 下自维护索引可以替代 RAG | `operational_rule` | `karpathy-x-launch-post` |  |
| `beyond-the-token-bottleneck-llm-wiki-case-study` | Beyond the Token Bottleneck——120 页 Obsidian 实现 Karpathy LLM Wiki 模式的案例 | `example_pattern` | `complete-tech-live-frontier` |  |
| `cognition-human-approved-skill-md` | SKILL.md 写入闸门：人工审批作为团队级 agent 记忆的第一道安全机制 | `operational_rule` | `cognitionus-llm-wiki-guide` |  |
| `cognition-skill-loop-evidence-to-teaching` | Cognition 的"证据 → 巩固 → 衰减 → 教学"四步技能闭环 | `mechanism` | `cognitionus-llm-wiki-guide` |  |
| `docs-as-code-five-pillars` | Docs as Code 的五条工程工具栈定义 | `concept` | `writethedocs-docs-as-code` |  |
| `docs-as-code-merge-block-incentive` | 把"无文档不合并"写进 CI 是 Docs as Code 的关键激励机制 | `operational_rule` | `writethedocs-docs-as-code` |  |
| `enterprise-llm-wiki-drift-detection-loop` | 企业级 LLM Wiki 的 drift detection 必须连续运行并按 owner 路由 | `mechanism` | `falconer-enterprise-guide` | `llm-wiki-health-checks` |
| `enterprise-llm-wiki-four-properties` | 企业级 LLM Wiki 必须同时具备 capture / link / compound / stay current 四性 | `concept` | `falconer-enterprise-guide` |  |
| `enterprise-llm-wiki-tool-native-ingestion` | 企业级 LLM Wiki 必须 tool-native 摄取，不能依赖 raw 目录 | `operational_rule` | `falconer-enterprise-guide` |  |
| `etamp-attack-payload-structure` | eTAMP 攻击 payload 的三段式结构：Importance Signal + Trigger Condition + Attack Goal | `mechanism` | `arxiv-etamp-memory-poisoning` |  |
| `etamp-capability-vs-security` | 模型能力越强 ≠ 越安全：GPT-5.2 在 authority framing 下显著脆弱 | `distinction` | `arxiv-etamp-memory-poisoning` |  |
| `etamp-chaos-monkey-agent-robustness` | Chaos Monkey for Agents：用概率性扰动模拟真实 web 环境压力 | `operational_rule` | `arxiv-etamp-memory-poisoning` |  |
| `etamp-direction-asymmetry-and-stealth` | 跨 site 攻击方向的非对称 ASR 与 ASR_A 接近零的攻击隐蔽性 | `source_claim` | `arxiv-etamp-memory-poisoning` |  |
| `etamp-environment-injected-memory-poisoning` | eTAMP：仅靠环境观测就能完成跨 session、跨 site 的 web agent 记忆投毒 | `concept` | `arxiv-etamp-memory-poisoning` |  |
| `etamp-frustration-exploitation` | Frustration Exploitation：受环境压力的 agent 对注入指令易感性最高放大 8 倍 | `source_claim` | `arxiv-etamp-memory-poisoning` |  |
| `etamp-long-context-recall-diagnostic` | 长上下文 recall 诊断：把"召不回"与"不服从"区分开 | `operational_rule` | `arxiv-etamp-memory-poisoning` |  |
| `etamp-pseudo-trajectory-methodology` | Pseudo vs non-pseudo trajectory：用 PR=100% 控制变量隔离攻击效力 | `operational_rule` | `arxiv-etamp-memory-poisoning` |  |
| `file-outputs-back-as-compounding-loop` | 把查询输出回写进 wiki 形成复利循环 | `operational_rule` | `karpathy-x-launch-post` |  |
| `gragpoison-additive-vs-edit-attack` | GraphRAG 投毒的两条家族：additive injection vs in-place edit | `distinction` | `arxiv-graph-poisoning` |  |
| `graphrag-adaptive-benchmark-via-personas` | 用"persona × task × question"自适应生成全局意义建构基准 | `operational_rule` | `arxiv-graphrag` |  |
| `graphrag-context-window-8k-optimal` | GraphRAG 用 8K 上下文窗口反而压过 16K/32K/64K——"小窗口"更全 | `source_claim` | `arxiv-graphrag` |  |
| `graphrag-global-sensemaking-pipeline` | GraphRAG 把 RAG 改造成"全局意义建构"的两阶段流水线 | `mechanism` | `arxiv-graphrag` |  |
| `graphrag-leiden-community-hierarchy` | 分层 Leiden 社群作为 GraphRAG 的"全局摘要索引" | `mechanism` | `arxiv-graphrag` |  |
| `graphrag-manipulation-only-attack-surface` | GraphRAG 的"只改字、不加文"攻击面 | `concept` | `arxiv-graph-poisoning` |  |
| `graphrag-pipeline-formalism` | GraphRAG 流水线的形式化：为什么 LLM 不直接看 chunk | `concept` | `arxiv-graph-poisoning` |  |
| `graphrag-root-community-token-efficiency` | GraphRAG 根级社群摘要（C0）以 ~2% token 成本接近全局方法效果 | `source_claim` | `arxiv-graphrag` |  |
| `graphrag-self-reflection-gleaning` | GraphRAG 用 "self-reflection gleaning" 抵消大 chunk 的实体召回损失 | `operational_rule` | `arxiv-graphrag` |  |
| `graphrag-text-defense-blind-spot` | 现有文本侧防御为何对 GraphRAG 投毒近乎失明 | `source_claim` | `arxiv-graph-poisoning` |  |
| `hn-llm-wiki-is-just-rag-debate` | HN 关于"LLM Wiki 只是 RAG"的争论——retrieval ≠ write loop | `distinction` | `hacker-news-original-thread` |  |
| `hn-source-granularity-changes-synthesis-quality` | HN 实证——源文件粒度是 LLM Wiki 合成质量的杠杆 | `example_pattern` | `hacker-news-original-thread` |  |
| `hn-writing-as-thinking-vs-llm-wiki` | HN 反对意见——委托写作给 LLM 等于让"思考"被外包 | `distinction` | `hacker-news-original-thread` |  |
| `idea-file-as-agent-era-artifact` | idea file 是智能体时代的分发载体 | `concept` | `karpathy-x-launch-post` | `idea-file-abstract-vague` |
| `karpathy-gist-bookkeeping-burden` | 个人 wiki 真正崩溃的不是读和想，而是"维护成本指数增长"——LLM 把它降到零 | `concept` | `karpathy-gist-llm-wiki` |  |
| `karpathy-gist-memex-connection` | LLM Wiki 是 Vannevar Bush Memex 的"现代化解法"——补上了"谁来维护"这块缺失拼图 | `source_claim` | `karpathy-gist-llm-wiki` |  |
| `karpathy-gist-three-layers` | Karpathy gist 把 LLM Wiki 形式化成"raw / wiki / schema"三层，每层的所有权严格分离 | `distinction` | `karpathy-gist-llm-wiki` | `llm-wiki-three-layer-architecture` |
| `karpathy-llm-kb-three-layer-arch` | Karpathy "LLM Knowledge Base" 的三层架构：Raw / Schema / Wiki | `concept` | `developersio-jp-pattern` | `llm-wiki-three-layer-architecture` |
| `karpathy-llm-kb-three-operations` | Karpathy "LLM KB" 的三个操作：Ingest / Query / Lint，与 Query 的 "filing back" | `mechanism` | `developersio-jp-pattern` |  |
| `karpathy-llm-wiki-obsidian-plugin-overview` | Karpathy LLM Wiki 的 Obsidian 插件实现：把 Karpathy 三层架构落地到日常写作流 | `example_pattern` | `obsidian-community-plugin` |  |
| `karpathy-llm-wiki-source-executable-analogy` | Karpathy 把 LLM wiki 比作"源码 vs 编译产物" | `distinction` | `anthemcreation-en-guide` |  |
| `karpathy-llm-wiki-three-layers` | Karpathy LLM Wiki 的三层 + 三操作：raw / wiki / schema + Ingest / Query / Lint | `concept` | `marvin-hn-persistent-knowledge` | `llm-wiki-three-layer-architecture` |
| `karpathy-llm-wiki-vs-rag` | LLM Wiki 与 RAG 的根本区别：wiki 是会被复利的 compiled artifact，RAG 是 transient 答案 | `distinction` | `marvin-hn-persistent-knowledge` |  |
| `karpathy-wiki-aliases-and-dedup` | 强制别名 + 两层语义重复检测：跨语言去重的工程承诺 | `mechanism` | `obsidian-community-plugin` |  |
| `karpathy-wiki-extraction-granularity` | 五档抽取粒度（Minimal / Coarse / Standard / Fine / Custom）：把成本与深度变成可调的旋钮 | `operational_rule` | `obsidian-community-plugin` |  |
| `karpathy-wiki-full-context-vs-rag` | "Feed full wiki context, not chunked RAG retrieval"——Karpathy 立场在插件中的执行 | `distinction` | `obsidian-community-plugin` |  |
| `knowledge-compounding-dynamic-roi` | 知识复利让 Agentic ROI 的成本项从常量变为时间函数 Cost(t) | `mechanism` | `arxiv-knowledge-compounding` |  |
| `knowledge-compounding-three-mechanisms` | 知识复利的三个微观机制：INGEST 摊销 / answer 回灌 / 外部检索写回 | `mechanism` | `arxiv-knowledge-compounding` |  |
| `knowledge-compounding-tokens-as-capital` | 把 LLM token 从"消耗品"重新归类为"资本品" | `distinction` | `arxiv-knowledge-compounding` |  |
| `kunal-llm-c-rag-misinterpretation` | "LLM Wiki"在 SEO 内容里被错认成"llm.c 上的本地 RAG"——一个值得标注的术语漂移 | `distinction` | `kunal-local-knowledge-base` |  |
| `kunal-local-setup-walls` | 本地 RAG 自建的三堵墙：macOS 编译、文档预处理、推理硬件 | `operational_rule` | `kunal-local-knowledge-base` |  |
| `langgraph-store-namespace-key-json-model` | LangGraph Store 的命名空间-键-JSON 文档存储模型 | `concept` | `langchain-long-term-memory-docs` |  |
| `langgraph-tool-runtime-store-access` | 通过 ToolRuntime 让工具读写 LangGraph Store | `operational_rule` | `langchain-long-term-memory-docs` |  |
| `lightmem-complexity-formula` | LightMem 的成本公式——O(N) 降到 O(Nr^x T/th) 的来源拆解 | `source_claim` | `arxiv-lightmem` |  |
| `lightmem-light2-topic-aware-stm` | LightMem 的 Light2 STM——以 topic 为输入粒度的"批 summary" | `mechanism` | `arxiv-lightmem` |  |
| `lightmem-precompress-and-topic-segmentation` | LightMem 的感觉记忆——LLMLingua-2 预压缩 + 注意力∩相似度的话题分段 | `mechanism` | `arxiv-lightmem` |  |
| `lightmem-sleep-time-offline-parallel-update` | LightMem 的"睡眠时更新"——把 LTM 整合从在线推理中解耦 | `mechanism` | `arxiv-lightmem` |  |
| `lightmem-three-stage-atkinson-shiffrin` | LightMem 把 Atkinson–Shiffrin 三级人类记忆移植成 LLM agent 的三层记忆架构 | `mechanism` | `arxiv-lightmem` |  |
| `llm-knowledge-base-five-stage-workflow` | LLM 维护的知识库五阶段工作流 | `mechanism` | `karpathy-x-launch-post` |  |
| `llm-wiki-contradictions-are-assets` | 矛盾不是 wiki 的 bug 而是资产——别让 LLM 重写，要让它标注 | `distinction` | `openaitoolshub-six-months` |  |
| `llm-wiki-ingest-vs-query-workflow` | LLM wiki 工作流分 ingest（写入侧）与 query（读取侧）两步 | `mechanism` | `anthemcreation-en-guide` |  |
| `llm-wiki-karpathy-lint-grounding-trail` | kb_lint 强制 wiki 内容必须有 grounding trail | `operational_rule` | `clawhub-llm-wiki-karpathy` |  |
| `llm-wiki-karpathy-multimodal-representation-path` | 非文本资产走 representation-first ingest 路径 | `mechanism` | `clawhub-llm-wiki-karpathy` |  |
| `llm-wiki-karpathy-runtime-vs-agent-split` | llm-wiki-karpathy 的 runtime / agent 责任分割 | `distinction` | `clawhub-llm-wiki-karpathy` |  |
| `llm-wiki-mcp-design-boundary-mechanics-not-content` | llm-wiki-mcp 的设计边界：server 只管 mechanics，schema 留给 wiki/CLAUDE.md | `distinction` | `pypi-llm-wiki-mcp` |  |
| `llm-wiki-mcp-four-tools` | llm-wiki-mcp 的四个 MCP 工具：read / write_page / log_append / inventory | `operational_rule` | `pypi-llm-wiki-mcp` |  |
| `llm-wiki-mcp-skills-vs-tools-workflow` | llm-wiki-mcp 的 skill 层 vs tool 层：工具给能力，skill 给 workflow | `distinction` | `pypi-llm-wiki-mcp` |  |
| `llm-wiki-rohit-v2-improvements` | Rohit v2 在 Karpathy 原始 gist 上加的三件事：Lifecycle / Typed Links / Contradiction Protocol | `mechanism` | `openaitoolshub-six-months` |  |
| `llm-wiki-schema-is-most-important` | schema.md 是 LLM Wiki 里最重要的文件——Karpathy gist 没说够 | `operational_rule` | `openaitoolshub-six-months` |  |
| `llm-wiki-tldr-load-bearing` | TL;DR 强制规则比 index 更省 context window——load-bearing 设计 | `operational_rule` | `openaitoolshub-six-months` |  |
| `locomo-event-summarization-five-error-types` | LoCoMo 给 LLM 事件摘要错误划出五类——失败模式比 ROUGE 分数更可操作 | `concept` | `arxiv-locomo` |  |
| `locomo-long-context-adversarial-collapse` | LoCoMo——长上下文 LLM 在 adversarial 问题上崩到 2.1%，是 "能塞 ≠ 能懂" 的清晰证据 | `source_claim` | `arxiv-locomo` |  |
| `locomo-observation-rag-beats-summary-rag` | RAG 检索单元用"observation"比 session 摘要更适合长对话 QA | `operational_rule` | `arxiv-locomo` |  |
| `locomo-persona-event-graph-pipeline` | LoCoMo 的对话生成靠 persona + 时间事件图 + reflect/respond 三件套 | `mechanism` | `arxiv-locomo` |  |
| `locomo-three-task-evaluation-framework` | LoCoMo 用 QA + 事件摘要 + 多模态对话三任务测量"长期记忆" | `concept` | `arxiv-locomo` |  |
| `locomo-very-long-term-dialogue-dataset` | LoCoMo 把"超长期对话"定义为 9K token、19 个 session 的量级 | `source_claim` | `arxiv-locomo` |  |
| `longmemeval-benchmark-construction-pipeline` | LongMemEval 的"persona 属性 → 自对话 → 大海捞针拼装"构造管线 | `mechanism` | `arxiv-longmemeval` |  |
| `longmemeval-chain-of-note-and-json-reading` | Chain-of-Note + JSON 结构化 prompt 即使在 oracle 检索下也能涨 10 分 | `operational_rule` | `arxiv-longmemeval` |  |
| `longmemeval-commercial-system-failure-modes` | LongMemEval pilot study——ChatGPT 与 Coze 在长记忆上的两种失败模式 | `source_claim` | `arxiv-longmemeval` |  |
| `longmemeval-five-core-memory-abilities` | LongMemEval 把"长期记忆"切成五种能力，KU/ABS 是它独有的 | `concept` | `arxiv-longmemeval` |  |
| `longmemeval-key-expansion-with-facts` | K = V + fact 比裸 value 平均 +9.4% recall、+5.4% QA 准确率 | `operational_rule` | `arxiv-longmemeval` |  |
| `longmemeval-three-stage-memory-framework` | 把 long-term memory 系统拆成 indexing / retrieval / reading 三阶段四控制点 | `concept` | `arxiv-longmemeval` |  |
| `longmemeval-time-aware-query-expansion` | 时间感知的索引与 query 扩展能把 temporal 召回提 6.8-11.3% | `mechanism` | `arxiv-longmemeval` |  |
| `mem0-answer-generation-prompt-design` | Mem0 的"答案生成 prompt"把时间换算与冲突仲裁写成显式指令 | `operational_rule` | `arxiv-mem0` |  |
| `mem0-baseline-failure-modes` | Mem0 论文里 5 个 baseline 各自的失败模式（不是统一败给 Mem0） | `distinction` | `arxiv-mem0` |  |
| `mem0-extract-update-pipeline` | Mem0 提取-更新两阶段管线：把每对消息变成可增量管理的事实 | `mechanism` | `arxiv-mem0` |  |
| `mem0-graph-memory-variant` | Mem0g 图记忆变体：实体-关系三元组 + 冲突解决，专攻时序与开放域 | `mechanism` | `arxiv-mem0` |  |
| `mem0-locomo-benchmark-evaluation` | Mem0 在 LOCOMO 上的评估：质量、token、延迟三轴的"性价比"故事 | `source_claim` | `arxiv-mem0` |  |
| `mem0-rag-chunk-size-ablation` | Mem0 的 RAG 基线扫表显示"块大小×k 个数"曲线非单调 | `source_claim` | `arxiv-mem0` |  |
| `mem0-tool-call-add-update-delete-noop` | Mem0 的 ADD/UPDATE/DELETE/NOOP：让 LLM 自己决定记忆该怎么改 | `mechanism` | `arxiv-mem0` |  |
| `memgpt-dmr-task-evaluation` | MemGPT 的 Deep Memory Retrieval 任务：把"记得住"做成可量化的 consistency 指标 | `source_claim` | `arxiv-memgpt` |  |
| `memgpt-docqa-pagination-failure-mode` | MemGPT 在 DocQA 上能突破 retriever top-K 限制，但**早停 paging** 是它的真实失败模式 | `example_pattern` | `arxiv-memgpt` |  |
| `memgpt-function-chaining-heartbeat` | MemGPT 的 request_heartbeat 标志位让函数调用可以串成多步检索 | `mechanism` | `arxiv-memgpt` |  |
| `memgpt-main-vs-external-context` | MemGPT 的"内存分层"由 3+2 五个具名区组成，每个区角色和写规则都不同 | `mechanism` | `arxiv-memgpt` |  |
| `memgpt-nested-kv-multi-hop` | 嵌套 KV 基准证明"上下文内多跳"瓶颈不是上下文长度而是迭代查询 | `example_pattern` | `arxiv-memgpt` |  |
| `memgpt-queue-eviction-policy` | MemGPT 用"警告水位—溢出—递归摘要"三段策略管 FIFO 队列驱逐 | `operational_rule` | `arxiv-memgpt` |  |
| `memgpt-virtual-context-os-analogy` | MemGPT 把上下文窗口当 RAM、外部存储当磁盘，给 LLM "OS 化"管自己的内存 | `concept` | `arxiv-memgpt` |  |
| `memory-as-metabolism-architectural-separability` | 架构可分离性：把 wiki 留在权重之外是安全承诺，不是工程便利 | `operational_rule` | `arxiv-memory-as-metabolism` |  |
| `memory-as-metabolism-conflict-routing-matrix` | §5.0 冲突路由矩阵：把"mirror vs compensate"程序化为 7 类显式路由 | `operational_rule` | `arxiv-memory-as-metabolism` |  |
| `memory-as-metabolism-contextualize-depth-fitted` | CONTEXTUALIZE：把外部源按用户当前 working-context depth 压缩，强制保留 linkout | `mechanism` | `arxiv-memory-as-metabolism` |  |
| `memory-as-metabolism-five-operations` | 伴侣记忆的五操作架构（TRIAGE / CONTEXTUALIZE / DECAY / CONSOLIDATE / AUDIT） | `mechanism` | `arxiv-memory-as-metabolism` |  |
| `memory-as-metabolism-mirror-vs-compensate` | 伴侣记忆的"镜像-补偿"设计原则 | `operational_rule` | `arxiv-memory-as-metabolism` |  |
| `memory-gravity-load-bearing-protection` | Memory Gravity：用结构承重保护知识基础，对抗"绝对在位陷阱" | `mechanism` | `arxiv-memory-as-metabolism` |  |
| `microsoft-agent-governance-eight-packages` | 微软 Agent Governance Toolkit 用八个包切分智能体治理面 | `concept` | `microsoft-agent-governance-toolkit-docs` |  |
| `microsoft-agent-governance-standards-alignment` | Agent Governance Toolkit 把四份外部合规标准做成可自动核验项 | `source_claim` | `microsoft-agent-governance-toolkit-docs` |  |
| `minority-pressure-promotion` | 少数派 buffer 压力 promotion：让多周期累积的反对证据有结构性翻盘通道 | `mechanism` | `arxiv-memory-as-metabolism` |  |
| `morishige-kb-compile-mem0-overlay` | 在 Mem0 + pgvector 之上叠 LLM Wiki：森茂的 /kb-compile 落地实践 | `example_pattern` | `developersio-jp-pattern` |  |
| `my-llm-wiki-supported-source-types` | my-llm-wiki 用 Tree-sitter + Docling + 视觉 OCR 覆盖代码/办公文档/图像 | `source_claim` | `pypi-my-llm-wiki` |  |
| `my-llm-wiki-three-layer-implementation` | my-llm-wiki 把 Karpathy 三层架构落地成 Obsidian-vault 工具 | `example_pattern` | `pypi-my-llm-wiki` |  |
| `nist-ai-rmf-gai-profile` | NIST AI 600-1 是 AI RMF 1.0 针对生成式 AI 的跨行业 profile | `source_claim` | `nist-gai-profile` |  |
| `nvk-llm-wiki-audit-and-librarian` | nvk/llm-wiki 的 audit + librarian——把"信任评估"做成可重复 workflow | `operational_rule` | `llm-wiki-net` |  |
| `nvk-llm-wiki-hub-and-topic-wikis` | nvk/llm-wiki 的 Hub + Topic-Wikis 结构——一题一库，互不污染 | `concept` | `llm-wiki-net` |  |
| `nvk-llm-wiki-parallel-multi-agent-research` | nvk/llm-wiki 的并行多 agent 研究流程——5/8/10 个 agent + 多轮 gap-driven | `mechanism` | `llm-wiki-net` |  |
| `obsidian-as-ide-llm-as-programmer` | Karpathy 的类比：Obsidian 是 IDE，LLM 是程序员，wiki 是 codebase | `concept` | `marvin-hn-persistent-knowledge` |  |
| `owasp-agentic-top10-2026-positioning` | OWASP Agentic Top 10 (2026) 的定位与受众 | `source_claim` | `owasp-agentic-top10-2026` |  |
| `owasp-agentic-vs-llm-top10-2025` | OWASP 为什么把 Agentic Top 10 与 LLM Top 10 分开列 | `distinction` | `owasp-agentic-top10-2026` |  |
| `owasp-genai-landscape-2026q2` | OWASP 2026 Q2 三件套：把"Top 10"扩成"防御方案地图" | `example_pattern` | `owasp-llm-top10-2025` |  |
| `owasp-llm-top10-community-genealogy` | OWASP Top 10 for LLM Applications：从社区议题列表到 LLM 安全治理坐标 | `concept` | `owasp-llm-top10-2025` |  |
| `poisonedrag-baselines-isolate-two-conditions` | PoisonedRAG 的五个基线分别"丢"哪一个条件 | `distinction` | `arxiv-poisonedrag` |  |
| `poisonedrag-existing-defenses-insufficient` | 四类现成防御都挡不住 PoisonedRAG | `source_claim` | `arxiv-poisonedrag` |  |
| `poisonedrag-knowledge-database-attack-surface` | RAG 的知识库是一个新的、可低成本投毒的攻击面 | `concept` | `arxiv-poisonedrag` |  |
| `poisonedrag-retrieval-generation-two-conditions` | PoisonedRAG 把"投毒文本"拆成检索条件+生成条件两段 | `mechanism` | `arxiv-poisonedrag` |  |
| `poisonedrag-survives-advanced-rag-and-agents` | PoisonedRAG 在 Self-RAG / CRAG / 真实 Wikipedia / LLM 智能体上同样有效 | `source_claim` | `arxiv-poisonedrag` |  |
| `rag-chunk-level-faithfulness` | RAG 生成器的"chunk 级 faithfulness"现象 | `source_claim` | `arxiv-ragchecker` |  |
| `ragas-answer-relevance-metric` | Ragas Answer Relevance：让 LLM 从 answer 反推 question，再用 embedding 算相似度 | `mechanism` | `arxiv-ragas` |  |
| `ragas-context-relevance-metric` | Ragas Context Relevance：让 LLM 抽出 crucial 句子，再算占比 | `mechanism` | `arxiv-ragas` |  |
| `ragas-faithfulness-metric` | Ragas Faithfulness：先把 answer 拆成 statements，再逐条对 context 做 LLM 验证 | `mechanism` | `arxiv-ragas` |  |
| `ragas-reference-free-rag-evaluation` | Ragas 框架：无需 ground truth 也能评估 RAG 的三维度自动评测 | `concept` | `arxiv-ragas` |  |
| `ragas-wikieval-dataset` | WikiEval：为验证 reference-free RAG 指标而构造的 50 题 Wikipedia 数据集 | `example_pattern` | `arxiv-ragas` |  |
| `ragchecker-claim-entailment-decomposition` | RAGChecker 的评估原子：把回答拆成 claim，再做 entailment 判断 | `mechanism` | `arxiv-ragchecker` |  |
| `ragchecker-generator-trilemma` | RAG 生成器的三难：faithfulness × context utilization × noise sensitivity | `distinction` | `arxiv-ragchecker` |  |
| `ragchecker-retriever-claim-vs-chunk-precision` | RAGChecker 检索端的非对称——claim-level recall vs chunk-level precision | `distinction` | `arxiv-ragchecker` |  |
| `ragchecker-tuning-knobs-saturate` | RAGChecker 给 RAG 调优者的四个具体结论 | `operational_rule` | `arxiv-ragchecker` |  |
| `retrieval-not-enough-for-stale-kb` | 检索工具无法解决"知识库陈旧"问题，只会更快地给出错答案 | `distinction` | `falconer-enterprise-guide` |  |
| `robin-cartier-scale-ceiling` | Karpathy 风 LLM Wiki 的实战上限：约 200 页 / 100K tokens 后必须降级到子 wiki 或 RAG | `operational_rule` | `robin-cartier-llm-knowledge-bases` |  |
| `robin-cartier-schema-as-product-doc` | 真正的创新不是 wiki 而是 schema 文件——"给 AI 同事的活产品需求文档" | `source_claim` | `robin-cartier-llm-knowledge-bases` | `llm-wiki-schema-configuration-document` |
| `tkpa-graph-guided-targeted-poisoning` | TKPA：用图论结构定位"该改哪一段"的定向投毒 | `mechanism` | `arxiv-graph-poisoning` |  |
| `ukpa-coreference-disruption` | UKPA：通过破坏指代链让 GraphRAG 的实体合并全面失败 | `mechanism` | `arxiv-graph-poisoning` |  |
| `ukpa-edit-distance-stealth-tradeoff` | UKPA 的"编辑距离 ≤3"甜点：再大就只涨困惑度、不涨攻击力 | `source_claim` | `arxiv-graph-poisoning` |  |
| `wicer-blind-compilation-catastrophic-loss` | 盲编译 wiki 会 2–3 倍超压并丢失关键事实 | `source_claim` | `arxiv-wicer` |  |
| `wicer-cegar-compile-evaluate-refine` | WiCER 把 wiki 编译当作 CEGAR 抽象细化 | `mechanism` | `arxiv-wicer` |  |
| `wicer-fc-rag-document-count-crossover` | 全上下文 KV cache 与 RAG 在文档数处发生质量翻转 | `distinction` | `arxiv-wicer` |  |
| `wicer-hardware-architecture-deployment` | WiCER 跨硬件部署画像：M4 Pro / RTX 4090 / Inferentia2 | `distinction` | `arxiv-wicer` |  |
| `wicer-llm-judge-human-validation` | WiCER 的 LLM-as-judge 与人评 Pearson r=0.94 的 n=100 验证 | `source_claim` | `arxiv-wicer` |  |
| `wicer-recovery-distribution-exceeds-fc-raw` | WiCER 在三个主题上超越 FC raw 基线（>100% recovery） | `source_claim` | `arxiv-wicer` |  |
| `wicer-targeted-vs-random-pinning-ablation` | 钉机制本身只值 +0.16，是"诊断"在做事 | `source_claim` | `arxiv-wicer` |  |
| `wikibase-conceptual-not-serialization` | Wikibase 数据模型是"概念模型"——不规定实现、不规定序列化、不规定形式语义 | `source_claim` | `wikibase-data-model` |  |
| `wikibase-item-property-snak-statement` | Wikibase 数据模型的四个核心结构——Item / Property / Snak / Statement | `concept` | `wikibase-data-model` |  |
| `wikibase-statement-rank-and-references` | Statement 的 Rank 与 ReferenceRecord——并存多值的筛选机制 | `mechanism` | `wikibase-data-model` |  |
| `wikibase-three-snak-types` | 三种 Snak——区分"未填"、"无值"、"未知值" | `distinction` | `wikibase-data-model` |  |
| `wikibase-timevalue-uncertain-dates` | Wikibase 的 TimeValue 用 precision + before/after 表达不确定日期 | `mechanism` | `wikibase-data-model` |  |
| `zep-bi-temporal-edges` | Zep 用双时间线 + 边失效让事实"会过期"而不是被覆盖 | `mechanism` | `arxiv-zep` |  |
| `zep-dmr-benchmark-critique` | DMR 已被 60 条消息的 full-context 打到 98%，不再适合评估长程记忆 | `source_claim` | `arxiv-zep` |  |
| `zep-graphiti-three-tier-graph` | Zep/Graphiti 用三层子图（情节-实体-社区）显式区分情节记忆与语义记忆 | `mechanism` | `arxiv-zep` |  |
| `zep-hybrid-search-rerank` | Zep 的检索把 cos+BM25+BFS 三路覆盖三种"相似性"，再叠多种重排器 | `mechanism` | `arxiv-zep` |  |

## v2-anchored 卡片（fusion_audit 通过的 `provenance_delta`）

下列 8 张 v3 卡片在 v2 accepted KB 中有同主题锚卡，本卡作为 delta / 扩展 / 第三方实现而被采纳：

- `agents-md-as-schema-layer` — AGENTS.md 充当 LLM Wiki 的 schema 层 ↔ v2 `llm-wiki-schema-configuration-document`
- `anthemcreation-llm-wiki-three-layer-architecture` — Karpathy 的 LLM wiki 是三层结构 ↔ v2 `llm-wiki-three-layer-architecture`
- `enterprise-llm-wiki-drift-detection-loop` — 企业级 drift detection 必须连续运行 ↔ v2 `llm-wiki-health-checks`
- `idea-file-as-agent-era-artifact` — idea file 是智能体时代的分发载体 ↔ v2 `idea-file-abstract-vague`
- `karpathy-gist-three-layers` — Karpathy gist 的 raw / wiki / schema 三层所有权严格分离 ↔ v2 `llm-wiki-three-layer-architecture`
- `karpathy-llm-kb-three-layer-arch` — Karpathy "LLM KB" 的 Raw / Schema / Wiki 三层 ↔ v2 `llm-wiki-three-layer-architecture`
- `karpathy-llm-wiki-three-layers` — Karpathy LLM Wiki 的三层 + 三操作 ↔ v2 `llm-wiki-three-layer-architecture`
- `robin-cartier-schema-as-product-doc` — 真正的创新不是 wiki 而是 schema 文件 ↔ v2 `llm-wiki-schema-configuration-document`

## 备注

- 全部 171 张 v3 卡片的 frontmatter 在 adoption 阶段已把 `status: draft` 改为 `status: accepted`，`edited_time` 更新为 adoption 时间。
- 每张卡片的 `provenance_card` 字段仍指向 `../provenance/<id>.md`（kb 与 drafts 目录镜像，相对路径解析一致）。
- 每张卡片的 `related: [...]` 字段在 interlink 阶段已填充（共 974 条边，平均 5.70 / 卡），id 引用对应其他 v3 卡片。
- 8 张 `provenance_delta` 卡的 kb provenance 文件包含 `v2_anchor:` 块，记录 v2 锚卡 id 与路径——未来如果需要把 comparison 反向写到 v2 accepted card provenance，依据是 kb provenance 与 `outputs/llm_wiki/drafts/comparison/<id>.md`。
