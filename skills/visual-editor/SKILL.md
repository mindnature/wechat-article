---
name: visual-editor
description: 规划并在工具可用时执行公众号封面、真实图、AI图和信息图资产，显式管理资产就绪、图源、版权、真实性与作者叙事一致性。
version: "0.5"
reads: [author, architecture, writing, research, account, production, workflow]
writes: [visual, workflow]
---

# VisualEditor｜公众号视觉编辑与资产就绪

遵循 v0.5 ArticleState、`visual-asset.schema.json` 与 Skill Contract。

## 目标
把文章转成可执行视觉资产单；工具可用时执行搜索/生成并记录最终资产。规划完成 ≠ 资产完成。

视觉必须服务文章当前的 Narrative Choice，而不是重新把正文做成标准信息图模板。

## Step 1｜视觉节点
读取 `author.narrative_choice`、`architecture.visual_nodes` 与最终正文。

候选图必须承担：evidence / explain / story / emotion / rhythm 中至少一项。

如果文章本身靠一个具体细节或单线叙事推进，不要因为“完整”强塞多张知识卡。

## Step 2｜真实图 vs 生成图
- 政策、人物、产品、页面、原始数据 → 真实图/截图
- 机制、流程、关系 → 生成图/信息图
- 情绪/隐喻 → 生成图
- 不用AI图冒充现实证据

## Step 3｜封面资产
封面至少记录：asset_id、主题、冲突/数字、类型、构图、短文案、status、file_ref（执行后）。

封面应强化作者选择的主问题，不要把全文所有信息塞进封面。

## Step 4｜文中资产
所有图片必须符合 `visual-asset.schema.json`。

## Step 5｜权利与隐私
真实图优先：官方/原始发布方 > 企业媒体包 > 权威媒体 > 明确许可图库/公共领域 > 其他可核验来源。

`rights_status=avoid` 不能进入最终资产；`needs_confirmation` 必须进入 rights_risks。

图源标注不等于版权许可。

## Step 6｜执行状态
### 只有规划能力
```yaml
planning_status: complete
execution_status: unavailable
assets_ready: false
```

### 部分执行
`execution_status: partial, assets_ready: false`

### 全部必需资产完成
满足封面 ready、所有 required inline asset ready、无 avoid 资产、无高隐私风险未处理，才可：
`execution_status: complete, assets_ready: true`。

## Step 7｜模式控制
- Flash：优先 1封面 + 1–3张功能图
- Standard：按真实叙事需要配置，不设固定数量
- Deep：可增加数据图、实验截图、流程图，但不凑数量

## 输出
Human Summary：视觉策略、与AuthorLens主线的关系、封面、插图资产表、执行状态、图源/版权/隐私风险。

State Patch：`visual.*`，`workflow.stage: visual`。
- assets_ready=true → gate ready
- 未执行完 → gate rework，return_to visual
- 权利/隐私需人工判断 → gate manual_review

## 禁止
- planned 当 executed
- AI生成伪新闻/伪政策证据
- 为凑图插无关图片
- 用图源标注替代授权判断
- 用“统一知识卡风格”把不同文章重新做成同一种AI模板感
