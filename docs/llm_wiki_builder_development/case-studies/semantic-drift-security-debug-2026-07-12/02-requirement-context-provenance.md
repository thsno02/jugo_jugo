# 02. 需求与上下文溯源

## 2.1 结论先行

`full_corpus.py` 的敏感扫描职能不是单一来源的需求。它经历了四层转换：

```text
既有 archive publication privacy invariant
  -> Planner 将其推广为 plugin Definition of Done
  -> 父代理把它写成 E6 的明确 executor contract
  -> E6 选择具体 regex、状态映射和单文件实现
```

因此，“它是 implicit 还是 explicit”必须说明观察层级：

- 对人类原始任务：**implicit / 未指定**。
- 对仓库既有公开档案规则：**privacy gate explicit，但作用域较窄**。
- 对 Planner 和 Completion Contract：**agent-derived explicit**。
- 对 E6 worker：**fully explicit**。
- 对具体 regex、`sensitivity_decisions` 和自动 `withheld`：**implementation implicit**。

## 2.2 第一层：仓库既有隐私不变量

plugin 开发之前，interaction archive 已经规定：

- 原始 Codex/Claude session 永远 local-only；
- 公开事件使用语义化 alias；
- 未通过隐私复核的事件不能进入公开 HTML；
- machine scan 与 human review 是两个独立门；
- 敏感字面量使用明确占位符；
- 绝对路径、私人会话链接和可关联身份信息不进入公开产物。

直接证据位于：

- `docs/claude_interaction_replay/README.md:65-75`
- `docs/claude_interaction_replay/README.md:94-101`
- `docs/claude_interaction_replay/archive.json:508-517`
- `docs/claude_interaction_replay/content/privacy-audit.md:14-32`
- `docs/claude_interaction_replay/tools/validate_archive.py:19-29,163-176`

这里的原始边界是 **processed public events**。旧 validator 只扫描准备公开的 visible event text；被标记 `withheld` 的事件不走同一失败条件。它不是对全部 repository corpus 的通用 DLP 扫描。

## 2.3 第二层：人类目标保持开放

人类在 `S-PARENT` 中提出的显式目标只有：

1. 把完整 LLM Wiki 开发链路做成 plugin；
2. 在仓库 `plugins/` 下开发；
3. 使用逐模块、逐阶段 loops；
4. 使用 Planner-Executor-Reviewer；
5. 调用 sub-agents 并行开发。

