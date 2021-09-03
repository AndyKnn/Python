# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на практике работу
# декоратора @property.

from abc import abstractmethod


class Clothes:
    def __init__(self, v=None, h=None):
        self.v = v
        self.h = h

    @abstractmethod
    def get_square(self, v=None, h=None):
        return str(f'Площадь общей ткани: {round((self.v / 6.5 + 0.5) + (self.h * 2 + 0.3), 2)}')


class Coat(Clothes):
    def __init__(self, v):
        super(Coat, self).__init__(v)

    @property
    def get_square(self, v=None, h=None):
        return f'Расход ткани на пальто: {round(self.v / 6.5 + 0.5, 2)}'


class Suit(Clothes):
    def __init__(self, h):
        super(Suit, self).__init__(h)
        self.h = h

    @property
    def get_square(self, v=None, h=None):
        return f'Расход ткани на костюм: {round(self.h * 2 + 0.3, 2)}'


c = Coat(12)

print(c.get_square)     # Проверяем работу декоратора @property

s = Suit(10)

print(s.get_square)     # Проверяем работу декоратора @property

clothes = Clothes(12, 10)       # Размер пальто = 12, рост костюма = 10
print(clothes.get_square())     # Расчета суммарного расхода ткани на производство одежды
