# Amazon Market Research Skill

**面向跨境电商选品与新品开发的八阶段 AI 市场调研工作流。**

将类目调研需求整理为可复用的Skill，明确每个阶段需要的数据、分析方法、交付物和继续执行条件，帮助研究者把市场信息转化为可核验的产品决策依据。


## 为什么做这个项目

跨境电商调研通常要在市场报告、商品表格、关键词工具和竞品网站之间来回切换。容易出现三个问题：分析输入不完整、指标口径混用、结论难以追溯。本项目将这些问题转化为具体的流程约束：阶段性确认、字段清单、统一指标口径、证据标注及缺失数据处理。

目标用户是需要开展类目研究的产品实习生、跨境运营人员与选品人员。设计来源于作者提出的八步业务工作流；文档与校验工具在 AI 辅助下整理与实现。

## 八阶段流程

| 阶段 | 核心输入 | 预期交付 |
| --- | --- | --- |
| 1. 市场与准入风险 | 站点、类目、产品属性 | 市场背景、准入风险及官方来源 |
| 2. 市场结构 | 用户提供的市场报告 | 容量、趋势、价格带、集中度和生命周期分析 |
| 3. 商品打标 | ASIN、标题、五点描述 | 全量打标Excel、标签字典、复核表 |
| 4. 透视与可视化 | 打标结果与可用经营指标 | 标签汇总、交叉分析、图表和洞察 |
| 5. 品牌与卖家研究 | 品牌/卖家排名及外部资料 | 头部品牌卖家对照、渠道证据和实力评分 |
| 6. 词频与需求线索 | 标题、五点描述 | 单/双/三词组合词频、场景及人群总结 |
| 7. 流量与推广 | 前十ASIN表现、关键词结构等 | 竞争评估、推广模型、前30天策略及机会点 |
| 8. 配置与利润 | 原始CPA模型、成本和费用 | 多配置定价、盈亏平衡CPA和敏感性分析 |

每阶段完成后等待用户确认，再进入下一阶段。必要输入缺失时先收集数据，不以假设替代真实市场结论。

## 设计重点

- **流程控制**：把大任务拆为八个有明确输入和输出的阶段，支持用户纠正范围、补充数据和续接进度。
- **可追溯打标**：每款商品保留来源、标签证据和复核状态；“未提及”和“不具备”分开处理。
- **指标约束**：区分Amazon自营与FBA第三方、流量得分与实际曝光、工具估算与真实订单；品牌和卖家分别分析。
- **决策可核验**：洞察列出来源、推断过程、替代解释及验证方式；利润模型统一税费、币种与归因口径。

## 安装与使用

将仓库中 `skills/amazon-market-research` 整个目录复制到本机技能目录。默认使用 `CODEX_HOME/skills`；未设置 `CODEX_HOME` 时使用用户目录下的 `.codex/skills`。

Windows PowerShell，从本仓库根目录执行（若目标已存在则停止，避免覆盖个人修改）：

```powershell
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME 'skills' } else { Join-Path $env:USERPROFILE '.codex/skills' }
$skillTarget = Join-Path $skillRoot 'amazon-market-research'
if (Test-Path -LiteralPath $skillTarget) { throw '目标技能已存在，请先检查已有版本。' }
New-Item -ItemType Directory -Path $skillRoot -Force | Out-Null
Copy-Item -LiteralPath './skills/amazon-market-research' -Destination $skillTarget -Recurse
```

在支持技能的会话里输入：

> 使用 $amazon-market-research，我需要亚马逊美国站吹风机类目的详细市场分析报告。按八步执行，每一步结束先询问是否继续。

技能会先收集必要条件，再逐步索取市场报告、商品表、关键词表及成本表。用户已明确要求报告时，不重复询问是否需要报告。

运行依赖：AI 助手须能检索网页及读取文件；Excel交付需可用的表格工具，Word/PDF仅在用户请求时需要对应工具。技能自身不提供市场数据账号、抓取服务、付费工具访问或自动广告投放。仅阅读技能无需Python；本仓库静态检查使用Python 3.10+标准库。

## 项目文件

```text
skills/amazon-market-research/
  SKILL.md                      八阶段入口与流程规则
  agents/openai.yaml            技能展示信息
  references/traffic-analysis.md 关键词、流量与推广分析规范
  references/profit-model.md    配置、费用与CPA核算规范
docs/
  product-design.md             产品设计与验收标准
  evaluation.md                 行为评估案例及待验证状态
  publishing.md                 GitHub发布方式
examples/
  walkthrough.md                明确标记的教学演示
scripts/
  validate_package.py           文件结构、链接与包装检查
```

本地检查：

```powershell
python scripts/validate_package.py
```

该检查只验证发布包结构与文档链接，不证明模型会遵守工作流，不检验市场结论准确性。见 [本地验证记录](docs/validation.md)。行为测试见 [评估案例](docs/evaluation.md)；案例尚待实际运行，不将预期输出当作已通过的测试。

## 展示与下一步

- 了解设计取舍：[产品设计说明](docs/product-design.md)。
- 看输入、证据与标签的关系：[教学示例](examples/walkthrough.md)。
- 发布到GitHub：[发布指南](docs/publishing.md)。
- 下一阶段：选择一个真实细分类目，取得有权使用的市场/商品/流量数据，跑通流程，记录人工修正量、耗时与结论复核情况。

目前适合展示的项目成果是工作流设计、分析规范与交付标准。尚不应声称完成真实市场洞察、实现商业收益或显著提升效率。未经授权的市场报告、账号凭据和第三方原始数据不包含在仓库中。发布前由作者决定是否采用开源许可证；当前未附开源许可证，不宣称已授予通用再分发许可。
