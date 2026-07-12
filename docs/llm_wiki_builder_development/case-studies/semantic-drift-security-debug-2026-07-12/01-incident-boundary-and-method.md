# 01. 事件边界与取证方法

## 1.1 研究问题

本案例要回答的不是笼统的“为什么触发安全审计”，而是六个可证伪问题：

1. `full_corpus.py` 为什么承担敏感模式扫描？
2. 该职能在人类、Planner、父代理和 E6 worker 各层分别是 implicit 还是 explicit？
3. `sensitivity_decisions` 从哪里产生，原始语义是什么？
4. v2/v3 worker 为什么又执行了一次本地扫描，漂移发生在哪个阶段？
5. 用户看到或指向的 cybersecurity gate 是否属于 v2/v3 线程？
6. 此前回答为什么把候选原因升级为确定原因？

## 1.2 必须分开的四个事件

| 事件 | 定义 | 当前状态 |
|---|---|---|
| `I1` archive privacy gate | 既有公开交互档案在进入 HTML 前执行 machine scan + human review | 已证实，早于 plugin 开发 |
| `I2` full-corpus readiness scan | `full_corpus.py` 对选定 repository corpus 做 secret/PII/path 形状检查 | 已证实 |
| `I3` v2/v3 output rescan | extraction worker 在完成语义 ledger 后额外运行通用敏感模式终检 | 已证实 |
| `I4` cybersecurity content gate | 父任务其他 runtime/reviewer 子任务返回 `possible cybersecurity risk` | 已证实，但不属于 v2/v3 线程 |

如果把 `I1`、`I2`、`I3`、`I4` 合并成一个“网络安全审计”，就会同时丢失作用域、执行者、时间和机制，后续因果分析必然失真。

## 1.3 证据模型

本专题沿用现有 Loop Engineering 审计的三级证据模型，并增加“不足证据”状态：

1. **直接证据（direct）**：代码、Schema、原始消息、工具调用、工具返回、任务终态或 byte-exact artifact。
2. **过程记录（process-record）**：代理派发、公开 commentary、Reviewer 报告、整改轮次和用户纠偏。
3. **推断（inference）**：由时间顺序、相同字段、相同 regex 类别或职责结构推导；必须同时记录替代解释。
4. **未知（unknown）**：本地证据不覆盖，尤其是 classifier 内部规则、阈值、所读上下文和远端事件关联。

以下表达受到严格限制：

- 只有 direct evidence 才能使用“发生了”“执行了”“返回了”。
- inference 使用“支持”“更可能”“与……一致”。
- 没有 event id、thread binding 和 detector metadata 时，不得写“由 X 触发”。

## 1.4 时间边界

本专题把证据分为三个窗口：

| 窗口 | 北京时间 | 用途 |
|---|---|---|
| `W1 genesis` | 08:32-10:12 | 人类目标、Planner 合同、E6 职能和 extraction prompt 的产生 |
| `W2 execution` | 10:12-10:25 | v2/v3 extraction、额外扫描、假阳性和正常完成 |
| `W3 gate/attribution` | 11:52-19:42 | 其他子任务的五次 gate、用户提问和事后错误归因 |

`W3` 的解释不能反向改写 `W2` 当时的行为理由；同样，`W2` 的本地扫描不能仅凭时间在前，就被认定为 `W3` gate 的原因。

## 1.5 来源别名与隐私控制

| Alias | 含义 | 发布策略 |
|---|---|---|
| `S-PARENT` | 人类发起的 plugin 开发父任务 | 只记录语义别名、时间、行号和行摘要 |
| `S-E6` | full-corpus readiness E6 worker | 同上 |
| `S-V23` | v2/v3 semantic extraction worker | 同上 |
| `R-ARCHIVE` | `docs/claude_interaction_replay/**` | 使用 repo-relative locator |
| `R-PLUGIN` | `plugins/llm-wiki-builder/**` | 使用 repo-relative locator |
| `L-DESKTOP` | Codex Desktop 与本地 audit logs | 只记录事件类别和时间范围，不复制账号或本机标识 |

原始 session locator 不进入专题。授权复核者可用 `07-evidence-index.md` 中的 source alias、UTC timestamp、原始行号和 line SHA256 在本机定位。

## 1.6 取证步骤

1. 冻结原始事件窗口，避免把事后调查文字当作原始触发证据。
2. 从人类消息开始追踪 Planner、父代理、E6 和 extraction worker 的每一次上下文压缩。
3. 对代码文件同时检查当前内容、首次补丁记录和 Git 基线状态；未跟踪文件不使用 `git blame` 伪造作者历史。
4. 将“字段诞生”“字段传播”“字段验证”“字段被解释”为四个不同动作。
5. 将本地工具执行、任务内容 gate 和网络访问区分为不同机制。
6. 对每个候选根因构建至少一个反例或反事实控制。
7. 最终结论同时给出置信度和仍缺失的观测量。

## 1.7 明确不做的声明

本专题不声称：

- 能恢复模型不可见的隐藏 chain-of-thought；
- 能看到 OpenAI 内部 classifier 的规则、阈值或全部上下文；
- 能从本地工具日志证明操作系统层面完全没有网络包；
- pattern finding 等于真实 PII 或真实 credential；
- 当前文件内容可以代替它首次产生时的历史版本；
- 用户提问一定指向五次 gate 中的某一个具体事件。

这些限制不是报告缺陷，而是可信安全分析必须保留的认识论边界（epistemic boundary）。
