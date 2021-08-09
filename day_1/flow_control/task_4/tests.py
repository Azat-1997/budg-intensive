import unittest
from datetime import (
    date,
)

from day_1.flow_control.task_4.implementation import (
    get_next_date,
)


class MyTestCase(unittest.TestCase):
    def test_next_day(self):
        self.assertEqual(get_next_date("2021-03-03"), "2021-03-04")

    def test_next_month(self):
        self.assertEqual(get_next_date("2021-04-30"),  "2021-05-01")

    def test_next_year(self):
        self.assertEqual(get_next_date("2021-12-31"), "2022-01-01")

    def test_next_extra_february(self):
        self.assertEqual(get_next_date("2020-02-28"), "2020-02-29")


if __name__ == '__main__':
    unittest.main()
