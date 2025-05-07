import unittest
from src.task_07 import combine_anagrams


class TestAnagrams(unittest.TestCase):
    def test(self):
        right_answer = [
            ["cars", "racs", "scar"],
            ["for"],
            ["potatoes"],
            ["four"],
            ["creams", "scream"],
        ]

        self.assertEqual(
            combine_anagrams(
                ["cars", "for", "potatoes", "racs",
                    "four", "scar", "creams", "scream"]
            ),
            right_answer,
        )


if __name__ == "__main__":
    unittest.main()
