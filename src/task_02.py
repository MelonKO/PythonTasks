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
