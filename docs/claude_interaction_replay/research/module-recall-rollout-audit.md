# Module Recall 分阶段实施审计

## 工作原则

不直接全量生成。每次扩展必须经过数据合同、事实证据、页面表达和覆盖率四类检查；发现 schema 无法表达反证或事实状态时，先修改合同，再扩大数据。

## Stage A：V5 垂直 Demo

范围：V5 query timeline、入库机制、审计机制。

验收条件：

- query timeline 按真实时间排序，并能从节点跳转到完整用户输入。
- 关键节点和全部事件可切换，默认不把 22 条输入压成不可读的一条线。
- module node 区分 specified、executed、observed failure、retrospective 和 contradicted。
- 每个重要 claim 能返回 event ID 或仓库 artifact。
- 页面同时显示正向生产流和失败后的 feedback/rework。
- schema、event reference、artifact path、隐私和浏览器布局全部通过。

扩展前必须反思：

- 是否把报告中的 claimed coverage 写成真实 full coverage。
- 是否把终态文件存在倒推成原运行顺序。
- 是否用可计算结构指标替代用户关心的知识质量。

## Stage B：完整入库机制

沿稳定 stage IDs 回溯 v0-v5，至少覆盖 source acquisition、material intake、questioning/extraction、reframing、ingest、fusion、governance、publication 和 failure feedback。

验收条件：每个 stage 有版本演化、关键 event、artifact、状态变化和 known gaps；V5 失败不得覆盖 V3/V4 的真实来源。

## Stage C：完整审计机制

扩展 provenance、citation、fusion、schema、graph、state、FSJS、pipeline conformance、knowledge depth 和 cost/throughput controls。

验收条件：每个 control 均有审计对象、方法、通过条件、失败动作、运行时机、覆盖范围和证据状态。

## Stage D：全版本 Query Timeline

为 v0-v5 分别标注关键决策、动作、挑战、纠偏、验证与失败节点；全部事件仍由既有 JSONL 提供，不复制用户原文。

## 当前进度

- Stage A 数据合同：通过 schema 校验。
- Stage A V5 数据：通过两份独立证据审计、event/artifact 引用校验和桌面浏览器验收。
- Stage B：V0-V5 八阶段入库机制已完成，并通过 schema、event/artifact 引用、逐版本 evidence filter 和浏览器布局验收。
- Stage C：V0-V5 七阶段与十项 control evolution 已完成，并通过 schema、事件、artifact 和逐版本浏览器验收。
- Stage D：六版时间线已完成；默认 87 个里程碑，全部模式对账 324 条输入，节点可跳回完整交互。

## Stage A 验收结果

保留的设计：

- Query timeline 使用真实 timestamp；事件列表仍可使用版本语义阶段排序。
- 默认显示关键节点，允许切换全部输入；节点点击可跳转到完整 user input。
- Module flow 同时表示正向生产和 feedback/rework。
- Evidence Trail 明确显示 specified、executed、observed_failure、retrospective 和 contradicted。

Demo 发现并修正的问题：

- `fusion_candidates.py` 只负责候选发现，不能把 163 对的汇总写成脚本完成语义裁决；状态降级为 partial。
- 所谓 sequential per-card governance 缺少逐卡轨迹；当前可证明的是 bulk link、reported orphan pass 和 backward backlink repair。
- 848 条 citation 的机械覆盖与语义 JUDGE 覆盖不是同一分母；来源忠实性控制降级为 partial。
- `ingest.py` 只是 status flip、copy 和 first-source index，不是内容质量门。
- 图健康存在 0/2 orphan、1813/1815 edges 等 snapshot 冲突，不能显示无条件单值。
- V5 最重要的 missing controls 是 pipeline conformance 与 knowledge-depth；页面将其显示为 missed，而不是藏在 known gaps。

Stage A 判定：**通过，可以扩大到一个完整专题；数据状态仍保持 demo，直到 v0-v5 入库演化完成。**

## Stage B 验收结果

覆盖范围：`source-route`、`questioning-extraction`、`reframe-drafts`、`scripted-ingest`、`fusion-decision`、`graph-governance`、`publish-kb`、`failure-feedback`，每个节点均有 V0-V5 evolution。

全量扩展后保留的关键分歧：

