import unittest

from utils import get_ip_version

class IsIpv4Test(unittest.TestCase):
    def test_should_return_ipv4(self):
        input = "127.0.0.1"

        output = get_ip_version(input)

        self.assertEqual("IPV4", output)

    def test_should_return_ipv6(self):
        input = "::1"

        output = get_ip_version(input)

        self.assertEqual("IPV6", output)

    def test_should_return_none_for_invalid_ipv4(self):
        input = "0.0.0.0.0"

        output = get_ip_version(input)

        self.assertEqual(None, output)

    def test_should_return_none_for_invalid_ipv6(self):
        input = "0:0:0:0:0:0:0:0:0"

        output = get_ip_version(input)

        self.assertEqual(None, output)

    def test_should_raise_error_for_invalid_input(self):
        input = None

        with self.assertRaises(ValueError):
            get_ip_version(input)
