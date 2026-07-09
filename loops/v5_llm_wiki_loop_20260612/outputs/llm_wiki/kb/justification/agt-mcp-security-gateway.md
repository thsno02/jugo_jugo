# Justification: agt-mcp-security-gateway

## 为什么产出此卡
MCP Security Gateway 是一个独立能力模块，有独立 spec 和 127 tests，且针对当前 agent 生态中 MCP 协议的特定安全问题（tool poisoning / drift / typosquatting / hidden instructions），构成独立原子概念。

## Evidence basis 判定
选择 `code_implementation`：有具体实现文件路径 (agent_os/mcp_security.py)、独立 spec、127 conformance tests。

## Hedge 说明
无显式 hedge——四类检测能力为材料直接陈述。
