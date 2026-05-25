# LLM Wiki 的 bounded origin/canon

这个节点记录的是一个有边界的 origin/canon：在当前语料批次内，LLM Wiki 的规范锚点是 Karpathy 的 `LLM Wiki` idea file；Hacker News 原始讨论串只能说明该 idea file 周围的早期公开讨论；本地 X capture 可作为 launch-context/source inventory，但不能支持采用率、生态成熟度、企业可用性或经验效果外推。这个节点因此不是完整思想史、不是采用率报告，也不是企业可用性或经验效果证明。[^1][^2][^3]

**来源支持的观察。** Karpathy 的 idea file 把 LLM Wiki 描述为一种用 LLM 构建个人知识库的模式，并明确说它是可交给 LLM agent 的 high-level idea file，而不是某个固定实现。它的核心区别不是“有没有 retrieval”，而是让 LLM 在 raw sources 与用户查询之间持续维护一个持久的 markdown/wiki 中间层：新来源进入后，LLM 读取、抽取、整合、更新相关页面，并把矛盾或新综合写回 wiki。[^1]

**工作定义。** 在这个 bounded canon 中，可以把 LLM Wiki 暂定为：一个保留 raw sources、由 LLM 编译并持续维护、受 schema/instructions 约束的持久知识层。这个定义是从 gist 的结构化描述中归纳出来的工作定义，不应被读作项目内已经完成的通用定义节点；后续 working definition 节点仍需要独立生成和审计。[^1]

**三层结构。** Gist 给出的 canonical structure 是三层：第一层是不可变 raw sources，作为来源真值；第二层是 LLM 生成和维护的 markdown wiki，包含摘要、实体页、概念页、比较、概览与综合；第三层是 schema/instructions 文档，用来约束目录结构、约定和 ingest/query/maintenance 流程。这个三层结构支持把 LLM Wiki 区分为“源材料保留 + 生成性知识层 + 操作规约”的系统，而不是单纯的聊天记录或一次性文件上传。[^1]

**核心操作。** Gist 明确列出三类操作：`ingest`、`query`、`lint`。`ingest` 把新来源纳入 raw collection，并更新 wiki 中相关页面、索引和日志；`query` 让 LLM 基于 wiki 搜索与综合回答，且有价值的回答可以被写回 wiki；`lint` 是周期性健康检查，用来发现矛盾、过时声明、孤立页面、缺失概念和可继续检索的数据缺口。这里的解释仍局限于 gist 所描述的 intended workflow，不能推出它在大规模或企业环境下已经有效。[^1]

**导航与日志。** Gist 把 `index.md` 与 `log.md` 分成两种导航支架：`index.md` 是内容导向的 catalog，帮助人和 LLM 找到 wiki 页面；`log.md` 是时间顺序的追加记录，帮助追踪 ingest、query 和 lint pass。Gist 还把本地 markdown 搜索、BM25/vector hybrid search、MCP、Obsidian、Marp、Dataview 等放在 optional/modular tooling 的位置，因此首版 canon 不能把这些工具写成必要条件。[^1]

**早期讨论记录。** HN capture 和 `item.json` 显示该条目标题为 `LLM Wiki - example of an "idea file"`，story by `tamnd`，结构化 story metadata 包含 `score: 296`、`descendants: 95`、gist URL 和 X/XCancel 链接。讨论里很快出现了两类相反读法：一类把它归入 RAG、assistant memory 或既有 PKM/wiki 系统；另一类强调它的 write/maintenance loop、backlinks、source files 和 linting，使它不只是静态 retrieval corpus。这些是早期 discourse notes，不是本节点用来裁定“到底是不是 RAG”的最终比较结论。[^2]

**早期风险语汇。** HN 讨论还出现了 model collapse、二阶信息、过时或过度概括的声明、context bloat、质量保证、维护规模，以及把写作和思考外包给 LLM 的担忧。这个节点只把它们记录为后续 risk/governance/provenance 节点的早期话题种子；它们不能替代风险文献、治理框架或经验评估。[^2]

**证据边界。** 当前 X source raw files 与 HN `item.json` 在本地 checkout 中有内容；早前 process artifacts 把它们说成空文件是本轮修复记录的流程失败。X capture 可支持 bounded launch context/source inventory，HN `item.json` 可支持结构化 story metadata；但更大的历史谱系、社区采用、实现生态、企业适用性和经验效果都需要另行 source mining。HN 讨论仍只作为 discourse，不作为技术证明。[^3][^4][^5]

## References

### [R1] Karpathy LLM Wiki idea file

