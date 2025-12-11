import sys
from typing import List, Optional
from dataclasses import dataclass
from queue import Queue


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    ans = 0
    for content in contents:
        line = content.strip()
        parts = line.split(" ")
        lights = parts[0][1:-1]
        # print(lights)
        buttons = parts[1:-1]
        # Reverse from lights to 0000 using BFS
        queue = Queue()
        queue.put(lights)
        seen_lights = set()
        seen_lights.add(lights)
        num_press = 0
        found = False
        while not queue.empty():
            layer_size = queue.qsize()
            # print(f"Layer size: {layer_size}")
            for _ in range(layer_size):
                cur_lights = queue.get()
                # print(cur_lights)
                if cur_lights == "." * len(cur_lights):
                    # print("Here!", cur_lights)
                    found = True
                    break
                for button in buttons:
                    next_lights = list(cur_lights)
                    for idx in button[1:-1].split(","):
                        i = int(idx)
                        if next_lights[i] == ".":
                            next_lights[i] = "#"
                        else:
                            next_lights[i] = "."
                    next_lights = "".join(next_lights)
                    if next_lights not in seen_lights:
                        seen_lights.add(next_lights)
                        queue.put(next_lights)
                        # print("Added")
            if found:
                break
            num_press += 1
        print(lights, num_press)
        ans += num_press
    print(f"Total: {ans}")



if __name__ == "__main__":
    main()

