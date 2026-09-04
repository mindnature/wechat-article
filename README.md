# WeChat Article｜公众号内容生产系统

模块化 AI Skills 工作流。目标不是让一个模型“按更多规则写得更像人”，而是改变生成和评审机制：先制造竞争性判断，再淘汰；把真实不确定性写进证据层；正文分段生成后重排；文风由独立上下文盲审。

## 当前版本：v0.6 Depth & Blind Review

v0.6 修复 v0.5 暴露的两个更底层问题：

1. `主旨浅`：AuthorLens 单次生成一个“够像观点”的角度，容易停在第二显然。
2. `同源自评`：Writer 与 QA 在同一个模型/同一上下文里共享盲点，自评 A 仍可能很AI。

### v0.6 核心变化
- TopicHunter 新增 `Tension Test`
- Standard/Deep 必须有“独家材料路径”或“可证据约束的强判断”
- AuthorLens 强制 `3 POV → 自我批判 → 淘汰2个 → 选1个`
- Material Graveyard：至少一半已研究信息单元被明确放弃
- ResearchPack 新增 `Uncertainty Ledger`
- 犹豫/保留判断只能绑定真实 Uxxx
- Writer 改成 Segment Brief → 分段生成 → Reorder/Delete Pass
- Voice Profile 降为低权重边界，新增用户确认的正/反 Voice Samples
- 新增 `BlindReview`：必须 fresh session 或 different model；same-context 不算通过
- Benchmark 从25个扩展到30个

v0.5 的 Evidence、Scope、Calculation、Originality、Visual Ready、PublishingPlan 等硬门全部保留。

## 核心原则

> 后台高度结构化；主旨必须竞争产生；文风必须独立评审。

## Standard 主链

```text
TopicHunter
  ↓
Tension Test
  ↓
ResearchPack
Evidence / Calculation / Uncertainty / Depth Material
  ↓
AuthorLens
3 POV candidates → 淘汰 → selected POV
Material Graveyard / Decision Change
  ↓
ArticleArchitect
只服务 selected POV
  ↓
ViralWriter
Segment Briefs → isolated/fallback segments → reorder/delete
  ↓
BlindReview
fresh session / different model
  ↓
VisualEditor
  ↓
PublisherQA
  ↓
PublishingPlan
  ↓
发布 → GrowthReviewer
```

## Tension Test

Standard/Deep 不能只满足“热点+未覆盖”。还必须回答：
- 具体矛盾/反常识是什么？
- 哪个问题还没被公开材料直接回答？
- 如果判断成立，读者会具体改变哪个决定？
- 能否拿到独家/一手材料？
- 如果没有独家材料，是否存在一个敢于不顺着主流走、但有证据边界的强判断？

两者都没有，应降为 Flash/backup，而不是包装成深度稿。

## AuthorLens：不再单次生成 POV

必须生成3个真正不同的 POV，每个都写：
- thesis
- evidence refs
- decision_change
- banality_self_critique
- replaceability

先淘汰最像普通AI账号能写出的两个，再让 selected POV 进入 Architect。

## Material Graveyard

不是要求把废料写成长文，而是对“信息单元”做可审计取舍：

```text
retained_units: 5
discarded_units: 7
```

Standard/Deep 默认 `discarded_units >= retained_units`。

目的是逼出真实选择，而不是嘴上说“我做了取舍”。

## Real Uncertainty

ResearchPack 新增 `research.uncertainty_nodes`。

只有真实存在的：
- 冲突信源
- partial evidence
- missing data
- calculation assumption
- scope boundary
- forecast

才能驱动“目前不能确定/这里保留判断”等表达。

证据已经明确时，不许为了人味表演犹豫。

## Segmented Generation

ViralWriter 不再一次性从标题连续顺写到结尾。

优先：
1. 为每个局部段建立 brief
2. 分 invocation 生成，不传前文完整 prose
3. 汇总后单独做 reorder/delete pass
4. 再做 Anti-Template

如果运行环境只能单上下文，必须记录：`single_context_fallback`，不能假装已经隔离。

## Blind Review

这一步不能由生产上下文自己完成。

有效：
- `fresh_session`
- `different_model`

无效：
- `same_context`
- Reviewer 能看到 AuthorLens/Architecture/Anti-Template 规则

Blind packet 只给纯正文，以及可选的用户确认 Voice 正/反例匿名混排。

Standard/Deep 没有独立 BlindReview pass，不得进入 VisualEditor。

## Voice Calibration

`skills/shared/voice-profiles.md` 现在只是低权重边界。

真正的风格校准来自：
`skills/shared/voice-samples/manifest.yaml`

每个账号至少需要：
- 3个用户确认 positive samples
- 2个用户确认 negative samples

历史文章如果用户没有明确说“这段像我/不像我”，不能自动当Gold Sample。

## 三档模式

### Flash
抢时效，可跳过完整 AuthorLens / BlindReview，但事实门不降。

### Standard
默认：完整 Tension → 3 POV → Graveyard → segmented writing → BlindReview。

### Deep
在 Standard 基础上要求更强的一手材料和A级原创资产；盲审优先 different model。

## 机器校验

```bash
pip install -r requirements-dev.txt
python scripts/validate_state.py path/to/article-state.yaml
```

v0.6 Validator 新增检查：
- Tension Test 是否具体
- decision_change 是否只是“多关注/多学习”
- 是否有独家材料路径或强判断
- AuthorLens 是否恰好生成3个POV并淘汰2个
- 每个POV是否做平庸自检
- Material Graveyard 是否形成足够选择压力
- uncertainty_usage 是否引用真实 Uxxx
- Writer 是否 segment + reorder
- BlindReview 是否 truly independent
- same-context reviewer 是否被拦截

## Benchmark

当前30个案例。v0.6 新增：
- B026：第二显然角度必须继续竞争
- B027：无独家料/无强判断不能装深度
- B028：伪犹豫必须被拦
- B029：同上下文自评无效
- B030：未标注历史稿不能自动成为Voice Gold Sample

## 当前边界

- 这个仓库可以规定“BlindReview必须独立”，但同一条 ChatGPT 对话本身无法证明自己已经独立。
- 真正盲审需要新会话或不同模型。
- Voice Samples 需要用户明确标注；系统不会擅自把旧文章当正例。
- SignalRadar / WeChatViralEngine Orchestrator 仍未加入，等 v0.6 真实文章压测稳定后再做。

## 最终质量标准

`Truth + Tension + Point of View + Selectivity + Real Uncertainty + Independent Voice Review`

事实正确只是底线；深度来自竞争性判断和真实材料，文风可靠性来自独立评审，而不是同一个模型给自己打高分。