对应证据为 [E-HUMAN-001](07-evidence-index.md#e-human-001)、[E-HUMAN-002](07-evidence-index.md#e-human-002) 和 [E-HUMAN-003](07-evidence-index.md#e-human-003)。这些消息没有出现：

- `full_corpus.py`
- secret/PII regex
- `consumed/failed/withheld`
- `sensitivity_decisions`
- 对 archive 全材料重新扫描

所以，安全扫描不是人类逐字给出的 closed ticket，而是开放目标下由 agent 规划层补出的完成条件。

## 2.4 第三层：Planner 的策略升格

父代理要求 Planner 阅读当前 plugin 与 v0-v5 事实源，自行输出 Definition of Done、缺失矩阵、loop 验收和 deterministic/semantic boundary。[E-PLAN-001](07-evidence-index.md#e-plan-001)

Planner 随后提出：

- schema、引用、图、隐私、密钥、路径泄漏是确定性阻断门；
- v0-v5 full corpus 的所有来源必须有 disposition；
- 冲突不能静默丢失；
- parallel extraction 后才能 serial fusion；
- 不得存在未审敏感项；
- 敏感扫描属于 deterministic script，价值判断属于 Agent Skill。

见 [E-PLAN-002](07-evidence-index.md#e-plan-002)。这是本案例的第一个关键设计判断：Planner 把一个原本位于 publication boundary 的 privacy rule，提升为 plugin completion boundary。

该判断有合理基础：full plugin 会读取并重放历史人类输入、构建 Recall 和 publication artifacts；如果不把隐私门带入新链路，既有 archive 的公开边界会在 plugin 化后发生回归。但 Planner 没有单独论证：检查应位于 ingestion、readiness、semantic extraction 还是 publication。

## 2.5 第四层：父代理冻结 Completion Contract

父代理将 Planner 输出写入 `plugins/llm-wiki-builder/development/COMPLETION_CONTRACT.md`：

- 语义判断进入结构化 ledger；脚本只发现、验证和安全应用；
- secret、PII、路径泄漏是确定性阻断门；
- v0-v5 全量材料都有 `consumed/failed/withheld`；
- loop-050 必须完成全来源状态、并行 extraction、串行 fusion 和隐私清零。

见 [E-CONTRACT-001](07-evidence-index.md#e-contract-001) 和当前文件 `COMPLETION_CONTRACT.md:11-16,28`。

到这一步，原先的 Planner 推导已经成为后续 Executor 必须遵守的显式合同。需要注意：这是 **agent-authored contract**，不能因为后来写入 Markdown 就追认为人类原始需求。

## 2.6 第五层：E6 派发把扫描明确放进 full_corpus

父代理为 E6B 指定了唯一写集合：

```text
plugins/llm-wiki-builder/scripts/integration/full_corpus.py
plugins/llm-wiki-builder/development/loops/loop-050-v0-v5-full-corpus/**
```

并明确要求：

- 覆盖 version registry、v0-v5 capsules、archive 及全部声明 shards、sources manifest；
- 稳定 repo-relative locator + SHA256；
- 每项 `consumed/failed/withheld` 且有 reason；
- 并行 JSON/JSONL parse；
- 文本 secret/PII/绝对路径扫描；
- cross-reference existence；
- 结果确定性和冲突保留；
- 语义部分只生成 structured work ledger。

见 [E-DISPATCH-E6](07-evidence-index.md#e-dispatch-e6)。所以，从 E6 的局部上下文看，敏感扫描不是“自行加戏”，而是 explicit executor requirement。

同时，E6 不得修改 module scripts、shared runtime 和 contracts。因为唯一可写的 integration script 就是 `full_corpus.py`，多个职能被集中到该文件并非偶然：这是任务拆分和文件 ownership 共同塑造的结构。

## 2.7 第六层：E6 读取旧机制并作实现扩张

补丁前，E6 读取了 archive manifest/schema、`validate_archive.py`、publication runtime、v0-v5 capsules 和 module loops。[E-E6-READ-ARCHIVE](07-evidence-index.md#e-e6-read-archive)

旧 `validate_archive.py` 只有四类 pattern：绝对用户路径、私人会话 URL、邮箱、generic secret-like 键值。E6 随后公开声明：敏感命中只记录类别和行定位，不复制原文、不输出绝对路径。[E-E6-DESIGN](07-evidence-index.md#e-e6-design)

E6 最终在 `full_corpus.py:22-33` 扩展出：

- private key header
- AWS key ID
- GitHub token
- OpenAI token
- email / US SSN / CN ID / phone
- POSIX / Windows absolute path

这些具体供应商格式、国家 PII 类型和长度阈值没有出现在 Planner 或 E6 prompt 中，属于 E6 的实现选择。代码将任何 pattern hit 自动映射为 `withheld`，同样是实现层政策决定。

## 2.8 职能来源矩阵

| `full_corpus.py` 职能 | 人类 | Planner/合同 | E6 prompt | 实现选择 | 最终定性 |
|---|---|---|---|---|---|
| v0-v5/source/archive 覆盖 | 未指定细节 | explicit | explicit | 文件枚举方式 implicit | agent-derived explicit |
| repo-relative locator + SHA256 | 未指定 | deterministic boundary 支持 | explicit | canonical 形式 implicit | explicit to E6 |
| `consumed/failed/withheld` | 未指定 | explicit | explicit | precedence implicit | explicit to E6 |
| JSON/JSONL parse | 未指定 | deterministic script | explicit | parser 细节 implicit | explicit to E6 |
| secret/PII/path scan | 未指定 | explicit gate | explicit | exact regex implicit | mixed |
| parallel scan + determinism | 只要求并行 agents | loop-050 explicit | explicit | ThreadPool 实现 implicit | agent-derived explicit |
| readiness/semantic 分离 | 未指定 | explicit principle | explicit | 三文件输出 implicit | agent-derived explicit |
| structured semantic ledger | 未指定 | explicit | explicit | schema/字段 implicit | mixed |
| `sensitivity_decisions` | 未指定 | 未命名 | 未命名 | E6 首创 | implicit implementation |

## 2.9 边界判断

这条链路不存在单一“违规插入点”。更准确的描述是：

1. **合理继承**：既有 archive privacy invariant 必须在 plugin 化后得到保留。
2. **未充分论证的升格**：Planner 把 publication rule 推广为 full-corpus completion gate。
3. **明确派发**：父代理要求 E6 对 full corpus 运行文本扫描。
4. **实现扩张**：E6 选择通用 credential/PII patterns 和自动 `withheld`。
5. **职责耦合**：同一 runner 又产生 semantic work ledger，为后续解释漂移创造条件。

因此，需求本身不是恶意或隐藏注入；问题是不同抽象层的合理要求在压缩与实现过程中失去了原始适用边界。
