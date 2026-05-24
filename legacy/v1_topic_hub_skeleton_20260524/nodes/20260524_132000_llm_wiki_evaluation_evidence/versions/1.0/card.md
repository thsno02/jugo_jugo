# LLM Wiki Evaluation Evidence: Dimensions, Evidence Levels, and Boundaries

这个节点的窄结论是：LLM Wiki 的评价应写成“评估维度、证据等级和边界”，而不是写成已经被全面实证验证的系统类型。当前最强的 direct evidence 是 WiCER：它把 LLM Wiki/wiki-memory 视为把领域知识编译成持久 artifact、再通过 KV-cache/full-context 推理服务给模型的模式，并把关键失败定义为 compilation gap，即 raw documents 被压缩成 wiki 时丢失关键事实。WiCER 用 17 个 RepLiQA domains / 6,800 questions、full-context、RAG baseline、blind compilation、diagnostic probes 和 compile-evaluate-refine iterations 来观察这个问题；但它也把适用范围收在特定模型、硬件、RAG baseline、LLM-as-judge 和验证范围里。[^1][^2]

**评估对象不是“LLM 质量”，而是知识编译和维护链路。** 对 LLM Wiki 来说，最应该被显式记录的维度包括：compilation loss、diagnostic probe coverage、refinement iteration effect、source-to-claim support、citation precision/recall、answer faithfulness、context relevance、claim recall、hallucination/noise sensitivity、drift/staleness、human review outcome、baseline disclosure、model/provider/corpus boundary 和 reproducibility artifact。WiCER 直接支持 compilation gap、诊断 probe、iteration/refinement、baseline 和 scope-limit 这些维度；ALCE、Ragas、ARES、RAGChecker 只提供相邻评价词汇，不能自动转成 LLM Wiki 的 direct benchmark evidence。[^1][^6][^7][^8][^9]

**证据等级应分层表达。** 第一层是 direct LLM Wiki evaluation evidence，例如 WiCER 对 wiki-memory compile/evaluate/refine 的实验。第二层是 narrow economic/token-cost framing，例如 Knowledge Compounding abstract 描述的四次 sequential query、matched RAG baseline、token consumption 和 30-day projection；在当前本地 mining 中，它只能提醒经济 claim 需要 query sequence、baseline、method、logs 和 projection boundary，不能用来宣称一般 ROI 或 enterprise value。第三层是 implementation-described auditability，例如 Atomicstrata 和 Kytmanov README 描述的 source ranges、lint、confidence/contradiction metadata、review queue、compare preview、source hashes、rejection feedback 和 low-confidence/single-source warning；这些是可审计机制的自述，不是独立效果测量。第四层是 adjacent evaluation vocabulary；第五层是 process/gap notes；prior KB anchors 只做连续性和边界。[^3][^4][^5][^10][^11][^12]

**citation auditability 不能简化为“有 citation”。** ALCE 的 citation evaluation 区分 citation recall 与 citation precision，并明确 partial support 会让自动判断变难；这对 LLM Wiki 的启发是：每个 claim 需要检查 citation 是否真正支持 claim，而不是只检查格式存在。Atomicstrata 的 source-range citation lint 与 Kytmanov 的 source hashes、compare previews、draft review 和 rejection feedback 可以降低审计门槛，但仍只能证明实现有这些控制表面，不能证明 citation accuracy 或 maintenance reliability 已经达标。[^4][^5][^6]

**相邻 RAG evaluation vocabulary 可以借用，但要贴标签。** Ragas 的 faithfulness、answer relevance、context relevance，ARES 的 context relevance / answer faithfulness / answer relevance、human preference validation 和 confidence interval 思路，以及 RAGChecker 的 claim-level precision/recall、claim recall、context precision、context utilization、hallucination、noise sensitivity，都适合转写成 LLM Wiki 的评价清单。边界是：这些来源评价的是 RAG 或 citation-augmented generation，不是已经评价了 persistent wiki artifact、writeback、versioned provenance、stale-claim maintenance 或 adoption workflow。[^7][^8][^9]

