import datetime


def is_datetime_validate(date_text):
    try:
        datetime.datetime.strptime(date_text, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def without_index(lst, index):
    return lst[:index] + lst[index + 1 :]
