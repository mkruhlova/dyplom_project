from datetime import datetime

from config import datetime_format


def is_datetime_validate(date_text):
    try:
        datetime.strptime(date_text, datetime_format)
        return True
    except ValueError:
        return False


def get_current_datetime():
    return datetime.today().strftime(datetime_format)


def without_index(lst, index):
    return lst[:index] + lst[index + 1:]
