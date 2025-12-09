import sys
from typing import List, Optional
from dataclasses import dataclass


# My attempt at greedy O(n log n), which is wrong.
def wrong_greedy():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    points = []
    for content in contents:
        c, r = content.strip().split(",")
        c = int(c)
        r = int(r)
        points.append((r, c))
    points = sorted(points)
    # sorted_by_col = sorted(points, key = lambda point: point[1])
    # print(sorted_by_row)
    # print(sorted_by_col)

    left = 0
    right = len(points) - 1
    max_area = 0
    while left < right:
        cur_row_diff = abs(points[left][0] - points[right][0])
        cur_col_diff = abs(points[left][1] - points[right][1])
        cur_area = cur_row_diff * cur_col_diff
        if cur_area > max_area:
            print(f"New max: ${cur_area} from {points[left]} x {points[right]}")
        max_area = max(max_area, cur_area)
        # Now we can move points closers in terms of row.
        # But we only need to compute if there's an increase in col diff.
        # Otherwise, the area must be smaller.
        if left + 1 == right:
            # No more moves.
            break
        # Decide between move left or right.
        next_left = left + 1
        next_left_col_diff = abs(points[next_left][1] - points[right][1])
        next_right = right - 1
        next_right_col_diff = abs(points[left][1] - points[next_right][1])
        if next_left_col_diff > cur_col_diff:
            left += 1
        elif next_right_col_diff > cur_col_diff:
            right -= 1
        else:
            # Both give a shorter col difference, just shrink both,
            # the area won't be larger than cur_area
            left += 1
            right -= 1
    print(max_area)


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    points = []
    for content in contents:
        c, r = content.strip().split(",")
        c = int(c)
        r = int(r)
        points.append((r, c))

    print(points)
    n = len(points)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            print(i, j)
            # Need to add 1 on the sides because it's inclusive.
            cur_area = (
                (abs(points[i][0] - points[j][0]) + 1)*
                (abs(points[i][1] - points[j][1]) + 1)
            )
            max_area = max(
                max_area,
                cur_area
            )
            if i == 1 and j == 5:
                print("Here", cur_area)
    print(max_area)


if __name__ == "__main__":
    main()

