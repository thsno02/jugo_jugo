Agent Governance Toolkit¶
Runtime governance for AI agents: deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents.
13,000+Tests
 10Formal Specs
 5Languages
 20+Integrations
 Packages¶
  ⚙️ Agent OS Policy engine, agent lifecycle, governance gate   🔗 Agent Mesh Agent discovery, routing, and trust mesh   🛡️ Agent Runtime Execution sandboxing with four privilege rings   📊 Agent SRE Kill switch, SLO monitoring, chaos testing   ✅ Agent Compliance OWASP verification, policy linting, integrity checks   🏪 Agent Marketplace Plugin governance and trust scoring   ⚡ Agent Lightning RL training governance with violation penalties   🔒 Agent Hypervisor Execution audit, delta engine, commitment anchoring  
 Language SDKs¶
| SDK | Install | 
|---|---|
| 🐍 Python | pip install agent-governance-toolkit | 
| 📘 TypeScript | npm install @microsoft/agent-governance-sdk | 
| 🔷 .NET | dotnet add package Microsoft.AgentGovernance | 
| 🦀 Rust | cargo add agent-governance | 
| 🐹 Go | go get github.com/microsoft/agent-governance-toolkit/agent-governance-golang | 
Framework Integrations¶
Works with any agent framework: LangChain, CrewAI, AutoGen, Google ADK, OpenAI Agents, LlamaIndex, Haystack, Mastra, MCP, A2A, and more. See the full list.
Examples¶
| Example | Framework | What it demonstrates | 
|---|---|---|
| openai-agents-governed | OpenAI Agents SDK | Policy-gated tool calls with trust tiers | 
| crewai-governed | CrewAI | Multi-agent governance with role-based policies | 
| smolagents-governed | HuggingFace smolagents | Lightweight agent governance | 
| maf-integration | MAF | Microsoft Agent Framework integration | 
| mcp-trust-verified-server | MCP | Trust-verified MCP server implementation | 
Specifications¶
Every major component has a formal RFC 2119 specification with conformance tests.
| Specification | Tests | 
|---|---|
| Agent OS Policy Engine | 68 | 
| AgentMesh Identity and Trust | 135 | 
| Agent Hypervisor Execution Control | 80 | 
| AgentMesh Trust and Coordination | 62 | 
| Agent SRE Governance | 111 | 
| MCP Security Gateway | 127 | 
| Agent Lightning Fast-Path | 100 | 
| Framework Adapter Contract | 152 | 
| Audit and Compliance | 157 | 
| AgentMesh Wire Protocol | -- | 
25 Architecture Decision Records document the reasoning behind key design choices.
Standards Compliance¶
| Standard | Coverage | 
|---|---|
| OWASP Agentic AI Top 10 | All 10 risks covered with deterministic controls | 
| NIST AI RMF 1.0 | Full GOVERN, MAP, MEASURE, MANAGE alignment | 
| EU AI Act | Compliance mapping with automated evidence | 
| SOC 2 | Control mapping with audit trail export |