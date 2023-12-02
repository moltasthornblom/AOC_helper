"""Solve AOC for day 2"""
import re
from aoc import get_day_input, post_day_answer

INP = get_day_input()


def solve():
    "Solve to puzzle"
    game = {}
    for line in INP.strip().split("\n"):
        g_id, cubes = re.findall(r'(\d+):(.*)', line)[0]
        for amount, ball in re.findall(r"(\d+)\s([a-z]+)", cubes):
            amount = int(amount)
            if g_id not in game:
                game[g_id] = {ball: amount}
            elif game[g_id].get(ball, 0) < amount:
                game[g_id][ball] = amount

    # part one
    total = 0
    for g_id, cubes in game.items():
        if cubes.get("green", 0) <= 13 and cubes.get("red", 0) <= 12 and cubes.get("blue", 0) <= 14:
            total += int(g_id)

    # part two
    total2 = 0
    for games in game.values():
        power = 1
        for ball in games.values():
            power *= ball
        total2 += power

    return total2


if __name__ == "__main__":
    ANSWER = solve()
    # print("Level one solved: " + post_day_answer(ANSWER))
    # print("Level two solved: " + post_day_answer(ANSWER, level=2))
