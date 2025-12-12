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
    ans = 0
    for line in contents:
        if line == "\n" or line.find("-") != -1:
            continue
        num = int(line.strip())
        fresh = False
        for left, right in ranges:
            if num >= left and num <= right:
                fresh = True
                break
        if fresh:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