- V0 前史 acquisition 与 V0 node production 分层，不能画成一个 adoption 动作。
- V1 是错误的 top-down 目标被完整执行，不是“没有流程”。
- V2 的 15 张产物早于 scoped-card / Top-3 最终合同，不能用最终设计反推旧卡。
- V3 的 171 份 comparison 实际只对 V2 语料，V3 self-dedup 与 merge 没有执行。
- V4 seed、full batch、post-publication repair 是三种 runtime shape；最终 328-card snapshot 不代表原始 pipeline。
- V5 deterministic ingest、YAML 与 graph audit 只能证明结构终态，不能补回缺失 knowledge。

验收动作：

- 完整模块触发 validator 对 6/6 版本和每个 stage evolution 的强制覆盖检查。
- 所有 evidence event、evolution event 和 artifact path 均通过引用校验。
- 浏览器分别切换 V0、V2、V3、V4、V5，确认 Evidence Trail 跟随版本过滤。
- 页头由静态 `v5 demo` 改为动态 `v0→v5 coverage`。

Stage B 判定：**通过。入库模块状态升级为 complete；下一阶段不得复用静态 control 状态，必须完成 control-level evolution。**

## Stage C 验收结果

- 七个稳定阶段全部覆盖 V0-V5；`mechanical-filter` 在 V2 标为 absent、V3 标为 retrospective，未把 FSJS 倒写回早期版本。
- 十项 controls 加入独立 evolution，validator 强制完整模块具有 6/6 control coverage。
- V4 明确保留 280-card FSJS 与 328-card 累积终态的分母差异；V5 保留 848 citation coverage 与语义 JUDGE 明细不足的差异。
- 页面切换 V0、V2、V3、V4、V5 时，stage evidence 与 control status 均来自对应版本；历史 coverage 不复用 V5 静态标签。
- `pipeline-conformance` 与 `knowledge-depth` 在各版按实际证据显示 failed、modified 或 retrospective，不因文件存在自动通过。

Stage C 判定：**通过。审计模块状态升级为 complete。**

## Stage D 验收结果

| 版本 | 默认里程碑 | 全部输入 |
|---|---:|---:|
| V0 | 11 | 22 |
| V1 | 14 | 28 |
| V2 | 12 | 80 |
| V3 | 16 | 157 |
| V4 | 20 | 69 |
| V5 | 14 | 22 |

- 六版均按 `source_recorded_at` 排序，默认节点只做 annotation，不复制或删减 user verbatim。
- causal edges 只连接有文本或执行证据支持的方向；未连边不等于无关系。
- V3 的 questioning future design 位于原 171-card execution 之后；V4 的 328 snapshot 分解为 seed、full batch、governance、repo demo 与 webpage remediation。
- 页面逐版切换 `关键节点 / 全部输入`，分母均与 events JSONL 对账；V0 与 V5 节点跳转回完整交互通过。

Stage D 判定：**通过。query timeline 状态升级为 complete。**

## Stage E：最终 QA

数据与隐私：

- `validate_archive.py`：324 events、324 unique ids、324 privacy-reviewed、41 redacted、6 versions、2 complete modules、6 annotated timelines。
- JSON、JSONL 与内嵌 JavaScript 语法通过；module/timeline 的 event 与 artifact 引用全部存在。
- publishable 目录未发现本机用户绝对路径、邮箱或常见 token pattern；唯一主机路径模式命中是 validator 自身的拦截正则。
- `registry/local-source-locators.json` 继续由本目录 `.gitignore` 排除，raw transcript 保持 local-only。

浏览器：

- 六版 `关键节点 / 全部输入` 分母逐项对账；V0 与 V5 节点跳转到完整事件通过。
- 入库模块 8 stages、审计模块 7 stages / 10 controls 在 V0、V2、V3、V4、V5 间切换均显示对应 evidence/evolution。
- 静态数据请求改为 `cache: no-store`，避免更新 JSON 后页面继续显示旧 timeline/module 状态。
- 桌面 1280×720 与移动 390×844 预览通过；时间线和机制 flow 在窄屏采用可滚动节点轨道，标题、按钮、卡片与侧栏无重叠。
- 页面运行日志为空，无浏览器 console/runtime error。

Stage E 判定：**通过。archive revision 升级为 r6；当前产物可作为 Git 发布前的完整 recall capsule。**
