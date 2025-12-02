import sys

def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    state = 50
    code = 0
    for content in contents:
        line = content.strip()
        dir = -1 if (line[0] == "L") else 1
        dist = int(line[1:])
        # Number of times it points at 0 during rotation.
        num_full_cycles = dist // 100
        code += num_full_cycles
        remainder = dist % 100
        if state != 0:
            # We just need to examine if going left crosses 0 or going right crosses 100.
            if dir == 1 and (state + remainder - 100) * (state - 100) < 0:
                code += 1
            if dir == -1 and (state - remainder) * (state) < 0:
                code += 1
        else:
            code += 1
        state += (dir * dist)
        state %= 100
        print(f"After {line} at {state}, collected {code}")
    print(f"Code is {code}")

if __name__ == "__main__":
    main()
