# Benchmarks｜回归测试

`cases.yaml` 用于验证 Skill 修改是否真正变好，而不是只让提示词更长。

## 当前版本
v0.4 共 20 个固定案例。

## 运行原则
- TopicHunter：重点 B001–B013、B019
- ResearchPack：重点 B001/B003/B004/B006/B007/B009/B011/B014/B018/B019
- ViralWriter / PublisherQA：重点 B001/B005/B014/B016/B017/B018
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

## 机器校验 fixtures

```bash
python scripts/validate_state.py benchmarks/fixtures/valid-standard.yaml
python scripts/validate_state.py benchmarks/fixtures/invalid-broken-evidence.yaml
```

第一个必须 PASS；第二个必须 FAIL。

GitHub Actions 会自动执行上述检查。

## LLM语义回归
B001–B020 中包含的 `must_* / should_*` 仍需人工或未来 Eval Runner 对 Skill 输出做语义断言。JSON Schema/validator 负责结构与交叉引用，不替代内容判断。
