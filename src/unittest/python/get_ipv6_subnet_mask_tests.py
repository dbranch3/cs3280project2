import unittest

from utils import get_ipv6_subnet_mask

class GetIpv6SubnetMask(unittest.TestCase):

    def test_should_get_128_bit_subnet(self):
        output = get_ipv6_subnet_mask(128)

        self.assertEqual(output, "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF")

    def test_should_get_64_bit_subnet(self):
        output = get_ipv6_subnet_mask(64)

        self.assertEqual(output, "FFFF:FFFF:FFFF:FFFF:0000:0000:0000:0000")

    def test_should_get_48_bit_subnet(self):
        output = get_ipv6_subnet_mask(48)

        self.assertEqual(output, "FFFF:FFFF:FFFF:0000:0000:0000:0000:0000")

    def test_should_get_32_bit_subnet(self):
        output = get_ipv6_subnet_mask(32)

        self.assertEqual(output, "FFFF:FFFF:0000:0000:0000:0000:0000:0000")

    def test_should_get_16_bit_subnet(self):
        output = get_ipv6_subnet_mask(16)

        self.assertEqual(output, "FFFF:0000:0000:0000:0000:0000:0000:0000")
