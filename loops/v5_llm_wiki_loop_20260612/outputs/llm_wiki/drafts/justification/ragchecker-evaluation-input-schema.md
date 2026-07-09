# Justification: ragchecker-evaluation-input-schema

## 为什么产出此卡
材料明确展示了 RAGChecker 的输入 JSON schema，包含完整字段定义和约束说明（唯一必需标注为 gt_answer）。该 schema 定义了用户接入框架的数据契约，是独立的原子知识单元。

## Evidence basis 选择: code_implementation
该 schema 直接从代码仓库的 examples/checking_inputs.json 格式规范中提取，README 以代码块形式呈现字段结构。

## 提取判断
- JSON schema 结构在 README 中以代码块完整给出
- "The only required annotation for each query is the ground truth answer" 是明确的约束陈述
- retrieved_context 作为列表结构在 schema 中有完整定义
