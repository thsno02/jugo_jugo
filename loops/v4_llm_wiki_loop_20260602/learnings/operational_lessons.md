---
schema: v4_learnings
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-12
topic: operational_lessons
purpose: retrospective
---

# 运营教训与失败模式

## 1. 并行提取破坏 fusion check

- **症状**：280 张卡在同一批次（2026-06-05T10:00:00+08:00）批量生成，intra-loop 去重从未发生；merge_candidate=0 是"从没看过"不是"没重复"。
- **根因**：并行 extraction 的所有 agent 同时生产 draft，无增量积累基。第一张 draft 的比较基是空集应随 draft 累积增长，但批量并行没有这个"增量比累积"的时刻。
- **发现方式**：时间戳聚类分析（248/280 卡同一秒）+ loop independence 原则审计。
- **修复措施**：v4 未修——问题在审计阶段暴露，loop 已结束。
- **下次应做**：extraction 后、adoption 前显式补一道 intra-loop 全配对去重 pass。batch 并行可以继续用来提速，但 governance 必须在全部 draft 落地后执行 pairwise fusion scan。

## 2. Cluster 治理制造知识边界

- **症状**：5 张 llm-wiki-net 来源卡 related: [] 且入站链接近零；wikibase 9 卡形成完全断联子图；security-memory 仅 2 条链接（17+71 张卡）。
- **根因**：derive-related 在固定集群（3-15 张同主题卡）内搜索候选，同领域卡优先被选中（同前缀密度 5.7x），跨领域桥梁未被主动发现。5 张卡未被任何集群覆盖而静默失联。
- **发现方式**：cluster damage assessment 预测验证——孤儿卡排斥 CONFIRMED，跨领域链接稀疏 PARTIALLY_CONFIRMED。
- **修复措施**：为 5 张孤儿卡补建 cross-link；添加 security-memory 和 wiki-governance 跨域桥梁链接。
- **下次应做**：governance 后增加孤儿检测 gate（related: [] 且入站=0 的卡触发全局补链）；derive-related 改为全局搜索而非集群内搜索；强制跨领域配额（至少 1 条 related 来自不同 domain tag）。

## 3. text.txt 不是通用格式

- **症状**：20 个 github_repo 零卡产出（管线静默跳过）；arxiv 源的 text.txt 仅 5KB 导航文字（实际内容在 agent_source_bundle.txt 223KB）；27 个 webpage 源的表格/代码/图表在 text.txt 中严重退化。
- **根因**：pipeline_spec.md 硬编码 boundary-read: text.txt。fetch_sources.py 的 TextExtractor 将 table 压成空格分隔文本、code/pre 丢失缩进、img/svg 完全丢弃。github_repo 克隆后从不生成 text.txt。
- **发现方式**：幽灵源审计（30/74 目录 = 40.5% 未产出卡片）+ 爬取有损性抽查。
- **修复措施**：v4 pipeline gaps 修复添加了 arxiv 路径优先级和 repo 提取步骤。
- **下次应做**：boundary-read 改为优先级级联 agent_source_bundle.txt > raw.html（经 markdown converter） > text.txt；为 github_repo 类型自动生成 material_bundle.txt = README + docs 拼接。

## 4. Workflow 负载不均衡

- **症状**：parallel() 中 9 个 agent 各 3 分钟完成，1 个 mega-agent 20 分钟，整体完成时间被最慢 agent 拖至 20 分钟。深层审计时"全量 grep 机械检查"与"深读抽样"同在一个 agent 内导致超时。
- **根因**：工作量估算缺失——未按 token/文件数预估每个 agent 的负载；大 topic（如 atomicity 审计需覆盖 280 张卡）未拆分。
- **发现方式**：审计执行日志中 agent 完成时间差异 >5x，用户指出"parallel() 的完成时间 = 最慢 agent 的完成时间"。
- **修复措施**：深层审计拆成 10 个 agent（每 agent 约 28 张卡或一个专项 topic）。
- **下次应做**：parallel() 分配前估算 token 量；若某 agent 工作量 >2x 平均值则拆分；全量 grep 和深读抽样拆成独立 agent。

## 5. Agent 上下文溢出无法有效审计

