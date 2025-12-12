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
        state += dir * dist
        state %= 100
        if state == 0:
            code += 1
    print(f"Code is {code}")


if __name__ == "__main__":
    main()
