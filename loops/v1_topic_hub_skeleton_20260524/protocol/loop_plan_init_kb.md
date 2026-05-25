# KB Initialization RPD

## 0. Project Position

当前项目阶段是 **KB initialization**。

已有 web data / raw data。当前目标不是继续无限采集资料，也不是构建一个最终完美百科，而是把已有 data 和必要的新检索资料，沉淀成一套 agent 可维护、可追溯、可演进的 knowledge base。

本项目的上层 research objective 来自 LLM Wiki coverage framework：LLM Wiki 应该是 persistent、source-backed、inspectable、interlinked、auditable、maintainable 的知识系统；重要内容最终需要能回到 raw sources、source records、claim/source rationale、revision history 和 update model。

---

# 1. Core Objective

构建一个 agent-maintained KB initialization loop。

这个 loop 的目标是：

```text
已有 data / raw knowledge
→ agent 生成 0-1 node
→ 记录 provenance
→ 审计 citation 和可信度
→ 采纳版本进入 kb view
→ 根据 major change 触发影响分析
→ 通过每次 0-1 run 评估和迭代 skills
```

当前 demo 的核心验证点：

1. Agent 是否能从已有 data 生成一个可信 node。
2. 每个 node 是否有完整 version bundle。
3. Provenance 是否能解释为什么这个 card 存在、为什么可信、为什么被采纳。
4. Citation 是否能驱动后处理 graph / impact queue。
5. Major/minor version 是否能控制后续演进。
6. Skill 是否能通过每次 0-1 生成被评估和改进。
7. 动态检索是否能在 evidence 不足时被纳入，而不是随意搜索。

---

# 2. Non-Goals

当前 demo 不做这些事情：

```text
1. 不构建严格 ontology。
2. 不强制 card 类型分类。
3. 不强制 abstraction level。
4. 不维护手写 graph。
5. 不依赖 Git 作为 card 历史阅读系统。
6. 不要求所有 card atomic。
7. 不要求一次性完成所有概念 deep research。
8. 不要求 kb/ 人类友好。
9. 不把最新 candidate version 自动采纳为 present version。
10. 不把 agent synthesis 当作 ground truth。
```

当前 demo 只要求：

```text
简约
粗糙
可管理
可追溯
可审计
可演进
```

---

# 3. Final File Architecture

推荐当前 demo 使用：

```text
.
├── data/
│   ├── raw/
│   ├── manifests/
│   ├── discovery/
│   └── logs/
│
├── nodes/
│   ├── 20260522_143012_source_preservation_precondition_trust/
│   │   ├── node.yaml
│   │   ├── versions/
│   │   │   ├── 1.0/
│   │   │   │   ├── node.yaml
│   │   │   │   ├── card.md
│   │   │   │   ├── provenance.md
│   │   │   │   └── change.md
│   │   │   ├── 1.1/
│   │   │   │   ├── node.yaml
│   │   │   │   ├── card.md
│   │   │   │   ├── provenance.md
│   │   │   │   └── change.md
│   │   │   └── 2.0/
│   │   │       ├── node.yaml
│   │   │       ├── card.md
│   │   │       ├── provenance.md
│   │   │       └── change.md
│   │   └── attachments/
│   │
│   └── 20260522_151044_llm_wiki_working_definition/
│       └── ...
│
├── kb/
│   ├── _schema.yaml
│   ├── _index.yaml
│   ├── 20260522_143012_source_preservation_precondition_trust.md
│   ├── 20260522_151044_llm_wiki_working_definition.md
│   └── _changes/
│
├── generated/
│   ├── citation_graph.yaml
│   ├── backlinks.yaml
│   ├── impact_queue.yaml
│   ├── status.yaml
│   └── html/
│
├── .llmwiki/
│   ├── control/
│   ├── agents/
│   ├── runs/
│   └── skills/
│
└── scripts/
    ├── kb_build_index.py
    ├── kb_build_view.py
    ├── kb_validate_node.py
    ├── kb_validate_card.py
    ├── kb_parse_citations.py
    ├── kb_compute_impact.py
    ├── kb_status.py
    └── kb_git_checkpoint.sh
```

---

# 4. Folder Semantics

## 4.1 `nodes/`

`nodes/` 是真实 node database。

规则：

```text
1. nodes/ 是平的。
2. nodes/ 不按类型、层级、主题分类。
3. 一个 folder 是一个 node/card 的完整维护范围。
4. folder name = timestamp + semantic slug。
5. 不使用 zk_ prefix。
6. folder name 不表达类型、状态、层级。
7. title 可以变，folder id 不变。
```

示例：

