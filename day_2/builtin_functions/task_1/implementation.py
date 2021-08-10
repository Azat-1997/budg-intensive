from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")
from common import MyException

class Value:

    def __init__(self, value):
        self.val = value

    def __repr__(self):
        return self.val

    def __add__(self, other):
        if type(other) in {float, int}:
            result = self.val + other

        elif isinstance(other, Value):
            result = self.val + other.val
        else: 
            raise TypeError("second argument is not instance of int, float or Value")
        return result

    def __sub__(self, other):        
        if type(other) in {float, int}:
            result = self.val - other
        elif isinstance(other, Value):
            result = self.val - other.val
        else: 
            raise TypeError("second argument is not instance of int, float or Value")
        return result



    def __mul__(self, other):
        if type(other) in {float, int}:
            result = self.val * other
        elif isinstance(other, Value):
            result = self.val * other.val
        else:
            raise TypeError("second argument is not instance of int, float or Value")
        return result

       

    def __truediv__(self, other):
        if other == 0:
           raise MyException
        if type(other) in {float, int}:
            result = self.val / other
        elif isinstance(other, Value):
            result = self.val / other.val
        else:
            raise TypeError("second argument is not instance of int, float or Value")
        return result
