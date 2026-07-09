# v5 审计方案

## 设计原则

1. **脚本优先**: 可机械化的检查全部脚本化，100% 覆盖全部 477 张卡
2. **Agent 仅做语义判断**: 脚本产出 suspect 清单，agent 只处理 suspect（不做全量读卡）
3. **分层验证**: 脚本 100% 覆盖 → agent 抽样深入 → 人工确认关键 findings
4. **历史问题回溯**: 明确标注 v4 遇到的问题及本轮解决方案
5. **阈值分层**: 按 evidence_basis 和源类型分层设定阈值，避免一刀切

---

## 审计维度总览

| ID | 维度 | 实现方式 | 覆盖率 |
|----|------|----------|--------|
| A1 | 源忠实性 grep | 脚本 | 100% |
| A2 | 权威扁平化 | 脚本 | 100% |
| A3 | 上下文保真（断章取义） | 脚本初筛 + agent 判断 | 初筛 100% |
| A4 | 推断标注 (says-vs-implies) | 脚本初筛 + agent 判断 | 初筛 100% |
| B1 | 悬空引用 | 脚本 | 100% |
| B2 | 孤儿卡 | 脚本 | 100% |
| B3 | 反向链接不对称 | 脚本 | 100% |
| B4 | 跨域桥梁 | 脚本 | 100% |
| C1 | YAML 格式验证 | 脚本 | 100% |
| C2 | 标题连词（原子性） | 脚本 | 100% |
| C3 | 概念重叠 | 脚本 | 100% |
| C4 | 循环/强连通分量 | 脚本 | 100% |
| D1 | 源消化率 | 脚本 | 100% |
| D2 | 覆盖率 (F2/F3) | 脚本 | 100% |
| E1 | 跨源泄漏 | 脚本初筛 + agent 判断 | 初筛 100% |
| E2 | 无脚注段落幻觉 | 脚本 | 100% |
| F1 | Loop 独立性 | 脚本 | 100% |
| F2 | JJ 文件完整性 | 脚本 | 100% |

---

## 审计维度详细方案

### A1 源忠实性 grep 全量验证

**问题定义**: 卡片脚注声称引用源文本某段落，但源文本中实际找不到对应内容（fabrication/hallucination）。

**v4 教训**:
- LaTeX 格式差异（`\%`、`&`、数学公式）导致 grep false negative
- Markdown 格式（bold/backtick/多空格）造成假阳性 suspect
- v4 解决方案: 二阶 agent JUDGE 消除假阳性，但成本高

