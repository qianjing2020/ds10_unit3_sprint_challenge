""" Part 4 Generate products and generate reports"""

import random
from acme import Product

ADJECTIVES = ["Awesome", "Shiny", "Impressive", "Portable", "Improved"]
NOUNS = ["Anvil", "Catapult", "Disguise", "Mousetrap", "???"]


def generate_products(num_products=30):
    products = []  # intialize a list for storing class objects
    i = 0
    while i < num_products:
        name = " ".join(random.sample(ADJECTIVES, 1) + random.sample(NOUNS, 1))
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)
        prod = "x" + str(i)
        prod = Product(name=name, price=price, weight=weight, flammability=flammability)

        products.append(prod)
        i += 1

    return products  # a list of class objects


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
    print("Unique product names: ", len(unique_list))
    average_price = price / count
    average_weight = weight / count
    average_flammability = flammability / count
    print("Average price is", average_price)
    print("Average weight is", average_weight)
    print("Average flammability is", average_flammability)
    print("All products:")


if __name__ == "__main__":
    inventory_report(generate_products())

