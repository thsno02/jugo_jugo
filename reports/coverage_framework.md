# LLM Wiki Coverage Framework

Last updated: 2026-05-21

## Purpose

This framework defines what the **LLM Wiki** topic must cover before the project can support any of the following outputs:

1. A reliable descriptive overview.
2. A technical landscape report.
3. A judgment about whether the pattern works.
4. A comparison with RAG, PKM, knowledge graphs, and agent memory.
5. A research paper or position paper.

The framework is deliberately evidence-oriented. Every substantive claim should eventually be backed by:

* Raw source material in `data/raw/`.
* A source record in `data/manifests/sources.jsonl`.
* A claim-to-source note explaining what the source supports.
* A confidence level and known limitations.

The project should distinguish between:

* **Observed facts**: directly supported by sources.
* **Interpretations**: reasonable readings of available evidence.
* **Hypotheses**: plausible but not yet demonstrated claims.
* **Evaluation results**: claims tested against explicit baselines.
* **Strategic judgments**: conclusions about where the pattern is useful, costly, risky, or overhyped.

---

# 1. Working Definition

An **LLM Wiki** is a persistent, source-backed, agent-readable knowledge system in which an LLM or agent transforms raw material into durable, inspectable, interlinked knowledge artifacts that can be reused, audited, revised, and maintained over time.

The key distinction from ordinary chat memory, one-shot RAG, or unmanaged notes is that knowledge is not merely retrieved or remembered. It is deliberately **compiled**, **stored**, **linked**, **cited**, **maintained**, and **reused**.

A strong definition should include five elements:

1. **Source preservation**
   Raw or near-raw materials are retained so later agents and humans can inspect the basis for claims.

2. **Knowledge compilation**
   Sources are transformed into structured or semi-structured artifacts such as pages, summaries, concept maps, source maps, indexes, or topic notes.

3. **Persistent representation**
   The compiled knowledge survives across sessions and can be read or modified by future agents.

4. **Provenance and auditability**
   Claims, summaries, and links can be traced back to their sources.

5. **Maintenance over time**
   The system supports updating, correcting, deleting, deduplicating, and reconciling knowledge as sources change.

## Boundary Test

A system should count as an LLM Wiki only if it satisfies most of these criteria:

| Criterion                         |          Required? | Explanation                                                                                       |
| --------------------------------- | -----------------: | ------------------------------------------------------------------------------------------------- |
| Persistent knowledge artifacts    |                Yes | The system must produce reusable artifacts, not just transient answers.                           |
| Source-backed claims              |                Yes | The system must preserve some connection between claims and sources.                              |
| LLM/agent-mediated transformation |                Yes | The system must use an LLM or agent to compile, structure, maintain, or query knowledge.          |
| Human or agent readability        |                Yes | Future users or agents must be able to inspect the knowledge layer.                               |
| Maintenance mechanism             | Strongly preferred | Without maintenance, it is closer to static summarization.                                        |
| Interlinking or navigation        | Strongly preferred | Wikis should support movement across related knowledge.                                           |
| Vector retrieval alone            |       Insufficient | A vector database over raw chunks is not enough by itself.                                        |
| Ordinary chat memory alone        |       Insufficient | Memory without source-backed, inspectable artifacts is not enough.                                |
| Human-only PKM vault              |       Insufficient | A human-authored note system becomes relevant only when LLMs help compile, query, or maintain it. |

---

# 2. Primitive Objects

The topic should be modeled around six primitive objects.

## 2.1 Sources

Examples:

* Papers.
* Web pages.
* Repositories.
* Notes.
* Issue threads.
* Forum discussions.
* Chat transcripts.
* PDFs.
* Code.
* Datasets.
* Meeting notes.
* Documentation.
* Screenshots or other multimodal material.

Coverage questions:

* What source types are supported?
* Are raw sources preserved?
* Are sources deduplicated?
* Are sources versioned?
* Are private, copyrighted, or sensitive sources handled safely?
* Can later agents inspect the source behind a claim?