```text
20260522_143012_source_preservation_precondition_trust
20260522_151044_llm_wiki_working_definition
20260522_160310_structured_markdown_artifact_policy
```

## 4.2 `kb/`

`kb/` 是主要消费 view。

它不必人类友好。它只是当前可被 agent 检索、引用、消费的 adopted-card view。

规则：

```text
1. kb/ 只渲染 adopted version。
2. kb/ 不作为维护层。
3. kb/ 文件可以被 agent 直接消费。
4. 维护发生在 nodes/。
5. kb/_index.yaml 是 agent 的入口契约。
```

## 4.3 `generated/`

`generated/` 是后处理结果。

```text
citation_graph.yaml
backlinks.yaml
impact_queue.yaml
status.yaml
html/
```

这些都不是 source of truth，可以删除重建。

## 4.4 `.llmwiki/`

`.llmwiki/` 是 agent control layer。

```text
control/  当前规则、队列、状态
agents/   agent task files
runs/     每次 run 的过程 artifacts
skills/   skill definitions and versions
```

---

# 5. Node Version Bundle Contract

一个 version bundle 由四个文件组成：

```text
versions/<version>/
  node.yaml
  card.md
  provenance.md
  change.md
```

含义：

| 文件              | 作用                                             |
| --------------- | ---------------------------------------------- |
| `node.yaml`     | 该版本 metadata。只做 metadata/config，不做正文，不做 graph。 |
| `card.md`       | 该版本完整知识内容，包含正文、footnotes、references。           |
| `provenance.md` | 该版本为什么存在、如何生产、为什么可信、如何被审计。                     |
| `change.md`     | 该版本相对于上一版本的变化说明。                               |

根目录的：

```text
nodes/<node_id>/node.yaml
```

是当前 adopted version 的 `node.yaml` presentation。

也就是说：

```text
nodes/<node_id>/node.yaml
= versions/<adopted_version>/node.yaml
```

如果 latest version 是 candidate，但没有被采纳，根目录 `node.yaml` 仍然指向 adopted version。

---

# 6. Metadata Contract

## 6.1 `node.yaml`

`node.yaml` 只做已有信息的 metadata presentation。

不写：

```text
summary
dependencies
supports
depends_on
incoming
outgoing
manual graph
```

推荐 schema：

```yaml
schema: kb.node_metadata.v1

id: 20260522_143012_source_preservation_precondition_trust
title: "Source preservation is a precondition for LLM Wiki trust"

version: "1.1"
version_status: adopted

node_created_at: "2026-05-22T14:30:12-07:00"
node_archived_at: null

version_created_at: "2026-05-22T15:00:00-07:00"
version_adopted_at: "2026-05-22T15:20:00-07:00"
version_superseded_at: null
version_archived_at: null

status: active
stability: solid
usable_as_support: true

paths:
  version_dir: "versions/1.1/"
  card: "versions/1.1/card.md"
  provenance: "versions/1.1/provenance.md"
  change: "versions/1.1/change.md"
  kb_view: "kb/20260522_143012_source_preservation_precondition_trust.md"

tags:
  - llm-wiki
  - provenance
  - source-preservation

audit:
  state: passed
  run: ".llmwiki/runs/run_20260522_143012/audit_report.md"
```

## 6.2 Time Fields

需要区分 node 和 version：

```text
node_created_at
node_archived_at

version_created_at
version_adopted_at
version_superseded_at
version_archived_at
```

含义：

| 字段                      | 含义                        |
| ----------------------- | ------------------------- |
| `node_created_at`       | 这个 node 第一次创建时间           |
| `node_archived_at`      | 整个 node 退出 active KB 的时间  |
| `version_created_at`    | 这个版本生成时间                  |
| `version_adopted_at`    | 这个版本进入 kb view 的时间        |
| `version_superseded_at` | 这个版本被新 adopted version 替代 |
| `version_archived_at`   | 这个版本被封存，不再作为候选或维护对象       |

---

# 7. Card Markdown Schema

`card.md` 不使用固定写作 template。

不强制：

```text
Core idea
Explanation
Limits
Open questions
```

但是必须有若干 schema sections。

最低要求：

```text
# Title

自由正文

## Footnotes

## References
```

建议由 renderer 或 validator 支持：

```text
## Tags
```

但 tags 的 source of truth 是 `node.yaml`。

## 7.1 Footnotes

Footnotes 支持正文中的具体 claim。

正文：

```markdown
Source preservation is a necessary precondition for trustworthy LLM Wiki synthesis because later agents must be able to inspect the material behind synthesized claims.[^1]
```

Footnote：

