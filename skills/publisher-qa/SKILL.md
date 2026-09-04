---
name: publisher-qa
description: 发布前检查事实、独立盲审、视觉与读者交付；新增 Thesis Prominence、First-Screen、Promise→Delivery 和具体任务覆盖硬门。
version: "0.7"
reads: [topic, research, author, architecture, writing, blind_review, visual, account, production, workflow]
writes: [qa, workflow]
resources: [../shared/voice-samples/manifest.yaml, ../../docs/BLIND-REVIEW.md, ../../docs/CLARITY-DELIVERY.md]
---

# PublisherQA｜公众号发布前硬质检

## 前置门
必须 `workflow.stage: visual`。

Standard/Deep 已通过独立 BlindReview；Flash可跳过。

visual.assets_ready=false → 整体最多B，退回visual。

## Step 1｜证据链与事实
核对标题和正文 Claim/Calc/Source、Scope、statement type、title_safe。

## Step 2｜Thesis Prominence｜核心结论突出度
Standard/Deep默认要求：
- `writing.clarity_pass.status=pass`
- `thesis_in_first_screen=true`
- 前300个中文字符能读到 core_answer 的等价表达
- 若标题为问题型，第一屏已有方向性答案

例外只允许 Architect 已记录合理 delayed_reason 的强叙事/调查稿。

如果最强观点埋在后半篇：最多B，退回 writing/architecture。

## Step 3｜First-Screen Gate
第一屏必须包含核心结论，并至少再完成以下一项：
- 明确告诉读者会拿到什么框架；
- 给一个具体事实/场景建立可信度。

检查：
- 是否被Benchmark缩写、参数、背景复述占满；
- 是否连续出现读者不需要先知道的术语；
- 是否300字读完仍说不出文章准备回答什么。

`evidence_overload_first_screen=true` → 最多B。

## Step 4｜Promise → Delivery Gate
读取 `architecture.reader_contract`，逐项核对标题承诺。

- which：是否明确给出“哪几类”，并逐类回答？
- how：是否给出步骤/动作？
- why：是否给出清楚因果链？
- compare：是否同口径比较？
- decide：是否有判断标准、代价和结论？
- list：是否真的交付标题承诺的数量/清单？

要求：`writing.clarity_pass.promise_delivery_status=pass` 且 missing_delivery_units为空。

标题问A、正文主要讲B → 最多B；严重误导 → C。

## Step 5｜Macro Clarity ≠ AI Template
编号结构本身不构成AI风险。

对于知识/工具/决策/政策文章：
- 01/02/03/04 是积极导航信号；
- 小标题应能单独说明本节答案；
- 读者扫一眼小标题，应能复述全文框架。

Anti-Template只检查微观机械重复：每节同长度、同句式、同反转、同总结。

禁止因为“结构太清楚”要求Writer拆掉编号。

## Step 6｜Concrete Delivery
对于“哪些工作/场景/怎么做”类标题：
- 每个Delivery Unit至少一个具体任务链/案例/动作；
- “教学/科研/管理/文献研究”这种大类词不能单独算交付；
- 必须能让读者想象明天具体怎么做。

`concrete_task_coverage != pass` → 最多B。

## Step 7｜Evidence / Uncertainty / Originality
继续执行v0.6硬门：Scope、Calculation、Uxxx真实不确定性、Originality、Tension、Material Graveyard。

证据服务结论，不要求把所有研究量展示在正文。

## Step 8｜Blind Review
Standard/Deep A的必要条件：
- blind_review.status=pass
- evaluator_independence=fresh_session|different_model
- ai_likeness != high
- 无未解决high finding

BlindReview负责语感与AI感，不能替代Clarity/Promise检查。

## Step 9｜Writer Process Audit
检查 segmented generation、reorder/delete pass、Anti-Template pass。

single_context_fallback不是直接失败，但提高BlindReview权重。

## Step 10｜视觉就绪
A必须assets_ready=true；封面/文中必需图ready，无严重版权隐私风险。

## 最终评级
### A
事实 + Scope + Originality + Thesis Prominence + Promise Delivery + Concrete Delivery + BlindReview + Visual 全部通过。

### B
最常见：结论埋太深、标题承诺未完整兑现、编号框架不清、具体任务不足、盲审pending、视觉未完成。

### C
核心事实失证、严重Scope错误、标题承诺实质误导、证据断裂、关键计算错误。

## State Patch
- qa.status
- qa.blocking_issues
- qa.recommended_fixes
- qa.clarity_review:
  - thesis_prominence
  - first_screen
  - promise_delivery
  - macro_structure
  - concrete_delivery
- qa.voice_review.blind_review_status

A → workflow.stage=qa, gate=ready。

## 禁止
- 同一上下文自己写、自己评、自己给A
- 把1234编号当成AI味
- 只审语气、不审标题承诺有没有兑现
- 允许核心观点埋到后半篇
- 允许“哪些工作”只写成几个抽象大类
- 用Benchmark研究量替代可读性
