# Audit Queue

共 8 张 draft 卡片在 comparison_provenance 阶段被判为 `provenance_delta`，需要进入 fusion_audit。每条须答 `PROVENANCE_CONTRACT_V3.md` 中的四项审计要求：

1. comparison 是否真的回答了三问；
2. 是否真的读了 v2 accepted card body（不是从 title 推断）；
3. 改 v2 provenance 时是否保留 v2 card 的 scope；
4. 新 provenance 链接是否是增量且可追溯的。

## 条目

### agents-md-as-schema-layer

- `draft_card`: `outputs/llm_wiki/drafts/cards/agents-md-as-schema-layer.md`
- `draft_provenance`: `outputs/llm_wiki/drafts/provenance/agents-md-as-schema-layer.md`
- `similarity_result`: `outputs/llm_wiki/drafts/similarity/agents-md-as-schema-layer.json`
- `comparison_provenance`: `outputs/llm_wiki/drafts/comparison/agents-md-as-schema-layer.md`
- `source_id`: `complete-tech-live-frontier`
- `target_v2_card`: `llm-wiki-schema-configuration-document` (`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md`)
- `top1_score`: 0.250
- `status`: `pending_audit`

### anthemcreation-llm-wiki-three-layer-architecture

- `draft_card`: `outputs/llm_wiki/drafts/cards/anthemcreation-llm-wiki-three-layer-architecture.md`
- `draft_provenance`: `outputs/llm_wiki/drafts/provenance/anthemcreation-llm-wiki-three-layer-architecture.md`
- `similarity_result`: `outputs/llm_wiki/drafts/similarity/anthemcreation-llm-wiki-three-layer-architecture.json`
- `comparison_provenance`: `outputs/llm_wiki/drafts/comparison/anthemcreation-llm-wiki-three-layer-architecture.md`
- `source_id`: `anthemcreation-fr-guide`
- `target_v2_card`: `llm-wiki-three-layer-architecture` (`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md`)
- `top1_score`: 0.286
- `status`: `pending_audit`

### enterprise-llm-wiki-drift-detection-loop

- `draft_card`: `outputs/llm_wiki/drafts/cards/enterprise-llm-wiki-drift-detection-loop.md`
- `draft_provenance`: `outputs/llm_wiki/drafts/provenance/enterprise-llm-wiki-drift-detection-loop.md`
- `similarity_result`: `outputs/llm_wiki/drafts/similarity/enterprise-llm-wiki-drift-detection-loop.json`
- `comparison_provenance`: `outputs/llm_wiki/drafts/comparison/enterprise-llm-wiki-drift-detection-loop.md`
- `source_id`: `falconer-enterprise-guide`
- `target_v2_card`: `llm-wiki-three-layer-architecture` (`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md`)
- `top1_score`: 0.200
- `status`: `pending_audit`

### idea-file-as-agent-era-artifact

- `draft_card`: `outputs/llm_wiki/drafts/cards/idea-file-as-agent-era-artifact.md`
- `draft_provenance`: `outputs/llm_wiki/drafts/provenance/idea-file-as-agent-era-artifact.md`
- `similarity_result`: `outputs/llm_wiki/drafts/similarity/idea-file-as-agent-era-artifact.json`
- `comparison_provenance`: `outputs/llm_wiki/drafts/comparison/idea-file-as-agent-era-artifact.md`
- `source_id`: `karpathy-x-launch-post`
- `target_v2_card`: `idea-file-abstract-vague` (`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/idea-file-abstract-vague.md`)
- `top1_score`: 0.300
- `status`: `pending_audit`

### karpathy-gist-three-layers

- `draft_card`: `outputs/llm_wiki/drafts/cards/karpathy-gist-three-layers.md`
- `draft_provenance`: `outputs/llm_wiki/drafts/provenance/karpathy-gist-three-layers.md`
- `similarity_result`: `outputs/llm_wiki/drafts/similarity/karpathy-gist-three-layers.json`
- `comparison_provenance`: `outputs/llm_wiki/drafts/comparison/karpathy-gist-three-layers.md`
- `source_id`: `karpathy-gist-llm-wiki`
- `target_v2_card`: `llm-wiki-three-layer-architecture` (`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md`)
- `top1_score`: 0.250
- `status`: `pending_audit`

### karpathy-llm-kb-three-layer-arch

- `draft_card`: `outputs/llm_wiki/drafts/cards/karpathy-llm-kb-three-layer-arch.md`
- `draft_provenance`: `outputs/llm_wiki/drafts/provenance/karpathy-llm-kb-three-layer-arch.md`
- `similarity_result`: `outputs/llm_wiki/drafts/similarity/karpathy-llm-kb-three-layer-arch.json`
- `comparison_provenance`: `outputs/llm_wiki/drafts/comparison/karpathy-llm-kb-three-layer-arch.md`
- `source_id`: `developersio-jp-pattern`
- `target_v2_card`: `llm-wiki-three-layer-architecture` (`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md`)
- `top1_score`: 0.500
- `status`: `pending_audit`

### karpathy-llm-wiki-three-layers

- `draft_card`: `outputs/llm_wiki/drafts/cards/karpathy-llm-wiki-three-layers.md`
- `draft_provenance`: `outputs/llm_wiki/drafts/provenance/karpathy-llm-wiki-three-layers.md`
- `similarity_result`: `outputs/llm_wiki/drafts/similarity/karpathy-llm-wiki-three-layers.json`
- `comparison_provenance`: `outputs/llm_wiki/drafts/comparison/karpathy-llm-wiki-three-layers.md`
- `source_id`: `marvin-hn-persistent-knowledge`
- `target_v2_card`: `llm-wiki-three-layer-architecture` (`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md`)
- `top1_score`: 0.308
- `status`: `pending_audit`

### robin-cartier-schema-as-product-doc

- `draft_card`: `outputs/llm_wiki/drafts/cards/robin-cartier-schema-as-product-doc.md`
- `draft_provenance`: `outputs/llm_wiki/drafts/provenance/robin-cartier-schema-as-product-doc.md`
- `similarity_result`: `outputs/llm_wiki/drafts/similarity/robin-cartier-schema-as-product-doc.json`
- `comparison_provenance`: `outputs/llm_wiki/drafts/comparison/robin-cartier-schema-as-product-doc.md`
- `source_id`: `robin-cartier-llm-knowledge-bases`
- `target_v2_card`: `llm-wiki-schema-configuration-document` (`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md`)
- `top1_score`: 0.222
- `status`: `pending_audit`