```markdown
## Footnotes

[^1]:
    target: ../../kb/20260522_150012_karpathy_llm_wiki_source_observation.md
    target_version: 1.0
    pinned_version: ../../nodes/20260522_150012_karpathy_llm_wiki_source_observation/versions/1.0/card.md
    citation_role: claim_support
    why_cited: Supports the claim that preserved source material is required for later audit.
    evidence_summary: The cited card records a source-backed observation from preserved source material.
    source_path: ../../data/raw/src_000001/
```

每个 footnote 必须包含：

```text
target
target_version
pinned_version
citation_role
why_cited
evidence_summary
```

## 7.2 References

References 支持整张 card 的背景、definition、idea、source scope。

```markdown
## References

### [R1] Working definition of LLM Wiki

target: ../../kb/20260522_151044_llm_wiki_working_definition.md
target_version: 2.0
pinned_version: ../../nodes/20260522_151044_llm_wiki_working_definition/versions/2.0/card.md
citation_role: background_definition
why_cited: This card uses the KB working definition of LLM Wiki as background.
evidence_summary: The cited card explains the current operational definition and its boundaries.
```

每个 reference 必须包含：

```text
target
target_version
pinned_version
citation_role
why_cited
evidence_summary
```

## 7.3 Citation Propagation

Citation 是方向。

```text
A cites B
=> A depends on B
=> B major update
=> A enters impact review
```

传播强度：

| Citation 类型 | 传播强度                             |
| ----------- | -------------------------------- |
| footnote    | strong                           |
| reference   | medium                           |
| plain link  | weak / no propagation by default |

不需要维护：

```text
depends_on
supports
uses_definition
```

这些由 citation 后处理推导。

---

# 8. Provenance Contract

`provenance.md` 是核心资产，不是附属说明。

它需要回答：

```text
1. 这个版本为什么存在？
2. 它用了哪些输入？
3. 哪些是已有 data？
4. 哪些是动态检索新增资料？
5. 哪些是 agent synthesis？
6. 为什么这个 synthesis 被允许？
7. 它被怎样 audit？
8. 它为什么能被采纳？
9. 它不能证明什么？
10. 什么情况会要求修订？
```

推荐 schema：

```markdown
# Provenance

node_id:: 20260522_143012_source_preservation_precondition_trust
version:: 1.1

## Why this version exists

...

## Inputs used

### Existing data

- ...

### Dynamic retrieval, if any

- ...

### Prior KB nodes

- ...

### Process artifacts

- `.llmwiki/runs/...`

## Production rationale

...

## Citation rationale

...

## Synthesis decisions

...

## Audit trail

audit_result:: passed
audit_report:: .llmwiki/runs/run_.../audit_report.md

## Adoption rationale

...

## Limits and uncertainty

...

## Revision triggers

...
```

Rule：

```text
card.md 是结果。
provenance.md 是为什么这个结果值得被暂时相信。
```

---

# 9. Change Contract

`change.md` 放在当前版本目录里。

```text
versions/1.0/change.md  # genesis
versions/1.1/change.md  # 1.0 -> 1.1
versions/2.0/change.md  # 1.1 -> 2.0
```

推荐 schema：

```markdown
# Change: 1.1 → 2.0

node_id:: 20260522_143012_source_preservation_precondition_trust
from_version:: 1.1
to_version:: 2.0
change_scale:: major
propagation_required:: true
created_at:: 2026-05-22T18:44:22-07:00
run_id:: .llmwiki/runs/run_20260522_184422/

## Why this changed

...

## Old meaning

...

## New meaning

...

## Semantic delta

...

## Why this is major

...

## Expected impact

...
```

Major `change.md` 是演进系统的核心输入。

---

# 10. Version Semantics

Version 使用：

```text
major.minor
```

## 10.1 Minor Version

例：

```text
1.0 → 1.1
```

含义：

```text
主体仍然成立。
fact holds。
core meaning 没变。
support contract 没变。
不触发 impact propagation。
```

典型 minor：

```text
补 citation
修 typo
补 provenance
补 footnote
补 reference
局部措辞优化
补 raw path
补 uncertainty 说明但不改变核心意思
```

## 10.2 Major Version

例：

```text
1.1 → 2.0
```

含义：

```text
主体意义变了。
fact 不再以旧形式 holds。
support contract 变了。
definition scope 变了。
下游引用必须 review。
```

典型 major：

```text
core claim 改变
source 不支持原 claim
working definition 改变
confidence 实质性降级
node 不再 usable_as_support
当前事实被 supersede
```

Major 版本可以先是 candidate，不必立刻 adopted。

---

# 11. Adoption Logic

每个 node 可以同时存在：

```text
adopted version
latest candidate version
old superseded versions
archived versions
```

规则：

