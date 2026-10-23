# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P51 emergent-topology-mapper — 涌现拓扑/规划/抽象

L0: 看谁跟谁常联系，画出'谁最能牵线'的关系网。
L1: 统计交互频次建图，返回度数最高节点(枢纽)。
L2: map_graph(interactions) → (hub, edges)。
"""

def map_graph(interactions):
    from collections import Counter
    deg = Counter()
    for a, b in interactions:
        deg[a] += 1; deg[b] += 1
    hub = deg.most_common(1)[0][0] if deg else None
    return hub, len(set(interactions))

def demo():
    print("[P51]", map_graph([("a","b"),("b","c"),("b","d"),("a","b")]))


if __name__ == "__main__":
    demo()
