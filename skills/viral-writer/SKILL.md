---
name: viral-writer
description: 基于证据与已筛选作者POV分段生成正文，再独立重排删减；禁止用同一连续生成节奏和伪犹豫制造“人味”。
version: "0.6"
reads: [topic, research, author, architecture, account, production, workflow]
writes: [writing, workflow]
resources: [../shared/account-profiles.md, ../shared/voice-profiles.md, ../shared/voice-samples/manifest.yaml, ../../learning/proven-patterns.md, ../../learning/hypotheses.yaml, ../../docs/AUTHOR-VOICE.md, ../../docs/PRODUCTION-MODES.md]
---

# ViralWriter｜公众号成稿

遵循 v0.6 ArticleState、Schema 与 Skill Contract。

## 前置门
### Flash
可从 research ready 进入，但必须有具体入口和一个明确判断。

### Standard / Deep
必须：architecture ready、AuthorLens 已完成、Originality Gate 达标、selected POV 可追溯。

## 核心原则
- 后台结构化，前台不展示流程。
- 先分段生成，再重排；不要一次性从标题顺写到结尾。
- 任何“犹豫/保留/我也不确定”必须绑定真实 Uxxx 节点。
- Voice 样例权重高于形容词规则。

## Step 1｜建立 Segment Briefs
从 architecture.structure 拆成 3–7 个局部写作包，每个只包含：
- 本段任务
- selected POV 的相关切面
- 本段 Claim/Calc/Case
- 本段允许使用的 uncertainty node
- 本段 voice exemplar（若已校准）
- 本段禁止动作

不得把“上一段已经怎么写”当作下一段必须延续的节奏模板。

## Step 2｜分段生成
优先真正隔离上下文：runner 若支持多调用，每个 segment 单独 invocation，只传局部 brief，不传已生成全文。

记录：
```yaml
writing:
  generation_trace:
    strategy: isolated_segments | single_context_fallback
    segment_count: 5
    isolated_context: true
    reorder_pass: false
    note: ""
```

如果运行环境只能单次连续生成，必须标 `single_context_fallback`，不能假装已经完成隔离。

## Step 3｜真实不确定性规则
允许不确定表达的前提：该句绑定 `research.uncertainty_nodes` 中真实 Uxxx。

禁止：
- 为显得像真人而写“我也拿不准”
- 证据已经明确却故意模糊
- 用“可能/或许”掩盖没有研究

## Step 4｜组装前先打散
将各 segment 作为独立文本块审视，先不加小标题。

检查：
- 是否有两个段落其实在说同一件事
- 是否存在“完整但不必要”的解释
- 哪一段可以挪到更前/更后
- 哪一段删掉后文章反而更有力

## Step 5｜Reorder / Delete Pass
必须单独进行一次重排删减，而不是在初稿上只改词。

动作至少包含一种：
- 删除一个完整段落/模块
- 合并两个模块
- 调换至少两段顺序
- 去掉一个标准总结段

如果完全不需要任何结构动作，要说明原因；默认视为风险信号。

完成后：`generation_trace.reorder_pass=true`。

## Step 6｜开头与结尾
开头从具体入口自然进入，不统一钩子公式。

结尾不负责“闭环所有问题”。可以停在一个判断、一个具体后果、一个尚未解决但有证据边界的问题。

## Step 7｜标题
8–15个候选即可。硬事实 title_safe；Scope 不得扩大。

## Step 8｜Anti-Template Pass
检查结构级痕迹：What→Why→So what→How、同长度小节、每节都反转、连续抽象过渡、标准三建议/六步法。

优先删段/换序/合并，不做同义词美容。

## Step 9｜Blind Review Handoff
正文完成后不直接让同一上下文自评 Voice。

生成一个最小 `blind_review.packet`：
- 纯正文（去掉 ArticleState、POV、pipeline规则）
- 账号名可匿名
- 若有用户确认 Voice samples，仅给匿名正/反例，不说明哪篇是机器生成

下一步进入独立 `BlindReview`。

## 输出
Human Summary：TOP3标题、完整正文、selected POV 如何落地、真实不确定性使用、generation trace、Anti-Template edits、Blind Review packet。

State Patch：`writing.*`；完成后 `workflow.stage: writing, gate: ready`。

## 禁止
- 一次连续顺写全文后假装“分段生成”
- 编造采访/数据/亲测
- 伪第一人称/伪犹豫
- 按后台 Evidence 顺序逐条解释
- 用禁词表代替结构重排
