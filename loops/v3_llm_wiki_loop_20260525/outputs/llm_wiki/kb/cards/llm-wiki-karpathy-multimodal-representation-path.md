---
id: llm-wiki-karpathy-multimodal-representation-path
title: 非文本资产走 representation-first ingest 路径
status: accepted
card_type: mechanism
tags: [#llm-wiki, #multimodal, #ocr, #pdf, #representation, #ingest]
created_time: 2026-05-26T11:38:00+08:00
edited_time: 2026-05-28T11:40:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
provenance_card: ../provenance/llm-wiki-karpathy-multimodal-representation-path.md
aliases: ["representation-first ingest", ".llm-kb/representations/"]
related: [llm-wiki-karpathy-runtime-vs-agent-split, llm-wiki-karpathy-lint-grounding-trail, my-llm-wiki-supported-source-types, enterprise-llm-wiki-tool-native-ingestion, karpathy-wiki-extraction-granularity]
---

`@harrylabs/llm-wiki-karpathy` v0.4.4 把 ingest 路径分成两条：

- **文本与结构化数据**（`.md`、`.txt`、`.csv`、`.tsv`、`.json`、`.html`）走"直接编译"路径：`kb_prepare_source` + `kb_read_raw` 直接从 raw/ 拉内容编译出 source note。
- **PDF 与图片**（`.png`、`.jpg`、`.jpeg`、`.webp`、`.gif`、`.svg`）走 **representation-first** 路径。这条路径的关键是 runtime 不做 OCR / vision，而是给 agent 一个"存放中间产物"的规范位置。

representation-first 的标准步骤：

1. **`kb_get_raw_asset`** 检查资产元数据（含 deterministic metadata + 给本地查看器用的 safe absolute path）。
2. **`kb_prepare_source_bundle`** 拉取整体 compile 上下文：raw metadata、asset refs、已存的 representations、compile_readiness（`ready` / `partial` / `needs_representation` 三态）。
3. agent 在外部执行 OCR / vision / 页面笔记 / metadata 提取 / 内容画像，把产物用 **`kb_prepare_representation`** + **`kb_upsert_representation`** 写到 `.llm-kb/representations/` 下，每条 representation 标 kind（如 `ocr_text`、`metadata`）。
4. 用 **`kb_read_representations`** 校验现有 representation trail 是否齐全。
5. 只有当 representation trail 存在、`compile_readiness=ready` 时，agent 才被允许 **`kb_upsert_source_note`** 把最终的 source note 落到 wiki/sources/。

这条路径的设计意图：

- **把"理解非文本资产"的随机性隔离在 agent 一侧**——runtime 不依赖 OCR / vision 引擎，确保 runtime 自身可以无 GPU、无外部 API 跑。
- **保留 grounding trail**：`kb_lint` 会检查 multimodal source note 是否有"a believable review trail"。如果 source note 引用的事实在 representations 里找不到，lint 会发警告。这意味着多模态笔记的可信度可以被自动复核。
- **manifest schema v2** 新增字段 `raw_kind`、`mime_type`、`size_bytes`、`asset_refs`、stored representations，把"这条 source 是什么类型 / 看过哪些资产 / 存了哪些中间产物"在 manifest 里串起来。
- **source note 校验**：source 笔记里的 `raw_kind`、`mime_type`、`asset_paths` 必须和实际 reviewed assets 对齐，否则 lint 会报不一致。

边界 / 反例：

- runtime **不会**自动跑 OCR 或 vision；如果 agent 跳过 representation 步骤直接写 source note，`compile_readiness` 不会到 `ready`，lint 会标 `needs_representation`。
- 当代理切换、模型升级导致旧的 representation 过期时，lint 会标 `stale representations`——但 runtime 不会自动重生成，要 agent 来做。
- representation 路径只覆盖列举出的 raw kinds；其它 mime（如视频、音频）目前不在 schema 内。

## References

- 两条 ingest 路径定义：`data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` L77–95（"Multimodal Ingest Model"）。
- 支持的 raw kinds 与 manifest v2 字段：同文件 L46–55（"What 0.4.4 Implements" 前段）。
- compile_readiness 三态与 lint 检查项：同文件 L66–73 + L172–174。
- representation 相关命令：同文件 L62（`.llm-kb/representations/` 与 `kb_prepare_representation` / `kb_upsert_representation` / `kb_read_representations`）。

## Footnotes

- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` L79-92：两路径全文 + `"The runtime intentionally does not perform OCR or vision itself."`
- 同文件 L51-52：支持的 raw kinds（text / PDF / image / structured data 各自的扩展名清单）。
- 同文件 L52-53：`"manifest schema version 2, including raw_kind, mime_type, size_bytes, asset_refs, and stored representations"`。
- 同文件 L67-68：`"compile-readiness tracking with ready, partial, and needs_representation"`。
- 同文件 L69: `"source note validation that keeps raw_kind, mime_type, and asset_paths aligned with the actual reviewed assets"`。
- 同文件 L73: lint 项里包含 `"missing representation trails, stale representations, inconsistent asset_paths"`。
