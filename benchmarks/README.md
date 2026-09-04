# Benchmarks｜回归测试

`cases.yaml` 用于验证 Skill 修改是否真正变好，而不是只让提示词更长。

## 当前版本
v0.5 共 25 个固定案例。

## 运行原则
- TopicHunter：重点 B001–B013、B019
- ResearchPack：重点 B001/B003/B004/B006/B007/B009/B011/B014/B018/B019
- AuthorLens / ArticleArchitect / ViralWriter：重点 B021–B025
- PublisherQA：重点 B001/B005/B014/B016/B017/B018/B021–B024
- PublishingPlan：B020
- GrowthReviewer：需真实后台数据；实验判断必须检查预登记

## 不可退化项
1. Scope 正确
2. 假新闻/弱证据能阻断
3. 重复选题能识别
4. 计算保留假设和公式
5. 个案不泛化趋势
6. 不伪造亲测/一手经验
7. 弱热点能说“不写”
8. blocked/rework 状态完整
9. planned 不等于 assets_ready
10. 正文证据引用不能断链
11. C级原创不能独立通过 Standard/Deep
12. QA后必须先 PublishingPlan 再 published
13. Standard/Deep 不能跳过 AuthorLens
14. Author POV、具体入口、材料取舍不能为空
15. 事实正确但作者缺席，不能直接 QA=A
16. 标准 What/Why/So what/How 结构必须触发模板风险
17. “每节同长度+每节反转”必须触发结构级返工
18. 禁止用虚构第一人称制造人味
19. Anti-Template Pass 不能只做同义词替换
20. 思然知己等账号必须符合独立 Voice Profile

## 机器校验 fixtures

```bash
python scripts/validate_state.py benchmarks/fixtures/valid-standard.yaml
python scripts/validate_state.py benchmarks/fixtures/invalid-broken-evidence.yaml
python scripts/validate_state.py benchmarks/fixtures/invalid-generic-ai-voice.yaml
```

要求：
- `valid-standard.yaml` 必须 PASS
- `invalid-broken-evidence.yaml` 必须 FAIL
- `invalid-generic-ai-voice.yaml` 必须 FAIL Author Gate

GitHub Actions 自动执行这三项。

## LLM语义回归
B001–B025 中的 `must_* / should_*` 仍需人工或未来 Eval Runner 对 Skill 输出做语义断言。

JSON Schema/validator 负责结构与机器门；它无法完全自动判断“文章是否像一个真实作者”，因此 Author Presence、Narrative Choice、Template Risk 仍需 PublisherQA 与真实文章压力测试共同验证。
