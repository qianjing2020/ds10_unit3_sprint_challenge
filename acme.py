"""
See readme.md for interpretation of this script
"""
import sys
from os import getcwd

sys.path.append(getcwd())
import random


class Product:
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


def generate_products(num_products=30):
    adj = ["Awesome", "Shiny", "Impressive", "Portable", "Improved", "Edible"]
    noun = [
        "Anvil",
        "Catapult" "Disguise" "Mousetrap",
        "Cupcake",
        "Flipflops",
        "Kimwipes",
    ]
    products = []
    i = 0
    while i < num_products:
        prod_adj = random.sample(adj, 1)
        prod_noun = random.sample(noun, 1)
        newlist = prod_adj + prod_noun
        name = " ".join(newlist)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        prodname = "class_obj_" + str(i)
        prod_single = Product(
            name=name, price=price, weight=weight, flammability=flammability
        )
        products.append(prod_single)
        i += 1

    return products


def inventory_report(products):
    print("ACME CORPORATION OFFICIAL INVENTORY REPORT")
    # initialize
    unique_list = []
    price = 0
    weight = 0
    flammability = 0
    count = 0
    i = 0
    while i < 30:
        name = products[i].name
        if name not in unique_list:
            unique_list.append(name)
        price += products[i].price
        weight += products[i].weight
        flammability += products[i].flammability
        i += 1
    count = i
    print("Unique product list: ", unique_list)
    average_price = price / count
    average_weight = weight / count
    average_flammability = flammability / count
    print("Average price is", average_price)
    print("Average weight is", average_weight)
    print("Average flammability is", average_flammability)
    print("All products:")


if __name__ == "__main__":
    inventory_report(generate_products())
