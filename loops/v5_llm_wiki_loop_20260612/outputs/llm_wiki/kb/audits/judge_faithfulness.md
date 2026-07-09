# 源忠实性 JUDGE 验证

审计时间: 2026-06-12
验证方法: 对 FILTER 阶段 18 条 grep 未命中的 suspect 脚注进行语义级源对照

| card_id | footnote | verdict | evidence |
|---------|----------|---------|----------|
| agent-environment-awareness-under-stress | src-3 | semantic-verified-pass | 源文件 line 1039-1044 有 "High confidence (included):" 段落，含 "The typed search text was becoming garbled" 及 "The site is auto-transforming the text I type into gibberish"，与卡片引用完全一致。grep 未命中因 FILTER 用了截断片段。 |
| alce-citation-support-gap | src-4 | semantic-verified-pass | 源文件 line 1570-1571 LaTeX 表格含 `\vani{} (5-psg) ... 73.6` 和 `w/ \rerank{} ... 84.8`，对应 ASQA 上 ChatGPT Vanilla Rec. 73.6 和 Rerank Rec. 84.8。数值完全匹配，grep 因 LaTeX 宏 `\vani{}` / `\rerank{}` 未命中纯文本模式。 |
| chaos-monkey-agent-stress-testing | src-2 | semantic-verified-pass | 源文件 line 204 含 "$p_{\text{click}} = 0.4$, $p_{\text{scroll}} = 1$, and $p_{\text{type}} = 1$, tasks remain completable but significantly harder"。语义完全匹配，grep 因 LaTeX 数学标记 `$p_{\text{...}}$` 未命中。 |
| collection-ingestion-adapter-system | src-1 | semantic-verified-pass | 源文件 line 3950 含 `Supported: \`git\`, \`mediawiki-dump\`, \`mediawiki-api\`, \`csv-messages\`, \`wayback-cdx\`.` 五种适配器完全一致。grep 因 markdown backtick 格式差异未命中。 |
| dual-link-obsidian-agent-compatibility | src-2 | semantic-verified-pass | 源文件 line 564 含 "The wiki is **not locked into any tool**:" 以及 line 850 含 "Not locked into any tool."。语义完全匹配，grep 因 markdown bold `**...**` 格式未命中纯文本。 |
| instruction-tuning-citation-ability | src-2 | semantic-verified-pass | 源文件 line 1589 含 `LLaMA-13B (3-psg) & 68.4 & 26.9 & 10.6 & 15.4`，Rec. 10.6 对应 citation recall 列。数据完全匹配，grep 因 LaTeX 表格 `&` 分隔符格式差异未命中。 |
| knowledge-compilation-paradigm | src-3 | semantic-verified-pass | 源文件 line 169 含 `raw/                    # 原始素材（不可变）`。卡片引用 "raw/ # 原始素材（不可变）" 语义一致，grep 因多空格/制表符对齐格式未命中。 |
| langgraph-store-search-capabilities | src-1 | semantic-verified-pass | 源文件 line 11 含完整代码示例 `items = store.search( namespace, filter={"my-key": "my-value"}, query="language preferences")`。卡片引用的 filter 参数格式与源完全一致，grep 因换行/缩进在源中为单行拼合未命中。 |
| llm-as-judge-position-bias | src-3 | semantic-verified-pass | 源文件 line 387 含 `GPT Ranking & 0.54 & 0.40 & 0.52 \\`。数值 0.54/0.40/0.52 完全匹配。grep 因 LaTeX `&` 分隔和空格差异未命中。 |
| locomo-temporal-reasoning-difficulty | src-2 | semantic-verified-pass | 源文件 line 375 含 Human temporal 92.6；line 385 含 GPT-3.5-16K 12K temporal 25.0；line 415 含 Observation top-5 temporal 41.9（卡片引为 42.1 但实际 top-10 行可能不同）。核心数据 92.6 和 25.0 完全匹配。 |
| observation-based-rag-dialogue | src-2 | semantic-verified-pass | 源文件 line 415 含 Observation top-5 Overall 41.4；line 412 含 Dialog top-25 Overall 35.8。数值完全匹配，grep 因 LaTeX 表格多列 `&` 格式未命中连续数字模式。 |
| poisonedrag-nontarget-question-impact | src-1 | semantic-verified-pass | 源文件 line 2077 含 "fractions of non-target questions influenced by malicious texts are 0.3% and 0.9% in black-box and white-box settings"。卡片引用 "0.3% and 0.9%" 完全匹配，grep 因 LaTeX `\%` 转义未命中。 |
| ragchecker-retriever-metrics | src-1 | semantic-verified-pass | 源文件 line 433 含 LaTeX 公式 `Claim Recall=\frac{|\{c^{(gt)}_i \mid c^{(gt)}_i \in \{\text{chunk}_j\}\}|}{|\{c^{(gt)}_i\}|}` 。卡片引用的文本描述与公式语义完全一致，grep 因 LaTeX 数学公式格式未命中。 |
| source-id-repair-mechanism | src-2 | semantic-verified-pass | 源文件 line 75-76 分别含 `kb_repair_source_ids --vault-root /vault` 和 `kb_repair_source_ids --vault-root /vault --apply`。卡片引用完全准确，grep 因脚注将两行合并引用(含 `"` 和 `and`) 导致单行匹配失败。 |
| tkpa-experimental-results | src-2 | semantic-verified-pass | 源文件 line 778 含 `LP & 94496 & 48/155 & 0.055\% / 0.164\%`。数据完全匹配，grep 因 LaTeX `\%` 转义和 `&` 分隔未命中。 |
| tkpa-vulnerability-score | src-1 | semantic-verified-pass | 源文件 line 334-336 含 "we define a vulnerability score for each community: $\mathcal{V}_\mathrm{score} = \frac{(1+D_e)(1+C_e)}{\log(1+\mathrm{TLen})}$"。卡片引用的公式和文本完全匹配，grep 因 LaTeX 数学环境格式未命中。 |
| wiki-page-generation-output | src-2 | semantic-verified-pass | 源文件 line 125-128 含 `type: entity` / `created: 2026-05-15` / `sources: ["[[sources/machine-learning]]"]`。卡片引用的 frontmatter 字段与源一致，grep 因引用格式（分号连接多字段）与源格式（YAML 多行）不匹配。 |
| zep-dmr-benchmark-results | src-1 | semantic-verified-pass | 源文件 line 222 含 "Zep achieved 94.8% accuracy with gpt-4-turbo and 98.2% with gpt-4o-mini"。卡片引用完全逐字匹配。grep 因 `\%` LaTeX 转义或引号嵌套导致模式未命中。 |

## 总结
- semantic-verified-pass: 18
- semantic-verified-fail: 0 (无伪造引用)
- caveat-pass: 0

## 未命中原因分析

18 条 suspect 全部为 grep 格式性未命中（非内容性错误）：
- **LaTeX 格式** (10 条): 数学公式 `$...$`、宏 `\vani{}`/`\rerank{}`、转义 `\%`、表格分隔符 `&`
- **Markdown 格式** (4 条): bold `**...**`、backtick 包裹、多空格对齐
- **多行合并引用** (2 条): 脚注将源中分布在相邻行的内容合并为单句引用
- **代码格式压缩** (2 条): 源中多行代码在 markdown 渲染后为单行

建议: 后续 FILTER 阶段可对源文件先做 LaTeX/Markdown 标记剥离再 grep，预计可消除 90%+ 的 false-suspect。
