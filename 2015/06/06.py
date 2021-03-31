import sys
sys.path.append("../../../")

from aoc.utils.utils import get_input_lines
from typing import List

INPUT: List[str] = get_input_lines()

def parse_instruction(line: str, grid: List[List[int]]):
    split = line.split(" ")
    if len(split) == 5:
        split = split[1:]

    # Handle the instruction, which is the first item in the split 
    instruction: str = split[0]
    start = [int(x) for x in split[1].split(",")]
    startx, starty = start
    end = [int (x) for x in split[-1].split(",")]
    endx, endy = end

    

def solve():
    global INPUT

    # False = Off
    # True = On
    
    # Every light is off
    grid: List[List[bool]] = [[False for x in range(1000)] for y in range(1000)]

    for line in INPUT[:5]:
        parse_instruction(line, grid)

solve()
