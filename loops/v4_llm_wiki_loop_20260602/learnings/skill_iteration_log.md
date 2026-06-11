---
schema: v4_learnings
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-12
topic: skill_iterations
purpose: retrospective
---

# 技能设计迭代记录

本文追踪 v4 四个核心技能从 v3 设计意图到 Phase 2 种子测试再到 Phase 4 全量运行的演化过程。每个技能记录：设计意图 → 种子发现 → 具体修改 → 遗留问题 → 关键洞察。

---

## 1. Questioning Skill (`skills/questioning/SKILL.md`)

### 1.1 原始设计意图（from v3 spec）

v3 spec S2.2 定义了五阶段提问策略：广度扫描 → 深度追问 → 评判性提问 → 批判性/对比性提问 → 覆盖率自检。关键设计决策：questioner 拥有材料全文（不是从 digest 盲问），digest 是 reviewer 的工具而非 questioner 的唯一视野。

### 1.2 种子测试（Phase 2）发现

在 karpathy-gist-llm-wiki 上运行完整 loop（15 张卡 → 审查后 19 张）暴露了：

- **次要节遗漏**：Phase 5 覆盖率自检跳过了"看似次要"的节（Tips、Note），但这些节往往包含材料独有的操作性知识
- **原子性盲区**：部分 Q&A 回答实际覆盖了两个独立 idea 却只产出一张卡；标题含「与」连词是拆卡信号
- **canonical 重复追问**：Phase 2 追问偶尔重复已有 canonical 覆盖的概念

### 1.3 具体修改

1. **Phase 5 覆盖率规则扩展**：加入"包括看似次要的节（如 Tips、Note）——材料认为值得写的节就值得至少被触碰"
2. **原子性检查**：Phase 5 加入显式自检步骤——"是否有 Q&A 实际覆盖了两个独立 idea 却只产出一张卡？如果标题需要连词，大概率需要追问来拆分"
3. **canonical 反馈机制**：每轮 reframe 后返回已产出 canonical_concept 列表，questioner 在 Phase 2 追问前显式检查

### 1.4 遗留问题

- 全量运行时，长材料（arxiv 论文 200+ pages via bundle）的 Phase 2 深度追问有时在 3 层后仍未触底——SATISFIED 判据的"信息递减"标准依赖主观判断
- Phase 4 批判性提问对单源材料价值有限（材料内部张力不多见），但跳过 Phase 4 又会导致隐含假设被遗漏

### 1.5 关键洞察

> **Digest as scope-without-bias**：digest 的正确定位是"提供足够 scope 让 questioner 能问出定向问题，但不提供足够细节以至于偏置提问方向"。questioner 拥有全文意味着 digest 不再承担信息传递职能——它变成了覆盖率审计的 checklist。

---

## 2. Reader Skill (`skills/reader/PROMPT.md`)

### 2.1 原始设计意图（from v3 spec）

v3 spec S2.6 定义了 reader 的四标准：源忠实、定位精确、卡片就绪、显式标注不确定性。reader 是被动应答者，不主动引导。首轮产出 digest（scope + toc + core_claims + terms）。

### 2.2 种子测试（Phase 2）发现

- **位置格式不一致**：reader 混用中文序数（"第三段"）和英文格式（"Section 3, P2"），导致 reframing 产出的 `[^src-N]` footnote 位置描述混乱
- **过度回答**：部分回答注入了材料外的背景知识（reader 的通用知识泄露）
- **分点信号缺失**：当回答覆盖多个独立 idea 时，未用 (a)(b)(c) 标记，reframing 难以判断拆卡

### 2.3 具体修改

1. **统一位置格式**：明确规定"使用英文节标题路径 + 段落编号，如 `"The core idea" P2`、`"Architecture > The schema" P1`。不要混用中文序数和英文格式——始终用 `Section > Subsection PN` 格式"
2. **不确定性标注强化**：三级分类——材料未讨论 / 材料仅部分讨论 / 材料表述模糊
3. **分点标记**：加入"如果一个回答覆盖多个独立 idea，用分点 (a)(b)(c) 标记，方便 reframing 拆卡"

### 2.4 遗留问题

- 全量运行时，reader 对长材料（>100KB bundle）的 KV cache warm 策略未标准化——有时同一 session 内多轮回答质量递减
- footnote 位置格式在实际卡片中仍有不一致（审计发现），部分是因为 reframing 未严格执行转化

### 2.5 关键洞察

> **Reader footnote format standardization**：位置描述的一致性直接决定了 typed footnote 的可操作性。`[^src-N]` 的 `-- <location>` 部分如果格式混乱，下游审计和跨卡引用验证就无法自动化。统一为 `"Section Title" PN` 格式是最低成本、最高收益的标准化决策。

---

## 3. Reframing Skill (`skills/reframing/PROMPT.md`)

### 3.1 原始设计意图（from v3 spec）

v3 spec S2.3 定义了 Q&A → card 的转化规则：对话体 → 知识陈述体；metadata 填写（canonical_concept grep 复用、aliases、summary 稠密 grep 靶子）；typed footnote 锚定；justification journal creation 事件。

### 3.2 种子测试（Phase 2）发现

- **cross-link 缺失**：首批 15 张卡几乎零 `[^card-N]` footnotes——reframing 只关注了 src-type 引用，忽略了卡间链接
- **拆卡信号不敏感**：回答含 2+ 不同源节 footnotes 时应考虑拆卡，但实际未执行
- **summary alias 覆盖率低**：summary 行缺少 aliases 导致 grep 召回失败
- **hedging 丢失**：reader 回答中的不确定性标记（"材料仅部分讨论"）在转化为卡片后被删除，变成了确定性陈述

