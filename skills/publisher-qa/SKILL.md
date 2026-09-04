---
name: publisher-qa
description: 发布前对标题、首屏、证据链、Scope、计算、视觉资产、版权、隐私和读者收益做硬质检。
version: "0.4"
reads: [topic, research, architecture, writing, visual, account, production, workflow]
writes: [qa, workflow]
---

# PublisherQA｜公众号发布前硬质检

遵循 v0.4 ArticleState、Schema 与 Skill Contract。

## 前置门
必须 `workflow.stage: visual`。

若 `visual.assets_ready=false`，不能给最终 A；正文可通过但整体最多 B，并退回 visual。

## Step 1｜证据链完整性
对标题、首屏、每个 `writing.sections` 检查：
- claim_ids 是否存在于 Evidence Ledger
- calc_ids 是否存在于 Calculation Ledger
- source_section_id 是否能追到架构（Flash 可空）
- statement_types 与 Claim 类型是否一致

任何引用不存在 → 阻断。

## Step 2｜标题
检查主题、目标人群、利益/冲突/数字、正文一致性、title_safe、Scope、计算假设。

## Step 3｜首屏
前250–300字是否快速出现事件/冲突、读者关系和收益；硬事实必须有 Claim/Calc。

## Step 4｜Evidence / Scope / Calculation
### Fact
verified 可直接陈述；partial/disputed 必须显示不确定性。

### Scope
city/institution/company/single_case 不得扩大成 national/行业普遍。

### Calculation
必须有 assumptions、formula、inputs、result、verification；正文数字与 Ledger 一致。

### Inference / Opinion
不得伪装成来源原话或确定事实。

## Step 5｜Originality
按 production.mode 检查：
- Flash：允许 conditional，但必须资讯属性清楚
- Standard：≥1A 或 ≥2B
- Deep：≥1A+1B，且A级进入核心正文

不达标：Standard/Deep 至少 B，严重则 C。

## Step 6｜视觉就绪
A 的必要条件：
- visual.assets_ready=true
- cover ready
- required inline assets ready
- 无 rights_status=avoid
- 无未解决高隐私风险
- 生成图无伪证据风险

## Step 7｜去AI腔与结构
检查套路化反转、空泛升华、机械排比、新闻复述过长、重复论证、信息增量太晚。

## Step 8｜手机端
段落、小标题、图注、表格、视觉节奏适合移动端。

## Step 9｜四个读者问题
为什么点？为什么读完？为什么转发？为什么关注？

## 最终评级
### A｜可进入 PublishingPlan
事实、Scope、计算、原创、视觉、版权/隐私均无阻断问题。

### B｜修改后再审
可修复问题；必须写 return_to。

### C｜暂缓
核心事实失证、Scope严重扩大、关键计算错误、证据引用断裂、严重版权/隐私风险、核心命题不成立。

## 输出
Human Summary：A/B/C、必改≤5、优化≤5、证据风险表、图片风险表、替代标题（需要时）。

State Patch：
- `qa.*`
- A：`workflow.stage: qa, gate: ready`
- B：`gate: rework, return_to: <module>`
- C：`gate: blocked/manual_review`

## A级硬清单
- [ ] 标题硬事实 title_safe
- [ ] 正文 Claim/Calc 引用有效
- [ ] Scope 未扩大
- [ ] 自算数字可复现
- [ ] Originality 达到模式门槛
- [ ] visual.assets_ready=true
- [ ] 无严重版权/隐私风险
- [ ] 手机端可读
- [ ] 有明确转发理由
