# Blind Review｜独立语感盲审协议

## 为什么存在
同一个模型、同一条上下文里的 Writer 与 QA 容易共享盲点。Writer 觉得自然的句子，Reviewer 也可能因为看过同样的规则而觉得自然。

Blind Review 不是再加一层普通检查，而是改变评审信息条件。

## 有效独立性
有效：
- fresh_session：同一模型但全新会话，且不提供pipeline规则
- different_model：不同模型/供应商，且不提供pipeline规则

无效：
- same_context
- Reviewer 能看到 AuthorLens、Anti-Template、POV 或“这篇为什么这么写”的解释

## Blind Packet
只给：
1. 成稿正文
2. 可选：用户确认过的 Voice 正例/反例，匿名混排

不给：
- 研究过程
- Evidence Ledger
- AuthorLens
- Architecture
- Anti-Template rules
- Writer 自评

## 评审问题
- 哪3处最像AI？请引用具体短句。
- 哪些段落是“为了完整而补出来”的？
- 哪些连接词/转折暴露了模型节奏？
- 哪些地方像作者做了真实取舍？
- 与匿名参考段相比，哪几段最不像同一作者？

## 输出
不追求一个伪精确分数。使用：
- ai_likeness: low | medium | high
- voice_consistency: high | medium | low | unavailable
- findings[]：原句、问题、严重度、建议动作

## 流程门
Standard / Deep 在进入 VisualEditor 前，必须有独立 Blind Review pass。

如果当前运行环境无法提供独立上下文：
- status=pending_external
- workflow.gate=manual_review
- 不得由同上下文自评替代。

Flash 可以跳过，但应记录 skipped_for_speed。
