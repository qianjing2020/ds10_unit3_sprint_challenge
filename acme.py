"""
See readme.md for interpretation of this script
"""
import sys
from os import getcwd
sys.path.append(getcwd())


class Product:
    import random
    ID = random.randint(1000000, 9999999)

    def __init__(self, name, identifier=ID, price=10, weight=20, flammability=0.5):
        self.name = name
        self.identifier = identifier
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        x = self.price / self.weight
        if x < 0.5:
            return "Not so stealable..."
        elif (x >= 0.5) and (x < 1.0):
            return "Kinda stealable..."
        else:
            return "Very stealable!"

    def explode(self):
        x = self.flammability * self.weight
        if x < 10:
            return "...fizzle"
        elif (x >= 10) and (x < 50):
            return "...boom!"
        else:
            return "...BABOOM!"


class BoxingGlove(Product):
    def __init__(self, name):
        self.name = name
        Product.__init__(self, name)
        self.weight = 10

    def explode(self):
        return "...it's a glove."

    def punch(self):
        x = self.weight
        if x < 5:
            self.punch = "That tickles."
        elif x >= 5 and x < 15:
            self.punch = "Hey that hurt!"
        else:
            self.punch = "OUCH!"


