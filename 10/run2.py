# Tried BFS -> too slow
# Tried DFS -> too slow
# Only seeing the first 2 answers and then got stuck.
# Switch to use ILP.
import sys
from collections import deque
from dataclasses import dataclass
from typing import List, Optional
from z3 import Int, Optimize, Sum, sat


def solve_with_z3(buttons: list[list[int]], joltage: list[int]):
    m = len(buttons)
    n = len(joltage)

    opt = Optimize()
    presses = [Int(f"t_{b}") for b in range(m)]

    total_j = sum(joltage)
    for t in presses:
        opt.add(t >= 0)
        opt.add(t <= total_j)

    for i in range(n):
        touching = [presses[b] for b, btn in enumerate(buttons) if i in btn]
        opt.add(Sum(touching) == joltage[i])

    total_presses = Sum(presses)
    opt.minimize(total_presses)

    # sat -> a satisfying assignment exists given the constraints
    if opt.check() != sat:
        print("No solution")
        return

    model = opt.model()
    solution = [model[t].as_long() for t in presses]
    total_val = sum(solution)
    print("Min total presses:", total_val)
    print("Presses on each butotn:", solution)
    return total_val


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    for content in contents:
        line = content.strip()
        parts = line.split(" ")
        joltage = parts[-1][1:-1].split(",")
        buttons = parts[1:-1]
        # Convert to numbers
        joltage = [int(x) for x in joltage]
        buttons = [[int(y) for y in x[1:-1].split(",")] for x in buttons]
        ans += solve_with_z3(buttons, joltage)
    print(ans)


if __name__ == "__main__":
    main()
