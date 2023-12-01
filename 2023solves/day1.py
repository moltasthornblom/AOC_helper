"""Solve AOC for day 1"""
from aoc import get_day_input, post_day_answer

INP = get_day_input()


def isDigit(string):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    for x in digits.keys():
        if x in string:
            return str(digits.get(x))


def solve(part_two=False):
    "Solve to puzzle"
    total = 0
    for x in INP.split("\n"):
        row = []
        tmp = ""
        for y in x:
            if y.isnumeric():
                row.append(y)
                tmp = ""
                continue
            else:
                tmp += y

            if isDigit(tmp) and part_two:
                row.append(isDigit(tmp))
                tmp = tmp[-1]
        if len(row) > 0:
            total += int(row[0] + row[-1])

    print("answer:", total)

    ans = total
    return ans


if __name__ == "__main__":
    ANSWER = solve(part_two=True)
    # print("Level one solved: " + post_day_answer(ANSWER))
    # print("Level two solved: " + post_day_answer(ANSWER, level=2))
