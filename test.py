#!/usr/bin/env python

class Animal:

    def __init__(self, specie, age, sex):
        self.specie = specie
        self.age = age
        self.sex = sex

    def __str__(self):
        return "I'm a " + str(self.specie) + " and i am " + str(self.age) + " years old."

if __name__ == "__main__":
    print('Hello world!')

    dog = Animal('dog', 16, 'male')
    print dog