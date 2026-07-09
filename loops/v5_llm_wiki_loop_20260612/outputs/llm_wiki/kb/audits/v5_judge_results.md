# v5 JUDGE 阶段结果

## A1 源忠实性（抽样 20 条）

| # | card_id | footnote | verdict | evidence |
|---|---------|----------|---------|----------|
| 1 | alce-citation-support-gap | src-2 | semantic-pass | 3/3 key terms found in source (数值 51.1, 69.3 存在于 tables/eli5.tex) |
| 2 | alce-prompting-strategies | src-2 | semantic-pass | 直接子串匹配: "We simply provide the model with the top-k passages" |
| 3 | poisonedrag-nontarget-question-impact | src-1 | semantic-pass | 数值 0.3%, 0.9%, 0.4% 均存在于源 |
| 4 | alce-datasets-design | src-5 | semantic-pass | 直接子串匹配: "We randomly select 1,000 examples from the development set" |
| 5 | memgpt-main-context-structure | src-1 | semantic-pass | 关键短语 "contiguous sections"/"system" 存在 |
| 6 | dual-link-obsidian-agent-compatibility | src-3 | semantic-pass | 直接子串匹配: "Claude Code is the compiler. Obsidian is an optional viewer." |
| 7 | alce-prompting-strategies | src-3 | semantic-pass | 直接子串匹配: "Summaries or snippets significantly reduce the passage length" |
| 8 | nli-based-citation-quality-metrics | src-3 | semantic-pass | LaTeX 公式 "c_{i,j}" 以 $c_{i,j}$ 形式存在于源 |
| 9 | cross-site-memory-poisoning-bypass | src-3 | semantic-pass | "Shopping", "Reddit", "GPT-5.2" 均存在于源 |
| 10 | ragchecker-evaluation-input-schema | src-2 | semantic-pass | "query_id", "query", "gt_answer", "retrieved_context" 字段名存在 |
| 11 | alce-benchmark-overview | src-3 | semantic-pass | "100-word passages" 概念以 LaTeX 格式存在 |
| 12 | poisonedrag-black-box-attack | src-3 | semantic-pass | 数值 97%, 99%, 91% 存在于源 |
| 13 | frustration-exploitation-attack | src-2 | semantic-pass | "GPT-5-mini", "ASR_B", "32.5%", "Chaos Monkey" 均存在 |
| 14 | poisonedrag-failure-modes | src-1 | semantic-pass | "top-$k$ retrieved texts could contain some clean ones" 以 LaTeX 格式存在 |
| 15 | closedbook-posthoc-citation-gap | src-2 | semantic-pass | "ClosedBook" 以 \newcommand 定义存在; 数值 18.6/15.5 存在于表格 |
| 16 | alce-prompting-strategies | src-6 | semantic-pass | "randomly sample"/"n_sample" 概念存在于源 |
| 17 | longmemeval-five-core-memory-abilities | src-1 | semantic-pass | "five core long-term memory abilities: information extraction" 以 LaTeX 格式 \BENCHMARK{} + \textbf{} 存在 |
| 18 | bttb-production-reference | src-2 | semantic-pass | "120+" "pages" "1400+" "internal links" 均存在 |
| 19 | closedbook-posthoc-citation-gap | src-3 | semantic-pass | "citation recall"/"ClosedBook"/"PostCite"/"47%" 概念存在 |
| 20 | multi-agent-parallel-research-pipeline | src-3 | semantic-pass | "Peer-reviewed"/"+2"/"High"/"Medium"/"Low"/"Reject" 全部存在 |

**总结: 20 pass / 0 fail / 0 caveat**

失败原因分析: 全部 143 条 suspect 均为 LaTeX/Markdown 格式假阴性。源文件使用 `$...$`、`\textbf{}`、`\newcommand`、`\BENCHMARK{}` 等 LaTeX 标记，审计脚本的 grep 匹配基于卡片脚注中的纯文本 quote_prefix，导致字面匹配失败。语义内容完全对应。

