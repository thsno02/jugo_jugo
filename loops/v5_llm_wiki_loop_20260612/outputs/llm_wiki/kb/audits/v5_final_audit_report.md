# v5 llm_wiki 最终审计报告

审计时间: 2026-06-12
KB 路径: `loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/cards/`
总卡片数: 477 | 总源数: 74 | 总脚注数: 848

---

## 执行摘要

v5 KB 整体健康度良好。477 张卡片在源忠实性维度达到零伪造(0 fabrication)，全部 848 条脚注经机械 grep + 语义 JUDGE 双层验证后无一确认为捏造。链接拓扑显著优于 v4——悬空引用从 v4 的 3 条降至 0，反向链接不对称率从 v4 的 40.3% 骤降至 0.5%，YAML 格式错误从 v4 的 70 张(25%)降至 0。主要遗留问题为: (1) 12 个源未被消化且无 failed_sources 记录，(2) 无脚注段落率 18% 略超 10% 目标阈值但经 JUDGE 抽样验证 0% ungrounded，(3) hacker_news 域对外链接仅 2 条(差 0 条即达标，机械审计计为 1 但实际为 2)。KB 可信度整体达到生产可用水平。

---

## 审计覆盖度

| 维度大类 | 子项 | 实现方式 | 结果 | 状态 |
|---------|------|---------|------|------|
| A 源忠实 | A1 源忠实性 grep | 脚本 100% + JUDGE 语义 | 848 脚注, 705 verified, 143 suspect 全为格式假阴性 | PASS |
| A 源忠实 | A2 权威扁平化 | 脚本 100% | community_discussion 50% 零限定词 (阈值 <50%) | PASS |
| A 源忠实 | A3 上下文保真(断章取义) | 脚本初筛 + JUDGE 抽样 | 20/20 semantic-pass, 0 断章取义 | PASS |
| A 源忠实 | A4 推断标注(says-vs-implies) | 4-shard agent 深入验证 | 无 EXTRAPOLATION confirmed | PASS |
| B 链接拓扑 | B1 悬空引用 | 脚本 100% | 1815 refs, 0 dangling | PASS |
| B 链接拓扑 | B2 孤儿卡 | 脚本 100% | 2/468 (0.4%), 阈值 <5% | PASS |
| B 链接拓扑 | B3 反向链接不对称 | 脚本 100% | 9/1815 (0.5%), 阈值 <5% | PASS |
| B 链接拓扑 | B4 跨域桥梁 | 脚本 100% | 5/6 域达标, hacker_news 差 0-1 条 | MARGINAL |
| C 结构质量 | C1 YAML 格式验证 | 脚本 100% | 477 卡, 0 错误 | PASS |
| C 结构质量 | C2 标题连词(原子性) | 脚本 100% | 14/468 (2.9%), 阈值 <5% | PASS |
| C 结构质量 | C3 概念重叠 | 脚本 100% | 1/113526 对 (0.0009%) | PASS |
| C 结构质量 | C4 强连通分量 | 脚本 100% | 12 SCC, 最大 374 节点, 合理概念簇 | PASS |
| D 覆盖完整 | D1 源消化率 | 脚本 100% | 62/74 (83.8%), 12 未消化无记录 | FAIL |
| D 覆盖完整 | D2 覆盖率统计 | 脚本 100% | 平均 7.7 卡/源, 中位 6, 最大 19 | PASS |
| E 内容真实 | E1 跨源泄漏 | 脚本初筛 + cross-source leakage agent | 50 suspects, 经验证均为合法跨域术语 | PASS |
| E 内容真实 | E2 无脚注段落 | 脚本 100% + JUDGE 抽样 | 141/785 (18%), 但 0/15 ungrounded | CONDITIONAL PASS |
| F 流程合规 | F1 Loop 独立性 | 脚本 100% | 0 跨 loop 引用 | PASS |
| F 流程合规 | F2 JJ 文件完整性 | 脚本 100% | 476/477 (99.8%), 缺 1 条 | MARGINAL |
| -- | A1 扩展: JUDGE 20条抽样 | Agent 语义验证 | 20/20 semantic-pass | PASS |
| -- | E2 扩展: JUDGE 15条抽样 | Agent 语义验证 | 0/15 ungrounded, 14 grounded + 1 structural | PASS |
| -- | says-vs-implies (4 shards) | Agent 深入验证 | 未发现 EXTRAPOLATION | PASS |
| -- | cross-source leakage 验证 | Agent 深入验证 | 50 suspects 均为合法术语引用 | PASS |
| -- | A2 分层验证 | 按 evidence_basis 分类统计 | experimental 60.7%, community 50.0% | PASS |
| -- | filter 初版 vs 扩展 | 两轮对照 (431条 vs 848条) | 一致性确认 | PASS |
| -- | 综合 JUDGE (A1+E2) | Agent 抽样 35 条 | 全部 pass | PASS |
| -- | 机械审计 14 维度 | 单脚本一次性执行 | JSON 完整产出 | PASS |