## 2.2 Transforms

Examples:

* Ingestion.
* Cleaning.
* OCR or text extraction.
* Chunking.
* Entity extraction.
* Summarization.
* Synthesis.
* Citation mapping.
* Link creation.
* Conflict detection.
* Refactoring.
* Deletion.
* Recompilation.

Coverage questions:

* Which transforms are deterministic, LLM-mediated, or human-reviewed?
* How are errors detected?
* Can transforms be replayed?
* Can outputs be regenerated from sources?
* Are prompts, tools, and model versions logged?

## 2.3 Persistent Representations

Examples:

* Markdown pages.
* Wiki pages.
* Obsidian vaults.
* Logseq graphs.
* Repo-backed notes.
* Knowledge graphs.
* Vector indexes.
* Citation maps.
* Source maps.
* Manifests.
* Embedding stores.
* Metadata records.
* Revision history.

Coverage questions:

* What exactly persists?
* What is human-readable?
* What is agent-readable?
* What is merely an index?
* What is the canonical state?
* How are revisions tracked?

## 2.4 Links And Provenance

Examples:

* Citations.
* Backlinks.
* Tags.
* Aliases.
* Concept edges.
* Source-to-claim mappings.
* Claim-to-claim dependencies.
* Conflict links.
* Uncertainty notes.

Coverage questions:

* Can every important claim be traced?
* Are links semantic, syntactic, or manually curated?
* Can conflicts be represented without being prematurely resolved?
* Are citations exact, approximate, or merely document-level?
* Can broken or stale citations be detected?

## 2.5 Users And Agents

Examples:

* Individual researchers.
* Programmers.
* Students.
* Teams.
* Enterprise knowledge workers.
* Coding agents.
* Research agents.
* Retrieval systems.
* Evaluators.
* Human reviewers.

Coverage questions:

* Who writes to the wiki?
* Who reads from it?
* Who approves changes?
* Who resolves conflicts?
* Who is harmed if the wiki is wrong?
* What level of trust does each user need?

## 2.6 Governance Layer

Examples:

* Permissions.
* Review policies.
* Audit logs.
* Deletion policies.
* Source licensing.
* Security boundaries.
* Secret detection.
* Access control.
* Human approval workflows.

Coverage questions:

* What can agents ingest?
* What can agents modify?
* What requires human approval?
* How are sensitive sources isolated?
* How are bad updates rolled back?
* How is organizational accountability assigned?

---

# 3. Core Claims To Test

The framework should treat the following as claims to be investigated, not assumptions to be repeated.

## Claim 1: LLM Wikis solve a real workflow limitation

Possible limitations:

* Context-window limits.
* Repeated re-explaining.
* Lossy chat history.
* Stale retrieval.
* Fragmented notes.
* Poor provenance.
* Brittle agent memory.
* Lack of cumulative research state.
* Difficulty onboarding future agents.

Evidence needed:

* User reports.
* Workflow traces.
* Before/after examples.
* Comparison with existing RAG or PKM workflows.
* Repeated-task measurements.

## Claim 2: LLM Wikis preserve source fidelity while producing useful abstraction

Evidence needed:

* Source-to-claim maps.
* Citation accuracy checks.
* Examples of faithful synthesis.
* Examples of failed or misleading synthesis.
* Human review of generated pages.
* Error taxonomies.

## Claim 3: LLM Wikis can be maintained safely over time

Evidence needed:

* Revision histories.
* Update policies.
* Staleness detection.
* Regression tests.
* Human approval workflows.
* Conflict handling.
* Deletion and correction behavior.

## Claim 4: LLM Wikis improve downstream performance

Possible outcomes:

* Better answer quality.
* Faster task completion.
* Lower setup cost.
* Better attribution.
* Reduced hallucination.
* Better agent planning.
* Better organizational memory.
* Better research continuity.

Evidence needed:

* Benchmarks.
* Ablations.
* Controlled comparisons.
* Longitudinal case studies.
* User studies.
* Cost and latency measurements.

