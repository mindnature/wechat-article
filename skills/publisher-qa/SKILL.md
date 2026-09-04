---
name: publisher-qa
description: 发布前对证据链、Scope、计算、独立盲审结果、视觉资产、版权、隐私和读者体验做硬质检；不再由同一上下文自评文风。
version: "0.6"
reads: [topic, research, author, architecture, writing, blind_review, visual, account, production, workflow]
writes: [qa, workflow]
resources: [../shared/voice-samples/manifest.yaml, ../../docs/BLIND-REVIEW.md]
---

# PublisherQA｜公众号发布前硬质检

## 前置门
必须 `workflow.stage: visual`。

Standard/Deep 进入 visual 前已经通过独立 BlindReview；Flash 可跳过。

若 `visual.assets_ready=false`，整体最多 B，退回 visual。

## Step 1｜证据链
核对标题和正文 sections 的 Claim/Calc/Source 引用、statement type、Scope。

## Step 2｜事实与标题
检查 title_safe、数字、范围、确定性，不为了点击扩大事实。

## Step 3｜真实不确定性
如果正文出现“还不能确定/我会保留判断/目前只能看到”等表达：
- 必须能追到 Uxxx；
- 不得把 Writer 自造犹豫当文风。

## Step 4｜Originality 与 Depth
- Flash：资讯属性明确即可
- Standard：≥1A 或 ≥2B
- Deep：≥1A+1B

同时检查：
- Tension Test 是否仍成立；
- selected POV 是否真正改变读者某个决定；
- 材料墓地是否有真实取舍。

QA 不负责重新生成 POV。

## Step 5｜Blind Review 是文风主证据
PublisherQA 不再把自己的 `voice_match` 当作主要依据。

Standard/Deep A 的必要条件：
- `blind_review.status=pass`
- `evaluator_independence=fresh_session|different_model`
- `ai_likeness != high`
- 无 unresolved high-severity finding

如果 blind review 未做或由 same_context 完成：最多 B / manual_review。

QA 可补充机械检查，但不能推翻有效独立盲审，也不能用同上下文自评分数替代它。

## Step 6｜Writer Process Audit
检查：
- generation_trace 是否真实记录 isolated_segments 或 fallback
- 是否完成 reorder/delete pass
- Anti-Template pass 是否通过

`single_context_fallback` 不是直接失败，但会提高 BlindReview 重要性。

## Step 7｜视觉就绪
A 必须 assets_ready=true，封面和必需文中图 ready，无 avoid 权利风险，无高隐私风险。

## Step 8｜手机端与读者价值
检查移动端可读性，以及文章至少提供一个主价值：新信息、新判断、实用决策、替读者表达或明确分享对象。

## 最终评级
### A｜可进入 PublishingPlan
事实、Scope、计算、Originality/Depth、独立 BlindReview、视觉、版权/隐私均无阻断。

### B｜修改后再审
包括 blind review pending、作者角度仍浅、视觉未完成等可修问题。

### C｜暂缓
核心事实失证、严重Scope错误、证据断裂、关键计算错误、核心命题不成立。

## State Patch
- `qa.status`
- `qa.blocking_issues`
- `qa.recommended_fixes`
- `qa.voice_review.blind_review_status`
- A：`workflow.stage: qa, gate: ready`
- B：`gate: rework/manual_review`
- C：blocked/manual_review

## 禁止
- 同一上下文自己写、自己评、自己给A
- 用“语气自然”覆盖盲审指出的具体AI句
- 把不存在的U节点当真实犹豫依据
- 只改词不处理结构问题
