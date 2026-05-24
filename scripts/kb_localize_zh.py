#!/usr/bin/env python3
"""Localize the KB initialization demo's human-readable artifacts to Chinese."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]

N = {
    "definition": "20260524_050031_llm_wiki_working_definition",
    "loop": "20260524_050032_current_kb_initialization_loop",
    "source": "20260524_050033_source_preservation_precondition_trust",
    "provenance": "20260524_050034_provenance_as_core_knowledge_asset",
    "citation": "20260524_050035_citation_driven_impact_propagation",
    "retrieval": "20260524_050036_dynamic_retrieval_as_controlled_fallback",
    "enterprise": "20260524_050318_enterprise_scale_requires_governed_context_layer",
}

RUN_BOOTSTRAP = ".llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap"
RUN_RETRIEVAL = ".llmwiki/runs/run_20260524_050318_dynamic_retrieval_enterprise_scale"
RUN_IMPACT = ".llmwiki/runs/run_20260524_050634_major_impact_simulation"


def write(path: str, text: str) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text.rstrip() + "\n", encoding="utf-8")


def load_yaml(path: str) -> dict[str, Any]:
    return yaml.safe_load((ROOT / path).read_text(encoding="utf-8"))


def write_yaml(path: str, data: Any) -> None:
    target = ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True, width=100) + "\n", encoding="utf-8")


def update_title(node_id: str, title: str) -> None:
    for rel in [f"nodes/{node_id}/node.yaml", f"nodes/{node_id}/versions/1.0/node.yaml"]:
        data = load_yaml(rel)
        data["title"] = title
        write_yaml(rel, data)


def citation_block(fields: dict[str, str]) -> str:
    lines = []
    for key in [
        "target",
        "target_version",
        "pinned_version",
        "citation_role",
        "why_cited",
        "evidence_summary",
        "source_path",
    ]:
        if key in fields:
            lines.append(f"    {key}: {fields[key]}")
    return "\n".join(lines)


def raw(target: str, role: str, why: str, summary: str, source_path: str | None = None) -> dict[str, str]:
    return {
        "target": target,
        "target_version": "source_snapshot_2026-05-21",
        "pinned_version": target,
        "citation_role": role,
        "why_cited": why,
        "evidence_summary": summary,
        "source_path": source_path or str(Path(target).parent),
    }


def artifact(target: str, version: str, role: str, why: str, summary: str) -> dict[str, str]:
    return {
        "target": target,
        "target_version": version,
        "pinned_version": target,
        "citation_role": role,
        "why_cited": why,
        "evidence_summary": summary,
    }


def node(node_id: str, role: str, why: str, summary: str) -> dict[str, str]:
    return {
        "target": f"kb/{node_id}.md",
        "target_version": "1.0",
        "pinned_version": f"nodes/{node_id}/versions/1.0/card.md",
        "citation_role": role,
        "why_cited": why,
        "evidence_summary": summary,
    }


PLAN = artifact(
    "loop_plan_init_kb.md",
    "plan_snapshot_2026-05-24",
    "process_contract",
    "该文件定义了本 demo 的初始化 loop、version bundle、provenance、citation、adoption 与 impact 规则。",
    "计划明确要求 nodes 是版本化知识对象库，kb/ 是 adopted view，citation 驱动 impact，动态检索必须受控并沉淀为 data asset。",
)
SOURCE_GAP = artifact(
    "reports/source_gap_review.md",
    "source_snapshot_2026-05-21",
    "evidence_inventory",
    "该报告总结了本地 raw corpus、覆盖状态和硬性 evidence gap。",
    "报告记录了 origin/workflow/implementation 证据，也记录了 Reddit 与 AICritique 等受阻来源。",
)
CLAIMS = artifact(
    "data/manifests/claims.jsonl",
    "source_snapshot_2026-05-21",
    "claim_manifest",
    "该 manifest 提供采集阶段生成的 source-linked claim records。",
    "记录包含 claim、coverage area、confidence 和 supporting sources，是从 raw data 进入 KB 的中间证据层。",
)
SOURCES = artifact(
    "data/manifests/sources.jsonl",
    "source_snapshot_2026-05-24",
    "source_manifest",
    "该 manifest 记录 source id、采集状态、本地路径、标签和来源类型。",
    "它是本地 source provenance 的入口，也记录了动态检索新增的成功与失败来源。",
)
GIST = raw(
    "data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt",
    "primary_source",
    "支持 LLM Wiki 工作定义：在 immutable raw sources 与用户查询之间维护一个 agent 生成的持久 wiki。",
    "Karpathy gist 描述了 raw sources、wiki、schema 三层，以及 ingest、query、lint 等操作。",
)
CLAW = raw(
    "data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt",
    "implementation_source",
    "支持 LLM Wiki runtime 可以暴露 raw/wiki/schema workflow、lint、gap mapping 与 MCP/CLI 接口。",
    "页面描述了 runtime、raw asset、wiki output、manifest、compile readiness、lint 和 gap mapping。",
)
COMPILER = raw(
    "data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md",
    "implementation_source",
    "支持把 LLM Wiki 理解为 compile-and-maintain 工作流，而不只是查询时检索。",
    "README 描述了把 raw sources 编译成 interlinked markdown wiki，并提供 ingest、compile、query、view 等命令。",
)
ALCE = raw(
    "data/raw/arxiv/arxiv-alce/text.txt",
    "research_context",
    "支持 citation 不能只看形式存在，还需要评价 citation quality 与 verifiability。",
    "ALCE 摘要把 citation 作为提升事实正确性和可验证性的机制，并提出自动评价 citation quality。",
)
ATLAN = {
    "target": "data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt",
    "target_version": "source_snapshot_2026-05-24_dynamic",
    "pinned_version": "data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt",
    "citation_role": "dynamic_retrieval_support",
    "why_cited": "该动态检索来源直接讨论 enterprise 场景下 LLM Wiki 与 RAG 的 scale、governance、access control 和 freshness 问题。",
    "evidence_summary": "来源认为 LLM Wiki 适合 bounded personal-scale corpus，而 enterprise 使用需要治理、访问控制、freshness 与并发控制。",
    "source_path": "data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524",
}


def standard_provenance(node_id: str, title: str, inputs: list[str], run_dir: str, dynamic: str, limits: str) -> str:
    lines = "\n".join(f"- {item}" for item in inputs)
    return f"""# Provenance / 溯源记录

node_id:: {node_id}
version:: 1.0

## 为什么存在这个版本

这个版本用于把 `{title}` 固化为一个可引用、可审计、可修订的 KB node。它不是最终百科条目，而是初始化阶段的 adopted knowledge object。

## 使用的输入

### 已有 data

{lines}

### 动态检索

{dynamic}

### prior KB nodes

如果本版本引用了已有 KB node，引用关系写在 `card.md` 的 footnotes 或 references 中，并通过 `pinned_version` 固定到具体版本。

### 过程 artifacts

- {run_dir}/run_plan.md
- {run_dir}/data_scope.md
- {run_dir}/generator_trace.md
- {run_dir}/audit_report.md

## 生产理由

本版本以小而可审计的 0-1 bundle 方式生成。正文中的具体 claim 绑定到保存过的 raw/source artifact 或已 adopted 的 KB node；综合判断只作为当前 demo 的暂时性 synthesis。

## Citation 理由

Footnotes 支持具体 claim；References 提供背景、过程或定义语境。路径保持 repo-root relative，便于 `nodes/` 与 `kb/` 两个视图共同解析。

## Synthesis 决策

