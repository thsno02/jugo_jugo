---
id: llm-wiki-manifest-schema-v2
title: LLM Wiki 清单 Schema v2 元数据模型
status: accepted
card_type: data-model
tags: [llm-wiki, manifest, schema, metadata, structured-data]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
justification: ../justification/llm-wiki-manifest-schema-v2.md
canonical_concept: llm-wiki-manifest-schema-v2
aliases: [manifest schema v2, 清单模式v2, manifest.json schema, 元数据模型]
summary: >-
  llm-wiki-manifest-schema-v2（清单模式v2 / manifest.json schema）llm-wiki-karpathy v0.4.4 引入的清单元数据模型，新增 raw_kind/mime_type/size_bytes/asset_refs/representations 五个字段，驱动编译就绪判断与源笔记验证
related: [representation-first-ingest, llm-wiki-vault-three-layer-shape, llm-wiki-deterministic-lint]
---

llm-wiki-karpathy v0.4.4 引入了 manifest schema version 2，扩展了 `.llm-kb/manifest.json` 中每条源记录的元数据字段[^src-1]。新增的五个字段共同支撑了多模态摄入和验证流程：

| 字段 | 用途 |
|------|------|
| `raw_kind` | 原始资料类型（text、pdf、image、structured）|
| `mime_type` | MIME 类型，用于精确识别文件格式 |
| `size_bytes` | 文件大小，用于预估处理成本 |
| `asset_refs` | 资产引用列表，关联原始文件与其衍生产物 |
| `representations` | 已存储的中间表示记录（OCR 文本、视觉描述等）|

这些字段服务于多个运行时操作[^src-2]：
- **编译就绪判断**——`kb_prepare_source_bundle` 根据 representations 字段判断资产处于 `ready`、`partial` 还是 `needs_representation` 状态
- **源笔记验证**——运行时确保 `raw_kind`、`mime_type` 和 `asset_paths` 与实际已审查的资产一致
- **lint 健康检查**——`kb_lint` 利用这些字段检测不一致的 asset_paths 和缺失的表示链

Schema v2 还支撑了「安全原始资产检查」——`kb_get_raw_asset` 返回确定性元数据加安全的绝对路径供本地查看器使用[^src-3]。整体设计将清单从简单的文件列表提升为多模态知识管理的状态追踪核心。

## Footnotes

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "manifest schema version 2, including raw_kind, mime_type, size_bytes, asset_refs, and stored representations"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "compile-readiness tracking with ready, partial, and needs_representation" 和 "source note validation that keeps raw_kind, mime_type, and asset_paths aligned with the actual reviewed assets"
[^src-3]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "safe raw-asset inspection through kb_get_raw_asset, including deterministic metadata plus a safe absolute path for local viewers"
