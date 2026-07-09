## Justification: long-context-recall-vs-safety-alignment

**为什么产出此卡**: 这是一个可复用的诊断方法论——区分"模型看不到攻击"vs"模型看到但拒绝"，对解释任何注入攻击实验结果有价值。

**Reframing 决策**:
- 聚焦方法论意义而非单纯数据报告
- 提炼"诊断原则"作为核心 takeaway
- 与 model-capability-security-disconnect 卡形成互补（那张卡用此诊断结果，本卡解释诊断方法本身）

**Hedge 标注**: 论文注明"仅测试了一种召回提示配置"，GPT-OSS-120B 低召回可能部分因空响应——此不确定性在卡中通过"严重 needle-in-haystack 失败"表述保留
