
from abc import ABCMeta,abstractmethod

class Animal():
    def hungry(self):
        print(f'I want to eat {self.my_favorate_food()}')

    #@abstractmethod
    def my_favotate_food(self):
        return 'No Favorate Food'


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def my_favorate_food(self):
        return 'ribs'

class Cat(Animal):
    def __init__(self, name):
        self.name = name


d = Dog('gimmy')
d.hungry()

c = Cat('Mauuu')
c.hungry()