"""Solve AOC for day 2"""
from aoc import get_day_input, post_day_answer
import re

INP = get_day_input()


def solve():
    "Solve to puzzle"
    game = {}
    for x in INP.split("\n"):
        if not x:
            continue
        info = x.split("Game ")[1]
        g_id, cubes = info.split(":")
        for y in cubes.split(";"):
            for y in y.split(","):
                amount, ball = y.strip().split(" ")
                amount = int(amount)
                if g_id not in game:
                    game[g_id] = {ball: amount}
                elif game[g_id].get(ball, 0) < amount:
                    game[g_id][ball] = amount

    # part one
    total = 0
    for x, y in game.items():
        if y.get("green", 0) <= 13 and y.get("red", 0) <= 12 and y.get("blue", 0) <= 14:
            total += int(x)

    # part two
    total2 = 0
    for games in game.values():
        power = 1
        for ball in games.values():
            power = power * ball
        total2 += power
    print(total2)
    ans = total2
    return ans


if __name__ == "__main__":
    ANSWER = solve()
    # print("Level one solved: " + post_day_answer(ANSWER))
    # print("Level two solved: " + post_day_answer(ANSWER, level=2))
