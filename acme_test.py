""" Part 5 """
# python !/user/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product("Test Product")
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        prod = Product("Test Product", 50, 10, 1.5)
        self.assertEqual(prod.stealability(), "Very stealable!")
        self.assertEqual(prod.explode(), "...fizzle")


class AcmeReportTests(unittest.TestCase):
    def test_default_num_products(self):
        products = generate_products(30)
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        products = generate_products(30)
        name_pool = ADJECTIVES+NOUNS
        i = 0
        while i < 30:
            x = products[i].name.split()
            for item in x:
                self.assertIn(item, name_pool)
            i += 1

# class

if __name__ == "__main__":
    unittest.main()

