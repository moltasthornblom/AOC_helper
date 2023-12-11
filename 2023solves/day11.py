"""Solve AOC for day 11"""
from aoc import get_day_input, post_day_answer
import numpy as np
from itertools import combinations
INP = get_day_input()

multiplier=1000000

def manhattan_distance(point1, point2):
    distance = 0
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance

def calculate_combinations(galaxies):
    total = 0
    for x, y  in list(combinations(galaxies, 2)):
        total+=manhattan_distance(x, y)
    return total

def solve():
    "Solve to puzzle"
    universe = np.array([list(x) for x in INP.strip().split("\n")])
    newarr = universe.copy()

    for i, row in enumerate(universe):
        if len([x for x in row if x == "."]) == len(row):
            newarr = np.insert(newarr, i+len(newarr)-len(universe), np.array("."*len(newarr[0])), 0)
    
        if len([x for x in universe[:,i] if x == "."]) == len(universe):
            newarr = np.insert(newarr, i+len(newarr[0])-len(universe[0]), np.array("."*len(newarr)), 1)
    galaxies = []

    for i, x in enumerate(newarr):
        for j, y in enumerate(x):
                if y == "#":
                    galaxies.append((i,j))  
   
    return calculate_combinations(galaxies)

def solve2():
    "Solve to puzzle"
    universe = np.array([list(x) for x in INP.strip().split("\n")])
    newarr = universe.copy()

    for i, row in enumerate(universe):
        if len([x for x in row if x == "."]) == len(row):
            newarr[i] = np.array("S"*len(newarr[0]))
    
        if len([x for x in universe[:,i] if x == "."]) == len(universe):
            newarr[:,i] = np.array("S"*len(newarr[0]))
    galaxies = []
    realx = 0
    realy = 0
    for i, x in enumerate(newarr):
        realx = 0
        for j, y in enumerate(x):
            if(y =="S"):
                realx+=multiplier
            else:
                realx+=1
            if y == "#":
                galaxies.append((realy,realx)) 
        if(x.tolist().count("S") == len(x)):
            realy+=multiplier
        else:
            realy+=1
    
    return calculate_combinations(galaxies)

if __name__ == "__main__":
    ANSWER=solve()

    ANSWER2=solve2()
    print(ANSWER, ANSWER2)
    #print("Level one solved: " , post_day_answer(ANSWER))
    #print("Level two solved: " , post_day_answer(ANSWER,level=2))
