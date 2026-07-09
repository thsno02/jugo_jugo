# Justification: agent-runtime-four-privilege-rings

## 为什么产出此卡
"四环特权模型"是该工具包中最具架构辨识度的设计概念之一，借鉴了 OS 特权环的经典模式并应用于 AI 代理执行隔离，值得独立建卡。

## 证据强度
- "four privilege rings" 和 "execution sandboxing" 直接出自文档
- 四环各层的具体定义文档未展开，卡片中已标注"据此推测"作为 hedge
- Agent Hypervisor 的三项能力（execution audit, delta engine, commitment anchoring）直接引用
- evidence_basis = documentation

## 原子性判断
本卡聚焦"Agent Runtime 的四环特权执行沙箱设计"这一单一概念。与 Agent Hypervisor 的配合关系属于该概念的必要上下文。

## Hedge 标注
- "据此推测该模型可能将代理操作从最高特权到最低特权分层管控" — 材料未展开四环细节，以推测标记
