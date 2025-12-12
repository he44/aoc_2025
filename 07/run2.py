# My approach was trying to enumerate all the possible paths :(.
# Which is probably a bad idea for this 140 x 140 grid.

import sys
from typing import List, Optional
from functools import cache


@cache
def _mutate_state(
    prev: str, r: int, c: int, height: int, width: int, new_char: str
) -> str:
    list_chars = list(prev)
    list_chars[r * width + c] = new_char
    return "".join(list_chars)


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0

    # Ignore the \n at the end of each line.
    init_state = [list(line.strip()) for line in contents]
    height = len(init_state)
    width = len(init_state[0])

    print(height, width)

    # Now we need to pass in the state

    # Find entry point
    entry_col = None
    for c in range(width):
        if init_state[0][c] == "S":
            entry_col = c
            break

    assert entry_col is not None

    # Let's use row-major-order and flatten out the list into string so that
    # we can properly cache this.
    init_state_str = "".join([x for line in init_state for x in line])
    print(init_state_str)

    # All unique multi-verse if we start at r, c, with state
    @cache
    def _recurse(r: int, c: int, state: str) -> set:
        # Base case: already at the last row
        if r + 1 == height:
            return set([state])
        # Try to move forward, simple case, no split
        unique_states_from_here = set()
        if state[(r + 1) * width + c] == ".":
            state = _mutate_state(state, r + 1, c, height, width, "|")
            new_states = _recurse(r + 1, c, state)
            state = _mutate_state(state, r + 1, c, height, width, ".")
            unique_states_from_here.update(new_states)
        # Try to move forward with splitting
        if state[(r + 1) * width + c] == "^":
            if c - 1 >= 0 and state[(r + 1) * width + c - 1] == ".":
                # (we are assuming no adjacent splitters?)
                state = _mutate_state(state, r + 1, c - 1, height, width, "|")
                new_states = _recurse(r + 1, c - 1, state)
                state = _mutate_state(state, r + 1, c - 1, height, width, ".")
                unique_states_from_here.update(new_states)
            if c + 1 < width and state[(r + 1) * width + c + 1] == ".":
                # (we are assuming no adjacent splitters?)
                state = _mutate_state(state, r + 1, c + 1, height, width, "|")
                new_states = _recurse(r + 1, c + 1, state)
                state = _mutate_state(state, r + 1, c + 1, height, width, ".")
                unique_states_from_here.update(new_states)
        return unique_states_from_here

    all_unique_states = _recurse(0, entry_col, init_state_str)
    print(len(all_unique_states))


def test():
    contents = r"""...S......|..."""

    height = 2
    width = 7
    print(contents)
    new_state = _mutate_state(contents, 0, 3, 2, 7, "|")
    print(new_state)
    reverted_state = _mutate_state(contents, 0, 3, 2, 7, "S")
    print(reverted_state)
    assert contents == reverted_state


if __name__ == "__main__":
    # test()
    main()
