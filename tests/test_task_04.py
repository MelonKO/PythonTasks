import unittest
from src.task_04 import sort_list


class TestSortList(unittest.TestCase):
    def test(self):
        empty = []
        sort_list(empty)
        self.assertEqual(empty, [])

        tstList = [2, 4, 6, 8]
        sort_list(tstList)

        self.assertEqual(tstList, [8, 4, 6, 2, 2])

        tstList = [1]
        sort_list(tstList)
        self.assertEqual(tstList, [1, 1])

        tstList = [1, 2, 1, 3]
        sort_list(tstList)
        self.assertEqual(tstList, [3, 2, 3, 1, 1])


if __name__ == "__main__":
    unittest.main()
