# Main-agent 长程执行计划

本计划给下一位主控 agent 使用。它的目标不是再讨论 loop 应该是什么，而是让新的 main-agent 拿到文件系统后，可以把整个 LLM Wiki loop 落实下去：持续生产 KB，持续演化 skills、sub-agent prompt、任务模板和控制面，同时保留 out-of-loop 的反思能力。

## 0. 先读什么

恢复时只先读这些文件：

1. `llm_wiki/loop/loop_state.json`
2. `llm_wiki/loop/loop_manifest.json`
3. `llm_wiki/loop/RUNBOOK.md`
4. `llm_wiki/loop/queues/task_queue.md`
5. `llm_wiki/loop/reports/loop_report.md`
6. 本文件

如果状态、队列和报告矛盾，以 `loop_state.json` 为准，先修控制面，再派发执行者。

不要从聊天记忆恢复循环。不要先读 `legacy/`。不要把 `user-insights/` 当成事实来源。

## 1. 当前稳定目标

当前 loop 的生产目标是：

```text
data/ 中一个本地来源
-> 事实候选
-> 一张草稿原子事实知识卡
-> 一份可读出处论证
-> 一份独立审计
-> 一张已采纳知识卡
```

当前非目标仍然是：

- 枢纽页。
- 聚类。
- 主题覆盖。
- 复杂元数据。
- 没有来源支撑的 agent 综合。

只有当已有足够数量的 accepted cards，并且主控 agent 写出新的阶段决策后，才能讨论 hub、cluster 或 topic 层。当前阶段不要提前铺这些结构。

## 2. 主控 agent 的身份

主控 agent 是决策者，不是执行者。

主控 agent 可以做：

- 读状态、队列、报告和任务包。
- 选择下一步最小动作。
- 用 `tools/` 创建任务包、渲染 dispatch、检查 scope 和交付。
- 派发预定义执行者。
- 检查 `loop_status.md`、`loop_delivery.md`、`read_log.md` 和产物。
- 写 `decisions/`。
- 在有失败证据时触发 skill、sub-agent prompt、任务模板或工具演化。
- 做 out-of-loop 反思，但反思必须落盘，并且不能直接替代生产执行。

主控 agent 不可以做：

- 亲自读大段来源并抽事实。
- 亲自写知识卡正文或出处论证。
- 亲自做知识卡审计并采纳。
- 用父聊天上下文补事实证据。
- 为了“推进快一点”绕开任务包和执行者。

如果主控 agent 发现自己开始具体生产知识，立即停止当前动作，写入 `decisions/` 或创建 `skill_evolution_worker` 任务。

## 3. 四条并行但隔离的链路

长程 loop 不是只有生产链路。它同时有四条链路，但每次只推进一个最小动作。

### 3.1 KB 生产链路

生产链路只围绕原子事实卡。

```text
source_mining_worker
-> card_drafting_worker
-> card_audit_worker
-> card_adoption_worker
```

每个 worker 默认 `fork_context: false`，只接收：

```text
system_prompts/base_worker.md
system_prompts/<role>.md
iterations/<iteration_id>/task.md
```

任何执行者结束前必须留下：

- `loop_status.md`
- `loop_delivery.md`
- `read_log.md`
- 任务包指定的 artifact

### 3.2 Skills / prompt 演化链路

skills、system prompts、task templates、tools 都可以演化，但只能由失败证据触发。

触发条件包括：

- 执行者越界读取或写入。
- 事实候选太粗或太少。
- 知识卡像中间状态、日志或主题报告。
- 出处论证不可读，或者像流水账。
- 审计标准不稳定。
- main-agent 被迫亲自执行具体生产。
- 文档主语言漂移。
- 同一类 concern 重复出现。

演化流程固定为：

```text
失败证据
-> skill_evolution_worker 任务包
-> 最小修改
-> scope / 交付校验
-> independent_evaluator 审计
-> main_agent 写 decisions/
-> 更新 loop_state / loop_report
```

不要直接凭感觉修改 skill。不要把一次偶发失败扩大成复杂新框架。

### 3.3 Sub-agent prompt 演化链路

sub-agent prompt 是控制面的稳定边界，不是每轮临场发挥。

可以修改：

- `system_prompts/<role>.md`
- `task_templates/<role>_task.md`
- `loop_manifest.json` 中角色的默认输入和写入。
- 必要时新增 role，但必须先证明现有 role 无法表达任务。

新增或修改 role 的门禁：

- 角色目标可以一句话说清。
- 允许输入、禁止输入、允许写入可以写清。
- 角色不承担主控 agent 的状态迁移、采纳决策或停止逻辑。
- 角色不会把当前阶段带到 hub、cluster 或 topic coverage。
- 修改后要有独立审计。

