---
name: publisher-qa
description: 发布前对证据链、Scope、计算、作者存在感、模板风险、视觉资产、版权、隐私和读者体验做硬质检。
version: "0.5"
reads: [topic, research, author, architecture, writing, visual, account, production, workflow]
writes: [qa, workflow]
resources: [../shared/voice-profiles.md, ../../docs/AUTHOR-VOICE.md]
---

# PublisherQA｜公众号发布前硬质检

遵循 v0.5 ArticleState、Schema 与 Skill Contract。

## 前置门
必须 `workflow.stage: visual`。

若 `visual.assets_ready=false`，不能给最终 A；正文可通过但整体最多 B，并退回 visual。

## Step 1｜证据链完整性
对标题和每个 `writing.sections` 检查：
- claim_ids 是否存在于 Evidence Ledger
- calc_ids 是否存在于 Calculation Ledger
- source_section_id 是否能追到架构（Flash 可空）
- statement_types 与 Claim 类型是否一致

任何引用不存在 → 阻断。

## Step 2｜标题与事实
检查：
- 标题是否与正文同一主问题
- hard facts 是否 title_safe
- Scope 是否被标题省略后造成误导
- 数字是否有可复现来源/计算
- 是否为了点击夸大确定性

## Step 3｜开头只审“是否值得继续读”
取消旧版“前250–300字必须同时出现事件/冲突/读者关系/收益”的检查。

改为检查：
- 是否从具体入口进入，而不是套话铺垫
- 是否很快出现一个事实、细节、判断、问题或场景
- 是否存在连续抽象过渡句
- 是否为了钩子虚构悬念

不同文章可以有不同开头。

## Step 4｜Evidence / Scope / Calculation
### Fact
verified 可直接陈述；partial/disputed 必须显示不确定性。

### Scope
city/institution/company/single_case 不得扩大成 national/行业普遍。

### Calculation
必须有 assumptions、formula、inputs、result、verification；正文数字与 Ledger 一致。

### Inference / Opinion
不得伪装成来源原话或确定事实。

## Step 5｜Originality 与 Author Voice 分开检查
Originality 按 production.mode 检查：
- Flash：允许 conditional
- Standard：≥1A 或 ≥2B
- Deep：≥1A+1B

然后单独检查作者性：
- 有没有明确 POV，而不是只有中立总结
- 有没有一个具体入口承载观点
- 有没有主动取舍，而不是把ResearchPack写全
- 是否符合对应账号 Voice Profile
- 是否用虚构第一人称制造“人味”

Originality PASS 不代表 Author Voice PASS。

## Step 6｜Anti-Template Review
A 的必要条件之一：`writing.anti_template_pass.status=pass`。

重点识别结构级AI痕迹：
- What → Why → So what → How 过于明显
- 每节长度接近
- 每节都“概括→解释→总结”
- 每节都需要一个反转
- 过渡句密度高于具体信息
- 连续使用“更值得关注的是/这意味着/对普通人来说”等结构句
- 最后机械生成三条建议/六步法/宏大升华

发现后优先建议删段、合段、换入口、改变顺序，而不是只换同义词。

## Step 7｜Author Presence Test
问三个问题：
1. 去掉账号名，是否任何AI资讯号都能原样发布？
2. 读者能否说出“作者这一篇到底判断了什么”？
3. 文章里是否存在至少一个只有经过取舍才会形成的表达选择？

输出 `qa.voice_review`：
- author_presence: high | medium | low
- template_risk: low | medium | high
- voice_match: high | medium | low

Standard/Deep 若 `author_presence=low` 或 `template_risk=high`，最多 B，退回 author/writing。

## Step 8｜视觉就绪
A 的必要条件：
- visual.assets_ready=true
- cover ready
- required inline assets ready
- 无 rights_status=avoid
- 无未解决高隐私风险
- 生成图无伪证据风险

## Step 9｜手机端与节奏
不以“段落长度一致”为好。

检查：
- 是否有大段难读
- 小标题是否真的需要
- 是否数字编号过多造成模板感
- 图注/表格手机端可读
- 视觉节奏是否服务内容

## Step 10｜读者价值
不再强制每篇同时回答“为什么点/读完/转发/关注”四项。

至少明确一个主价值：
- 有用
- 新判断
- 新信息
- 替读者表达
- 可分享给特定对象

## 最终评级
### A｜可进入 PublishingPlan
事实、Scope、计算、原创、作者声音、Anti-Template、视觉、版权/隐私均无阻断问题。

### B｜修改后再审
包括：作者性偏弱、模板风险高、视觉未完成等可修问题。必须写 return_to。

### C｜暂缓
核心事实失证、Scope严重扩大、关键计算错误、证据断裂、严重版权/隐私风险、核心命题不成立。

## State Patch
- `qa.status`
- `qa.blocking_issues`
- `qa.recommended_fixes`
- `qa.voice_review`
- A：`workflow.stage: qa, gate: ready`
- B：`gate: rework, return_to: <author|writing|visual|research>`
- C：`gate: blocked/manual_review`

## A级硬清单
- [ ] 标题硬事实安全
- [ ] 正文证据引用有效
- [ ] Scope 未扩大
- [ ] 自算数字可复现
- [ ] Originality 达标
- [ ] Author Presence 至少 medium
- [ ] Template Risk low/medium 且 Anti-Template pass
- [ ] Voice Match 至少 medium
- [ ] visual.assets_ready=true
- [ ] 无严重版权/隐私风险
