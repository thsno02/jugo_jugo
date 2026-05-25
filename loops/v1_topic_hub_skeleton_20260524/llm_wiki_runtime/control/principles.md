# LLM Wiki Topic KB 原则

1. `loop_plan_init_kb.md` 是生产协议，不是内容主题。
2. `data/` 是 LLM Wiki topic KB 的 primary evidence layer。
3. Topic nodes 必须围绕 LLM Wiki 本体：起源、定义、架构、工作流、生态、证据、风险、比较和边界。
4. 不再把 `current_kb_initialization_loop`、`provenance_as_core_knowledge_asset` 这类 meta-production nodes 写入 active topic KB，除非作为方法附录或 archive。
5. 每个 topic claim 尽量回到 raw source；manifest/digest 可作为导航和 secondary evidence。
6. Citation 必须解释 `why_cited` 和 `evidence_summary`，不能只贴路径。
7. Provenance 必须说明 raw paths、manifest rows、prior KB nodes、process artifacts 和 synthesis boundary。
8. 动态检索只在本地 data 不足时使用；公司电脑网络受限时，有限尝试后记录并延期。
9. `kb/` 只渲染 adopted topic nodes。
10. Demo-0 meta KB 保存在 `archive/demo_0_meta_kb_initialization_20260524/`，可审计但不作为 active topic KB。
