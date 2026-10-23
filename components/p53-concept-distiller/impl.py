# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P53 concept-distiller — 涌现拓扑/规划/抽象

L0: 一堆零碎概念，归出一个大类小类的树。
L1: 按共同前缀分组形成一层层级。
L2: distill(concepts) → {group: [items]}。
"""

def distill(concepts):
    out = {}
    for c in concepts:
        key = c.split("_")[0] if "_" in c else c[:3]
        out.setdefault(key, []).append(c)
    return out

def demo():
    print("[P53]", distill(["parse_a","parse_b","render_x"]))


if __name__ == "__main__":
    demo()
