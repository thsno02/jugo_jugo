# Evidence Gaps

target_candidate:: cand_008_risks_governance_provenance
decision:: ready_to_plan

## Not Blocking Bounded First Version

- Direct LLM Wiki incident evidence is absent. The node must not claim observed real-world LLM Wiki attacks, incident rates, or production failures.
- Measured risk reduction from governance controls is absent. The node may describe controls and failure modes, not quantify mitigation effectiveness.
- Enterprise access control, multi-user governance, legal/compliance sufficiency, source licensing policy, and institutional review are under-covered.
- Captured OWASP pages are landing/overview pages; detailed OWASP category claims require preserved whitepaper/category text before use.
- NIST and Microsoft sources provide general governance/control vocabulary but are not LLM Wiki-specific.
- eTAMP, PoisonedRAG, and GraphRAG poisoning are adjacent threat models; the generator must not copy their attack success rates into LLM Wiki claims.
- Reddit is blocked in the local corpus and should not be used substantively.

## Blocking Claims To Avoid

- "LLM Wiki is enterprise-ready/safe/compliant if it has provenance."
- "Claim-level citations prevent hallucination."
- "LLM Wiki has documented poisoning incidents at rates similar to RAG/agent-memory papers."
- "OWASP/NIST/Microsoft prescribe LLM Wiki-specific controls."
- "Human review solves drift or poisoning."
- "A provenance layer makes generated wiki pages authoritative."

## Retrieval Priority For Later Runs

1. Detailed OWASP LLM/agentic category pages or whitepapers preserved locally.
2. Independent incident reports or security analyses of LLM Wiki-like systems.
3. Enterprise access-control / audit-trail docs from non-vendor or primary standards sources.
4. Licensing/source-retention guidance for generated summaries and private sources.
5. Community discourse from Reddit or other blocked forums if accessible on a non-company network.

