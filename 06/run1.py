import sys
from typing import Optional


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    print(len(contents))
    rows_of_numbers = []
    # Parse numbers
    for content in contents[:-1]:
        line = content.strip().split(" ")
        numbers = [int(x) for x in line if x != ""]
        print(f"Number of nums: {len(numbers)}")
        rows_of_numbers.append(numbers)
    # Parse operators
    ops = [x for x in contents[-1].strip().split(" ") if x != ""]
    print(f"Number of ops: {len(ops)}")

    height = len(rows_of_numbers)
    width = len(ops)
    ans = [1 if ops[i] == "*" else 0 for i in range(width) ]
    for r in range(height):
        for c in range(width):
            if ops[c] == "*":
                ans[c] *= rows_of_numbers[r][c]
            else:
                ans[c] += rows_of_numbers[r][c]
    print(sum(ans))


if __name__ == "__main__":
    main()