### 3.3 具体修改

1. **Cross-link 规则新增**：规则 5 完整定义——"每张新卡产出后，检查本轮已有卡 + 已有 KB 卡的 canonical_concept 和 aliases；如果新卡与某张已有卡共享主题或存在明确关联 → 在新卡 body 中添加 `[^card-N]` footnote"
2. **拆卡信号强化**：新增"拆卡信号：回答引用了 2+ 个不同源节标题的 footnotes → 大概率应拆卡"
3. **Summary 验证规则**：新增"验证：如果 grep 任何一个 alias 无法命中此 summary，则不合格"
4. **标题测试**：新增"如果标题需要『与』『和』等连词连接两个名词短语，几乎肯定应该拆成两张卡"

### 3.4 遗留问题

- **Hedging 保留**：reframing prompt 中缺少显式规则要求保留 reader 回答中的不确定性标记。实际卡片中，"材料暗示 X 但未明确论证"这类 hedging 经常在转化时被省略，变为"X 是 Y"的确定性陈述
- **cross-link 密度审计**发现仍有 gap：跨家族链接覆盖率仅 25%，说明 reframing 时的卡间关联检查主要局限于同批次/同源材料内

### 3.5 关键洞察

> **Reframing must preserve hedging**：知识卡的价值不仅在于记录 claims，更在于记录 claims 的确信度。reader 回答中的 hedging（"材料暗示"、"未明确论证"、"仅部分讨论"）是源忠实性的关键组成部分。reframing 的对话体 → 陈述体转化不应删除这些限定词——它们应转化为卡片正文中的认知标记（如"据材料推测"、"源证据有限"）。

---

## 4. Reviewer Skill (`skills/reviewer/PROMPT.md`)

### 4.1 原始设计意图（from v3 spec）

v3 spec S2.4 定义了 reviewer 为独立角色，做覆盖率检查 + 源忠实抽查。verdict = pass / needs_more_questions。spec 隐含的心理模型是 reviewer 作为"质量门控"——不通过就不能进入 ingest。

### 4.2 种子测试（Phase 2）发现

- **早 pass 问题**：reviewer 对覆盖率采用宽松标准时，部分 gap 被忽略（"部分覆盖也算 covered"的规则被过度使用）
- **抽查覆盖率有限**：3-5 张卡的源忠实抽查是抽样性质，无法发现系统性问题（如 arxiv text.txt 误读，需要全量审计才能发现）
- **reviewer 无法发现数据层问题**：reviewer 验证的是"卡的内容是否有源支撑"，但如果源本身是浅层的（text.txt 仅含摘要），reviewer 的 supported verdict 仍然成立——问题在源的深度而非引用的准确性

### 4.3 具体修改

1. **附加检查新增**：源节覆盖检查（材料节标题 vs footnote 引用位置比对）、链接密度检查（>50% 无 card-type footnote → 警告）、重叠检测（共享 >2 条同源段 footnotes → potential_overlap）
2. **角色定位调整**：从"质量门控"调整为"quit-audit"——重点从"足够好才能通过"变为"是否有 early stop 的系统性证据"
3. **审查后 JJ 事件**：通过审查的卡片 append review 事件到 justification journal

### 4.4 遗留问题

- reviewer 无法检测"源深度不足"问题——这是数据采集层的职责，不是 extract 层能解决的
- 覆盖率检查依赖 digest 的 core_claims 质量——如果 digest 遗漏了某个重要主张，reviewer 也不会发现 gap

### 4.5 关键洞察

> **Reviewer as quit-audit not quality gate**：reviewer 的核心价值不是"保证每张卡质量"（这是不现实的 best-effort 系统中的预期），而是"防止系统性 early stop"。当 questioner 过早声明 SATISFIED 时，reviewer 通过 digest coverage 比对能发现遗漏区域。这是一个保守的安全网，不是精确的质量门控。认识到这个定位后，reviewer 的 verdict 标准可以适当宽松（ambiguous 不阻塞），同时附加检查（链接密度、源节覆盖）提供额外信号但不直接阻塞流程。

---

## 跨技能模式总结

| 模式 | 涉及技能 | 内容 |
|------|---------|------|
| Digest as scope-without-bias | reader → questioner | digest 提供方向不提供答案；questioner 拥有全文后 digest 退化为审计工具 |
| Reviewer as quit-audit | reviewer | 防 early stop，不做质量门控；verdict 宽松，附加检查补充 |
| Reframing must preserve hedging | reader → reframing | 不确定性标记是源忠实性的一部分；对话体→陈述体不删 hedging |
| Reader footnote format standardization | reader → reframing | 位置描述统一为 `"Section" PN` 格式；可操作性依赖一致性 |
| Canonical feedback loop | reframing → questioner | 每轮 reframe 后返回 canonical 列表；避免重复追问 |
| Cross-link as reframing responsibility | reframing | 卡间链接必须在 reframing 阶段主动建立，不能依赖后续 governance 补充 |

---

## 参考文件

- Questioning skill: `../skills/questioning/SKILL.md`
- Reader prompt: `../skills/reader/PROMPT.md`
- Reframing prompt: `../skills/reframing/PROMPT.md`
- Reviewer prompt: `../skills/reviewer/PROMPT.md`
- 原始 spec: `../../v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`
- 任务清单（Phase 2 记录）: `../task.md`
