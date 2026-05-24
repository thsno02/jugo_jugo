# Provenance / 溯源记录

node_id:: 20260524_050032_current_kb_initialization_loop
version:: 1.0

## 为什么存在这个版本

这个版本用于把 `当前 KB 初始化 loop 把 raw data 转化为可审计 adopted nodes` 固化为一个可引用、可审计、可修订的 KB node。它不是最终百科条目，而是初始化阶段的 adopted knowledge object。

## 使用的输入

### 已有 data

- loop_plan_init_kb.md
- nodes/20260524_050031_llm_wiki_working_definition/versions/1.0/card.md
- reports/source_gap_review.md
- data/manifests/sources.jsonl
- data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt

### 动态检索

无。本版本只使用已有本地 data 和 process artifacts。

### prior KB nodes

如果本版本引用了已有 KB node，引用关系写在 `card.md` 的 footnotes 或 references 中，并通过 `pinned_version` 固定到具体版本。

### 过程 artifacts

- .llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap/run_plan.md
- .llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap/data_scope.md
- .llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap/generator_trace.md
- .llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap/audit_report.md

## 生产理由

本版本以小而可审计的 0-1 bundle 方式生成。正文中的具体 claim 绑定到保存过的 raw/source artifact 或已 adopted 的 KB node；综合判断只作为当前 demo 的暂时性 synthesis。

## Citation 理由

Footnotes 支持具体 claim；References 提供背景、过程或定义语境。路径保持 repo-root relative，便于 `nodes/` 与 `kb/` 两个视图共同解析。

## Synthesis 决策

本 node 区分 source-backed observation、process rule 和 agent synthesis，不把 agent synthesis 当作 ground truth。

## Audit trail

audit_result:: passed
audit_report:: .llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap/audit_report.md

## Adoption 理由

1.0 被 adopted，因为 version bundle 完整，`card.md` 有 Footnotes 和 References，citation 字段可解析，provenance 说明了输入、综合、审计和修订触发条件。

## 限制与不确定性

这是初始化阶段 node，后续如果出现更强 evidence、semantic citation audit 或 downstream impact review，应修订。

## 修订触发条件

- citation 指向的 source 缺失、过期、被误读或不足以支持 claim。
- 后续 major version 改变定义或 support contract。
- citation audit 发现 footnote 过度支持正文。
- 动态检索加入更强或相矛盾的 evidence。
