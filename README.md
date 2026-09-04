# WeChat Article｜公众号爆款生产系统

面向微信公众号内容生产的模块化 AI Skills 工作流。目标不是一个“大而全 Prompt”，而是一条可核验、可分模式生产、可视觉执行、可发布规划、可复盘学习的内容链。

## 当前版本：v0.4 Production

v0.4 重点修复 v0.3 审核出的 6 个结构问题：

1. `status` 拆成 `workflow.stage + workflow.gate`
2. ArticleState 从模板升级为 JSON Schema + 交叉引用 validator
3. Evidence 链从 Source → Claim → Architecture → Writing 全程保留
4. Originality Gate 升级为 A/B/C 三级原创资产
5. 增加 Flash / Standard / Deep 三档生产模式
6. 增加 PublishingPlan，发布不再是黑盒

同时新增：
- Visual Ready Gate：planned ≠ executed
- QA=A 必须 `assets_ready=true`
- 实验预登记，避免事后故事化归因
- GitHub Actions 运行时校验
- Benchmark 从 14 个扩展到 20 个

## 目录

```text
wechat-article/
├── README.md
├── docs/
│   ├── SKILL-CONTRACT.md
│   ├── ORIGINALITY-RUBRIC.md
│   └── PRODUCTION-MODES.md
├── schemas/
│   ├── article-state.yaml
│   ├── article-state.schema.json
│   ├── source.schema.json
│   ├── claim.schema.json
│   ├── calculation.schema.json
│   ├── writing-section.schema.json
│   ├── visual-asset.schema.json
│   └── learning-rule.schema.json
├── scripts/
│   └── validate_state.py
├── ledger/
├── learning/
├── benchmarks/
└── skills/
    ├── topic-hunter/
    ├── research-pack/
    ├── article-architect/
    ├── viral-writer/
    ├── visual-editor/
    ├── publisher-qa/
    ├── publishing-plan/
    ├── growth-reviewer/
    └── shared/
```

## v0.4 状态机

流程位置与失败状态分离：

```text
workflow.stage:
signal → topic → research → architecture → writing → visual → qa → publishing → published → reviewed

workflow.gate:
ready | blocked | rework | manual_review
```

阻断时必须记录 `blocked_by`、`return_to`、`retry_count`。

## 三档生产模式

### Flash｜抢热点
1000–1500字。允许跳过完整 ArticleArchitect，但关键事实、Scope、版权、隐私门不降。

### Standard｜标准爆款
1500–2500字。默认主力模式，完整 Research → Architect → Writer → Visual → QA → PublishingPlan。

### Deep｜深度旗舰
2500–5000字或更长。强调亲测、实验、访谈、数据、商业拆解和品牌资产。

详见 `docs/PRODUCTION-MODES.md`。

## 生产链

```text
原始信号
  ↓
TopicHunter
去重 / Scope / 竞争样本 / 账号路由 / 模式选择 / 锚定评分
  ↓
ResearchPack
Source Registry / Evidence / Calculation / Originality
  ↓
ArticleArchitect（Flash可简化/跳过）
证据绑定结构 / 情绪线 / 原创资产落位
  ↓
ViralWriter
正文 + Claim/Calc 引用 + 结构化标题候选
  ↓
VisualEditor
规划 + 执行状态 + 资产就绪 + 图源/权利
  ↓
PublisherQA
证据链 / Scope / Calculation / Originality / Visual Ready
  ↓
PublishingPlan
最终标题 / 封面 / 摘要 / 发布窗口 / 分发 / 承接 / 实验 / 数据回收
  ↓
真实发布
  ↓
GrowthReviewer
1h / 24h / 72h 漏斗 + 实验评估 + learning/
```

## Evidence Chain

v0.4 不允许写作阶段切断来源：

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

正文 `writing.sections` 必须保留 `claim_ids / calc_ids / case_ids`。

## Originality Gate

### A级
亲测、自主计算、采访、一手职业经验、自建数据、独立实验。

### B级
独立对比、跨源数据整理、新框架、结构化重编码、新综合。

### C级
公开截图、普通摘要、常规汇总、常识解释。

门槛：
- Flash：可 conditional
- Standard：≥1A 或 ≥2B
- Deep：≥1A + ≥1B

C级不能单独通过 Standard/Deep。

## Visual Ready Gate

```text
planning_status: complete
execution_status: complete
assets_ready: true
```

只有封面和必需文中资产真实 ready、无阻断性版权/隐私问题，PublisherQA 才能给 A。

## PublishingPlan

QA=A 后不直接“发布”。必须确定：
- 最终标题
- 最终封面资产
- 摘要
- 发布窗口与紧迫度
- 分发渠道
- 后续承接
- 1h/24h/72h 数据回收
- 如有实验，发布前预登记

## 机器校验

安装：

```bash
pip install -r requirements-dev.txt
```

校验 ArticleState：

```bash
python scripts/validate_state.py path/to/article-state.yaml
```

Validator 除 JSON Schema 外，还检查：
- 重复 ID
- Claim → Source 引用
- Writing → Claim/Calc 引用
- blocked/rework 状态完整性
- QA=A 的视觉 ready 条件
- publishing/published 的前置条件
- Standard/Deep 原创资产门槛
- Calculation 必填字段

GitHub Actions 会自动运行合法/非法 fixtures。

## Benchmark

`benchmarks/cases.yaml` 当前 20 个案例，覆盖：
- Scope扩大
- 单一个案泛化
- 假新闻
- 弱热点
- 重复选题
- 伪亲测
- 计算缺假设
- 状态机阻断
- 视觉只规划未执行
- 正文证据链断裂
- 原创门伪通过
- Flash/Deep模式
- QA后发布计划

## 五个公众号

- 思然日新：高校青年教师
- 思然知己：AI热点与学习
- 思然天工：AI工具与工作流
- 思然经世：AI商业机会
- 思然修远：30+长期成长

账号画像：`skills/shared/account-profiles.md`。

## 当前边界

v0.4 仍未加入：
- SignalRadar 自动信号发现
- WeChatViralEngine 总控 Orchestrator
- 独立 Visual Asset Executor（VisualEditor在有工具时可执行）
- 自动语义去重索引
- 全自动微信后台发布
- LLM Benchmark Eval Runner

这些应在真实压力测试后进入下一阶段，而不是先堆自动化。

## 核心原则

- 热点不是选题，角度才是。
- 范围比措辞更重要。
- 关键事实必须可追溯。
- 计算必须可复现。
- planned 不等于 executed。
- 速度模式不降低事实门。
- 文章必须有新增价值。
- 发布是生产环节，不是一个按钮。
- 单篇爆文只能产生观察，不能直接改写长期规则。
