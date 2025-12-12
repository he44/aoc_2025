import sys
from typing import Optional


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    for content in contents:
        line = content.strip()
        n = len(line)
        # ml[i] is the largest value in line[:i]
        # ml[0] is -inf, ml[n] is the max in all
        # mr[i] is the largest value in line[i:]
        # mr[0] is the max in all, mr[n] is inf
        max_on_left = [float("-inf") for _ in range(n + 1)]
        max_on_right = [float("-inf") for _ in range(n + 1)]
        for i in range(1, n + 1):
            max_on_left[i] = max(max_on_left[i - 1], int(line[i - 1]))
        for i in range(n - 1, -1, -1):
            max_on_right[i] = max(max_on_right[i + 1], int(line[i]))
        # construct the largest number by picking a i with max on left and max on right
        max_joltage = 0
        for i in range(n):
            max_joltage = max(max_joltage, 10 * max_on_left[i] + max_on_right[i])
        # print(line)
        # print(max_on_left)
        # print(max_on_right)
        # print(max_joltage)
        # print("-----")
        ans += max_joltage
    print(ans)


if __name__ == "__main__":
    main()