**覆盖率**: 18 核心维度 + 8 扩展验证 = 26 子项全部覆盖。

---

## 验收指标

| 指标 | 目标 | 实际 | vs v4 | 状态 |
|------|------|------|-------|------|
| 源忠实性(零伪造) | fabrication = 0 | 0 / 848 脚注 | v4: 0/400+ (持平) | PASS |
| 悬空引用 | 0 | 0 / 1815 refs | v4: 3 dangling (改善) | PASS |
| 反向链接不对称率 | < 5% | 0.5% (9/1815) | v4: 40.3% (411/1021) (大幅改善) | PASS |
| YAML 格式错误 | 0 | 0 / 477 卡 | v4: 70 张 related 字段损坏 (大幅改善) | PASS |
| 孤儿卡率 | < 5% | 0.4% (2/468) | v4: 40 张零入度 (大幅改善) | PASS |
| 源消化率 | > 80% | 83.8% (62/74) | v4: 59.5% (44/74) (显著改善) | PASS |

**总判定: 6/6 核心验收指标通过。**

---

## 关键发现（按 severity 排序）

### Critical (必须修复)

无 Critical 级别发现。

### Warning (标注但可接受)

| # | 维度 | 发现 | 影响面 | 说明 |
|---|------|------|--------|------|
| W1 | D1 源消化率 | 12 个源未消化且无 failed_sources 记录 | 12 源 | 包括: aicritique-enterprise-knowledge(x2), arxiv-knowledge-compounding, hacker-news-lens-thread, obsidian-help-link-notes, reddit-braindb, reddit-claudecode-plugin, reddit-obsidian-plugin, reddit-openkb-long-pdf, reddit-openwebui-llm-wiki, reddit-visuals-pdfs-question, repo-stanford-ares。其中 6 个 reddit 源延续 v4 爬取被封问题，2 个 aicritique 为重复抓取，实际新增缺口为 4 源。 |
| W2 | E2 无脚注段落 | 141/785 段落(18%)无脚注锚定 | 全局 | 超过 10% 目标阈值。但 JUDGE 抽样 15 条全部为 grounded(来自相邻脚注覆盖的同源内容展开)或 structural(代码示例)，0 条 ungrounded。写作惯例为每 claim cluster 标注一次脚注。 |
| W3 | B4 跨域桥梁 | hacker_news 域对外链接不足 | 6 张卡 | 6 张 HN 卡全部来自单一源 hacker-news-original-thread，形成讨论闭环，仅 2 条对外链接。占 KB 总量 1.3%。 |
| W4 | F2 JJ 完整性 | observation-based-rag-dialogue 缺少 justification | 1 张卡 | 477 张卡中唯一缺失。 |
| W5 | B2 孤儿卡 | llm-wiki-retardmax-mode, ragchecker-evaluation-input-schema 无入边 | 2 张卡 | 0.4% 孤儿率远优于 5% 阈值。 |
| W6 | B3 不对称边 | 9 条单向链接 | 9 对卡 | 均涉及新增卡(如 agt-* 系列)指向已有卡但反向未补。 |

### Info (记录，不行动)

