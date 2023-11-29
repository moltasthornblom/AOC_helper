"""Generate AOC boilerplate"""
from aoc.aoc_controller import get_current_day_and_year

day =  get_current_day_and_year()[0]
with open("template.txt", "r", encoding="utf-8") as f:
    file = f.read()
    new = file.replace("{day_here}", str(day))
    with open(f"day{day}.py", "w", encoding="utf-8") as f2:
        f2.write(new)
    print("Generated boilerplate for day", day)
