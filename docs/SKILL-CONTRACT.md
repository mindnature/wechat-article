# Skill Contract｜v0.3

所有子 Skill 必须遵守同一份状态契约，避免自由文本接力造成上下文漂移。

## 1. 统一 Front Matter

每个 `SKILL.md` 必须以以下字段开头：

```yaml
---
name: <kebab-case>
description: <一句话职责>
version: "0.3"
reads: [<ArticleState fields>]
writes: [<ArticleState fields>]
---
```

## 2. 单一共享状态

默认状态模板：`schemas/article-state.yaml`。

子 Skill 不重新发明字段名；只读取自己需要的字段，并只修改声明的 `writes` 字段。

如没有结构化状态文件，也要按同一字段名输出 `State Patch`，供下一环节合并。

## 3. 输出必须分两层

每个 Skill 输出：

1. `Human Summary`：给作者快速阅读；
2. `State Patch`：仅包含本 Skill 新增或修改的 ArticleState 字段。

禁止让下一 Skill 依靠解析整段散文来猜上一步结论。

## 4. 事实与判断分层

关键内容必须使用以下类型之一：

- `fact`：外部可核验事实；
- `calculation`：基于明确假设和公式得到的结果；
- `inference`：由证据推出但不是来源直接陈述；
- `opinion`：作者判断；
- `unknown`：暂未核验。

## 5. Scope 是硬字段

涉及政策、规则、统计、行业趋势时必须标注范围：

`global | national | province | city | institution | company | single_case | unknown`

不得把 `single_case` 或 `company` 自动提升成 `national` 或行业普遍结论。

## 6. Evidence Ledger

所有准备进入标题、导语、关键结论的事实，必须写入 `research.claims`：

```yaml
- claim_id: C001
  text: "..."
  type: fact
  scope: national
  source_ids: [S001]
  verification: verified
  confidence: high
  note: ""
```

验证状态：`verified | partial | disputed | unsupported | false | unknown`。

## 7. Calculation Ledger

所有算账、比例、增速、收益、房贷等自行计算必须记录：

```yaml
- calc_id: K001
  question: "..."
  assumptions: []
  formula: "..."
  result: "..."
  verification: reproduced
```

结果不能脱离假设单独进入标题。

## 8. Originality Gate

进入正式写作前必须检查 `research.originality_gate`。

至少满足一种有效增量：

- 作者亲测
- 自主计算
- 一手职业经验
- 原始截图/数据整理
- 独立对比
- 采访/小调查
- 新框架/新综合

如果没有，允许继续写热点快讯，但必须标记 `commodity_content_risk: high`；标准/深度文章原则上不得无提示进入 ViralWriter。

## 9. 失败与缺失处理

缺数据时写 `unknown/N/A`，不能补猜。

无法完成真实竞争扫描时，必须写：

```yaml
competition:
  status: unverified
```

不得把模型记忆当作“市场已经这样写”的证据。

## 10. 状态门

推荐状态迁移：

`signal -> topic_selected -> researched -> architected -> drafted -> visually_planned -> qa_passed -> published -> reviewed`

任何 Skill 可因关键证据问题把状态退回上一阶段。

## 11. 可回归测试

修改 Skill 后至少跑 `benchmarks/cases.yaml` 中对应测试项。若核心失败条件恶化，不得仅因文案更流畅就认定升级成功。
