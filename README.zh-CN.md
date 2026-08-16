# 低摩擦产品设计 Skill

这是 `design-low-friction-products` 的中文介绍页。可执行的 Skill 以英文为唯一权威版本，避免中英文两套规则逐渐产生行为差异。

它适用于表单、工作流、仪表盘、业务操作和面向用户的 AI 功能，重点处理：

- 降低学习成本和重复录入；
- 最近使用与高频选项的稳定排序；
- 安全默认值和自动带入历史确认数据；
- 人工修改保护、来源说明和历史重置；
- 自动化、确认、权限与恢复边界；
- 控制功能堆叠，保持最短完整主路径。

## 安装

```bash
mkdir -p ~/.agents/skills
cp -R skills/design-low-friction-products ~/.agents/skills/
```

## 调用

```text
$design-low-friction-products 审查这个订单录入流程，减少重复输入并保护人工修改
```

## 当前状态

这是正式开源的英文运行包。公开内容已移除本机路径、内部项目名称和工作记录，只保留可复用规则、通用案例与公开依据。

## 验证

```bash
python3 scripts/validate.py
```

许可证为 MIT，详见 [LICENSE](LICENSE)。
