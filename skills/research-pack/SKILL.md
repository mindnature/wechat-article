---
name: research-pack
description: 为高潜公众号选题建立可核验研究包，形成来源注册表、Evidence Ledger、Calculation Ledger、Scope 与 Originality Gate。
version: "0.3"
reads: [signal, topic, account]
writes: [research, topic.evidence_confidence, status]
---

# ResearchPack｜深度素材研究

## 目标
把一个高潜选题做实，形成可直接交给 ArticleArchitect 使用的研究包。重点不是搜得多，而是让每个关键主张可追溯、范围清楚、计算可复现，同时建立至少一种内容增量。

遵循 `../../schemas/article-state.yaml` 与 `../../docs/SKILL-CONTRACT.md`。

## 核心原则
1. 一手来源优先于二手转述。
2. 事实、计算、推断、观点必须分开。
3. 标题、导语和核心结论中的事实必须进入 Evidence Ledger。
4. 政策、规则、统计必须记录 Scope。
5. 自行计算必须记录假设、公式和结果，不能只留下最终数字。
6. 必须主动寻找反方证据、限制条件与失败案例。
7. 标准/深度文章在进入写作前必须过 Originality Gate。

## Step 1｜Source Registry
为来源建立唯一 ID：

```yaml
- source_id: S001
  title: ""
  publisher: ""
  url: ""
  published_at: ""
  source_type: official | primary | academic | company | media | social | secondary
  authority: A | B | C | D
  notes: ""
```

建议：
- A：官方原文、法律/政策、论文原文、财报、项目主页、原始数据库
- B：权威媒体直接采访/高质量专业来源
- C：普通媒体二手转述
- D：社交帖子、搬运、自媒体未核验信息

D 级不能单独支撑关键事实。

## Step 2｜Evidence Ledger
所有可能进入文章的关键主张写入 `research.claims`：

```yaml
- claim_id: C001
  text: ""
  type: fact | calculation | inference | opinion | unknown
  scope: global | national | province | city | institution | company | single_case | unknown
  source_ids: [S001]
  verification: verified | partial | disputed | unsupported | false | unknown
  confidence: high | medium | low
  title_safe: true | false
  note: ""
```

规则：
- 地方规则不得标成 national。
- 单个案例不得标成行业趋势。
- `partial/disputed/unsupported` 原则上不得作为标题核心。
- 推断可以写，但必须在正文中以判断语气呈现。

## Step 3｜Calculation Ledger
房贷、收益率、成本、同比、增长、回收期等自行计算写入：

```yaml
- calc_id: K001
  question: ""
  assumptions: []
  formula: ""
  inputs: {}
  result: ""
  sensitivity: ""
  verification: reproduced | checked | unchecked
```

必须检查：
- 单位
- 年/月口径
- 名义/实际利率
- 是否含税/手续费
- 百分比基数
- 四舍五入

计算结果用于标题时，标题或正文首个解释段必须快速交代关键假设。

## Step 4｜七层素材包
1. 原始来源
2. 关键事实
3. 关键数字
4. 时间线：此前—触发点—当前—下一步
5. 人物/案例
6. 舆论与争议
7. 反方与限制

社交平台观点只能代表讨论，不得当事实。

## Step 5｜Originality Gate
判断文章相较普通新闻/公开资料，是否至少增加一种：
- calculation：自主计算
- test：亲测产品/功能
- interview：访谈/小调查
- proprietary_experience：作者职业经验
- comparison：独立对比
- synthesis：新框架/跨源综合
- dataset：自行整理数据
- screenshot：一手页面/实验结果截图
- other

输出：
- `status: pass | conditional | fail`
- `original_value`
- `commodity_content_risk: low | medium | high`
- `missing_original_material`

规则：
- 热点快讯可在 conditional 下继续，但必须缩短、明确其资讯属性。
- 标准/深度文若 `fail + high risk`，原则上退回补素材，不直接进入 ViralWriter。
- 绝不伪造“作者亲测/采访/内部经验”。

## Step 6｜可视化素材池
同步记录：
- 可引用官方/产品/媒体真实图
- 推荐截图页面
- 可做信息图的数据
- 需要 AI 解释图的抽象概念
- 每张真实图建议图源与权利风险

## Step 7｜研究状态判断
### researched
关键主张可支撑，范围明确，核心数字可核验，Originality Gate pass/conditional。

### blocked
出现任一：
- 核心事实只有单一低质量来源
- 关键数字冲突无法解释
- 政策范围/主体不清
- 源头无法追溯
- 关键标题事实 unsupported/false

被 blocked 时不得装作研究完成。

## 输出
### Human Summary
1. 研究结论摘要（≤300字）
2. Source Registry
3. Evidence Ledger
4. Calculation Ledger
5. 时间线
6. 人物/案例
7. 舆论与争议
8. 反方与限制
9. Originality Gate
10. 可视化素材池
11. 未解决证据缺口
12. 可安全用于标题的事实

### State Patch
仅写：
- `research.*`
- `topic.evidence_confidence`
- `status: researched` 或保留/标记 blocked

## 禁止
- 为凑素材引用低质量转载站
- AI生成事实、数据、采访或网友评论
- 忽略冲突证据
- 把“可能/讨论”改写成“已经/全面”
- 只给数字不给假设和公式
