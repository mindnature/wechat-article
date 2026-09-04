# Learning｜增长学习层

GrowthReviewer 的结论必须沉淀到本目录，供后续 TopicHunter、ViralWriter 和 PublisherQA 读取。

## 经验等级

- Level 0 `observation`：单篇出现，仅记录。
- Level 1 `hypothesis`：至少两篇出现类似信号，可设计实验。
- Level 2 `local_rule`：同账号/同题型 3–5 篇重复出现且无明显反例。
- Level 3 `stable_pattern`：跨时间窗口仍成立，可进入稳定规则。

## 文件

- `account-baselines.yaml`：五个账号自己的历史基线；没有数据就保持 N/A。
- `hypotheses.yaml`：正在验证的假设与实验。
- `proven-patterns.md`：达到 Level 2/3 的规则。
- `rejected-patterns.md`：被反例推翻或失效的规则，防止未来重复学习错误经验。

## Promotion 规则

任何规则升级时必须记录：

- 适用账号
- 适用题型
- 样本量
- 时间窗口
- 支持证据
- 反例
- 置信度
- 最后复核日期

禁止把头部账号的公开经验直接写成本账号稳定规则；外部经验只能作为初始假设。
