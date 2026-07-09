---
schema: process_provenance.v1
project: jugo_jugo_llm_wiki
main_language: zh
publish_status: sanitized
created: 2026-07-09
---

# Process Provenance

本文档说明 LLM Wiki KB 是如何从交互、source mining、agent loop、审计和 git history 中长出来的。它是公开版过程溯源（process provenance），不是原始聊天 transcript。

## Scope And Coverage

覆盖范围：

- v1-v5 loop artifacts，包括 handoff、reports、learnings、audit files 和 KB outputs。
- Claude Code / Codex 交互中的可复用机制、设计决策和失败模式。
- v5 发布分支中的过程化 commit history。

不覆盖：

- 完整 Claude JSONL。
- 完整 Codex JSONL。
- 本机全局配置、token、endpoint、绝对路径、邮箱或完整工具输出。

覆盖判断（coverage）：

- repo artifact coverage：高，来自 tracked files。
- Claude session coverage：中，来自本地 session group 的二次整理。
- Codex session coverage：有限，当前只作为本轮发布整理的上下文来源，不发布 raw transcript。

## Source Classes

| Source Class | Publish Status | 用途 |
| --- | --- | --- |
| Loop handoff / reports / learnings | publishable | 记录 loop 启动边界、阶段状态、执行复盘和下一轮输入。 |
| KB cards / draft cards / justification journals | publishable | 记录知识从 source 到 draft，再到 active KB 的转化结果。 |
| Audit outputs | publishable | 记录 source faithfulness、backlink/orphan、mechanical filter 和 semantic judge。 |
| User-insights sanitized summaries | publishable summary | 记录用户纠偏、设计决策和交互中形成的机制。 |
| Claude/Codex raw transcripts | local-only | 仅作为本地证据源，不进入 git。 |

## Timeline

| Phase | Process | Published Evidence |
| --- | --- | --- |
| v1 | topic hub skeleton 和 coverage framing | `loops/v1_topic_hub_skeleton_20260524/reports/` |
| v2 | early KB loop、brain mailbox、draft/adoption 试验 | `loops/v2_llm_wiki_loop_20260525/reports/loop_report.md` |
| v3 | draft-first pipeline、similarity、interlink、candidate KB | `loops/v3_llm_wiki_loop_20260525/CLAUDE_CODE_HANDOFF.md` |
| v4 | full material extraction、governance、audit methodology | `loops/v4_llm_wiki_loop_20260602/learnings/` |
| v5 | source routing、parallel extraction、fusion、governance、FSJS audit | `loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md` |
| post-v5 | information-density regression diagnosis | `loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md` |

## Workflow Architecture

核心结构：

```text
source material
-> routed read surface
-> draft card
-> justification journal
-> fusion / duplicate / distinct-link decision
-> active KB card
-> governance links
-> audit report
-> learnings for next loop
```

关键角色：

- main-agent：控制面（control plane），负责边界、调度、验收和历史整理。
- reader / questioning / reframing / reviewer：单源提取与重构角色。
- scripts：执行确定性治理动作，例如 YAML lint、batch link、backward backlink、mechanical audit。
- user-insights sidecar：整理交互中的设计判断，输出摘要化项目洞察。

## Design Decisions

- 中文主语言（Chinese main language）：人类可读文档用中文，schema keys 和 technical identifiers 保持英文。
- 自底向上（bottom-up）：先做 atomic cards，再形成 hub/topic，不提前用 top-down taxonomy 固化结构。
- provenance first：card 是结果，justification/provenance 是把 draft 做实为 fact-like knowledge 的过程。
- no raw transcript publication：原始聊天记录风险高、噪声高，只作为本地 evidence source。
- anti-merge bias：fusion 阶段宁可保留 distinct_link，也不轻易合并造成 cluster damage。
- derived governance：related/backlink 应尽量从 citation graph 和 batch governance 派生，而不是手工维护。

## Failure Modes And Corrections

| Failure Mode | Correction |
| --- | --- |
| 目标漂移：从“生成 KB”变成“讨论如何生成 KB” | 明确 loop 文件和 task contract，要求 source-grounded production。 |
| 防御性截断 source | 在大上下文条件下优先完整读取 source。 |
| 卡片过粗或过少 | 引入 draft-first、questioning loop 和 evidence_basis。 |
| 过度合并 | fusion scan 使用 anti-merge bias，并通过 justification 记录 merge/duplicate/distinct_link。 |
| orphan / backlink 不对称 | batch_link + orphan governance + backward_backlink 独立 pass。 |
| v5 信息密度下降 | post-v5 诊断指出论证层次、边界条件和 distinction footnotes 需要进入 v6 hard gate。 |

## Audit And Quality Gates

v5 的主要审计门禁：

- Source faithfulness：机械 grep filter + semantic judge。
- Graph health：orphan rate、backlink asymmetry、cross-domain bridge。
- YAML/schema：frontmatter 和 justification link 检查。
- FSJS：Filter -> Shard -> Judge -> Synthesize。
- Loop learning：execution summary 与 next_loop_prep 作为下一轮输入。

## Redaction Policy

发布规则：

- 不提交 Claude/Codex 原始 JSONL。
- 不提交本机路径、邮箱、endpoint、token、private config。
- 不发布完整 Raw Input 长摘录。
- 可以发布经过摘要化的 timeline、decision log、workflow lesson、failure mode 和 audit result。
- 可公开文件应能独立解释“为什么生成这些文档”和“它们在 loop 中承担什么作用”。

## Evidence Map

| Claim | Evidence |
| --- | --- |
| v3 需要 cold-start self-contained loop | `loops/v3_llm_wiki_loop_20260525/CLAUDE_CODE_HANDOFF.md` |
| v4 固化了审计和治理经验 | `loops/v4_llm_wiki_loop_20260602/learnings/audit_methodology.md` |
| v5 使用 source routing 和治理工具链 | `loops/v5_llm_wiki_loop_20260612/tools/` |
| v5 完成 63 有效源到 477 active cards | `loops/v5_llm_wiki_loop_20260612/learnings/execution_summary.md` |
| v5 审计通过但存在权威扁平化和信息密度风险 | `loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_final_audit_report.md` |
| post-v5 需要修复论证深度 | `loops/v5_llm_wiki_loop_20260612/outputs/llm_wiki/kb/audits/v5_info_density_diagnosis.md` |
| 交互洞察已摘要化发布 | `user-insights/index.md` |
