import sys
from typing import List, Optional
from dataclasses import dataclass

# Quite challenging for me.
# https://www.reddit.com/r/adventofcode/comments/1phywvn/comment/nt2rxav/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    points = []
    # Horizontal lines
    row_bounds = []
    # Vertical lines
    col_bounds = []
    for content in contents:
        c, r = content.strip().split(",")
        c = int(c)
        r = int(r)
        # Update boundaries
        if points:
            if points[-1][0] == r:
                row_bounds.append((points[-1], (r, c)))
            elif points[-1][1] == c:
                col_bounds.append((points[-1], (r, c)))
            else:
                assert False, "Not valid boundary"
        points.append((r, c))
    # Connect last point to the first point
    if points[-1][0] == points[0][0]:
        row_bounds.append((points[-1], points[0]))
    elif points[-1][1] == points[0][1]:
        col_bounds.append((points[-1], points[0]))
    else:
        assert False, "Not valid boundary"
    print(len(row_bounds))
    print(len(col_bounds))
    print(len(points))

    n = len(points)
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            # Need to add 1 on the sides because it's inclusive.
            cur_area = (abs(points[i][0] - points[j][0]) + 1) * (
                abs(points[i][1] - points[j][1]) + 1
            )
            # Examine whether this rectangle gets crossed by boundaries
            min_r = min(points[i][0], points[j][0])
            max_r = max(points[i][0], points[j][0])
            min_c = min(points[i][1], points[j][1])
            max_c = max(points[i][1], points[j][1])
            # print(
            #     min_r, max_r, min_c, max_c
            # )
            # Rectangle: upside and downside
            # at min_r, between (min_c, max_c)
            # at max_r, between (min_c, max_c)
            intersected = False
            for v_bar in col_bounds:
                v_bar_up = min(v_bar[0][0], v_bar[1][0])
                v_bar_down = max(v_bar[0][0], v_bar[1][0])
                v_bar_col = v_bar[0][1]
                # I missed the case when the vertical bar is within my rectangle.
                # Asked AI for this hint.
                # if (v_bar_up < min_r < v_bar_down and
                #     min_c < v_bar_col < max_c):
                #     intersected = True
                # if (v_bar_up < max_r < v_bar_down and
                #     min_c < v_bar_col < max_c):
                #     intersected = True
                if min_c < v_bar_col < max_c and not (
                    v_bar_down <= min_r or v_bar_up >= max_r
                ):
                    intersected = True
            if intersected:
                continue
            # Rectangle: left and right
            # at min_c, betweeen (min_r, max_r)
            # at max_c, betweeen (min_r, max_r)
            for h_bar in row_bounds:
                h_bar_left = min(h_bar[0][1], h_bar[1][1])
                h_bar_right = max(h_bar[0][1], h_bar[1][1])
                h_bar_row = h_bar[0][0]
                # if (h_bar_left < min_c < h_bar_right
                #         and min_r < h_bar_row < max_r):
                #     intersected = True
                # if (h_bar_left < max_c < h_bar_right
                #         and min_r < h_bar_row < max_r):
                #     intersected = True
                if min_r < h_bar_row < max_r and not (
                    h_bar_right <= min_c or h_bar_left >= max_c
                ):
                    intersected = True
            if intersected:
                continue
            max_area = max(max_area, cur_area)
    print(max_area)


if __name__ == "__main__":
    main()
