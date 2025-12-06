import sys
from typing import Optional


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    print(len(contents))
    # Parse numbers. We cannot ignore spaces here since they affect
    # the computation.
    rows = contents[:-1]
    print([len(row) for row in rows])
    # Parse operators. We need to ignore extra spaces here.
    ops = [x for x in contents[-1].strip().split(" ") if x != ""]
    print(f"Number of ops: {len(ops)}")

    height = len(rows)
    # Ignore the last new line character: \n
    width = len(rows[0]) - 1

    ans = 0
    op_idx = 0
    operands = []
    block_start_c = 0
    for c in range(width):
        all_empty_string = True
        for r in range(height):
            if rows[r][c] != " ":
                # First time a number shows up in this column
                if c - block_start_c >= len(operands):
                    operands.append(int(rows[r][c]))
                else:
                    operands[c - block_start_c] = operands[c - block_start_c] * 10 + int(rows[r][c])
                # print(rows[r][c], operands[r])
                all_empty_string = False
        # If we reach a column without any number or if we reached end,
        # it means we can finish a block of computation and move to
        # the next block.
        if all_empty_string or c == width - 1:
            result = 0 if ops[op_idx] == "+" else 1
            print(operands)
            for operand in operands:
                if ops[op_idx] == "+":
                    result += operand
                else:
                    result *= operand
            ans += result
            print("Result: ", result)
            print("Opreands: ", operands)
            op_idx += 1
            operands = []
            block_start_c = c + 1
    print(ans)



if __name__ == "__main__":
    main()

