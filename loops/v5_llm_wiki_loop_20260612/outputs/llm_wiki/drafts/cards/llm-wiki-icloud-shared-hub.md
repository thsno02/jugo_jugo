---
id: llm-wiki-icloud-shared-hub
title: iCloud Drive 共享 Hub 配置
status: draft
card_type: how-to
tags: [llm-wiki, icloud, shared-hub, multi-mac, permissions]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-icloud-shared-hub.md
canonical_concept: icloud-shared-hub-config
aliases: [iCloud hub, shared wiki hub, multi-Mac wiki, iCloud 共享配置]
summary: >-
  icloud-shared-hub-config：hub 可设为 iCloud Drive 路径使多 Mac 可见，config 存于 ~/.config/llm-wiki/config.json，共享 config 用逻辑 hub_path 非绝对用户路径，wikis.json 用相对 topic paths，macOS 隐私权限按 Mac 和启动进程隔离需分别授权
related: [llm-wiki-hub-architecture, llm-wiki-zero-runtime-dependencies]
---

llm-wiki 支持将 hub 设置为 iCloud Drive 路径以便多 Mac 共享同一 wiki。通过 `/wiki config hub-path "~/Library/Mobile Documents/com~apple~CloudDocs/wiki"` 配置，写入 ~/.config/llm-wiki/config.json。[^src-1]

关键规则：共享 config 应使用逻辑路径（hub_path），不写机器特定的绝对用户目录。wikis.json 条目应存储相对 topic paths（如 topics/bitcoin），而非 /Users/alice/.../topics/bitcoin。[^src-2]

macOS 隐私权限是按每台 Mac 和确切启动进程（launcher app）隔离的。同一 Apple ID 同步的文件，在一台机器上可读在另一台可能返回 Operation not permitted。需为不同启动方式分别授权 Full Disk Access。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "iCloud" P209-211 -- "Set the hub with a portable path: /wiki config hub-path..."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "iCloud" P211 -- "New configs should keep hub_path and avoid writing a machine-specific resolved_path. Shared wikis.json entries should store topic paths such as topics/bitcoin, not /Users/alice/.../topics/bitcoin."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "FAQ" P297 -- "macOS privacy permissions are local to each Mac and to the exact process launching the agent."
