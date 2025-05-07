import unittest
from src.task_01 import is_palindrome


class TestPalindrome(unittest.TestCase):
    def runTest(self):
        self.assertEqual(is_palindrome(
            "A man, a plan, a canal -- Panama"), True)
        self.assertEqual(is_palindrome("Madam, I'm Adam!"), True)
        self.assertEqual(is_palindrome(333), True)
        self.assertEqual(is_palindrome(None), False)
        self.assertEqual(is_palindrome("Abracadabra"), False)
        self.assertEqual(is_palindrome(""), True)
        self.assertEqual(is_palindrome("a"), True)
        self.assertEqual(is_palindrome("abba"), True)
        self.assertEqual(is_palindrome("abcba"), True)


if __name__ == "__main__":
    unittest.main()
