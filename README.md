# C14 · Emergent Topology

> **机制簇**：涌现拓扑/规划/抽象 ｜ **家族**：EIM-1.0（Emergent Intelligence Mechanisms）｜ **组件数**：5
>
> 本仓是 EIM-1.0 的**簇级入口**：一个机制簇 + 该簇全部可运行参考实现。
> 单组件仓与旗舰合集见文末「家族」段。

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
复杂任务别一条直线做到底，让系统自己长出「分头做再合并」的结构。

**L1 · 机制本质**
从任务图动态生长子目标拓扑，按依赖/并行性/失败代价剪枝，提炼可复用子图。

**L2 · 怎么用上**
topology-grower 生长；subgoal-decomposer 拆解；abstraction-extractor 提子图。

## 30 秒跑起来

```bash
git clone https://github.com/chenhz01/eim-c14-emergent-topology.git && cd eim-c14-emergent-topology
python run_all.py        # 跑全簇 5 个组件，逐个 selftest + 输出快照比对
```

单个组件也可独立跑：

```bash
python components/p51-emergent-topology-mapper/impl.py        # 看 demo 输出
python components/p51-emergent-topology-mapper/selftest.py    # 断言 + 与 golden_output.txt 比对
```

零第三方依赖，Python 3.9+ 即可。

## 本簇组件

| ID | 组件 | 机制本质 | 目录 |
|---|---|---|---|
| `P51` | emergent-topology-mapper | 统计交互频次建图，返回度数最高节点(枢纽)。 | `components/p51-emergent-topology-mapper/` |
| `P52` | subgoal-decomposer | 按'并且/然后'等连接词切分子目标。 | `components/p52-subgoal-decomposer/` |
| `P53` | concept-distiller | 按共同前缀分组形成一层层级。 | `components/p53-concept-distiller/` |
| `P54` | uncertainty-calibrator | 期望校准误差 ECE。 | `components/p54-uncertainty-calibrator/` |
| `P55` | causal-discoverer | 条件概率提升度 lift 作为因果候选。 | `components/p55-causal-discoverer/` |

## 该用 / 不该用 / 常见误用

**该用**
长流程、多工具、可并行的复杂任务；重复出现的复合流程。

**不该用**
线性小任务（生长与剪枝开销不划算）。

**常见误用（这条最重要）**
认为越复杂越好。拓扑复杂度必须由失败代价证明其必要性。

## 这份代码是什么、不是什么

- **是**：可直接运行、带断言与输出快照的最小参考实现。每个 `impl.py` 都能单独跑出 demo，`selftest.py` 会在行为漂移时报错。
- **不是**：生产级库。缺少配置化、并发安全、错误恢复、性能优化。**生产使用请按自己的约束扩展**，不要原样上生产。
- **诚实边界**：本簇解决的是「机制怎么落地」这个问题，不承诺在任何数据分布下都优于基线。基准数据请自测。

## 家族

- **旗舰合集（55 组件）**：https://github.com/chenhz01/emergent-mechanisms
- **单组件仓**：`eim-p01-…` ~ `eim-p55-…`，与 `components/` 内文件一致，任一处修复会双向同步。

## 许可（双许可）

- **代码**：**Apache-2.0**（Apache License 2.0）— 见 [LICENSE](LICENSE)
- **规范/文档**：**CC BY 4.0**（Creative Commons Attribution 4.0 International）— 见 [LICENSE-SPEC](LICENSE-SPEC)

声明符合 EIM-1.0 规范时须署名：

```
EIM-1.0 · C14 · Emergent Topology © 2026 chenhz01, CC BY 4.0
```

详见 [NOTICE](NOTICE)。
