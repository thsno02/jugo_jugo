LLM Knowledge Bases (Karpathy pattern)
A personal-knowledge-management pattern where an LLM incrementally builds and maintains a persistent, interlinked markdown wiki instead of performing retrieval-augmented generation at query time. Andrej Karpathy’s 3 April 2026 gist made this pattern famous, but the core idea predates it — several practitioners had been running structured compounding knowledge bases long before the gist went viral.
Key points
- Three layers by design [src-002]:
1. raw/ — immutable source documents (PDFs, articles, transcripts). Never edited.
2. wiki/ — LLM-generated markdown pages with cross-references, summaries, and concept maps. The LLM owns these.
3. Schema file (e.g. CLAUDE.md) — governs folder structure, citation rules, ingest workflow, and linting conventions.
Plus two load-bearing meta-files: index.md (category-organised catalogue, updated on every ingest) and log.md (chronological record of every operation).
- The workflow is simple: drop a source into raw/, tell the LLM to ingest it, and it creates or updates 10–15 wiki pages in one pass — extracting entities, concepts, relationships, and cross-references. Queries are answered by reading the index and following links, not by vector similarity search [src-002].
- Zero infrastructure: no embedding model, no vector database, no chunking pipeline. Just markdown files in a folder. Token cost per ingest: ~$2–5 for a major session (10–15 pages); linting <$1; queries negligible [src-002].
- The wiki is just markdown, which means any editor works. The role of Obsidian is to add a graph view for browsing — useful but optional [src-002].
- The schema file is the real innovation, not the wiki itself. Treating CLAUDE.md as “a living product requirements document for an AI colleague” scales far beyond knowledge management to any workflow that needs operational knowledge encoded for the LLM to follow autonomously [src-002].
- Karpathy’s Sequoia interview adds the cognitive reason this pattern matters: even when LLMs can outsource thinking, humans cannot outsource understanding, and wiki-style projections help information make it into the human’s own mental model [src-055].
- Jack Roberts places the same pattern inside a broader AI memory operating system: Obsidian/markdown is the readable long-term memory option, while Pinecone/vector memory is the scalable semantic-search option [src-059].
Strengths and limits
Strengths: reliability (no retrieval misses — the LLM reads the index directly), zero infrastructure, excellent human readability, version-controlled via git.
Limits [src-002]:
- Scale ceiling around ~200 pages / ~100K tokens of index + content. Beyond that, the LLM can’t hold the index in context and you need sub-wikis or a retrieval layer.
- Deduplication is LLM-dependent and fragile at scale — without a deterministic guard, the wiki will accumulate near-duplicate pages over time.
- Temporal signal is weak: a single “last updated” field loses the trend-tracking capability a relational store would give you (first_seen / last_seen).
- Single-user by default: no access control, no merge conflicts, no audit trail beyond the log file.
When to use it vs alternatives [src-002]
| Scenario | Best fit | 
|---|---|
| Personal second brain, research, learning | LLM wiki (this pattern) | 
| Operational automation, trend tracking, pipeline-fed knowledge | structured knowledge bases (relational) | 
| Enterprise scale, millions of documents | Retrieval-Augmented Generation (RAG) (or hybrid) | 
Related entities
- Claude Code — the runtime used by Karpathy’s reference implementation
- Obsidian — the reference browsing layer
- Pinecone — vector-memory alternative for scalable semantic search
- Jack Roberts — practical memory-system workflow source
- Paperclip — related pattern (multi-agent orchestration) that also uses a schema-driven approach
Related concepts
- Agent Orchestration
- Retrieval-Augmented Generation (RAG)
- Understanding Bottleneck
- Software 3.0
- AI Memory Operating System
- Conversation Wrap-Up Memory
- Expert Knowledge Index