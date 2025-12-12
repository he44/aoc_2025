import sys
from typing import Optional


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    height = len(contents)
    width = len(contents[0].strip())

    def _count_paper_in_neighbor(r: int, c: int) -> int:
        num_paper = 0
        for dr, dc in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ):
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width and contents[nr][nc] == "@":
                num_paper += 1
        return num_paper

    # We only keep track neighbor count of cells with paper.
    neighbor_count = [[0 for c in range(width)] for r in range(height)]
    to_remove = set()
    for r in range(height):
        for c in range(width):
            if contents[r][c] == "@":
                neighbor_count[r][c] = _count_paper_in_neighbor(r, c)
                if neighbor_count[r][c] < 4:
                    to_remove.add((r, c))
            else:
                neighbor_count[r][c] = None
    print(f"Part 1: {len(to_remove)}")

    # Part 2
    num_removed = 0
    while to_remove:
        # We're about to remove those, so the `neighbor_count` of each of
        # their neighbor will decrease by 1. This opens up potentially new
        # ones to remove
        next_round_to_remove = set()
        for r, c in to_remove:
            num_removed += 1
            neighbor_count[r][c] = None
            for dr, dc in (
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ):
                nr, nc = r + dr, c + dc
                # Out of bounds.
                if nr < 0 or nr >= height or nc < 0 or nc >= width:
                    continue
                # Already being removed.
                if (nr, nc) in to_remove:
                    continue
                # Haven't been removed, and haven't been "planned" to get removed
                if neighbor_count[nr][nc] is not None:
                    neighbor_count[nr][nc] -= 1
                    if neighbor_count[nr][nc] < 4:
                        next_round_to_remove.add((nr, nc))
        to_remove = next_round_to_remove
        # print(sorted(list(to_remove)))
        # print("\n".join(["".join([str(i) if i is not None else "." for i in line]) for line in neighbor_count]))
    print(f"Part 2: {num_removed}")


if __name__ == "__main__":
    main()
