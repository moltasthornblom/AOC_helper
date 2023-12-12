"""Solve AOC for day 10"""
from aoc import get_day_input, post_day_answer
from rich import print

INP = get_day_input(day=10)
INP2 = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""


pipes = INP.split("\n")

outputs = {
    "S": "udlr",
    "J": "lu",
    "F": "rd",
    "|": "ud",
    "-": "lr",
    "L": "ru",
    "7": "ld",
}
inputs = {"S": "udlr", "J": "lu", "F": "rd", "|": "ud", "-": "lr", "L": "ru", "7": "ld"}


def lookaround(x, y, map, prev):
    sign = map.get(f"({x},{y})")
    out = outputs.get(sign, None)
    ops = []

    if "u" in out and "d" in inputs.get(map.get(f"({x},{y-1})", ""), []):
        ops.append((x, y - 1))
    if "d" in out and "u" in inputs.get(map.get(f"({x},{y+1})", ""), []):
        ops.append((x, y + 1))
    if "l" in out and "r" in inputs.get(map.get(f"({x-1},{y})", ""), []):
        ops.append((x - 1, y))
    if "r" in out and "l" in inputs.get(map.get(f"({x+1},{y})", ""), []):
        ops.append((x + 1, y))
    ops = [x for x in ops if x not in prev]
    return ops


def solve():
    step_dic = {}
    start = ""
    pipes_map = {}
    for i, arr in enumerate(pipes):
        for i2, sign in enumerate(arr):
            if sign == "S":
                start = (i2, i)
            pipes_map[f"({i2},{i})"] = sign
    for x in [-1, 0]:
        nxt = start
        steps = 0
        prev = []

        while True:
            if step_dic.get(str(nxt)):
                step_dic[str(nxt)].append(steps)
            else:
                step_dic[str(nxt)] = [
                    steps,
                ]

            prev.append(nxt)
            ops = lookaround(nxt[0], nxt[1], pipes_map, prev)
            if len(ops) == 0:
                break
            nxt = ops[x]
            steps += 1

    min_v = 0
    for x in step_dic.values():
        if min(x) > min_v:
            min_v = min(x)

    print(min_v)


if __name__ == "__main__":
    ANSWER = solve()
    # print("Level one solved: " , post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
