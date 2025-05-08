# Дан список элементов произвольной природы. Необходимо разработать метод
# max_odd(array), который определит максимальный нечетный элемент
# (21.000 = 21 и тоже считается нечетным элементом).
# Вернуть None, если таких элементов нет в переданном массиве.
from typing import List, Union


def max_odd(lst: List) -> Union[int, float, None]:
    filtered = []
    for x in lst or []:
        if isinstance(x, int):
            if x % 2 != 0:
                filtered.append(x)
        elif isinstance(x, float):
            if x.is_integer() and int(x) % 2 != 0:
                filtered.append(int(x))
    return max(filtered, default=None)
