from pickle import TRUE
from typing import Any
import unittest

# Разработайте метод is_palindrome(string), который будет определять, является ли
# параметр string палиндромом (строкой, которая читается одинаково как сначала
# так и с конца), при условии игнорирования пробелов, знаков препинания и регистра.


def is_palindrome(string) -> bool:
    processed = ''.join(char.lower() for char in str(string) if char.isalnum())
    if not len(processed):
        return True
    i = 0
    j = len(processed)-1
    while i < j:
        if processed[i] != processed[j]:
            return False
        i += 1
        j -= 1
    return True


class TestPalindrome(unittest.TestCase):
    def test(self):
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
