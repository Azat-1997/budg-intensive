from math import sqrt

def great_comprehension(list1, list2, list3):
    """
    Возвращает список с перемноженными элементами списков list1, list2 и list3 согласно условию
    """
    # x % 10 - берем последнюю цифру. Отсев в условии гарантирует совпадение с первой цифрой
    return [2 * (x % 10) * int(sqrt(y)) * z for x in list1 for y in list2 for z in list3
            if (x > 9 and str(x)[0] == str(x)[-1]) and
            (y < 1000 and y > 99 and y % 2 == 0) and
            (z % 2 == 1 or z == 4)]


list1 = [12, 2, 17, 44, 131]
list2 = [127, 69, 144, 0, 1024]
list3 = [8, 6, 5, 4, 7]

