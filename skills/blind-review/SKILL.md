---
name: blind-review
description: 在不知道生产pipeline规则的独立上下文中，对成稿做匿名语感盲测，定位最像AI的段落与句子；同上下文自评不得通过。
version: "0.6"
reads: [writing, account, workflow]
writes: [blind_review, workflow]
resources: [../shared/voice-samples/manifest.yaml, ../../docs/BLIND-REVIEW.md]
---

# BlindReview｜独立盲审

## 核心原则
Blind Review 的价值来自“评审者不知道生产规则”。

因此以下情况均不算有效盲审：
- Writer 与 Reviewer 是同一次模型调用；
- Reviewer 能看到 AuthorLens、Architecture、Anti-Template 规则；
- Reviewer 已知道哪些段落是“为了过规则”写的；
- 只是让同一上下文再次给自己打分。

## 前置门
- `workflow.stage: writing`
- `writing.body_status` 至少 revised/final
- 已生成 `blind_review.packet`

## Step 1｜独立性声明
必须记录：
```yaml
blind_review:
  evaluator_independence: fresh_session | different_model | same_context | unknown
```

只有 `fresh_session` 或 `different_model` 可获得正式 pass。

如果当前环境只能同上下文：
`status: pending_external`
`workflow.gate: manual_review`

不得自我盖章。

## Step 2｜最小盲审包
Reviewer 只能看到：
- 成稿正文；
- 可选：2–5段用户确认过的 Voice 正例与1–3段反例，匿名混排；
- 不提供 TopicHunter、ResearchPack、AuthorLens、Architecture、写作规则、作者POV标签。

如果没有用户确认过的样例，就做纯正文盲审，并标记 voice comparison unavailable。

## Step 3｜任务
让评审者只凭真实语感判断：
1. 哪3段最像AI？
2. 具体是哪一句/哪种连接方式暴露？
3. 哪些句子虽然正确，但像“模型为了完整而补的”？
4. 哪些地方像真人做了真实取舍？
5. 如果与匿名参考段混排，哪些段落最不像同一作者？

禁止只返回“自然/不自然”形容词。

## Step 4｜结构化 Findings
```yaml
findings:
  - finding_id: BR001
    severity: low | medium | high
    span: "原文短片段"
    issue: ""
    diagnosis: ""
    suggested_action: delete | merge | reorder | rewrite | keep
```

另外记录：
- `ai_likeness: low | medium | high`
- `voice_consistency: high | medium | low | unavailable`
- `strongest_human_passages`

## Step 5｜判定
### pass
- evaluator_independence 有效；
- ai_likeness != high；
- 无未解决 high severity AI-template finding。

### revise
存在明确可修问题，退回 writing。

### pending_external
无法提供独立上下文。

## 输出
Human Summary：最像AI的3处、最像真人的2处、逐句证据、建议动作、是否通过。

State Patch：
- pass：`workflow.stage: blind_review, gate: ready`
- revise：`workflow.stage: blind_review, gate: rework, return_to: writing`
- pending_external：`workflow.stage: blind_review, gate: manual_review, return_to: blind_review`

## 禁止
- 同一生产上下文假装盲审
- 评审者先读pipeline规则再“凭语感”
- 只打一个A/B分数不指出原句
- 未经用户确认把历史稿当Voice黄金样本
