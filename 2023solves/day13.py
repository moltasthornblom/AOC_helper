"""Solve AOC for day 13"""
from aoc import get_day_input, post_day_answer
import numpy as np

INP = get_day_input()


def eqc(arr1, arr2, p2):
    if len(arr1) != len(arr2):
        return False

    if p2:
        smudge = 0
        for i, x in enumerate(np.flip(arr1, 1)):
            for i2, y in enumerate(x):
                if y != arr2[i][i2]:
                    smudge += 1
                if smudge > 1:
                    return False
        if smudge != 1:
            return False
    else:
        if not np.array_equal(arr1, np.flip(arr2, 1)):
            return False
    return True


def findVerticalSum(array, p2=False):
    tmp = 0
    # np.flip(arr, axis)
    for flipped, arr in [(0, array), (1, np.flip(array, 1))]:
        nr = 1
        for x in range(1, len(arr[0]) + 1):
            nr += 1
            if x + x > len(arr[0]):
                break

            if eqc(arr[:, 0:x], arr[:, x : x + x], p2):
                if flipped == 0:
                    tmp += x
                else:
                    tmp += len(array[0]) - x
    return tmp


def solve():
    "Solve to puzzle"
    patterns = INP.strip().split("\n\n")
    total = 0
    for pattern in patterns:
        tmpArr = np.array([list(x) for x in pattern.split("\n")])
        vertical = findVerticalSum(tmpArr)
        horizontal = findVerticalSum(np.transpose(tmpArr))

        total += vertical + (100 * horizontal)
    total2 = 0
    for pattern in patterns:
        tmpArr = np.array([list(x) for x in pattern.split("\n")])
        vertical = findVerticalSum(tmpArr, p2=True)
        horizontal = findVerticalSum(np.transpose(tmpArr), p2=True)
        total2 += vertical + (100 * horizontal)
    print(total, total2)

    ans = ""
    return ans


if __name__ == "__main__":
    ANSWER = solve()
    # print("Level one solved: " , post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
