# LLM Wiki 是由来源支撑、由 agent 维护的持久 wiki artifact

在这个 KB initialization demo 中，LLM Wiki 指的是一种持久知识系统：raw sources 先被保存为不可随意改写的 evidence layer，agent 再从这些来源编译和维护 markdown wiki，schema/control rules 则让 wiki 可检查、可引用、可修订。[^1]

本地证据也支持把 LLM Wiki 理解为一种 maintenance architecture，而不是单次 query-time retrieval：source capture、readable extraction、digest/compile、claim mapping、report update、lint/audit 和 human review 都是反复出现的流程元素。[^2]

这个定义是 operational definition，不是宇宙真理。它服务于 node generation、citation audit 和后续 revision；它不要求所有实现都采用相同 graph model、storage engine、interface 或 evaluation method。[^3]

## Footnotes

[^1]:
    target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    target_version: source_snapshot_2026-05-21
    pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    citation_role: primary_source
    why_cited: 支持 LLM Wiki 工作定义：在 immutable raw sources 与用户查询之间维护一个 agent 生成的持久 wiki。
    evidence_summary: Karpathy gist 描述了 raw sources、wiki、schema 三层，以及 ingest、query、lint 等操作。
    source_path: data/raw/gist_raw/karpathy-gist-llm-wiki

[^2]:
    target: reports/source_gap_review.md
    target_version: source_snapshot_2026-05-21
    pinned_version: reports/source_gap_review.md
    citation_role: evidence_inventory
    why_cited: 该报告总结了本地 raw corpus、覆盖状态和硬性 evidence gap。
    evidence_summary: 报告记录了 origin/workflow/implementation 证据，也记录了 Reddit 与 AICritique 等受阻来源。

[^3]:
    target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    target_version: source_snapshot_2026-05-21
    pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    citation_role: implementation_source
    why_cited: 支持把 LLM Wiki 理解为 compile-and-maintain 工作流，而不只是查询时检索。
    evidence_summary: README 描述了把 raw sources 编译成 interlinked markdown wiki，并提供 ingest、compile、query、view 等命令。
    source_path: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo

## References

### [R1] 初始化计划
    target: loop_plan_init_kb.md
    target_version: plan_snapshot_2026-05-24
    pinned_version: loop_plan_init_kb.md
    citation_role: process_contract
    why_cited: 该文件定义了本 demo 的初始化 loop、version bundle、provenance、citation、adoption 与 impact 规则。
    evidence_summary: 计划明确要求 nodes 是版本化知识对象库，kb/ 是 adopted view，citation 驱动 impact，动态检索必须受控并沉淀为 data asset。

### [R2] Claim manifest
    target: data/manifests/claims.jsonl
    target_version: source_snapshot_2026-05-21
    pinned_version: data/manifests/claims.jsonl
    citation_role: claim_manifest
    why_cited: 该 manifest 提供采集阶段生成的 source-linked claim records。
    evidence_summary: 记录包含 claim、coverage area、confidence 和 supporting sources，是从 raw data 进入 KB 的中间证据层。
