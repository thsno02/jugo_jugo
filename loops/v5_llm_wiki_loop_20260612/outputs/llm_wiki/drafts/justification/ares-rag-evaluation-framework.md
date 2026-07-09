# Justification: ares-rag-evaluation-framework

## 为什么产出此卡
材料（README.md）的核心主题即 ARES 框架本身，描述了其设计目标（最小化人工标注的 RAG 评估）和完整工作流程（合成数据→分类器→PPI）。这是材料最高层级的原子概念。

## Evidence basis 选择
选择 `code_implementation`：README 包含完整 Python 代码示例展示框架的各模块调用方式（ARES class 的 synthetic_query_generator、classifier_model、ppi 配置），属于代码实现层面的证据。

## 信息完整性
- 框架版本 v0.5.7，论文 arXiv:2311.09476
- 作者：Jon Saad-Falcon, Omar Khattab, Christopher Potts, Matei Zaharia
- 安装方式：pip install ares-ai
- 支持 OpenAI API 和 vLLM 本地部署
