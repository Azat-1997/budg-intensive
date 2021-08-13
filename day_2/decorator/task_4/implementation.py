from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")
from time import sleep
from common import MyException

def decorator_maker(times, delay):
    """
    Обертка, которая повторяет вызов функции times раз с паузой delay секунд
    Args:
        times: количество повторений
        delay: задержка (с)

    Returns:
        валидное значение (при вызове bool() -> True)
    """
    def repeat(function):
        
        
        def wrapper(*args):
            for i in range(times):
                try:
                    result = function(*args)
                    break
                except AssertionError:
                    sleep(delay)
            else:
                raise MyException

            return result

        return wrapper

    return repeat
