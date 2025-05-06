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


def cached(max_size: int | None = None, seconds: int | None = None):
    # Валидация параметров max_size и seconds
    if not isinstance(max_size, int):
        max_size = None
    if not isinstance(seconds, int):
        seconds = None

    def actual_decorator(func):
        cache = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Генерация уникального ключа на основе аргументов
            key = (args, tuple(sorted(kwargs.items())))

            # Проверка истекшего времени устаревания
            current_time = time.time()
            for k in list(cache.keys()):
                _, timestamp = cache[k]
                if seconds is not None and current_time - timestamp > seconds:
                    del cache[k]

            # Проверка наличия ключа в кэше
            if key in cache:
                return cache[key][0]

            # Вычисление результата
            result = func(*args, **kwargs)

            # Ограничение размера кэша
            if max_size is not None and len(cache) >= max_size:
                # Удаление самого старого элемента
                cache.popitem(last=False)

            cache[key] = (result, current_time)

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
# Забиваем буффер
# len(buff) == 1
print(slow_function(1))  # len(buff) == 2
print(slow_function(3))  # len(buff) == 3
print(slow_function(4))  # len(buff) == 3 (стёрся кэш для 2)
print(slow_function(3))  # len(buff) == 3 (кэш для 3 остался)

# len(buff) == 3 (стёрся кэш для 1, снова добавился для 2)
print(slow_function(2))

# Через 15 секунд кэш устареет, и будет новое вычисление
time.sleep(15)
print(slow_function(2))  # Вывод: "Вычисляю для 2..." → 4