## Claim 5: LLM Wikis are meaningfully different from adjacent systems

Comparison targets:

* Raw RAG.
* Chat memory.
* Vector databases.
* PKM systems.
* Human-authored wikis.
* Knowledge graphs.
* Agent memory systems.
* Documentation systems.
* Data catalogs.

Evidence needed:

* Feature matrix.
* Architecture comparison.
* Workflow comparison.
* Failure-mode comparison.
* Use-case boundaries.

## Claim 6: Benefits outweigh costs in identifiable settings

Costs and risks:

* Ingestion cost.
* Maintenance burden.
* Token cost.
* Latency.
* Review overhead.
* False confidence.
* Privacy exposure.
* Copyright/licensing risk.
* Compounding errors.
* Tooling complexity.

Evidence needed:

* Cost models.
* Operational case studies.
* User adoption signals.
* Failure reports.
* Governance requirements.
* Clear use-case segmentation.

---

# 4. Coverage Map

## 4.1 Origin And Canon

The framework must establish what the term originally meant and how its meaning evolved.

Must cover:

* Original Karpathy statement.
* Exact text.
* Date.
* Platform.
* Immediate context.
* Stated examples.
* Intended workflow.
* Stated or implied non-goals.
* Earliest public discussions.
* Early forks, templates, or implementations.
* Whether “LLM Wiki” was proposed as a product, workflow, architecture, metaphor, or research direction.

Evidence to collect:

* Original post or reliable mirror.
* GitHub gist or repo if applicable.
* X/Twitter mirrors.
* Hacker News thread.
* Reddit discussions if accessible.
* Discord/Claude Code/Obsidian community references if accessible.
* Early blog posts.
* Early GitHub repos.

Output should answer:

* What did the original idea actually say?
* What did early adopters think it meant?
* Which parts of the current interpretation are original versus later extrapolation?

---

## 4.2 Terminology And Concept Drift

The framework must track how related terms are used across communities.

Terms to cover:

* LLM Wiki.
* LLM Knowledge Base.
* Agent-maintained wiki.
* Knowledge compounding.
* Compiled memory.
* Source-backed memory.
* AI-native wiki.
* Agent-readable notes.
* Long-term agent memory.
* Research memory.
* Semantic memory.

Must distinguish:

* Synonyms.
* Near-synonyms.
* Competing terms.
* Community-specific usage.
* Marketing usage.
* Research usage.
* Implementation-specific usage.

Evidence to collect:

* Community posts.
* README language.
* Product pages.
* Papers.
* Plugin descriptions.
* Issue threads.
* Blog posts.

Output should answer:

* Is “LLM Wiki” a stable term?
* Is it a narrow architecture or a loose family of workflows?
* Which terms should the project use, avoid, or define explicitly?

---

## 4.3 Problem And Motivation

The framework must identify the concrete pain points the pattern addresses.

Must cover:

* Context-window limits.
* Repeated context setup.
* Lossy or inaccessible chat history.
* Stale RAG retrieval.
* Fragmented notes.
* Weak source attribution.
* Brittle agent memory.
* Lack of cumulative research state.
* Poor collaboration between humans and agents.
* Inability to transfer state between agents or sessions.

User groups:

* Individual researchers.
* Software engineers.
* Students.
* Writers.
* Analysts.
* Teams.
* Enterprises.
* Domain experts.
* Coding-agent users.
* AI research workflows.

Output should answer:

* Who has the problem?
* How severe is it?
* What do they do today?
* Why are existing tools insufficient?
* What would count as a meaningful improvement?

---

## 4.4 Architecture And Data Model

The framework must describe the system architecture in implementation-neutral terms.

Must cover:

### Source acquisition

* Input types.
* Raw preservation.
* Metadata.
* Deduplication.
* Hashing.
* Trust level.
* Source version.
* Update detection.
* Licensing.
* Access permissions.

### Compilation

