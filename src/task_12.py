# Создайте класс JellyBean, расширяющий класс Dessert (из Упражнения 11) новым
# геттером и сеттером для атрибута flavor (все параметры являются не
# обязательными). Измените метод is_delicious таким образом, чтобы он возвращал
# false только в тех случаях, когда flavor равняется «black licorice».

from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name: str = "", calories: int = 0, flavor: str = ""):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, new_value: str):
        if isinstance(new_value, str):
            self.__flavor = new_value
        else:
            raise TypeError("Flavor should be a str type")

    def is_delicious(self) -> bool:
        return not (self.flavor == "black licorice")
