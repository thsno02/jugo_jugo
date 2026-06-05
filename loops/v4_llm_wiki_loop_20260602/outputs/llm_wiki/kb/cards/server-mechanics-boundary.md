---
id: server-mechanics-boundary
title: 服务器力学边界原则
status: accepted
card_type: distinction
tags: [llm-wiki, design-boundary, server, schema-validation, separation-of-concerns]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [pypi-llm-wiki-mcp]
justification: ../justification/server-mechanics-boundary.md
canonical_concept: server-mechanics-boundary
aliases: [力学边界, mechanics boundary, 服务器不验证内容, server enforces mechanics not content]
summary: >-
  server-mechanics-boundary（力学边界 / mechanics boundary / 服务器不验证内容）
  是 llm-wiki-mcp 的设计边界原则：服务器只强制执行力学层（原子写入、乐观并发、路径限制、日志格式），
  刻意不验证内容形状（frontmatter/分类/链接目标）——"将 schema 烘焙进服务器会违背初衷"
related: [optimistic-concurrency-etag, schema-as-configuration, three-layer-architecture]
---

llm-wiki-mcp 的设计核心是一条明确的**力学-内容边界**：服务器强制执行力学（mechanics），而非内容形状（content shape）[^src-1]。

**服务器强制执行的力学层**包括四项[^src-2]：

1. **原子写入**——页面写入采用 tmp-file + fsync + rename；日志追加采用 `O_APPEND` 单次写入
2. **乐观并发**——etag（`sha256(body) || mtime_ns`）的 CAS 机制
3. **路径限制**——slug 正则验证 + 解析路径与 wiki 根目录 realpath 比对，阻止 CVE-2025-53109 类型的符号链接逃逸攻击[^src-3]
4. **格式锁定的日志行**——`## [YYYY-MM-DD] operation | Title`，操作名为自由字符串，仅拒绝会破坏行格式的字符[^src-4]

**服务器刻意不做的事**：不验证 frontmatter 形状、页面分类或链接目标。这一层存在于 `wiki/CLAUDE.md` schema 文档中，随 LLM 的使用而增长[^src-5]。

**设计论据**：「Karpathy 的 gist 对内容形状刻意保持沉默；将 schema 烘焙进服务器会违背初衷」[^src-6]。这意味着服务器承担的是「LLM 反复犯错的无聊层」——保证数据完整性，而将领域语义的演化权交给 schema 文档和 LLM 本身[^src-7]。

## Footnotes

[^src-1]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L177 -- "The server enforces mechanics, not content shape"
[^src-2]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L179-186 -- "Atomic writes... Optimistic concurrency... Path containment... Format-locked log line"
[^src-3]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L183-184 -- "Slugs are regex-validated. Resolved paths are checked against the realpath of the root, blocking the CVE-2025-53109 symlink-escape class."
[^src-4]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L185-186 -- "Format-locked log line. ## [YYYY-MM-DD] operation | Title. Operation names are free strings; only characters that would break the line shape are rejected."
[^src-5]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L187 -- "The server does not validate frontmatter shape, page categories, or link targets. That layer lives in your wiki/CLAUDE.md schema doc and grows with the LLM."
[^src-6]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L187 -- "Karpathy's gist is deliberately silent on content shape; baking a schema into the server would defeat the point."
[^src-7]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` -- L117 -- "The server handles the boring layer LLMs keep getting wrong: atomic writes, etag conflict checks, append-only log integrity, path containment."
