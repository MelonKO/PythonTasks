# Написать метод multiply_numbers(inputs), который вернет произведение цифр,
# входящих в inputs.

from functools import reduce


def multiply_numbers(inputs=None):
    if not inputs is None:
        digits = list(filter(str.isdigit, str(inputs)))
        if len(digits):
            return reduce(lambda x, y: x * y, map(int, digits), 1)
    return None