### 3.4 Out-of-loop 反思链路

长程任务需要思维性活动，但反思不能污染生产链路。

允许的反思活动：

- 轨迹反思：当前几轮是否真的支持状态迁移。
- 组件反思：哪些大组件或小组件在拖慢循环。
- 失败簇归纳：重复 concern 是否来自同一设计缺口。
- 文件系统整理：是否有产物位置、命名、链接或恢复入口混乱。
- 角色边界检查：main-agent 是否又变成执行者。
- 成本/周期检查：是否因为流程过重导致生产周期异常长。

反思的写入位置：

```text
llm_wiki/loop/reflections/<timestamp>-<topic>.md
llm_wiki/loop/decisions/<timestamp>-<decision>.md
```

如果 `reflections/` 不存在，先创建。反思文档只能使用 loop 状态、交付、审计、报告和人类可读记录作为材料；不能把反思结论写成知识卡事实。

反思结束必须给出一个明确下一步：

```text
continue_production
skill_evolution
prompt_evolution
tooling_repair
filesystem_repair
human_checkpoint
defer
```

## 4. 大组件和小组件的迭代逻辑

把系统分成两层，不要混在同一轮里改。

### 4.1 小组件

小组件包括：

- 单个 task template。
- 单个 system prompt。
- 单个工具脚本。
- 单张知识卡。
- 单份出处论证。
- 单个索引字段。

小组件可以高频迭代，但每轮只改一个变量，并保留失败证据。

### 4.2 大组件

大组件包括：

- KB schema。
- 角色体系。
- 状态机。
- 文件系统布局。
- 采纳策略。
- provenance 范式。
- 后续 hub/cluster 阶段设计。

大组件只能低频迭代。触发前必须有至少一个反思文档和一个 decision。大组件变化后，必须先跑小规模 smoke，再继续生产。

## 5. 文件系统管理规则

文件系统是 loop 的记忆，不是附属品。

### 5.1 目录职责

- `data/`：来源和来源获取日志。
- `llm_wiki/kb/`：最终 KB 产物面。
- `llm_wiki/loop/`：控制面、状态、任务、审计、报告和决策。
- `llm_wiki/skills/`：项目内 skills。
- `user-insights/`：人类输入和设计演化的 recall 记录，不是事实来源。
- `legacy/`：历史版本和错误路线，不是当前恢复入口。

### 5.2 iteration 目录

每个实际动作一个 iteration：

```text
llm_wiki/loop/iterations/<iteration_id>/
  task.md
  dispatch_request.json
  loop_status.md
  loop_delivery.md
  read_log.md
  artifacts/
```

iteration 完成后不要重写历史产物。需要修订时开新 iteration，并在 `decisions/` 说明为什么。

### 5.3 报告和决策

`reports/loop_report.md` 是人类可读的累计报告。

`decisions/` 记录状态迁移、接受残余风险、拒绝产物、修改 skill、修改 prompt、进入新阶段等关键判断。

任何重要状态迁移都必须同时更新：

- `loop_state.json`
- `reports/loop_report.md`
- 必要时更新 `queues/task_queue.md`
- 必要时写 `decisions/`

### 5.4 链接规则

报告中的证据链接必须指向 canonical 文件。

不把 pre-skill fallback、旧审计报告或 legacy 文件作为当前入口，除非文档明确说明它们只是历史证据。

## 6. 下一位 main-agent 的具体启动步骤

### Step 1：确认状态

读取 `loop_state.json`。当前预期应为：

```text
READY_FOR_SOURCE_MINING
```

如果不是，先按状态文件修复或恢复。

### Step 2：选择一个本地来源

读取：

```text
data/manifests/acquired_sources_index.md
data/manifests/sources.jsonl
```

只选一个 `status: ok` 的本地来源。优先选择：

- 本地文件可读。
- 来源权威或原始度高。
- 适合产出清楚事实候选。
- 不需要网络 retrieve。

不要按主题覆盖选源。不要为了平衡 topic 而选源。

### Step 3：创建 source mining 任务包

使用：

```text
python3 llm_wiki/loop/tools/create_task.py \
  --role source_mining_worker \
  --iteration-id <iteration_id> \
  --task-id <task_id> \
  --set source_manifest=data/manifests/acquired_sources_index.md \
  --set source_path=<chosen_source_path>
```

然后人工检查 `task.md`：

