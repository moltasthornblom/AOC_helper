"""Solve AOC for day 9"""
from aoc import get_day_input, post_day_answer

INP = get_day_input()


def solve():
    "Solve to puzzle"
    readings = []
    for line in INP.strip().split("\n"):
        extrapolate = [
            [int(x) for x in line.split(" ")],
        ]
        while len([x for x in extrapolate[-1] if x != 0]) != 0:
            arr = []
            for i, x in enumerate(extrapolate[-1]):
                if i + 1 < len(extrapolate[-1]):
                    arr.append(extrapolate[-1][i + 1] - x)
                else:
                    break
            extrapolate.append(arr)
        extrapolate[-1].append(0)
        readings.append(extrapolate)
    total = 0
    for ext in readings:
        tmp = 0
        for x in ext[::-1]:
            tmp += x[-1]
        total += tmp
    total2 = 0
    for ext in readings:
        tmp = 0
        for i, x in enumerate(ext[::-1]):
            if i == 0:
                continue
            tmp = x[0] - tmp
        total2 += tmp
    print(total, total2)
    ans = ""
    return ans


if __name__ == "__main__":
    ANSWER = solve()
    # print("Level one solved: " , post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
