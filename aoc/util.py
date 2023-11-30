"""Basic utility for the project"""


def get_diff_date(date1, date2):
    """Get number of days between two dates"""
    return (date2-date1).days+1