本 node 区分 source-backed observation、process rule 和 agent synthesis，不把 agent synthesis 当作 ground truth。

## Audit trail

audit_result:: passed
audit_report:: {run_dir}/audit_report.md

## Adoption 理由

1.0 被 adopted，因为 version bundle 完整，`card.md` 有 Footnotes 和 References，citation 字段可解析，provenance 说明了输入、综合、审计和修订触发条件。

## 限制与不确定性

{limits}

## 修订触发条件

- citation 指向的 source 缺失、过期、被误读或不足以支持 claim。
- 后续 major version 改变定义或 support contract。
- citation audit 发现 footnote 过度支持正文。
- 动态检索加入更强或相矛盾的 evidence。
"""


def standard_change(node_id: str, created_at: str, run_dir: str, meaning: str) -> str:
    return f"""# Change: genesis -> 1.0

node_id:: {node_id}
from_version:: null
to_version:: 1.0
change_scale:: minor
propagation_required:: false
created_at:: {created_at}
run_id:: {run_dir}/

## 为什么变化

这是该 node 的 genesis version。

## 旧含义

之前没有 adopted version。

## 新含义

{meaning}

## Semantic delta

初始创建，没有替代旧 support contract。

## 为什么是 minor

genesis version 不会改变既有下游依赖。

## 预期影响

不需要触发 downstream impact propagation。
"""


def localize_nodes() -> None:
    titles = {
        N["definition"]: "LLM Wiki 是由来源支撑、由 agent 维护的持久 wiki artifact",
        N["loop"]: "当前 KB 初始化 loop 把 raw data 转化为可审计 adopted nodes",
        N["source"]: "Source preservation 是 KB 信任的前提",
        N["provenance"]: "Provenance 是核心知识资产，不是附录",
        N["citation"]: "Citation edges 在 major change 后驱动 impact review",
        N["retrieval"]: "动态检索是受控 fallback，不是临时补料",
        N["enterprise"]: "Enterprise-scale LLM Wiki 需要 governed context layer",
    }
    for node_id, title in titles.items():
        update_title(node_id, title)

    write(
        f"nodes/{N['definition']}/versions/1.0/card.md",
        f"""# {titles[N['definition']]}

在这个 KB initialization demo 中，LLM Wiki 指的是一种持久知识系统：raw sources 先被保存为不可随意改写的 evidence layer，agent 再从这些来源编译和维护 markdown wiki，schema/control rules 则让 wiki 可检查、可引用、可修订。[^1]

本地证据也支持把 LLM Wiki 理解为一种 maintenance architecture，而不是单次 query-time retrieval：source capture、readable extraction、digest/compile、claim mapping、report update、lint/audit 和 human review 都是反复出现的流程元素。[^2]

这个定义是 operational definition，不是宇宙真理。它服务于 node generation、citation audit 和后续 revision；它不要求所有实现都采用相同 graph model、storage engine、interface 或 evaluation method。[^3]

## Footnotes

[^1]:
{citation_block(GIST)}

[^2]:
{citation_block(SOURCE_GAP)}

[^3]:
{citation_block(COMPILER)}

## References

### [R1] 初始化计划
{citation_block(PLAN)}

### [R2] Claim manifest
{citation_block(CLAIMS)}
""",
    )
    write(
        f"nodes/{N['loop']}/versions/1.0/card.md",
        f"""# {titles[N['loop']]}

当前 demo loop 从已经保存的本地 data 出发，创建小型 node version bundle，记录 provenance，审计 citation，把通过审计的版本 adopted 到 `kb/`，再从 citation 派生 graph 和 impact artifacts，而不是手写维护 graph。[^1]

这个流程把 LLM Wiki 工作定义落实为 filesystem contract：raw sources 留在 `data/`，维护层知识对象放在 `nodes/`，adopted cards 渲染到 `kb/`，可重建的后处理结果放在 `generated/`。[^2]

这个 loop 的目标很窄：它不是一次性写出完美百科，而是验证 agent 能不能持续生产、采纳、审计、解释和更新可追溯知识对象。[^3]

## Footnotes

[^1]:
{citation_block(PLAN)}

[^2]:
{citation_block(node(N['definition'], "background_definition", "提供本 loop 正在操作化的 adopted working definition。", "被引 node 定义了由来源支撑、由 agent 维护的持久 wiki artifact。"))}

[^3]:
{citation_block(SOURCE_GAP)}

## References

### [R1] Source manifest
{citation_block(SOURCES)}

### [R2] Runtime 实现例子
{citation_block(CLAW)}
""",
    )
    write(
        f"nodes/{N['source']}/versions/1.0/card.md",
        f"""# {titles[N['source']]}

如果后续 agent 不能从 synthesized claim 回到背后的保存材料，KB 就无法被真正审计。在这个 repo 里，这意味着 source id、acquisition status、本地 raw path、readable text path、digest、claim links 和 access failure 都要和 synthesized nodes 一起保留下来。[^1]

LLM Wiki 的工作定义依赖这个分层：wiki 是 maintained layer，位于 immutable raw sources 和面向用户的 answers 之间；它不能替代 source record。[^2]

Source preservation 本身不保证 synthesis 为真。它保证 synthesis 可检查：auditor 可以判断一个 claim 是否被支持、是否过宽、是否过期、是否被反驳，或是否只是 process decision。[^3]

## Footnotes

[^1]:
{citation_block(SOURCES)}

[^2]:
{citation_block(node(N['definition'], "background_definition", "定义 raw-source 与 maintained-wiki 的分工。", "被引 node 说明 preserved raw sources 和 maintained wiki artifacts 具有不同职责。"))}

[^3]:
{citation_block(SOURCE_GAP)}

## References

### [R1] 本地 claim records
{citation_block(CLAIMS)}

### [R2] Runtime implementation evidence
{citation_block(CLAW)}
""",
    )
    write(
        f"nodes/{N['provenance']}/versions/1.0/card.md",
        f"""# {titles[N['provenance']]}

在初始化 contract 中，`card.md` 写知识结果，`provenance.md` 写这个结果为什么存在、用了哪些输入、哪些部分是 synthesis、citation 为什么这样选、为什么允许 adoption，以及什么情况会触发 revision。[^1]

这使 provenance 成为可复用知识对象的一部分，而不是事后说明。Source preservation 给 auditor 材料可查，但 provenance 解释 agent 如何从材料走到 adopted node。[^2]

如果缺少 provenance，后续 agent 即使找到 raw files，也可能无法理解 synthesis boundary、adoption rationale 或被拒绝的 evidence。[^3]

## Footnotes

[^1]:
{citation_block(PLAN)}

[^2]:
{citation_block(node(N['source'], "claim_support", "支持 audit 依赖可检查 source paths 和 source records 的主张。", "被引 node 说明 preserved evidence 为什么是后续信任检查的前提。"))}

[^3]:
{citation_block(ALCE)}

## References

### [R1] 工作定义
{citation_block(node(N['definition'], "background_definition", "提供 provenance 所处的 source-backed maintained-wiki 语境。", "被引 node 把 KB 定义为 grounded in preserved sources 的 maintained artifact。"))}

### [R2] Source gap review
{citation_block(SOURCE_GAP)}
""",
    )
    write(
        f"nodes/{N['citation']}/versions/1.0/card.md",
        f"""# {titles[N['citation']]}

这个 demo 把 citation 当作 dependency information 的来源。A footnote from node A to node B 表示 A 对某个 claim 强依赖 B；reference 表示较弱的背景依赖；plain link 默认不传播。[^1]

当 node B 出现 major version candidate，系统可以解析 citation edges，把 citing nodes 放入 impact queue，而不是手动维护 `depends_on` 字段。[^2]

