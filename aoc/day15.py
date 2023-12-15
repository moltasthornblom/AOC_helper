"""Solve AOC for day 15"""
from aoc import get_day_input, post_day_answer

INP = get_day_input()
INP = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

boxes = {}


def HASH(string):
    cur_val = 0

    for char in string:
        cur_val += ord(char)
        cur_val *= 17
        cur_val = cur_val % 256

    return cur_val


def solve():
    "Solve to puzzle"
    hsum = 0
    for ins in INP.split(","):
        hsum += HASH(ins.strip())
    print(hsum)
    ans = ""
    return ans


def update_lens(ins):
    label, focal_length = ins.split("=")
    hsh = str(HASH(label))
    box = boxes.get(hsh)
    if box:
        for i, (x, y) in enumerate(box):
            if x == label:
                boxes[hsh][i] = (label, focal_length)
                return
        boxes[hsh].append((label, focal_length))
    else:
        boxes[hsh] = [
            (label, focal_length),
        ]


def remove_lens(ins):
    label = ins[:-1]
    hsh = str(HASH(label))
    box = boxes.get(hsh)
    if box:
        for i, (x, y) in enumerate(box):
            if x == label:
                boxes[hsh].pop(i)


def solve2():
    for ins in INP.strip().split(","):
        if "=" in ins:
            update_lens(ins)
        elif "-" in ins:
            remove_lens(ins)
    tot = 0
    for box_num, content in boxes.items():
        for i, (label, focal_length) in enumerate(content):
            tot += int(focal_length) * (i + 1) * (int(box_num) + 1)
    print(tot)


if __name__ == "__main__":
    ANSWER = solve2()
    # print("Level one solved: " , post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
