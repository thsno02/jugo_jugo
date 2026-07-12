# 用户 GitHub Issue 写作偏好审计

## 结论

用户把 Issue 当作个人推理账本（reasoning ledger）和追加式研究日志（append-only research log），而不是一次写完的规范工单。

稳定模式是：**用一个短问题打开 Issue，在评论中保留假设、证据、失败、纠偏和最终判断；答案出现后关闭，后续证据推翻时重开；新问题从具体评论派生，并链接回原来的推理现场。**

因此，LLM Wiki 的 GitHub Issues 不应在创建时写成“问题—方案—结果”的完整文章。它们应尽可能还原用户当时不知道答案的状态。

## 审计范围

### `thsno02/potential-giggle`

- 25 个 Issues、34 条 comments。
- 22 个关闭、3 个开放。
- Issue 与评论均由 `thsno02` 撰写。
- 正文中位数约 83 字符；15/25 不超过 120 字符。
- 13/25 标题以问号结束，其中 10 个以 `How to` 开头。

代表证据：

- [#11 How to DIY the color for each character?](https://github.com/thsno02/potential-giggle/issues/11)：正文先记 requirements，解决方案后置到评论。
- [#24 How to insert some non-text elements into text?](https://github.com/thsno02/potential-giggle/issues/24)：评论依次保留 Plan A、Plan B；关键问题未解决，所以保持 open。
- [#31 Naming rules for background](https://github.com/thsno02/potential-giggle/issues/31)：关闭后因新案例暴露旧规格缺口而重开。
- [#1 Task Manager](https://github.com/thsno02/potential-giggle/issues/1)：评论分别展开 Text Structure、Font、Color、Size，Issue 本身承担父问题。

### `lowspace/zhipu-2024`

- 32 个非 PR Issues、41 条 comments。
- 22 个 Issue 有评论；作者均为 `lowspace`。
- 17/32 标题以问号结束；15/32 以“如何、怎么、为什么、如果、当”开头。
- 正文中位数约 291 字、5 行；没有固定模板。
- 13 个“已关闭且有评论”的 Issue 中，10 个在最后评论后 60 秒内关闭。

代表证据：

- [#5 如何设计 table finder agent？](https://github.com/lowspace/zhipu-2024/issues/5)：宽泛设计问题保持为父 Issue，后续派生具体问题。
- [#13 如何设计 CoT 逻辑？](https://github.com/lowspace/zhipu-2024/issues/13)：评论跨 19 天推进，结论不是创建时预写。
- [#23 Bad Case](https://github.com/lowspace/zhipu-2024/issues/23)：直接保留“之前的理解错了”和方案不好，不清洗失败历史。
- [#32 如何设计多轮对话？](https://github.com/lowspace/zhipu-2024/issues/32)：先写“重要假设”，再从评论派生 #33/#34。
- [#36](https://github.com/lowspace/zhipu-2024/issues/36)：三小时内保留“两套方案 → 都不 work → 修改后可用”的完整实验线。

## 稳定偏好

### 1. 问题优先，结论后置

标题通常是“如何……？”“为什么……？”或直接的错误症状。Issue 创建时不假装已经知道最终答案。

但标题不能只复制一句脱离语境的用户原话。一个可检索标题至少要交代：

- **阶段或版本**：问题发生在 v2、v3 还是跨版本；
- **构建对象**：知识卡、source pipeline、sub-agent 或 citation；
- **异常或冲突**：慢在哪里、错在哪里、哪两个目标冲突；
- **开放问题**：需要理解原因，还是需要选择方案。

例如，不使用“为什么 7h 只有 15 张 cards？”，而使用“为什么 v2 知识卡生产流程运行 7 小时只产出 15 张卡？”。后者保留用户的真实困惑，同时让脱离聊天现场的人知道 Issue 在讨论什么。

### 2. 正文轻量

正文一般只需要 1-5 行：当前观察、困惑或异常、一个工作假设、下一步需要确认什么。没有必要固定填满 Context、Decision、Outcome 等字段。

### 3. 评论才是主要内容

Requirements、Observation、Plan A/B、实验、raw evidence、纠偏和最终结论按时间追加。正文不承担整段历史。

Comment 应优先使用 Markdown 构建可扫描结构：

- 用 bullets 分开“观察、判断、候选解释、下一步、结果”；
- 用户原话使用 blockquote；
- raw evidence 使用代码块或表格；
- Issue/comment 关系独立成一条 link；
- 不把五个推理步骤压成一个长段落，也不为每条评论强制填满固定模板。

### 4. 保留不确定性和错误路径

“可能”“目前来看”“didn't work”“之前理解错了”“看错了”都应保留。不能用最终答案回写历史，制造线性成功叙事。

### 5. 具体证据推动抽象设计

用户偏好 literal query、错误信息、模型输出、JSON、SQL、schema、截图和对照实验。抽象架构 Issue 往往从一个具体 bad case 或结果异常中长出来。

### 6. 从评论派生新 Issue

当评论里的问题足够独立，就创建子 Issue，并链接到具体 comment，而不只链接父 Issue 首页。父 Issue 保留宽问题，子 Issue承载可关闭的小问题。

### 7. 最终评论靠近关闭

最后一条评论写当前可执行答案或设计判断，随后关闭。仍有关键变量未知则保持 open。新证据推翻时重开并追加 trigger，不修改旧结论。

### 8. 标签稀疏

标签只表达类型或组件，如 `question`、`bug`、`task`、`bad case`、`table finder`。不自动制造 priority、severity、status 等管理标签。

### 9. 中英自然混合

中文承载逻辑，`query`、`CoT`、`card`、`agent`、`work` 等术语直接嵌入，不做不必要翻译。

### 10. 发现流程时主动使用 Mermaid

由于这些 Issues 主要由 Codex 从历史交互中构建，只要 comment 中存在流程、状态变化、角色协作、条件分支或版本迁移，就应主动考虑 Mermaid，而不是只用长段文字描述。

适合画图的场景包括：

- 材料采集与缺口补充循环；
- main-agent / sub-agent 的职责和消息流；
- draft、comparison、fusion、publish 的生产顺序；
- similarity 召回之后的判断分支；
- citation 与 metadata 的派生关系；
- questioner / reader 的多轮读取；
- source type 到 reader/router 的分流；
- Issue 被派生、关闭、重开和替代的演化关系。

Mermaid 后必须继续解释关键取舍、执行顺序与依赖关系。图不能替代思考文本，也不能只是把 bullets 换成节点。

## 不应泛化的仓库习惯

- `RT`、空正文、`pic slots` 是快速便笺，不应成为模板要求。
- `ChangeLog/ChageLog/更新 log` 的混写反映捕获速度，不应复制拼写错误。
- `task manager`、checklist 只适合有限维度的 tracker，不适合所有 Issue。
- 两个仓库都是单作者研究仓库，不能据此推导多人协作礼仪和 assignee 规则。

## LLM Wiki Issues 的写作规则

1. 普通 Issue 只对应一个当前问题、异常或设计困惑。
2. 创建时只写当时已知内容，不写后来才出现的答案。
3. 用户原话作为主要叙事；模型输出只以 action/result 摘要出现。
4. 同一个问题的演化留在 comments，不拆成“问题文章”和“答案文章”。
5. 新的独立问题从触发它的 comment 派生为 sub-issue。
6. 版本 ChangeLog 只负责串联该版本采用、否定或重新打开的 Issues，不替代问题 Issue。
7. 失败方案保留，并明确标为 `didn't work` 或“之前理解错了”。
8. 关闭前追加一条简短 final comment；结论不需要重新整理成正式报告。
9. Reopen comment 必须说明新 trigger、旧结论缺口和新的待验证点。
10. 原始 evidence 按需附加，不统一套重型模板。
11. 一旦识别出稳定流程或关系结构，优先在对应 comment 内加入 Mermaid，并在图后解释关键决策。

## 推荐的三类 Issue

| 类型 | 标题 | 正文 | 评论演化 |
|---|---|---|---|
| 研究问题 | `为什么……？` / `如何设计……？` | 观察、困惑、假设 | 假设 → 实验 → 纠偏 → 当前答案 |
| Bad Case | literal query / 失败症状 | Expected / Actual + 最小证据 | 排查 → 方案 → 结果 → 是否派生设计问题 |
| ChangeLog | `v3 ChangeLog` | 本轮准备改变什么 | 链接 adopted / rejected / reopened Issues |

## 对上一版 Demo 的纠偏

上一版错误地预写了 `Seed question / State / Related / Timeline` 等完整合同，并把所有阶段压缩成确定性摘要。这会丢失用户原本的困惑、语气和错误路径。

新版 Demo 应：短正文、原话优先、评论追加、结论后置、链接到具体触发 comment，并让父子关系从事件中自然长出来。
