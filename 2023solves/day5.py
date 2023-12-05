"""Solve AOC for day 5"""
from aoc import get_day_input, post_day_answer
import re
INP= get_day_input()
mapss = []
maps_raw = INP.split("\n\n")
for x in maps_raw[1:]:
    mapss.append(re.findall(r"(\d+\s\d+\s\d+)", x))
    
seeds = [int(x) for x in re.findall(r"(\d+)", maps_raw[0])]


def solve(seeds):
    "Solve to puzzle"
    for maps in mapss:
        newarr = seeds.copy()
        for x in maps:
            after, pre, rng = x.split(" ")
            after = int(after)
            pre = int(pre)
            rng = int(rng)
            for i, val in enumerate(newarr):
                if (val >= pre and val < pre+rng):
                    seeds[i] = after+(val-pre)
    lowest = min(seeds)
    return lowest
                            
def get_overlap(r1, r2):
    r1s = r1[0]
    r1e = r1[1]
    r2s = r2[0]
    r2e = r2[1]
    if((r1s >= r2s and r1s <= r2e)):
        if(r1e >= r2e):
            return (r1s, r2e), (r2e, r1e)
        if(r1e < r2e):
            return (r1s, r1e), (1,1)
    elif((r1e >= r2s and r1e <= r2e)):
        return (r2s, r1e), (r1s, r2s)
    elif(r1e >= r2s and r1s <= r2s):
        return (r2s, r2e), (1, 1)
    else:
        return (1,1), (1,1)

def solve2(seeds):
    pairs = []
    i = 0
    while i+1 < len(seeds):
        pairs.append((int(seeds[i]), int(seeds[i+1])))
        i += 2
    for maps in mapss:
        for i, (start, rng_2) in enumerate(pairs):
            for x in maps:
                after, pre, rng = x.split(" ")
                after, pre, rng = int(after), int(pre), int(rng)
                overlap, remains = get_overlap((start, start+rng_2), (pre,pre+rng))
                diff = after-pre
                if(overlap[1]-overlap[0] > 0):  
                    pairs[i] = (overlap[0]+diff,overlap[1]-overlap[0])
                    if(remains[1]-remains[0] > 0):
                        pairs.append((remains[0], remains[1]-remains[0]))
                    
    return min([x[0] for x in pairs])


if __name__ == "__main__":
    ans1 = solve(seeds.copy())
    ans2 = solve2(seeds)
    print(ans1, ans2)


    
    #ANSWER = solve2(seeds)
    # print("Level one solved: " , post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