```text
1. kb/ 只渲染 adopted version。
2. latest candidate 不自动进入 kb/。
3. major candidate 必须完成 impact review 才能 adopted。
4. adopted version 由根目录 node.yaml 表示。
```

Adoption 步骤：

```text
1. 创建 versions/2.0/
2. 写 versions/2.0/node.yaml, card.md, provenance.md, change.md
3. version_status = candidate
4. 如果 major，运行 impact analysis
5. downstream review 完成后
6. 更新 versions/2.0/node.yaml -> adopted
7. 更新旧 adopted version -> superseded
8. 复制 versions/2.0/node.yaml 到根目录 node.yaml
9. 重新生成 kb/ 和 kb/_index.yaml
```

---

# 12. Generated Artifacts

这些不是 source of truth。

```text
generated/citation_graph.yaml
generated/backlinks.yaml
generated/impact_queue.yaml
generated/status.yaml
generated/html/
```

## 12.1 Citation Graph

由 `kb/*.md` 的 footnotes 和 references 生成。

```yaml
schema: kb.citation_graph.v1
generated_at: "2026-05-22T00:00:00-07:00"

edges:
  - citing_node: 20260522_143012_source_preservation_precondition_trust
    citing_version: "1.1"
    citation_kind: footnote
    citation_id: "1"
    cited_node: 20260522_150012_karpathy_llm_wiki_source_observation
    cited_version: "1.0"
    pinned_version: "../../nodes/20260522_150012_karpathy_llm_wiki_source_observation/versions/1.0/card.md"
    propagation_strength: strong
```

## 12.2 Impact Queue

由 major change + citation graph 生成。

```yaml
schema: kb.impact_queue.v1
generated_from_change: 1.1_to_2.0
generated_at: "2026-05-22T00:00:00-07:00"

impacts:
  - impact_id: imp_001
    changed_node: 20260522_143012_source_preservation_precondition_trust
    changed_from_version: "1.1"
    changed_to_version: "2.0"
    impacted_node: 20260522_162530_claim_level_provenance_makes_agent_reuse_auditable
    citation_kind: footnote
    impact_level: high
    status: open
    suggested_action: review_and_revise
    reason: "Impacted node cites the changed node for a claim-level support relation."
```

Propagation 不自动重写下游 nodes。它只生成 impact queue。

---

# 13. Agent Hierarchy

当前使用：

```text
GPT-5.5
Codex
Codex sub-agents
sub-sub-agents
```

建议分层：

```text
L0 Outer Controller
L1 Run Orchestrator
L2 Specialist Agents
L3 Micro Sub-Agents
```

## 13.1 L0 Outer Controller

建议使用 GPT-5.5。

职责：

```text
1. 选择当前 loop。
2. 判断 demo 进度。
3. 读取 kb/_index.yaml、generated/status.yaml、.llmwiki/control/state.md。
4. 决定下一次 run 的目标。
5. 不直接写 card，除非需要高层审查。
```

输出：

```text
.llmwiki/runs/<run_id>/run_plan.md
.llmwiki/control/action_queue.yaml
```

## 13.2 L1 Run Orchestrator

建议使用 Codex。

职责：

```text
1. 创建 run folder。
2. 调用 sub-agents。
3. 执行 scripts。
4. 写入 nodes/。
5. 生成 kb/。
6. 生成 generated/。
7. 做 git checkpoint。
```

## 13.3 L2 Specialist Agents

| Agent                | 职责                                        |
| -------------------- | ----------------------------------------- |
| Skill Architect      | 创建和更新 skills                              |
| Data Profiler        | 盘点已有 data                                 |
| Retriever            | 动态检索新增资料                                  |
| Source Materializer  | 把 raw source 变成可用 source fact/source node |
| Node Planner         | 选择当前 0-1 node                             |
| Card Generator       | 写 card.md                                 |
| Provenance Generator | 写 provenance.md                           |
| Change Writer        | 写 change.md                               |
| Citation Auditor     | 检查 footnotes/references                   |
| Adoption Auditor     | 判断 version 是否可以 adopted                   |
| Impact Analyzer      | major change 后生成 impact queue             |
| Skill Evaluator      | 评估本 run 暴露出的 skill failure                |
| View Builder         | 生成 kb view 和 indexes                      |

## 13.4 L3 Micro Sub-Agents

每个 L2 agent 可以再开 micro sub-agent。

例如 Card Generator 可以开：

```text
Evidence Reader
Draft Writer
Citation Inserter
Markdown Normalizer
```

Provenance Generator 可以开：

```text
Input Trace Extractor
Synthesis Rationale Writer
Audit Trail Writer
Revision Trigger Writer
```

Citation Auditor 可以开：

