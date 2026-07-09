# Justification: claude-first-multi-runtime-packaging

## 抽卡理由
多运行时包装策略展示了如何从单一行为规范生成多平台分发——这是 LLM 插件生态中的一个实际工程问题。同步脚本 + 漂移检测测试是该策略的实现机制。

## 证据强度
- README "Claude-First, Multi-Runtime" 段完整描述
- CLAUDE.md Project Structure 列出文件布局
- sync-codex-plugin.sh 实际同步脚本代码
- 支持客户端对比表（5 种运行时）
- evidence_basis: code_implementation

## 原子性检验
单一核心 idea：一个行为源 + 多个生成的包装层 + 自动漂移检测。
