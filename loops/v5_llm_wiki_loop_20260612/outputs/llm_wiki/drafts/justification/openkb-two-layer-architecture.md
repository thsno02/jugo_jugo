# Justification: openkb-two-layer-architecture

## 为什么产出此卡
材料明确将系统划分为两层并分节详述各层职责。这是理解 OpenKB 功能组织的关键架构卡，与设计哲学卡互补但原子性不同——本卡聚焦"怎么组织"而非"为什么存在"。

## Evidence basis 选择
`code_implementation`：README 中列出的命令均为已实现的 CLI 命令（pip install openkb 可用）。

## 拆卡决策
wiki foundation 内部的知识编译流程（add 时的四步）足够原子且与架构总论紧耦合，合并入本卡。Skill Factory 作为独立生成器拆为专卡。PageIndex 作为底层检索技术拆为专卡。
