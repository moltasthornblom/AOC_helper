"""Interact with AOC website"""
from decouple import config
import requests


def _aoc_get_request_with_oath(uri):
    """Perform get request to AOC with Session cookie"""
    response = requests.get(uri, cookies={"session": config("AOC_SESSION")}, timeout=10)
    return response.status_code, response.text


def _aoc_post_request_with_oath(uri, data):
    """Perform post request to AOC with Session cookie"""
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(
        uri,
        headers=headers,
        cookies={"session": config("AOC_SESSION")},
        data=data,
        timeout=10,
    )
    return response.status_code, response.text
