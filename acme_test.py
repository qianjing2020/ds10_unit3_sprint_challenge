import unittest
from acme import Product
from acme_report import generate_products


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product', 10, 20, 0.7)
        self.assertEqual(prod.price, 10)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, 0.7)



if __name__ == '__main__':
    unittest.main()





