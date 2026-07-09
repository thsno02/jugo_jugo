---
id: agt-mcp-security-gateway
title: AGT MCP 安全网关
status: draft
card_type: protocol-security-mechanism
tags: [mcp-security, tool-poisoning, drift-detection, typosquatting, hidden-instruction]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-microsoft-agent-governance-toolkit]
evidence_basis: code_implementation
justification: ../justification/agt-mcp-security-gateway.md
canonical_concept: mcp-security-gateway
aliases: [MCP Security Gateway, MCP Scanner, tool poisoning detection, description drift monitoring, mcp_security, MCP 安全网关]
summary: >-
  AGT 的 MCP Security Gateway 针对 MCP tool definitions 提供四类防护：tool poisoning detection、description drift monitoring、typosquatting checks、hidden instruction scanning。127 conformance tests。保护 agent 免受恶意或被篡改的 MCP tool 影响。mcp-security-gateway MCP Scanner tool poisoning drift typosquatting
related: [agt-deterministic-policy-enforcement, agt-privilege-ring-sandboxing]
---

AGT 提供专门的 MCP Security Gateway，针对 Model Context Protocol (MCP) tool definitions 的安全威胁进行防护 [^src-1]。

四类检测能力：
1. **Tool poisoning detection** -- 识别恶意注入的 tool 定义
2. **Description drift monitoring** -- 监控 tool 描述的意外变更
3. **Typosquatting checks** -- 检测名称相似的仿冒 tool
4. **Hidden instruction scanning** -- 扫描 tool 定义中隐藏的指令注入

[^src-1]

该网关有 127 conformance tests 和独立 spec (MCP-SECURITY-GATEWAY-1.0) [^src-2]，与 [^card-1] 中的策略引擎配合——MCP Gateway 识别威胁后，策略引擎执行 deny 决策。

[^src-1]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "MCP Security Gateway" P1 -- "Tool poisoning detection, description drift monitoring, typosquatting checks, and hidden instruction scanning for MCP tool definitions."
[^src-2]: `data/raw/github_repo/repo-microsoft-agent-governance-toolkit/repo/README.md` -- "Specifications" P1 -- "MCP Security Gateway ... Tool poisoning, drift detection, hidden instructions | 127"
[^card-1]: agt-deterministic-policy-enforcement -- 策略引擎作为 MCP Gateway 检测结果的执行层
