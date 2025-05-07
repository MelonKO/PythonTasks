import unittest
from src.task_14 import EvenNumbers


class TestEvenNumbers(unittest.TestCase):
    def test(self):
        self.assertEqual(list(EvenNumbers(5)), [0, 2, 4, 6, 8])
        self.assertEqual(list(EvenNumbers(1)), [0])
        self.assertEqual(list(EvenNumbers(0)), [])
        self.assertEqual(list(EvenNumbers(-1)), [])


if __name__ == "__main__":
    unittest.main()
