---
schema: v4_learnings
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-12
topic: kb_health
purpose: retrospective
---

# KB 健康快照（328 张卡）

> 本快照反映全流程完成后的最终状态（含 pipeline gaps 修复 + webpage 重提取增量）

详细卡片索引见 ../outputs/llm_wiki/kb/indexes/cards.md

## 基础指标

| 维度 | 数值 | 来源 |
|------|------|------|
| 活跃卡片数 | 328 | cards.md index（含 pipeline gaps 修复 + webpage 重提取增量 48 张） |
| 有效来源数 | 44（原始 74 目录中 30 为幽灵） | deep_audit Topic 6 |
| related 链接总数 | 1022 条有向边 | deep_audit Topic 8（governance pass 基于 280 卡；扩展 48 卡尚未完全链接） |
| 有链接卡片比例 | 264/280 = 94.3%（基于 governance pass 时的 280 卡） | cards.md index |
| 平均链接密度 | 3.3 条/卡（有链接卡，基于 280 卡 governance pass） | cards.md index |
| comparison/distinction 卡 | 21 张 | comprehensive_audit |
| 卡片类型分布 | mechanism 108, distinction 65, source_claim 48, concept 40, operational_rule 11, example_pattern 8 | cards.md index |

## 健康维度评估

### 源忠实性：优良

- 400+ 条 `[^src-*]` 脚注零伪造引用、零凭空捏造数字
- 仅 2 处数值混淆（73% gap 基准错置）、1 处真实上下文泄漏（确认优先规则）、1 处溯源缺口（GraphRAG map-reduce）
- 不确定性洗白 **NOT FOUND**——引用链中置信度传递准确，最大 hedge-drop 仅为 3 且均为 APPROPRIATE-UPGRADE
- 静默分歧裁决 **NOT FOUND**——21 张 comparison 卡中 19 张 NEUTRAL-ACKNOWLEDGED，零张直接裁定一方

### 源权威扁平化：中度风险

- 62% 卡片（174/280）零认识论限定词
- 问题本质是扁平化而非捏造——管线系统性剥离了 hedging
- 跨源类型高度一致（arxiv 63%、blog 60%、gist 59%），HN 反而最谨慎（零限定比例仅 18%）
- pypi 卡 100% 零限定词（7/7），是最不透明的子集

### 链接图结构：有缺陷但可用

- 反向链接不对称 40.3%：1021 边中 411 条单向
- 40 张零入度卡：21 张 comparison（设计性 sink）+ 19 张非 comparison
- Hub 集中度：前 5 hub 吸收 28% 入边（llm-wiki-pattern=27, three-layer-architecture=21, lint-operation=17）
- wikibase 9 卡完全断联主图（100% 同源链接，零对外边）
- ALCE 10 卡近回音室（79.2% 同源），桥梁链接未建立

### 直述与推断混淆：50% 学术型卡片

- 首批 26 条 source footnote 中 13 条为 REASONABLE-INFERENCE
- 问题集中在学术综述型卡片；实现型/文档型卡片几乎不受影响
- 脚注语义实为「基于此源推导」而非「此源原文如此」
- 零条 EXTRAPOLATION（超源推断），推导均在合理范围内

### 爬取有损性：中度

- 表格扁平化影响 4/5 抽查源（25 张 HTML 表格变为连续文本）
- wikibase 3 张 UML 图完全丢失
- 代码块缩进/结构在 3/5 源中消失
- 现已通过 markdown.md 级联方案部分缓解

## 已知遗留问题

### 幽灵源（30 个目录未产出卡片）

- 20 个 github_repo：管线无 text.txt 生成步骤，已克隆但未提取
- 6 个 reddit：全部被反爬封锁（text.txt 仅 222-224 字节 blocked 消息）
- 4 个 webpage：text.txt 为空或噪声
- 其中 15 个非重复 github_repo 是最大未利用信息源

### YAML 序列化缺陷（已修复）

- 69/280 卡双格式 related 字段——governance rescue commit (b26dafc) 的 derive-related 步骤引入
- 11 张全损（解析为空数组）、58 张部分损
- **已通过脚本批量修复**

### 源验证盲区

- 10 张 knowledge-compounding 卡引用不可提取文本的 PDF
- 仅通过摘要级一致性 + 内部算术校验，未做 section 级脚注验证
- 判定为 "passed with caveat"，不可与 grep-verified 卡等同

### 爬取有损内容

- 表格/代码/图表在 text.txt 提取时丢失结构
- wikibase 源最严重（UML 图丢失 + 图孤立 + 同源链接）
- 根因：pipeline boundary-read 硬编码 text.txt，未使用 raw.html 的结构化转换

## 系统性模式总结

1. **管线工程缺陷 > 内容判断错误**：三大问题（幽灵源、权威扁平化、爬取有损）均为管线设计问题
2. **认识论失真集中在「源→卡」边界**：卡→卡引用链可信，但源→卡注册环节系统性损失了置信度标注
3. **缺失内容 >> 错误内容**：KB 几乎无事实错误，但有大量认知空白未被自身承认
4. **comparison 卡的矛盾地位**：判断质量高（19/21 中立），但结构上完全不可通过 related 导航发现（零入度 sink）（详见 ./design_decisions.md #5 — Comparison cards as pure sinks）
5. **wikibase 三重困境**：100% 同源链接 + 完全断联子图 + UML 图丢失——认知可靠性最低的子集
