# LLM Wiki 原子事实知识库

这是下一轮 KB 的可见工作入口。

当前目标不是枢纽页、聚类、主题覆盖，也不是重建一个复杂图谱。当前目标只有一个：

```text
来源 / 论文 / 博客 / 代码库 / 帖子
-> 事实候选
-> 草稿态 zet 风格原子事实知识卡
-> 出处论证
-> 已采纳原子事实知识卡
```

## 核心想法

知识本身是混沌的。图谱、双链、枢纽页、聚类都是对知识关系的建模，不是对知识本身的建模。

当前最重要的是把底层事实单元做实。原子不是绝对不可分，而是当前 KB 中足够小、足够清楚、足够可验证、可以被其它知识卡引用的相对粒度。

## 知识卡

知识卡是结果。

它应该像 zet 风格知识卡一样可读：

- 一个主要事实或当前被接受的事实。
- 短标题。
- 简洁正文。
- 轻量引用区和脚注区。
- 不写流程日志。
- 不写枢纽页或主题覆盖框架。
- 不把出处论证和审计过程塞进正文。

## 出处论证

出处论证不是事后挑战，也不是流水日志。

它是整理后的可读文档，用来说明这张知识卡为什么可以暂时被当作事实：

- 事实从哪里来。
- 来源为什么能支撑它。
- 哪部分是来源明说的。
- 哪部分是整理后的表述。
- 成立范围是什么。
- 目前为什么可以接受。

## 最小原子卡契约

初版只保留极简字段：

```text
statement
fact_type: known_fact | accepted_fact
support
scope
status: draft | accepted | rejected
```

不要一开始加入复杂元数据。依赖、标签、枢纽提示、置信度、失效条件等，只有在循环中证明必要时再演化。

## 语言约定

新写的人类可读文档以中文为主语言，并统一使用这些词：

- `source` 写作“来源”。
- `fact candidate` 写作“事实候选”。
- `card` 写作“知识卡”。
- `provenance` 写作“出处论证”。
- `worker` 写作“执行者”。
- `loop` 写作“循环”。
- `adoption` 写作“采纳”。
- `hub` 写作“枢纽页”，`cluster` 写作“聚类”，`topic` 写作“主题”。

允许保留英文的地方：文件名、路径、状态码、schema 字段、命令参数、包名、论文或网页原文标题，以及 `References` / `Footnotes` 这类固定 Markdown section 名称。

## 当前非目标

- 不做枢纽页。
- 不做聚类。
- 不追求主题覆盖。
- 不把旧 v1 枢纽骨架当作当前 KB 主体。
- 不把 agent 综合当作事实来源。

## 当前技能

当前活跃技能放在 `skills/`，主语言为中文：

- `llmwiki-loop-controller`：主控 agent 决策、派发、上下文隔离和偏差干预。
- `llmwiki-source-mining`：从单一来源抽取原子事实候选。
- `llmwiki-card-drafting`：把一个事实候选写成一张原子事实知识卡和出处论证。
- `llmwiki-card-audit`：审计知识卡的事实粒度、出处论证、适用范围和中文可读性。
- `llmwiki-card-adoption`：采纳审计通过的知识卡，更新最小索引和状态。
- `llmwiki-skill-evolution`：根据循环失败和审计结果迭代技能。

旧版 `legacy/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/skills/` 是节点/主题循环的历史快照，不是当前活跃技能集。

## 循环控制面

循环不再藏在聊天上下文里，也不再散落在 README、脚本输出和临时报告中。

当前循环控制面放在 `loop/`：

- `loop/README.md`：说明这个循环为什么存在、当前只做什么。
- `loop/RUNBOOK.md`：主控 agent 如何启动、恢复、派发、审计和干预。
- `loop/SUBAGENT_SCOPE.md`：执行者的行为边界、输入输出约束和禁止事项。
- `loop/loop_state.json`：可恢复的机器状态。
- `loop/loop_manifest.json`：角色、目录、门禁和非目标。
- `loop/system_prompts/`：主控 agent 和执行者的稳定 system prompt。
- `loop/task_templates/`：派发给执行者的任务包模板。
- `loop/iterations/`：每一轮循环的任务包、状态、交付和证据。
- `loop/reports/`：给人类和未来 agent 审计的循环报告。

主控 agent 是决策者，不是具体挖掘者。只要主控 agent 开始亲自做大段来源挖掘、写卡、采纳，就应该视为流程或技能设计出现偏差，并回到 `loop/system_prompts/main_agent.md`、`loop/SUBAGENT_SCOPE.md` 和 `loop/RUNBOOK.md` 修复。

## 知识库产物面

知识库产物放在 `kb/`。

当前 `kb/` 只用于沉淀事实候选、知识卡、出处论证和索引，不放循环控制文件。循环过程中的中间状态、任务包和审计报告都留在 `loop/`。

## 旧产物

旧产物已移入 `../legacy/`：

- `../legacy/v0_meta_kb_initialization_demo_20260524/`
- `../legacy/v1_topic_hub_skeleton_20260524/`
