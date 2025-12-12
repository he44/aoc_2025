import sys


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    graph = {}
    reverse_graph = {}
    for content in contents:
        src, dst_part = content.strip().split(": ")
        dst_nodes = dst_part.split(" ")
        graph[src] = dst_nodes
        for dst in dst_nodes:
            if dst not in reverse_graph:
                reverse_graph[dst] = []
            reverse_graph[dst].append(src)
    print(len(graph))
    print(len(reverse_graph))

    # Find set of graphs that can achieve "dac" and "fft"
    stack = ["dac"]
    reachable = set(stack)
    while stack:
        cur = stack.pop()
        if cur not in reverse_graph:
            continue
        for next_node in reverse_graph[cur]:
            if next_node not in reachable:
                reachable.add(next_node)
                stack.append(next_node)
    print(f"Can reach dac: {len(reachable)}")
    print(reachable)

    stack = ["fft"]
    reachable2 = set(stack)
    while stack:
        cur = stack.pop()
        if cur not in reverse_graph:
            continue
        for next_node in reverse_graph[cur]:
            if next_node not in reachable2:
                reachable2.add(next_node)
                stack.append(next_node)
    print(f"Can reach fft: {len(reachable2)}")
    print(reachable2)

    reachable_from_both = reachable.intersection(reachable2)
    print(f"Can reach both: {len(reachable_from_both)}")
    print(reachable_from_both)

    if "svr" not in reachable_from_both:
        print("Cannot go hit both dac / fft from svr")
        return

    num_total_paths = 0
    num_problem_paths = 0
    seen = set()

    def _dfs(
        cur_node: str, cur_path: list[str], seen_dac: bool, seen_fft: bool
    ) -> None:
        print(cur_node, cur_path)
        nonlocal num_total_paths, num_problem_paths
        if cur_node == "out":
            num_total_paths += 1
            if seen_dac and seen_fft:
                num_problem_paths += 1
            return
        if cur_node not in graph:
            return
        for next_node in graph[cur_node]:
            if next_node == "out":
                num_total_paths += 1
                if seen_dac and seen_fft:
                    num_problem_paths += 1
                continue
            if next_node in seen:
                continue
            if not seen_dac and next_node not in reachable:
                continue
            if not seen_fft and next_node not in reachable2:
                continue
            seen.add(next_node)
            _dfs(
                next_node,
                cur_path + [next_node],
                seen_dac or next_node == "dac",
                seen_fft or next_node == "fft",
            )
            seen.remove(next_node)

    seen.add("svr")
    _dfs("svr", ["svr"], False, False)
    print("Total: ", num_total_paths)
    print("Passing dac and fft: ", num_problem_paths)


if __name__ == "__main__":
    main()
