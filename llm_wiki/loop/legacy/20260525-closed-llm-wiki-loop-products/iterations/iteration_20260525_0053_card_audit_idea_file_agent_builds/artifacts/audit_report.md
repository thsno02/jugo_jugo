# 知识卡审计报告

audit_result: revise
reason:
- 草稿卡只表达一个主要事实：`idea file` 在这条发布帖中的分享逻辑是分享 idea，而不是交付具体 code/app，并由他人的 agent 按需求定制和构建。
- 草稿卡的核心 statement 被 `data/raw/webpage/karpathy-x-launch-post/raw.json` 的 `$.tweet.text` 支撑；原文包含 “less of a point/need of sharing the specific code/app”、“share the idea” 和 “other person's agent customizes & builds it for your specific needs”。
- `fact_type: known_fact` 合理；当前证据只是单条发布帖字段，尚不足以标成 `accepted_fact`。
- `scope` 清楚限制在指定 raw.json 的 `$.tweet.text` 字段，不外推为行业通用定义。
- `support` 具体指出了 code/app、idea、agent customizes & builds 三个支撑点，能对应来源和候选 3。
- 出处论证能 justify 这张卡暂时成立，并说明整理表述没有扩展为外部事实。
- 正文可读，保持原子事实和简短说明，符合 zet 风格知识卡。
- `References` 在 `Footnotes` 前，`Footnotes` 是最后一个 section。
- 未出现枢纽页、聚类、主题覆盖或复杂元数据漂移。
- 需要修订的一点是：草稿卡 statement 写成 “Karpathy 的发布帖”，但允许使用的来源证据字段 `$.tweet.text` 本身没有直接证明发帖者身份；允许候选 3 也只写“这条帖子”。这属于可修订的来源支撑边界问题，不需要 reject。
required_changes:
- 将 statement 中 “Karpathy 的发布帖” 改为 “这条发布帖” 或 “该来源帖文”，除非采纳流程另行提供允许使用的作者/帖主元数据来源。
- 如保留 “Karpathy” 归属，需要把支撑来源限定为任务允许的可验证字段；当前任务包只允许 `$.tweet.text` 作为来源证据，不足以直接支撑该归属语。
residual_risk:
- 修订后仍然只是单一来源字段支持的 `known_fact`，适用范围应继续限于这条发布帖对 `idea file` 概念的表述。