**v5 实现方式**: 纯脚本
1. 遍历每张卡的每条 `[^src-N]` 脚注
2. 解析脚注格式: `path -- section -- quote`
3. 对源文件和 quote 均做标记剥离（strip LaTeX: `\%` → `%`, `\&` → `&`, `$$..$$` → 空; strip Markdown: `**`, `` ` ``, 多空格归一）
4. 在剥离后的源文本中搜索剥离后的 quote（容忍 leading/trailing whitespace）
5. 未找到者列入 suspect

**判定标准**: quote 短语（取前 40 字符）在源文件剥离后文本中出现
**验收阈值**: suspect 率 < 5%（剩余由 agent 语义验证），fabrication = 0

---

### A2 权威扁平化统计

**问题定义**: 非学术源（blog/HN/gist）的卡片使用比学术源更少的限定词（qualifier/hedge），导致轶事被呈现为高置信度断言。

**v4 教训**:
- v4 发现 "flattening" 主要是假阳性：arxiv 实验论文本身就是断言体
- 真正的问题集中在 community_discussion 类型

**v5 实现方式**: 纯脚本
1. 按 `evidence_basis` 字段分类卡片
2. grep 限定词词表（中/英各 15+ 词）
3. 统计各类别的零限定词比例和平均密度
4. 特别关注 community_discussion 和 practitioner_report

**判定标准**: 按 evidence_basis 分层阈值
- experimental_paper / theoretical_paper / code_implementation: 不设硬性限定词目标
- practitioner_report: 零限定词 < 85%
- community_discussion: 零限定词 < 50%

**验收阈值**: community_discussion 类零限定词 < 50%

---

### A3 上下文保真（断章取义检测）

**问题定义**: 卡片引用了源文本的某个片段，但去除了原始上下文中的重要限定条件、对比对象、或否定前缀，使引用在脱离上下文后改变含义。

**v4 教训**: 此维度 v4 未实施（v5 新增）

**v5 实现方式**: 脚本初筛 + agent 语义判断
1. 脚本初筛: 检测 quote 中是否包含截断标记（`...`、省略号），quote 长度是否过短（< 15 字），是否 quote 所在段落包含 but/however/although/但是/然而/尽管 等转折词但 quote 未包含
2. 产出 suspect 清单
3. Agent 对 suspect 读原文上下文，判断是否存在含义扭曲

**判定标准**: agent 判断卡片陈述与源文完整上下文含义一致则 PASS
**验收阈值**: 断章取义 confirmed cases < 2%

---

### A4 推断标注 (says-vs-implies)

**问题定义**: 卡片内容混淆了源文本的直接陈述（DIRECT）、合理推断（REASONABLE-INFERENCE）和外推（EXTRAPOLATION），且未标注推断层级。

**v4 教训**: v4 将此作为专题但未全量执行，仅抽样发现少量问题

**v5 实现方式**: 脚本初筛 + agent 分类
1. 脚本初筛: 检测卡片 body 中的推断标记词（"据此推测"、"据材料推测"、"暗示"、"似乎"、"可能意味着"、"implies"、"suggests that"、"this means"）
2. 检测无脚注锚定的断言句（含推断词但无 `[^src-N]`）
3. 产出 suspect 清单
4. Agent 对 suspect 分类: DIRECT / REASONABLE-INFERENCE / EXTRAPOLATION

**判定标准**:
- DIRECT: 源文本明确说的 → 必须有 `[^src-N]`
- REASONABLE-INFERENCE: 源文本暗示、可逻辑推出 → 应标注推断性质
- EXTRAPOLATION: 超出源文本范围 → 不应出现或需明确标注为卡片作者观点

**验收阈值**: 未标注的 EXTRAPOLATION < 1%

---

### B1 悬空引用检测

**问题定义**: `related` 字段引用了不存在的卡片 slug，或 `[^card-N]` 脚注指向不存在的卡片。

**v4 教训**: v4 已有完善实现（yaml_lint.py），直接复用逻辑

**v5 实现方式**: 纯脚本
1. 构建全量 slug 集合（从 cards/ 目录扫描）
2. 检查每张卡 related 列表中每个 slug 是否存在
3. 检查 body 中 `[^card-N]` 脚注定义中的 slug 是否存在
4. 检查 body 中 `[[slug]]` wikilink 格式是否存在

**判定标准**: 引用目标在 cards/ 目录中存在对应 .md 文件
**验收阈值**: 悬空引用 = 0

---

### B2 孤儿卡检测

**问题定义**: 某张卡既不被任何其他卡的 `related` 引用，也不出现在任何其他卡的 `[^card-N]` 脚注中。

**v4 教训**: comparison-sink 类卡片天然被少量引用（它们是 hub），需排除

**v5 实现方式**: 纯脚本
1. 构建引用图: 对每张卡，提取 related + body 中 [^card-N] 提及的 slug
2. 计算每张卡的入度（被引用次数）
3. 入度 = 0 的卡标记为 orphan
4. 排除 card_type == "comparison" 的卡片（comparison sink 不计为孤儿）

**判定标准**: 非 comparison 卡入度 > 0
**验收阈值**: 孤儿率 < 5%

---

### B3 反向链接不对称检测

**问题定义**: A.related 包含 B，但 B.related 不包含 A（单向链接）。

**v4 教训**:
- comparison-sink 是被大量引用但不反向引用所有引用者的合理设计
- 需排除 comparison-sink 后再计算不对称率

**v5 实现方式**: 纯脚本
1. 构建 related 有向图
2. 对每条边 (A→B)，检查是否存在反向边 (B→A)
3. 统计不对称边数
4. 排除: 如果 B 是 comparison 类卡片，(A→B) 无需反向

**判定标准**: 排除 comparison-sink 后，每条 related 边都应对称
**验收阈值**: 不对称率 < 5%

---

### B4 跨域桥梁统计

**问题定义**: 每个 domain（arxiv/webpage/github_repo/...）应有足够的对外链接，避免形成信息孤岛。

**v4 教训**: hacker_news 域因卡片少+单源封闭，容易不达标

**v5 实现方式**: 纯脚本
1. 从 source_ids 提取每张卡所属 domain
2. 从 related 统计每张卡的对外链接（目标卡属于不同 domain）
3. 按 domain 聚合: 对外链接总数

**判定标准**: 每个 domain 对外链接 >= 2
**验收阈值**: 所有 domain 达标

---

### C1 YAML 格式验证

**问题定义**: 卡片 frontmatter 格式错误导致解析失败。

**v4 教训**: related 字段双格式（行内 [] 与缩进 - 共存）是最常见错误

**v5 实现方式**: 纯脚本
1. 每张卡 frontmatter 必须能被 yaml.safe_load 正确解析
2. related 不得混用行内和缩进格式
3. 必填字段检查: id, title, source_ids, canonical_concept, related, summary

**判定标准**: 零解析错误，零缺失字段
**验收阈值**: YAML 错误 = 0

---

### C2 标题连词检测（原子性）

**问题定义**: Zettelkasten 卡片应为原子概念，标题中出现连词暗示卡片可能包含多个概念应被拆分。

**v4 教训**: 此维度 v4 未实施（v5 新增）

**v5 实现方式**: 纯脚本
1. grep 连词词表: 与/和/及/以及/and/vs/versus/or (排除 "and" 出现在固有名词中如 "Model Context Protocol and ..." 的情况)
2. 仅检查 title 字段
3. 排除: comparison 类卡片标题中的 "vs/versus" 是合理的

**判定标准**: 非 comparison 卡标题不含连词
**验收阈值**: 连词标题 < 5%（信息性指标，非硬性门槛）

---

### C3 概念重叠检测

**问题定义**: 两张卡共享过多同源脚注（引用同一源文本的相同段落），暗示概念边界模糊、可能应合并。

**v4 教训**: 此维度 v4 未实施（v5 新增）

**v5 实现方式**: 纯脚本
1. 对每张卡提取全部 `[^src-N]` 的 path + section + quote_prefix(前 30 字符) 作为指纹
2. 对每对卡计算共享指纹数
3. 共享 > 2 条同源段脚注的卡对标记为 overlap suspect

**判定标准**: 两卡共享 > 2 条指向同一源同一段落的脚注
**验收阈值**: overlap pairs < 3%（相对于总卡对数）

---

### C4 循环/强连通分量检测

**问题定义**: related 图中的强连通分量（mutual dependency cycles > 2 nodes）可能暗示概念循环定义。

**v4 教训**: 此维度 v4 未实施（v5 新增）

**v5 实现方式**: 纯脚本
1. 从 related 构建有向图
2. 运行 Tarjan 算法检测所有强连通分量（SCC）
3. 报告 size > 2 的 SCC

**判定标准**: size > 2 的 SCC 需人工评估是否为合理概念簇
**验收阈值**: 信息性指标（SCC 不一定是错误，但需标注）

---

### D1 源消化率

**问题定义**: 每个 data/raw/ 源目录是否至少产出一张卡片，未消化的源意味着信息遗漏或读取失败。

**v4 教训**: v4 的 failed_sources 列表可追溯

**v5 实现方式**: 纯脚本
1. 扫描 data/raw/ 所有源目录，构建 source_id 集合
2. 从所有卡的 source_ids 字段构建已消化集合
3. 未消化 = 全量源 - 已消化源
4. 验证 loop_state.json 中的 failed_sources 与未消化源匹配

**判定标准**: 未消化源应出现在 loop_state.json 的 failed_sources 中
**验收阈值**: 未被记录的遗漏源 = 0

---

### D2 覆盖率 (F2/F3)

**问题定义**: 产出卡片覆盖了源总量的多大比例，每个源的平均产出卡片数。

**v5 实现方式**: 纯脚本
1. 统计: 总源数、已消化源数、消化率
2. 统计: 每源平均卡片产出、中位数、最大值

**判定标准**: 消化率 = 已消化源 / 总有效源
**验收阈值**: 消化率 > 80%

---

### E1 跨源泄漏检测

**问题定义**: 卡片 body 中提及了另一张卡的 canonical_concept（或其 aliases），但该被提及的卡与当前卡不共享同一 source_id，且当前卡 body 中对该概念无 `[^card-N]` 脚注锚定。这可能意味着 LLM 在写作时泄漏了其他源的知识。

**v4 教训**: 此维度 v4 未实施（v5 新增）

**v5 实现方式**: 脚本初筛 + agent 判断
1. 构建: 每张卡的同源组（共享至少一个 source_id 的所有卡）
2. 构建: canonical_concept + aliases 的全量索引
3. 对每张卡 body，搜索是否出现了非同源组卡片的 canonical_concept/alias
4. 排除: body 中有 `[^card-N]` 指向该卡（合法跨引用）
5. 排除: 通用技术术语（"LLM"、"RAG"、"agent" 等）
6. 产出 suspect 清单

**判定标准**: 非同源概念在 body 中出现且无卡间脚注锚定
**验收阈值**: confirmed leakage < 1%

---

### E2 无脚注段落幻觉检测

**问题定义**: 卡片 body 中存在超过 2 句的段落，完全没有任何 `[^src-N]` 标记，意味着该段落内容可能是 LLM 自行生成而非源自引用材料。

**v4 教训**: 此维度 v4 未实施（v5 新增）

**v5 实现方式**: 纯脚本
1. 将卡片 body 按空行分段
2. 对每段计算句数（按中英文句末标点断句: 。/！/？/./?/!）
3. 检查段落中是否包含至少一个 `[^src-N]` 或 `[^card-N]` 标记
4. 句数 > 2 且无任何脚注标记的段落标记为 suspect
5. 排除: frontmatter 下紧接的单句引言段

**判定标准**: > 2 句的段落应至少有一个脚注锚定
**验收阈值**: 无脚注段落率 < 10%

---

### F1 Loop 独立性

**问题定义**: v5 loop 的产出不应包含对先前 loop 的引用或依赖（每个 loop 是独立 0→1 过程）。

**v4 教训**: loop 交叉引用是常见 session 污染

**v5 实现方式**: 纯脚本
1. 在 cards/ 全量文件中 grep 搜索: `v0`, `v1`, `v2`, `v3`, `v4`, `loop_20260`, 以及具体 loop 标识
2. 排除: 卡片 body 中讨论 "version" 概念时自然出现的 "v1/v2" 不算（检查上下文）
3. 在 justification/ 全量文件中同样检查

**判定标准**: 无对先前 loop 产物路径的硬引用
**验收阈值**: 硬引用 = 0

---

### F2 JJ 文件完整性

**问题定义**: 每张 accepted 卡应有对应的 justification 文件（`../justification/{card-id}.md`），justification 文件应存在且非空。

**v5 实现方式**: 纯脚本
1. 遍历 cards/ 目录中 status: accepted 的卡
2. 检查 justification/ 目录中是否存在同名 .md 文件
3. 检查文件是否非空（> 10 bytes）

**判定标准**: 每张 accepted 卡有对应非空 justification 文件
**验收阈值**: 完整率 100%

---

## 执行流程

```
┌─────────────────────┐
│ audit_mechanical.py │  ← 14 维度一次性执行
│ (100% 覆盖脚本)     │
└──────────┬──────────┘
           │ JSON report + suspect 清单
           ▼
┌─────────────────────┐
│ Agent JUDGE 阶段     │  ← 仅处理 A3/A4/E1 的 suspect
│ (语义验证)           │
└──────────┬──────────┘
           │ confirmed findings
           ▼
┌─────────────────────┐
│ 人工确认             │  ← 关键 findings 最终裁决
└─────────────────────┘
```

## 产出物

1. `audit_mechanical.py` — 完整脚本，输出 JSON
2. `v5_mechanical_audit_report.json` — 脚本执行结果
3. `v5_suspect_list.json` — 需 agent 进一步验证的 suspect
4. 本文档 — 方案说明
