import unittest
from src.task_10 import count_words


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
