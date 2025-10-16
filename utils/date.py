from datetime import datetime, timedelta
from dateutil.parser import parse


def parse_date(date_str: str) -> datetime:
    """
    Parses a date string into a datetime object.

    :param date_str: A string representing a date.
    :return: A datetime object.
    """
    return parse(date_str)


def add_days(date: str, days: int) -> datetime:
    """
    Adds a specified number of days to a date.

    :param date: A datetime object.
    :param days: An integer representing the number of days to add.
    :return: A new datetime object with the added days.
    """
    return date + timedelta(days=days)


def format_date(date: datetime, format_str: str = "%Y-%m-%d") -> str:
    """
    Formats a datetime object into a string.

    :param date: A datetime object.
    :param format_str: A string representing the desired date format.
    :return: A formatted date string.
    """
    return date.strftime(format_str)
