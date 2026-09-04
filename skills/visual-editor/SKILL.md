---
name: visual-editor
description: 在独立盲审通过后规划并执行公众号封面、真实图、AI图和信息图资产，显式管理就绪、图源、版权、真实性与叙事一致性。
version: "0.7"
reads: [author, architecture, writing, blind_review, research, account, production, workflow]
writes: [visual, workflow]
---

# VisualEditor｜公众号视觉编辑与资产就绪

## 前置门
### Flash
允许 `workflow.stage: writing` 且 blind review `skipped_for_speed`。

### Standard / Deep
必须：
- `workflow.stage: blind_review`
- `workflow.gate: ready`
- `blind_review.status: pass`
- `evaluator_independence: fresh_session | different_model`

不允许为了赶视觉进度绕过独立盲审。

## Step 1｜视觉节点
读取 Narrative Choice、visual_nodes 与最终正文。候选图必须承担 evidence / explain / story / emotion / rhythm 中至少一项。

如果文章靠一个具体细节或单线叙事推进，不要为了“完整”强塞知识卡。

## Step 2｜真实图 vs 生成图
- 政策、人物、产品、页面、原始数据 → 真实图/截图
- 机制、流程、关系 → 生成图/信息图
- 情绪/隐喻 → 生成图
- 不用AI图冒充现实证据

## Step 3｜封面资产
封面强化作者选择的主问题，不把全文所有信息塞进一个画面。

## Step 4｜文中资产
符合 `visual-asset.schema.json`；真实图记录 source/rights/privacy。

## Step 5｜执行状态
只有规划能力：`planning_status: complete, execution_status: unavailable, assets_ready: false`。

全部必需资产完成且无阻断权利/隐私问题，才可 `assets_ready: true`。

## Step 6｜模式控制
- Flash：1封面 + 1–3张功能图
- Standard：按叙事节点配置，不设固定数量
- Deep：可增加数据图、实验截图、流程图，不凑数量

## 输出
Human Summary：视觉策略、资产表、执行状态、权利/隐私风险。

State Patch：`visual.*`，完成后 `workflow.stage: visual`。

## 禁止
- planned 当 executed
- AI生成伪新闻/伪政策证据
- 为凑图插无关图片
- 图源标注替代版权判断
- Standard/Deep 绕过 BlindReview
