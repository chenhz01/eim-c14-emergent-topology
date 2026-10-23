# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P54 uncertainty-calibrator — 涌现拓扑/规划/抽象

L0: AI 说'我八成确定'时，它真的八成对吗？这个工具算差值。
L1: 期望校准误差 ECE。
L2: ece(confs, outcomes, bins) → float。
"""

def ece(confs, outcomes, bins=5):
    n = len(confs)
    if n == 0: return 0.0
    tot = 0.0
    for b in range(bins):
        lo, hi = b/bins, (b+1)/bins
        idx = [i for i, c in enumerate(confs) if lo <= c < hi or (b == bins-1 and c == 1.0)]
        if not idx: continue
        acc = sum(outcomes[i] for i in idx)/len(idx)
        conf = sum(confs[i] for i in idx)/len(idx)
        tot += len(idx)/n * abs(acc - conf)
    return round(tot, 4)

def demo():
    print("[P54]", ece([0.9,0.9,0.1,0.1],[1,1,1,0]))


if __name__ == "__main__":
    demo()
