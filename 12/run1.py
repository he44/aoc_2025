import sys

"""
I initially thought of backtracking but the state space looks huge.
Reminded me of Day 10 Part 2. :|
Drew a bunch of shapes by hand. Didn't find any tricks.
Then I saw some comments / memes saying it's a troll problem. :)
I got the answer by just multiplying the number of shapes we need to fit by 9. 
If the region space is larger than that, we increment the answer.

Later, I saw this Reddit post:
https://www.reddit.com/r/adventofcode/comments/1pkjynl/comment/ntlq9n3/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button
and decided to actually assert that all test cases fall into "easy cases".
Easy case as in:
- not enough space for "perfect fitting shapes" (i.e. these shapes can be put together without a single space in between
- enough space for giving each shape a 3 x 3 sub-region for itself 
    - for this case, I think it's safer to assert both width and legnth, instead of just the size.
      A counter example is 9 x 2 region cannot fit two 3 x 3 box, or a C shape. 
Turns out all the cases in the actual input is "easy"

The first example case is a "hard" case though :sad.
"""


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).read().strip()
    sections = contents.split("\n\n")
    print(sections)
    shapes = []
    shape_sizes = []
    for section in sections[:-1]:
        shape = section.split("\n")[1:]
        shapes.append(shape)
        # Number of occupied space.
        shape_sizes.append(sum([x.count("#") for x in shape]))
    for shape, shape_size in zip(shapes, shape_sizes):
        print(shape, shape_size)
    # It seems all the presents are 3 x 3.
    trees = sections[-1].split("\n")
    ans = 0
    for tree in trees:
        width_times_height, counts = tree.split(": ")
        width, height = width_times_height.split("x")
        width, height = int(width), int(height)
        available_space = width * height
        counts = [int(x) for x in counts.split(" ")]
        needed_space_no_overlap = 9 * sum(counts)
        needed_space_perfect_overlap = 0
        for num_shape, shape_size in zip(counts, shape_sizes):
            needed_space_perfect_overlap += num_shape * shape_size
        # print(
        #     f"Have {available_space}. "
        #     f"If perfect overlap: {needed_space_perfect_overlap}."
        #     f"If no overlap: {needed_space_no_overlap}"
        # )
        if available_space < needed_space_perfect_overlap:
            # Definitely not possilbe! Even if we are breaking all
            # shapes into unit squares and placing them one by one,
            # we still cannot fit all.
            continue
        elif available_space >= needed_space_no_overlap:
            # Definitely possible (?)
            # Techinically we need to assert row / col as well I think?
            # Because a 9 x 2 cannot fit 2 3 x 3
            assert (width // 3) * (height // 3) >= sum(
                counts
            ), f"Enough units, but not enough side lengths"
            ans += 1
        else:
            print(
                f"Available space in between: {needed_space_perfect_overlap}"
                f" < {available_space} < {needed_space_no_overlap}"
            )
            assert False
    print(ans)


"""
1 0 1 0 2 2
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

....AAAFFE.E
.BBBAAFFFEEE
DDDBAAFFCECE
DBBB....CCC.
DDD.....C.C.
"""


if __name__ == "__main__":
    main()
