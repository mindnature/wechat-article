# Skill Contract｜v0.4

所有子 Skill 必须遵循统一状态、Schema 和资源契约，避免自然语言接力造成漂移。

## 1. Front Matter

```yaml
---
name: <kebab-case>
description: <一句话职责>
version: "0.4"
reads: [<ArticleState fields>]
writes: [<ArticleState fields>]
resources: [<optional external files>]
---
```

- `reads` 只声明 ArticleState 字段。
- `writes` 只声明本 Skill 可修改字段。
- `resources` 声明 Ledger、learning、账号画像等持久化资源。

## 2. 共享状态与机器验证

默认状态模板：`../schemas/article-state.yaml`。
机器 Schema：`../schemas/article-state.schema.json`。

结构化输出必须满足 JSON Schema；若运行环境无法自动校验，也要进行等价字段检查。

## 3. Stage 与 Gate 分离

禁止用一个 `status` 同时表达流程位置和失败状态。

`workflow.stage`：
`signal | topic | research | architecture | writing | visual | qa | publishing | published | reviewed`

`workflow.gate`：
`ready | blocked | rework | manual_review`

被阻断时同时记录：
- `blocked_by`
- `return_to`
- `retry_count`

## 4. 输出三层

每个 Skill 输出：
1. `Human Summary`
2. `State Patch`
3. 如涉及持久化：`Persistence Patch`

无法写入资源时标记 `not_persisted`，不能假装已学习/去重。

## 5. 事实类型
- `fact`
- `calculation`
- `inference`
- `opinion`
- `unknown`

## 6. Scope
`global | national | province | city | institution | company | single_case | unknown`

Scope 扩大视为事实错误。

## 7. Evidence Ledger
关键事实必须进入 `research.claims`，并符合 `claim.schema.json`。

```yaml
- claim_id: C001
  text: "..."
  type: fact
  scope: national
  source_ids: [S001]
  verification: verified
  confidence: high
  title_safe: true
  note: ""
```

## 8. Calculation Ledger
自行计算必须记录：

```yaml
- calc_id: K001
  question: "..."
  assumptions: []
  formula: "..."
  inputs: {}
  result: "..."
  sensitivity: ""
  verification: reproduced
```

## 9. Claim → Architecture → Writing 证据链
正文不得切断证据引用。

每个正文 section 至少包含：

```yaml
- section_id: W01
  source_section_id: A01
  text: "..."
  claim_ids: [C001]
  calc_ids: [K001]
  case_ids: []
  statement_types: [fact, calculation]
```

PublisherQA 必须沿此链审计，而不是重新猜测正文来源。

## 10. Originality Gate
按 `../docs/ORIGINALITY-RUBRIC.md` 分 A/B/C 级原创资产。

标准/深度模式通过条件：
- 至少 1 个 A 级；或
- 至少 2 个 B 级。

C 级资产不能单独通过。

Flash 模式可 conditional，但必须明确资讯属性。

## 11. Production Mode
按 `../docs/PRODUCTION-MODES.md`：
- `flash`
- `standard`
- `deep`

事实门槛不因模式降低；只减少研究深度、结构复杂度和字数。

## 12. Visual Ready Gate
视觉规划和视觉执行分开：
- `planning_status`
- `execution_status`
- `assets_ready`

若公众号文章所需资产未完成，PublisherQA 不得给最终 A 可发布。

## 13. Publishing Gate
通过 QA 后必须进入 PublishingPlan，而不是直接把“发布”当黑盒。

PublishingPlan 至少确定：最终标题、封面资产、摘要、发布窗口、紧迫度、分发渠道、后续承接、1h/24h/72h 数据计划。

## 14. Competition Scan
只能对实际扫描到的样本做结论。禁止写“全网没人写”。推荐表述：
“在本次已扫描样本中未发现”。

## 15. Score Anchors
0–5 分必须使用明确锚点，见 TopicHunter。不得凭感觉给出无解释分值。

## 16. Experiment Preregistration
如 GrowthReviewer 提出可验证假设，下一轮正式实验应在发布前登记 `experiment.*`，避免事后故事化归因。

## 17. 失败处理
缺数据写 `unknown/N/A`。
无法竞争扫描：`competition.status: unverified`。
无法取得图片：`execution_status: unavailable`。
关键事实失证：`workflow.gate: blocked` 并退回 ResearchPack。

## 18. 回归测试
修改 Skill 后至少运行 `../benchmarks/cases.yaml` 对应案例。
文案更顺不能覆盖 Scope、假新闻、重复、计算、伪亲测等能力退化。
