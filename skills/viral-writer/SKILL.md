---
name: viral-writer
description: 基于已验证选题、研究包和证据绑定架构生成可发布公众号正文，并保持事实、计算、推断和观点边界。
version: "0.3"
reads: [topic, research, architecture, account, learning]
writes: [writing, status]
---

# ViralWriter｜公众号成稿

## 目标
把 ArticleArchitect 的结构写成完整公众号文章。优先保证信息价值、可信度、可读性、转发价值和作者独特性，不追求模板化“爆款腔”。

遵循 `../../schemas/article-state.yaml` 与 `../../docs/SKILL-CONTRACT.md`。

## 前置门
只有以下条件满足才进入：
- `status: architected`
- Originality Gate 为 pass，或 conditional 且文章明确为快讯/简报
- 核心段落已绑定 Claim/Calc/Case

标准/深度文若 `commodity_content_risk: high`，必须提示补一手增量，原则上不直接输出“高完成度深度稿”。

## 核心原则
1. 写给具体读者。
2. 新闻事实、计算结果、作者推断、个人观点必须保持语气边界。
3. 数据、案例、场景优先于空泛观点。
4. 保留“活人感”，但不伪造亲测、经历、采访或内部消息。
5. 长度由信息价值决定。
6. 标题高信息量、清晰完整，不制造超出 Evidence Ledger 的承诺。

## 默认长度
- 抢热点：1000–1500字
- 标准文章：1500–2500字
- 深度调查/案例：2500–5000字
用户另有要求时以用户要求为准。

## Step 1｜加载账号与学习规则
读取：
- `../shared/account-profiles.md`
- `../../learning/proven-patterns.md`
- 如有需要读取对应账号基线/假设

只有 Level 2/3 规则可以当稳定规则；Level 0/1 只能作为实验提示。

## Step 2｜按证据绑定大纲写正文
每节只能使用架构中绑定的 Claim/Calc/Case，新增事实必须先补 ResearchPack。

语气规则：
- `fact + verified`：可陈述
- `calculation`：必须快速交代关键假设
- `inference`：使用“更可能/这意味着/可以理解为”等判断语气
- `opinion`：明确是作者判断
- `partial/disputed`：必须显示不确定性

## Step 3｜开头
前250–300字尽快出现：
- 事实/场景
- 冲突/反差
- 读者关系
- 阅读收益

禁止空泛时代感开场，也禁止使用未核验事实做强钩子。

## Step 4｜信息密度与节奏
- 正常段落2–4句为主
- 允许少量一句话重点段
- 每300–500字至少出现一种有效信息：事实、数据、案例、机制、决策框架或有依据判断
- 不为了“短”删掉必要证据，也不为“深度”堆无关背景

## Step 5｜语言
- 中文自然、直接、具体
- 减少模板词：真正、不是……而是、看似、其实、值得注意的是、不得不说
- 不滥用感叹号、排比、宏大结论
- 专业概念首次出现时用普通人能理解的话解释

## Step 6｜标题
正文完成后生成12–20个候选，覆盖：
- 事件 + 冲突
- 人群 + 利益
- 数字 + 反差
- 事件 + 决策
- 案例 + 机制

每个候选标题检查：
- 所有硬事实是否 `title_safe: true`
- Scope 是否被标题省略后造成误导
- 计算数字是否需要在标题/导语快速给出假设

最终推荐3个。

## Step 7｜图片占位
按 `architecture.visual_nodes` 插入：
`[插图：功能｜内容｜为什么这里需要]`

不编造图片；真实图写建议来源，生成图写表达目标。

## Step 8｜结尾
优先：决策建议、行动清单、回扣开头、开放问题。
文末关键词标签≤5个。

## 输出
### Human Summary
1. 推荐标题 TOP3
2. 完整正文
3. 图片占位
4. 文末标签
5. 待核验/边界风险

### State Patch
- `writing.title_candidates`
- `writing.selected_title`
- `writing.body_status: draft/final`
- `writing.word_count`
- `writing.risk_notes`
- `status: drafted`

## 自检
- 标题事实均可追溯
- 前300字有继续读的理由
- 没有“只有观点没有证据”的长段
- 个案没有写成趋势
- Scope没有扩大
- 计算结果没有脱离假设
- 没有明显AI套话
- 至少存在一个可转发理由：有用、替我表达、让我显得懂、值得提醒别人

## 禁止
- 编造采访/数据/亲测
- 新增无法追溯的事实性细节
- 把推断写成事实
- 为点击制造超出证据范围的标题
- 结尾强行升华
