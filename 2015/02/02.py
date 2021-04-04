from typing import List, Tuple, Set
import sys
sys.path.append("../../..")

from advent_of_code.utils.utils import *
from itertools import permutations

# Clean up the input into ints
file: List[str] = get_input_lines()
file: List[str] = [x.rstrip() for x in file]
# Oh yeah, this line is gnarly.
file: List[Tuple[int]]  = [tuple((int(x) for x in x.split("x"))) for x in file]

def get_area(t: Tuple[int]) -> int:
    """
    Return the square footage of the dimensions,
    plus the square footage of the smallest side.
    """
    l: int = t[0]
    w: int = t[1]
    h: int = t[2]

    side_areas: Set[int] = set([x[0]*x[1] for x in permutations(t,2)])

    return (2*l*w + 2*w*h + 2*h*l) + min(side_areas)

# Test to make sure this func works
assert get_area((2,3,4)) == 58

def solve():
    global file

    total_area: int = 0

    for box in file:
        total_area += get_area(box)

    return total_area

answer_one = solve()

def calc_smallest_perimiter(t: Tuple[int]) -> int:
    perms = permutations(t, 2)
    perimiters: Set[int] = set([2*x[0]+2*x[1] for x in perms])

    return min(perimiters)

assert calc_smallest_perimiter((2,3,4)) == 10
assert calc_smallest_perimiter((1,1,10)) == 4

def solve_two():
    global file

    total_footage: int = 0

    for box in file:
        segment_one: int = calc_smallest_perimiter(box)
        segment_two: int = box[0]*box[1]*box[2]
        total_footage += segment_one + segment_two

    return total_footage

answer_two = solve_two()
print(answer_two)
