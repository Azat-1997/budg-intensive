import unittest
from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")

from implementation import (
    decorator_maker,
)
from common import (
    MyException,
    specific_func
)


class MyTestCase(unittest.TestCase):
    def test_on_getting_right_value(self):
        new_factorial = decorator_maker(3, 0)(specific_func)
        self.assertEqual(new_factorial(), 1)

    def test_on_getting_incorrect_Value(self):
        new_factorial = decorator_maker(4, 0)(specific_func)
        self.assertEqual(new_factorial(), 1)

    def test_on_no_getting_value(self):
        new_factorial = decorator_maker(2, 0)(specific_func)
        self.assertRaises(MyException, new_factorial)


if __name__ == '__main__':
    unittest.main()