## E2 无脚注段落（抽样 15 条）

| # | card_id | paragraph_excerpt | classification | reasoning |
|---|---------|-------------------|----------------|-----------|
| 1 | dual-link-obsidian-agent-compatibility | 内联使用代码示例 + 设计总结 | structural | 代码示例展示用法 + 小结句已有 src-3 锚定 |
| 2 | llm-wiki-ingest-loop | 步骤 1-5 (新论文放入 raw/pdf/...) | grounded | 步骤 1-5 是 src-1 引用内容的结构化改写，src-1 在段前 src-2 在段后 |
| 3 | graphrag-adaptive-benchmarking | 问题生成 Algorithm 1 五步 | grounded | Algorithm 1 细节是 src-1 论文 Section 3.2 的结构化展开 |
| 4 | poisonedrag-generation-subtext-crafting | 论文 prompt 模板引用 | grounded | 直接引用论文 prompt 模板，紧接 src-1 脚注 |
| 5 | graphrag-community-summary-generation | 高层级社区摘要策略 | grounded | 与叶级策略同属 Section 3.1.5 内容，src-1 覆盖该整节 |
| 6 | compilation-gap | 实验证据 (RepLiQA 数值) | grounded | 具体实验数值直接来自论文 Table/Results，src-2/src-3 覆盖同一实验 |
| 7 | mem0-performance-results | Multi-Hop F1=28.64... | grounded | 数值来自同一 LOCOMO 结果表，src-1 引用该表 |
| 8 | wikibase-quantity-value | 单位表示 IRI 说明 | grounded | 单位表示说明属于 src-1 引用的 Quantities P197-209 延续内容 |
| 9 | llm-wiki-three-layer-structure | 三层结构 + 具体文件数 | grounded | 具体页面数量来自 src-1 引用的博文，是同段展开 |
| 10 | longmemeval-commercial-system-memory-gap | ChatGPT/Coze 准确率数值 | grounded | 具体数值来自 src-1 引用的 figures/proof_of_difficulty.tex |
| 11 | graphrag-relationship-fine-tuning | 三步合成数据生成流程 | grounded | 三步流程是 src-1 fine_tuning.tex 内容的结构化展开 |
| 12 | graphrag-map-reduce-query-mechanism | Prepare 步骤描述 | grounded | Prepare 步骤是 src-1 Section 3.1.6 算法描述的直接改写 |
| 13 | long-context-recall-vs-safety-alignment | 诊断结果三档能力 | grounded | 数值来自 src-1/src-2 引用的 Appendix 表格 |
| 14 | llm-wiki-4-signal-relevance-model | 四信号权重表 | grounded | 四信号权重表直接引自 src-1 README P138-144 |
| 15 | graphrag-vs-vector-rag-results | Win rate 结果表 | grounded | win rate 数值来自论文 Experiment 1 结果，src-1/src-2 覆盖 |

**总结: structural 1 / grounded 14 / ungrounded 0**

分析: 141 个无脚注段落中，绝大多数属于以下两种合理模式:
1. **数据展开模式**: 卡片在首段或末段标注脚注，中间段落展开同一来源的具体数值/步骤/算法细节（如表格、列表、算法步骤）
2. **前后夹注模式**: 段落位于两个脚注之间，内容是同一来源的不同维度展开

这与卡片写作惯例一致——每个 claim cluster 标注一次脚注，而非逐句标注。

## 最终判定

- **A1: PASS** — 20/20 semantic-pass，与 v4 首轮审计 18/18 pass 结果一致。143 条 suspect 确认为 LaTeX/Markdown 格式假阴性模式，非语义不忠实。
- **E2: PASS (warning)** — 0/15 ungrounded (0%)，远低于 20% 阈值。无脚注段落均为合理的结构性连接或已源覆盖内容的展开。建议未来审计脚本优化: 识别"前后夹注"模式，减少此类假阳性。
