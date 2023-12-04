"""Solve AOC for day 4"""
from aoc import get_day_input, post_day_answer
import re
INP = get_day_input()


def solve():
    "Solve to puzzle"
    lines = INP.strip().split("\n")
    total=0
    total2=0
    new_cards={}
    for i, x in enumerate(lines, start=1):
        nrs = re.findall("(\d+)", x)
        win_nr = nrs[1:11]
        my_num = nrs[11:]
        points=0
        points2 = 0
        for x in win_nr:
            if x in my_num:
                if not points:
                    points = 1
                else:
                    points*=2
                points2+=1
                    
        if points2:
            nm = new_cards.get(str(i),0)+1
            for x in range(1, points2+1):
                if new_cards.get(str(i+x)):
                    new_cards[str(i+x)] += 1*nm
                else:
                    new_cards[str(i+x)] = 1*nm
        total+=points
        total2+=new_cards.get(str(i),0)+1

    return total


if __name__ == "__main__":
    ANSWER=solve()
    #print("Level one solved: " , post_day_answer(ANSWER))
    #print("Level two solved: " , post_day_answer(ANSWER,level=2))
