from typing import List
import hashlib
from joblib import Parallel, delayed

hashkey: str = "bgvyzdsv"

def solve(start: int, num_zeroes: int):
    global hashkey
    
    while True:
        current_hex: str = hashlib.md5((hashkey + str(start)).encode()).hexdigest()
        if current_hex[:5] == "0"*num_zeroes:
            return start
            break

        start += 1

answer_1: str = solve(start=0, num_zeroes=5)
print(answer_1)
# answer_2: str = solve(answer_1,6)

# The next part will be done in rust since python's GIL and threading is a bit annoying.
