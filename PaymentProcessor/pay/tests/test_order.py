from PaymentProcessor.pay.order import *
import unittest


class MyTestCase(unittest.TestCase):
    def test_empty_order_total(self):
        order = Order()
        self.assertEqual(order.total, 0)

    def test_order_total(self):
        order = Order()
        order.line_items.append(LineItem(name="Item", price=100))
        self.assertEqual(order.total, 100)

    def test_order_total_2(self):
        order = Order()
        order.line_items.append(LineItem(name="Item", price=100))
        order.line_items.append(LineItem(name="Item", price=100))
        self.assertEqual(order.total, 200)

    def test_order_pay(self):
        order = Order()
        order.pay()
        self.assertEqual(order.status, OrderStatus.PAID)


if __name__ == '__main__':
    unittest.main()