* Extractive compilation.
* Abstractive synthesis.
* Template-driven pages.
* Graph-driven compilation.
* Agent-orchestrated workflows.
* Manual review.
* Prompt and model logging.

### Storage

* Markdown vault.
* Repo-backed wiki.
* Obsidian or Logseq.
* Local database.
* Vector store.
* Graph database.
* MCP server.
* Desktop app.
* Web app.
* Hybrid architecture.

### Link model

* Citations.
* Backlinks.
* Tags.
* Aliases.
* Topic hierarchy.
* Source maps.
* Claim maps.
* Concept graph.
* Conflict representation.

### Update model

* Append-only logs.
* Mutable pages.
* Revision history.
* Staleness checks.
* Auto-rebuilds.
* Human review.
* Garbage collection.
* Rollbacks.
* Conflict resolution.

### Query model

* Agent reads wiki pages directly.
* Keyword search.
* Semantic search.
* Graph traversal.
* MCP tools.
* Wiki navigation.
* Hybrid retrieval.
* Answer generation with citations.

Output should answer:

* What is the smallest common architecture across implementations?
* Which components are essential?
* Which components are optional?
* Which design choices create the biggest tradeoffs?

---

## 4.5 Workflow And Operations

The framework must describe the lifecycle of knowledge inside an LLM Wiki.

Canonical lifecycle:

```text
Capture source
→ Preserve raw material
→ Extract readable content
→ Normalize metadata
→ Compile knowledge artifact
→ Link artifact to sources and related pages
→ Validate claims and citations
→ Query or reuse artifact
→ Update when sources or interpretations change
→ Archive, delete, or refactor stale material
```

Must cover:

* Capture workflows.
* Ingestion queues.
* Human-in-the-loop boundaries.
* Agent write permissions.
* Review and approval.
* Citation checking.
* Conflict handling.
* Staleness checks.
* Rebuild policies.
* Rollback.
* Deletion.
* Error reporting.

Failure handling:

* Blocked sources.
* Malformed PDFs.
* Unavailable source files.
* Broken links.
* Duplicate sources.
* Conflicting sources.
* Inaccessible private data.
* Hallucinated citations.
* Overwritten human notes.
* Model drift.
* Prompt drift.
* Corrupt indexes.

Output should answer:

* What does a complete operational workflow look like?
* Where do agents act autonomously?
* Where must humans approve?
* How does the system recover from errors?

---

## 4.6 Ecosystem And Implementations

The framework must survey representative implementations without treating any one implementation as definitive.

Tool families:

* Obsidian vault templates.
* Claude, Codex, Cursor, or other coding-agent workflows.
* MCP servers.
* Repo templates.
* Desktop apps.
* Local-first systems.
* Research prototypes.
* Enterprise knowledge tools.
* Graph-based tools.
* Retrieval-first tools.
* Documentation compilers.

Implementation taxonomy:

| Type               | Core idea                               | Likely strength        | Likely weakness                       |
| ------------------ | --------------------------------------- | ---------------------- | ------------------------------------- |
| File-first         | Markdown or repo is the canonical store | Inspectable, portable  | Harder to query at scale              |
| Graph-first        | Entities and relations are central      | Strong structure       | Extraction and maintenance complexity |
| Retrieval-first    | Search/index layer dominates            | Fast query             | May be weak as a wiki                 |
| Agent-loop-first   | Agents maintain pages through workflows | Powerful automation    | Higher risk of drift or bad edits     |
| UI-first           | Human interface is primary              | Usable for individuals | May lack rigorous provenance          |
| Enterprise-first   | Governance and access control dominate  | Safer for teams        | Heavier operational burden            |
| Research-prototype | Tests a specific mechanism              | Useful evidence        | May not be production-ready           |

Evidence to collect:

* READMEs.
* Code structure.
* Release history.
* GitHub stars and forks.
* Issues and bug reports.
* Examples and demos.
* Package downloads.
* Plugin listings.
* User reports.
* Screenshots or workflows.
* Governance docs.

Output should answer:

