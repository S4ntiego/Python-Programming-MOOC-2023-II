# Write your solution here
import re


def is_dotw(my_string: str):
    day_of_the_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    for day in day_of_the_week:
        if re.search(day, my_string):
            return True
    return False


def all_vowels(my_string: str):
    for char in my_string:
        if re.search("[aeiouAEIOU]", char):
            continue
        else:
            return False
    return True


def time_of_day(my_string: str):
    if re.search("^([0-1][0-9]|[2][0-4]):[0-5][0-9]:[0-5][0-9]$", my_string):
        return True
    else:
        return False
