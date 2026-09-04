# Skill Contract｜v0.7

所有子 Skill 遵循统一状态、证据链、深度生成、读者交付与独立盲审契约。

## 1. Stage / Gate
`workflow.stage`：
`signal | topic | research | author | architecture | writing | blind_review | visual | qa | publishing | published | reviewed`

`workflow.gate`：`ready | blocked | rework | manual_review`。

## 2. Truth Gate
Evidence / Calculation / Scope 继续保持严格。`research.uncertainty_nodes` 只允许真实证据不确定性驱动犹豫表达。

## 3. Tension + Reader Promise Gate
Standard / Deep 在 Research 前必须同时通过：

### Tension Test
- 具体 contradiction / unresolved question；
- 具体 decision_change；
- exclusive material path 或 strong judgment candidate 至少一个成立。

### Reader Promise Test
- promise 具体；
- provisional_answer 不为空；
- knowledge/tool/decision类文章能预览3–5个交付单元；
- “了解趋势/提高认知”不能作为有效承诺。

## 4. Author Competition Gate
AuthorLens 必须：
- 恰好3个真正不同的 POV；
- 每个都有 banality_self_critique；
- 每个评价 novelty / reader_value / specificity / frameworkability / evidence_strength；
- 淘汰至少2个；
- selected POV 的 reader_value / specificity / frameworkability / evidence_strength 不得过低；
- 生成 `provisional_core_answer`；
- Material Graveyard 满足 `discarded_units >= retained_units`。

最深的POV不自动胜出；必须兼顾可读和可交付。

## 5. Reader Contract Gate
ArticleArchitect 必须冻结：
- promise_type
- promise
- core_answer
- answer_shape
- expected_units
- delivery_units

标题问什么，正文必须显式交付什么。

对于 `which | how | list`，默认使用 `numbered_framework`，并至少3个Delivery Units。

## 6. Thesis Prominence Gate
Standard / Deep 默认要求核心结论在第一屏出现：
- `required_in_first_screen=true`
- 默认 `max_chars <= 300`

强叙事/调查稿可以延迟，但必须记录 `delayed_reason`。

## 7. Macro Structure Rule
01/02/03/04 本身不是AI模板。

知识型、工具型、决策型、政策解读型文章默认允许并鼓励清晰编号。

Anti-Template 只打击微观重复：同长度、同句式、同反转、同总结、同升华。

## 8. Concrete Delivery Gate
每个 Delivery Unit 至少需要：
- unit_id
- label
- answer
- concrete_examples

大类词不算具体交付。

例如“文献研究”必须继续拆到：
`搜索→下载→去重→提取→矩阵→Gap`。

## 9. Segmented Generation + Clarity Pass
Writer 继续使用：
- isolated_segments 或 single_context_fallback
- segment_count
- reorder_pass

但在 BlindReview 前新增 `writing.clarity_pass`：
- first_screen_excerpt
- thesis_in_first_screen
- promise_delivery_status
- numbered_framework_used
- missing_delivery_units
- evidence_overload_first_screen
- concrete_task_coverage

Clarity不过，不进入BlindReview。

## 10. Real Uncertainty
第一人称犹豫/保留判断只能引用 Uxxx。不许用“可能/我也不确定”模拟人味。

## 11. Voice Calibration
Voice Profile 只是低权重边界；真正风格依据用户确认的正/反 Voice Samples。未确认历史稿不得自动升格为Gold Sample。

## 12. Blind Review
Standard / Deep 在 VisualEditor 前必须独立 BlindReview。

有效：`fresh_session | different_model`。

无效：`same_context`。

BlindReview审AI感、语感、Voice，不替代 Reader Contract / Thesis Prominence / Promise Delivery。

## 13. PublisherQA
QA=A 必须同时通过：
- Truth / Scope / Calculation
- Originality
- Thesis Prominence
- First Screen
- Promise → Delivery
- Concrete Delivery
- Anti-Template
- Independent BlindReview
- Visual Ready / Rights / Privacy

## 14. Failure Routing
- 张力弱/Reader Promise弱：回 topic
- 材料不足：回 research
- POV深但不可交付：回 author
- Reader Contract不清：回 architecture
- 核心结论埋太深/标题未兑现/具体任务不足：回 writing/architecture
- AI语感问题：回 writing，经独立BlindReview复审
- 视觉未完成：回 visual

## 15. Regression
v0.7 不可退化项：
- “哪些/怎么做”必须有明确编号交付
- 核心结论不能埋在后半篇
- 1234不能仅因“规整”被判AI味
- Delivery Unit不能只有抽象大类
- 深但frameworkability低的POV不能自动胜出
- same-context BlindReview仍必须失败
