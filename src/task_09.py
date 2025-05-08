import unittest

# Необходимо разработать метод connect_dicts(dict1, dict2), который соединит два
# переданных словаря, значениями ключей в которых являются числа, и вернет
# новый словарь, полученный по следующим правилам:
#     • приоритетными являются ключи того словаря, сумма значений ключей
#     которого больше (если суммы значений ключей будут равны, то второй
#     словарь считается более приоритетным)
#     • ключи со значениями меньше 10 не должны попасть в финальный
#     словарь
#     • получившийся словарь должен вернуться упорядоченным по значениям
#     ключей в порядке возрастания.


def connect_dicts(dict1: dict, dict2: dict) -> dict:
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())
    result = {}
    all_keys = set(dict1) | set(dict2)

    for key in all_keys:
        if (key in dict1) and (key in dict2):
            value = dict1[key] if sum1 > sum2 else dict2[key]
        elif key in dict1:
            value = dict1[key]
        else:
            value = dict2[key]

        if value >= 10:
            result[key] = value

    return dict(sorted(result.items(), key=lambda x: x[1]))


class TestConnect(unittest.TestCase):
    def test(self):
        self.assertEqual(
            connect_dicts({"a": 2, "b": 12}, {"c": 11, "e": 5}),
            {'c': 11, 'b': 12})

        self.assertEqual(
            connect_dicts({"a": 13, "b": 9, "d": 11}, {"c": 12, "a": 15}),
            {'d': 11, 'c': 12, 'a': 13})

        self.assertEqual(
            connect_dicts({"a": 14, "b": 12}, {"c": 11, "a": 15}),
            {'c': 11, 'b': 12, 'a': 15})


if __name__ == "__main__":
    unittest.main()
