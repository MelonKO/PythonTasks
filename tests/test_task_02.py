import unittest
from src.task_02 import coincidence


class TestCoincidence(unittest.TestCase):
    def test(self):
        self.assertEqual(coincidence([1, 2, 3, 4, 5], range(3, 6)), [3, 4, 5])
        self.assertEqual(coincidence(), [])
        self.assertEqual(
            coincidence([None, 1, "foo", 4, 2, 2.5], range(1, 4)), [1, 2, 2.5]
        )
        self.assertEqual(coincidence([], range(1, 4)), [])
        self.assertEqual(coincidence(rng=range(1, 4)), [])
        self.assertEqual(coincidence([1, 2, 3, 4, 5]), [])


if __name__ == "__main__":
    unittest.main()
