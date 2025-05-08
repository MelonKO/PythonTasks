import unittest

# Дан список list и числовой диапазон range. Разработайте метод coincidence(list,range)
# для определения элементов из массива list, значения которого входят в
# указанный диапазон range. Если не передан хотя бы один из параметров, то
# должен вернуться пустой массив.


def coincidence(lst: list | None = None, rng: range | None = None) -> list[int | float]:
    if lst is None or rng is None:
        return []
    return [
        x for x in lst if (isinstance(x, (int, float))) and (rng.start <= x < rng.stop)
    ]


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
