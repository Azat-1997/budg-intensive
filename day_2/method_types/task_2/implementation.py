from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")
from common import MyException

class ClassFather:
    registered_list = set()
    @staticmethod
    def get_name():
        raise MyException

    @classmethod
    def register(cls):
        raise MyException


class User1(ClassFather):
    _name = ''

    @classmethod
    def register(cls):
       cls._name = "User1"
       ClassFather.registered_list.add(cls._name)

    @classmethod
    def get_name(cls):
       if cls._name in ClassFather.registered_list:
          return cls._name
       else:
          raise MyException

       return cls._name


class User2(ClassFather):
    _name = ''

    @classmethod
    def register(cls):
       cls._name = "User2"
       ClassFather.registered_list.add(cls._name)

    @classmethod
    def get_name(cls):
       if cls._name in ClassFather.registered_list:
           return cls._name
       else:
           raise MyException
