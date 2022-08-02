# import pytest
import unittest
from PaymentProcessor.pay.processor import PaymentProcessor

API_KEY = "6cfb67f3-6281-4031-b893-ea85db0dce20"


class MyTestCase(unittest.TestCase):
    def test_invalid_api_key(self):
        with self.assertRaises(ValueError):
            payment_processor = PaymentProcessor("")
            payment_processor.charge("1249190007575069", 12, 2024, 100)

    def test_card_number_valid_date(self):
        payment_processor = PaymentProcessor(API_KEY)
        self.assertTrue(payment_processor.validate_card("1249190007575069", 12, 2024))

    def test_card_number_invalid_date(self):
        payment_processor = PaymentProcessor(API_KEY)
        self.assertFalse(payment_processor.validate_card("1249190007575069", 12, 1900))

    def test_card_number_invalid_luhn(self):
        payment_processor = PaymentProcessor(API_KEY)
        self.assertFalse(payment_processor.luhn_checksum("1249190007575068"))

    def test_card_number_valid_luhn(self):
        payment_processor = PaymentProcessor(API_KEY)
        self.assertTrue(payment_processor.luhn_checksum("1249190007575069"))

    def test_charge_card_valid(self):
        payment_processor = PaymentProcessor(API_KEY)
        payment_processor.charge("1249190007575069", 12, 2024, 100)

    def test_charge_card_invalid(self):
        with self.assertRaises(ValueError):
            payment_processor = PaymentProcessor(API_KEY)
            payment_processor.charge("1249190007575068", 12, 2024, 100)


if __name__ == '__main__':
    unittest.main()