from abc import ABC, abstractmethod


class MyAbsClass(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Clothes(MyAbsClass):
    def __init__(self, name, length):
        self.name = name
        self.length = length

    @property
    def consumption(self):
        if self.name == 'пальто':
            con = self.length/6.5+0.5
        if self.name == 'костюм':
            con = self.length*2+0.3
        return con


my_clothes_1 = Clothes('пальто', 10)

print(my_clothes_1.consumption)

my_clothes_2 = Clothes('костюм', 10)

print(my_clothes_2.consumption)
