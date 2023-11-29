"Test auth and day recognition"
from aoc.aoc_controller import get_current_day_and_year, check_if_authorized
print("Authorized: ", check_if_authorized())
day, year = get_current_day_and_year()
print("Day and year: ", day, year)
