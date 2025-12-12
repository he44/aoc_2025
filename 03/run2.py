import sys
from typing import Optional
from functools import cache


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    for content in contents:
        line = content.strip()
        n = len(line)
        k = 12

        # dp[i][j] denote the maximum number we can generate
        # with strings in line[i:] with j digits. So the final answer will be dp[0][12]
        # Unbounded DP
        @cache
        def _dp(start_index: int, length: int, line: str):
            # No enough characters to generate a string of `length`
            if start_index + length > n:
                return float("-inf")
            # No more characters to pick from.
            if start_index >= n or length < 0:
                return float("-inf")
            # Can only pick one character.
            if start_index == (n - 1) and length == 1:
                return int(line[start_index])
            if length == 0:
                return 0
            # We can generate the number based on sub-cases.
            # Let's pick the max number among line[start_index : i],
            # and then pick the rest of the numbers in line[i:]
            max_num_so_far = int(line[start_index])
            max_joltage = float("-inf")
            for i in range(start_index + 1, n):
                max_joltage = max(
                    max_num_so_far * (10 ** (length - 1)) + _dp(i, length - 1, line),
                    max_joltage,
                )
                max_num_so_far = max(int(line[i]), max_num_so_far)
            return max_joltage

        max_j = _dp(0, k, line)
        ans += max_j
    print(ans)


if __name__ == "__main__":
    main()
