from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")
from common import MyException

class ClassFather:
    registered_list = set()
    @classmethod
    def get_name(cls):
        if cls == ClassFather:
           raise MyException
        elif cls._name not in ClassFather.registered_list:
           raise MyException

        return cls._name

    @classmethod
    def register(cls):
        if cls == ClassFather:
           raise MyException

        ClassFather.registered_list.add(cls._name)

class User1(ClassFather):
    _name = 'Roma'


class User2(ClassFather):
    _name = 'Vasya'
