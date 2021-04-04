import sys
sys.path.append("../../..")

from advent_of_code.utils.utils import get_input

file = get_input()

def solve():
    global file

    val: int = 0

    for char in file:
        if char == "(":
            val += 1
        elif char == ")":
            val -= 1

    return val

def solve_two():
    idx: int = 0
    val: int = 0

    while idx != len(file):
        if file[idx] == "(":
            val += 1
        elif file[idx] == ")":
            val -= 1
        if val == -1:
            return idx + 1
            break
        idx += 1

print(solve())
print(solve_two())
