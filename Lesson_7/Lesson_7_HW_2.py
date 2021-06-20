#Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
# этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Clothes(ABC):

    def __init__(self, x):
        self.x = x

    @property
    def all_leather(self):
        self.x = self.x / 6.5 + 0.5 + 2 * self.x + 0.3
        return self.x

    @abstractmethod
    def nothing(self):
        return 'None'

class Coat(Clothes):
    def all_leather(self):
        return self.x / 6.5 + 0.5

    def nothing(self):
        pass

class Costume(Clothes):
    def all_leather(self):
        return 2 * self.x + 0.3

    def nothing(self):
        pass

coat_new = Coat(50)
costume_new = Costume(5)
print(f'Для пошива пальто нужно: {coat_new.all_leather():.1f} метров ткани')
print(f'Для пошива пальто нужно: {costume_new.all_leather():.1f} метров ткани')
print(f'Cуммарный расход ткани на производство одежды: {costume_new.all_leather() + costume_new.all_leather():.1f} метров')





