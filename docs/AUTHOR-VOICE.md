# Author Voice Architecture｜v0.6

v0.6 的核心判断：

> 文风AI不是靠更多形容词规则解决，而要改变素材、判断、生成和评审的机制。

## 1. 深主旨来自竞争，不来自一次性“想一个角度”
AuthorLens 必须生成3个POV，并主动指出每个为什么可能仍然平庸。最容易被任何AI账号推出的角度先淘汰。

## 2. 作者性来自真实取舍
Material Graveyard 让“哪些资料不写”可审计。作者不是把全部研究结果展示给读者，而是围绕 selected POV 放弃一半以上非核心信息单元。

## 3. 真犹豫必须有材料来源
允许作者不确定，但只能绑定 ResearchPack 的 Uxxx：冲突信源、partial evidence、missing data、计算假设、Scope边界、预测。

没有真实不确定性，就不要表演犹豫。

## 4. Voice Profile 只是边界
“自然、口语、有判断”没有足够可操作性。

真正Voice来自用户确认的正/反例，详见 `VOICE-CALIBRATION.md` 与 `voice-samples/manifest.yaml`。

## 5. 分段生成优先于连续全文生成
连续生成会自然形成统一节奏并一路延续。v0.6 优先每个segment独立brief、独立调用，再做重排/删减。

无法隔离上下文时必须记录 fallback。

## 6. 同上下文自评不算文风验证
Writer/QA共享同一上下文时共享盲点。

Standard/Deep 必须由 fresh session 或 different model 做 BlindReview，Reviewer 不得看到 pipeline 规则。

## 7. 最终评价
`Truth + Tension + POV Competition + Selectivity + Real Uncertainty + Independent Review`

“像人”不是目标函数；它应该是这些机制共同工作的结果。
