# WeChat Article｜公众号内容生产系统

面向微信公众号内容生产的模块化 AI Skills 工作流。目标不是“一个Prompt写全文”，而是把事实研究、作者视角、叙事选择、写作、视觉、发布与复盘拆开：后台高度结构化，前台保持作者性和自然表达。

## 当前版本：v0.5 Author Voice

v0.5 专门修复 v0.4 实跑暴露出的最大问题：文章事实正确、结构完整，但AI味仍然很重。

原因不是缺少禁词，而是后台工程结构泄漏到了前台：每篇都容易变成“发生了什么→为什么重要→说明什么→普通人怎么办”。

v0.5 新增：
- `AuthorLens`：ResearchPack 与 ArticleArchitect 之间的作者视角层
- `author.*` 状态：why_write / POV / entry_point / material_to_ignore / narrative_choice / voice_profile
- 五账号 Voice Profile
- Narrative Choice，替代固定情绪曲线
- Anti-Template Pass，做结构级去AI而非同义词替换
- PublisherQA 增加 Author Presence / Template Risk / Voice Match
- Validator 增加 Author Gate
- Benchmark 从20个扩展到25个，新增AI味回归案例

v0.4 的 Evidence、Scope、Calculation、Originality、Visual Ready、PublishingPlan 等硬门全部保留。

## 核心原则

> 后台高度结构化，前台高度自由。

后台继续严格：
- Source Registry
- Evidence Ledger
- Calculation Ledger
- Scope
- Schema
- Validator
- Claim → Writing 证据链

前台不再强制：
- 固定五段/六段结构
- 固定情绪曲线
- 前300字钩子四件套
- 2–4句平均段落
- 每300–500字强制新增信息
- 每篇都反转
- 每篇都给行动清单

## 目录

```text
wechat-article/
├── README.md
├── docs/
│   ├── SKILL-CONTRACT.md
│   ├── AUTHOR-VOICE.md
│   ├── ORIGINALITY-RUBRIC.md
│   └── PRODUCTION-MODES.md
├── schemas/
│   ├── article-state.yaml
│   └── article-state.schema.json
├── scripts/
│   └── validate_state.py
├── ledger/
├── learning/
├── benchmarks/
└── skills/
    ├── topic-hunter/
    ├── research-pack/
    ├── author-lens/
    ├── article-architect/
    ├── viral-writer/
    ├── visual-editor/
    ├── publisher-qa/
    ├── publishing-plan/
    ├── growth-reviewer/
    └── shared/
        ├── account-profiles.md
        └── voice-profiles.md
```

## v0.5 状态机

```text
signal
  ↓
topic
  ↓
research
  ↓
author
  ↓
architecture
  ↓
writing
  ↓
visual
  ↓
qa
  ↓
publishing
  ↓
published
  ↓
reviewed
```

失败状态单独使用：
`ready | blocked | rework | manual_review`。

## 三档生产模式

### Flash｜抢热点
通常1000–1500字。允许简化/跳过完整 AuthorLens 与 Architect，但仍必须有一个具体入口、一个明确判断和完整事实门。

### Standard｜标准文章
默认模式。完整：
`Research → AuthorLens → Architect → Writer → Visual → QA → PublishingPlan`。

### Deep｜旗舰深度
强调亲测、实验、采访、数据、商业拆解与A级原创资产；AuthorLens 必须把一手材料放进核心叙事。

## 完整生产链

```text
原始信号
  ↓
TopicHunter
热点 → 独特角度 / 去重 / Scope / 账号路由
  ↓
ResearchPack
Source / Evidence / Calculation / Originality
  ↓
AuthorLens
为什么写 / 作者POV / 具体入口 / 材料取舍 / Narrative Choice / Voice Profile
  ↓
ArticleArchitect
结构服务POV / 证据映射 / 不追求完整
  ↓
ViralWriter
自然成稿 / 作者存在 / Anti-Template Pass
  ↓
VisualEditor
视觉规划与资产执行状态
  ↓
PublisherQA
事实 + Author Presence + Template Risk + Voice Match + Visual Ready
  ↓
PublishingPlan
标题 / 封面 / 摘要 / 发布时间 / 分发 / 数据回收
  ↓
真实发布
  ↓
GrowthReviewer
1h / 24h / 72h 数据与 learning/
```

