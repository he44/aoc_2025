import heapq
import math
import sys
from typing import List, Optional
from dataclasses import dataclass

@dataclass
class JunctionBox:
    x: int
    y: int
    z: int
    # Row nubmer in the input file
    id: int
    # Group lead id. The id of the first point in this group
    group_lead_id: int
    # Child ids. Will be empty unless this is a group lead.
    child_ids: Optional[List[int]]


def compute_distance(p1: JunctionBox, p2: JunctionBox):
    return math.sqrt(
        (p1.x - p2.x) ** 2 + 
        (p1.y - p2.y) ** 2 + 
        (p1.z - p2.z) ** 2
    )


def main():
    assert len(sys.argv) == 2, f"Unable to parse args {sys.argv}"
    input_file = sys.argv[1]
    contents = open(input_file).readlines()
    points = []
    i = 0
    for content in contents:
        x, y, z = content.strip().split(",")
        points.append(JunctionBox(int(x), int(y), int(z), i, i, [i]))
        i += 1

    num_points = len(points)

    # Let's compute the distance, and put it in  a priority queue.
    sorted_pairs_by_dist = []
    heapq.heapify(sorted_pairs_by_dist)

    for start in range(num_points):
        for end in range(start + 1, num_points):
            dist = compute_distance(points[start], points[end])
            # Python heapq is min-heap. We need max-heap behavior here.
            heapq.heappush(sorted_pairs_by_dist, (-dist, start, end))

    # Let's start adding.
    # For the example case
    # num_connections = 10
    num_connections = 1000

    to_connect = heapq.nlargest(num_connections, sorted_pairs_by_dist)
    for dist, start_id, end_id in to_connect:
        dist = -dist
        print(f"Trying to connect {points[start_id]} and {points[end_id]} with distance {dist}.")
        start_circuit_lead = points[start_id].group_lead_id
        end_circut_lead = points[end_id].group_lead_id
        if start_circuit_lead == end_circut_lead:
            # Already connected, nothing to do.
            continue

        start_box = points[start_circuit_lead]
        end_box = points[end_circut_lead]
        start_circuit_size = len(start_box.child_ids)
        end_circut_size = len(end_box.child_ids)

        def _merge(bigger_id: int, smaller_id: int):
            bigger_box = points[bigger_id]
            smaller_box = points[smaller_id]
            # Write group lead
            smaller_box.group_lead_id = bigger_box.id
            bigger_box.child_ids = bigger_box.child_ids + smaller_box.child_ids
            # I forgot to update the `group_lead_id` in `child_ids`... Wasn't seeing
            # issue with the example text case.
            # In the end I asked AI to spot this issue for me.
            for child_id in smaller_box.child_ids:
                points[child_id].group_lead_id = bigger_id
            smaller_box.child_ids = []

        if start_circuit_size > end_circut_size:
            _merge(start_circuit_lead, end_circut_lead)
        else:
            _merge(end_circut_lead, start_circuit_lead)

        print(start_box.group_lead_id, end_box.group_lead_id)

    top_3_circuits_size = []
    for point in points:
        # Python is min heap.
        print(len(point.child_ids))
        heapq.heappush(top_3_circuits_size, len(point.child_ids))
        if (len(top_3_circuits_size) == 4):
            heapq.heappop(top_3_circuits_size)
    print(top_3_circuits_size)
    ans = 1
    for size in top_3_circuits_size:
        ans *= size
    print(ans)



if __name__ == "__main__":
    main()

