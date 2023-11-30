"""Advent of code controller"""
from datetime import date
from ._util import _get_diff_date
from ._aoc import _aoc_get_request_with_oath, _aoc_post_request_with_oath
from ._cache_middleware import _cache_request

# CONSTANTS

DATE1 = date(2023, 12, 1)
DATE2 = date.today()
WRONG_ANSWER = "That's not the right answer."
TOO_MANY_ANSWERS = "You gave an answer too recently"


def _check_if_valid_day(day):
    """Check if day is within timespan of calendar"""
    if day <= 0 or day > 25:
        return True
    return False


def get_current_day_and_year():
    """Returns current day and year of aoc"""
    return _get_diff_date(DATE1, DATE2), DATE2.year


def _check_if_status_ok(status):
    """Validate status code is 200"""
    if status == 200:
        return True
    return False


def check_if_authorized():
    """Test if client is authorized"""
    status = _aoc_get_request_with_oath("http://adventofcode.com/2022/day/1/input")[0]
    if _check_if_status_ok(status):
        return True
    return False


def get_day_input(day=_get_diff_date(DATE1, DATE2), year=DATE2.year):
    """Get aoc input of current day or specified day"""
    if _check_if_valid_day(day):
        print("Invalid day.")
        return 0
    uri = f"http://adventofcode.com/{year}/day/{day}/input"
    status, response = _cache_request(_aoc_get_request_with_oath, uri, verbose=True)
    if _check_if_status_ok(status):
        return response
    print(f"Aoc responded with code {status}")
    return 0


def post_day_answer(
    answer, level="1", day=_get_diff_date(DATE1, DATE2), year=DATE2.year
):
    """Post day answer to aoc"""
    uri = f"https://adventofcode.com/{year}/day/{day}/answer"
    response = _aoc_post_request_with_oath(uri, f"level={level}&answer={answer}")[1]
    print(response)
    if WRONG_ANSWER in response or TOO_MANY_ANSWERS in response:
        return False
    return True
