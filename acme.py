""" part1:
create a class object to organize Acme Corp products

- `name` (string with no default)
- `price` (integer with default value 10)
- `weight` (integer with default value 20)
- `flammability` (float with default value 0.5)
- `identifier` (integer, automatically genererated as a random (uniform) number
  anywhere from 1000000 to 9999999, includisve)(inclusive).
"""
import sys
from os import getcwd

sys.path.append(getcwd())
import numpy as np


class Product:
    ID = np.random.randint(1000000, 9999999)

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

import random

adj = ["Awesome", "Shiny", "Impressive", "Portable", "Improved", "Edible"]
noun = ["Anvil", "Catapult" "Disguise" "Mousetrap", "Cupcake", "Flipflops", "Kimwipes"]


def generate_products(num_products=30):
    products = []

    for item in range(0, num_products):
        prod_adj = random.sample(adj, 1)
        prod_noun = random.sample(noun, 1)
        newlist = prod_adj + prod_noun

        name = " ".join(newlist)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        products = Product(
            name=name, price=price, weight=weight, flammability=flammability
        )

    return products


products = generate_products(20)