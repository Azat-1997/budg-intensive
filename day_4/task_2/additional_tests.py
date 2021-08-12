import unittest
from sys import path
path.append("/home/azat/BARS_GROUP/budg-intensive")

from day_4.magic_method.task_2.implementation import (
    MathClock
)


class MyTestCase(unittest.TestCase):
    def test_on_zero_time(self):
        time_obj = MathClock()
        self.assertEqual(time_obj.get_time(), '00:00')

    def test_on_sub_minutes(self):
        time_obj = MathClock(0, 10)
        time_obj - 9
        self.assertEqual(time_obj.get_time(), '00:01')
        time_obj - 2
        self.assertEqual(time_obj.get_time(), '23:59')
        time_obj - 70
        self.assertEqual(time_obj.get_time(), '22:49')

    def test_on_sub_hours(self):
        time_obj = MathClock(10, 0)
        time_obj / 9
        self.assertEqual(time_obj.get_time(), '01:00')
        time_obj / 2
        self.assertEqual(time_obj.get_time(), '23:00')
        time_obj / 49
        self.assertEqual(time_obj.get_time(), '22:00')

    def test_on_hours_and_minutes(self):
        time_obj = MathClock()
        time_obj / 1
        time_obj - 61
        self.assertEqual(time_obj.get_time(), '21:59')


if __name__ == '__main__':
    unittest.main()
