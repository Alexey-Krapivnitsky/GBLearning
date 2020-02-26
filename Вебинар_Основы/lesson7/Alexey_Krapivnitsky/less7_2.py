from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, name=None):
        self.name = name

    @abstractmethod
    def __add__(self, other):
        pass


class Coat(Clothes):

    def __init__(self, name=None, param=0):
        super().__init__(name)
        self.consumption = param

    def __add__(self, other):
        total_consumption = self.consumption + other.consumption
        result = Coat()
        result.consumption = total_consumption
        return result

    def __str__(self):
        return f'{self.consumption}'

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, param):
        if not self.name:
            self.__consumption = param
        else:
            self.__consumption = round(param / 6.5 + 0.5, 2)


class Suit(Clothes):

    def __init__(self, name=None, param=0):
        super().__init__(name)
        self.consumption = param

    def __add__(self, other):
        total_consumption = self.consumption + other.consumption
        result = Suit()
        result.consumption = total_consumption
        return result

    def __str__(self):
        return f'{self.consumption}'

    @property
    def consumption(self):
        return self.__consumption

    @consumption.setter
    def consumption(self, param):
        if not self.name:
            self.__consumption = param
        else:
            self.__consumption = round(2 * param + 0.3, 2)


if __name__ == '__main__':

    coat_1 = Coat('Плащ', 48)
    coat_2 = Coat('Шуба', 52)
    suit_1 = Suit('Тройка', 170)
    suit_2 = Suit('Фрак', 185)

    my_consum = coat_1 + coat_2 + suit_1 + suit_2

    my_total_consum = coat_1.consumption + coat_2.consumption + suit_2.consumption + suit_1.consumption

    print(my_consum)
    print(my_total_consum)
