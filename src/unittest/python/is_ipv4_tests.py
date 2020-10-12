import unittest

from utils import is_ipv4

class IsIpv4Test(unittest.TestCase):
    def test_should_return_true_for_min_address(self):
        input = "0.0.0.0"

        output = is_ipv4(input)

        self.assertEqual(True, output)

    def test_should_return_true_for_max_address(self):
        input = "255.255.255.255"

        output = is_ipv4(input)

        self.assertEqual(True, output)

    def test_should_return_false_for_5_segments(self):
        input = "0.0.0.0.0"

        output = is_ipv4(input)

        self.assertEqual(False, output)

    def test_should_return_false_for_3_segments(self):
        input = "0.0.0"

        output = is_ipv4(input)

        self.assertEqual(False, output)
