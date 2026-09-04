# Skill Contract｜v0.6

所有子 Skill 遵循统一状态、证据链、深度生成和独立盲审契约。

## 1. Stage / Gate
`workflow.stage`：
`signal | topic | research | author | architecture | writing | blind_review | visual | qa | publishing | published | reviewed`

`workflow.gate`：`ready | blocked | rework | manual_review`。

## 2. 事实层
保持 v0.5 的 Evidence / Calculation / Scope 规则不变。新增 `research.uncertainty_nodes`：只有真实证据不确定性才能驱动犹豫语气。

## 3. Tension Gate
Standard / Deep 在 Research 前必须通过 `topic.tension_test`：
- 具体 contradiction/unresolved question；
- 具体 decision_change；
- exclusive material path 或 strong judgment candidate 至少一个成立。

只有公开资料+第二显然观点，不应包装成深度稿。

## 4. Author Competition Gate
AuthorLens 必须：
- 生成恰好3个真正不同的 POV candidates；
- 每个写 banality_self_critique；
- 淘汰至少2个；
- selected POV 有具体 decision_change；
- Standard/Deep 记录 Material Graveyard，`discarded_units >= retained_units`。

## 5. Real Uncertainty
第一人称犹豫/保留判断只能引用 Uxxx。不许凭空生成“我也不确定”来模拟人味。

## 6. Voice Calibration
`voice-profiles.md` 只是低权重边界。

真正 Voice 依据 `voice-samples/manifest.yaml` 中用户确认的正/反例。历史稿未被用户明确标注，不得自动当正例。

## 7. Segmented Generation
Standard / Deep Writer 先建立局部 briefs，再优先分 invocation 生成 segments。

必须记录：
- strategy: isolated_segments | single_context_fallback
- segment_count
- isolated_context
- reorder_pass

初稿后必须单独执行重排/删减 pass，不能只改词。

## 8. Blind Review
Standard / Deep 在 VisualEditor 前必须执行独立 BlindReview。

有效独立性：`fresh_session | different_model`。

`same_context` 不算通过；当前环境不能提供独立上下文时，必须 `pending_external + manual_review`，不能自己给自己盖章。

Blind reviewer 不得看到：ResearchPack、AuthorLens、Architecture、Anti-Template 规则或 Writer 自评。

## 9. Blind Packet
只包含纯正文，以及可选的用户确认 Voice 样例匿名混排。Reviewer 必须指出具体AI句/段，而不是只打分。

## 10. PublisherQA
QA 继续负责事实、Scope、计算、版权、视觉；文风主证据改为独立 BlindReview，不再依赖同一上下文的 Voice Match 自评。

Standard/Deep QA=A 必须 blind_review pass。

## 11. Originality / Visual / Publishing / Learning
沿用 v0.5：Originality、Visual Ready、PublishingPlan、真实后台数据学习门不降低。

## 12. 失败处理
- 张力浅：回 topic
- 材料不足：回 research
- POV 平庸/取舍不足：回 author
- 连续生成节奏/AI痕迹：回 writing
- 无独立评审：manual_review / blind_review
- 视觉未完成：回 visual

## 13. 回归测试
不可退化项新增：
- Standard/Deep 必须有 Tension Test
- AuthorLens 必须3选1而非单次生成
- Graveyard 必须形成可审计取舍
- 假犹豫不能没有 Uxxx
- Writer 必须 segment + reorder
- same-context BlindReview 必须失败
- 未确认历史文章不能进入 Voice Gold Samples
