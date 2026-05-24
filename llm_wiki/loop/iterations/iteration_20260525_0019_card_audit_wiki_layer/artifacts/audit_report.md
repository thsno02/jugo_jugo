audit_result: pass
reason:
草稿卡只表达一个主要事实：在该来源描述的架构中，wiki 层是由 LLM 生成和维护的 markdown 文件目录，并列出其内容类型与维护职责。`statement` 中关于 markdown 文件目录、summaries、entity pages、concept pages、comparisons、overview、synthesis、LLM 创建页面、在新来源到来时更新页面、维护交叉引用并保持一致的说法，均由 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:31` 直接支撑。第 32 行为空行，不增加证据但也不冲突。

`fact_type: known_fact` 合理，因为该事实是来源明说内容的整理，不是已采纳事实。`status: draft` 与当前草稿阶段一致。`scope` 明确限制为“仅限该来源对 wiki 层的规定”，避免外推到所有 wiki 或所有 LLM 知识库。`support` 具体指出来源定义、内容类型和 LLM 职责，足以支撑 statement。出处论证区分了来源明说与整理表达，能 justify 该卡暂时成立。

正文可读，符合单张 zet 风格知识卡的压缩事实表达；未出现枢纽页、聚类、主题覆盖或复杂元数据漂移。`References` 位于 `Footnotes` 之前，`Footnotes` 是最后一个 section。
required_changes:
无。
residual_risk:
该卡仅由一处来源证据支撑，且来源证据只有第 31 行为实质内容；采纳后仍应保持当前 scope，不应扩展为通用 wiki 架构结论。
