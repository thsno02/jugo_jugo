# Justification: compile-readiness-tracking

## 提取理由
compile readiness 是 representation-first 架构的核心控制机制，有明确的三态定义。

## 证据锚定
- 材料 L22: "compile-readiness tracking with ready, partial, and needs_representation"
- 材料 L21: kb_prepare_source_bundle 返回 compile_readiness

## 原子性
单一机制：三态就绪度追踪及其在工作流中的作用。