**KB 节点应表达 claim status，而不是抹平缺口。** 对实证、benchmark-style 或 economic claim，卡片应说明 source、method/baseline scope 和 limitation；对 implementation README，只能写“该实现自述有某控制”；对 adjacent framework，只能写“可借用评价维度”；对没有 citation target 的内容，应降级为 evidence gap、deferred retrieval 或 non-goal。`coverage_framework.md` 要求区分 observed fact、interpretation、hypothesis、evaluation result 和 strategic judgment；`source_gap_review.md` 则把 evaluation/quality coverage 标为 medium，并记录 independent replication、broader provider tests、long-term drift、citation audits 和 human expert evaluation 等缺口。[^10][^11]

**当前可以采用的边界表述。** 在本地证据范围内，可以说：LLM Wiki 评价需要覆盖知识编译损失、source-support auditability、引用支持度、维护漂移、review/adoption gates、baseline 与可复现性；WiCER 是最强直接证据，支持把 compile/evaluate/refine 当作一个需要被测量的链路；实现 README 显示一些项目已经把 citation、lint、review 和 confidence metadata 做成可检查表面；相邻 RAG/citation 论文提供可借用的 metric vocabulary。不能说：LLM Wiki 已经整体优于 RAG/GraphRAG/PKM/agent memory，已经解决 hallucination、citation faithfulness、长期维护、enterprise readiness 或 general ROI。[^12][^13][^14][^15]

## References

### [R1] WiCER source bundle

target: data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
citation_role: primary_direct_evaluation_source
why_cited: Provides the strongest direct local evidence for evaluating an LLM Wiki/wiki-memory compile-evaluate-refine loop and its compilation-gap boundary.
evidence_summary: Supports evaluation dimensions such as compilation loss, diagnostic probes, refinement iterations, RAG/full-context baselines, model/hardware scope, LLM-as-judge validation, and reproducibility constraints.

### [R2] WiCER arXiv abstract page

target: data/raw/arxiv/arxiv-wicer/text.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-wicer/text.txt
citation_role: primary_direct_metadata_source
why_cited: Pins the title, abstract, submission metadata, and high-level summary of WiCER without relying only on the source bundle.
evidence_summary: The abstract states the LLM Wiki pattern, compilation gap, RepLiQA scope, baseline comparisons, WiCER iteration result, ablation claim, and source-availability statement.

### [R3] Knowledge Compounding arXiv abstract page

target: data/raw/arxiv/arxiv-knowledge-compounding/text.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-knowledge-compounding/text.txt
citation_role: cautious_economic_framing_source
why_cited: Provides narrow abstract-level support that economic and token-cost claims need explicit query sequence, baseline, method, and projection boundaries.
evidence_summary: The abstract describes a controlled four-query experiment, matched RAG baseline, token consumption comparison, dynamic ROI framing, and projection claims, but this card does not use it as broad ROI proof.

### [R4] atomicstrata/llm-wiki-compiler README

target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
citation_role: implementation_self_description_source
why_cited: Provides implementation-described auditability controls such as paragraph source markers, line-range citations, lint validation, confidence/contradiction metadata, review queues, and future evaluation harness gaps.
evidence_summary: Used only as project self-description for auditability surfaces, not as proof that these controls are correct or effective.

### [R5] kytmanov/obsidian-local README

target: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
target_version: raw_snapshot
pinned_version: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
citation_role: implementation_self_description_source
why_cited: Provides implementation-described compare previews, source hashes, hand-edit protection, item audit, rejection feedback, and confidence warnings.
evidence_summary: Used only as local-first implementation self-description, not as independent benchmark or reliability evidence.

### [R6] ALCE source bundle

target: data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
citation_role: adjacent_citation_evaluation_vocabulary
why_cited: Supplies adjacent vocabulary for citation recall, citation precision, human evaluation, and partial-support caveats.
evidence_summary: Supports the distinction between citation presence and citation support; it is not direct LLM Wiki evidence.

### [R7] Ragas source bundle

