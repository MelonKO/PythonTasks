# Дан список целых чисел. Необходимо разработать метод sort_list(list), который
# поменяет местами все минимальные и максимальные элементы массива, а также
# добавит в конец массива одно минимальное значение из него.


def sort_list(lst: list):
    if not len(lst):
        return

    _min = _max = lst[0]
    for elem in lst:
        if elem > _max:
            _max = elem
        if elem < _min:
            _min = elem

    for i in range(len(lst)):
        if lst[i] == _max:
            lst[i] = _min
        elif lst[i] == _min:
            lst[i] = _max
    lst.append(_min)