```text
Footnote Parser
Reference Parser
Pinned Version Checker
Why-Cited Checker
Evidence Summary Checker
```

---

# 14. Core Loops

## Loop A: System Bootstrap Loop

目的：

```text
创建初始化 demo 所需的文件契约、schema、scripts、skills。
```

输入：

```text
reports/coverage_framework.md
当前设计规则
已有 repo 结构
```

输出：

```text
kb/_schema.yaml
.llmwiki/control/principles.md
.llmwiki/control/state.md
.llmwiki/skills/*
scripts/kb_*.py
```

完成条件：

```text
1. nodes/ version bundle contract 已写入 schema。
2. card.md required sections 已定义。
3. citation syntax 已定义。
4. provenance.md schema 已定义。
5. change.md schema 已定义。
6. kb_build_index.py 和 kb_build_view.py 至少可运行。
```

---

## Loop B: Data Inventory Loop

目的：

```text
盘点已有 data，判断哪些 raw data 可以支撑第一批 0-1 nodes。
```

输入：

```text
data/raw/
data/manifests/
reports/source_gap_review.md
```

输出：

```text
.llmwiki/control/data_inventory.yaml
.llmwiki/control/source_candidates.yaml
```

Agent：

```text
Data Profiler
Source Materializer
Citation Auditor
```

完成条件：

```text
1. 每个可用 source 有 source_id。
2. 每个 source 有 raw path。
3. 可被用于 node generation 的 source 被列入 source_candidates.yaml。
4. 不足的 source 被列为 evidence gap 或 retrieval request。
```

---

## Loop C: 0-1 Node Build Loop

目的：

```text
每次从 0 到 1 创建一个 node，以便评估技能和生成质量。
```

这是初始化阶段的核心 loop。

输入：

```text
.llmwiki/control/source_candidates.yaml
kb/_index.yaml
已有 nodes/
相关 data/raw/
```

输出：

```text
nodes/<new_node_id>/versions/1.0/node.yaml
nodes/<new_node_id>/versions/1.0/card.md
nodes/<new_node_id>/versions/1.0/provenance.md
nodes/<new_node_id>/versions/1.0/change.md
nodes/<new_node_id>/node.yaml
kb/<new_node_id>.md
```

流程：

```text
1. Node Planner 选择一个候选 node。
2. Run Orchestrator 创建 run folder。
3. Card Generator 写 versions/1.0/card.md。
4. Provenance Generator 写 versions/1.0/provenance.md。
5. Change Writer 写 versions/1.0/change.md，genesis change。
6. 写 versions/1.0/node.yaml。
7. Audit 检查 card/provenance/citation。
8. 如果 pass，root node.yaml 指向 1.0。
9. View Builder 渲染 kb。
10. Skill Evaluator 评估本次生成。
```

完成条件：

```text
1. 版本 bundle 完整。
2. card.md 有 Footnotes 和 References sections。
3. provenance.md 能解释 why。
4. node.yaml metadata 可被 index script 读取。
5. kb view 生成。
6. audit pass。
```

---

## Loop D: Dynamic Retrieval Loop

目的：

```text
当现有 data 不足时，允许 agent 动态检索新信息，但必须沉淀进 data 和 provenance。
```

触发条件：

```text
1. Generator 认为 evidence 不足。
2. Audit 认为 citation 不支持 claim。
3. Node Planner 认为某 node 需要外部资料才能生成。
4. Skill Evaluator 发现当前技能缺少某类知识。
```

输入：

```text
retrieval_request.md
current evidence gap
目标 node / target claim
```

输出：

```text
data/raw/<new_source_id>/
data/manifests/sources.jsonl
.llmwiki/control/retrieval_log.yaml
source-backed node 或 source observation node
```

流程：

```text
1. 写 retrieval_request.md。
2. Retriever 执行 web search。
3. 选 source。
4. 保存 raw source。
5. 写 source manifest。
6. Source Materializer 生成 source-level support。
7. 回到 Node Build Loop。
```

规则：

```text
动态检索不是临时补脑。
动态检索必须变成 data asset。
```

---

## Loop E: Audit and Adoption Loop

目的：

```text
判断某个 version 是否可以 adopted，是否可以进入 kb view。
```

输入：

```text
versions/<version>/node.yaml
versions/<version>/card.md
versions/<version>/provenance.md
versions/<version>/change.md
```

输出：

```text
.llmwiki/runs/<run_id>/audit_report.md
root node.yaml updated, if adopted
kb view updated
```

检查项：

```text
1. node.yaml 是否合法。
2. card.md 是否有 Footnotes / References。
3. footnote 是否含 target_version / pinned_version / why_cited / evidence_summary。
4. provenance.md 是否解释输入、综合、审计、采纳理由。
5. change.md 是否解释版本变化。
6. card 是否把 synthesis 伪装成 ground truth。
7. 动态检索是否已经进入 data/raw。
```

