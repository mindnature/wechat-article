# Skill Contract｜v0.5

所有子 Skill 必须遵循统一状态、Schema、证据链与作者声音契约。

## 1. Front Matter

```yaml
---
name: <kebab-case>
description: <一句话职责>
version: "0.5"
reads: [<ArticleState fields>]
writes: [<ArticleState fields>]
resources: [<optional external files>]
---
```

- `reads` 只声明 ArticleState 字段。
- `writes` 只声明本 Skill 可修改字段。
- `resources` 声明 Ledger、learning、账号画像、Voice Profile 等资源。

## 2. 共享状态与机器验证

默认状态模板：`../schemas/article-state.yaml`。
机器 Schema：`../schemas/article-state.schema.json`。

结构化输出必须满足 JSON Schema；若运行环境无法自动校验，也要进行等价字段检查。

## 3. Stage 与 Gate 分离

`workflow.stage`：
`signal | topic | research | author | architecture | writing | visual | qa | publishing | published | reviewed`

`workflow.gate`：
`ready | blocked | rework | manual_review`

被阻断时同时记录 `blocked_by`、`return_to`、`retry_count`。

## 4. 输出三层

每个 Skill 输出：
1. `Human Summary`
2. `State Patch`
3. 如涉及持久化：`Persistence Patch`

无法写入资源时标记 `not_persisted`，不能假装已学习/去重。

## 5. 事实层保持严格

事实类型：`fact | calculation | inference | opinion | unknown`。

Scope：`global | national | province | city | institution | company | single_case | unknown`。

Scope 扩大视为事实错误。

## 6. Evidence / Calculation Ledger

关键事实进入 `research.claims`；自行计算进入 `research.calculations`。

正文继续保持：
`Source → Claim/Calc → Architecture → Writing`。

证据链必须可审计，但证据ID和后台结构不得泄漏成前台文风。

## 7. Originality Gate

按 `../docs/ORIGINALITY-RUBRIC.md`：
- Standard：≥1A 或 ≥2B
- Deep：≥1A+1B
- Flash：可 conditional

Originality 只回答“有没有信息增量”，不等于 Author Voice。

## 8. Author Gate｜v0.5新增

Standard / Deep 在 ResearchPack 后必须经过 AuthorLens。

最少记录：
- `author.why_write`
- `author.pov`
- `author.entry_point`
- `author.material_to_ignore`
- `author.narrative_choice`
- `author.voice_profile`
- `author.humanity_test`

原则：
- 必须有明确取舍，不允许把 ResearchPack 全写进正文。
- 第一人称不是必须；作者性可以来自判断、入口、选择与不确定性。
- 禁止伪造经历来制造“人味”。

Flash 可跳过完整 AuthorLens，但必须至少有一个具体入口和一个明确判断。

## 9. 后台结构化，前台自由

ArticleArchitect / ViralWriter 不得把系统流程直接投射成文章模板。

不再强制：
- 固定情绪曲线
- 前300字同时完成四个钩子任务
- 2–4句固定段落
- 每300–500字强制新增信息
- What→Why→So what→How
- 结尾行动清单

详见 `../docs/AUTHOR-VOICE.md`。

## 10. Narrative Choice

每篇只选一个主推进方式：
`single-thread | scene-led | evidence-led | argument-led | case-led | diary-led | compare-led`。

结构服务作者 POV，而不是为“完整”服务。

## 11. Anti-Template Pass

Standard / Deep 完稿后必须执行 `writing.anti_template_pass`。

检查重点：
- 结构是否过于可预测
- 每节是否长度/功能过于均匀
- 抽象过渡句是否过密
- 是否机械反转
- 是否自动生成方法论/建议清单
- 去掉账号名后是否任何AI号都能发布

未 pass 不得进入最终 QA A级。

## 12. Voice Profile

账号定位见 `../skills/shared/account-profiles.md`。
具体声音见 `../skills/shared/voice-profiles.md`。

Account Profile 决定写什么；Voice Profile 决定怎么像这个账号的人在说。

## 13. Visual Ready Gate

视觉规划和执行分开：`planning_status`、`execution_status`、`assets_ready`。

资产未完成，PublisherQA 不得给最终 A。

## 14. Publishing Gate

QA A 后进入 PublishingPlan，确定最终标题、封面、摘要、发布窗口、分发与数据计划。

## 15. Production Mode

按 `../docs/PRODUCTION-MODES.md`：`flash | standard | deep`。

模式只改变研究/结构深度，不降低事实、Scope、版权等硬门。

## 16. Competition / Score / Experiment

- Competition 只能对实际扫描样本下结论。
- 0–5评分必须使用 TopicHunter 明确锚点。
- 增长实验尽量发布前登记 `experiment.*`，避免事后归因。

## 17. 失败处理

缺数据：`unknown/N/A`。
关键事实失证：退回 research。
作者视角空泛：退回 author。
模板风险高：退回 writing/author。
视觉未执行：退回 visual。

## 18. 回归测试

修改 Skill 后至少运行 `../benchmarks/cases.yaml` 对应案例。

v0.5 新增不可退化项：
- AuthorLens 不能被跳过（Standard/Deep）
- Author POV/具体入口不得为空
- Anti-Template Pass 必须真实运行
- QA A 时 Author Presence 不能 low、Template Risk 不能 high
