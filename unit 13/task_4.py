from __future__ import annotations
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print('Гав!')


class Cat(Animal):
    def speak(self):
        print('Мяу!')


class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError('Неверный тип животного')


factory = AnimalFactory()
dog = factory.create_animal('dog')
dog.speak()

cat = factory.create_animal('cat')
cat.speak()










