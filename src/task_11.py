import unittest

# Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
# принимающим на вход name и calories (не обязательные параметры), а также двумя
# методами is_healthy (возвращает true при условии калорийности десерта менее
# 200) и is_delicious (возвращает true для всех десертов).


class Dessert:
    def __init__(self, name: str = "", calories: int = 0):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        if isinstance(new_value, str):
            self.__name = new_value
        else:
            raise TypeError("Name should be a str type")

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, new_value):
        if isinstance(new_value, int):
            self.__calories = max(0, new_value)
        else:
            raise TypeError("Calories should be an int type")

    def is_healthy(self) -> bool:
        return self.calories < 200

    def is_delicious(self) -> bool:
        return True


class TastyTest(unittest.TestCase):
    def test(self):
        # Default constructed
        unknow_dessert = Dessert()
        unknow_dessert.name = "Cockerel on a stick"
        self.assertEqual(unknow_dessert.name, "Cockerel on a stick")
        unknow_dessert.calories = 300
        self.assertEqual(unknow_dessert.calories, 300)
        self.assertFalse(unknow_dessert.is_healthy())
        unknow_dessert.calories = 200
        self.assertFalse(unknow_dessert.is_healthy())
        unknow_dessert.calories = 199
        self.assertTrue(unknow_dessert.is_healthy())

        # Cheesecake
        cheesecake = Dessert("Cheesecake", 321)
        self.assertEqual(cheesecake.name, "Cheesecake")
        self.assertEqual(cheesecake.calories, 321)
        self.assertFalse(cheesecake.is_healthy())

        # Anyway, both are delicious
        self.assertTrue(unknow_dessert.is_delicious()
                        and cheesecake.is_delicious())

        with self.assertRaises(TypeError):
            bad_dessert = Dessert(5, -5)

        with self.assertRaises(TypeError):
            bad_dessert = Dessert("abba", -5.0)

        bad_dessert = Dessert("Some new bad desert", -5)
        self.assertEqual(bad_dessert.name, "Some new bad desert")
        self.assertEqual(bad_dessert.calories, 0)


if __name__ == "__main__":
    unittest.main()
