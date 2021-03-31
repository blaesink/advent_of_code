import sys
sys.path.append("../../../")

from aoc.utils.utils import get_input_lines

INPUT = get_input_lines()
INPUT = [x.rstrip() for x in INPUT]

def naughty_nice(string: str) -> bool:
    """
        Returns:
            True if nice
            False if naughty
    """

    for combo in ["ab", "cd", "pq", "xy"]:
        if string.find(combo) > 0:
            return False

    # Get a count of the vowels in the input string
    vowel_count: int = 0
    for char in "aeiou":
        vowel_count += string.count(char)

    # Get the individual chars
    chars = set(string)
    has_duplicate: bool = False
    for char in chars:
        if string.find(char*2) >= 0:
            has_duplicate = True
            break

    return (vowel_count >= 3
            and has_duplicate)

assert naughty_nice("ugknbfddgicrmopn") == True
assert naughty_nice("aaa") == True
assert naughty_nice("jchzalrnumimnmhp") == False
assert naughty_nice("haegwjzuvuyypxyu") == False
assert naughty_nice("dvszwmarrgswjxmb") == False

def solve():
    global INPUT

    num_naughty: int = 0
    num_nice: int = 0

    for line in INPUT:
        if naughty_nice(line):
            num_nice += 1
        else:
            num_naughty += 1

    return (num_nice, num_naughty)

answer_one = solve()
print(answer_one)
