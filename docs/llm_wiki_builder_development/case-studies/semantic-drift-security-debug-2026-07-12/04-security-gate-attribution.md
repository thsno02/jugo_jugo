# 04. 安全 Gate 的跨线程归因

## 4.1 两种机制，不是一个事件

本案例同时出现了两种表面上都与“安全”相关、实际上机制完全不同的行为：

| 机制 | 执行位置 | 结果 |
|---|---|---|
| 本地敏感模式扫描（local pattern scan） | v2/v3 worker 调用本地 shell/regex | 正常执行，产生 SHA 假阳性，任务完成 |
| cybersecurity content gate | 父任务的其他 runtime/reviewer sub-agent turn | agent 以 `possible cybersecurity risk` errored |

前者是任务主动执行的质量检查；后者是模型/任务内容安全边界返回的 turn-level error。没有证据表明前者触发后者。

## 4.2 v2/v3 本地扫描时间线

| 北京时间 | 事件 | 结果 |
|---|---|---|
| 10:22:43 | 第一次敏感模式检查 | shell 引号错误 `unmatched`，不是 policy denial |
| 10:24:32 | 对 `extraction-v2.json`、`extraction-v3.json` 执行有效扫描 | 只报告两个 `sha256` 字段所在位置 |
| 10:24:43 | 提取实际命中形状 | 是 SHA256 中的 18 位数字片段，不是 credential |
| 10:24:57 | 删除 `sha256` 字段后复检 | 零命中 |
| 10:25:09 | 原任务结束 | `task_complete`，无 turn error |

证据分别见 [E-V23-SCAN-PARSE-ERROR](07-evidence-index.md#e-v23-scan-parse-error)、[E-V23-SCAN](07-evidence-index.md#e-v23-scan)、[E-V23-SHA-FALSE-POSITIVE](07-evidence-index.md#e-v23-sha-false-positive)、[E-V23-SCAN-CLEAN](07-evidence-index.md#e-v23-scan-clean) 和 [E-V23-COMPLETE](07-evidence-index.md#e-v23-complete)。

这条线程没有 classifier decision、audit id、denied/refused、policy action 或 cybersecurity error。任务完成本身是一个强反例：若该扫描已经在此线程触发阻断，原 turn 不应以正常完成结束。

## 4.3 真实 gate 时间线

`S-PARENT` 中出现五个不同 sub-agent path 的真实 gate：

| 北京时间 | Evidence | 子任务类别 |
|---|---|---|
| 11:52:33 | [E-GATE-001](07-evidence-index.md#e-gate-001) | runtime/security review 相关子任务 |
| 13:33:25 | [E-GATE-002](07-evidence-index.md#e-gate-002) | 同一父任务下另一子任务 |
| 16:26:08 | [E-GATE-003](07-evidence-index.md#e-gate-003) | 对抗性 regression/reviewer 轨迹 |
| 19:08:47 | [E-GATE-004](07-evidence-index.md#e-gate-004) | runtime integrity 审查 |
| 19:30:00 | [E-GATE-005](07-evidence-index.md#e-gate-005) | reviewer 读取审计内容并设计 fresh mutation |

这些记录都明确返回：`This content was flagged for possible cybersecurity risk`。所以“真实 gate 是否存在”不是推断；不确定的是用户 19:42 的提问具体指向哪一次，以及内部 detector 为什么作出判定。

## 4.4 真实 gate 的任务语义

父任务附近的 runtime/reviewer 工作包含以下组合：

- exploit reproduction / bypass
- malformed transaction + write entrypoint
- symlink pointing outside run root
- hardlink、no-follow、TOCTOU
- attacker-controlled path
- HMAC/trust root replacement
- replay / tamper
- 设计 fresh mutation

这些词单独并不等于有害任务；整体目标也是用户授权仓库中的防御性完整性修复。但组合后具有明显双重用途安全工程（dual-use security engineering）表面形态。

更重要的是，至少最后一个 reviewer 的初始 prompt 已明确：本地授权、只读、无网络、无第三方目标。它成功启动并运行数分钟后才返回 gate。这使“初始 prompt 缺少授权说明”不再是充分解释，并提高了以下候选阶段的可能性：

1. 读取已有审计报告后，整体上下文风险升高；
2. 为满足 `fresh mutation` 开始生成具体绕过或 race 序列；
3. 工具调用或最终输出再次接受内容分类；
4. 异步 initial screening 延后返回。

目前不能区分上述阶段，也不能确认 gate 是否读取内部推理、工具参数、工具结果或最终输出。

## 4.5 网络行为核验

对 `S-V23` 原始任务窗口的工具记录统计显示：

- 40 次本地执行；
- 3 次等待；
- 0 次 web/browser/network 工具调用；
- 未见 HTTP client、上传下载、远程 Git、SSH/SCP 或外部 endpoint 命令。

因此可以写：**没有任务主动发起的外部网络工具调用**。

不能写：**系统层面完全没有网络流量**。Codex 客户端正常模型服务通信、Desktop 基础设施路由以及未被该日志覆盖的 OS packet 不在证据范围内。

Desktop 日志中的 `browser use session route` 属于多个无关任务共享的 UI 生命周期消息，没有网页导航、URL 或浏览器动作证据。事故窗口附近的 `unknown conversation` / `No turns` overlay 错误在扫描前已经存在，不能归因为安全事件。

## 4.6 为什么错误归因发生在旧线程

用户于北京时间 19:42 在 `S-V23` 中提问，距离该线程扫描约 9 小时 17 分，距离父任务最近一次真实 gate 约 12 分钟。[E-USER-GATE-QUESTION](07-evidence-index.md#e-user-gate-question)

`S-V23` 是 `fork_context:false` 的窄上下文 worker。它看得到：

- 自己执行过一组 credential/PII regex；
- 自己刚讨论过 `sensitivity_decisions`；
- 用户现在问安全审计。

它看不到或没有主动回查：

- 父任务其他 sub-agent 的五次 gate；
- 最近一次 gate 的 runtime reviewer prompt；
- gate 与具体 thread/turn 的绑定关系。

在这种信息不对称下，旧 regex 是最显著的本地候选。模型先形成 plausible explanation，再在后续追问中把它固化为事实。这是 availability-driven attribution（由可用上下文驱动的归因），不是经过跨线程取证的根因分析。

## 4.7 归因结论

| 命题 | Verdict |
|---|---|
| v2/v3 worker 主动运行了敏感模式扫描 | confirmed |
| 扫描发现了真实 AK/secret | contradicted |
| v2/v3 线程发生 cybersecurity gate | contradicted by normal completion and zero turn error |
| 父任务其他子任务发生真实 gate | confirmed |
| 用户提问更可能指向最近父任务 gate | inference，时间证据较强但无 UI event id |
| v2/v3 regex 触发这些 gate | unsupported，且被多个反例削弱 |
| runtime/reviewer 执行轨迹触发 gate | plausible inference |
| 精确 classifier 原因 | unknown |

## 4.8 事件类型修正

“网络安全审计”是用户对现象的描述。根据可见记录，更准确的工程术语是：

> **sub-agent turn-level cybersecurity content gate**

它不是已证实的 IDS、WAF、DLP endpoint 或网络外发拦截。文档保留用户原称呼作为问题入口，但所有分析使用实际可证事件类型。
