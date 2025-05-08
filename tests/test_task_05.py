import datetime
import unittest
from unittest.mock import patch
from src.task_05 import date_in_future, format_date_time


class DateTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Устанавливаем фиктивное текущее время
        cls.fixed_time = datetime.datetime(2001, 3, 24, 22, 33, 44)
        cls.fixed_time_str = format_date_time(cls.fixed_time)
        # Подменяем datetime.now()
        cls.patcher = patch('src.task_05.datetime')
        cls.mock_datetime = cls.patcher.start()
        cls.mock_datetime.now.return_value = cls.fixed_time

    @classmethod
    def tearDownClass(cls):
        # Восстанавливаем оригинальный datetime.datetime
        cls.patcher.stop()

    def test_print_format(self):
        # 24-03-2001 22:33:44
        self.assertEqual(format_date_time(
            datetime.datetime(2001, 3, 24, 22, 33, 44)), "24-03-2001 22:33:44")

    def test_non_integer_day(self):
        self.assertEqual(date_in_future(None), self.fixed_time_str)
        self.assertEqual(date_in_future([]), self.fixed_time_str)

    def test_zero_days(self):
        self.assertEqual(date_in_future(0), self.fixed_time_str)

    def test_yesterday(self):
        days_offset = 1
        result = date_in_future(days_offset)
        expected = format_date_time(
            self.fixed_time + datetime.timedelta(days=days_offset))
        self.assertEqual(result, expected)

    def test_tomorrow(self):
        days_offset = -1
        result = date_in_future(days_offset)
        expected = format_date_time(
            self.fixed_time + datetime.timedelta(days=days_offset))
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
