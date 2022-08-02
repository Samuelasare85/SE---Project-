from PaymentProcessor.pay.order import LineItem
import unittest


class MyTestCase(unittest.TestCase):
    def test_line_item_total(self):
        line_item = LineItem(name="Item", price=100)
        self.assertEqual(line_item.total, 100)

    def test_line_item_total_quantity(self):
        line_item = LineItem(name="Item", price=100, quantity=2)
        self.assertEqual(line_item.total, 200)


if __name__ == '__main__':
    unittest.main()