target: data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
citation_role: adjacent_rag_evaluation_vocabulary
why_cited: Supplies adjacent vocabulary for faithfulness, answer relevance, context relevance, and reference-free RAG evaluation.
evidence_summary: Used as method vocabulary for grounding and relevance checks, not as a persistent wiki maintenance benchmark.

### [R8] ARES source bundle

target: data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
citation_role: adjacent_rag_evaluation_vocabulary
why_cited: Supplies adjacent vocabulary for evaluator calibration, context relevance, answer faithfulness, answer relevance, human validation, PPI, confidence intervals, and domain-shift limits.
evidence_summary: Used as adjacent evaluation vocabulary only; it does not validate LLM Wiki compiled artifacts.

### [R9] RAGChecker source bundle

target: data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
target_version: raw_snapshot
pinned_version: data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
citation_role: adjacent_rag_diagnostic_vocabulary
why_cited: Supplies adjacent claim-level diagnostic vocabulary for retriever/generator decomposition, claim recall, context precision, faithfulness, hallucination, context utilization, and noise sensitivity.
evidence_summary: Used as diagnostic vocabulary only; its RAG setting is not direct LLM Wiki evidence.

### [R10] Coverage framework

target: reports/coverage_framework.md
target_version: process_snapshot
pinned_version: reports/coverage_framework.md
citation_role: process_framework_source
why_cited: Provides local process rules for evidence grades, claim records, citation discipline, evaluation dimensions, and judgment gates.
evidence_summary: Supports the requirement to label observed facts, interpretations, hypotheses, evaluation results, strategic judgments, baselines, methods, and limitations.

### [R11] Source gap review

target: reports/source_gap_review.md
target_version: process_snapshot
pinned_version: reports/source_gap_review.md
citation_role: process_gap_source
why_cited: Provides local gap status for evaluation/quality coverage and missing direct evidence.
evidence_summary: Supports the boundary that evaluation evidence is medium, with WiCER strongest, while replication, provider/model comparisons, drift data, citation audits, and human expert evaluation remain missing.

### [R12] Evidence matrix for evaluation evidence

target: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_matrix.yaml
target_version: source_mining_snapshot
pinned_version: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_matrix.yaml
citation_role: process_evidence_map
why_cited: Pins the source-to-claim mapping, source tier labels, confidence notes, and retrieval state used for this candidate.
evidence_summary: Separates direct evidence, economic framing, implementation self-description, adjacent vocabulary, process notes, and prior KB anchors.

### [R13] Evidence gaps for evaluation evidence

target: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_gaps.md
target_version: source_mining_snapshot
pinned_version: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_gaps.md
citation_role: process_gap_boundary
why_cited: Records non-blocking gaps and claims to avoid during generation.
evidence_summary: Supports deferred retrieval boundaries for independent replication, local citation audits, long-term drift, provider/model/corpus comparisons, Knowledge Compounding full extraction, and adjacent metric transfer.

### [R14] Retrieval requests for evaluation evidence

target: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/retrieval_requests.md
target_version: source_mining_snapshot
pinned_version: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/retrieval_requests.md
citation_role: deferred_retrieval_boundary
why_cited: Identifies future retrieval that is useful but not required for the bounded first version.
evidence_summary: Preserves deferred work for WiCER code/logs, Knowledge Compounding full extraction, local adopted-card audits, independent replications, negative cases, and user studies.

### [R15] Evidence scope for evaluation evidence

target: .llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.yaml
target_version: planning_snapshot
pinned_version: .llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.yaml
citation_role: process_scope_source
why_cited: Pins allowed source tiers, supported sections, unsupported claims, prior-KB policy, and deferred retrieval for this candidate.
evidence_summary: Authorizes bounded generation and forbids broad superiority, production reliability, enterprise readiness, adoption/scale, general ROI, benchmark leadership, generic LLM evaluation, and direct transfer of adjacent RAG results.

### [R16] Adopted working definition node

target: kb/20260524_072000_llm_wiki_working_definition.md
target_version: "1.0"
pinned_version: nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity for the LLM Wiki working definition without serving as new evaluation evidence.
evidence_summary: Used only as a vocabulary and boundary anchor.

### [R17] Adopted three-layer architecture node

