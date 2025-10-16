import re


def remove_all_spaces(text: str) -> str:
    """
    Remove all spaces from a string.

    :param text: The input string.
    :return: The string with all spaces removed.
    """
    return "".join(text.split())


def capitalize(text: str) -> str:
    """
    Capitalize the first letter of each word in a string.

    :param text: The input string.
    :return: The string with the first letter of each word capitalized.
    """
    return re.sub(r"(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), text)


def pluralize(count: int, singular: str, plural: str) -> str:
    """
    Return the singular or plural form of a word based on the count.

    :param count: The count of items.
    :param singular: The singular form of the word.
    :param plural: The plural form of the word.
    :return: The appropriate form of the word based on the count.
    """
    return singular if count == 1 else plural
