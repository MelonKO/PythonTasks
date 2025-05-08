import unittest

from src.task_12 import JellyBean


class TastyTestPlus(unittest.TestCase):
    def test(self):
        # JellyBean (not delicious)
        jb = JellyBean("JellyBean", 15, "black licorice")
        self.assertFalse(jb.is_delicious())

        # JellyBean (delicious)
        jb = JellyBean("JellyBean", 15, "not a black licorice")
        self.assertTrue(jb.is_delicious())


if __name__ == "__main__":
    unittest.main()
