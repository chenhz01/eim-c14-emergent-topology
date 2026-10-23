# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 chenhz01 (EIM-1.0)
"""P52 subgoal-decomposer — 涌现拓扑/规划/抽象

L0: 大目标拆成小步骤，先干什么后干什么。
L1: 按'并且/然后'等连接词切分子目标。
L2: decompose(goal) → 子目标列表。
"""

import re
def decompose(goal):
    parts = re.split(r"\s*(?:,|\band\b|then|;)\s*", goal)
    return [p.strip() for p in parts if p.strip()]

def demo():
    print("[P52]", decompose("read file and parse it then run tests"))


if __name__ == "__main__":
    demo()
