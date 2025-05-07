import unittest
from src.task_05 import date_in_future


class DatTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print()
        print("="*4, "TASK 05", "="*4)
        return super().setUpClass()

    def test(self):
        print(date_in_future(-1))
        print(date_in_future(None))
        print(date_in_future(1))


if __name__ == "__main__":
    unittest.main()
