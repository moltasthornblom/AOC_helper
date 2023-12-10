"""Solve AOC for day 7"""
from aoc import get_day_input, post_day_answer
import re
from functools import cmp_to_key

INP = get_day_input()

cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def is_nth_of_a_kind(hand, nth, occ=1):
    sp = [*hand]
    times = []
    for x in sp:
        if x not in times and sp.count(x) == nth:
            if len(times) == occ - 1:
                return True
            else:
                times.append(x)
    return False


def compare(item1, item2):
    h1 = item1[1][0]
    h2 = item2[1][0]
    if item1[0] == item2[0]:
        for x in range(5):
            i1, i2 = cards.index(h1[x]), cards.index(h2[x])
            if i1 != i2:
                return i2 - i1

    elif item1[0] < item2[0]:
        return -1
    else:
        return 1


def rank_hand(hand):
    if re.search(r"(\w+)\1{4}", hand):
        return 7
    elif is_nth_of_a_kind(hand, 4):
        return 6
    elif is_nth_of_a_kind(hand, 3) and is_nth_of_a_kind(hand, 2):
        return 5
    elif is_nth_of_a_kind(hand, 3):
        return 4
    elif is_nth_of_a_kind(hand, 2, 2):
        return 3
    elif is_nth_of_a_kind(hand, 2):
        return 2
    else:
        return 1


def solve(part=1):
    "Solve to puzzle"
    hands = []
    for line in INP.strip().split("\n"):
        hand, bid = re.findall(r"(\w+)\s(\d+)", line)[0]
        best_rank = 0
        # Part two
        if "J" in hand and part == 2:
            for card in cards:
                tmp = rank_hand(hand.replace("J", card))
                if tmp > best_rank:
                    best_rank = tmp
        else:
            best_rank = rank_hand(hand)
        hands.append((best_rank, (hand, int(bid))))

    hands = sorted(hands, key=cmp_to_key(compare))
    tot = 0
    for i, (x, hand) in enumerate(hands):
        tot += (i + 1) * hand[1]
    print(tot)
    return tot


if __name__ == "__main__":
    ANSWER = solve()
    # print("Level one solved: ", post_day_answer(ANSWER))
    # print("Level two solved: " , post_day_answer(ANSWER,level=2))