- 允许输入只包含当前来源和必要 manifest。
- 禁止输入包括父聊天、legacy、其它来源、旧审计。
- 允许写入只包含当前 iteration 和可选候选路径。
- 成功门禁和阻塞条件完整。

运行：

```text
python3 llm_wiki/loop/tools/validate_scope.py <task.md>
python3 llm_wiki/loop/tools/render_dispatch.py --role source_mining_worker --iteration-id <iteration_id>
```

### Step 4：派发 source_mining_worker

派发时：

- `fork_context: false`
- 使用 `dispatch_request.json`
- 明确不使用父聊天上下文
- worker 完成后关闭

主控 agent 等待或用 monitor 检查结果。不要在等待时自己读来源抽事实；可以做不重叠的控制面维护。

### Step 5：验收来源挖掘

运行：

```text
python3 llm_wiki/loop/tools/inspect_delivery.py <iteration_id>
```

检查：

- `fact_candidates.md` 是否存在。
- 候选是否有具体 source evidence。
- 是否至少有几个可继续 drafting 的候选，除非来源不足。
- 是否出现主题页、hub、cluster、复杂元数据。
- `read_log.md` 是否记录越界读取。

如果通过，写 decision 或更新报告，选择一个候选进入 drafting。不要一次性把所有候选都写成卡。

### Step 6：单卡流水线

每次只推进一张卡：

```text
card_drafting_worker
-> card_audit_worker
-> card_adoption_worker
```

每一步都新建 iteration。每一步都保留 task、status、delivery、read_log 和 artifacts。

如果 audit 是 `revise`，不要 main-agent 自己修卡。创建新的 drafting revision 任务。

如果 audit 是 `reject` 或 `defer`，记录原因，回到 fact candidate 队列或 source mining。

### Step 7：小批量后做反思

当出现以下任一情况时，暂停生产，做一次 out-of-loop 反思：

- 已完成一个小批量 accepted cards。
- 连续两轮出现同类 revise / reject。
- source mining 产出密度明显过低。
- card drafting 周期明显过长。
- main-agent 感到需要亲自补内容。
- 文件链接或状态恢复出现混乱。

反思文档写到：

```text
llm_wiki/loop/reflections/
```

反思不直接修改 KB。反思必须选择一个下一步动作。

## 7. 演化优先级

当生产和演化冲突时，按以下优先级：

1. 安全边界：越界读取、越界写入、事实来源污染。
2. 可恢复性：状态、报告、交付、链接不一致。
3. 知识可靠性：来源证据不足、provenance 不可读。
4. 输出可读性：卡片不像卡、语言漂移、脚注布局错误。
5. 生产效率：周期过长、候选太少、任务包太重。
6. 后续结构：索引、轻量链接、未来 hub/cluster 准备。

不要为了效率牺牲 provenance。不要为了结构感提前做 hub。

## 8. 网络和外部 runtime

当前公司电脑环境下：

- 优先使用 `data/` 已获取来源。
- 网页 retrieve 有限制时，最多有限尝试，记录后搁置。
- 不把 retrieve 失败当作整个 loop 阻塞。

外部 runtime：

- 短期首选原生 Codex sub-agent + `render_dispatch.py`。
- Claude CLI 可作为无工具写作 worker 候选，但写文件闭环未验证。
- Codex CLI 可作为外部 read-only worker 候选，但会触发已信任 hooks 并有日志噪声。

不要让外部 CLI 绕过任务包、写入边界和交付检查。

## 9. 人类不在时如何继续

人类离开电脑时，主控 agent 可以继续推进窄任务，但必须满足：

- 当前动作来自 `queues/task_queue.md` 或 `loop_state.json.next_action`。
- 每轮只推进一个最小动作。
- 每轮结束都更新状态和报告。
- 任何扩大 scope、改变 schema、进入 hub/cluster、批量采纳、同步外部 doc folder、git push，都需要人类明确授权。

如果不知道下一步是什么，停止生产，写 `loop_state.json.blockers` 和 `reports/loop_report.md`，不要凭空发明大任务。

## 10. 自检清单

每次准备结束主控回合前检查：

- `loop_state.json` 是否反映真实状态。
- `queues/task_queue.md` 是否没有过期任务。
- `reports/loop_report.md` 是否有最新过程和证据链接。
- 新 iteration 是否有 `task.md`、`loop_status.md`、`loop_delivery.md`、`read_log.md`。
- 是否有必要写 `decisions/`。
- 是否有任何人类可读文档语言漂移。
- 是否有任何事实来自聊天、user-insights 或 agent 综合。
- 是否需要触发 skill/prompt/tool 演化，而不是继续生产。

如果有一项不确定，先修控制面，不继续生产。
