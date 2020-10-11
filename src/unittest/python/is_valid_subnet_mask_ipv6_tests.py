import unittest

from utils import is_valid_subnet_mask_ipv6

class IsValidSubnetMaskIpv6Test(unittest.TestCase):
    def test_should_return_true_for_0(self):
        input = "0"

        output = is_valid_subnet_mask_ipv6(input)

        self.assertEqual(True, output)

    def test_should_return_true_for_128(self):
        input = "128"

        output = is_valid_subnet_mask_ipv6(input)

        self.assertEqual(True, output)

    def test_should_return_false_for_under_0(self):
        input = "-1"

        output = is_valid_subnet_mask_ipv6(input)

        self.assertEqual(False, output)

    def test_should_return_false_for_over_128(self):
        input = "129"

        output = is_valid_subnet_mask_ipv6(input)

        self.assertEqual(False, output)

    def test_should_raise_error_for_invalid_input(self):
        input = None

        with self.assertRaises(ValueError):
            is_valid_subnet_mask_ipv6(input)
