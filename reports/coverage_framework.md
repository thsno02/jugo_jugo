# LLM Wiki Coverage Framework

Last updated: 2026-05-21

This framework lists, from first principles, what the LLM Wiki topic must cover before the project can support a solid judgment, landscape report, or research paper. It is intentionally evidence-oriented: each item should eventually be backed by raw sources in `data/raw/`, a manifest row in `data/manifests/sources.jsonl`, and a short claim-to-source note.

## First-Principles Definition

An LLM Wiki is a persistent, source-backed knowledge system in which an LLM or agent transforms raw material into durable, inspectable, interlinked knowledge artifacts that future agents can read and maintain. The key distinction from ordinary chat memory or one-shot RAG is that knowledge is deliberately compiled, stored, revised, audited, and reused across time.

The topic therefore has to cover four primitive objects:

- **Sources**: documents, web pages, repos, papers, notes, discussions, transcripts, issue threads, code, and datasets.
- **Transforms**: ingestion, cleaning, extraction, chunking, synthesis, linking, validation, refactoring, and deletion.
- **Persistent representations**: Markdown/wiki pages, graphs, indexes, citations, source maps, embeddings, metadata, manifests, and revision history.
- **Users/agents**: humans, coding agents, research agents, note-taking agents, retrieval services, and evaluators.

And six primitive claims:

- LLM Wikis solve a real limitation in current LLM workflows.
- They can preserve source fidelity while producing useful abstraction.
- They can be maintained safely over time.
- They improve downstream agent performance, user cognition, or organizational memory.
- They are meaningfully different from existing RAG, PKM, knowledge graph, and agent-memory systems.
- Their benefits outweigh costs, risks, and operational complexity in identifiable settings.

## Facts That Must Be Covered

### Origin And Canon

- The original Karpathy statement: exact text, date, context, examples, intended workflow, and stated non-goals.
- Immediate launch/discussion context: X post, Hacker News thread, Reddit/Discord/Claude Code/Obsidian reactions, and early forks.
- Canonical terminology: "LLM Wiki", "LLM Knowledge Base", "knowledge compounding", "compiled memory", "agent-maintained wiki", and how communities use these terms differently.
- Minimal example: what a seed file, source folder, compiled note, citation map, and query flow look like in the original pattern.

### Problem And Motivation

- What failures the pattern addresses: context-window limits, repeated re-explaining, lossy chat history, stale RAG retrieval, unstructured notes, poor provenance, and brittle agent memory.
- Who has the pain: individual researchers, programmers, students, teams, enterprises, AI coding workflows, and domain experts.
- What "better" means: faster reuse, less context setup, better attribution, higher answer quality, less hallucination, easier collaboration, or long-term compounding.

### Architecture And Data Model

- Source acquisition model: supported input types, raw preservation policy, metadata, deduplication, hashing, source trust, and update detection.
- Compilation model: how raw sources become topic pages; whether compilation is extractive, abstractive, template-driven, graph-driven, or agent-orchestrated.
- Storage model: Markdown vault, Obsidian/Logseq, repo-backed wiki, local database, vector store, graph DB, MCP server, desktop app, or hybrid.
- Link model: citations, backlinks, tags, aliases, topic hierarchy, concept graph, source-to-claim traceability, and conflict representation.
- Update model: append-only vs mutable pages, revision history, staleness checks, human review, auto-rebuild, and garbage collection.
- Query model: direct reading by agent, keyword search, semantic retrieval, graph traversal, MCP tools, wiki navigation, and answer generation.

### Workflow And Operations

- End-to-end lifecycle: capture source -> preserve raw -> extract readable text/source -> compile knowledge -> validate -> query -> update.
- Human-in-the-loop boundaries: when the agent can write, when it must propose, when a human approves, and how disagreements are resolved.
- Agent interfaces: slash commands, skills/plugins, MCP tools, CLI commands, editor integrations, web apps, desktop apps, and automation loops.
- Failure handling: blocked sources, malformed PDFs, unavailable TeX, duplicate sources, conflicting sources, inaccessible private data, and hallucinated citations.

### Evaluation And Evidence

- Retrieval/answer quality: whether wiki-backed agents answer better than raw RAG, chat memory, or no memory.
- Maintenance quality: citation accuracy, page coherence, link quality, duplicate/conflict management, freshness, and regression rate.
- Agent usability: time to ingest, time to query, time to update, cost, token usage, latency, and cognitive overhead.
- Robustness: performance under large corpora, long PDFs, code repos, mixed media, multi-language content, and noisy discussions.
- Benchmarks and case studies: reproducible tasks, ablations, before/after comparisons, user studies, and real workflows.