target: kb/20260524_080000_llm_wiki_three_layer_architecture.md
target_version: "1.0"
pinned_version: nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity for raw/wiki/schema and artifact-layer language without supporting new evaluation claims.
evidence_summary: Used only to keep layer vocabulary stable.

### [R18] Adopted workflow node

target: kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md
target_version: "1.0"
pinned_version: nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity for ingest, compile, query, lint, review, and writeback vocabulary without acting as evaluation proof.
evidence_summary: Used only as workflow terminology anchor.

### [R19] Adopted LLM Wiki vs RAG/write-loop node

target: kb/20260524_094000_llm_wiki_vs_rag_write_loop.md
target_version: "1.0"
pinned_version: nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around adjacent-system boundaries and prevents superiority or equivalence overclaims.
evidence_summary: Used only as a boundary anchor for RAG/GraphRAG/PKM/agent-memory comparisons.

### [R20] Adopted risks/governance/provenance node

target: kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md
target_version: "1.0"
pinned_version: nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around provenance, risk, and citation-audit boundary language.
evidence_summary: Used only as provenance/audit vocabulary anchor.

### [R21] Adopted implementation ecosystem node

target: kb/20260524_122000_llm_wiki_implementation_ecosystem.md
target_version: "1.0"
pinned_version: nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around implementation self-description boundaries and ecosystem wording.
evidence_summary: Used only as boundary anchor; implementation evidence in this node still comes from raw README sources.

### [R22] Adopted origin/canon node

target: kb/20260524_062000_llm_wiki_origin_and_canon.md
target_version: "1.0"
pinned_version: nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md
citation_role: prior_kb_anchor
why_cited: Provides continuity around bounded canon and non-goal discipline.
evidence_summary: Used only as a boundary anchor, not as evaluation evidence.

## Footnotes

[^1]:
    target: data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
    citation_role: primary_direct_evaluation_support
    why_cited: Supports the claim that WiCER directly evaluates a wiki-memory compile-evaluate-refine loop and should be treated as the strongest direct evidence, with model, hardware, RAG baseline, validation, judge, and scope limits.
    evidence_summary: The source bundle includes the WiCER algorithm, RepLiQA setup, diagnostic probes, results, ablation, reproducibility notes, and limitations.

[^2]:
    target: data/raw/arxiv/arxiv-wicer/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-wicer/text.txt
    citation_role: primary_direct_metadata_support
    why_cited: Supports title, abstract-level summary, RepLiQA scope, compilation-gap framing, and high-level result wording for WiCER.
    evidence_summary: The abstract describes the LLM Wiki pattern, compilation gap, 17 RepLiQA domains, 6,800 questions, baseline comparisons, WiCER improvement, ablation, and source availability.

[^3]:
    target: data/raw/arxiv/arxiv-knowledge-compounding/text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-knowledge-compounding/text.txt
    citation_role: cautious_economic_framing_support
    why_cited: Supports only the narrow point that economic/token-cost claims need explicit baseline, query sequence, method, reproducibility, and projection boundaries.
    evidence_summary: The abstract records four sequential queries, matched RAG baseline, token consumption comparison, dynamic ROI framing, and projections; this card does not use it as broad ROI or enterprise proof.

[^4]:
    target: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md
    citation_role: implementation_self_description_support
    why_cited: Supports implementation-described source markers, line-range citations, citation linting, confidence and contradiction metadata, review queues, and future evaluation harness gap.
    evidence_summary: The README is used as self-description of auditability controls, not as measured reliability evidence.

[^5]:
    target: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
    target_version: raw_snapshot
    pinned_version: data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md
    citation_role: implementation_self_description_support
    why_cited: Supports implementation-described compare previews, source hashes, non-overwrite behavior, item audit, rejection feedback, review, and low-confidence/single-source warnings.
    evidence_summary: The README is used as source-specific implementation self-description only.

[^6]:
    target: data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
    citation_role: adjacent_citation_evaluation_support
    why_cited: Supports the distinction between citation recall, citation precision, citation support, human evaluation, and partial-support caveats.
    evidence_summary: ALCE provides adjacent citation-quality vocabulary and cautions; it is not direct LLM Wiki evidence.