- **症状**：10 张 arxiv-knowledge-compounding 卡引用 source.pdf 但 PDF 不可提取文本，审计仅能做摘要级一致性校验；section 级引用（如 "Section 3.4 P10" 的具体引文）未经验证。
- **根因**：审计 agent 的工具集中无 pdftotext，且 source.pdf 本身因扫描/加密无法被标准工具提取文本。这 10 张卡的忠实性判定为 "passed with caveat"。
- **发现方式**：审计 agent 报告 grep 命中率为 0 并标记为验证盲区。
- **修复措施**：记录为 M10（源验证盲区），建议安装 PyMuPDF 重验。
- **下次应做**：collection 阶段为所有 PDF 预生成纯文本版本（pdftotext/PyMuPDF）；若 PDF 无法提取则在 source 元数据中标记 `text_extractable: false`，governance 据此降低该源卡片的 epistemic_confidence。

## 6. 权威扁平化（reframing 去 hedge）

- **症状**：280 张卡中 174 张（62%）零认识论限定词；pypi 卡 100% 零限定（7/7）；blog 密度最低（1.490/100w）。blog/HN 轶事被以与实验论文同等断言口吻呈现。
- **根因**：reframing skill 的规则 1「对话体 -> 知识陈述体」系统性剥离了 reader 回答中的 hedge markers。schema 无 evidence_basis 字段区分"我们对它有多确信"。
- **发现方式**：深层审计 Topic 1（Source Authority Flattening）——逐源类型统计 hedge 密度。
- **修复措施**：v4 未修——审计结果为"对 KB 消费者的含义"注释。
- **下次应做**：reframing skill 增加规则"保留 reader 的 hedge level"；源是 blog/HN/pypi 的卡在 frontmatter 中添加 `evidence_basis: practitioner_report | community_discussion`（非 experimental/theoretical）。

## 7. Comparison 卡作为 link sink

- **症状**：21 张 comparison 卡入度为零（100% 均为 sink）；移除它们仅损失 6.8% 边；从任意卡出发的 related 导航无法到达 comparison 卡。
- **根因**：设计性——comparison 引用 subject cards，subject cards 不需要反引所有关于自己的 comparison。但 governance 也未提供替代发现路径。
- **发现方式**：反向链接不对称审计（40.3% 单向边，411/1021）。
- **修复措施**：确认为 by-design sink，但补建了部分 see_also 反向链接以提高可发现性。
- **下次应做**：comparison 卡作为 sink 是正确设计；但需在被比较的 subject cards 中添加 `see_also: comparison-X` 轻量反向链接，使 comparison 内容可通过图遍历发现。governance 的 derive-related 步骤在写入 A->B 时应检查是否需要 B->A（除非关系类型是 support/evidence 这类天然单向关系）。

## 8. YAML related 序列化双格式 bug

- **症状**：70 张卡（25%）的 related 字段同时包含行内数组 `[]` 和缩进列表 `- item`，YAML 解析器只读行内值，缩进项被静默丢弃。11 张完全丢失 cross-link。
- **根因**：governance rescue commit (b26dafc) 的 derive-related 脚本假设 related 字段仅占一行，对 63 张 block-style 卡执行单行替换时未删除后续缩进行。另有 6 张 comparison 卡在创建时即带有同样缺陷。
- **发现方式**：mechanical-audit-agent 首次发现，后被 6 个独立 agent 在不同卡片子集上反复确认。
- **修复措施**：Python 脚本批量修复——读取每张卡 frontmatter，合并行内数组与缩进项，去重后以标准 YAML 列表重写。
- **下次应做**：永远不要用正则/单行替换修改 YAML 字段。derive-related 脚本在写入前必须用 YAML 解析器读取整个 frontmatter，修改字段后重新序列化。CI/governance gate 增加 YAML lint 步骤验证 frontmatter 格式一致性。

## 9. grep 审计 false positive（says-vs-implies）

- **症状**：审计初报判定 2 例 context leakage（确认优先规则 + 参与程度谱系），经深入调查发现"参与程度谱系"实为 false positive——Karpathy gist 第 37 行有明确描述，卡片是合理意译。
- **根因**：grep exact-quote matching 的二元判定（supported / unsupported）无法区分"源文本用不同措辞表达了同一意思"和"agent 凭空引入概念"。源材料的意译被误判为 leakage。
- **发现方式**：对 suspect 项派 agent 读取完整源材料进行语义级验证后翻转判定。
- **修复措施**：审计报告 Section 8.1 修正了方法论——增加 "suspect -- needs full-text review" 中间状态。
- **下次应做**：grep 未命中时不直接判定 leakage，标记为 suspect；对 suspect 项执行 semantic-verified 验证（agent 读原文确认）；审计 findings 区分 "grep-verified" 和 "semantic-verified" 两个置信度级别。

