# Source Gap Review

Date: 2026-05-21

Scope: evidence audit of the locally acquired LLM Wiki raw knowledge database. This review uses only repo-local materials and does not extend acquisition beyond the downloaded corpus.

## Existing Evidence Summary

### Acquisition Manifests and Status

- `data/manifests/sources.jsonl` records 45 seed acquisitions: 38 successful, 6 Reddit blocked, and 1 webpage HTTP/intercept failure. It is the strongest source for acquisition provenance, status, priority, tags, local paths, and failure modes.
- `data/manifests/acquired_sources_index.md` gives a human-readable inventory by source type and local directory.
- `reports/acquisition_status.md` summarizes the snapshot: 162 MB raw data, 2,765 raw files, 15 GitHub repositories cloned, 3 arXiv entries, 2 extracted TeX/source bundles, 1 PDF-only arXiv source, plus known blocked Reddit and AICritique gaps.

### Origin and Definition Materials

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` is the cleanest origin artifact. It defines the LLM Wiki as a persistent, LLM-maintained, interlinked markdown wiki that sits between immutable raw sources and user queries. It names the three layers: raw sources, wiki, and schema; and the core operations: ingest, query, lint.
- `data/raw/webpage/karpathy-x-launch-post/raw.json` preserves the viral X launch post and quoted original "LLM Knowledge Bases" post. It adds adoption context and quantitative social signals from the mirror: millions of views, high bookmark/like counts, and the original claim that Karpathy's own recent research wiki reached roughly 100 articles and 400K words.
- `data/raw/hacker_news/hacker-news-original-thread/item.json` and `data/raw/hacker_news/hacker-news-original-thread/text.txt` preserve the HN discussion around the gist: 296 points, 95 comments, and a mix of support, skepticism, RAG-comparison arguments, model-collapse concerns, scale concerns, and reports from adjacent personal workflows.
- `data/raw/webpage/hacker-news-lens-thread/text.txt` and `data/raw/webpage/marvin-hn-persistent-knowledge/text.txt` provide mirror/summary coverage of the same HN event.

### Web Explainers, Guides, Directories, and Case Narratives

- `data/raw/webpage/aillm-wiki-directory/text.txt` frames the pattern for non-hackers and positions it as markdown-first, LLM-maintained, token-efficient, and template-driven.
- `data/raw/webpage/anthemcreation-en-guide/text.txt` and `data/raw/webpage/anthemcreation-fr-guide/text.txt` are multilingual explainers for Claude + Obsidian setup, cost claims, and LLM Wiki vs RAG framing.
- `data/raw/webpage/developersio-jp-pattern/text.txt` is a Japanese practitioner interpretation that treats Karpathy's post as naming and structuring practices already emerging around Claude Code, agent rules, Notion, and Obsidian.
- `data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt` is a concise wiki-style concept page. It usefully states scale limits and risks: about 200 pages / 100K tokens as a likely ceiling for pure index-reading, fragile deduplication, weak temporal modeling, and single-user assumptions.
- `data/raw/webpage/openaitoolshub-six-months/text.txt` is a practitioner narrative claiming six months of use across 35 pages and 80 raw articles. It emphasizes schema importance, lifecycle frontmatter, typed relationships, contradiction protocols, and pitfalls not covered by the origin gist.
- `data/raw/webpage/falconer-enterprise-guide/text.txt`, `data/raw/webpage/complete-tech-live-frontier/text.txt`, and `data/raw/webpage/cognitionus-llm-wiki-guide/text.txt` broaden the enterprise/team-memory context, although some are more marketing/product narrative than primary evidence.
- `data/raw/webpage/obsidian-community-plugin/text.txt` and `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` show plugin directory/listing evidence. ClawHub is especially useful for runtime capability claims: CLI, MCP server, OpenClaw compatibility, multimodal raw kinds, representation storage, source-id repair, compile-readiness tracking, gap mapping, and deterministic lint.

### Package Registry Evidence

- `data/raw/pypi/pypi-my-llm-wiki/text.txt` records `my-llm-wiki` 0.9.0, released 2026-04-28, as a beta Python package for turning folders into queryable knowledge graphs.
- `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` records `llm-wiki-mcp` 0.1.1, released 2026-04-08, as an alpha MCP server plus Claude Code skills for Karpathy-style LLM wikis.
- These pages support ecosystem existence, package metadata, license tags, Python version requirements, and maturity labels. They do not by themselves prove usage volume or quality.

### GitHub Repository Evidence

The repo clones are rich evidence for implementation patterns. As of the updated local corpus, the 15 `data/raw/github_repo/*/github_repo.json` files also contain usable GitHub API metadata rather than the earlier rate-limit placeholders. The `README.remote` captures may still show rate-limit text, so implementation evidence should come from local cloned files, especially `repo/README.md`, while adoption metadata should come from `github_repo.json`.

Across the 15 acquired repos, current metadata shows roughly 25.5K total stars, 3.1K total forks, and 181 open issues. The largest locally captured repos by stars are `nashsu/llm_wiki` (8,658), `AgriciDaniel/claude-obsidian` (5,296), `SamurAIGPT/llm-wiki-agent` (2,697), `VectifyAI/OpenKB` (1,879), and `sdyckjq-lab/llm-wiki-skill` (1,589). Many repos show pushes or updates in May 2026, supporting evidence of rapid post-Karpathy implementation activity.

- `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` describes a cross-platform desktop app with two-step ingest, multimodal image ingestion, graph relevance signals, Louvain clustering, vector semantic search, persistent queue, auto-watch, deep research, async review, web clipper, and local HTTP API.
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` describes an agent skill with raw/wiki/index/log/overview/sources/entities/concepts/syntheses, graph visualization, contradiction flags, lint reports, and support for multiple document formats via conversion.
- `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` provides a Chinese/multiplatform skill implementation with graph UX, confidence labels, cache, conversation crystallization, hooks, reports, comparison tables, and timeline outputs.
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` is one of the strongest engineering sources. It documents an npm CLI/MCP compiler with ingest, compile, query, view, lint, watch, review candidates, paragraph-level source markers, source-range citations, confidence/contradiction metadata, per-concept prompt budgets, chunked retrieval/reranking, and an explicit roadmap calling for an evaluation harness.
- `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` documents a Claude + Obsidian knowledge companion with skills, hot cache, lint, multi-agent support, DragonScale Memory, and comparison against Obsidian AI plugins.
- `data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md` documents a cross-agent Obsidian wiki framework and extensive agent compatibility.
- `data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md` packages the idea as an Agent Skills-compatible skill and claims a production knowledge base with 94 wiki articles, 99 sources, and recent operation logs.
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` is useful for local-first implementation evidence: Ollama/OpenAI-compatible providers, incremental compiles, file watcher, rejection feedback, hand-edit preservation, query/save, lint/maintain, no-vector mode up to about 100 source notes, and maintenance-mode caveat.
- `data/raw/github_repo/repo-ndjordjevic-pin-llm-wiki/repo/README.md` gives a clean source queue workflow with `inbox.md`, immutable raw captures, cited wiki pages, generated `AGENTS.md`, soft delete/archive, and explicit limits: reviewable workflow, not unattended publishing; contradiction checks deferred in phase 1.
- `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md` is adjacent but relevant: local MCP server for markdown vaults with trigram search, graph traversal, auto-wikilinks, community detection, D3 graph view, and no telemetry.
- `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` shows a more advanced OpenKB implementation with PageIndex for long PDFs, short vs long document handling, MarkItDown conversion, multimodality, wiki foundation, query/chat generators, and skill factory.
- `data/raw/github_repo/repo-ss1024ss-llm-wiki/repo/README.md` provides a pragmatic bootstrap/playbook view: compile-first, writeback mandatory, wiki-before-RAG under roughly 100 docs or 80K tokens, Obsidian optional, and tests/scripts for bootstrapping.

### Research Grounding

- `data/raw/arxiv/arxiv-knowledge-compounding/text.txt` is an economics/ROI paper claiming a controlled four-query experiment: 47K tokens under a compounding regime vs 305K under a matched RAG baseline, or 84.6% savings, plus 30-day projections. However, its arXiv source is PDF-only in this corpus: `data/raw/arxiv/arxiv-knowledge-compounding/metadata.json`.
- `data/raw/arxiv/arxiv-memory-as-metabolism/text.txt` and `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` provide a theory/governance paper situating LLM Wiki among personal wiki-style memory architectures and memory literature. It foregrounds entrenchment, user-coupled drift, memory gravity, minority-hypothesis retention, TRIAGE/DECAY/CONTEXTUALIZE/CONSOLIDATE/AUDIT, and the limits of single-agent safety.
- `data/raw/arxiv/arxiv-wicer/text.txt` and `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` are the strongest empirical evidence. WiCER evaluates wiki-memory compilation on RepLiQA domains, compares full-context KV cache inference and RAG, reports blind compilation failure rates, proposes iterative evaluation/refinement, and states limitations: Apple M4 Pro only, Llama 3.1 8B only, fixed RAG baseline, partial WiCER validation, and LLM-as-judge concerns.

### Community Discourse and Blocked Sources

- HN is covered via `data/raw/hacker_news/hacker-news-original-thread/text.txt`, with useful skeptical and supportive arguments.
- Reddit is not substantively covered. Each `data/raw/reddit/*/metadata.json` has `blocked: true`, and `browser_text.txt` / `text.txt` largely contain the Reddit network-security block message. This is a hard evidence gap for community adoption, criticism, plugin reception, long-PDF discussion, BrainDB/database framing, OpenWebUI discussion, and multimodal/PDF/PPT handling questions.
- `data/raw/webpage/aicritique-enterprise-knowledge/text.txt` contains only "域名拦截"; `data/raw/webpage/aicritique-enterprise-knowledge/metadata.json` marks the acquisition as an HTTP/intercept failure. This is a hard gap for the enterprise-knowledge angle.

## Coverage Against First Principles

### origin/definition

Coverage: strong.

The Karpathy gist, X mirror, HN thread, and multiple secondary explainers provide a stable definition: immutable raw sources, LLM-authored wiki, schema/instructions, index/log, ingest/query/lint, and compounding writeback. The corpus is enough to describe the pattern and distinguish its intended novelty from ordinary note-taking or one-shot RAG.

Remaining weakness: exact historical precedence is not well established. Some sources claim the core idea predates the viral gist, but the corpus lacks a systematic pre-April-2026 history of similar systems.

### workflow architecture

Coverage: strong.

The gist, repo READMEs, ClawHub listing, and OpenKB README cover raw/wiki/schema, source queues, compile pipelines, review queues, source summaries, entity/concept/synthesis pages, graph views, hot caches, watch mode, writeback, lint, and saved query outputs.

Remaining weakness: there is no neutral architecture taxonomy. Most implementation evidence comes from project authors describing their own systems.

### source ingestion

Coverage: good.

Sources cover manual source drop, URL ingest, web clipper, PDFs, Markdown, DOCX/PPTX/XLSX via converters, images, structured data, YouTube transcripts, long PDF handling, PageIndex-style tree summaries, SHA256 caching, source manifests, and queue/retry/watch workflows.

Remaining weakness: ingestion quality is asserted more than measured. The corpus lacks systematic tests of extraction fidelity across PDFs, images, PowerPoints, websites, tables, scans, and multilingual sources.

### compilation/maintenance

Coverage: strong for mechanisms; medium for reliability.

Evidence covers incremental compile, concept extraction, two-phase pipelines, per-concept budgets, candidate review, hand-edit preservation, rejection feedback, lifecycle fields, contradiction metadata, stale claim checks, gap mapping, lint, and archive lifecycle.

Missing: independent evidence that these maintenance mechanisms remain coherent at scale and under repeated updates.

### retrieval/query

Coverage: good.

Evidence covers index-first query, grep/trigram search, optional vector search, hybrid search, graph traversal, chunked retrieval/reranking, MCP tools, saved answers, and full-context/KV-cache comparisons in WiCER.

Missing: robust retrieval-quality comparison across corpora and query types. HN skepticism also highlights ambiguity over whether this is "just RAG" or a distinct retrieval-plus-writeback architecture.

### evaluation/quality

Coverage: medium.

WiCER provides the strongest benchmark-style evidence, including catastrophic compilation failure rates and a refinement algorithm. Atomicstrata explicitly lists evaluation harnesses as future work, and several repos include lint/health checks. The HN thread surfaces concerns about model collapse, drift, stale claims, and N-squared contradiction checking.

Missing: independent replication, broader model/provider tests, statistical significance, long-term drift measurement, citation accuracy audits, and human expert evaluation.

### UX/tooling/ecosystem

Coverage: strong.

The corpus includes desktop apps, CLI tools, MCP servers, Codex/Claude/OpenCode/OpenClaw plugins, Obsidian vault workflows, graph viewers, D3/vis.js visualizations, web clippers, PyPI packages, and skill packages. It is enough to write a credible ecosystem landscape.

Missing: GitHub stars/forks/issues and activity metadata are now available, but deeper adoption metrics are still weak: package downloads, plugin installs, active-user counts, issue/PR outcome analysis, and real deployment reports are not present locally.

### empirical outcomes

Coverage: weak to medium.

Available outcomes include Karpathy's anecdotal 100 articles / 400K words, HN popularity, OpenAIToolsHub's claimed six-month 35-page setup, Astro-Han's claimed 94 articles / 99 sources, arXiv Knowledge Compounding's token-savings claim, and WiCER's benchmark claims.

Missing: most outcomes are author-reported, small, not independently reproduced, or not tied to released raw experimental logs in this corpus.

### comparison with RAG/PKM/agent memory

Coverage: medium to strong conceptually.

The gist, repo READMEs, HN discussion, Robin Cartier page, Memory as Metabolism, and WiCER all compare the pattern to RAG, PKM, Obsidian-style note systems, agent memory, and lab/product memory systems. Strong themes: RAG retrieves from raw chunks at query time; LLM Wiki compiles and maintains a structured artifact; the systems may be complementary.

Missing: rigorous comparison with production RAG, graph RAG, agent memory frameworks, MemGPT/Mem0/Zep/A-Mem/MemOS, and enterprise knowledge-management systems.

### risks/governance

Coverage: medium.

Memory as Metabolism is the strongest governance source, with user-coupled drift, entrenchment, minority-hypothesis retention, decay, audit, and conformance invariants. HN provides real criticism around slop, subtle errors, cognitive offloading, stale claims, and complexity debt. Implementation docs provide mitigation mechanisms: citations, confidence labels, contradiction fields, review queues, hand-edit protection, archive lifecycle, lint.

Missing: privacy/security, access control, multi-user governance, audit trails, legal/compliance, poisoning, prompt injection, source licensing, and institutional review are under-covered.

### adoption/community discourse

Coverage: medium.

The corpus supports a claim that the idea triggered rapid implementation activity across GitHub repos, PyPI packages, plugin listings, and HN discussion. GitHub metadata now provides concrete traction signals for the acquired repos: stars, forks, open issues, creation dates, update times, pushed times, languages, and licenses. However, broader community discourse remains incomplete because Reddit is blocked, package downloads are absent, and directory/plugin pages often lack usage counts.

### research grounding

Coverage: medium.

Three arXiv entries anchor the research side: economic ROI/knowledge compounding, memory governance, and WiCER evaluation/refinement. The HN thread also points to broader concerns like model collapse and older human-computer symbiosis lineage.

Missing: literature review remains incomplete. The corpus lacks the full chain of primary sources for RAG, long-context degradation, graph RAG, memory systems, PKM/HCI, cognitive offloading, and knowledge-base maintenance.

## Missing Evidence

1. Reddit community discourse is missing. The blocked Reddit sources are not usable beyond their titles and block metadata. This matters because the blocked URLs map exactly to practical reception: Claude Code plugin feedback, OpenKB long-PDF claims, BrainDB/database framing, OpenWebUI integration, Obsidian plugin reception, and questions about visuals/PDFs/PowerPoints.

2. AICritique enterprise article is missing. `data/raw/webpage/aicritique-enterprise-knowledge/text.txt` contains only an intercept message. This matters because enterprise suitability is one of the largest claims in the discourse, and current enterprise evidence is mostly vendor/blog/product narrative.

3. GitHub metadata is improved but still incomplete for adoption analysis. The refreshed `github_repo.json` files now provide stars, forks, open issues, language, license, and activity timestamps for all 15 repos. This materially improves ecosystem/adoption evidence. Remaining gaps: contributors, traffic/clones, issue/PR content analysis, release history, dependency/security posture, and whether stars reflect actual usage.

4. Independent empirical validation is thin. WiCER is promising, but the current evidence base does not include independent replications, full experimental logs, multiple model families, broader RAG baselines, human expert grading, or statistical significance strong enough for a solid paper.

5. Longitudinal maintenance evidence is mostly anecdotal. The core claim is compounding over time, but the corpus lacks month-by-month diffs, drift curves, stale-claim rates, contradiction resolution histories, or controlled comparisons of maintained vs unmaintained wikis.

6. Scale boundaries are under-evidenced. Sources mention likely ranges such as 35 pages, 94 pages, 100 sources, 200 pages, 500 pages, 100K tokens, 400K words, and long PDF tree indexing. These are not yet reconciled into a measured scale curve by corpus size, page count, index size, source diversity, and model context window.

7. Citation/provenance accuracy is not audited. Many implementations support citations, source ranges, frontmatter source lists, confidence fields, and paragraph markers, but the corpus lacks measured citation precision/recall and source-faithfulness audits.

8. Multimodal ingestion remains claim-heavy. Several projects claim image/PDF/PPT/multimodal handling, but the missing Reddit multimodal thread and lack of benchmark evidence mean this area is not solid.

9. Governance and risk coverage is incomplete. Memory as Metabolism provides a strong conceptual frame, but there is not enough evidence on privacy, access control, data deletion, poisoning, source licensing, security, enterprise auditability, and team conflict resolution.

10. Comparison space is incomplete. The corpus has repeated "LLM Wiki vs RAG" framing, but not enough primary evidence on modern RAG, graph RAG, long-context full-read systems, agent memory products, PKM systems, or knowledge-graph/semantic-layer alternatives.

11. Negative cases and failures are sparse. HN has skepticism and Kytmanov notes maintenance mode, but there is no collected set of abandoned repos, failed deployments, bad compiles, duplicate-page drift, or user reports of harm.

12. Economic claims need stronger raw support. The Knowledge Compounding paper claims large token savings, but this local acquisition only has arXiv text and a PDF-only e-print, not a convenient TeX/source bundle or independent reproduction.

## Further Acquisition Priorities

### P0

- Recover blocked Reddit threads through an approved export path or manual capture: `reddit-claudecode-plugin`, `reddit-openkb-long-pdf`, `reddit-braindb`, `reddit-openwebui-llm-wiki`, `reddit-obsidian-plugin`, and `reddit-visuals-pdfs-question`.
- Recover the AICritique enterprise article body or replace it with another primary enterprise deployment/case-study source.
- Extend GitHub evidence beyond the refreshed repo metadata: contributors, commit history, releases, issue/PR content, topics, dependency manifests, CI status, and representative user reports.
- Acquire or extract full reproducibility artifacts for WiCER and Knowledge Compounding: benchmark code, data, scripts, raw logs, evaluation prompts, and exact baselines.
- Build a primary-source comparison set for RAG, graph RAG, long-context degradation, MemGPT/Mem0/Zep/A-Mem/MemOS, and agent memory governance.

### P1

- Gather independent user reports and failed/abandoned examples, not only polished READMEs and launch posts.
- Collect package registry usage indicators: PyPI release history, download counts if available locally in future acquisition, changelogs, dependencies, and security notes.
- Acquire Obsidian/community/plugin forum details beyond minimal plugin pages, including reviews, install counts if available, and issue discussions.
- Sample representative implementation internals from cloned repos without reading all source: schema files, test coverage, lint rules, citation validators, ingestion modules, and evaluation scripts.
- Add enterprise/team governance evidence: access control, audit logs, source permissions, retention/deletion, human review workflows, and compliance.
- Add multimodal benchmark evidence for PDFs, images, slides, tables, screenshots, and diagrams.

### P2

- Map the idea's pre-Karpathy lineage: Memex, Licklider, zettelkasten, wikis, Obsidian/PKM, semantic wikis, literate programming, knowledge compilation, and AI-agent memory.
- Acquire multilingual adoption evidence from Japanese, French, Chinese, and other language communities.
- Track ecosystem taxonomy over time: desktop app, CLI compiler, MCP server, Codex/Claude plugin, Obsidian plugin, local-first runtime, enterprise/team memory.
- Collect pricing/cost data across models and local/cloud runtimes.
- Acquire examples of generated wikis with raw sources and diffs so compounding behavior can be inspected directly.

## Final Recommendation

The current corpus is enough to write a solid preliminary landscape memo. It can confidently describe the LLM Wiki pattern, its origin story, core architecture, workflow variants, emerging tools, implementation motifs, common claims, and known skepticism.

The current corpus is not enough to write a solid paper that makes strong empirical, economic, enterprise, or durable adoption claims. For a solid paper, the next pass must close the Reddit and AICritique gaps, deepen GitHub evidence beyond surface metadata, add independent empirical replication, audit citation/maintenance quality, cover modern comparison baselines, and gather negative cases.

Best current claim: LLM Wiki is a fast-emerging agentic knowledge-maintenance pattern with strong implementation activity and plausible value for small-to-mid personal or project knowledge bases.

Claims that are not yet solid: it reliably beats RAG, scales beyond modest corpora, solves enterprise knowledge management, handles multimodal sources robustly, or compounds without drift over long periods.