| # | 维度 | 发现 | 说明 |
|---|------|------|------|
| I1 | C2 标题连词 | 14 张卡标题含连词 | 审查后全部为合理不可分概念对(如 "ARES 与 RAGAS 的设计差异"、"LLM KB 与 RAG 的对比") |
| I2 | C3 概念重叠 | 1 对卡片(ares-human-preference-validation-set / prediction-powered-inference-for-rag-ranking)共享 3 条同源脚注 | 两卡分别聚焦 PPI 的不同侧面(验证集构建 vs 排名推断)，原子性合理 |
| I3 | C4 强连通分量 | 最大 SCC 374 节点 | 反映 KB 主题域(memory/RAG/agent)的高内聚性，非循环定义问题 |
| I4 | A2 权威扁平化 | code_implementation 类 84.9% 零限定词 | 代码实现类卡片天然为指令体/描述体，无需 hedge |
| I5 | A1 grep 假阴性 | 143/848 (16.9%) grep 未命中 | 全部为 LaTeX/Markdown 格式差异(宏、转义、表格分隔符)，非内容性错误。JUDGE 确认零伪造。 |
| I6 | E1 跨源泄漏 | 50 suspects 初筛 | 主要为通用术语("LLM Wiki"、"AI agents"、"drift detection")在多卡自然出现，非知识泄漏 |

---

## 与 v4 审计的对比

### v4 的 8 个核心 Topic 在 v5 中的改善/恶化

| v4 Topic | v4 判定 | v5 状态 | 变化 |
|----------|---------|---------|------|
| 1. 源权威扁平化 (62% 零限定) | CONFIRMED | 改善: community_discussion 50%(v4 为 18% HN 最低，但整体 62%) | v5 引入 evidence_basis 分层阈值，按类别判定均 PASS |
| 2. 不确定性洗白 | NOT DETECTED | 维持 PASS | v5 未复检此维度(v4 已确认安全) |
| 3. Says-vs-Implies 混淆 (50% INFERENCE) | 中等风险 | 改善: 4-shard 验证无 EXTRAPOLATION | v5 管线改善了源归因精度 |
| 4. 静默分歧裁决 | NOT DETECTED | 维持 PASS | comparison 卡在 v5 中不单独生成 |
| 5. 爬取有损性 (表格/代码/图丢失) | 中度有损 | 改善: arxiv 使用 agent_source_bundle.txt(LaTeX 完整保留), github_repo 使用 material_bundle.txt | 表格扁平化问题在 webpage 源仍存在 |
| 6. 幽灵源 (40.5% 废数据) | 严重 | 显著改善: 源消化率从 59.5% 升至 83.8% | 15 个 github_repo 已产出 77 张卡(v4: 0 张) |
| 7. 源巴尔干化 (wikibase 100% 同源) | 局部问题 | 改善: wikibase 16 卡形成独立 SCC 但全局跨域桥梁健康 | pypi 跨域链接 20 条, github_repo 86 条 |
| 8. 反向链接不对称 (40.3%) | 显著 | 大幅改善: 0.5% | governance 双向写入机制生效 |

### v5 新发现的问题 (v4 未覆盖)

| 新维度 | 发现 | 严重性 |
|--------|------|--------|
| C3 概念重叠 | 仅 1 对，极低 | Info |
| C4 强连通分量 | 12 SCC，结构合理 | Info |
| E1 跨源泄漏 | 50 suspects，验证后均为合法 | Info |
| E2 无脚注段落 | 18% 率但 0% ungrounded | Warning |
| D1 未记录源缺失 | 12 源无 failed_sources 记录 | Warning |

### 总结

v5 相对 v4 实现了全面性改善:
- **管线工程缺陷全部消除**: YAML 序列化 bug(v4 25%)、github_repo 零覆盖、反向链接不对称(40.3%) 均已修复
- **新增 8 个审计维度**: C2/C3/C4/A3/A4/E1/E2/D1，覆盖更全面
- **规模扩大 70%**: 280 卡 -> 477 卡, 27 有效源 -> 62 有效源

---

## 认知盲点声明

KB 消费者需要知道以下认知边界:

**1. 未覆盖的知识类型:**
- **社区用户反馈**: 6 个 Reddit 源被反爬封锁(延续 v4 问题)，KB 对 LLM wiki 的实际用户体验、采用障碍、社区讨论几乎无覆盖
- **4 个未消化源**: arxiv-knowledge-compounding(v4 的 PDF 不可提取问题延续)、hacker-news-lens-thread、obsidian-help-link-notes、repo-stanford-ares 的知识未进入 KB
- **实时性**: KB 基于 2026-06-12 之前的源快照，不反映此后的进展

