---
name: research-pack
description: 为高潜选题建立可核验研究包，形成 Source Registry、Evidence Ledger、Calculation Ledger、Scope 与分级 Originality Gate。
version: "0.5"
reads: [signal, topic, account, production, workflow]
writes: [research, topic.evidence_confidence, workflow]
resources: [../../docs/ORIGINALITY-RUBRIC.md, ../../docs/PRODUCTION-MODES.md]
---

# ResearchPack｜深度素材研究

遵循 v0.5 ArticleState、JSON Schema 和 Skill Contract。

## 目标
把选题做实，让关键主张可追溯、范围清楚、计算可复现，并建立符合生产模式的原创增量。

ResearchPack 只负责“有什么证据可用”，不负责把所有资料都推进正文。材料取舍由后续 AuthorLens 完成。

## Step 1｜Source Registry
为来源建立唯一 `Sxxx` ID，记录 publisher/url/date/type/authority。

权威等级：
- A：官方原文、论文原文、财报、项目主页、原始数据库
- B：权威媒体直接采访/专业来源
- C：普通媒体二手转述
- D：社交帖子、搬运、未核验自媒体

D级不能单独支撑关键事实。

## Step 2｜Evidence Ledger
所有标题、导语、核心结论候选事实写入 `research.claims`，必须通过 `claim.schema.json`。

规则：
- 地方规则不得 national
- 单个案例不得行业泛化
- partial/disputed/unsupported 原则上不得 title_safe
- inference/opinion 必须显式区分

## Step 3｜Calculation Ledger
房贷、收益率、成本、同比、回收期等必须记录：假设、公式、inputs、result、sensitivity、verification。

检查单位、年/月口径、名义/实际利率、税费、百分比基数、四舍五入。

## Step 4｜七层素材
原始来源、关键事实、关键数字、时间线、人物/案例、舆论争议、反方与限制。

## Step 5｜分级 Originality Gate
读取 `ORIGINALITY-RUBRIC.md`。

每个原创资产写：
```yaml
- asset_id: O001
  level: A | B | C
  type: calculation | test | interview | proprietary_experience | comparison | synthesis | dataset | screenshot | other
  description: ""
  evidence_refs: []
```

门槛：
- Flash：允许 conditional；必须明确资讯属性
- Standard：至少 1×A 或 2×B
- Deep：至少 1×A + 1×B

普通截图、常规汇总、摘要属于 C，不能单独过门。

绝不伪造亲测、采访、内部经验。

## Step 6｜模式化研究深度
### Flash
优先锁定 3–5 条关键 Claim；可简化时间线/争议，但事实门不降。

### Standard
完整 Evidence Ledger + 限制条件 + 原创资产。

### Deep
扩大竞争扫描与反证；A类原创资产必须进入核心论证，可增加实验/访谈/数据集。

## Step 7｜为 AuthorLens 准备“可选材料池”
除研究包本身外，额外提示：
- 最奇怪/最具体的一条证据
- 最可能形成作者判断的争议点
- 一个可作为入口的真实细节
- 哪些材料虽然正确但可能只是背景噪音

这些只是候选，不直接决定文章结构。

## Step 8｜可视化素材池
记录可用真实图、截图页面、图表数据、生成解释图机会及权利风险。

## Step 9｜研究门
通过：
- 核心 Claim 可支撑
- Scope 清楚
- 关键数字可核验
- Originality 达到对应模式要求或 Flash conditional

则：`workflow.stage: research, gate: ready`。

阻断条件：源头不可追、关键数字冲突、Scope不清、关键标题事实 unsupported/false、Standard/Deep 原创门 fail。

阻断时：
```yaml
workflow:
  stage: research
  gate: blocked
  blocked_by: [C003]
  return_to: research
```

## 输出
Human Summary：研究摘要、Source Registry、Evidence Ledger、Calculation Ledger、原创资产、限制、可视化池、AuthorLens候选入口、证据缺口、title_safe事实。

State Patch：仅 `research.*`、`topic.evidence_confidence`、`workflow.*`。

## 禁止
- 为凑素材引用低质量转载
- AI生成事实/采访/网友评论
- 忽略冲突证据
- 只给计算结果不给假设与公式
- 用C级“截图/汇总”冒充深度原创
- 因为搜到了很多资料就默认全部进入正文
