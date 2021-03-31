from typing import List, TypeVar

T = TypeVar("T")

def get_input_lines() -> List[T]:
    with open("input", "r") as f:
        return [x.rstrip() for x in f.readlines()]

def get_input() -> str:
    with open("input", "r") as f:
        return f.read()
