import sys


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    graph = {}
    for content in contents:
        src, dst_part = content.strip().split(": ")
        dst_nodes = dst_part.split(" ")
        graph[src] = dst_nodes

    num_solutions = 0

    def _dfs(cur_node: str, cur_path: list[str]) -> None:
        nonlocal num_solutions
        if cur_node == "out":
            num_solutions += 1
            return
        for next_node in graph[cur_node]:
            if next_node == "out":
                num_solutions += 1
                continue
            _dfs(next_node, cur_path + [next_node])

    _dfs("you", ["you"])
    print(num_solutions)


if __name__ == "__main__":
    main()
