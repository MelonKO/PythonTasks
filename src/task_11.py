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
