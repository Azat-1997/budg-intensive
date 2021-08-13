"""
Что будет выведено после выполнения кода? Почему?
"""
def print_msg(number):

    def printer():
        nonlocal number
        number=3
        print(number)

    printer()
    print(number)


print_msg(9)

# Внутри print_msg() вызывается printer()
# внутри printer() ссылаемся на number, который находится в области видимости print_msg
# далее меняем на 3 и печатаем number. На печати будет 3.
# после printer() идет стандартный print(). Так как значение number было перезаписано в printer(),
# то также будет выведена тройка на печать
# Итого:
# 3
# 3
