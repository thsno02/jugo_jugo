---
schema: accepted_card_provenance.v3
card: ../cards/mem0-extract-update-pipeline.md
material_id: arxiv-mem0
digest_id: digest_arxiv-mem0
source_paths:
  - data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt
draft_card: ../../drafts/cards/mem0-extract-update-pipeline.md
draft_provenance: ../../drafts/provenance/mem0-extract-update-pipeline.md
similarity_result: ../../drafts/similarity/mem0-extract-update-pipeline.json
comparison_provenance: ../../drafts/comparison/mem0-extract-update-pipeline.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:49:00+08:00
  gate_notes: 6/6 项通过；提取与更新两阶段定义、异步摘要、m/s=10、与 full-context/RAG/MemGPT 差异齐备。
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-27T11:49:00+08:00
edited_entity: llm
---

## 源证据

- 第 1140–1155 行（`sections/proposed_work.tex` 内容）：提取阶段定义 + 异步摘要 + update 阶段四操作 + 不使用独立分类器的设计选择。verbatim 节选：
  > "the system employs two complementary sources: (1) a conversation summary S retrieved from the database that encapsulates the semantic content of the entire conversation history, and (2) a sequence of recent messages..."
  > "Rather than using a separate classifier, we leverage the LLM's reasoning capabilities to directly select the appropriate operation based on the semantic relationship between the candidate fact and existing memories."
- 第 1158 行（实验默认）：
  > "we configured the system with `m` = 10 previous messages for contextual reference and `s` = 10 similar memories for comparative analysis. All language model operations utilized `GPT-4o-mini` as the inference engine."
- 第 911–966 行（appendix Algorithm 1）：UpdateMemory 与 ClassifyOperation 伪代码。
- 第 1097–1098 行（intro 中素食 + 乳制品示例）。
- 第 689–691 行（abstract）：26% relative improvement in LLM-as-Judge over OpenAI 等总体数据。

## 卡片范围是否成立

- 卡片以"两阶段管线 + 默认配置"为单一焦点，与论文 §3.1 的章节划分一致；ADD/UPDATE/DELETE/NOOP 的语义细节单独拆到 `mem0-tool-call-add-update-delete-noop`，避免一张卡同时承担"管线骨架 + 操作语义"两件不同密度的事。
- 直接来自源：抽取阶段三段上下文、异步摘要的非阻塞性、$m=s=10$ 的实验配置、`GPT-4o-mini` 的引擎、不使用独立分类器的设计。
- 引申点：与 MemGPT 的对比是基于论文 intro 中对 MemGPT 的引用（packer2023memgpt）以及 v3 paper（memory-as-metabolism）中提到的 MemGPT 在保留决策上的沉默——本 mem0 论文确实没明说"MemGPT 在保留决策上沉默"，但本卡片只用 MemGPT 作为对比锚点，描述其分页机制而不归纳其设计立场，避免越界。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:49:00+08:00
- 检查要点：
  - mechanism 卡两阶段流程 + 实验默认配置 + 与其他路径差异，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-mem0`，正文锚到 proposed_work.tex 第 1139-1158 行 / Algorithm 1 第 911-966 行。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- v2 卡片中暂无 mem0 相关条目，无重叠。
- 与 batch 中 `mem0-tool-call-add-update-delete-noop` 紧密配对：本卡是管线骨架，后者是 update 决策的语义细节。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/mem0-extract-update-pipeline.md`
- draft provenance: `../../drafts/provenance/mem0-extract-update-pipeline.md`
- similarity: `../../drafts/similarity/mem0-extract-update-pipeline.json`
- comparison provenance: `../../drafts/comparison/mem0-extract-update-pipeline.md`
