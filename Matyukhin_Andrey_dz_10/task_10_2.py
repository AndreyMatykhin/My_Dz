from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculation(self):
        pass


class Coat(Clothes):
    def __init__(self, name, v):
        super().__init__(name)
        self.v = v

    @property
    def calculation(self):
        return self.v / 6.5 + 0.5

    def __str__(self):
        return f'На пошив одного польто "{self.name}" нужно {round(self.calculation, 2)} м ткани'


class Suit(Clothes):
    def __init__(self, name, h):
        super().__init__(name)
        self.h = h

    @property
    def calculation(self):
        return self.h * 2 + 0.3

    def __str__(self):
        return f'На пошив одного костюма "{self.name}" нужно {round(self.calculation, 2)} м ткани'


coat_m1 = Coat("Модель 1", 52)
coat_m2 = Coat("Модель 2", 44)
suit_m1 = Suit("Сокинг", 1.76)
suit_m2 = Suit("Классический", 1.86)
print(coat_m1)
print(coat_m2)
print(suit_m1)
print(suit_m2)
print(f'{round(sum([coat_m2.calculation, coat_m2.calculation, suit_m2.calculation, suit_m1.calculation]), 2)}')
