---
name: research-pack
description: 为高潜选题建立可核验研究包，形成 Source Registry、Evidence/Calculation/Uncertainty Ledger、Scope 与分级 Originality Gate。
version: "0.7"
reads: [signal, topic, account, production, workflow]
writes: [research, topic.evidence_confidence, workflow]
resources: [../../docs/ORIGINALITY-RUBRIC.md, ../../docs/PRODUCTION-MODES.md]
---

# ResearchPack｜深度素材研究

遵循 v0.7 ArticleState、JSON Schema 和 Skill Contract。

## 目标
把选题做实，同时为“深主旨”提供真实摩擦：独家材料、冲突信源、数据缺口、主观假设或可被反驳的证据边界。

## Step 1｜Source Registry
来源唯一 `Sxxx` ID。权威等级：A官方/原始；B权威采访/专业来源；C二手媒体；D社交/未核验。D不能单独支撑关键事实。

## Step 2｜Evidence Ledger
标题、导语、核心结论候选事实进入 `research.claims`。

规则：Scope不得扩大；个案不得泛化；partial/disputed/unsupported原则上不得 title_safe；inference/opinion显式区分。

## Step 3｜Calculation Ledger
自行算账必须记录 assumptions、formula、inputs、result、sensitivity、verification。

## Step 4｜Uncertainty Ledger｜真实不确定性
把真实存在的不确定节点结构化，而不是以后由 Writer 自己表演犹豫。

```yaml
research:
  uncertainty_nodes:
    - node_id: U001
      type: claim_conflict | partial_evidence | missing_data | calculation_assumption | scope_boundary | forecast
      description: ""
      evidence_refs: [C001, S002]
      what_is_known: ""
      what_is_unknown: ""
      allowed_voice_effect: hedge | question | explicit_uncertainty | none
```

只有这里存在的节点，后续才允许写“目前还不能确定”“这里我会保留判断”等不确定表达。

如果证据已经明确，不许为了人味制造犹豫。

## Step 5｜深度材料路径
围绕 TopicHunter 的 Tension Test 主动寻找：
- 真实招聘 JD / 职责变化
- 一手访谈/对话
- 产品、项目、公司真实操作
- 原始数据或可自行计算数据
- 作者职业经验可验证的对应场景
- 与主流说法冲突的反方证据

记录 `research.depth_material`，并标明 `exclusive: true/false`。

如果 TopicHunter 声称存在 exclusive_material_path，但研究阶段没有找到，应降级该判断，不能假装已经拥有独家材料。

## Step 6｜七层素材
原始来源、关键事实、数字、时间线、人物/案例、舆论争议、反方与限制。

## Step 7｜分级 Originality Gate
- Flash：可 conditional
- Standard：至少 1×A 或 2×B
- Deep：至少 1×A + 1×B

普通截图、常规汇总、摘要属于C，不能单独过门。

## Step 8｜模式化研究深度
### Flash
锁定3–5条关键 Claim，可简化背景。

### Standard
完整 Evidence + Uncertainty + 限制 + 原创资产；尽量验证 Tension Test 的独家材料或强判断基础。

### Deep
扩大竞争扫描和反证；A级原创资产进入核心论证。

## Step 9｜研究门
通过：核心 Claim 可支撑、Scope清楚、数字可核验、Originality达标，并且 Tension Test 的关键张力没有被研究结果证伪。

如果研究发现候选角度只是“第二显然”：
`workflow.gate: rework`
`workflow.return_to: topic`

如果关键事实失证：blocked，退回 research。

## 输出
Human Summary：Source Registry、Evidence Ledger、Calculation Ledger、Uncertainty Ledger、Depth Material、原创资产、限制、证据缺口、title_safe事实。

State Patch：`research.*`、`topic.evidence_confidence`、`workflow.*`。

## 禁止
- 为凑素材引用低质量转载
- AI生成事实/采访/网友评论
- 忽略冲突证据
- 只给计算结果不给假设
- 把“模型可以想象到的一手场景”冒充一手材料
- 为了文风自然，制造不存在的不确定性