这个设计是保守的：impact analysis 只创建 review tasks，不自动重写下游 nodes。这样可以把 semantic revision 和 graph computation 分开。[^3]

## Footnotes

[^1]:
{citation_block(PLAN)}

[^2]:
{citation_block(node(N['provenance'], "claim_support", "解释 citations 与 provenance 为什么必须保留 support boundary。", "被引 node 把 provenance 和 citation rationale 视为可复用 audit surface。"))}

[^3]:
{citation_block(ALCE)}

## References

### [R1] Source preservation node
{citation_block(node(N['source'], "background_support", "提供 citation audit 可行所需的 source-preservation 前提。", "被引 node 说明 support 必须可追溯到 preserved source records。"))}

### [R2] Claim manifest
{citation_block(CLAIMS)}
""",
    )
    write(
        f"nodes/{N['retrieval']}/versions/1.0/card.md",
        f"""# {titles[N['retrieval']]}

动态检索只在现有 evidence 不足以支持某个目标 claim 或 node 时才允许，并且必须先把 gap 写下来再搜索。[^1]

本地 source review 已经记录了硬性缺口，包括被 blocked 的 Reddit captures 和被拦截的 enterprise article。这些缺口可以触发 retrieval request，但不能被 unsupported synthesis 静默替代。[^2]

当 retrieval 被使用时，新 source 必须进入 `data/raw/`，写入 source manifest，并出现在 provenance 中；否则 KB 只是多了一段文字，却没有增加 auditability。[^3]

## Footnotes

[^1]:
{citation_block(PLAN)}

[^2]:
{citation_block(SOURCE_GAP)}

[^3]:
{citation_block(node(N['source'], "claim_support", "支持新 evidence 必须先保存才能支撑可信 synthesis 的要求。", "被引 node 说明 source preservation 是后续 audit 的前提。"))}

## References

### [R1] 当前初始化 loop
{citation_block(node(N['loop'], "process_context", "把受控 retrieval 放回整个 initialization loop。", "被引 node 描述了 0-1 node loop、audit、adoption 和 generated artifacts。"))}

### [R2] Source manifest
{citation_block(SOURCES)}
""",
    )
    write(
        f"nodes/{N['enterprise']}/versions/1.0/card.md",
        f"""# {titles[N['enterprise']]}

动态检索 run 保存了一个 enterprise/RAG comparison 来源，因为原有本地 corpus 中 enterprise article 被公司网络拦截，形成了 evidence gap。新来源认为，LLM Wiki 与 RAG 回答的是相关但尺度不同的知识访问问题：wiki-style approach 更适合 bounded、stable、personal-scale corpus；enterprise 场景则会引入 scale、access control、freshness 和 concurrency 问题，不能靠放大 markdown folder 自行解决。[^1]

对这个 KB 来说，可采纳的 claim 比来源中的产品叙事更窄：enterprise-scale LLM Wiki use 不应被理解为“把个人 wiki 做大一点”。它需要 governed context layer 或等价控制机制，才能让 source-backed synthesis 在多用户、多系统环境中保持可信。[^2]

这也符合本地 KB 规则：新 evidence 必须先保存为 data，并写入 provenance，才能支撑 adopted synthesis。[^3]

## Footnotes

[^1]:
{citation_block(ATLAN)}

[^2]:
{citation_block(node(N['definition'], "background_definition", "提供 LLM Wiki 作为 source-backed maintained wiki artifact 的 adopted definition。", "被引 node 区分 preserved raw sources、maintained wiki artifacts 和 control rules。"))}

[^3]:
{citation_block(node(N['retrieval'], "process_support", "说明动态检索为什么必须 request、preserve、enter manifest 并写入 provenance。", "被引 node 说明 retrieval 不能作为没有 audit trail 的临时补料。"))}

## References

### [R1] Retrieval log
{citation_block(artifact(".llmwiki/control/retrieval_log.yaml", "retrieval_log_2026-05-24", "process_artifact", "记录 AICritique 失败尝试和 Atlan 成功检索。", "log 显示同一个 enterprise evidence-gap request 下有一个 intercepted source 和一个 preserved ok source。"))}

### [R2] Source preservation node
{citation_block(node(N['source'], "audit_background", "解释为什么 synthesized claim 必须能回到保存的本地 source material。", "被引 node 把 source preservation 视为后续 inspection 与 trust 的前提。"))}
""",
    )

    provenance_inputs = {
        N["definition"]: [
            "data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt",
            "reports/source_gap_review.md",
            "data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md",
            "loop_plan_init_kb.md",
            "data/manifests/claims.jsonl",
        ],
        N["loop"]: [
            "loop_plan_init_kb.md",
            f"nodes/{N['definition']}/versions/1.0/card.md",
            "reports/source_gap_review.md",
            "data/manifests/sources.jsonl",
            "data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt",
        ],
        N["source"]: [
            "data/manifests/sources.jsonl",
            f"nodes/{N['definition']}/versions/1.0/card.md",
            "reports/source_gap_review.md",
            "data/manifests/claims.jsonl",
            "data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt",
        ],
        N["provenance"]: [
            "loop_plan_init_kb.md",
            f"nodes/{N['source']}/versions/1.0/card.md",
            "data/raw/arxiv/arxiv-alce/text.txt",
            f"nodes/{N['definition']}/versions/1.0/card.md",
            "reports/source_gap_review.md",
        ],
        N["citation"]: [
            "loop_plan_init_kb.md",
            f"nodes/{N['provenance']}/versions/1.0/card.md",
            "data/raw/arxiv/arxiv-alce/text.txt",
            f"nodes/{N['source']}/versions/1.0/card.md",
            "data/manifests/claims.jsonl",
        ],
        N["retrieval"]: [
            "loop_plan_init_kb.md",
            "reports/source_gap_review.md",
            f"nodes/{N['source']}/versions/1.0/card.md",
            f"nodes/{N['loop']}/versions/1.0/card.md",
            "data/manifests/sources.jsonl",
        ],
    }
    created = {
        N["definition"]: "2026-05-24T05:00:31+08:00",
        N["loop"]: "2026-05-24T05:00:32+08:00",
        N["source"]: "2026-05-24T05:00:33+08:00",
        N["provenance"]: "2026-05-24T05:00:34+08:00",
        N["citation"]: "2026-05-24T05:00:35+08:00",
        N["retrieval"]: "2026-05-24T05:00:36+08:00",
    }
    for node_id in [N["definition"], N["loop"], N["source"], N["provenance"], N["citation"], N["retrieval"]]:
        dynamic = "无。本版本只使用已有本地 data 和 process artifacts。"
        limits = "这是初始化阶段 node，后续如果出现更强 evidence、semantic citation audit 或 downstream impact review，应修订。"
        if node_id == N["retrieval"]:
            dynamic = "本版本没有执行外部 retrieval；它记录 retrieval policy 和 evidence gap。实际动态检索在后续 enterprise-scale node 中执行。"
            limits = "本 node 只记录 retrieval policy 和 evidence gap，不声称已恢复被 blocked 的 Reddit 或 enterprise evidence。"
        write(
            f"nodes/{node_id}/versions/1.0/provenance.md",
            standard_provenance(node_id, titles[node_id], provenance_inputs[node_id], RUN_BOOTSTRAP, dynamic, limits),
        )
        write(
            f"nodes/{node_id}/versions/1.0/change.md",
            standard_change(node_id, created[node_id], RUN_BOOTSTRAP, f"该 node 现在有一个可渲染到 `kb/` 并可被后续 nodes 引用的 adopted 1.0 version bundle。"),
        )

    write(
        f"nodes/{N['enterprise']}/versions/1.0/provenance.md",
        f"""# Provenance / 溯源记录

