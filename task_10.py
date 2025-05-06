import unittest
from collections import defaultdict

# Разработайте функцию count_words(string), которая будет возвращать словарь со
# статистикой частоты употребления входящих в неё слов.


def count_words(string: str) -> dict:
    word_counts = defaultdict(int)
    string = "".join(char.lower()
                     for char in str(string) if char.isalnum() or char.isspace())
    for word in string.split():
        word_counts[word] += 1
    return word_counts


class TestCounting(unittest.TestCase):
    def test(self):
        self.assertEqual(count_words("A man, a plan, a canal -- Panama"),
                         {"a": 3, "man": 1, "canal": 1, "panama": 1, "plan": 1})

        self.assertEqual(count_words("Doo bee doo bee doo"),
                         {"doo": 3, "bee": 2})
        self.assertEqual(count_words(""), {})
        self.assertEqual(count_words("Hello, world! 123"), {
                         "hello": 1, "world": 1, "123": 1})


if __name__ == "__main__":
    unittest.main()
