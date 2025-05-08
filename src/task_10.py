# Разработайте функцию count_words(string), которая будет возвращать словарь со
# статистикой частоты употребления входящих в неё слов.

from collections import defaultdict


def count_words(string: str) -> dict:
    word_counts = defaultdict(int)
    string = "".join(char.lower()
                     for char in str(string) if char.isalnum() or char.isspace())
    for word in string.split():
        word_counts[word] += 1
    return word_counts