node_id:: {N['enterprise']}
version:: 1.0

## 为什么存在这个版本

这个版本把动态检索测试从单纯 log event 转化为 adopted KB node。它记录检索到的来源能支持什么、失败来源为什么不能作为 evidence，以及综合结论的边界。

## 使用的输入

### 已有 data

- reports/source_gap_review.md
- {RUN_BOOTSTRAP}/retrieval_request.md
- .llmwiki/control/retrieval_log.yaml
- nodes/{N['definition']}/versions/1.0/card.md
- nodes/{N['retrieval']}/versions/1.0/card.md
- nodes/{N['source']}/versions/1.0/card.md

### 动态检索

- 失败但已保存：data/raw/webpage/aicritique-enterprise-knowledge-dynamic-20260524/
- 使用为 evidence：data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt

### prior KB nodes

- {N['definition']}
- {N['retrieval']}
- {N['source']}

### 过程 artifacts

- {RUN_RETRIEVAL}/run_plan.md
- {RUN_RETRIEVAL}/data_scope.md
- {RUN_RETRIEVAL}/audit_report.md

## 生产理由

本 node 不把动态来源中的产品叙事整体采纳为事实，只采纳一个更窄的 process claim：enterprise-scale use 会引入 governance、access-control、freshness 和 concurrency 要求，不能靠放大 personal markdown wiki 自动解决。

## Citation 理由

动态来源用 footnote 支持核心 claim；已有 KB nodes 用来连接 definition、retrieval discipline 和 source-preservation background。

## Synthesis 决策

AICritique 抓取结果是公司网络拦截页，保存但拒绝作为 evidence。Atlan 来源可用于 enterprise framing，但其 vendor-authored 性质在限制中明确记录。

## Audit trail

audit_result:: passed
audit_report:: {RUN_RETRIEVAL}/audit_report.md

## Adoption 理由

1.0 被 adopted，因为 dynamic source 已保存到 `data/raw/`，manifest 记录了来源，card 有 required citation sections，provenance 区分了 retrieved evidence、失败尝试和 synthesis。

## 限制与不确定性

Atlan 是 vendor-authored source，适合支持 enterprise framing，不适合当作独立 empirical validation 或产品优越性证据。

## 修订触发条件

- 后续个人设备重新 retrieve 到更独立的 enterprise source。
- semantic citation audit 发现 Atlan source 被过度使用。
- 新 evidence 反驳 scale/governance framing。
- dynamic retrieval policy 改变。
""",
    )
    write(
        f"nodes/{N['enterprise']}/versions/1.0/change.md",
        standard_change(N["enterprise"], "2026-05-24T05:03:18+08:00", RUN_RETRIEVAL, "KB 现在有一个使用动态检索来源生成的 adopted node，用于讨论 enterprise-scale governance requirements。"),
    )


def localize_candidate() -> None:
    cand_yaml = f"nodes/{N['source']}/versions/2.0/node.yaml"
    data = load_yaml(cand_yaml)
    data["title"] = "Source preservation 需要 provenance 才能支撑 KB 信任"
    write_yaml(cand_yaml, data)
    write(
        f"nodes/{N['source']}/versions/2.0/card.md",
        f"""# Source preservation 需要 provenance 才能支撑 KB 信任

这个 candidate 修改了 1.0 的 support contract：保存 source files 对 KB trust 是必要条件，但单独保存 source files 还不充分。后续 auditor 还需要 provenance 来解释 source 为什么被使用、synthesis 如何产生、哪些材料被拒绝，以及什么时候应该修订 node。[^1]

因为这个变化把 node 从“source preservation 是前提”改成“source preservation 加 provenance 才构成 support contract”，所有引用 1.0 framing 的下游 nodes 都需要 review，才能决定这个 candidate 是否可 adopted。[^2]

## Footnotes

[^1]:
{citation_block(node(N['provenance'], "claim_support", "支持 provenance 是可复用知识对象的一部分，而不是附录。", "被引 node 说明 provenance 记录 inputs、synthesis、citation rationale、audit、adoption、limits 和 revision triggers。"))}

[^2]:
{citation_block(node(N['citation'], "impact_rule", "解释为什么 major support-contract change 应该创建 impact review tasks，而不是自动重写下游 nodes。", "被引 node 说明 citation edges 在 major changes 后驱动 impact review。"))}

## References

### [R1] 工作定义
{citation_block(node(N['definition'], "background_definition", "提供本 candidate 所修订的 source-backed maintained-wiki 语境。", "被引 node 定义 preserved raw sources、maintained wiki artifacts 和 control rules。"))}
""",
    )
    write(
        f"nodes/{N['source']}/versions/2.0/provenance.md",
        f"""# Provenance / 溯源记录

node_id:: {N['source']}
version:: 2.0

## 为什么存在这个版本

这个 candidate 只用于测试 major-change impact propagation。它故意改变 adopted 1.0 node 的 support contract：source preservation 必要但不充分，还需要 provenance。

## 使用的输入

### 已有 data

- nodes/{N['source']}/versions/1.0/card.md
- nodes/{N['provenance']}/versions/1.0/card.md
- nodes/{N['citation']}/versions/1.0/card.md

### 动态检索

无。这是 impact test 使用的 simulated major candidate。

### prior KB nodes

- {N['provenance']}
- {N['citation']}
- {N['definition']}

### 过程 artifacts

- {RUN_IMPACT}/run_plan.md
- {RUN_IMPACT}/audit_report.md

## 生产理由

该 candidate 不会 adopted。它是一个受控测试 artifact，用来验证 `change.md` 与 `generated/citation_graph.yaml` 是否能共同生成 `generated/impact_queue.yaml`。

## Citation 理由

Candidate 引用 provenance 和 impact-rule nodes，用于说明这个 semantic change 为什么是 major，以及为什么需要 downstream review。

## Synthesis 决策

Candidate 把 trust contract 从单一前提收窄为两个部分：source preservation + provenance。

## Audit trail

audit_result:: held_for_impact_review
audit_report:: {RUN_IMPACT}/audit_report.md

## Adoption 理由

此 candidate 有意不 adopted。impact review 完成之前，它不得进入 `kb/`。

## 限制与不确定性

这是 simulated major change，不应被当成已采纳 correction。

## 修订触发条件

- impact queue 为空，说明 citation propagation 失败。
- downstream review 表明这个 candidate 实际不改变 support contract。
- demo 不再需要 simulation artifact。
""",
    )
    write(
        f"nodes/{N['source']}/versions/2.0/change.md",
        f"""# Change: 1.0 -> 2.0

node_id:: {N['source']}
from_version:: 1.0
to_version:: 2.0
change_scale:: major
propagation_required:: true
created_at:: 2026-05-24T05:06:34+08:00
run_id:: {RUN_IMPACT}/

## 为什么变化

这个 candidate 把 support contract 从“source preservation 是信任前提”改成“source preservation 加 provenance 才能支撑信任”。

## 旧含义

1.0 强调 preserved local source material 是后续 audit 的主要前提。

## 新含义

2.0 认为 preservation 仍然必要，但如果没有 provenance 记录 source use、synthesis rationale、rejection decisions、audit trail 和 revision triggers，就不足以支撑信任。

## Semantic delta

Candidate 把 provenance 从 supporting downstream concept 提升为 trust contract 的必要组成部分。

## 为什么这是 major

