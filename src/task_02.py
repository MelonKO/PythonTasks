# Дан список list и числовой диапазон range. Разработайте метод coincidence(list,range)
# для определения элементов из массива list, значения которого входят в
# указанный диапазон range. Если не передан хотя бы один из параметров, то
# должен вернуться пустой массив.
from typing import List, Union

def coincidence(lst: Union[List, None] = None, rng: Union[range, None] = None) -> List[Union[int, float]]:
    if lst is None or rng is None:
        return []
    return [
        x for x in lst if (isinstance(x, (int, float))) and (rng.start <= x < rng.stop)
    ]
