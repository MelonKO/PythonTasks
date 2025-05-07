import unittest
from src.task_08 import multiply_numbers


class TestMultiply(unittest.TestCase):
    def test(self):
        self.assertEqual(multiply_numbers(), None)
        self.assertEqual(multiply_numbers("ss"), None)
        self.assertEqual(multiply_numbers("1234"), 24)
        self.assertEqual(multiply_numbers("sssdd34"), 12)
        self.assertEqual(multiply_numbers(2.3), 6)
        self.assertEqual(multiply_numbers([5, 6, 4]), 120)
        self.assertEqual(multiply_numbers((5, 6, 4)), 120)


if __name__ == "__main__":
    unittest.main()
