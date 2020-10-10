import unittest

from utils import is_valid_subnet_mask

class IsValidSubnetMaskTest(unittest.TestCase):
    def test_should_return_true_for_int_under_32(self):
        input = "14"

        output = is_valid_subnet_mask(input)

        self.assertEqual(True, output)

    def test_should_return_true_for_valid_ip_notation(self):
        input = "255.255.255.255"

        output = is_valid_subnet_mask(input)

        self.assertEqual(True, output)

    def test_should_return_false_for_int_over_32(self):
        input = "33"

        output = is_valid_subnet_mask(input)

        self.assertEqual(False, output)

    def test_should_return_false_for_invalid_ip_notation(self):
        input = "255.255.255.255.0"

        output = is_valid_subnet_mask(input)

        self.assertEqual(False, output)

    def test_should_raise_error_for_invalid_input(self):
        input = None

        with self.assertRaises(ValueError):
            is_valid_subnet_mask(input)
