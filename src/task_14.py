import unittest


# Реализуйте класс EvenNumbers, который в конструкторе принимает целое число n
# — количество чётных чисел для генерации.
# Итератор должен выдавать числа по порядку, начиная с 0: 0, 2, 4, ..., 2*(n-1).


class EvenNumbers:

    def __init__(self, num: int) -> None:
        self.__num = num

    def __iter__(self):
        self.__count = 0
        return self

    def __next__(self):
        if self.__count < self.__num:
            res = 2 * self.__count
            self.__count += 1
            return res
        else:
            raise StopIteration


if __name__ == "__main__":
    unittest.main()
