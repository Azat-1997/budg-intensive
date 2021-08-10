from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")
from common import MyException

class ClassFather:
    @staticmethod
    def get_name():
        raise MyException

    @staticmethod
    def register():
        raise MyException


class User1(ClassFather):
    _name = ''

    @staticmethod
    def register():
       _name = "User1"

    @staticmethod
    def get_name():
       if _name == '':
          raise MyException
       
       return _name


class User2(ClassFather):
    _name = ''

    @staticmethod
    def register():
       _name = "User2"

    @staticmethod
    def get_name():
       if _name == '':
          raise MyException

       return _name
