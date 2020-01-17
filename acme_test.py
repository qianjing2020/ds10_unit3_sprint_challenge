import random
import acme

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

