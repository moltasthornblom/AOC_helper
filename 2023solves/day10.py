"""Solve AOC for day 10"""
from aoc import get_day_input, post_day_answer
from rich import print

INP = get_day_input(day=10)

pipes = INP.split("\n")
axis = [-1,0,1]
mod = [(1,0), (-1, 0), (0, 1), (0, -1)]
signs = {
    "|":[(0, -1), (0, 1)],
    "-":[(1,0), (-1, 0)],
    "L":[(-1, 0), (0, 1)],
    "J": [(0, 1), (1, 0)],
    "7": [(1, 0), (0, -1)],
    "F": [(-1, 0), (0, -1)]
}

def find_viable(row, col):
    paths = []
    for aR, aC in mod:
        if row+aR < 0 or col+aC < 0 or col+aC > len(pipes[0])-1 or row + aR > len(pipes)-1:
            continue
        sign = pipes[row+aR][col+aC]
        rules = signs.get(sign, None)
        if rules is None:
            continue
        for x, y in rules:
            if (row+y == row+aR) and (col+x == col+aC):
                paths.append((row+aR, col+aC))
    return paths

def pathfind(row,col):
    counts = {}
    paths=[]
    step = 0
    while True:
        viables = [(x,y) for (x,y) in find_viable(row, col) if f"({x},{y})" not in counts]

        counts[f"({row},{col})"] = step

        if len(viables) == 0:
            break
        else:
            row, col = viables[0]
        step+=1

    return counts



def solve():
    "Solve to puzzle"
    s_ind = INP.replace("\n", "").index("S")
    col = s_ind % len(pipes[0])
    row = int((s_ind-col)/len(pipes[0]))
    counts = []
    furthest = 0
    for x, y in find_viable(row, col):
        counts.append(pathfind(x, y))
    print(counts)
    for x in counts:
        for y, val in x.items(): 
            other = counts[1].get(y)
            if other:
                tmp = min(val, other)
            else: 
                tmp = val
            if(tmp > furthest):
                furthest = tmp
    for i, row in enumerate(pipes):
        for i2, x in enumerate(row):
            if counts[0].get(f"({i},{i2})"):
                print("[green]{x}[/green]".format(x=x), end="")
            else:
                print("[reset]{x}[/reset]".format(x=x), end="")
        print("")
    print(furthest+1)
    ans = ""
    return ans


if __name__ == "__main__":
    ANSWER=solve()
    #print("Level one solved: " , post_day_answer(ANSWER))
    #print("Level two solved: " , post_day_answer(ANSWER,level=2))
