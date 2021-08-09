from datetime import date, timedelta
def leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """

    last_days = [None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    further_date = some_date

    if some_date.day == 28 and some_date.month == 2 and not leap_year(some_date.year):
        further_date = date(some_date.year, some_date.month, some_date.day + 1)

    elif some_date.day == last_days[some_date.month] and some_date.month == 12:
        further_date = date(some_date.year + 1, 1, 1)

    elif some_date.day == last_days[some_date.month]:
        further_date = date(some_date.year, some_date.month + 1, 1) 

    else:
        further_date = date(some_date.year, some_date.month, some_date.day + 1)

   
    return further_date
   
