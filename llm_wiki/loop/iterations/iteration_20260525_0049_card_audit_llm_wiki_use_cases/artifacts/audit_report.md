# 审计报告：candidate 6

audit_result: pass
reason:
- 知识卡只表达一个主要事实：该来源列举了 LLM Wiki 的一组可能应用场景。草稿的 `statement`、`support` 和正文都围绕这个来源清单展开，没有扩展成主题覆盖或用例体系。
- `statement` 被 `raw.txt:17-23` 支撑。来源第 17 行引出示例清单，第 19-23 行列出 Personal、Research、Reading a book、Business/team，以及 Competitive analysis、due diligence、trip planning、course notes、hobby deep-dives。草稿把这些英文项整理为个人记录、长期研究、读书陪伴 wiki、业务团队内部 wiki等中文表述，未增加新场景。
- `fact_type: known_fact` 合理，因为本卡记录的是“来源明说列举了这些场景”这一可由文本直接核对的事实，不是已采纳知识库事实。
- `scope` 清楚限制为“仅限该来源列举的可能应用场景”，并明确不声称已验证有效，也不声称清单穷尽全部用法。
- `support` 足够具体，指向 `raw.txt:17-23`，并列出对应场景名称。出处论证也说明了来源明说部分、中文整理方式和成立范围，可以 justify 该卡暂时成立。
- 正文可读，符合 zet 风格知识卡的短事实记录方式。`References` 位于 `Footnotes` 前，`Footnotes` 是最后一个 section。
- 未发现枢纽页、聚类、主题覆盖或复杂元数据漂移。
required_changes:
- 无。
residual_risk:
- 证据只来自一个来源片段，且部分中文名称是对英文清单项的压缩整理；后续采纳时应继续保持“该来源列举”这一限定，避免写成实际有效性或完整用例分类。
