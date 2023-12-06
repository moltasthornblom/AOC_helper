"""Solve AOC for day 6"""
from aoc import get_day_input, post_day_answer
import re


def boat_race(time, distance):
    ways_to_win = []
    for hold in range(0, time):
        if (time - hold) * hold > distance:
            ways_to_win.append(hold)
    return len(ways_to_win)


def solve(v):
    values = list(map(int, v))
    tot = 1
    for i, time in enumerate(values[:4]):
        tot *= boat_race(time, values[4:][i])
    return tot


def solve2(v):
    return boat_race(int("".join(v[:4])), int("".join(v[4:])))


if __name__ == "__main__":
    INP = get_day_input()
    t_and_d = re.findall(r"(\d+)", INP)
    ANSWER1 = solve(t_and_d)
    ANSWER = solve2(t_and_d)
    # print("Level one solved: ", post_day_answer(ANSWER))
    # print("Level two solved: ", post_day_answer(ANSWER, level=2))