[^7]:
    target: data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
    citation_role: adjacent_rag_evaluation_support
    why_cited: Supports adjacent terms faithfulness, answer relevance, context relevance, and reference-free evaluation.
    evidence_summary: Ragas vocabulary is useful for LLM Wiki query/synthesis evaluation checklists but remains RAG-centered.

[^8]:
    target: data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-ares/agent_source_bundle.txt
    citation_role: adjacent_rag_evaluation_support
    why_cited: Supports adjacent evaluator-calibration vocabulary, human preference validation, PPI confidence intervals, and domain-shift boundaries.
    evidence_summary: ARES evaluates RAG triples and evaluator confidence, not persistent wiki artifacts.

[^9]:
    target: data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
    target_version: raw_snapshot
    pinned_version: data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
    citation_role: adjacent_rag_diagnostic_support
    why_cited: Supports claim-level diagnostic vocabulary including claim recall, context precision, context utilization, faithfulness, hallucination, and noise sensitivity.
    evidence_summary: RAGChecker provides adjacent module-diagnostic vocabulary and is not used as direct LLM Wiki benchmark proof.

[^10]:
    target: reports/coverage_framework.md
    target_version: process_snapshot
    pinned_version: reports/coverage_framework.md
    citation_role: process_framework_support
    why_cited: Supports local requirements for evidence grades, claim records, citation discipline, evaluation dimensions, baselines, methods, and limitations.
    evidence_summary: The framework instructs this KB to distinguish observed facts, interpretations, hypotheses, evaluation results, and strategic judgments.

[^11]:
    target: reports/source_gap_review.md
    target_version: process_snapshot
    pinned_version: reports/source_gap_review.md
    citation_role: process_gap_support
    why_cited: Supports the statement that evaluation/quality coverage is medium and that direct replication, broader tests, drift measurement, citation audits, and human expert evaluation remain missing.
    evidence_summary: The report identifies WiCER as strongest benchmark-style evidence while listing non-blocking but important evidence gaps.

[^12]:
    target: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_matrix.yaml
    target_version: source_mining_snapshot
    pinned_version: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_matrix.yaml
    citation_role: process_evidence_map_support
    why_cited: Supports source tier separation and claim-to-source boundaries used throughout the card.
    evidence_summary: The matrix labels WiCER as primary direct evidence, Knowledge Compounding as narrow economic framing, READMEs as implementation self-description, RAG/citation papers as adjacent vocabulary, and process reports as gap/process sources.

[^13]:
    target: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_gaps.md
    target_version: source_mining_snapshot
    pinned_version: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/evidence_gaps.md
    citation_role: process_gap_boundary_support
    why_cited: Supports the explicit list of claims to avoid and future evidence needed before stronger evaluation statements.
    evidence_summary: The gap note forbids superiority, solved-hallucination, proven-reliability, universal scale, general ROI, and direct-transfer claims.

[^14]:
    target: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/retrieval_requests.md
    target_version: source_mining_snapshot
    pinned_version: .llmwiki/runs/run_20260524_132000_worker_source_mining_evaluation_evidence/retrieval_requests.md
    citation_role: deferred_retrieval_support
    why_cited: Supports the statement that further retrieval is useful but not required for this bounded first version.
    evidence_summary: Deferred retrieval includes WiCER code/logs, Knowledge Compounding full extraction, direct local citation audits, independent replications, negative cases, and user studies.

[^15]:
    target: .llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.yaml
    target_version: planning_snapshot
    pinned_version: .llmwiki/runs/run_20260524_133000_worker_node_planning_evaluation_evidence/evidence_scope.yaml
    citation_role: process_scope_support
    why_cited: Supports the final boundary statement and the permitted evidence scope for the candidate.
    evidence_summary: The scope authorizes a bounded first version about evaluation dimensions, evidence levels, citation auditability, and deferred retrieval while excluding broad empirical, production, enterprise, adoption, ROI, benchmark, and generic LLM-eval claims.

