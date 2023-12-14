"""Solve AOC for day 14"""
from aoc import get_day_input, post_day_answer
import numpy as np

INP = get_day_input()
INP2 = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
rocks = np.array([list(line) for line in INP.strip().split("\n")])


def tiltNorth(array):
    exhausted = False
    while not exhausted:
        mod = 0
        for i, row in enumerate(array):
            for j, rock in enumerate(row):
                if rock == "O" and i - 1 >= 0 and array[i - 1][j] == ".":
                    array[i - 1][j] = "O"
                    array[i][j] = "."
                    mod += 1
        if not mod:
            exhausted = True
    return array


def calculateWeight(array):
    total = 0
    for i, row in enumerate(array):
        for rock in row:
            if rock == "O":
                total += len(array) - i

    return total


def performCycle(array):
    array = tiltNorth(array)  # Tilt north
    array = np.transpose(tiltNorth(np.transpose(array)))  # Tilt west,

    array = np.flip(tiltNorth(np.flip(array, 0)), 0)  # Tilt South

    array = np.transpose(
        np.flip(tiltNorth(np.flip(np.transpose(array), 0)), 0)
    )  # Tilt east
    return array


def solve():
    rocks = np.array([list(line) for line in INP.strip().split("\n")])

    "Solve to puzzle"
    rocks = tiltNorth(rocks)
    total = calculateWeight(rocks)

    print(total)
    ans = ""
    return ans


def solve2():
    rocks = np.array([list(line) for line in INP.strip().split("\n")])
    for x in range(150):
        rocks = performCycle(rocks)

    cycles = 0
    prevWeights = []
    for x in range(100):
        cycles += 1
        rocks = performCycle(rocks)
        w = calculateWeight(rocks)
        prevWeights.append(w)

    index = 0
    for i in range(1, len(prevWeights)):
        if (
            prevWeights[i] == prevWeights[0]
            and prevWeights[i + 1] == prevWeights[1]
            and prevWeights[i + 2] == prevWeights[2]
        ):
            index = i
            break
    print(prevWeights[999999850 % index - 1])


if __name__ == "__main__":
    ANSWER = solve2()
    # print("Level one solved: " , post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
