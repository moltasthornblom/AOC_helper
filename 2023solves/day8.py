"""Solve AOC for day 8"""
from aoc import get_day_input, post_day_answer
import re
from math import lcm

INP = get_day_input(day=8).strip()


def solve():
    "Solve to puzzle"
    maps = {}
    ins = INP.split("\n")[0].replace("L", "0").replace("R", "1")
    for line in INP.split("\n")[2:]:
        g = re.findall(r"(\w{3})\s=\s\((\w{3}),\s(\w{3})\)", line)[0]
        maps[g[0]] = (g[1], g[2])

    nxt = "AAA"
    pointer = 0
    steps = 0
    while nxt != "ZZZ":
        nxt = maps[nxt][int(ins[pointer])]
        steps += 1
        if pointer + 1 == len(ins):
            pointer = 0
            continue
        pointer += 1

    ans = steps
    return ans


def solve2():
    "Solve to puzzle"
    maps = {}
    ins = INP.split("\n")[0].replace("L", "0").replace("R", "1")
    for line in INP.split("\n")[2:]:
        g = re.findall(r"(\w{3})\s=\s\((\w{3}),\s(\w{3})\)", line)[0]
        maps[g[0]] = (g[1], g[2])

    start = [x for x in maps if x[-1] == "A"]
    nxt = ""
    pointer = 0
    steplist = []
    for x in start:
        steps = 0
        nxt = x
        while nxt[-1] != "Z":
            nxt = maps[nxt][int(ins[pointer])]
            steps += 1
            if pointer + 1 == len(ins):
                pointer = 0
                continue
            pointer += 1
        steplist.append(steps)

    ans = lcm(*steplist)
    return ans


if __name__ == "__main__":
    print(solve())
    print(solve2())
    # print("Level one solved: " , post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
