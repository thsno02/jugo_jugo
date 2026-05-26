---
schema: draft_card_provenance.v3
draft_card: ../cards/memory-as-metabolism-contextualize-depth-fitted.md
material_id: arxiv-memory-as-metabolism
digest_id: digest_arxiv-memory-as-metabolism
source_paths:
  - data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-26T15:10:00+08:00
edited_entity: llm
---

## 源证据

### §5.4 开篇 Product Owner vs Developer 例子（第 1216–1224 行）

> "CONTEXTUALIZE is the framework's response to a problem the other operations do not handle: external sources do not have a single canonical compression. The same architecture decision record yields a different useful summary for a Product Owner than for a Developer reading it the same afternoon. The Product Owner needs goals, tradeoffs, and stakeholder rationale; the Developer needs implementation constraints, library choices, and edge cases. Neither is wrong. Both are contextually correct compressions of the same artifact, fitted to the working depth at which the user is currently engaging the topic."

### §5.4 dream-cycle vs streaming 论证（第 1255–1266 行）

> "First, CONTEXTUALIZE runs in the dream cycle, not at runtime ingestion. Streaming ingestion (TRIAGE) is intentionally shallow because runtime cost has to stay low; depth-fitting compression is expensive enough that batching it with sleep consolidation is the right place architecturally. The raw external source survives in the buffer until the next dream cycle, which is also a safety property: if the user's context shifts between ingestion and consolidation ... the next dream cycle compresses against the new context rather than the old one."

### §5.4 inferred depth（第 1268–1281 行）

> "Second, the depth is inferred by default, not explicitly set by the user. Asking the user to specify their working-context depth on every ingested source is operationally absurd ... The companion infers depth from the user's other wiki entries, recent query patterns, and the topical neighborhood the source falls into ... Inferred depth fails sometimes, in ways the user cannot easily catch—which is why the linkout to the full source is non-optional."

### §5.4 三层存储（第 1291–1306 行）

> "This introduces a third storage tier beyond the raw buffer and the active wiki: cold memory. The raw external source ... should not be deleted either, because CONTEXTUALIZE's mandatory linkout commitment means the user must be able to retrieve it when context shifts. Cold memory is the named destination for these originals: high-capacity, low-access-frequency storage that holds the sources the wiki has already processed."

### §5.4 与 D-Mem 区分（第 1240–1253 行）

> "The closest prior art is D-Mem (You, Yuan & Cai, arXiv 2603.18631), which proposes a dual-process memory architecture ... CONTEXTUALIZE differs in two ways: it decides the appropriate compression depth before integration rather than switching reactively at retrieval time, and it infers that depth from the user's wiki topology and query behavior rather than from the retrieval query alone. The coordination bundle—depth inference from user context, compression fitted to that depth, originals preserved as a structural non-optional commitment, deferred to the dream cycle rather than run at streaming ingestion—is what prior work does not assemble together."

### §7.5 CONTEXTUALIZE MUST（第 1906–1912 行）

> "MUST preserve a linkout to the original external source — this is non-optional and cannot be traded off for storage efficiency - MUST run in the scheduled consolidation cycle, not at streaming ingestion time - MUST create a cold memory object for every processed external source before producing a depth-fitted representation - MUST NOT discard the original source after compression"

### §9 limitations（第 2188–2210 行）

> "Working-context depth inference is an open modeling problem. CONTEXTUALIZE infers the user's depth of engagement from query patterns and wiki topology rather than requiring explicit specification. If that inference is wrong, the operation produces systematic compression distortion that propagates into the active wiki during the next CONSOLIDATE cycle. Linkout preservation is a partial mitigation—the original source remains reachable—but anchoring effects mean users may rely on the compressed entry without inspecting the source."

## 卡片范围是否成立

本卡聚焦 CONTEXTUALIZE 操作；现有 `memory-as-metabolism-five-operations` 卡片只用一段文字概括了 CONTEXTUALIZE，没有覆盖：

- depth-fitted compression 的"PO vs Developer"动机（这是非平凡的设计 insight）；
- 三层存储模型的"cold memory"层引入（这是 §5.4 直接产物）；
- 与 D-Mem 的 prior art 区分（论文专门写了的对照）；
- §7.5 中 4 条 conformance MUST（其中 linkout 不可让渡是核心安全承诺）。

所有主张都直接来自 §5.4、§4、§7.5、§9。"selective absorption" metabolic 比喻是论文显式给出的，本卡保留为整张框架的引子。

## 发表门控结果

本轮未运行。

## 备注

- 与 `memory-as-metabolism-five-operations` 卡片的关系：那张卡覆盖五操作总图，本卡是 CONTEXTUALIZE 的**专卡**——后者把"为什么这个操作单独存在 / 它的 conformance / 它的失败模式"展开。在 wiki 内可双向 link。
- 与 D-Mem (arxiv:2603.18631) 有 prior-art 关系；如果未来有 D-Mem 自身的材料进入 wiki，应做 comparison。