* What implementation patterns actually exist?
* Which claims are supported by running systems?
* Which claims are only aspirational?
* Which tools are closest to the LLM Wiki concept?

---

## 4.7 Comparison Space

The framework must compare LLM Wikis against adjacent systems precisely.

## RAG

Compare on:

* Raw retrieval versus compiled knowledge.
* Chunk-level evidence versus page-level synthesis.
* Query-time reasoning versus precompiled structure.
* Freshness.
* Provenance.
* Maintenance cost.
* Hallucination risk.
* Deployment simplicity.

Key question:

> What does an LLM Wiki add beyond retrieval over raw documents, and when is that addition worth the extra complexity?

## PKM Tools

Compare on:

* Human-authored notes.
* Bidirectional links.
* Personal knowledge workflows.
* Agent-assisted maintenance.
* Source fidelity.
* Collaboration.
* Portability.

Key question:

> Is an LLM Wiki an AI-augmented PKM system, or a distinct knowledge infrastructure layer?

## Knowledge Graphs

Compare on:

* Explicit entities and relations.
* Ontologies.
* Entity linking.
* Graph databases.
* Reasoning over structured relations.
* Human-readable synthesis.

Key question:

> Does the wiki need a graph, or does the graph merely support the wiki?

## Agent Memory

Compare on:

* Episodic memory.
* Semantic memory.
* Procedural memory.
* Reflection.
* Skill memories.
* Long-term stores.
* Inspectability.

Key question:

> Is an LLM Wiki a form of agent memory, or a source-governed knowledge layer that agents can use?

## Documentation Systems

Compare on:

* Docs-as-code.
* Wikis.
* Literate documentation.
* Data catalogs.
* Internal knowledge bases.
* Versioning.
* Editorial control.

Key question:

> What changes when documentation is continuously compiled and maintained by agents?

---

## 4.8 Evaluation And Evidence

The framework must define how to test whether LLM Wikis work.

Evaluation dimensions:

| Dimension           | What to measure                                                      |
| ------------------- | -------------------------------------------------------------------- |
| Answer quality      | Correctness, completeness, citation quality, uncertainty handling    |
| Retrieval quality   | Recall, precision, relevance, source diversity                       |
| Source fidelity     | Whether generated claims match cited sources                         |
| Maintenance quality | Freshness, duplicate handling, conflict handling, page coherence     |
| Agent performance   | Task success, planning quality, fewer repeated explanations          |
| Human usability     | Time saved, cognitive overhead, trust, review burden                 |
| Cost                | Token usage, latency, storage, engineering time                      |
| Robustness          | Large corpora, noisy sources, PDFs, code repos, multilingual content |
| Governance          | Privacy, permissions, auditability, deletion, review compliance      |

Baselines:

* No memory.
* Chat history only.
* Raw RAG.
* Human-authored notes.
* Vector database over raw sources.
* Traditional wiki.
* Knowledge graph.
* Agent memory store.
* Hybrid systems.

Evaluation methods:

* Reproducible benchmark tasks.
* Before/after workflow studies.
* Ablations.
* Citation audits.
* Human expert review.
* Longitudinal maintenance tests.
* Adversarial source tests.
* Cost/latency measurements.
* Case studies.

Minimum empirical questions:

* Does the wiki improve answer quality over raw RAG?
* Does it reduce repeated context setup?
* Does it improve citation accuracy?
* Does it remain accurate after updates?
* Does it help agents perform multi-step tasks?
* Does maintenance cost outweigh benefits?
* Which source types break the pattern?

---

## 4.9 Risks, Governance, And Ethics

The framework must treat risks as central, not as an appendix.

## Provenance risk

Examples:

* Fabricated claims.
* Broken citations.
* Source laundering.
* Misleading synthesis.
* Unsupported generalization.
* Overconfident pages.

Required coverage:

* Citation validation.
* Claim-level provenance.
* Uncertainty labels.
* Source confidence.
* Human review policies.

## Maintenance risk

