import unittest

# Дан список элементов произвольной природы. Необходимо разработать метод
# max_odd(array), который определит максимальный нечетный элемент
# (21.000 = 21 и тоже считается нечетным элементом).
# Вернуть None, если таких элементов нет в переданном массиве.


def max_odd(lst: list) -> int | float | None:
    filtered = []
    for x in lst or []:
        if isinstance(x, int):
            if x % 2 != 0:
                filtered.append(x)
        elif isinstance(x, float):
            if x.is_integer() and int(x) % 2 != 0:
                filtered.append(int(x))
    return max(filtered, default=None)


class TestMaxOdd(unittest.TestCase):
    def test(self):
        self.assertEqual(max_odd([1, 2, 3, 4, 4]), 3)
        self.assertEqual(max_odd([21.0, 2, 3, 4, 4]), 21)
        self.assertEqual(max_odd(["ololo", 2, 3, 4, [1, 2], None]), 3)
        self.assertEqual(max_odd(["ololo", "fufufu"]), None)
        self.assertEqual(max_odd([2, 2, 4]), None)


if __name__ == "__main__":
    unittest.main()
