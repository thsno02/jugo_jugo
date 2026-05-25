# 人提问，LLM 维护

statement: 该来源把人的角色描述为负责来源策展、探索、提出问题、指挥分析和理解意义；把 LLM 的角色描述为负责写作、维护、总结、交叉引用、归档和簿记等知识库劳动。

fact_type: known_fact

support: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:15-16` 说明用户通常很少亲自写 wiki，而由 LLM 写作并维护；同一段把人的职责列为来源、探索和提出正确问题，把 LLM 的职责列为总结、交叉引用、归档和簿记。`data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:68-69` 进一步概括：人负责策展来源、指挥分析、提出好问题并思考意义，LLM 负责其余工作。

scope: 仅限该来源对人机分工的描述；不外推为所有 LLM 知识库、所有 Obsidian 工作流或所有人机协作模式的通用规则。

status: accepted

provenance: `llm_wiki/kb/provenance/llm-wiki-human-llm-role-division.md`

## 说明

这张卡只记录来源中的角色划分：人主要承担方向、来源和问题层面的判断，LLM 主要承担知识库内容与结构的持续维护工作。

## References

- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:15-16`
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:68-69`

## Footnotes

- `status: accepted` 表示该事实已通过本轮审计和采纳流程，但仍只在 `scope` 限定范围内成立。