## AuthorLens 为什么重要

Originality 回答：
> 这篇有没有新增信息？

AuthorLens 回答：
> 为什么是这个账号在写？

一篇文章即使有独立综合和新框架，也可能依然像AI。

Standard/Deep 至少要明确：
- 为什么写这个题
- 作者真正判断什么
- 从哪个具体细节切入
- 哪些资料明确不写
- 用什么叙事方式推进
- 本账号这篇应该是什么声音

如果“去掉账号名后任何AI号都能发”，Author Gate 不应通过。

## Narrative Choice

每篇选择一个主推进方式，而不是套统一模板：
- single-thread
- scene-led
- evidence-led
- argument-led
- case-led
- diary-led
- compare-led

允许一篇文章只说透一个问题。

## Anti-Template Pass

Writer 初稿后必须检查：
- 是否明显 What→Why→So what→How
- 小标题/段落是否过度均匀
- 是否每节都概括→解释→总结
- 是否机械制造反转
- 抽象过渡句是否过密
- 是否结尾自动生成三条建议/六步法
- 去掉账号名后是否任何AI号都能发布

发现问题优先：删、合并、重排、换入口；不是只换同义词。

## 五个账号

Account Profile 决定“写什么”，Voice Profile 决定“怎么像这个账号的人在说”。

- 思然日新：高校内部人视角
- 思然知己：持续跟AI变化，但不急着追新词；从真实任务变化判断学习价值
- 思然天工：亲测、踩坑、可复现
- 思然经世：钱、成本、供需、复制门槛
- 思然修远：现实选择、生活代价、允许矛盾存在

详见：
- `skills/shared/account-profiles.md`
- `skills/shared/voice-profiles.md`

## Evidence Chain

作者声音不能破坏事实链：

```text
Source S001
  ↓
Claim C001 / Calculation K001
  ↓
Architecture A01
  ↓
Writing W01
  ↓
PublisherQA
```

第一人称、强判断、叙事自由都不能绕过证据边界。

## Originality Gate

- A级：亲测、自主计算、采访、一手职业经验、自建数据、独立实验
- B级：独立对比、跨源数据整理、新框架、结构化重编码、新综合
- C级：公开截图、普通摘要、常规汇总、常识解释

门槛：Flash可conditional；Standard≥1A或≥2B；Deep≥1A+≥1B。

注意：Originality PASS ≠ Author Voice PASS。

## Visual / Publishing

`planned ≠ executed`。

PublisherQA 给 A 前仍要求 `visual.assets_ready=true`；之后必须经过 PublishingPlan，不能直接把“发布”当黑盒。

## 机器校验

```bash
pip install -r requirements-dev.txt
python scripts/validate_state.py path/to/article-state.yaml
```

Validator 除 v0.4 的 Schema、证据引用、Originality、Visual、Publishing 条件外，v0.5 还检查：
- Standard/Deep 是否经过 Author Gate
- author.why_write 是否存在
- author.pov 是否存在
- 是否有具体 entry_point
- 是否记录 material_to_ignore
- 是否选定 narrative_choice / voice_profile
- Humanity Test 是否仍为高AI风险
- QA=A 时 Anti-Template Pass 是否通过

## Benchmark

`benchmarks/cases.yaml` 当前25个案例。

v0.5 新增：
- B021：事实正确但作者缺席
- B022：标准AI四段式
- B023：均匀结构AI味
- B024：伪第一人称
- B025：新职业“思然知己”文章不得再写成完整AI说明文

## 当前边界

仍未加入：
- SignalRadar 自动信号发现
- WeChatViralEngine 总控 Orchestrator
- 自动语义去重索引
- 全自动微信后台发布
- LLM Eval Runner

在 Author Voice 经过真实文章压力测试之前，不优先增加总控自动化。

## 最终质量标准

一篇合格文章同时看六件事：

`Truth + Point of View + Specificity + Selectivity + Rhythm + Voice`

事实正确只是底线；作者为什么要说这件事、选择说什么和不说什么，才决定文章是不是一个“人”写出来的。
