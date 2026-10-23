# P55 · causal-discoverer

> 机制簇：**涌现拓扑/规划/抽象** ｜ 家族：**EIM-1.0**（55 个涌现智能人工化机制之一）

## 费曼三层

**L0 · 这是什么（12 岁能懂）**
看两个事件是不是总一起出现，猜它们有没有关系。

**L1 · 机制本质**
条件概率提升度 lift 作为因果候选。

**L2 · 怎么用上**
discover(pairs) → [(a,b,lift)]。

## 30 秒跑起来

```bash
python impl.py        # 看 demo 输出
python selftest.py    # 跑自检（含输出快照比对）
```

真实运行输出（本仓发布时快照，`golden_output.txt` 同内容）：

```text
[P55] [('rain', 'wet', 1.25), ('sun', 'dry', 5.0)]
```

## 什么时候该用 / 不该用

| | 内容 |
|---|---|
| **该用** | 复杂可分解任务、需要动态决定「谁和谁协作、分几层」的场景。 |
| **不该用** | 线性流程、步骤固定的流水线。 |
| **常见误用** | 拓扑越复杂越好——每多一层协调就多一层失败面，复杂度必须由收益证明。 |

## 在这个家族里

- 组合仓（55 个机制合集）：https://github.com/chenhz01/emergent-mechanisms
- 同簇伙伴：`P51` emergent-topology-mapper · `P52` subgoal-decomposer · `P53` concept-distiller · `P54` uncertainty-calibrator
- 本仓是 **P55 的独立署名锚**：可单独引用、单独开 issue、单独打星；实现与组合仓
  `components/P55-causal-discoverer/` 一致，修复会双向同步。

## License

**双许可**：

- **代码**：Apache-2.0 — 见 [LICENSE](../../LICENSE)
- **文档/规范**：CC BY 4.0 — 见 [LICENSE-SPEC](../../LICENSE-SPEC)

对外声明「符合 / 兼容 / 通过 EIM-1.0」时须署名：
`EIM-1.0 · P55 · causal-discoverer © 2026 chenhz01, CC BY 4.0`
未作上述声明者可自由使用、商用、闭源、改名，无需署名。详见 [NOTICE](../../NOTICE)。
