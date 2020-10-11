import unittest

from utils import is_ipv6

class IsIpv4Test(unittest.TestCase):
    def test_should_return_true_for_min_address(self):
        input = "0:0:0:0:0:0:0:0"

        output = is_ipv6(input)

        self.assertEqual(True, output)

    def test_should_return_true_for_max_address(self):
        input = "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"

        output = is_ipv6(input)

        self.assertEqual(True, output)

    def test_should_return_true_for_loopback(self):
        input = "::1"

        output = is_ipv6(input)

        self.assertEqual(True, output)

    def test_should_return_false_for_9_segments(self):
        input = "0:0:0:0:0:0:0:0:0"

        output = is_ipv6(input)

        self.assertEqual(False, output)

    def test_should_return_false_for_7_segments(self):
        input = "0:0:0:0:0:0:0"

        output = is_ipv6(input)

        self.assertEqual(False, output)

    def test_should_return_false_for_ipv4(self):
        input = "127.0.0.1"

        output = is_ipv6(input)

        self.assertEqual(False, output)

    def test_should_raise_error_for_invalid_input(self):
        input = None

        with self.assertRaises(ValueError):
            is_ipv6(input)