Examples:

* Stale pages.
* Contradictory sources.
* Silent overwrites.
* Compounding errors.
* Prompt drift.
* Model drift.
* Broken rebuilds.
* Duplicate pages.

Required coverage:

* Revision history.
* Regression checks.
* Conflict representation.
* Update triggers.
* Rollback.
* Page aging indicators.

## Privacy and security risk

Examples:

* Ingesting private documents.
* Exposing secrets.
* Mixing public and private sources.
* Making sensitive conversations agent-readable.
* Weak access control.
* Unsafe exports.

Required coverage:

* Source permissions.
* Secret scanning.
* Access control.
* Local-first options.
* Deletion.
* Audit logs.
* Data minimization.

## Legal and licensing risk

Examples:

* Copyrighted sources.
* Unclear reuse rights.
* License-incompatible code or text.
* Generated summaries of restricted material.
* Team-wide redistribution of private sources.

Required coverage:

* License metadata.
* Source-use policy.
* Retention rules.
* Export rules.
* Attribution requirements.

## Epistemic risk

Examples:

* Exploratory synthesis appearing settled.
* Weak sources becoming canonical.
* Agent-generated pages gaining false authority.
* Conflicts being erased rather than represented.
* Uncertainty being compressed away.

Required coverage:

* Confidence labels.
* Disagreement sections.
* Evidence grading.
* Known limitations.
* Claim status tracking.

---

# 5. Evidence Standards

## 5.1 Source Record Standard

Each source should have a manifest entry containing:

```json
{
  "source_id": "stable identifier",
  "title": "source title",
  "url_or_path": "raw source location",
  "source_type": "paper | repo | post | thread | docs | transcript | dataset | other",
  "author_or_org": "creator",
  "date_published": "YYYY-MM-DD or unknown",
  "date_accessed": "YYYY-MM-DD",
  "license": "license or unknown",
  "trust_level": "high | medium | low | unknown",
  "raw_preserved": true,
  "hash": "content hash if available",
  "notes": "limitations, access issues, or caveats"
}
```

## 5.2 Claim Record Standard

Each important claim should be tracked as:

```json
{
  "claim_id": "stable identifier",
  "claim": "plain-language claim",
  "claim_type": "observed fact | interpretation | hypothesis | evaluation result | judgment",
  "supporting_sources": ["source_id_1", "source_id_2"],
  "contradicting_sources": ["source_id_3"],
  "confidence": "high | medium | low",
  "status": "draft | supported | disputed | stale | retired",
  "notes": "why the evidence is sufficient or insufficient"
}
```

## 5.3 Evidence Grades

| Grade | Meaning                     | Suitable for                                           |
| ----- | --------------------------- | ------------------------------------------------------ |
| A     | Direct primary evidence     | Origin claims, implementation facts, benchmark results |
| B     | Strong secondary evidence   | Community interpretation, adoption signals             |
| C     | Indirect evidence           | Hypotheses, weak trend claims                          |
| D     | Anecdotal evidence          | User impressions, informal reports                     |
| F     | Unsupported or contradicted | Claims to avoid or mark as speculative                 |

## 5.4 Minimum Citation Discipline

The project should avoid unsupported synthesized claims. In particular:

* Every historical claim needs a date and source.
* Every implementation claim needs a repo, docs page, demo, or code reference.
* Every empirical claim needs a baseline and method.
* Every strategic claim needs an explicit assumption.
* Every risk claim needs either a documented failure, a plausible threat model, or an analogy to adjacent systems.

---

# 6. Judgment Gates

The framework should separate five levels of judgment.

## 6.1 Descriptive Judgment

Question:

> What is an LLM Wiki?

Minimum evidence:

* Origin text.
* Representative implementations.
* Terminology survey.
* Workflow examples.
* Ecosystem taxonomy.

Pass condition:

* The project can define the concept without relying on one anecdote or one implementation.

## 6.2 Technical Judgment

Question:

> Is the pattern technically coherent?

