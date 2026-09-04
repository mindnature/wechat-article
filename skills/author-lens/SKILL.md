---
name: author-lens
description: 在研究完成后生成多个竞争性作者判断，既淘汰平庸角度，也淘汰难以形成清晰读者交付的“深但不好读”角度。
version: "0.7"
reads: [topic, research, account, production, workflow]
writes: [author, workflow]
resources: [../shared/account-profiles.md, ../shared/voice-profiles.md, ../shared/voice-samples/manifest.yaml, ../../docs/AUTHOR-VOICE.md, ../../docs/VOICE-CALIBRATION.md, ../../docs/CLARITY-DELIVERY.md]
---

# AuthorLens｜作者视角层

本 Skill 位于 ResearchPack 与 ArticleArchitect 之间。

v0.7 不再把“越深越好”当唯一方向。最优 POV 必须同时满足：有判断、对读者有用、足够具体、能组织成清晰交付结构。

## 前置门
- `workflow.stage: research`
- `workflow.gate: ready`
- 核心 Claim 可用
- Standard/Deep Originality Gate 达标
- Standard/Deep `topic.tension_test.status=pass`

## Step 1｜为什么写
指出具体细节、矛盾、措辞、案例或数据，不能写“因为这是热点”。

## Step 2｜强制生成3个 POV 候选
必须恰好3个，而且彼此真正不同。

```yaml
- pov_id: P01
  thesis: ""
  evidence_refs: [C001]
  tension: ""
  decision_change: ""
  banality_self_critique: "为什么它仍可能只是第二显然"
  replaceability: high | medium | low
  evaluation:
    novelty: 1-5
    reader_value: 1-5
    specificity: 1-5
    frameworkability: 1-5
    evidence_strength: 1-5
  framework_preview:
    - "01 ..."
    - "02 ..."
    - "03 ..."
  risk: ""
```

至少覆盖：
- 一个从材料异常/矛盾出发；
- 一个从读者现实决策出发；
- 一个允许更锋利、可能反对主流叙事的判断。

## Step 3｜POV竞争不只比“深”
五项一起看：
- novelty：是不是人人都会说
- reader_value：读者看完会不会改变决定
- specificity：能不能落到具体任务/对象/动作
- frameworkability：能不能自然组织成3–5个清晰交付单元
- evidence_strength：证据是否足以支撑

一个“哲学上更深”但 frameworkability=1、specificity=1 的 POV，不应自动胜出。

知识型公众号优先选择：
> 有一个明确判断 + 能变成清晰1234框架 + 每一部分都有具体例子。

## Step 4｜主动枪毙两类坏角度
优先淘汰：
1. 第二显然：任何AI资讯号都能直接推出；
2. 深但悬空：听起来深，却不能回答读者“所以我具体怎么判断/怎么做”；
3. decision_change 只有“多关注/多学习/提高认知”；
4. 需要靠夸大证据才能锋利；
5. framework_preview 只能写成“背景/原因/意义/建议”的通用模板。

写入 rejected_pov_ids 与理由。

## Step 5｜Selected POV 必须能生成一句 Core Answer
在进入 Architect 前，先写：

```yaml
author:
  provisional_core_answer: "一句可直接回答标题的问题"
```

它必须：
- 具体；
- 能改变读者判断；
- 能在第一屏出现；
- 能被后续3–5个Delivery Units拆开证明。

如果只能写成“AI正在重塑高校工作”，视为未通过。

## Step 6｜Entry Point + Decision Change
入口必须具体，并附：content / evidence_refs / decision_change。

如果判断成立，读者必须会改变一个具体决定，例如：
- 哪类工作交给Agent；
- 哪类工作仍亲自做；
- 是否报名某培训；
- 是否采用某工具；
- 是否改变研究/教学流程。

## Step 7｜Material Graveyard
继续使用信息单元而非废话字数：Standard/Deep 默认 discarded_units >= retained_units。

每条墓地材料记录 refs / summary / why_excluded / weight。

“因为与标题承诺无关”是有效排除理由。

## Step 8｜真实不确定性绑定
第一人称犹豫、保留判断只允许引用 research.uncertainty_nodes。

没有Uxxx，不得表演式犹豫。

## Step 9｜Narrative Choice 与 Macro Structure Preview
Narrative Choice 仍保留，但新增宏观结构预览。

对于思然日新/知己/天工/经世的大多数知识型稿件，默认允许：
`01 / 02 / 03 / 04`。

只有叙事本身是内容价值时，才优先 narrative/hybrid。

反模板不等于反编号。

## Step 10｜Voice Calibration
Voice Profile 低权重；用户确认样例高权重。没有确认样例则标 uncalibrated。

## Step 11｜Humanity + Clarity Test
进入 Architect 前检查：
1. 是否真的生成3个POV并淘汰2个？
2. 最显然角度是否被淘汰？
3. selected POV 是否有具体 decision_change？
4. provisional_core_answer 能否在一句话里回答标题？
5. framework_preview 是否能自然变成3–5个读者交付单元？
6. 每个单元是否有具体对象/任务，而不是抽象概念？
7. material graveyard 是否形成真实取舍？
8. 是否存在假犹豫/伪第一人称？

若“深度高但清晰度低”，不要硬进写作；回 author 重选POV。

## 输出
Human Summary：3个POV候选、五维评价、淘汰理由、最终POV、provisional core answer、framework preview、具体入口、decision_change、材料墓地、真实不确定性、Voice Calibration。

State Patch：`author.*`；通过后 `workflow.stage: author, gate: ready`。

## 禁止
- 只生成一个POV
- 把“更深”自动等同“更适合公众号”
- 用抽象宏大判断压过读者实际收益
- 用“我觉得”代替作者性
- 用假犹豫制造人味
- 未经用户确认把历史稿当Voice正例
