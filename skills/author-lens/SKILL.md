---
name: author-lens
description: 在研究完成后生成多个竞争性作者判断，主动淘汰平庸角度，确定具体切入、材料墓地、真实不确定性和叙事选择。
version: "0.6"
reads: [topic, research, account, production, workflow]
writes: [author, workflow]
resources: [../shared/account-profiles.md, ../shared/voice-profiles.md, ../shared/voice-samples/manifest.yaml, ../../docs/AUTHOR-VOICE.md, ../../docs/VOICE-CALIBRATION.md]
---

# AuthorLens｜作者视角层

本 Skill 位于 ResearchPack 与 ArticleArchitect 之间。

它不负责补事实，也不写全文。它负责把“够像一个观点”继续往下逼一层。

## 前置门
- `workflow.stage: research`
- `workflow.gate: ready`
- 核心 Claim 可用
- Standard/Deep Originality Gate 达标
- Standard/Deep `topic.tension_test.status=pass`

## Step 1｜为什么写
不能写“因为这是热点”。要指出：哪个细节、矛盾、措辞、案例或数据让作者觉得值得追。

## Step 2｜强制生成3个 POV 候选
必须生成恰好3个，不允许只出1个就停止。

```yaml
- pov_id: P01
  thesis: ""
  evidence_refs: [C001]
  tension: ""
  decision_change: ""
  banality_self_critique: "这个角度为什么仍可能只是第二显然？"
  replaceability: high | medium | low
  risk: ""
```

三个候选必须彼此真正不同，不能只是换措辞。

至少覆盖：
- 一个从材料矛盾/异常点出发；
- 一个从读者决策出发；
- 一个允许更锋利、可能反对主流叙事的判断。

## Step 3｜主动枪毙平庸角度
先淘汰：
1. 最像“发生了什么→为什么重要→普通人怎么办”的；
2. 任何同类AI账号都能从公开材料直接推出的；
3. decision_change 只能写成“多关注/多学习/提高认知”的；
4. 需要靠夸大证据才能显得锋利的。

写入 `author.rejected_pov_ids` 和淘汰理由。

最终只选择一个 `author.selected_pov_id` 进入 Architect。

## Step 4｜Entry Point + Decision Change
入口必须具体，并附：
- `content`
- `evidence_refs`
- `decision_change`

硬指标：
> 如果这篇判断是对的，读者会具体改变哪个决定？

空泛答案视为未通过。

## Step 5｜Material Graveyard｜材料墓地
ResearchPack 搜到的材料必须出现可审计的取舍。

不是把弃用材料重新写成长文，而是按“信息单元”计数：

```yaml
material_graveyard:
  - item_id: G001
    refs: [C004, S006]
    summary: ""
    why_excluded: ""
    weight: 2
selection_stats:
  retained_units: 5
  discarded_units: 6
```

Standard/Deep 默认要求：`discarded_units >= retained_units`。

目的不是逼模型制造废话，而是保证至少有一半已研究材料被明确放弃，形成真实选择压力。

如果研究包本身太薄，回 ResearchPack，不要伪造墓地。

## Step 6｜真实不确定性绑定
第一人称犹豫、保留判断、开放问题，只能引用 `research.uncertainty_nodes`。

```yaml
uncertainty_usage:
  - node_id: U001
    intended_expression: explicit_uncertainty
```

没有 Uxxx 节点时，不得凭空写“我也不确定”“这里值得怀疑”等表演式犹豫。

## Step 7｜Narrative Choice
只选一个主结构：single-thread / scene-led / evidence-led / argument-led / case-led / diary-led / compare-led。

结构服务 selected POV，不负责把所有材料装进去。

## Step 8｜Voice Profile + Exemplars
`voice-profiles.md` 只提供低权重边界。

如果 `voice-samples/manifest.yaml` 对应账号存在用户确认的正例/反例，则优先读取具体样例：
- 正例告诉模型“什么句子像”；
- 反例告诉模型“什么句子虽正确但不像”。

没有已确认样例时必须标记：`author.voice_calibration: uncalibrated`，不能把形容词画像冒充已校准声音。

## Step 9｜Humanity / Depth Test
进入 Architect 前检查：
1. 3个候选是否真的竞争过？
2. 最显然的角度是否被主动淘汰？
3. selected POV 是否有具体 decision_change？
4. material graveyard 是否达到选择压力？
5. 读者能否说出“作者反对/提醒/坚持什么”？
6. 是否有任何假犹豫或伪第一人称？

未通过：`gate: rework`，优先回 author；材料不足则回 research/topic。

## 输出
Human Summary：3个POV候选、各自平庸风险、淘汰过程、最终POV、具体入口、decision_change、材料墓地、真实不确定性、叙事选择、Voice Calibration状态。

State Patch：`author.*`；通过后 `workflow.stage: author, gate: ready`。

## 禁止
- 只生成一个 POV
- 用“我觉得”代替作者性
- 为了锋利制造没有证据约束的观点
- 用假犹豫制造人味
- 研究了很多材料却全部写进正文
- 未经用户确认就把历史稿自动当作 Voice 正例
