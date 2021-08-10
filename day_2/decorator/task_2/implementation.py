from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")

from common import ( 
  MyException
)


def check_value(function):
    """
    Обертка, проверяющая валидность переданного значения(неотрицательный int).
    В случае валидного значения - передает дальше в функцию,
    в противном случае - выбрасывает исключение MyException.
    """
    def wrapper(arg):

        if type(arg) is int and arg >= 0:

            result = function(arg)

        else:
            
            raise MyException


        return result

    return wrapper


def cache_values(functions):
   cache = {}

   def wrapper(*args):
       if args in cache:
           result = cache[args]
       else: 
           result = function(*args)

       return result

   return wrapper 


