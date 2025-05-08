import unittest
from functools import reduce

# Написать метод multiply_numbers(inputs), который вернет произведение цифр,
# входящих в inputs.


def multiply_numbers(inputs=None):
    if not inputs is None:
        digits = list(filter(str.isdigit, str(inputs)))
        if len(digits):
            return reduce(lambda x, y: x * y, map(int, digits), 1)
    return None


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
