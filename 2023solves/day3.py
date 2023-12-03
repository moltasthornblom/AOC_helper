"""Solve AOC for day 3"""
from aoc import get_day_input, post_day_answer
from itertools import combinations
INP = get_day_input()


def lookaround(prev, grid, gears):
    isAdj = False
    gearCoords = ""
    number = ""
    for coords, num  in prev:
        number+=num
        xPos, yPos = [int(x) for x in coords.split(",")]
        axis = [-1,0,1]
        mod = [(n1, n2) for n1 in axis for n2 in axis]
        for val in mod:
            x, y = val
            newCoords = f"{xPos+x}, {yPos+y}"

            adj = grid.get(newCoords)
            if(adj == "*"):
                if not gears.get(newCoords):
                    gears[newCoords]=[]
                gearCoords = newCoords
            if(adj and not adj.isdigit() and adj != "."):
                isAdj = True
    if(gearCoords != ""):
        gears[gearCoords].append(number)
    if isAdj:
        return int(number)
    return 0


def solve():
    "Solve to puzzle"
    grid={}
    gears={}

    x=0
    y=0
    for row in INP.split("\n"):
        for val in row:
            grid[f"{x}, {y}"] = val
            x+=1
        y+=1
        x=0

    prev = []
    total = 0
    for x, y in grid.items():
        if(y.isnumeric()):
            prev.append([x,y])
        elif(len(prev) != 0):
            total += lookaround(prev,grid, gears)
            prev = []


    #part two
    total2 = 0
    for numbers in gears.values():
        tmpNum = 1
        if(len(numbers) < 2):
            continue
        for x in numbers:
            tmpNum*=int(x)
        total2+=tmpNum



    print(total2)


    return total2


if __name__ == "__main__":
    ANSWER=solve()
    #print("Level one solved: " , post_day_answer(ANSWER))
    #print("Level two solved: " , post_day_answer(ANSWER,level=2))