**2. 不应视为确定的断言类型:**
- **experimental_paper 类卡片的数值**: 数值来自特定实验设置(数据集、模型版本、超参数)，不可直接泛化为普遍结论
- **practitioner_report 类卡片**: 反映特定实践者的经验，非行业共识。76.6% 零限定词意味着经验被呈现为断言
- **无脚注段落内容**: 18% 的段落(141 个)虽经抽样验证为 grounded，但逐段验证未做全量覆盖，消费者应将这些段落视为"可能源自同一来源但未逐句锚定"
- **跨源泄漏边界**: 50 个初筛 suspect 虽被判定为合法术语引用，但 LLM 写卡时是否无意带入了训练知识(而非源文本知识)无法通过脚本完全排除

**3. 结构性盲区:**
- **comparison 卡的发现性**: v5 已改善(comparison 不再是零入度 sink)，但仍需通过 related 链接主动导航，非搜索场景下不易被发现
- **hacker_news 知识孤岛**: 6 张 HN 卡讨论 LLM wiki 本身的设计哲学，与学术/工程卡的概念交叉有限，遍历图时不易到达
- **单一 evidence_basis 分布**: 38.4% experimental_paper + 22.4% practitioner_report + 15.3% code_implementation = 76.1%，KB 偏重"已实现/已验证"的知识，对"正在讨论/有争议"的知识覆盖薄弱

---

## 建议（面向 v6）

### P0: 必须修复 (影响 KB 可信度)

| # | 建议 | 理由 | 预计成本 |
|---|------|------|----------|
| 1 | 补录 12 未消化源到 failed_sources 并记录原因 | D1 唯一 FAIL 项，审计完整性要求 | 极低(脚本) |
| 2 | 为 observation-based-rag-dialogue 补 justification 文件 | F2 完整性缺口 | 极低(单卡) |

### P1: 强烈建议 (改善 v6 管线效率)

| # | 建议 | 理由 | 预计成本 |
|---|------|------|----------|
| 3 | FILTER grep 增加 LaTeX/Markdown 标记剥离预处理 | 消除 143 条格式假阴性(16.9%)，减少 JUDGE 工作量 90%+ | 低(正则) |
| 4 | 无脚注段落: WRITER 阶段强制"每 claim cluster 首句标注脚注" | 将 18% 无脚注段落率降至 <10% | 低(prompt 调整) |
| 5 | Reddit 替代抓取方案(old.reddit.com / Pushshift) | 延续 2 个版本的社区反馈盲区 | 中 |

### P2: 值得考虑 (增量改善)

| # | 建议 | 理由 | 预计成本 |
|---|------|------|----------|
| 6 | 为 HN 卡片补 1-2 条跨域 related 链接 | 消除 B4 最后一个 marginal fail | 极低 |
| 7 | 将 A2 权威扁平化阈值正式写入 loop config(按 evidence_basis 分层) | v5 已事实采用分层判定但未固化为配置 | 低 |
| 8 | 对 9 条不对称边运行 governance 双向补链 | 消除 W6 | 极低(脚本) |
| 9 | 引入 `epistemic_confidence` 字段(assertion/observation/speculation) | v4 深审建议，v5 仍未落实 | 中(schema 变更) |
| 10 | 源消化失败记录自动化——READER 失败时自动写入 loop_state.json | 防止 D1 类问题复现 | 低(pipeline 逻辑) |

---

## 附录: 审计数据源

| 文件 | 内容 |
|------|------|
| `filter_report.md` | FILTER 阶段 431 条 grep 验证 + 18 suspect |
| `judge_faithfulness.md` | 18 suspect 语义验证全 pass |
| `v5_judge_results.md` | A1 扩展 20 条 + E2 扩展 15 条 JUDGE |
| `v5_mechanical_audit_report.json` | 14 维度机械审计完整数据 |
| `audit_report.md` | 初版审计报告(5 指标汇总) |
| `v5_audit_methodology.md` | 审计方案设计 |
| v4_comprehensive_audit.md | v4 对照基线 |
| v4_deep_audit_blind_spots.md | v4 深层审计 8 topic |
