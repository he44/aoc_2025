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
    beam_points = set()
    # Find entry point
    for c in range(width):
        if contents[0][c] == "S":
            beam_points.add((0, c))

    num_split = 0
    # Layer by layer
    while True:
        new_beam_points = set()
        while beam_points:
            r, c = beam_points.pop()
            # print(r, c)
            # Check the next line
            splitted = False
            if r + 1 < height and contents[r + 1][c] == "^":
                if c - 1 >= 0:
                    new_beam_points.add((r + 1, c - 1))
                    splitted = True
                if c + 1 < width:
                    new_beam_points.add((r + 1, c + 1))
                    splitted = True
            if r + 1 < height and contents[r + 1][c] == ".":
                new_beam_points.add((r + 1, c))
            if splitted:
                num_split += 1
        beam_points = new_beam_points
        if not beam_points:
            break
    print(num_split)


if __name__ == "__main__":
    main()

