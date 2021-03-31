import sys
sys.path.append("../../../")

from typing import List, Set
from aoc.utils.utils import get_input

file = get_input()

def solve():
    current_position = [0,0]

    visited = {}

    for char in file:
        if char == "^":
            current_position[1] += 1
        elif char == "v":
            current_position[1] -= 1
        elif char == "<":
            current_position[0] -= 1
        elif char == ">":
            current_position[0] += 1

        t_pos = tuple(current_position)
        if not visited.get(t_pos):
            visited[t_pos] = 1
        else:
            visited[t_pos] += 1

    return visited

visited = solve()

# Filter out houses that were only visited once
visited_more = [visited[x] for x in visited.keys() if visited[x] > 1]
print(visited_more)