Minimum evidence:

* Architecture comparison.
* Data model examples.
* Source preservation rules.
* Compilation methods.
* Query mechanisms.
* Maintenance policies.
* Failure modes.

Pass condition:

* The project can describe the essential architecture and identify major design tradeoffs.

## 6.3 Empirical Judgment

Question:

> Does the pattern work better than plausible alternatives?

Minimum evidence:

* Benchmarks.
* Case studies.
* Before/after comparisons.
* Citation audits.
* Longitudinal maintenance evidence.
* Baseline comparisons.

Pass condition:

* The project can say where LLM Wikis outperform raw RAG, chat memory, or ordinary notes, and where they do not.

## 6.4 Strategic Judgment

Question:

> Where does the pattern matter?

Minimum evidence:

* Adoption signals.
* Use-case segmentation.
* Cost model.
* Complexity analysis.
* Comparison with adjacent systems.
* Risk assessment.

Pass condition:

* The project can identify settings where LLM Wikis are worth building, and settings where simpler systems are better.

## 6.5 Research-Paper Judgment

Question:

> Can this support a serious paper?

Minimum evidence:

* Clear definition.
* Literature grounding.
* Taxonomy.
* Implementation survey.
* Evaluation or carefully bounded qualitative evidence.
* Threat model.
* Limitations.
* Reproducible artifacts.

Pass condition:

* The project can make a bounded, evidence-backed contribution rather than a broad speculative argument.

---

# 7. Minimum Evidence Matrix

| Area                 | Key question                                | Minimum evidence needed                             | Acquisition target                                   |
| -------------------- | ------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------- |
| Origin               | What did the original idea say?             | Primary text, date, context, examples               | Karpathy post/gist, mirrors, first discussion thread |
| Early interpretation | How did communities understand it?          | HN, Reddit, Discord, blogs, early forks             | Discussion archives, community posts                 |
| Terminology          | Is the term stable?                         | Usage examples across communities                   | READMEs, blog posts, product pages, papers           |
| Implementations      | What has actually been built?               | 10–20 representative systems                        | Repos, docs, demos, code structure                   |
| Architecture         | What is the common system shape?            | Data models, storage choices, query flows           | READMEs, diagrams, source code, configs              |
| Workflow             | How does knowledge move through the system? | End-to-end examples                                 | Ingestion scripts, command logs, demos               |
| Provenance           | Can claims be traced?                       | Citation maps, source maps, audits                  | Compiled pages, manifests, examples                  |
| Maintenance          | Can the system stay correct?                | Revision history, update policies, staleness checks | Issues, tests, update scripts, docs                  |
| Evaluation           | Does it improve outcomes?                   | Benchmarks, ablations, user studies                 | Papers, experiments, reproducible tasks              |
| Adoption             | Is anyone using it seriously?               | Stars, forks, issues, posts, testimonials           | GitHub, forums, plugin listings                      |
| Comparisons          | What is it better or worse than?            | RAG/PKM/KG/memory feature matrix                    | Literature, tools, benchmark comparisons             |
| Risks                | What can go wrong?                          | Security, privacy, provenance, governance evidence  | Issue threads, threat models, policy docs            |
| Economics            | Is it worth the cost?                       | Token, latency, review, maintenance costs           | Experiments, case studies, operational reports       |

---

# 8. Suggested Research Questions

## Definition And Scope

* What minimum features distinguish an LLM Wiki from RAG?
* Is the wiki primarily a storage layer, workflow pattern, agent interface, or epistemic discipline?
* Does “LLM Wiki” describe a single architecture or a family of related systems?

## Architecture

* What is the smallest common architecture across independent implementations?
* Is Markdown sufficient as the canonical representation?
* When does a graph become necessary?
* Should source maps be document-level, passage-level, or claim-level?
* What parts of the system must be deterministic?

## Provenance

* Do implementations preserve enough provenance for future agents to trust compiled notes?
* What citation granularity is necessary for reliable reuse?
* How often do compiled pages misrepresent sources?
* Can agents detect unsupported or stale claims?

