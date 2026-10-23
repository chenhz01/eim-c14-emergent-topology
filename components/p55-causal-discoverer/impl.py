# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P55 causal-discoverer — 涌现拓扑/规划/抽象

L0: 看两个事件是不是总一起出现，猜它们有没有关系。
L1: 条件概率提升度 lift 作为因果候选。
L2: discover(pairs) → [(a,b,lift)]。
"""

def discover(pairs, min_lift=1.2):
    from collections import Counter
    tot = len(pairs); ca, cb, cab = Counter(), Counter(), Counter()
    for a, b in pairs:
        ca[a] += 1; cb[b] += 1; cab[(a,b)] += 1
    out = []
    for (a, b), n in cab.items():
        lift = (n/tot) / ((ca[a]/tot)*(cb[b]/tot))
        if lift >= min_lift: out.append((a, b, round(lift, 2)))
    return out

def demo():
    print("[P55]", discover([("rain","wet")]*4 + [("sun","dry")], 1.2))


if __name__ == "__main__":
    demo()
