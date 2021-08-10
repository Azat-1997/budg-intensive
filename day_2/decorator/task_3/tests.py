import unittest
from sys import path
path.append("/home/azat/BARS_GROUP/HW/budg-intensive/day_2")

from implementation import (
    counter
)

from common import (

some_func

)

class MyTestCase(unittest.TestCase):

    def test_on_number_calling_times(self):
        new_some_func = counter(some_func)
        new_some_func()
        new_some_func()
        new_some_func()
        new_some_func()
        self.assertEqual(new_some_func(), 5)


if __name__ == '__main__':
    unittest.main()
