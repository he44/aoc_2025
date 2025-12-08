# https://www.reddit.com/r/adventofcode/comments/1pgxv5w/year_2025_day_7_no_memoization_still_runs_in_10_%C2%B5s/
# Hmmm... I'm really trying the memoization approach.


import sys
from typing import Optional


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    height = len(contents)
    # Ignore the \n at the end of each line.
    width = len(contents[0]) - 1
    entry_c = None
    # Find entry point
    for c in range(width):
        if contents[0][c] == "S":
            entry_c = c
    assert entry_c is not None

    counts = [0 for r in range(width)]
    counts[entry_c] = 1
    print(0, counts)
    for r in range(1, height):
        new_counts = [0 for r in range(width)]
        for c in range(width):
            if contents[r - 1][c] == "S" or contents[r - 1][c] == ".":
                # Same number of ways to achieve this row, at the same column.
                new_counts[c] += counts[c]
            if c - 1 >= 0 and contents[r - 1][c - 1] == "^":
                new_counts[c] += counts[c - 1]
            if c + 1 < width and contents[r - 1][c + 1] == "^":
                new_counts[c] += counts[c + 1]
        counts = new_counts
        print(1, counts)

    print(sum(counts))


if __name__ == "__main__":
    main()