### Ecosystem And Implementations

- Tool families: Obsidian vault templates, Claude/Codex/Cursor skills, MCP servers, desktop apps, repo templates, compilers, and local-only systems.
- Implementation taxonomy: file-first, graph-first, retrieval-first, agent-loop-first, UI-first, enterprise-first, and research-prototype systems.
- Adoption signals: GitHub stars/forks/issues, package downloads, community posts, plugin listings, HN/Reddit discussion, and real user reports.
- Interoperability: Markdown compatibility, citation formats, embeddings, MCP APIs, import/export, Git workflows, and private/local deployment.

### Comparison Space

- RAG: what LLM Wiki adds beyond retrieval over raw chunks, and where RAG remains simpler or better.
- PKM tools: relation to Obsidian, Logseq, Notion, Roam, Zettelkasten, and human-authored notes.
- Knowledge graphs: relation to explicit graph extraction, ontologies, entity linking, and graph databases.
- Agent memory: relation to episodic/semantic/procedural memory, skill memories, reflective agents, and long-term memory stores.
- Documentation systems: relation to literate documentation, wikis, docs-as-code, data catalogs, and knowledge management.

### Risks, Governance, And Ethics

- Provenance risk: fabricated claims, broken citations, source laundering, and over-trusting synthesized pages.
- Maintenance risk: stale pages, contradictory sources, silent overwrites, prompt drift, and compounding errors.
- Privacy/security risk: ingesting private docs, secrets, copyrighted material, or sensitive conversations into agent-readable stores.
- Governance: permission model, review workflow, audit logs, deletion, access control, license compliance, and organizational accountability.
- Epistemic risk: making exploratory synthesis look more certain than the evidence warrants.

## Aspects Needed For A Solid Judgment

### Descriptive Judgment

To say what LLM Wiki is, we need origin text, representative implementations, terminology usage, workflow examples, and ecosystem taxonomy.

### Technical Judgment

To say whether it is technically coherent, we need architecture details, source preservation rules, maintenance algorithms, query mechanisms, and failure modes across multiple implementations.

### Empirical Judgment

To say whether it works, we need reproducible evaluations, user case studies, benchmark comparisons, and longitudinal maintenance evidence.

### Strategic Judgment

To say where it matters, we need adoption signals, target use cases, cost/complexity analysis, comparison with RAG/PKM/agent memory, and evidence of durable advantage.

### Research-Paper Judgment

To write a solid paper, we need a clear definition, taxonomy, literature grounding, implementation survey, empirical results or carefully bounded qualitative evidence, threat model, and explicit limitations.

## Minimum Evidence Matrix

| Area | Minimum evidence needed | Current acquisition target |
|---|---|---|
| Origin | Karpathy gist, launch post, first discussion thread | raw gist, X mirror, HN |
| Community interpretation | HN, Reddit, blog posts, plugin listings | HN acquired; Reddit blocked |
| Implementations | 10-20 representative repos with README and code structure | initial 15 repos cloned |
| Paper grounding | TeX/source bundles where possible, abstracts, related work | arXiv source-first pass added |
| Tooling | Obsidian, Claude/Codex/Cursor, MCP, desktop apps, package registries | partial coverage |
| Evaluation | benchmarks, tests, issue reports, case studies, user outcomes | weak coverage so far |
| Risks | security/privacy/provenance discussions, issue threads, governance docs | weak coverage so far |
| Comparisons | RAG, PKM, knowledge graph, agent memory literature | mostly missing |

## Next Evidence Questions

- What is the smallest common architecture across independent implementations?
- Which claims are community enthusiasm versus demonstrated behavior?
- Do implementations preserve enough provenance for later agents to trust compiled notes?
- Are there repeatable evaluation tasks where LLM Wiki beats raw RAG or chat memory?
- Which source types break the pattern: PDFs, YouTube, code repos, spreadsheets, images, private docs, multilingual content?
- What maintenance policies prevent compounding errors?
- What governance model makes the system acceptable for teams or enterprises?
- Which use cases are genuinely better served by an LLM Wiki than by a vector database, a human wiki, or a normal PKM vault?