target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
target_version: raw_snapshot
pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
citation_role: primary_canonical_source
why_cited: Provides the direct source for the node's canonical pattern, architecture, workflow, indexing/logging, optional tooling, and implementation-boundary claims.
evidence_summary: The source is the readable local gist text for the LLM Wiki idea file.

### [R2] Hacker News original thread capture

target: data/raw/hacker_news/hacker-news-original-thread/text.txt
target_version: raw_snapshot
pinned_version: data/raw/hacker_news/hacker-news-original-thread/text.txt
citation_role: secondary_discourse_source
why_cited: Provides immediate public-discussion evidence without promoting HN comments into authoritative technical conclusions.
evidence_summary: The source contains the captured HN story text, visible story metadata, links, and comments around RAG comparison, writeback, maintenance, and risks.

### [R3] Evidence scope for origin/canon planning

target: .llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/evidence_scope.yaml
target_version: process_snapshot
pinned_version: .llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/evidence_scope.yaml
citation_role: process_boundary
why_cited: Records the earlier planning boundary for this candidate, including overclaim prohibitions that still apply.
evidence_summary: The process artifact enumerates allowed primary and secondary evidence and lists forbidden claims; its empty-file basis for the X inventory boundary is superseded by the repair report.

### [R4] Repair report for false empty-file claim

target: .llmwiki/runs/run_20260524_065000_worker_repair_origin_canon/repair_report.md
target_version: process_snapshot
pinned_version: .llmwiki/runs/run_20260524_065000_worker_repair_origin_canon/repair_report.md
citation_role: repair_process_source
why_cited: Supersedes the stale empty-file boundary with verified current local file state.
evidence_summary: The report records that the X launch files and HN item JSON are present and non-empty, and that use remains bounded to launch context, source inventory, and HN story metadata/discourse.

## Footnotes

[^1]:
    target: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
    citation_role: primary_canonical_evidence
    why_cited: Supports the bounded canonical description of LLM Wiki as an idea file with a persistent wiki layer, three-layer architecture, ingest/query/lint operations, index/log navigation, and optional tooling.
    evidence_summary: The gist describes LLM Wiki as a pattern for LLM-built personal knowledge bases, gives raw sources/wiki/schema layers, names ingest/query/lint, explains index.md and log.md, and frames implementation details as abstract and modular.

[^2]:
    target: data/raw/hacker_news/hacker-news-original-thread/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/hacker_news/hacker-news-original-thread/text.txt
    citation_role: early_discourse_evidence
    why_cited: Supports only the observed early public discussion around the idea file, including visible story metadata, RAG comparison debate, support, skepticism, and risk/maintenance concerns.
    evidence_summary: The HN text includes the story title, visible points/comment count/byline, links to gist and X mirrors, and comments discussing RAG, writeback, raw-source discipline, staleness, scale, and cognitive offloading concerns.

[^3]:
    target: .llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/evidence_scope.yaml
    target_version: process_snapshot
    pinned_version: .llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon/evidence_scope.yaml
    citation_role: evidence_boundary
    why_cited: Defines which sources may support this candidate and forbids X-specific wording, broad adoption, historical lineage, enterprise, and empirical-effectiveness claims.
    evidence_summary: The evidence scope marks the gist as primary evidence and HN as secondary early-discourse evidence, but its empty-file characterization of X/HN JSON was later found false and is superseded by the repair report.

[^4]:
    target: .llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/evidence_gaps.md
    target_version: process_snapshot
    pinned_version: .llmwiki/runs/run_20260524_062000_worker_source_mining_origin_canon/evidence_gaps.md
    citation_role: gap_record
    why_cited: Records non-blocking gaps that must remain visible in this first version and retrieval blockers for broader future claims.
    evidence_summary: The gap record documents the earlier boundary decision, but its empty-file statement for X raw files and HN item JSON was later found false; remaining broader gaps include historical lineage, ecosystem/adoption, empirical, governance, Reddit, and enterprise claims.

[^5]:
    target: .llmwiki/runs/run_20260524_065000_worker_repair_origin_canon/repair_report.md
    target_version: process_snapshot
    pinned_version: .llmwiki/runs/run_20260524_065000_worker_repair_origin_canon/repair_report.md
    citation_role: repair_boundary
    why_cited: Records the local file-size/content verification that supersedes the false empty-file claims in earlier source-mining and planning artifacts.
    evidence_summary: The repair report states that X text/raw/raw.json and HN item.json are non-empty in the current checkout, corrects the evidence boundary, preserves candidate_pending_audit, and records the process failure.