Adoption rule：

```text
minor version audit pass 后可以直接 adopted。
major version 必须完成 impact review 后才能 adopted。
```

---

## Loop F: Major Change / Impact Loop

目的：

```text
处理 major version 对下游 nodes 的影响。
```

输入：

```text
major version change.md
generated/citation_graph.yaml
kb/_index.yaml
```

输出：

```text
generated/impact_queue.yaml
后续 revise runs
```

流程：

```text
1. 检测 major change。
2. 解析 change.md。
3. 构建 citation graph。
4. 找到 citing nodes。
5. 根据 footnote/reference 判断 impact level。
6. 写 impact_queue.yaml。
7. Controller 决定是否 revise impacted nodes。
8. 每个 impacted node 进入 Node Revision Loop。
```

规则：

```text
impact analysis 不自动改写下游。
它只创建任务。
```

---

## Loop G: Skill Evolution Loop

目的：

```text
通过每次 0-1 run 评估、优化、迭代 skills。
```

输入：

```text
run artifacts
audit_report.md
card.md
provenance.md
failure cases
```

输出：

```text
.llmwiki/skills/<skill>/skill.md
.llmwiki/skills/<skill>/versions/
.llmwiki/control/skill_eval_log.yaml
```

Skill categories：

```text
node_planning
card_generation
provenance_generation
citation_formatting
citation_audit
dynamic_retrieval
source_materialization
version_adoption
impact_analysis
view_generation
```

Skill evolution 规则：

```text
1. 不以“是否更好”为目标。
2. 以减少明确 failure mode 为目标。
3. 每次 run 最多升级少数核心 skill。
4. 如果只是 case-level observation，不升级 global skill。
5. skill 改动必须记录原因。
6. 每次 0-1 node 是一次 skill evaluation sample。
```

Skill lifecycle：

```text
seed
candidate
active
revised
deprecated
```

---

## Loop H: KB View and Index Loop

目的：

```text
从 adopted versions 构建 kb/ 和 indexes。
```

输入：

```text
nodes/*/node.yaml
nodes/*/versions/<adopted>/card.md
```

输出：

```text
kb/_index.yaml
kb/<node_id>.md
generated/citation_graph.yaml
generated/backlinks.yaml
generated/status.yaml
```

流程：

```text
1. 扫描 nodes/*/node.yaml。
2. 找 adopted version。
3. 渲染 adopted card 到 kb/。
4. 构建 kb/_index.yaml。
5. 解析 citations。
6. 构建 generated/citation_graph.yaml。
7. 更新 generated/status.yaml。
```

---

# 15. One Run Protocol

每次 run 的标准结构：

```text
.llmwiki/runs/run_YYYYMMDD_HHMMSS_<slug>/
  run_plan.md
  task.md
  data_scope.md
  generator_trace.md
  provenance_trace.md
  audit_report.md
  skill_eval.md
  git_trace.md
```

## Step 1: Plan

```text
Controller 决定本次是：
- new node 0-1
- dynamic retrieval
- skill creation
- skill revision
- major impact review
- node revision
```

## Step 2: Scope

```text
明确本次可用 data / source / existing nodes。
```

## Step 3: Generate

```text
生成 version bundle。
```

## Step 4: Audit

```text
检查 schema、citation、provenance、evidence sufficiency。
```

## Step 5: Adopt or Hold

```text
pass + minor/new 1.0 => adopted
major candidate => hold until impact review
fail => revise or evidence gap
```

## Step 6: Build View

```text
生成 kb/ 和 generated/。
```

## Step 7: Skill Eval

```text
记录哪个 skill 成功、失败、需要升级。
```

## Step 8: Git Checkpoint

Git 只做 repo checkpoint：

```text
git commit -m "run: initialize node <node_id>"
```

不要把 Git 当作主要 card version reader。

---

# 16. Skills Needed For Demo

## 16.1 Node Planning Skill

目标：

```text
选择下一个 0-1 node。
```

输入：

```text
data_inventory.yaml
kb/_index.yaml
existing nodes
source_candidates.yaml
```

输出：

```text
run_plan.md
```

判断标准：

```text
1. 是否有足够 evidence。
2. 是否是 useful node。
3. 是否能形成可信 version bundle。
4. 是否适合测试当前 skills。
```

---

## 16.2 Card Generation Skill

目标：

```text
生成 card.md。
```

要求：

```text
1. 不强制模板。
2. 必须有 Footnotes。
3. 必须有 References。
4. 具体 claim 用 footnote。
5. broad idea 用 reference。
6. 不把 synthesis 当 ground truth。
```

