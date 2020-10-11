import unittest

from utils import expand_ipv6_address

class ExpandIpv6AddressTest(unittest.TestCase):

    def test_should_fill_zeroes_from_beginning_of_address(self):
        inputIpAddress = "::1"

        output = expand_ipv6_address(inputIpAddress)

        self.assertEqual(output, "0000:0000:0000:0000:0000:0000:0000:0001")

    def test_should_fill_zeroes_in_middle_of_address(self):
        inputIpAddress = "2001:db8::1"

        output = expand_ipv6_address(inputIpAddress)

        self.assertEqual(output, "2001:0db8:0000:0000:0000:0000:0000:0001")

    def test_should_fill_zeroes_at_end_of_address(self):
        inputIpAddress = "2601:cb:0:d9e0::"

        output = expand_ipv6_address(inputIpAddress)

        self.assertEqual(output, "2601:00cb:0000:d9e0:0000:0000:0000:0000")
