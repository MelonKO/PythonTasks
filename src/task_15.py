# Реализовать класс BlockTranspositionCipher, который будет шифровать и
# расшифровывать текст методом блочной перестановки с помощью текстового
# ключа.

# Основная идея:
# 1. Ключ — строка, состоящая из уникальных английских букв. Пример:
# acb
# 2. Шифрование — алгоритм, который преобразует исходный текст в
# набор зашифрованных символов.
# 3. Дешифрование — алгоритм, который преобразует набор
# зашифрованных символов в исходный текст.

# Ключ и его обработка:
# • ключ состоит только из букв английского алфавита
# • символы в ключе должны быть уникальны (регистр букв не имеет
# значения — "A" и "a" считаются одинаковыми)
# • ключ преобразуется в числовой массив. Каждому символу
# присваивается его порядковый номер в алфавите (a = 0, b = 1, ..., z =
# 25)

# Правила шифрования:
# • исходный текст делится на блоки длины, равной длине ключа
# • если длина блока не кратна длине ключа, то оставшийся блок
# дополняется пробелами
# • в каждом из блоков символы переставляются согласно порядку из
# ключа

# Пример алгоритма шифрования:
# Ключ: "acb"
# Текст: "helloworld"
# Блоки: ["hel", "low", "orl", "d "]
# Блоки после перестановки: ["hle", "lwo", "olr", "d "]
# Результат: "hlelwoolrd "

# Правила дешифрования:
# • исходный порядок восстанавливает символы в каждом блоке
# • лишние пробелы после дешифровки удаляются

# Валидации и работа с ошибками:
# • проверяется, что ключ состоит только из букв английского алфавита
# • проверяется, что все буквы в ключе уникальны, игнорируя регистр
# • если ключ не соответствует требованиям, вызывается исключение
# ValueError с понятным сообщением об ошибке

from typing import OrderedDict


class BadKeyError(Exception):

    def __init__(self, message: str = "Invalid key"):
        self.message = message
        super().__init__(self.message)


class BlockTranspositionCipher_Iter:

    def __init__(self, text: list[str], key: list[int], decrypt: bool) -> None:
        self._blocked_text = text
        self._key = key if not decrypt else self.inverse_key(key)
        self._index = 0
        self._decrypt = decrypt

    def __iter__(self):
        return self

    def __next__(self):
        if (self._index < len(self._blocked_text)):
            self._blocked_text[self._index]
            block = ""
            for i in range(len(self._key)):
                block += self._blocked_text[self._index][self._key[i]]
            self._index += 1
            return block if not self._decrypt else block.strip()
        else:
            raise StopIteration

    @staticmethod
    def inverse_key(key):
        inverse_key = [0] * len(key)
        for i, pos in enumerate(key):
            inverse_key[pos] = i
        return inverse_key


class BlockTranspositionCipher:

    __alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                  'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, text: str, key: str, decrypt: bool = False) -> None:
        #  Convert key to int array
        self.validate_key(key)
        self.__key = self.__make_key(key.lower())

        # Split text to blocks
        self.__blocked_text = self.__make_blocks(text, self.key)

        self.__decrypt = decrypt

    @property
    def key(self):
        return self.__key

    @property
    def decrypt(self):
        return self.__decrypt

    @property
    def blocked_text(self):
        return self.__blocked_text

    @staticmethod
    def __make_blocks(text: str, key: list[int]) -> list[str]:
        block_size = len(key)
        blocks = []
        for i in range(0, len(text), block_size):
            block = text[i:i + block_size]
            if len(block) < block_size:
                block += ' ' * (block_size - len(block))
            blocks.append(block)
        return blocks

    @staticmethod
    def __make_key(key):
        key_adjustment = OrderedDict()
        key_count = 0
        for ch in sorted(key):
            key_adjustment[ch] = key_count
            key_count += 1
        del key_count

        converted_key: list[int] = []
        for ch in key:
            converted_key.append(key_adjustment[ch])
        del key_adjustment
        return converted_key

    def __iter__(self):
        return BlockTranspositionCipher_Iter(
            self.blocked_text, self.key, self.decrypt)

    @staticmethod
    def validate_key(key: str):

        # Check if a key is string
        if not isinstance(key, (str)):
            raise BadKeyError("Key is not a string")

        key = key.lower()

        # Check that key contains only unique chars
        if len(key) != len(set(key)):
            raise BadKeyError(
                "Key contains duplicated chars. Each character in the key should be unique.")

        if not all((char in BlockTranspositionCipher.__alphabet) for char in key):
            raise BadKeyError(
                "Key contains invalid characters (not from English alphabet).")
