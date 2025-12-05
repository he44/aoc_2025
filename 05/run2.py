import sys
from typing import Optional


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    # Let's try brute-force
    ranges = []
    for line in contents:
        if line == "\n":
            continue
        if line.find("-") != -1:
            left, right = line.strip().split("-")
            ranges.append((int(left), int(right)))
    ranges.sort()
    # Sort by left first, then right
    max_right = float("-inf")
    ans = 0
    for left, right in ranges:
        if left > max_right:
            ans += (right - left + 1)
            max_right = right
        elif right > max_right:
            ans += (right - max_right)
            max_right = right
        print(left, right, ans)
    print(ans)


if __name__ == "__main__":
    main()

