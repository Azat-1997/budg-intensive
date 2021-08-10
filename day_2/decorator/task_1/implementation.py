import time

from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")
from common import factorial

def time_execution(function):
    """
    Обертка, печатающая время выполнения функции.
    """
    def wrapper(*args):
        start = time.time()
        result = function(*args)
        end = time.time()
        t = end - start 
        print("--- {:.03} sec. ---".format(t))
        return result

    return wrapper


if __name__ == "__main__":
    estimate_factorial = time_execution(factorial)
    print("factorial(n = 10):", end = " ")
    estimate_factorial(10)
    print("factorial(n = 100):", end = " ")
    estimate_factorial(100)
    print("factorial(n = 1000):", end = " ")
    estimate_factorial(1000)