---

## 16.3 Provenance Generation Skill

目标：

```text
生成 provenance.md。
```

这是核心 skill。

要求：

```text
1. 写清 why this version exists。
2. 写清 inputs used。
3. 写清 synthesis rationale。
4. 写清 citation rationale。
5. 写清 audit / adoption rationale。
6. 写清 limits and uncertainty。
7. 写清 revision triggers。
```

---

## 16.4 Citation Formatting Skill

目标：

```text
保证 citation 既能读，也能解析。
```

要求：

```text
1. footnote 格式一致。
2. references 格式一致。
3. target 使用 file path。
4. target_version 必须存在。
5. pinned_version 必须存在。
6. why_cited 必须存在。
7. evidence_summary 必须存在。
```

---

## 16.5 Citation Audit Skill

目标：

```text
检查 citation 是否真的支持正文。
```

检查：

```text
1. footnote target 是否存在。
2. pinned version 是否存在。
3. why_cited 是否具体。
4. evidence_summary 是否可验证。
5. citation 是否过度支持。
6. cited card 是否 active/adopted。
```

---

## 16.6 Dynamic Retrieval Skill

目标：

```text
当 evidence 不足时，检索并沉淀新资料。
```

要求：

```text
1. 先写 retrieval_request。
2. 记录为什么现有 data 不足。
3. 检索结果进入 data/raw。
4. source manifest 更新。
5. provenance 中记录动态检索。
```

---

## 16.7 Version Adoption Skill

目标：

```text
判断 version 是否进入 kb view。
```

规则：

```text
1. 1.0 pass 后可以 adopted。
2. minor pass 后可以 adopted。
3. major candidate 必须 impact review。
4. latest 不等于 adopted。
```

---

## 16.8 Impact Analysis Skill

目标：

```text
根据 major change 和 citation graph 生成 impact queue。
```

规则：

```text
1. footnote citation = high impact。
2. reference citation = medium impact。
3. plain link 默认不传播。
4. 不自动重写下游。
```

---

## 16.9 View Build Skill

目标：

```text
生成 kb/ 和 generated/。
```

要求：

```text
1. kb 只渲染 adopted version。
2. kb/_index.yaml 从 root node.yaml 生成。
3. citation graph 从 kb/*.md 解析。
4. status 可被 agent 快速读取。
```

---

## 16.10 Skill Eval Skill

目标：

```text
用每次 0-1 run 评估 skill。
```

输出：

```text
skill_eval.md
skill_eval_log.yaml
```

评估维度：

```text
citation correctness
provenance quality
schema compliance
evidence sufficiency
audit pass rate
dynamic retrieval usefulness
node adoption readiness
impact clarity
```

---

# 17. 0-1 Run Evaluation

初始化阶段每次都是 0-1 是合理的。

原因：

```text
1. 每个 run 都是独立生成样本。
2. 可以评估 skill 在新内容上的 zero-shot 能力。
3. 可以比较 skill version 改动前后效果。
4. 可以快速暴露 schema、citation、provenance 的失败点。
5. 可以避免只优化某一个旧 card 的局部模式。
```

每次 0-1 run 记录：

```text
run_id
skill_bundle_version
target_node
data_scope
dynamic_retrieval_used
audit_result
adopted_or_not
failure_modes
skill_patch_recommended
```

推荐评分：

| 维度                           |  分数 |
| ---------------------------- | --: |
| Schema compliance            | 0-5 |
| Citation quality             | 0-5 |
| Provenance quality           | 0-5 |
| Evidence fit                 | 0-5 |
| Card usefulness              | 0-5 |
| Adoption readiness           | 0-5 |
| Dynamic retrieval discipline | 0-5 |

不是为了追求“更好”，而是为了发现：

```text
哪个 skill 导致了哪个 failure mode？
```

---

# 18. Dynamic Retrieval Policy

动态检索允许，但必须受控。

## 18.1 Allowed

```text
1. 当前 data 明显不足。
2. audit 发现 citation 不能支持 claim。
3. concept/definition 需要额外 source 才能不胡编。
4. skill construction 需要外部 pattern。
```

## 18.2 Not Allowed

```text
1. 为了让 card 看起来丰富而随意搜索。
2. 搜完不保存 raw source。
3. 搜完只把内容写进 card，不进入 provenance。
4. 不写 retrieval_request。
```

## 18.3 Retrieval Request Schema

