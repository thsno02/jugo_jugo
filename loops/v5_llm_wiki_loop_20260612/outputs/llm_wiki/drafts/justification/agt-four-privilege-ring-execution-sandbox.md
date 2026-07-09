# Justification: agt-four-privilege-ring-execution-sandbox

## 为什么产出此卡
此卡为 fusion card，合并了 agent-runtime-four-privilege-rings (docs) 和 agt-privilege-ring-sandboxing (code repo) 两张卡。两张原卡描述同一概念（AGT 四特权环执行沙箱）但各自有对方不包含的独特知识：docs 版提供 Agent Hypervisor 能力和 80 项规范测试；code 版提供具体环名称（kernel/supervisor/user/untrusted）、Saga orchestration、kill switch 和 Python middleware 层限制。

## 证据强度
- 四环名称 (kernel/supervisor/user/untrusted) 直接出自代码仓库 README
- Saga orchestration + kill switch 直接出自代码仓库
- Agent Hypervisor 三项能力直接出自官方文档
- 80 项合规测试直接出自官方文档
- Python middleware 限制直接出自代码仓库 Security 章节
- evidence_basis = documentation + code_implementation

## 原子性判断
本卡聚焦"AGT Agent Runtime 的四特权环执行沙箱模型"这一单一概念及其直接配套机制。

## Hedge 标注
无推测内容——所有论断均有直接引用。
