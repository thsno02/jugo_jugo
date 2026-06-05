# comparison-multihop-runtime-vs-compiletime justification

## Why this card exists

This distinction card captures an atomic architectural insight that emerges from comparing two source cards in the knowledge base: memgpt-nested-kv-retrieval and llm-wiki-rag-depth-distinction. Both address multi-hop reasoning but resolve hop dependencies at fundamentally different stages of the system lifecycle.

## Source evidence

- **MemGPT (runtime path)**: The nested KV retrieval experiment (arxiv-memgpt, sections/experiments.tex) demonstrates that agentic function chaining at query time can maintain multi-hop accuracy where baseline models fail. The key data point: MemGPT+GPT-4 stays stable across 0-4 nesting levels while GPT-4 baseline drops to 0% at level 3.

- **LLM Wiki (compile-time path)**: The anthemcreation-fr-guide source (L156) explicitly states that wiki's advantage is reasoning depth from pre-synthesized knowledge with pre-built cross-links, making multi-hop reasoning "natural."

## Why this is a distinct card (not just a footnote)

The runtime-vs-compiletime distinction for multi-hop dependency resolution is itself an atomic, reusable concept that:
1. Generalizes beyond the two specific systems (any multi-hop architecture faces this design choice)
2. Maps to the broader compile-time vs runtime tradeoff in systems design
3. Has predictive power: it tells you which failure modes to expect from each approach

## Governance note

Created during cross-cluster governance pass on the "multi-hop-reasoning-across-architectures" cluster. Both source cards received reciprocal [^dist-1] footnotes pointing to each other, and [^card-1]/[^card-2] footnotes pointing to this comparison card.
