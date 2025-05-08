# Анаграмма — литературный приём, состоящий в перестановке букв или звуков
# определённого слова (или словосочетания), что в результате даёт другое слово
# или словосочетание.
# Разработайте метод combine_anagrams(words_array), который принимает на вход
# массив слов и разбивает их в группы по анаграммам, регистр букв не имеет
# значения при определении анаграмм.

from collections import defaultdict


def combine_anagrams(words_array: list[str]) -> list[list[str]]:
    anagram_groups = defaultdict(list)
    for word in words_array:
        key = ''.join(sorted(word.lower()))
        anagram_groups[key].append(word)
    return list(anagram_groups.values())
