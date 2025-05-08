import unittest
from src.task_15 import BlockTranspositionCipher, BadKeyError


class TestTransposition(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print()
        return super().setUpClass()

    def test_invalid_key(self):
        with self.assertRaises(BadKeyError):
            cipher = BlockTranspositionCipher("helloworld", "авб")

    def test1(self):
        cipher = BlockTranspositionCipher("helloworld", "acb")
        self.assertEqual(list(cipher), ["hle", "lwo", "olr", "d  "])

    def test2(self):
        cipher = BlockTranspositionCipher("hlelwoolrd  ", "acb", decrypt=True)
        self.assertEqual("".join(cipher), "helloworld")

    @unittest.skipIf(True, "Skipped to keep stdout clean.")
    def test_with_print(self):
        print("="*4, "TASK 15", "="*4)
        # Пример 1: Шифрование с явной итерацией по блокам
        text = "HELLOWORLD"
        key = "bAc"
        print("Процесс шифрования по блокам:")
        cipher = BlockTranspositionCipher(text, key)
        for i, encrypted_block in enumerate(cipher, 1):
            print(f"Блок {i}: '{encrypted_block}'")

        # Пример 2: Полное шифрование
        cipher = BlockTranspositionCipher(text, key)
        encrypted = ''.join(cipher)
        print(f"\nПолный зашифрованный текст: '{encrypted}'")

        # Пример 3: Дешифрование с итерацией
        print("\nПроцесс дешифрования по блокам:")
        decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
        for i, decrypted_block in enumerate(decipher, 1):
            print(f"Блок {i}: '{decrypted_block}'")

        # Пример 4: Полное дешифрование с обрезкой пробелов
        decipher = BlockTranspositionCipher(encrypted, key, decrypt=True)
        decrypted = ''.join(decipher)
        print(f"\nПолный расшифрованный текст: '{decrypted}'")


if __name__ == "__main__":
    unittest.main()
