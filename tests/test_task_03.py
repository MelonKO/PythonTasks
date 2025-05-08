import unittest
from src.task_03 import max_odd


class TestMaxOdd(unittest.TestCase):
    def test(self):
        self.assertEqual(max_odd([1, 2, 3, 4, 4]), 3)
        self.assertEqual(max_odd([21.0, 2, 3, 4, 4]), 21)
        self.assertEqual(max_odd(["ololo", 2, 3, 4, [1, 2], None]), 3)
        self.assertEqual(max_odd(["ololo", "fufufu"]), None)
        self.assertEqual(max_odd([2, 2, 4]), None)


if __name__ == "__main__":
    unittest.main()
