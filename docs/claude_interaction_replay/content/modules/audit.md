# 审计机制（Audit Mechanism）

## Recall 目标

这个专题还原审计 finding 怎样产生、如何被误判、为什么被重新打开：从审计合同、机械检查、独立 reviewer 或风险分片、语义判断、综合 verdict，一直到用户 adversarial probe、root-cause audit 和 remediation。页面不把 `PASS` 当终点，而把它当一个带时间、分母和覆盖边界的历史判断。

## V0-V5 演化主线

| 版本 | 主要审计形态 | 能证明什么 | 没有发现什么 |
|---|---|---|---|
| V0 | 结构/citation/impact validators 与 completion audit | 7-node 文件机制可运行 | 生产对象错成 meta KB |
| V1 | 逐 topic-node 独立 audit、repair/re-audit、final QA | 局部 gate 能阻断缺陷 | top-down、不可读和错误产品目标 |
| V2 | fresh per-card audit worker | 单卡来源、scope、fact type 与可读性 | 15-card 卡集质量、吞吐和后期 fusion 合同 |
| V3 | batch publication gate + fusion audit | 163/163 与 8/8 对当时合同通过 | comparison 只读 V2，未做 V3 self-dedup |
| V4 | seed reviewer、post-hoc governance、280-card FSJS | 机械全量、source-affinity JUDGE 和 scoped verdict | 43-source prompt conformance、328-card 终验和知识深度 hard gate |
| V5 | 脚本化 mechanical audit + FSJS + 用户质量 probe | 多类结构、引用和图终态健康 | 完整 skills 未注入、card 知识为空壳 |

## 稳定审计闭环

```text
定义审计问题与通过条件
  → 机械全量初筛
  → 按风险分片与语义 JUDGE
  → 综合验收与冲突披露
  → 用户阅读与对抗式 Probe
  → 追溯生产合同是否执行
  → 修复实验与再审计
```

这些节点是跨版本坐标，不是历史伪装。V0 没有 suspect sharding，V2 没有独立 mechanical FILTER，V3 的完整 process audit 在 publication 后，V4 的 328 cards 也没有重跑 280-card 同级 FSJS。节点中的 Version Evolution（版本演化）明确标注 `absent`、`introduced`、`modified`、`failed` 或 `retrospective`。

## 十项稳定控制

- `source-eligibility`：agent 实际读取的 source surface 是否正确、充分、可追踪。
- `source-faithfulness`：claim 是否由 source evidence 支撑。
- `inference-boundary`：直接陈述、推断、hedge 与 source authority 是否保留。
- `schema-validity`：当前版本的结构、字段、section 和引用标识是否合法。
- `fusion-boundary`：duplicate、merge、provenance delta 与 distinct-link 是否有语义依据。
- `graph-integrity`：citation、related、impact、dangling、orphan 和方向性是否可复算。
- `cross-source-leakage`：其他来源或其他卡的知识是否未经 provenance 进入正文。
- `state-consistency`：task、state、queue、artifacts、indexes、metrics 与 Git 是否一致。
- `pipeline-conformance`：实际 agent 是否遵守目标、语料、prompt、角色、顺序和 exit gate。
- `knowledge-depth`：知识对象是否自包含地解释机制、边界、因果、反例与 tradeoff。

## 跨版本结论

- 机械结果只能确定结构事实或产生 suspects，不能自动做语义 verdict。
- 局部 `adopt_recommended`、全量 workflow success 和产品 acceptance 是三种不同结论。
- 覆盖必须带分母：`full card-set` 不等于 `full claims`，`sample` 也不能被 synthesis 扩写成全量。
- 修复后的终态不能证明原 pipeline 当时合规；时间方向、对象集合和执行证据都不可逆。
- 设计文档和 skills 文件存在不等于执行节点收到它们。
- 用户 probe 是正式 control discovery 机制，不是审计外的偶然反馈。

## 证据状态

本模块已覆盖 V0-V5 七阶段和十项 control evolution。V5 的 `6/6 PASS`、V4 的 `5 PASS / 3 PARTIAL`、V3 的 `171 accepted`、V1 的 `v1_delivered` 和 V0 的 completion pass 都作为当时 verdict 保留，同时并列展示后续反证；任何一个都不会被升级为无条件的产品成功。