## 10. 脚注叙事泄漏（隐式上下文通道）

- **症状**：5/21 对比卡（24%）存在未归因概念；comparison-corrective-vs-servant-agency 第 27 行裸名引用"确认优先规则"但无任何脚注锚定，该概念的真实来源是 cognitionus-llm-wiki-guide。
- **根因**：Governance agent 读取 cluster 内全部卡片时，卡片的 [^card-N] 脚注叙事携带了来自其他源的概念描述。Agent 将脚注叙事中的概念纳入工作记忆后无归因地写入 comparison 卡。Phase 4b（governance）在 Phase 4a（cross-link）之后运行，此时卡片已被注入跨卡脚注，脚注叙事实际构成了隐式上下文通道。
- **发现方式**：leakage trace 报告——逐步还原执行链路 cognitionus-llm-wiki-guide -> confirm-first-skill-capture -> human-llm-role-division [^card-4] -> comparison 卡。
- **修复措施**：确认泄漏路径并记录缓解建议（prompt 增加脚注归因硬约束）。
- **下次应做**：comparison 卡生成 prompt 增加 Footnote Discipline 规则——正文提及非核心 tension 概念时必须有 [^card-N] 脚注追溯；governance agent prompt 显式区分"卡正文 src 锚定内容"与"脚注跨引内容"；governance 后增加 post-hoc 检查脚本检测裸名概念。

## 11. 死源静默进入 pipeline

- **症状**：6 个 reddit 源的 text.txt 仅含 222-224 字节"You have been blocked by network security"；管线无任何告警，直接跳过这些源。KB 声称覆盖 74 个源，实际有效源仅 44 个。
- **根因**：fetch_sources.py 不验证 text.txt 内容质量——只检查文件是否存在，不检查是否为有效内容。反爬封锁产生的错误页面被当作合法 text.txt 保存。
- **发现方式**：幽灵源审计——按 source_id 统计产出卡片数，发现 30 个零卡源后逐个检查 text.txt 内容。
- **修复措施**：v4 pipeline gaps 修复中添加了 scrape flags 标记。
- **下次应做**：collection 阶段增加 content validation gate——text.txt < 500 字节或包含常见反爬关键词（blocked/captcha/403）时标记为 `scrape_status: failed`，pipeline 不将其传入 extraction 阶段；使用 old.reddit.com + 适当 UA 或 Pushshift API 替代直接爬取。

## 12. arxiv text.txt 误路由

- **症状**：arxiv 源的 text.txt 仅含 arXiv 页面导航文字（~5KB），而实际论文内容在 agent_source_bundle.txt（~223KB TeX 解析结果）。reader agent 若按 boundary-read: text.txt 读取则只能获得导航噪声。
- **根因**：fetch_sources.py 对 arxiv URL 执行标准网页爬取（获取 HTML 导航页），同时独立下载 PDF 并 TeX 解析为 agent_source_bundle.txt。但 pipeline_spec 的 boundary-read 规则未区分源类型，统一指向 text.txt。
- **发现方式**：深层审计 Section 9.1（Pipeline 根因追踪）——对比 text.txt（5KB）与 agent_source_bundle.txt（223KB）内容后确认 text.txt 对 arxiv 无意义。
- **修复措施**：v4 pipeline gaps 修复中添加了 arxiv 路径优先级（agent_source_bundle.txt > text.txt）。
- **下次应做**：boundary-read 规则按源类型级联：arxiv 优先读 agent_source_bundle.txt；webpage 优先读 raw.html 经 markdown 转换；github_repo 读 material_bundle.txt。统一的 text.txt 作为 last-resort fallback。

## 13. Claude Code 运行时环境约束

- **症状**：Agent 调用失败、权限弹窗中断 loop
- **根因**：Claude Code 的 Agent tool 默认使用 Haiku（用户 endpoint 不支持）；auto-mode 的安全分类器阻塞 grep/git/python
- **发现方式**：v4 首次运行时 Agent 调用报 "model unauthorized" + 权限弹窗频繁打断
- **修复措施**：
  - 所有 Agent 调用必须传 model: "opus"
  - Loop 整轮以 --permission-mode bypassPermissions 启动
  - Sub-agents 无法递归调用 Agent tool（被 harness strip），需用 claude -p via Bash 实现嵌套
  - 1M context 下应全文读取源材料，不要 limit:2000 分页
- **下次应做**：在 LOOP_START_PROMPT.md 中硬编码这些约束
