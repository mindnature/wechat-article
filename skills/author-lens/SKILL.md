---
name: author-lens
description: 在研究完成后提炼作者真正想说的话、个人判断、具体切入点与叙事选择，避免结构化研究直接泄漏成AI说明文。
version: "0.5"
reads: [topic, research, account, production, workflow]
writes: [author, workflow]
resources: [../shared/account-profiles.md, ../shared/voice-profiles.md, ../../docs/AUTHOR-VOICE.md]
---

# AuthorLens｜作者视角层

本 Skill 位于 ResearchPack 与 ArticleArchitect 之间。

它不负责补事实，也不负责写全文。它只回答一个问题：

> 这篇文章为什么必须由这个账号来写，而不是任何一个通用AI都能写？

## 前置门
- `workflow.stage: research`
- `workflow.gate: ready`
- 核心 Claim 已可用
- Standard / Deep 的 Originality Gate 已满足最低要求

## Step 1｜作者为什么想写
不要复述“因为这是热点”。必须给出更具体的动机：
- 哪个细节让作者停下来多看了一眼？
- 哪个说法让作者觉得不对劲、过度简化或被忽略？
- 这件事与账号长期关注的问题有什么真实连接？

写入 `author.why_write`。

## Step 2｜作者真正的判断
用1–3句话写出 POV：
- 作者同意什么？
- 不同意什么？
- 最想提醒读者什么？

POV 可以是 opinion / inference，但不能伪装成事实。

## Step 3｜挑一个具体入口
优先从以下入口中选一个，而不是默认“先介绍新闻背景”：
- 一个反常细节
- 一个数字
- 一句官方措辞
- 一个具体岗位/JD/产品/页面
- 作者亲测中的一个瞬间
- 一个真实人物或场景
- 一个作者自己也曾误判的问题

写入 `author.entry_point`。

如果没有足够具体的入口，标记 `author.voice_risk: high`，优先回 ResearchPack 补案例/细节，而不是靠文风硬救。

## Step 4｜个人材料与作者资产
整理本篇可合法使用的作者材料：
- first_hand_experience
- field_observation
- personal_judgment
- test_result
- calculation
- analogy_from_other_domain
- uncertainty

禁止编造任何第一人称经历。

如果当前没有作者亲历，也可以保留“明确判断 + 独立选择 + 具体证据”形成作者性，但不得假装亲历。

## Step 5｜主动删东西
研究包越丰富，越容易写成AI百科。

必须列出 `author.material_to_ignore`：
- 哪些背景虽正确但不服务主线
- 哪些数据不必写
- 哪些标准答案式建议不写
- 哪些“为了完整”才出现的段落应删除

原则：宁可只说透一个判断，也不要把所有资料都写进去。

## Step 6｜Narrative Choice
从内容本身选择一种最自然的叙事，不强制情绪模板：
- single-thread：沿一个问题一路挖到底
- scene-led：从具体场景展开
- evidence-led：从一个证据/数字展开
- argument-led：围绕一个明确判断推进
- case-led：沿一个案例拆机制
- diary-led：适合真实亲测/过程记录
- compare-led：两件事并置产生理解

只选一个主结构。允许中途自然偏移，但禁止“每篇都反转”。

## Step 7｜Voice Profile
读取 `../shared/voice-profiles.md` 对应账号。

输出本篇具体约束：
- voice_traits：3–5个
- preferred_moves：本篇可用的表达动作
- banned_moves：本篇尤其要避免的套路
- first_person_level：none | low | medium | high
- looseness：tight | natural | conversational

## Step 8｜Humanity Test
在进入 Architect 前检查：
1. 去掉作者名，这篇是否任何AI账号都能写？
2. 有没有至少一个具体选择，体现“作者决定讲什么、不讲什么”？
3. 有没有一句明确判断，而不是只有中立总结？
4. 有没有具体细节承载观点？
5. 是否仍然像“发生了什么→为什么重要→怎么办”的标准回答？

若第1或第5项答案明显为“是”，设置：
`workflow.gate: rework`
`workflow.return_to: author`

## 输出
### Human Summary
- 为什么写
- 作者POV
- 具体入口
- 可用个人/原创材料
- 主动删除的材料
- Narrative Choice
- 本篇声音约束
- Humanity Test

### State Patch
写入：
- `author.*`
- 通过后：`workflow.stage: author, gate: ready`

## 禁止
- 把“普通人该怎么办”自动当成作者观点
- 用“我觉得”伪造作者性
- 为了人味虚构经历、情绪或聊天
- 强制制造反转
- 为了完整把ResearchPack全部写进正文
