# -*- coding: utf-8 -*-

class Animal(object):

    def run(self):
        print('Animal is running')

class Dog(Animal):

    def run(self):
        print('Dog is running')

    def eat(self):
        print('Dog is eating')

class Cat(Animal):
    def run(self):
        print('Cat is running')

    def eat(self):
        print('Cat is eating')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly')

    def eat(self):
        print('Tortoise is eating')

def run_twice(animal):
    animal.run()
    animal.run()

dog = Dog()
dog.run()
cat = Cat()
cat.run()
cat.eat()

run_twice(Animal())
run_twice(Dog())
run_twice(Tortoise())

a = Animal()
d = Dog()

print(isinstance(a, Animal))
print(isinstance(d, Dog))