```markdown
# Retrieval Request

run_id:: ...
target_node:: ...
created_by:: generator | audit | planner
status:: open

## Why existing data is insufficient

...

## Missing evidence

...

## Desired source types

- paper
- repo
- docs
- discussion
- benchmark
- governance doc

## Suggested queries

...

## Acceptance criteria

- Raw source must be preserved.
- Source manifest must be updated.
- Provenance must record retrieval.
- Retrieved evidence must be cited or rejected.
```

---

# 19. Agent Task Files

每个 agent 通过文件接收指令，而不是通过长 prompt。

## 19.1 Planner Task

```text
.llmwiki/agents/planner/task.md
```

职责：

```text
选择 loop
选择 run target
写 run_plan.md
不直接写 card
```

## 19.2 Generator Task

```text
.llmwiki/agents/generator/task.md
```

职责：

```text
生成 version bundle
不擅自扩大 data scope
evidence 不足时写 retrieval_request
```

## 19.3 Audit Task

```text
.llmwiki/agents/audit/task.md
```

职责：

```text
检查 schema
检查 citation
检查 provenance
检查 version adoption
```

## 19.4 Eval Task

```text
.llmwiki/agents/eval/task.md
```

职责：

```text
评估本次 run 对 skill 的启发
区分 case-level observation 和 skill-level failure
```

---

# 20. Git Policy

Git 只做 checkpoint。

不作为：

```text
card version reader
knowledge evolution reader
primary history system
```

Git commit 粒度：

```text
1. bootstrap checkpoint
2. run complete checkpoint
3. skill update checkpoint
4. major impact checkpoint
```

Commit message：

```bash
git commit -m "run: initialize node 20260522_143012_source_preservation_precondition_trust" \
  --trailer "Run-ID: run_20260522_143012" \
  --trailer "Node-ID: 20260522_143012_source_preservation_precondition_trust" \
  --trailer "Adopted-Version: 1.0"
```

---

# 21. Demo Acceptance Criteria

Demo 成功需要满足：

```text
1. 至少生成 5 个 adopted nodes。
2. 每个 node 有完整 version bundle。
3. 每个 adopted card 进入 kb/。
4. kb/_index.yaml 可由 script 生成。
5. 每个 card.md 有 Footnotes 和 References sections。
6. 每个 provenance.md 能解释 why。
7. 至少有 1 个动态检索案例。
8. 至少有 1 个 evidence insufficient 被记录。
9. 至少有 1 个 skill_eval.md。
10. 至少有 1 个 major candidate 或 simulated major change 触发 impact_queue。
```

---

# 22. Initial Demo Backlog

建议第一批 0-1 nodes：

```text
1. current_kb_initialization_loop
2. structured_markdown_as_process_artifact_policy
3. llm_wiki_working_definition
4. source_preservation_precondition_trust
5. provenance_as_core_knowledge_asset
6. citation_driven_impact_propagation
7. dynamic_retrieval_as_controlled_fallback
```

第一批 skills：

```text
1. node_bundle_generation
2. provenance_generation
3. citation_formatting
4. citation_audit
5. dynamic_retrieval
6. adoption_gate
7. view_building
8. skill_eval
```

---

# 23. Recommended Execution Order

## Phase 1: Bootstrap Contracts

```text
create kb/_schema.yaml
create .llmwiki/control/principles.md
create scripts skeleton
create skill seeds
```

## Phase 2: Inventory Existing Data

```text
scan data/raw
scan data/manifests
create source_candidates
identify first nodes
```

## Phase 3: First 0-1 Node

```text
generate one simple node
write card
write provenance
write change
audit
adopt
build kb
```

## Phase 4: Repeat 0-1 Nodes

```text
generate 3-5 more nodes
evaluate skill performance after each
patch skills only when failure mode is clear
```

## Phase 5: Dynamic Retrieval Test

```text
force or encounter one evidence gap
write retrieval_request
retrieve new information
preserve raw source
generate node using new source
record provenance
```

## Phase 6: Major Change Test

```text
create or simulate 1.1 -> 2.0
write change.md
parse citations
generate impact_queue
do not auto rewrite downstream
```

## Phase 7: Skill Eval and Demo Report

```text
summarize nodes created
summarize skill failures
summarize schema friction
summarize next improvements
```

---

# 24. Final Operating Principle

当前 demo 的核心不是生成一个完美 KB。

核心是验证：

```text
agent 是否能在文件系统中持续生产、采纳、审计、解释、更新知识对象。
```

最终 contract：

```text
nodes/ 是平面知识对象数据库。
version bundle = node.yaml + card.md + provenance.md + change.md。
kb/ 是 adopted version 的消费视图。
citation 在 card 内部。
provenance 是核心资产。
change 解释版本跃迁。
graph 和 impact 从 citation 后处理出来。
动态检索必须沉淀进 data。
每次 0-1 run 都是 skill evaluation sample。
```