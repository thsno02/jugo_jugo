# Justification: graphrag-prompt-auto-tuning

## 提取依据
材料 docs/prompt_tuning/overview.md 和 docs/prompt_tuning/auto_prompt_tuning.md 详尽描述了 auto-tuning 的动机、流程、文档选择策略、命令行参数和产出物。

## 原子性判断
Prompt Auto-Tuning 是一个独立的预处理功能，有明确的输入（原始文本）、算法（采样+LLM 推断+模板替换）和输出（3 个 prompt 文件），适合独立成卡。

## Evidence basis
code_implementation -- `graphrag prompt-tune` 是已实现的 CLI 命令，文档中有明确的使用示例。
