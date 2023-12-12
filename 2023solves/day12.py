"""Solve AOC for day 12"""
from aoc import get_day_input, post_day_answer
import itertools
from functools import cache

INP = get_day_input()
INP2 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1"""


def isValidRow(row, nums):
    groups = [x.strip() for x in row.split(".") if x.count("#") >= 1]
    if len(groups) != len(nums):
        return False
    for i, x in enumerate(nums):
        if i >= len(groups):
            return False
        if x != len(groups[i]):
            return False

    return True


def solve():
    "Solve to puzzle"
    total = 0
    for line in INP.strip().split("\n"):
        valid_c = 0
        row, nums = line.split(" ")
        nums = [int(x) for x in nums.split(",")]
        comb = [
            list(seq) for seq in itertools.product(".#", repeat=list(row).count("?"))
        ]
        for ops in comb:
            tmpStr = list(row)
            for i, x in enumerate(tmpStr):
                if x == "?":
                    tmpStr[i] = ops.pop(0)
            if isValidRow("".join(tmpStr), nums):
                valid_c += 1

        total += valid_c
        # print(row, nums)
    print(total)
    ans = ""
    return ans


if __name__ == "__main__":
    ANSWER = solve()
    # print("Level one solved: " , post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