下游 nodes 如果把 source preservation 当作充分背景，就可能需要把 provenance requirements 一起纳入 claim。

## 预期影响

所有通过 footnotes 或 references 引用 1.0 的 nodes 都应进入 impact review。Impact analysis 不应自动重写它们。
""",
    )


def localize_control() -> None:
    write(
        "kb/_schema.yaml",
        yaml.safe_dump(
            {
                "schema": "kb.schema.v1",
                "generated_at": "2026-05-24T05:10:00+08:00",
                "language": "zh-CN",
                "contracts": {
                    "node_database": "nodes/ 是可维护 node version bundles 的 source of truth。",
                    "kb_view": "kb/ 只渲染 adopted versions。",
                    "generated": "generated/ 保存可重建的 citation graph、backlinks、impact queue 和 status。",
                    "version_bundle": ["node.yaml", "card.md", "provenance.md", "change.md"],
                    "required_card_sections": ["# Title", "## Footnotes", "## References"],
                    "required_citation_fields": [
                        "target",
                        "target_version",
                        "pinned_version",
                        "citation_role",
                        "why_cited",
                        "evidence_summary",
                    ],
                    "version_semantics": {
                        "minor": "核心含义和 support contract 仍成立，不触发 impact propagation。",
                        "major": "核心含义或 support contract 改变，下游 citation 需要 review。",
                    },
                },
            },
            sort_keys=False,
            allow_unicode=True,
            width=100,
        ),
    )
    write(
        ".llmwiki/control/principles.md",
        """# KB 初始化原则

1. 先保存 raw source，再进行 synthesis。
2. `nodes/` 是可维护知识对象数据库。
3. `kb/` 是 adopted version 的消费视图。
4. 每个 node version 都必须包含 `node.yaml`、`card.md`、`provenance.md`、`change.md`。
5. 具体 claim 用 footnote 支撑，背景/定义/过程语境用 reference 支撑。
6. Provenance 是知识对象本身的一部分，不是附录。
7. Major change 只创建 impact review tasks，不自动重写下游。
8. 动态检索必须先写 gap/request，再保存 raw source，再进入 provenance。
9. 每次 0-1 node run 都是 skill evaluation sample。
10. 公司电脑网络受限时，只做有限普通检索；被拦截就记录并延期到个人设备重试。
""",
    )
    write(
        ".llmwiki/control/autonomy.md",
        """# 自治 Loop 策略

created_at:: 2026-05-24T05:10:00+08:00
latest_run:: .llmwiki/runs/run_20260524_050634_major_impact_simulation

## 目的

这个 KB initialization loop 需要在人类离开电脑时仍能推进。Agent 应把状态落盘，选择边界清晰的下一步，并定期反思当前行动是否仍在降低核心不确定性。

## 可自治执行

- 运行 validators 和 builders。
- 基于已保存的本地 evidence 创建额外 0-1 nodes。
- 为 evidence gap 写 retrieval request。
- 在 request 已存在且 raw source 可保存时，做小范围动态检索。
- 模拟一个 major candidate 来测试 impact analysis。
- 当 run 暴露明确 failure mode 时，更新 skill seeds。
- 写 report、summary state 和 decision log。

## 必须停止或记录 blocker

- 破坏性 git 操作。
- 覆盖 KB 初始化范围以外的人类文件。
- 把 audit 失败的 version 当作 adopted。
- 没有 retrieval request 和 preservation plan 就扩展到大规模 web research。
- 改变核心 node/version/citation contract，导致已有 bundles 失效。

## 公司网络检索限制

当前是在公司电脑中运行，网页检索可能被拦截或限制。不要尝试绕过网络控制。只做有限的正常 retrieval attempts；如果被 blocked/intercepted，就保存响应、写入 `retrieval_log.yaml`，并把完整 retrieve 留到未来个人设备运行。

## 决策规则

每个暂停点只选择一个 next action：

1. 如果脚本或 validators 失败，选择 `repair_instrumentation`。
2. 如果 adopted node 少于 5 且 evidence 充足，选择 `iterate_node_batch`。
3. 如果 recorded evidence gap 阻塞有用 node，选择 `dynamic_retrieval_test`。
4. 如果 citation graph 已存在但 impact propagation 未测试，选择 `major_impact_test`。
5. 如果 run 暴露重复 skill failure，选择 `skill_reflection`。
6. 如果 acceptance criteria 基本满足，选择 `demo_report`。
""",
    )
    write(
        ".llmwiki/control/reflection_policy.md",
        """# 反思策略

## 反思频率

每个 run 完成后反思一次；每次 validation/build failure 后也反思一次。

## 反思问题

1. 最近一步是提高了 KB auditability，还是只是增加了内容？
2. 哪个假设失败了？
3. 这是 case-level 问题，还是 reusable skill failure？
4. 另一个 agent 是否能只凭磁盘状态恢复？
5. 下一步最高价值的单一 action 是什么？

## 必需输出

- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/decision_log.yaml`
- `.llmwiki/runs/<run_id>/skill_eval.md`
""",
    )
    write(
        ".llmwiki/control/state.md",
        """# KB 初始化状态

current_phase:: demo_complete_for_review
loop_owner:: main_owned_with_autonomous_reflection
latest_run:: .llmwiki/runs/run_20260524_050634_major_impact_simulation
last_updated:: 2026-05-24T05:10:00+08:00

## 当前决策

初始化 demo 已经达到 review 状态。公司电脑上的动态检索保持有限尝试；被 blocked/intercepted 的来源已保存并记录，后续在个人设备重新 retrieve。

## 下一步

先 review `generated/impact_queue.yaml`、`reports/kb_initialization_demo_report.md` 和 `.llmwiki/control/completion_audit.md`，再决定是否继续做 downstream revision。
""",
    )
    state = load_yaml(".llmwiki/control/state.yaml")
    state["current_phase"] = "demo_complete_for_review"
    state["latest_run"] = RUN_IMPACT
    state["last_updated"] = "2026-05-24T05:10:00+08:00"
    state["next_action"] = "review_impact_queue_or_prepare_next_iteration"
    state.setdefault("autonomy", {})["company_network_retrieval_policy"] = "limited_attempts_then_defer"
    write_yaml(".llmwiki/control/state.yaml", state)
    write(
        ".llmwiki/control/summary_state.md",
        """# Summary State / 摘要状态

current_phase:: demo_complete_for_review
latest_run:: .llmwiki/runs/run_20260524_050634_major_impact_simulation
last_completed_action:: major_impact_queue_generated
current_blocker:: none
human_checkpoint_needed:: no
recommended_next_action:: review_impact_queue_or_prepare_next_iteration

## 恢复说明

Demo acceptance state 已满足：7 个 adopted nodes、1 个成功动态检索案例、1 个保存的失败检索、1 个未 adopted major candidate、4 个 open impact queue entries。公司网络检索受限，不要做网络绕行；后续如果要补 blocked sources，应在个人设备重新 retrieve。恢复时先读 `reports/kb_initialization_demo_report.md`、`.llmwiki/control/completion_audit.md` 和 `generated/status.yaml`。
""",
    )
    write(
        ".llmwiki/control/standing_status.md",
        """# Standing Status / 低噪状态

state:: demo_complete_for_review
latest_run:: .llmwiki/runs/run_20260524_050634_major_impact_simulation
last_updated:: 2026-05-24T05:10:00+08:00
next_action:: review_impact_queue_or_prepare_next_iteration
blocker:: none
human_needed:: no
network_retrieval_policy:: limited_company_network_attempts_then_defer
""",
    )


def localize_runs_and_skills() -> None:
    agent_tasks = {
        "planner": "选择 loop 和本次 run target，写 run_plan，不直接写 card。",
        "generator": "在限定 evidence scope 内生成完整 version bundle；evidence 不足时先写 retrieval_request。",
        "audit": "检查 schema、citation、provenance、change 和 adoption readiness。",
        "eval": "评估本次 run 对 skill 的启发，区分 case-level observation 和 skill-level failure。",
    }
    for name, duty in agent_tasks.items():
        write(
            f".llmwiki/agents/{name}/task.md",
            f"""# {name} task

run_dir:: {RUN_IMPACT}

## 职责

{duty}

## 安全边界

你不是 repo 里唯一的执行者。不要 revert、overwrite 或清理无关文件。任何超出 scoped inputs 的读取都应记录理由。
""",
        )

    skills = {
        "node_bundle_generation": "创建完整 version bundle：node metadata、card、provenance 和 change notes。",
        "provenance_generation": "解释版本为什么存在、使用了哪些输入、为什么 synthesis 可被暂时采纳、如何审计、何时修订。",
        "citation_formatting": "写出可解析 footnotes/references，并包含 target、target_version、pinned_version、citation_role、why_cited、evidence_summary。",
        "citation_audit": "检查 citation 是否存在、是否 pin 到版本、why_cited 是否具体、是否过度支持 claim。",
        "dynamic_retrieval": "把 evidence gap 转化为 retrieval request，保存 retrieved raw source，更新 manifest，并写入 provenance。",
        "adoption_gate": "只有 bundle、citation、provenance 和 change notes 通过 audit 的 version 才能 adopted；major candidate 必须先 impact review。",
        "view_building": "把 adopted versions 渲染到 kb/，重建 index、citation graph、backlinks、impact queue 和 status。",
        "skill_eval": "用每个 0-1 node run 记录明确 skill failure，避免从一次性观察升级全局 skill。",
    }
    for name, desc in skills.items():
        write(
            f".llmwiki/skills/{name}/skill.md",
            f"""# {name}

status:: seed
created_at:: 2026-05-24T05:10:00+08:00
language:: zh-CN

## 目的

{desc}

## Demo 规则

优先减少明确 failure mode，而不是追求抽象意义上的“更好”。只有 completed run 暴露出可命名 failure mode，才升级 skill。
""",
        )

    run_files = {
        f"{RUN_BOOTSTRAP}/run_plan.md": """# Run Plan / 运行计划

run_id:: run_20260524_050031_kb_initialization_bootstrap
run_type:: bootstrap_plus_0_1_node_batch

## 目标

建立 KB 初始化所需的契约、控制层、脚本、skill seeds，并从已有本地 data 生成第一批 adopted 0-1 nodes。

## 目标 Nodes

- 20260524_050031_llm_wiki_working_definition
- 20260524_050032_current_kb_initialization_loop
- 20260524_050033_source_preservation_precondition_trust
- 20260524_050034_provenance_as_core_knowledge_asset
- 20260524_050035_citation_driven_impact_propagation
- 20260524_050036_dynamic_retrieval_as_controlled_fallback

## 固定范围

- 使用已有 `data/`、`reports/` 和 `loop_plan_init_kb.md`。
- 本 run 不执行外部 web retrieval。
- 每个 node 都以完整 1.0 version bundle 保存。
""",
        f"{RUN_BOOTSTRAP}/task.md": """# Task / 任务

创建 Phase 1 bootstrap contracts、data inventory、source candidates、skill seeds，以及第一批可审计 0-1 node bundle。
""",
        f"{RUN_BOOTSTRAP}/data_scope.md": """# Data Scope / 数据范围

允许输入：

- loop_plan_init_kb.md
- reports/coverage_framework.md
- reports/source_gap_review.md
- data/manifests/sources.jsonl
- data/manifests/source_digests.jsonl
- data/manifests/claims.jsonl
- data/manifests/claim_source_links.jsonl
- selected local raw source text under data/raw/

本 run 没有执行动态检索。
""",
        f"{RUN_BOOTSTRAP}/generator_trace.md": """# Generator Trace / 生成记录

从已有本地 artifacts 生成了 6 个 adopted 1.0 node bundles。每个 bundle 都包含 `node.yaml`、`card.md`、`provenance.md` 和 `change.md`。
""",
        f"{RUN_BOOTSTRAP}/provenance_trace.md": """# Provenance Trace / 溯源过程记录

生成器使用 repo-root relative citation paths，使 version card 复制到 `kb/` 后仍可解析。所有 nodes 都区分 source-backed observation、process decision 和 agent synthesis。
""",
        f"{RUN_BOOTSTRAP}/audit_report.md": """# Audit Report / 审计报告

audit_result:: passed

## 检查项

- 所有生成 nodes 的 version bundle 完整。
- `card.md` 包含 Footnotes 和 References。
- Footnotes/References 包含必需 citation fields。
- Provenance 包含输入、综合、审计、采纳和修订触发条件。
- Genesis change notes 存在。

## 残余风险

这是 bootstrap audit，重点检查结构和路径存在；还不是每个 claim 的深度语义 faithful audit。
""",
        f"{RUN_BOOTSTRAP}/skill_eval.md": """# Skill Eval / 技能评估

| 维度 | 分数 | 说明 |
| --- | ---: | --- |
| Schema compliance | 5 | Bundle contract 与 metadata 完整。 |
| Citation quality | 4 | Citation 可解析且已 pinned；深度语义 audit 待补。 |
| Provenance quality | 4 | 说明了 why、inputs、synthesis、audit、adoption 和 revision triggers。 |
| Evidence fit | 4 | 现有本地 evidence 足够支持 bootstrap nodes。 |
| Dynamic retrieval discipline | 4 | Evidence gap 已记录，实际 retrieval 延后到后续 run。 |

## 后续 skill 改进候选

- 增加 semantic citation-audit sampling。
- 增加 candidate-version validator mode。
""",
        f"{RUN_BOOTSTRAP}/git_trace.md": """# Git Trace / Git 记录

本 run 没有自动创建 git checkpoint。需要 checkpoint 时再由人或后续 agent 执行。
""",
        f"{RUN_BOOTSTRAP}/retrieval_request.md": """# Retrieval Request / 检索请求

run_id:: bootstrap_node_batch
target_node:: dynamic_retrieval_as_controlled_fallback
created_by:: audit
status:: completed_with_partial_failure

## 为什么现有 data 不足

本地 source gap review 记录了 blocked Reddit captures 和 intercepted enterprise article。这些是 community reception 与 enterprise suitability 的硬性 evidence gap。

## 缺失 evidence

- 可用的 community discussion evidence。
- 可替代 intercepted AICritique 页面的 enterprise evidence。

## Desired source types

- discussion_thread
- issue_thread
- blog_post
- enterprise_guide

## Acceptance criteria

- Raw source 必须保存。
- Source manifest 必须更新。
- Provenance 必须记录 retrieval。
- Retrieved evidence 必须被引用或明确拒绝。

## 公司网络说明

当前运行环境可能拦截网页。只做有限正常尝试；被拦截来源记录后，后续在个人设备重新 retrieve。
""",
        f"{RUN_RETRIEVAL}/run_plan.md": """# Run Plan / 运行计划

run_id:: run_20260524_050318_dynamic_retrieval_enterprise_scale
run_type:: dynamic_retrieval_0_1_node

## 目标

使用已经记录的 enterprise evidence gap 做一次受控动态检索，保存 raw evidence，并从成功检索来源创建一个 adopted node。
""",
        f"{RUN_RETRIEVAL}/data_scope.md": """# Data Scope / 数据范围

允许输入：

- bootstrap run 的 retrieval_request.md
- .llmwiki/control/retrieval_log.yaml
- data/raw/webpage/aicritique-enterprise-knowledge-dynamic-20260524/
- data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/
- data/manifests/sources.jsonl
- 被引用的 adopted KB nodes

AICritique 被公司网络拦截，保存但不作为 evidence。Atlan 来源保存成功，并用于 dynamic retrieval node。
""",
        f"{RUN_RETRIEVAL}/generator_trace.md": """# Generator Trace / 生成记录

生成一个 adopted 1.0 node：

- 20260524_050318_enterprise_scale_requires_governed_context_layer

该 card 使用 Atlan 动态来源支撑 enterprise-scale governance claim，并引用已有 KB nodes 作为定义、检索纪律和 source-preservation 背景。
""",
        f"{RUN_RETRIEVAL}/audit_report.md": """# Audit Report / 审计报告

audit_result:: passed

## 检查项

- 使用 source 前已有 retrieval request。
- AICritique 失败响应被保存并拒绝作为 evidence。
- Atlan 来源保存到 `data/raw/`。
- `data/manifests/sources.jsonl` 记录了两个动态检索尝试。
- Node version bundle 完整。
- Card 有 Footnotes 和 References。
- Provenance 区分 source evidence、失败尝试、synthesis 和 vendor bias。
""",
        f"{RUN_RETRIEVAL}/skill_eval.md": """# Skill Eval / 技能评估

| 维度 | 分数 | 说明 |
| --- | ---: | --- |
| Schema compliance | 5 | Version bundle 完整。 |
| Citation quality | 4 | Dynamic source 和 prior KB citations 均 pinned 且可解析。 |
| Provenance quality | 5 | 区分了失败与成功 retrieval。 |
| Evidence fit | 4 | Source 支持 enterprise framing，但它是 vendor-authored。 |
| Dynamic retrieval discipline | 5 | Request、raw preservation、manifest update、rejection、use 和 provenance 均已记录。 |
""",
        f"{RUN_RETRIEVAL}/git_trace.md": """# Git Trace / Git 记录

本 run 没有自动创建 git checkpoint。
""",
        f"{RUN_IMPACT}/run_plan.md": """# Run Plan / 运行计划

run_id:: run_20260524_050634_major_impact_simulation
run_type:: simulated_major_change_impact_test

## 目标

为 `20260524_050033_source_preservation_precondition_trust` 创建一个未 adopted 的 2.0 major candidate，并验证 citation graph 是否能生成 impact queue。

## 规则

不更新 root `node.yaml`，不把 candidate 渲染进 `kb/`。
""",
        f"{RUN_IMPACT}/audit_report.md": """# Audit Report / 审计报告

audit_result:: held_for_impact_review

## 检查项

- Candidate bundle 位于 `versions/2.0/`。
- Root node metadata 仍指向 adopted 1.0。
- Candidate `change.md` 标记 `change_scale:: major`。
- Candidate `change.md` 标记 `propagation_required:: true`。
- Adoption 被有意 hold。

## 预期结果

`scripts/kb_compute_impact.py` 应把引用 changed node 的下游 nodes 写入 `generated/impact_queue.yaml`。
""",
        f"{RUN_IMPACT}/skill_eval.md": """# Skill Eval / 技能评估

| 维度 | 分数 | 说明 |
| --- | ---: | --- |
| Schema compliance | 4 | Candidate bundle 存在；当前 validator 主要检查 adopted roots。 |
| Citation quality | 4 | Candidate citations 可解析且 pinned。 |
| Provenance quality | 4 | Provenance 清楚说明 simulation 和 non-adoption。 |
| Impact clarity | 5 | `change.md` 明确包含 major scale 与 propagation flag。 |

## 后续 skill 改进候选

- 增加 candidate-version validator mode。
- 增加 impact queue acceptance check。
""",
        f"{RUN_IMPACT}/git_trace.md": """# Git Trace / Git 记录

本 run 没有自动创建 git checkpoint。该 run 是 non-adopted impact simulation。
""",
    }
    for path, text in run_files.items():
        write(path, text)


def localize_reports() -> None:
    write(
        "reports/kb_initialization_demo_report.md",
        """# KB 初始化 Demo 报告

generated_at:: 2026-05-24T05:10:00+08:00
status:: complete_for_demo_scope
language:: zh-CN

## 摘要

KB initialization demo 已经形成一个 filesystem-backed、可审计、可恢复的 loop。当前产物包括 contracts、control files、scripts、skill seeds、data inventory、adopted nodes、generated views、动态检索记录，以及 major-change impact queue。

来自 `generated/status.yaml` 的当前计数：

- adopted_nodes: 7
- kb_view_cards: 7
- citation_edges: 35
- dynamic_retrieval ok_attempts: 1
- dynamic_retrieval failed_attempts: 1
- major_candidates: 1
- impact_queue_open: 4

## Artifact Map

Contracts 与 control：

- `kb/_schema.yaml`
- `.llmwiki/control/principles.md`
- `.llmwiki/control/state.md`
- `.llmwiki/control/autonomy.md`
- `.llmwiki/control/reflection_policy.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/decision_log.yaml`
- `.llmwiki/control/data_inventory.yaml`
- `.llmwiki/control/source_candidates.yaml`

Scripts：

- `scripts/kb_common.py`
- `scripts/kb_bootstrap_demo.py`
- `scripts/kb_build_index.py`
- `scripts/kb_build_view.py`
- `scripts/kb_validate_node.py`
- `scripts/kb_validate_card.py`
- `scripts/kb_parse_citations.py`
- `scripts/kb_compute_impact.py`
- `scripts/kb_status.py`
- `scripts/kb_git_checkpoint.sh`

Views 与 generated artifacts：

- `kb/_index.yaml`
- `kb/*.md`
- `generated/citation_graph.yaml`
- `generated/backlinks.yaml`
- `generated/impact_queue.yaml`
- `generated/status.yaml`

Run artifacts：

- `.llmwiki/runs/run_20260524_050031_kb_initialization_bootstrap/`
- `.llmwiki/runs/run_20260524_050318_dynamic_retrieval_enterprise_scale/`
- `.llmwiki/runs/run_20260524_050634_major_impact_simulation/`

## Adopted Nodes

- `20260524_050031_llm_wiki_working_definition`
- `20260524_050032_current_kb_initialization_loop`
- `20260524_050033_source_preservation_precondition_trust`
- `20260524_050034_provenance_as_core_knowledge_asset`
- `20260524_050035_citation_driven_impact_propagation`
- `20260524_050036_dynamic_retrieval_as_controlled_fallback`
- `20260524_050318_enterprise_scale_requires_governed_context_layer`

每个 adopted node 都有 root `node.yaml`、`versions/1.0/node.yaml`、`card.md`、`provenance.md`、`change.md`，并渲染为 `kb/<node_id>.md`。

## 动态检索

Bootstrap run 记录了 enterprise/community evidence gap。动态检索 run 保存了两个尝试：

- 失败但保存：`data/raw/webpage/aicritique-enterprise-knowledge-dynamic-20260524/`
- 成功并使用：`data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/`

成功来源被 adopted node `20260524_050318_enterprise_scale_requires_governed_context_layer` 使用。失败来源保留为非 evidence retrieval attempt。

当前运行在公司电脑上，网络拦截是预期限制。策略是有限正常尝试；blocked sources 记录并延期到个人设备重新 retrieve。

## Major Impact Test

Demo 包含一个未 adopted 的 2.0 candidate：

- `nodes/20260524_050033_source_preservation_precondition_trust/versions/2.0/`

其 `change.md` 标记：

- `change_scale:: major`
- `propagation_required:: true`

`generated/impact_queue.yaml` 包含 4 个 open impact entries，均来自 parsed citation edges。Candidate 没有进入 `kb/`，`kb/` 仍只渲染 adopted 1.0。

## 验证

已运行：

- `python3 -m py_compile ...`
- `python3 scripts/kb_validate_node.py --all`
- `python3 scripts/kb_validate_card.py --all`
- `python3 scripts/kb_parse_citations.py`
- `python3 scripts/kb_compute_impact.py`
- `python3 scripts/kb_status.py`

最新结果：

- node validation passed: 7 nodes
- card validation passed: 15 cards
- citation graph edges: 35
- impact queue open: 4

## 残余风险

- Citation validation 仍偏结构性：它检查 required fields 和路径存在，但只做了轻量 semantic faithfulness audit。
- Atlan 是 vendor-authored source，适合 enterprise framing，不适合作为独立 empirical validation。
- 公司网络可能拦截网页，blocked sources 应在个人设备重新 retrieve，而不是在公司网络中绕行。
- Candidate-version validation 仍是间接的：candidate card 可验证，impact computation 会读取 candidate `change.md`，但 `kb_validate_node.py` 主要检查 adopted root metadata。

## 下一步建议

- 增加 candidate-version validator mode。
- 增加 semantic citation-audit sampling。
- Review 4 个 impact queue entries，不自动重写下游 nodes。
""",
    )
    write(
        ".llmwiki/control/completion_audit.md",
        """# Completion Audit / 完成审计

generated_at:: 2026-05-24T05:10:00+08:00
audit_result:: passed
language:: zh-CN

## Requirement Evidence

| Requirement | Evidence | Status |
| --- | --- | --- |
| 阅读并执行 `loop_plan_init_kb.md` | 当前 contracts、scripts、nodes、views、dynamic retrieval 和 impact artifacts 都按计划结构落盘。 | passed |
| 建立文件契约 | `kb/_schema.yaml`、`nodes/` version bundles、`kb/` adopted view、`generated/` artifacts 已存在。 | passed |
| 建立 control layer | `.llmwiki/control/principles.md`、`state.md`、`state.yaml`、`action_queue.yaml`、autonomy/reflection files 已存在。 | passed |
| 添加 scripts | 计划中的 `scripts/kb_*.py`、checkpoint shell、bootstrap/localization helpers 均存在并可编译。 | passed |
| 添加 skill seeds | `.llmwiki/skills/*/skill.md` 中有 8 个 seed skills。 | passed |
| 盘点 existing data | `.llmwiki/control/data_inventory.yaml` 和 `source_candidates.yaml` 已从当前 manifests 生成。 | passed |
| 生成并 adopt 0-1 nodes | 7 个 adopted nodes 存在，每个都有完整 1.0 version bundle 和 root metadata。 | passed |
| 审计 nodes/cards | `kb_validate_node.py --all` passed；`kb_validate_card.py --all` passed。 | passed |
| 构建 KB view | `kb/_index.yaml` 和 7 张 `kb/*.md` cards 已从 adopted versions 生成。 | passed |
| 构建 generated artifacts | `citation_graph.yaml`、`backlinks.yaml`、`impact_queue.yaml`、`status.yaml` 已存在。 | passed |
| 记录 run/audit/skill eval | 三个 `.llmwiki/runs/*` 目录包含 run plans、audit reports 和 skill eval files。 | passed |
| 动态检索验证 | retrieval request/log 存在；一个失败来源和一个成功来源已保存；成功动态来源被 adopted node 使用。 | passed |
| 记录 evidence insufficient | bootstrap run 的 `retrieval_request.md` 记录了缺失 enterprise/community evidence。 | passed |
| Major/impact 验证 | 未 adopted 2.0 major candidate 存在；`generated/impact_queue.yaml` 有 4 个 open impacts。 | passed |
| 自治和反思 | `.llmwiki/control/autonomy.md`、`reflection_policy.md`、`summary_state.md`、`standing_status.md`、`decision_log.yaml` 定义了 out-of-loop continuation 和 reflection。 | passed |
| 中文主内容 | 人类可读 artifacts、node cards、provenance、change、run reports、skills 和 demo report 已重写为中文主内容；机器字段保留英文以维持解析。 | passed |
| 公司网络检索限制 | autonomy、retrieval_log 和 report 记录了有限尝试、失败保存、未来个人设备重新 retrieve 的策略。 | passed |

## Completion Decision

本次中文化重做已完成。剩余事项是质量改进建议，不阻塞 demo acceptance state。
""",
    )


def localize_misc_yaml() -> None:
    decision = load_yaml(".llmwiki/control/decision_log.yaml")
    decision["updated_at"] = "2026-05-24T05:10:00+08:00"
    decision["language"] = "zh-CN"
    for row in decision.get("decisions", []):
        if row["id"] == "dec_001":
            row["decision"] = "bootstrap 后继续自治执行"
            row["reason"] = "人类可能长时间离开；loop 已有边界明确的 validation、build、retrieval-request 和 impact-test action，可依据磁盘状态继续。"
        elif row["id"] == "dec_002":
            row["decision"] = "adopt 动态检索 node"
            row["reason"] = "retrieval request 已存在，失败来源已保存并拒绝，成功来源已保存并进入 manifest，node 只采纳窄范围可支持 claim。"
        elif row["id"] == "dec_003":
            row["decision"] = "hold major candidate 并接受 impact queue"
            row["reason"] = "2.0 candidate 有意不 adopted，impact queue 从 parsed citation edges 生成 4 个 downstream review tasks。"
    write_yaml(".llmwiki/control/decision_log.yaml", decision)

    queue = load_yaml(".llmwiki/control/action_queue.yaml")
    queue["updated_at"] = "2026-05-24T05:10:00+08:00"
    queue["language"] = "zh-CN"
    translations = {
        "bootstrap_contracts_scripts_and_skill_seeds": "bootstrap contracts、scripts 和 skill seeds",
        "generate_and_audit_first_0_1_node_batch": "生成并审计第一批 0-1 nodes",
        "run_dynamic_retrieval_test_for_recorded_evidence_gap": "针对已记录 evidence gap 执行动态检索测试",
        "simulate_major_change_and_compute_impact_queue": "模拟 major change 并生成 impact queue",
        "review_impact_queue_or_prepare_next_iteration": "review impact queue 或准备下一轮 iteration",
    }
    for row in queue.get("items", []):
        row["action"] = translations.get(row.get("action"), row.get("action"))
    write_yaml(".llmwiki/control/action_queue.yaml", queue)

    retrieval = load_yaml(".llmwiki/control/retrieval_log.yaml")
    retrieval["updated_at"] = "2026-05-24T05:10:00+08:00"
    retrieval["language"] = "zh-CN"
    for row in retrieval.get("requests", []):
        row["reason"] = "source_gap_review 记录了 blocked Reddit 和 intercepted enterprise source gaps。"
        row["policy"] = "在公司电脑上只做有限正常 retrieval；不要绕过网络控制。Blocked sources 未来在个人设备重新 retrieve。"
    write_yaml(".llmwiki/control/retrieval_log.yaml", retrieval)


def main() -> int:
    localize_nodes()
    localize_candidate()
    localize_control()
    localize_runs_and_skills()
    localize_reports()
    localize_misc_yaml()
    print("localized KB initialization demo artifacts to zh-CN")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
