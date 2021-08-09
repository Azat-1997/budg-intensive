def is_leap_year(year:int) -> bool:
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0


def get_next_date(some_date):
    """Возвращает следующую дату для заданной

    Args:
        some_date: определенная исходная дата

    Returns: следующая дата
    """
    # последние дни в месяцах: 1 - январь, февраль и.т.д 
    last_days = [None, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    year, month, day = map(int, some_date.split("-"))

    # Бросаем исключение на невалидные даты
    if month > 12 or day > last_days[month]:
       raise ValueError("Out of months or days")

    # Проверяем случай, когда последний день февраля
    # Если 28 и год не високосный - переходим на первое марта
    if month == 2 and day == 28 and not is_leap_year(year):
       day = 1
       month += 1
       
    else:
       # Если натыкаемся на последний день в году
       if month == 12 and day == last_days[month]:
          year += 1
          month = 1
          day = 1
       # Если натыкаемся на последний день в месяце
       elif day == last_days[month]:
          month += 1
          day = 1    
       else:
          day += 1


    return "{0}-{1:02}-{2:02}".format(year, month, day)

#    raise NotImplementedError


