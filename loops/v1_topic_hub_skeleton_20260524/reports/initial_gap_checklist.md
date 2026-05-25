# Initial Gap Checklist

Last updated: 2026-05-21

This is the main-thread quick coverage check after the arXiv source-first refresh. The independent sub-agent review in `reports/source_gap_review.md` should be treated as the deeper audit.

## Current Evidence Shape

- **Origin/core text is strong enough for v0**: Karpathy's raw gist is acquired at `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`; HN thread text and item JSON are acquired at `data/raw/hacker_news/hacker-news-original-thread/`.
- **Implementation landscape is reasonably broad for an initial scan**: 15 GitHub repos are shallow-cloned, with `README.remote` and refreshed `github_repo.json` metadata. The set includes desktop app, agent template, Obsidian/Claude/Codex skills, compilers, MCP-oriented projects, and PDF/multimodal-adjacent systems.
- **Paper acquisition is now agent-oriented**: arXiv e-print was used before PDF. Two entries have TeX/source archives and `agent_source_bundle.txt`; one entry is `pdf_only` because arXiv returned a PDF from the e-print endpoint.
- **Community reaction is partial**: HN is covered, Reddit is not locally accessible and is marked blocked. Plugin directories and blog posts are partially covered.
- **Discovery provenance exists**: GitHub search exports are stored in `data/discovery/`, but broader web/search result provenance is still thin.

## Coverage By First-Principles Area

| Area | Current state | Gap severity |
|---|---|---|
| Origin and definition | Strong: gist, X mirror, HN | Low |
| Workflow architecture | Medium: gist plus repo READMEs | Medium |
| Source ingestion | Medium: many repos mention ingestion, but little comparative evidence | Medium |
| Compilation and maintenance | Medium: core idea covered; implementation details vary | Medium |
| Retrieval/query | Partial: some repo docs, little empirical comparison | High |
| Evaluation/quality | Weak: few benchmarks or systematic tests acquired | High |
| UX/tooling/ecosystem | Medium-strong: GitHub, Obsidian, plugin pages, PyPI | Medium |
| Empirical outcomes | Weak: stars and anecdotes are not outcomes | High |
| Comparison with RAG/PKM/agent memory | Weak: origin text frames RAG, but literature/comparison missing | High |
| Risks/governance | Partial: HN raises drift/model-collapse/provenance concerns; governance docs missing | High |
| Adoption/community discourse | Partial: GitHub/HN/blogs; Reddit blocked | Medium-high |
| Research grounding | Partial: 3 arXiv entries, only 2 TeX-readable | High |

## P0 Missing Evidence

- **Systematic evaluation evidence**: benchmark tasks, ablations, or user studies comparing LLM Wiki to raw RAG, chat memory, vector search, and human PKM.
- **Maintenance evidence**: logs or case studies showing whether LLM-maintained pages stay correct over weeks/months, especially under contradictions and source updates.
- **Provenance and trust evidence**: examples of source-to-claim citation fidelity, conflict handling, deletion/retraction, and audit workflows.
- **Reddit/community critique**: current Reddit seeds are blocked; this loses practical objections around PDFs, visuals, OpenWebUI, database framing, and Claude Code plugin usage.
- **Related-work grounding**: agent memory, semantic memory, knowledge graphs, RAG evaluation, PKM, memex/Zettelkasten, and docs-as-code literature.

## P1 Missing Evidence

- **Representative issue/discussion threads from repos**: bugs, user confusion, requested features, and maintainer design decisions.
- **Package/plugin usage signals**: downloads, release history, active maintenance, install friction, and compatibility with Claude/Codex/Cursor/Obsidian.
- **Enterprise/team use cases**: access control, governance, audit logs, Slack/meeting/customer-source ingestion, and cost models.
- **Non-text and difficult-source handling**: long PDFs, images, slides, code repos, YouTube/transcripts, tables/spreadsheets, and multilingual material.
- **Operational economics**: token cost, runtime, storage size, model dependency, failure recovery, and human review burden.

## P2 Missing Evidence

- **Design patterns taxonomy**: file-first vs graph-first vs MCP-first vs UI-first vs compiler-first.
- **Security/license analysis**: copyright, private-source ingestion, secrets handling, and public/private boundary management.
- **Longitudinal adoption signals**: forks, issue velocity, commit activity, plugin installs, and whether projects persist after the initial hype.

## Current Judgment

The current database is enough to write a credible **landscape memo** or initial taxonomy. It is not enough to write a solid paper with strong claims about effectiveness, reliability, or superiority over RAG/PKM/agent-memory systems. For that, the next acquisition pass needs evaluation evidence, failure cases, governance/provenance material, and stronger related-work coverage.