## Evaluation

* Are there repeatable tasks where LLM Wiki beats raw RAG?
* Are there repeatable tasks where raw RAG is simpler and better?
* Does precompiled knowledge improve agent planning?
* Does a wiki reduce hallucination, or merely make hallucinations more persistent?
* How does performance change as the corpus grows?

## Maintenance

* What maintenance policies prevent compounding errors?
* Should pages be mutable, append-only, or rebuilt from source?
* How should conflicts be represented?
* How should old claims be retired?
* What happens when source material disappears?

## Use Cases

* Which workflows benefit most: research, coding, enterprise knowledge, education, writing, or personal notes?
* Which source types break the pattern: PDFs, YouTube, code repos, spreadsheets, images, private docs, multilingual content?
* Which users need human-readable pages versus machine-readable indexes?
* Which teams need governance before they can safely adopt the pattern?

## Strategy

* Which claims are community enthusiasm versus demonstrated behavior?
* What would make LLM Wikis a durable infrastructure pattern?
* What would make them a temporary workaround for current model limitations?
* Which use cases are better served by a vector database, traditional wiki, or normal PKM vault?

---

# 9. Recommended Project Outputs

The research project should eventually produce the following artifacts.

## 9.1 Definition Note

A concise, source-backed definition of LLM Wiki with boundary cases.

## 9.2 Origin Dossier

A historical note covering the original statement, early discussion, and term evolution.

## 9.3 Implementation Survey

A structured survey of representative systems, including architecture, storage model, query model, provenance model, and maintenance model.

## 9.4 Comparison Matrix

A matrix comparing LLM Wiki against RAG, PKM, knowledge graphs, agent memory, documentation systems, and traditional knowledge management.

## 9.5 Evaluation Plan

A reproducible benchmark plan with tasks, baselines, metrics, and failure analysis.

## 9.6 Risk And Governance Note

A threat model covering provenance, maintenance, privacy, security, licensing, and epistemic risk.

## 9.7 Evidence Registry

A structured claim-to-source registry that separates facts, interpretations, hypotheses, and judgments.

## 9.8 Final Judgment

A bounded conclusion answering:

* What is LLM Wiki?
* What is new about it?
* What works?
* What remains unproven?
* Where is it useful?
* Where is it overkill?
* What research or tooling would most improve the pattern?

---

# 10. Current Highest-Priority Evidence Gaps

The most important gaps to close are:

1. **Origin certainty**
   Capture the exact original statement, date, context, and immediate discussion.

2. **Implementation reality**
   Identify whether existing systems actually implement source-backed, maintainable wikis or merely use the label loosely.

3. **Provenance quality**
   Test whether compiled notes preserve enough source fidelity for later agents to rely on them.

4. **Empirical comparison**
   Build tasks that compare LLM Wiki against raw RAG, chat memory, and ordinary notes.

5. **Maintenance evidence**
   Determine whether wikis stay accurate over time or accumulate errors.

6. **Governance feasibility**
   Assess whether teams can safely use agent-maintained knowledge stores with private or sensitive material.

7. **Use-case segmentation**
   Identify where the pattern is genuinely superior and where simpler alternatives are better.

---

# 11. Bottom-Line Standard

The project should not conclude that LLM Wikis are valuable merely because the idea is intuitive, popular, or architecturally appealing.

A strong conclusion requires evidence that:

1. The concept is definable.
2. The architecture is coherent.
3. The workflow solves real problems.
4. The compiled knowledge remains source-faithful.
5. Maintenance is feasible.
6. The system improves outcomes against plausible baselines.
7. Risks can be governed.
8. The benefits justify the added complexity in specific use cases.

Until those conditions are met, the strongest defensible position is:

> LLM Wikis are a promising pattern for persistent, source-backed, agent-readable knowledge compilation, but their durable value depends on provenance quality, maintenance discipline, empirical performance against simpler baselines, and governance in real-world workflows.
