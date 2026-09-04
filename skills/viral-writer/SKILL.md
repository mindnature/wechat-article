---
name: viral-writer
description: 基于证据和架构生成公众号正文，并在每个正文 Section 中保留 Claim/Calc/Case 证据引用。
version: "0.4"
reads: [topic, research, architecture, account, production, workflow]
writes: [writing, workflow]
resources: [../shared/account-profiles.md, ../../learning/proven-patterns.md, ../../learning/hypotheses.yaml, ../../docs/PRODUCTION-MODES.md]
---

# ViralWriter｜公众号成稿

遵循 v0.4 ArticleState、Schema 与 Skill Contract。

## 前置门
### Flash
允许从 `workflow.stage: research, gate: ready` 直接进入，但必须基于 3–5 条已验证核心 Claim 建立简化结构。

### Standard / Deep
必须 `stage: architecture, gate: ready`，且 Originality Gate 达标。

## Step 1｜加载账号、模式和学习规则
Level 2/3 可作为稳定规则；Level 0/1 只能作为实验提示。

## Step 2｜正文证据链
正文写入 `writing.sections`，不得只保存一坨纯文本：

```yaml
- section_id: W01
  source_section_id: A01
  text: "..."
  claim_ids: [C001]
  calc_ids: [K001]
  case_ids: []
  statement_types: [fact, calculation]
```

Flash 无 Axx 时 `source_section_id` 可空，但 Claim/Calc 必须保留。

新增事实必须退回 ResearchPack，不得在写作阶段凭空补。

## Step 3｜语气边界
- verified fact：可陈述
- calculation：快速交代关键假设
- inference：使用判断语气
- opinion：明确为作者判断
- partial/disputed：显示不确定性

## Step 4｜开头
前250–300字尽快出现事实/场景、冲突、读者关系和阅读收益；硬事实必须映射到 Claim/Calc。

## Step 5｜信息密度与节奏
- 正常段落2–4句为主
- 允许少量一句话重点段
- 每300–500字至少一个有效新增信息
- 不为短删证据，不为深度堆背景

## Step 6｜标题候选结构化
每个标题候选记录：
```yaml
- text: ""
  claim_ids: [C001]
  calc_ids: []
  scope_note: ""
  risk: low | medium | high
```

所有硬事实必须 title_safe；省略 Scope 会误导时不能选。

## Step 7｜原创资产可见性
Standard/Deep 至少有一处正文明确承载通过 Originality Gate 的 A/B级资产。不能把原创资产藏在脚注或结尾一句。

## Step 8｜图片占位
按 visual_nodes 插入功能占位；不编造图片。

## Step 9｜模式长度
- Flash：1000–1500字
- Standard：1500–2500字
- Deep：2500–5000字或按价值延长

## 输出
Human Summary：TOP3标题、完整正文、证据映射摘要、图片占位、标签、风险。

State Patch：
- `writing.title_candidates`
- `writing.selected_title`
- `writing.sections`
- `writing.body_status`
- `writing.word_count`
- `writing.risk_notes`
- `workflow.stage: writing, gate: ready`

发现新增未核验事实：`gate: rework, return_to: research`。

## 禁止
- 编造采访/数据/亲测
- 切断 Claim→正文证据链
- 把推断写成事实
- 标题超出 Evidence Ledger
- 结尾强行升华
