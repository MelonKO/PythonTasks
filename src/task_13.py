# Напишите декоратор @cached, который кэширует результаты функции, чтобы
# избежать повторных вычислений для одних и тех же аргументов. Декоратор
# должен поддерживать:
#    • ограничение размера кэша: при превышении максимально хранимого
#    количества записей (max_size) удаляются самые старые записи:
#    • если max_size=None, то размер кэша не ограничен
#    • если max_size не соответствует целому числу, то также
#    инициализировать его как None
#
#    • время жизни записей: автоматически удалять результаты, сохранённые
#    более seconds назад:
#    • если seconds=None, то записи не устаревают
#    • размер кэша не ограничен, если seconds не соответствует целому
#    числу, то также инициализировать его как None
#
#    • декоратор должен учитывать как позиционные (*args), так и
#    именованные аргументы (**kwargs)

from functools import wraps
import time
from collections import OrderedDict
from typing import Any


class TimedCache:
    def __init__(self, max_size: int | None, seconds: int | None):
        if not isinstance(max_size, int):
            self._max_size = None
        else:
            self._max_size = max_size

        if not isinstance(seconds, int):
            self._seconds = None
        else:
            self._seconds = seconds

        self._cache = OrderedDict()

    @staticmethod
    def make_key(*args, **kwargs) -> tuple:
        # Генерация уникального ключа на основе аргументов
        key = (args, tuple(sorted(kwargs.items())))
        return key

    def check_cache(self, key: tuple) -> Any | None:
        # Проверка истекшего времени устаревания
        current_time = time.time()
        for k in list(self._cache.keys()):
            _, timestamp = self._cache[k]
            if self._seconds is not None and (current_time - timestamp > self._seconds):
                del self._cache[k]

            # Проверка наличия ключа в кэше
            if key in self._cache:
                return self._cache[key][0]

    def add(self, key: tuple, value):
        # Ограничение размера кэша
        if self._max_size is not None and len(self._cache) >= self._max_size:
            # Удаление самого старого элемента
            self._cache.popitem(last=False)

        self._cache[key] = (value, time.time())


def cached(max_size: int | None = None, seconds: int | None = None):

    def actual_decorator(func):

        cache = TimedCache(max_size, seconds)

        @wraps(func)
        def wrapper(*args, **kwargs):
            cache_key = cache.make_key(*args, **kwargs)
            cached_result = cache.check_cache(cache_key)
            if cached_result != None:
                return cached_result

            result = func(*args, **kwargs)
            cache.add(cache_key, result)
            return result

        return wrapper
    return actual_decorator


@cached(max_size=3, seconds=10)
def slow_function(x):
    print(f"Вычисляю для {x}...")
    return x ** 2


# Первый вызов — вычисляется
print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4
# Повторный вызов с теми же аргументами — берётся из кэша
print(slow_function(2))  # Вывод: 4 (без вычисления)
# Через 15 секунд кэш устареет, и будет новое вычисление
time.sleep(15)
print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4
