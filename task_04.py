import unittest

# Дан список целых чисел. Необходимо разработать метод sort_list(list), который
# поменяет местами все минимальные и максимальные элементы массива, а также
# добавит в конец массива одно минимальное значение из него.


def sort_list(lst: list):
    if not len(lst):
        return

    _min = min(lst)
    _max = max(lst)

    # _min = lst[0]
    # _max = lst[0]
    # for elem in lst:
    #     if elem > _max:
    #         _max = elem
    #     if elem < _min:
    #         _min = elem

    for i in range(len(lst)):
        if lst[i] == _max:
            lst[i] = _min
        elif lst[i] == _min:
            lst[i] = _max
    lst.append(_min)


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
