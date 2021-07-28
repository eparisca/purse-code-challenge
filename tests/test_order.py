import unittest
import re

import api.order


class OrderNumberTestCase(unittest.TestCase):

    def test_order_number(self):
        """
        Order Number: 232-9384712-9823512
        <3digits>-<7digits>-<7digits>
        """
        input_data = "232-9384712-9823512"
        expected = input_data
        pattern = re.compile(r"^\d{3}-\d{7}-\d{7}$")
        actual = pattern.match(input_data)
        self.assertEqual(expected, actual.group())

    def test_valid_order_number(self):
        input_data = "232-9384712-9823512"
        try:
            api.order.validate_order_number(input_data)
        except ValueError:
            self.fail("validate_order_number() raised ValueError unexpectedly!")

    def test_invalid_order_number(self):
        with self.assertRaises(ValueError) as context:
            input_data = "xxx-xxx-xxx"
            api.order.validate_order_number(input_data)

    def test_create_order_model(self):
        order_number = "232-9384712-9823512"
        date_string = "Dec. 20, 2016 - Dec. 30, 2016"
        order_model = api.order.create_order_model(order_number, date_string)
        expected = order_number
        actual = order_model["order"]
        self.assertEqual(expected, actual)

        expected = "2016-12-30"
        actual = order_model["delivery"]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
