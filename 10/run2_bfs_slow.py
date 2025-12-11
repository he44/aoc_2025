import sys
from typing import List, Optional
from dataclasses import dataclass
from collections import deque


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    for content in contents:
        line = content.strip()
        parts = line.split(" ")
        joltage = tuple(parts[-1][1:-1].split(","))
        print(joltage)
        buttons = parts[1:-1]
        # Reverse from lights to 0000 using BFS
        queue = deque()
        queue.append(joltage)
        seen_joltage = set()
        seen_joltage.add(joltage)
        num_press = 0
        found = False
        while queue:
            layer_size = len(queue)
            print(f"Layer size: {layer_size}")
            for _ in range(layer_size):
                cur_joltage = queue.popleft()
                # Let's say the joltage we are trying to get is (52, 32, 33).
                # Since we can only monotonically increase the value by 1
                # with each press, we can never exceed 52 presses.
                # print(cur_joltage)
                if cur_joltage == ("0",) * len(cur_joltage):
                    found = True
                    break
                for button in buttons:
                    next_joltage = list(cur_joltage)
                    applicable = True
                    for idx in button[1:-1].split(","):
                        i = int(idx)
                        # Cannot subtract 1 any more. Overflow.
                        if int(next_joltage[i]) == 0:
                            applicable = False
                            break
                        next_joltage[i] = str(int(next_joltage[i]) - 1)
                    next_joltage = tuple(next_joltage)
                    if applicable and next_joltage not in seen_joltage:
                        seen_joltage.add(next_joltage)
                        queue.append(next_joltage)
            if found:
                break
            num_press += 1
        print(joltage, num_press)
        ans += num_press
    print(f"Total: {ans}")



if __name__ == "__main__":
    main()

