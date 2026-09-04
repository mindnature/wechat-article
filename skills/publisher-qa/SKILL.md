---
name: publisher-qa
description: 在公众号发布前对标题、首屏、结构、证据、Scope、计算、图片、版权、隐私和读者收益做硬质检。
version: "0.3"
reads: [topic, research, architecture, writing, visual, account]
writes: [qa, status]
---

# PublisherQA｜公众号发布前质检

## 目标
在文章进入微信公众号后台或正式发布前完成结构化终检。发现会影响点击率、完读率、推荐理解、可信度、版权/隐私和读者体验的问题，并给出最小必要修改。

遵循 `../../schemas/article-state.yaml` 与 `../../docs/SKILL-CONTRACT.md`。

## 硬规则
1. 事实优先于表达。
2. 标题不能制造超出 Evidence Ledger 的承诺。
3. 标题、导语、核心结论里的硬事实必须能映射到 Claim/Calc。
4. Scope 扩大属于事实错误，不是“措辞问题”。
5. 真实图负责证据，生成图不能冒充现实证据。
6. 发现阻断问题时允许把状态退回 ResearchPack/Writer/VisualEditor。

## Step 1｜标题质检
检查：
- 主题是否明确
- 是否有目标人群/利益/冲突/数字/反差
- 是否与正文一致
- 是否过度夸张
- 是否省略 Scope 后造成误导
- 标题硬事实是否 `title_safe: true`
- 数字是否来自已验证 Claim/Calc

评分可作为编辑参考，但不得覆盖硬性事实问题。

## Step 2｜首屏质检
重点检查前250–300字：
- 核心事件/冲突是否快速出现
- 读者是否知道“与我有什么关系”
- 是否铺垫过长
- 是否有阅读收益
- 是否重复标题
- 所有事实钩子是否有证据ID

## Step 3｜结构与价值质检
检查：
- 核心命题是否一致
- 每节是否服务主命题
- 新闻复述是否过长
- 信息增量是否太晚
- 情绪线是否由信息推进产生
- 是否重复论证
- 是否连续长段无视觉锚点
- Originality Gate 是否满足文章类型

标准/深度文章若 `commodity_content_risk: high`，至少评为 B；若没有任何新增价值且依赖二手资料堆砌，可评 C。

## Step 4｜Evidence Ledger 对账
逐项核验标题、导语、关键数字和核心判断：

### Fact
必须：`verification=verified` 或在正文明确呈现 partial/disputed。

### Scope
检查原文表述是否超出 Claim Scope。

例如：
- `city` 不得写成“全国”
- `institution` 不得写成“高校都”
- `single_case` 不得写成“行业正在”

### Calculation
必须存在：
- assumptions
- formula
- inputs
- result
- verification

文章里的数字必须与 Ledger 一致。

### Inference / Opinion
不得伪装为来源原话或确定事实。

使用标签：
`Verified | Needs source | Scope mismatch | Calculation mismatch | Inference | Opinion | Risky claim`。

## Step 5｜去AI腔
重点寻找：
- 套路化反转：真正、不是而是、看似其实
- 空泛升华
- 过密三段式/排比
- 每节机械“首先/其次/最后”
- 没有作者判断或真实细节
- “拭目以待”式结尾

只修改影响阅读的部分，不为了“去AI”故意粗糙化。

## Step 6｜视觉、版权与隐私
检查：
- 封面是否一眼识别主题
- 每张图是否有功能
- 需要证明的内容是否用了真实图
- 生成图是否可能被误认为真实现场
- 图源是否可追溯
- rights_status 是否存在 needs_confirmation/avoid
- 是否有水印/转载限制/隐私
- 数据图是否改变原始含义

仅标图源不能自动消除版权风险。

## Step 7｜手机端排版
检查：
- 段落长度
- 小标题跳读能力
- 是否过度加粗/颜色/符号
- 图注/引用/表格是否可读
- 是否存在视觉断层

## Step 8｜四个读者问题
必须能回答：
1. 为什么点？
2. 为什么读完？
3. 为什么转发？
4. 为什么关注这个账号？

## 最终评级
### A｜可发布
无阻断性事实/Scope/计算/版权/隐私问题。

### B｜修改后发布
存在1–3个影响点击、留存、可信度或原创性的可修复问题。

### C｜暂缓发布
出现任一：
- 核心事实无法核验
- 标题与正文严重不符
- Scope严重扩大
- 关键数字错误或计算不可复现
- 图片严重误导/隐私/版权风险
- 核心命题不成立

## 输出
### Human Summary
- 发布结论 A/B/C
- 标题/首屏/结构/事实/读者收益/视觉评分（仅辅助）
- 必改问题≤5
- 建议优化≤5
- 事实风险表
- 图片风险表
- 替代标题（如需要）

### State Patch
- `qa.status`
- `qa.blocking_issues`
- `qa.recommended_fixes`
- A时 `status: qa_passed`
- B/C时保留当前状态并指出应退回模块

## 发布清单
- [ ] 标题与正文一致
- [ ] 标题硬事实 title_safe
- [ ] 关键事实可追溯
- [ ] Scope未扩大
- [ ] 自算数字可复现
- [ ] 真实图图源可追溯
- [ ] 生成图无伪证据风险
- [ ] 无明显隐私泄露
- [ ] 手机端阅读顺畅
- [ ] 有明确转发理由
