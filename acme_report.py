from acme import Product
import random

""" generate products and generate reports"""
import random

def generate_products(num_products=30):
    adj = ["Awesome", "Shiny", "Impressive", "Portable", "Improved", "Edible"]
    noun = ["Anvil", "Catapult", "Disguise", "Mousetrap", "Cupcake", "Flipflops", "Kimwipes"]
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
        products[i] = Product(
            name=name, price=price, weight=weight, flammability=flammability
        )
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
