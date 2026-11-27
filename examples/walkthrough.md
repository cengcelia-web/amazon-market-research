# 教学演示：从产品文案到标签

**以下商品和响应是编写的教学示例，不是亚马逊真实商品，也不是已执行的模型测试。** 本例演示步骤3的规范，使用前应已完成或明确跳过前面的步骤。

## 假设输入

| 示例ID（非ASIN） | 标题 | 五点摘录 |
| --- | --- | --- |
| EXAMPLE-A | Foldable Hair Dryer 1600W | Two heat settings; foldable handle; includes concentrator |
| EXAMPLE-B | Compact Travel Hair Dryer | Lightweight design; travel pouch included |
| EXAMPLE-C | Hair Dryer 1800W | Rated power: 1600W; three heat settings |

用户提示：

> 请按步骤3对以上全部商品打标，重点提取功率、温度档位、折叠设计和配件，保留证据。缺失不要猜，冲突标待核实。本例仅验证打标规则。

## 期望展示的标签逻辑

| 示例ID | 功率W | 温度档位 | 折叠设计 | 配件 | 证据与复核状态 |
| --- | --- | --- | --- | --- | --- |
| EXAMPLE-A | 1600 | 2 | 是 | 集风嘴 | 标题与五点直接支持 |
| EXAMPLE-B | 未提及 | 未提及 | 未提及 | 旅行袋 | “Compact”不证明可折叠 |
| EXAMPLE-C | 待核实 | 3 | 未提及 | 未提及 | 标题1800W与五点1600W冲突 |

这张表仅解释预期行为。真实执行需生成用户要求的Excel、覆盖全部源行、附标签字典与检查表，再询问是否进入步骤4。
